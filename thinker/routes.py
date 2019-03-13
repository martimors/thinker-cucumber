#from thinker.models import ...
from thinker import app

@app.route("/")
def hello():
    return "Hello World!"