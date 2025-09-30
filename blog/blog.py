import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "blogging"

connection =sqlite3.connect('blog.db', check_same_thread=False)
cursor =connection.cursor()

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/signin", methods=["GET", "POST"]) 
def signin():
    print(session)
    return render_template("signin.html")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        session.clear()
        username = request.form.get("name")
        password = request.form.get("password")

        #must put input
        if not username or not password:
            flash(f"MUST ENTER ALL INPUTS")
            return render_template("signin.html")

        #check if in data
        cursor.execute("SELECT * FROM users WHERE username=?",(username,))
        name =cursor.fetchall()
        passcheck = check_password_hash(name[0][1],password)
        if len(name) != 1 or not passcheck:
            flash(f"Invalid username or password")
            return render_template("signin.html") 
        
        #home page show
        session["username"] = name[0][0]
        print(session)
        return render_template("home.html",active_page='home')
    return render_template("home.html",active_page='home')

@app.route("/signout")
def signout():
    session.clear()
    return render_template("signin.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":       
        username = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        conpassword = request.form.get("confirm-password")
        
        #must enter all
        if not username or not password or not email or not conpassword:
            flash(f"MUST ENTER ALL INPUTS")
            return render_template("signup.html")

        #user exists
        cursor.execute("SELECT * FROM users WHERE username=?",(username,))
        name =cursor.fetchall()
        if len(name) != 0:
            flash(f"Username already exists")
            return render_template("signup.html")

        #insert into db and pass same
        if password == conpassword:
            newpass = generate_password_hash(password)
            cursor.execute("INSERT INTO users (username,password,email) VALUES(?,?,?)",(username,newpass,email))
            session["username"] = username
            connection.commit() 
            flash(f"Signed up!!!")

            #profile setup
            profpic="https://static.vecteezy.com/system/resources/thumbnails/005/544/718/small_2x/profile-icon-design-free-vector.jpg"
            cover = "https://upload.wikimedia.org/wikipedia/commons/9/9b/No_cover.JPG"
            
            cursor.execute("INSERT INTO info (username,profile_pic,bg_pic) VALUES (?,?,?)", (username,profpic,cover))
            connection.commit()        
            return redirect("/signin")
        else:
            flash(f"Passwords don't match")    
    return render_template("signup.html")

@app.route("/article")
def article():
    cursor.execute("SELECT * FROM posts ORDER BY number DESC")
    newpost = cursor.fetchall()

    post = []
    for i in newpost:
        cursor.execute("SELECT * FROM info WHERE username=?",(i[1],))
        info = cursor.fetchone()

        post.append({
            "username" :i[1],
            "title" : i[2],
            "desc" : i[3],
            "topic" : i[4],
            "pic" : i[5],
            "time" : i[6],
            "info":info
        })

    return render_template("home.html",post=post,active_page='article')

@app.route("/topic")
def topic():
    topic= request.args.get("topic")
    cursor.execute("SELECT * FROM posts WHERE topic=? ORDER BY number DESC",(topic,))
    newpost = cursor.fetchall()
    print(topic,newpost)
    post = []
    for i in newpost:
        cursor.execute("SELECT * FROM info WHERE username=?",(i[1],))
        info = cursor.fetchone()

        post.append({
            "username" :i[1],
            "title" : i[2],
            "desc" : i[3],
            "topic" : i[4],
            "pic" : i[5],
            "time" : i[6],
            "info":info
        })
    return render_template("home.html",post=post,active_page='article')

######sign in need
#newposting
@app.route("/post",  methods=["GET", "POST"])
def post():
    if request.method == "POST":
        title= request.form.get("title")
        desc = request.form.get("desc")
        topic = request.form.get("topic")
        pic = request.form.get("pic")

        cursor.execute("INSERT INTO posts (username,title,desc,topic,pic,time) VALUES(?,?,?,?,?,CURRENT_TIMESTAMP)",(session["username"],title,desc,topic,pic))
        connection.commit()  
        return redirect("/article")
    return render_template("home.html")

###profile categories
@app.route("/profile")
def profile():
    if not session.get("username"):
        return redirect("/signin")
    cursor.execute("SELECT * FROM info WHERE username=?",(session["username"],))
    info = cursor.fetchone()
    
    cursor.execute("SELECT * FROM posts WHERE username=? ORDER BY number DESC",(session["username"],))
    newpost = cursor.fetchall()
    
    post = []
    for i in newpost:
        post.append({
            "username" :i[1],
            "title" : i[2],
            "desc" : i[3],
            "topic" : i[4],
            "pic" : i[5],
            "time" : i[6]
        })
    return render_template("profile.html",post=post,info=info,active_page='profile')

@app.route("/others")
def others():
    if not session.get("username"):
        return redirect("/signin")

    page= request.args.get("page")
    cursor.execute("SELECT * FROM info WHERE username=?",(session["username"],))
    info = cursor.fetchone()
   
    return render_template("profile.html",info=info,active_page=page)

#profile changing
@app.route("/change", methods=["GET", "POST"])
def change():
    if not session.get("username"):
        return redirect("/signin")

    if request.method == "POST":
        cover= request.form.get("cover")
        profpic = request.form.get("profpic")
        description = request.form.get("description")
        contact = request.form.get("contact")
        about = request.form.get("about")
      
        cursor.execute("UPDATE info set profile_pic=?, bg_pic=?, about=?, description=?, Contacts=? WHERE username=?",(profpic,cover,about,description,contact,session["username"]))
        connection.commit()
        return redirect("/profile")
    return render_template("profile.html")

    