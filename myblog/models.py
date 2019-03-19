from myblog.extensions import db
from datetime import datetime

class Admin(db.Modle):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20))
	password_hash = db.Column(db.String(128))
	blog_title = db.Column(db.String(60))
	blog_sub_title = db.Column(db.String(100))
	name = db.Column(db.String(30))
	about = db.Column(db.TEXT)


class Category(db.Modle):   # 文章分类模型
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30),unique=True)
	posts = db.relationship('Post',back_populates='category')


class Post(db.Model):    #发表文章模型
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(60))
	body = db.Column(db.Text)
	timestamp = db.Column(db.DateTime,default=datetime.utcnow,index=True)
	category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
	category = db.relationship('Category', back_populates='posts')
	comments = db.relationship('Comment',backref='post',cascade='all,delete-orphan')

class Comment(db.Model):    #评论模型
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	email = db.Column(db.String(256))
	site = db.Column(db.String(256))
	body = db.Column(db.String(256))
	from_admin = db.Column(db.Boolean,default=False)
	reviewed = db.Column(db.Boolean,default=False)
	timestamp = db.Column(db.DateTime,default=datetime.utcnow,index=True)
	post_id = db.Column(db.Integer,db.ForeignKey('post.id'))
	post = db.relationship('Post',back_populates='comments')

	#邻接列表
	replied_id =db.Column(db.Integer,db.ForeignKey('comment.id'))
	replied = db.relationship('Comment',back_populates='replies',remote_side=[id])
	replies = db.relationship('Comment',back_populates='replied',cascade='all')

