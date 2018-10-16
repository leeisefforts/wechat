from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os
class Application( Flask ):
    def __init__(self,import_name , template_folder = None,root_path = None, static_folder= None):
        super( Application,self ).__init__( import_name ,template_folder = template_folder,root_path = root_path, static_folder = static_folder)

        self.config.from_pyfile('config/local_setting.py')

        db.init_app(self)


db = SQLAlchemy()
app = Application( __name__ ,template_folder = os.getcwd() + "/templates", root_path= os.getcwd(), static_folder=os.getcwd()+"/static")
manager = Manager(app)