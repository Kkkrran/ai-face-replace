from flask import Flask
from flask_cors import CORS
from api.face_swap import face_swap_bp

def create_app():
    """创建并配置Flask应用"""
    app = Flask(__name__)
    
    # 启用CORS支持
    CORS(app)
    
    # 注册Blueprint
    app.register_blueprint(face_swap_bp, url_prefix='/api')
    
    @app.route('/')
    def index():
        """主页面"""
        from flask import render_template
        return render_template('index.html')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)

