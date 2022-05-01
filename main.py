from flask import Flask, render_template, request, session

users={}

app= Flask(__name__)

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/signup")

def signup():
    return render_template("signup.html")

@app.route("/signedup",methods=["POST"])

def content():
    username=request.form.get("username")
    first_name=request.form.get("first_name")
    last_name=request.form.get("last_name")
    password=request.form.get("password")
    email=request.form.get("email")
    age=request.form.get("age")
    country=request.form.get("country")
    city=request.form.get("city")
    
    if not username in users:
        users[username]={"first_name":first_name,
                        "last_name":last_name,
                        "password":password,
                        "email":email,
                        "age":age,
                        "country":country,
                        "city":city 
                        
                        
                        }
        print(users)

    elif username in users:
        return render_template("signup.html",error=True)
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/authenticator",methods=["POST"])

def authenicate():
    if request.method =="POST":
        username=request.form.get("username")
        password=request.form.get("password")    
        if username in users:
            if users[username]["password"]==password:
                return render_template("success.html",first_name=users[username]["first_name"],
                                       last_name=users[username]["last_name"],
                                       city=users[username]["city"],
                                       age=users[username]["age"],
                                       country=users[username]["country"]
                                       )
            else:
                return render_template("login.html",errors=True)
        else:
            return render_template("login.html",error=True)
        
    
app.run(debug=True,port=8085)