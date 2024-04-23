from flask import Flask, request, render_template

app = Flask(__name__, template_folder='')

@app.route('/recruto/', methods=['GET'])
def hello_recruto():
    name = request.args.get('name')
    message = request.args.get('message')
    if name and message:
        greeting = f"Привет {name}! {message}!"
    else:
        greeting = "Привет Recruto! Давай дружить!"
    return render_template('main.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)