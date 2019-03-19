import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
load_dotenv(os.path.join(basedir,'.env'))


class BaseConfig(object):
	SECRET_KEY = os.getenv('SECRET_KEY', 'secret strings')

	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = os.getenv('MAIL_SERVER')
	MAIL_PORT = 465
	MAIL_USE_SSL = True
	MAIL_USERNAME = os.getenv('MAIL_USERNAME')
	MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
	MAIL_DEFAULT_SENDER = ('BlueBlog Admin', MAIL_USERNAME)

	BLUEBLOG_EMAIL = os.getenv('BLUEBLOG_EMAIL')
	BLUEBLOG_POST_PER_PAGE = 10
	BLUEBLOG_MANAGE_POST_PER_PAGE = 15
	BLUEBLOG_COMMENT_PER_PAGE = 15


class DevelopmentConfig(BaseConfig):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
	TSETING = True
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(BaseConfig):
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///' + os.path.join(basedir, 'data.db'))


config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
}
