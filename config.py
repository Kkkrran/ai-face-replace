"""
配置文件
可以从环境变量或配置文件中读取配置
"""
import os

class Config:
    """应用配置类"""
    # Flask配置
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    # 火山方舟API配置
    ARK_API_KEY = os.getenv('ARK_API_KEY', '0750cb99-ead9-4d2f-b7ba-17f8b89e4549')
    API_URL = os.getenv('API_URL', 'https://ark.cn-beijing.volces.com/api/v3/images/generations')
    
    # 目录配置
    CLOTHES_DIR = os.getenv('CLOTHES_DIR', './clothes')
    FACE_DIR = os.getenv('FACE_DIR', './face')
    
    # 默认模型配置
    DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'doubao-seedream-4-5-251128')
    DEFAULT_SIZE = os.getenv('DEFAULT_SIZE', '2K')
    DEFAULT_WATERMARK = os.getenv('DEFAULT_WATERMARK', 'False').lower() == 'true'

