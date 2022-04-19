from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>ALUNO: MÁRCIO SOARES</h1>\nMBA! o/ \n\n\nV2"

if __name__ == '__main__':
    # application.run()
    application.run(host='0.0.0.0',debug=True)
