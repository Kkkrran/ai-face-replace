import requests
import base64
import json
import os
from config import Config

class FaceSwapService:
    """AI换脸服务类"""
    
    def __init__(self):
        # 从配置类读取配置
        self.ARK_API_KEY = Config.ARK_API_KEY
        self.API_URL = Config.API_URL
        self.CLOTHES_DIR = Config.CLOTHES_DIR
        self.FACE_DIR = Config.FACE_DIR
    
    def encode_image_to_base64(self, image_path):
        """
        将本地图片编码为Base64字符串
        :param image_path: 本地图片路径
        :return: Base64编码字符串（Data URI格式）
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"图片文件不存在: {image_path}")
        
        # 支持的图片格式
        allowed_formats = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')
        if not image_path.lower().endswith(allowed_formats):
            raise ValueError(f"不支持的图片格式，仅支持: {allowed_formats}")
        
        with open(image_path, "rb") as image_file:
            # 编码为Base64
            base64_encoded = base64.b64encode(image_file.read()).decode("utf-8")
            # 构造Data URI格式
            image_format = image_path.split('.')[-1].lower()
            if image_format == 'jpg':
                image_format = 'jpeg'
            return f"data:image/{image_format};base64,{base64_encoded}"
    
    def base64_to_data_uri(self, base64_string, image_format='jpeg'):
        """
        将纯Base64字符串转换为Data URI格式
        :param base64_string: Base64编码字符串（不含前缀）
        :param image_format: 图片格式
        :return: Data URI格式字符串
        """
        if image_format == 'jpg':
            image_format = 'jpeg'
        return f"data:image/{image_format};base64,{base64_string}"
    
    def generate_image_with_base64(self, prompt, clothes_image_base64, face_image_base64, 
                                   model="doubao-seedream-4-5-251128", size="2K", watermark=False):
        """
        使用Base64编码的图片调用API生成新图片
        :param prompt: 提示词
        :param clothes_image_base64: Base64编码的衣物图片（不含data URI前缀）
        :param face_image_base64: Base64编码的人脸图片（不含data URI前缀）
        :param model: 模型名称
        :param size: 生成图片尺寸
        :param watermark: 是否加水印
        :return: 响应结果（包含生成的图片URL）
        """
        try:
            # 转换为Data URI格式（如果还没有的话）
            if not clothes_image_base64.startswith('data:'):
                clothes_image_base64 = self.base64_to_data_uri(clothes_image_base64)
            if not face_image_base64.startswith('data:'):
                face_image_base64 = self.base64_to_data_uri(face_image_base64)
            
            # 构造请求头
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.ARK_API_KEY}"
            }
            
            # 构造请求体
            payload = {
                "model": model,
                "prompt": prompt,
                "image": [clothes_image_base64, face_image_base64],
                "sequential_image_generation": "disabled",
                "size": size,
                "watermark": watermark
            }
            
            # 发送请求
            response = requests.post(
                self.API_URL,
                headers=headers,
                data=json.dumps(payload),
                timeout=120  # 超时时间设为2分钟
            )
            response.raise_for_status()  # 抛出HTTP错误
            
            # 返回响应结果
            return response.json()
            
        except requests.exceptions.Timeout:
            raise Exception("请求超时，请检查网络或重试")
        except requests.exceptions.RequestException as e:
            error_msg = f"请求失败: {str(e)}"
            if hasattr(e, 'response') and e.response is not None:
                error_msg += f" - 错误响应: {e.response.text}"
            raise Exception(error_msg)
    
    def get_files_from_dir(self, directory):
        """获取目录中所有支持的图片文件"""
        if not os.path.exists(directory):
            os.makedirs(directory)
            return []
        
        allowed_formats = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')
        files = [f for f in os.listdir(directory) 
                 if os.path.isfile(os.path.join(directory, f)) 
                 and f.lower().endswith(allowed_formats)]
        return files

