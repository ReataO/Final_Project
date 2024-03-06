

from flask import Flask, render_template, request
from makeup import makeup_info

app = Flask(__name__)
#app.secret_key = 'your_secret_key'


@app.route('/')
def index():

#    information = makeup_info(makeup_data)
    return render_template('index.html')


@app.route('/get_makeup_info', methods=["GET", "POST"])
def get_makeup_info():
    if request.method == 'POST':
        product_type = request.form['product_type']
        tag_list = request.form['tag_list']

        results = makeup.makeup_data(product_type, tag_list=tag_list)
        return render_template('results.html', results=results)

            # In case of an error or no makeup data

    else:
        return "Wrong HTTP method", 400
#        return render_template('index.html', makeup_data=None)

if __name__ == '__main__':
    app.run(debug=True)