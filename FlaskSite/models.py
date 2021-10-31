from datetime import datetime
from FlaskSite import db
from flask_login import UserMixin


class Info(db.Model):
    __tablename__ = "info"
    InfoId  = db.Column(db.Integer , primary_key=True)
    Time    = db.Column(db.DateTime , default = datetime.now())
    TopicId = db.Column(db.Integer , db.ForeignKey("topic.TopicId")  )
    Key = db.Column(db.String(50), nullable = False ,index=True , default = "other")
    Text    = db.relationship( "Text", backref="Info", lazy="joined" )
    Pics    = db.relationship( "Pic", backref="Info", lazy="joined" )
    Links   = db.relationship( "Link", backref="Info", lazy="joined" )
    Voices  = db.relationship( "Voice", backref="Info", lazy="joined" )


class SearchKey(db.Model):
    __tablename__ = "searchkey"
    KeywordId = db.Column(db.Integer , primary_key=True)
    Key = db.Column(db.String(50), nullable = False ,unique= True,index=True , )

class Text(db.Model):
    __tablename__ = "text"
    TextId  = db.Column(db.Integer , primary_key=True)
    Text = db.Column(db.Text , nullable=True)
    TextHead   = db.Column(db.String(200) , nullable = True )
    TextComment   = db.Column(db.String(200) , nullable = True )
    InfoId = db.Column(db.Integer , db.ForeignKey("info.InfoId"))


class Voice(db.Model):
    __tablename__ = "voice"
    VoiceId  = db.Column(db.Integer , primary_key=True)
    VoiceHead   = db.Column(db.String(200) , nullable = True )
    VoiceComment   = db.Column(db.String(200) , nullable = True )
    VoicePath   = db.Column(db.String(500), nullable = True )
    InfoId = db.Column(db.Integer , db.ForeignKey("info.InfoId"))


class Pic(db.Model):
    __tablename__ = "pic"
    PicId  = db.Column(db.Integer , primary_key=True)
    PicHead   = db.Column(db.String(200) , nullable = True )
    PicComment   = db.Column(db.String(200) , nullable = True )
    PicPath   = db.Column(db.String(500), nullable = True )
    InfoId = db.Column(db.Integer , db.ForeignKey("info.InfoId"))

class Link(db.Model):
    __tablename__ = "link"
    LinkId  = db.Column(db.Integer , primary_key=True)
    LinkHead   = db.Column(db.String(200) , nullable = True )
    LinkComment   = db.Column(db.String(200) , nullable = True )
    LinkPath   = db.Column(db.String(500), nullable = True )
    InfoId = db.Column(db.Integer , db.ForeignKey("info.InfoId"))


  
class Topics(db.Model):
    __tablename__ = "topic"
    TopicId  = db.Column(db.Integer , primary_key=True)
    TopicName   = db.Column(db.String(40), index = True , nullable = False )
    Infos = db.relationship("Info", backref="topic")


class User(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(30),unique= True, index=True)
    password = db.Column(db.String(128))
