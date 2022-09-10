from flask import Blueprint, render_template, request
import website.autoSol.autoSol as c

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/generate')
def generate():
    return render_template("generate.html")

@views.route('/FAQ')
def FAQ():
    return render_template("FAQ.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/signin')
def signin():
    return render_template("signin.html")

@views.route('/download', methods=['GET','POST'])
def download():
    if request.method == 'POST':
        print("post")
    else:
        print("get")
    
    return render_template("download.html")

@views.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    jsdata = request.form['soulMetaData']
    with open('website/autoSol/solMeta.json', 'w') as outfile:
        outfile.write(jsdata)
    contract = c.readJson()
    c.createContract(contract)
    return jsdata


