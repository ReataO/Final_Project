

from flask import Flask, render_template, request
import makeup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=["GET", "POST"])
def results():
  if request.method == 'POST':
    product_type = request.form['makeupType']
    wanted_tag = request.form.get('products')

    data = makeup.get_makeup_data(product_type)

    if wanted_tag:
        makeups = makeup.makeup_info(data, wanted_tag)
    else:
        makeups = makeup.makeup_info(data)
    return render_template('results.html', makeups=makeups)

  else:
    return "Wrong HTTP method", 400

if __name__ == '__main__':
    app.run(debug=True)

##FFF5F3