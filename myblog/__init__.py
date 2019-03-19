import os

from flask import Flask,render_template

from myblog.settings import config
from myblog.extensions import mail,moment,db,bootstrap,ckeditor
from myblog.blueprints.blog import blog_bp
from myblog.blueprints.admin import admin_bp
from myblog.blueprints.auth import auth_bp

def create_app(config_name=None):
	if config_name is None:
		config_name = os.getenv('FLASK_CONFIG', 'development')

	app = Flask(__name__)
	app.config.from_object(config[config_name])

	register_logging(app)
	register_blueprints(app)
	register_extensions(app)
	register_errors(app)
	register_shell_context(app)
	register_template_context(app)
	register_commands(app)
	return app

def register_logging(app):  # 注册日志
	pass


def register_extensions(app):  # 注册扩展
	bootstrap.init_app(app)
	ckeditor.init_app(app)
	mail.init_app(app)
	db.init_app(app)
	moment.init_app(app)


def register_blueprints(app):
	app.register_blueprint(blog_bp)
	app.register_blueprint(admin_bp, url_prefix='/admin')
	app.register_blueprint(auth_bp, url_prefix='/admin')

def register_shell_context(app):
	@app.shell_context_processor
	def make_shell_context():
		return dict(db=db)

def register_template_context(app):
	pass

def register_errors(app):
	@app.errorhandler(400)
	def bad_request(e):
		return render_template('error/404.html') , 400

def register_commands(app):
	pass