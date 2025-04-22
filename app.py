from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # ← templates/index.html を表示

# この行は「このファイルが直接実行されたときだけ下の処理を実行してください」という意味です
if __name__ == '__main__':
    # アプリを起動します（http://localhost:5000 でアクセス可能）.
    app.run()