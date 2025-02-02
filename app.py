from flask import Flask, render_template, url_for
# from numpy import true_divide
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index1():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
        
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5009, debug=True)


