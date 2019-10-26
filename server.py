from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('front_page.html')

if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    
    app.run()