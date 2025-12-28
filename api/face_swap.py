from flask import Blueprint, request, jsonify
from services.face_service import FaceSwapService

face_swap_bp = Blueprint('face_swap', __name__)
face_service = FaceSwapService()

@face_swap_bp.route('/generate', methods=['POST'])
def generate_image():
    """
    生成换脸图片API
    接收JSON格式的请求：
    {
        "prompt": "提示词",
        "clothesImage": "base64编码的衣物图片",
        "faceImage": "base64编码的人脸图片",
        "model": "模型名称（可选）",
        "size": "图片尺寸（可选）",
        "watermark": false（可选）
    }
    """
    try:
        data = request.get_json()
        
        # 验证必需参数
        if not data:
            return jsonify({'error': '请求体不能为空'}), 400
        
        prompt = data.get('prompt', '')
        clothes_image_base64 = data.get('clothesImage')
        face_image_base64 = data.get('faceImage')
        
        if not clothes_image_base64 or not face_image_base64:
            return jsonify({'error': '缺少必需的图片参数'}), 400
        
        # 获取可选参数
        model = data.get('model', 'doubao-seedream-4-5-251128')
        size = data.get('size', '2K')
        watermark = data.get('watermark', False)
        
        # 调用服务生成图片
        result = face_service.generate_image_with_base64(
            prompt=prompt,
            clothes_image_base64=clothes_image_base64,
            face_image_base64=face_image_base64,
            model=model,
            size=size,
            watermark=watermark
        )
        
        if result is None:
            return jsonify({'error': '图片生成失败，请检查参数和网络连接'}), 500
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({'error': f'服务器错误: {str(e)}'}), 500

@face_swap_bp.route('/health', methods=['GET'])
def health_check():
    """健康检查接口"""
    return jsonify({'status': 'ok', 'message': '服务运行正常'}), 200

