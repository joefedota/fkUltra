from flask import Flask
from flask_login import LoginManager
from app.config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.ledger_manager import Ledger
import json

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#open the ledger
f = open("ledger.json")

if not len(f.readlines()):
    ledger = Ledger({}, 0)
else:
    f.close()
    f = open("ledger.json")
    data = json.load(f)["data"]
    ledger = Ledger(data["dids"], data["count"])
f.close()

from app import routes
