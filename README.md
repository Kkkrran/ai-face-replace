# AI换脸工具

基于Flask Blueprint和Vue.js的AI换脸Web应用。

## 功能特性

- 🎨 上传衣物图片和人脸图片
- 🤖 使用火山方舟API进行AI换脸
- 💻 现代化的Vue.js前端界面
- 🔧 Flask Blueprint架构，易于扩展
- 📱 响应式设计，支持移动端

## 安装和运行

### 1. 进入虚拟环境

```bash
# Windows
./.venv/Scripts/activate
```

### 2. 配置API密钥

编辑 `config.py` 文件，或设置环境变量：

```bash
# Windows
set ARK_API_KEY=your_api_key_here
```

### 3. 运行应用

```bash
python app.py
```

应用将在 `http://localhost:5000` 启动。

## 项目结构

```
ai-face-replace/
├── app.py                 # Flask应用主文件
├── config.py              # 配置文件
├── requirements.txt       # Python依赖
├── api/                   # API Blueprint
│   ├── __init__.py
│   └── face_swap.py       # 换脸API路由
├── services/              # 服务层
│   ├── __init__.py
│   └── face_service.py   # 换脸服务逻辑
├── templates/             # Flask模板
│   └── index.html        # Vue前端页面
├── static/               # 静态文件（如需要）
├── clothes/              # 衣物图片目录
└── face/                 # 人脸图片目录
```

## API接口

### POST /api/generate

生成换脸图片

**请求体：**
```json
{
    "prompt": "将图1的人脸换为图2的人脸，注意脸的角度",
    "clothesImage": "base64编码的衣物图片（不含data URI前缀）",
    "faceImage": "base64编码的人脸图片（不含data URI前缀）",
    "model": "doubao-seedream-4-5-251128",  // 可选
    "size": "2K",                            // 可选
    "watermark": false                        // 可选
}
```

**响应：**
```json
{
    "data": [
        {
            "url": "生成的图片URL"
        }
    ]
}
```

### GET /api/health

健康检查接口

## 技术栈

- **后端**: Flask, Flask-CORS
- **前端**: Vue.js 3 (CDN)
- **API**: 火山方舟API

## 注意事项

1. 确保已配置有效的火山方舟API密钥
2. 图片格式支持：JPG、PNG、WEBP、BMP
3. 建议图片大小不超过10MB
4. API调用可能需要较长时间，请耐心等待

## 开发说明

### 添加新的API端点

1. 在 `api/` 目录下创建新的Blueprint文件
2. 在 `app.py` 中注册Blueprint

### 修改前端

编辑 `templates/index.html` 中的Vue代码和样式。

## 许可证

MIT License

