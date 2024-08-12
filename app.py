from flask import Flask, render_template_string, request, send_from_directory
# from src.main import main_fn
from src.routes.links import links_blueprint
from src.routes.prompt_analysis import prompt_blueprint

app = Flask(__name__)

app.register_blueprint(links_blueprint, url_prefix='/')
app.register_blueprint(prompt_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, port=3001)
