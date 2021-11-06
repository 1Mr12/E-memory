from flask import render_template , url_for ,redirect ,flash, request,g
from werkzeug.utils import secure_filename
from FlaskSite.forms import LoginForm , RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


from FlaskSite import app ,db
from FlaskSite.forms import InfoF,NewTopic
from FlaskSite.models import *


IMG_FOLDER = 'FlaskSite/static/Files/imgs/'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg',"txt",'py'}

app.config['IMG_FOLDER'] = IMG_FOLDER




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def StoreText(info):
    NData = request.form.getlist("Text-TextData")
    NHead = request.form.getlist("Text-Head")
    NComment = request.form.getlist("Text-Comment")


    #ListOfText = []
    for i in range(len(NData)):
        resume = 0

        if NData[i]:
            t = Text(Text=NData[i] , Info = info)
            resume = 1
        if NHead[i] and resume == 1:
            t.TextHead = NHead[i]
        if NComment[i] and resume ==1 :
            t.TextComment = NComment[i]
        if resume:
            db.session.add(t)
    return True

def StoreLink(info):
    NData = request.form.getlist("Link-Url")
    NHead = request.form.getlist("Link-Head")
    NComment = request.form.getlist("Link-Comment")

    #ListOfLink = []
    for i in range(len(NData)):
        resume = 0
        if NData[i]:
            t = Link(LinkPath=NData[i] , Info = info)
            resume = 1
        if NHead[i] and resume == 1:
            t.LinkHead = NHead[i]
        if NComment[i] and resume ==1 :
            t.LinkComment = NComment[i]
        if resume:
            db.session.add(t)
    return True


def StorePic(info,ListOfFiles):
    NHead = request.form.get("Pic-Head")
    NComment = request.form.get("Pic-Comment")
    for i in ListOfFiles:
        if i and  allowed_file(i.filename):
            filename = secure_filename(i.filename)
            filename = info.Key +"-"+ str(datetime.now()) + filename[filename.rfind("."):]
            filename = IMG_FOLDER+filename
            i.save(filename)
            filename=filename.replace("FlaskSite",'')
            t = Pic(PicPath=filename , Info=info)
            if NHead:
                t.PicHead = NHead
            if NComment:
                t.PicComment = NComment
            db.session.add(t)

    return True

def StoreFile():
    pass


def StoreKey(ToStoreKey):
    exist = SearchKey.query.filter_by(Key=ToStoreKey).first()
    if exist:
        return True
    else:
        Key = SearchKey(Key=ToStoreKey)
        db.session.add(Key)
        return True


@app.route('/FirstLook', methods=['GET',"POST"])
def Home():
    return render_template('Home.html')


@app.route('/', methods=['GET',"POST"])
def Infospage():
    form = InfoF()
    TopicsValue = {  x.TopicName : x.TopicId for x in Topics.query.all()}

    if form.validate_on_submit():
        ToStoreKey = request.form.get("Key")
        TID = request.form.get("TopicId" , "other")
        TID = TopicsValue.get(TID , 1)

        #DataBase Operaction
        info = Info(TopicId=TID ,Key=ToStoreKey)
        TextList = StoreText(info)
        LinkList = StoreLink(info)
        Files = request.files.getlist("Pic-Pic")
        PicList = StorePic( info ,Files)
        StoreK = StoreKey(ToStoreKey)
        db.session.add(info)
        db.session.commit()

        return redirect(url_for("Infospage"))
    else:
        print(form.errors)
        print(form.validate_on_submit())
    return render_template('InfoPage.html', form=form , TopicsValue=TopicsValue.keys())



@app.route('/topic', methods=['GET','POST'])
def Topic():
    form = NewTopic()
    TopicsValue = {  x.TopicName : x.TopicId for x in Topics.query.all()}
    if form.validate_on_submit():
        if form.Name.data:
            topic = Topics(TopicName=form.Name.data)
            db.session.add(topic)
            db.session.commit()
            return redirect(url_for("Topic"))
        elif request.form.get("TopicId" , "") :
            TID = request.form.get("TopicId" , "")
            if TID:
                TID = TopicsValue[TID]
                ToDelete = Topics.query.filter_by(TopicId=TID).first()
                db.session.delete(ToDelete)
                db.session.commit()
                return redirect(url_for("Topic"))
        elif request.form.get("SearchTopic",""):
            TID = request.form.get("SearchTopic","")
            if TID:
                TID = TopicsValue[TID]
                SearchKeys = [ i.Key for i in  SearchKey.query.all() ]
                AllInfo = Info.query.filter_by(TopicId=TID).all()
                return render_template("Search.html" , AllInfo =AllInfo ,t=True,SearchKeys="" )
    else:
        print(form.errors)

    return render_template('Topic.html', form=form , TopicsValue=TopicsValue.keys())


@app.route('/Search' , methods=['GET','POST'])
def Search():
    SearchKeys = [ i.Key for i in  SearchKey.query.all() ]
    if request.method == "POST":
        ToSearchKey = request.form.get("SearchKey")
        ToEditId      = request.form.get("InfoId")
        ToEditText    = request.form.get("Text-TextData")
        if ToSearchKey:
            AllInfo = Info.query.filter_by(Key=ToSearchKey).all()
            return render_template("Search.html" , AllInfo =AllInfo ,SearchKeys=SearchKeys )
        elif ToEditId:
            Einfo = Info.query.filter_by(InfoId=ToEditId).first()
            Einfo.Text[0].Text = ToEditText
            db.session.add(Einfo)
            db.session.commit()
            return redirect(url_for("Search"))
    return render_template("Search.html" , AllInfo = "",t=False,SearchKeys=SearchKeys )


@app.route('/New' , methods=['GET','POST'])
def Register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(UserName=form.UserName.data,password=form.Password.data)
        db.session.add(user)
        try:
            print("Hello New User - Moriaty HI")
            db.session.commit()
            return render_template("success.html",title="Welcome",type="success")
        except Exception as e:
            print(e)
            print(form.errors)
            return render_template("success.html",title="Error",type="error")
    else:
        if form.errors:
            flash("Form Error",form.errors)
        else:
            print(form.validate_on_submit())

    return render_template('register.html', title='Register', form=form)


@app.route('/Login', methods=['GET', 'POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        UserName = form.UserName.data
        Pass  = form.Pass.data
        user = User.query.filter_by(UserName=form.UserName.data,password=form.Pass.data).first()
        if user :
            return redirect(url_for("Infospage"))
        else:
            return render_template("success.html",title="Error",type="error")

    return render_template("login.html",title="Login",form=form)



@app.route('/Login', methods=['GET'])
def Message():
    return render_template("success.html",title="Success",type="success")

'''
@app.after_request
def h(r):
    print("After Request Is Running ")
    return r

@app.before_request
def before_req():
    g.target = request.args.get('target', 'default')

'''


@property
def password(self):
    raise AttributeError('password is not a readable attribute')

@password.setter
def password(self, password):
    self.password_hash = generate_password_hash(password)

def verify_password(self, password):
    return check_password_hash(self.password_hash, password)











