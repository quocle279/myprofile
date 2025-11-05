from flask import Flask, render_template

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Định nghĩa Route chính
@app.route('/')
def home():
    """
    Render ra trang chủ portfolio. 
    Flask sẽ tự động tìm file index.html trong thư mục 'templates'.
    """
    return render_template('index.html')

# Đây là cấu hình cơ bản cho môi trường local. 
# Khi deploy lên Vercel, Vercel sẽ tự động sử dụng máy chủ WSGI/ASGI riêng.
if __name__ == '__main__':
    # Chạy ứng dụng trên cổng 5000
    app.run(debug=True)