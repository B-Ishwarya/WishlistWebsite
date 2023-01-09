from flask import Flask,flash,redirect,render_template,url_for,request,jsonify,session
from flask_session import Session
from flask_mysqldb import MySQL
stripe.api_key="sk_test_4eC39HqLyjWDarjtT1zdp7dc"
app=Flask(__name__)

app.secret_key='hello'
app.config['SESSION_TYPE'] = 'filesystem'

app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']='Bisshwarya@05'
app.config['MYSQL_DB']='website'
mysql=MySQL(app)
Session(app)
@app.route('/')
def welcome():
    return render_template('welcome.html')
@app.route('/homepage/<id1>')
def home(id1):
    return render_template('starting.html',id1=id1)

@app.route('/homepage1')
def homepage():
    return render_template('starting.html')

@app.route('/grocery',methods=['GET','POST'])
def grocery():
    return render_template('grocery.html')

@app.route('/fruit',methods=['GET','POST'])
def fruit():
    return render_template('fruits.html')
@app.route('/cart/<name>/<q>/<price>',methods=['GET','POST'])
def cart(name,q,price):
        session['cart'][name]=[q,price]
        session.modify=True
        return render_template('starting.html',id1=session['name'])
@app.route('/cartdisplay')
def view():
    print(session['cart'])
    data=session['cart']
    return render_template('cart.html',data=data)
@app.route('/login',methods=['GET','POST'])
def login():
    if session['name']:
        return redirect(url_for('home',id1=session['name']))
    if request.method=="POST":
        print(request.form)
        user=request.form['user']
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT number from signup')
        users=cursor.fetchall()
        password=request.form['password']
        cursor.execute('select password from signup where number=%s',[user])
        data=cursor.fetchone()
        cursor.close()
        if (int(user),) in users:
            if password==data[0]:
                session['name']=user
                session['cart']={}
                return redirect(url_for('home',id1=user))
            else:
                flash('Invalid Password')
                return render_template('loginpage.html')
        else:
            print('hi')
            flash('Invalid user id')
            return render_template('starting.html')      
    return render_template('loginpage.html')
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
            name=request.form['name']
            number=request.form['number']
            gender=request.form['gender']
            password=request.form['password']
            email=request.form['email']
            cursor=mysql.connection.cursor()
            cursor.execute('insert into signup values(%s,%s,%s,%s,%s)',[name,number,gender,password,email])
            mysql.connection.commit()
            flash('Details registered succesfully')
            return render_template('signuppage.html')
    return render_template('signuppage.html')

#Category Routes
@app.route('/vegetables',methods=['GET','POST'])
def vegetables():
    return render_template('vegetables.html')

@app.route('/spices',methods=['GET','POST'])
def spices():
    return render_template('spices.html')

@app.route('/oils',methods=['GET','POST'])
def oils():
    return render_template('oils.html')

@app.route('/snacks',methods=['GET','POST'])
def snacks():
    return render_template('snacks.html')

@app.route('/drinks',methods=['GET','POST'])
def drinks():
    return render_template('drink.html')

@app.route('/care',methods=['GET','POST'])
def care():
    return render_template('care.html')

@app.route('/milk',methods=['GET','POST'])
def milk():
    return render_template('milk.html')

@app.route('/dal',methods=['GET','POST'])
def dal():
    return render_template('dal.html')

@app.route('/women',methods=['GET','POST'])
def women():
    return render_template('women.html')
    

@app.route('/men',methods=['GET','POST'])
def men():
    return render_template('men.html')

@app.route('/kids',methods=['GET','POST'])
def kids():
    return render_template('kids.html')

@app.route('/house',methods=['GET','POST'])
def house():
    return render_template('home.html')

#Women

@app.route('/ethnicwomen',methods=['GET','POST'])
def ethnicwomen():
    return render_template('ethnic.html')

@app.route('/westernwomen',methods=['GET','POST'])
def westernwomen():
    return render_template('west.html')

@app.route('/watch',methods=['GET','POST'])
def watch():
    return render_template('watch.html')

@app.route('/footwearwomen',methods=['GET','POST'])
def footwearwomen():
    return render_template('foot.html')

@app.route('/jewellery',methods=['GET','POST'])
def jewellery():
    return render_template('jewellery.html')

@app.route('/handbags',methods=['GET','POST'])
def handbags():
    return render_template('handbag.html')

@app.route('/sunglasses',methods=['GET','POST'])
def sunglasses():
    return render_template('sunglasses.html')

@app.route('/cosmetics',methods=['GET','POST'])
def cosmetics():
    return render_template('cos.html')

@app.route('/perfumes',methods=['GET','POST'])
def perfumes():
    return render_template('perfume.html')

@app.route('/ethnicmen',methods=['GET','POST'])
def ethnicmen():
    return render_template('menwestern.html')

#Men

@app.route('/menethnic',methods=['GET','POST'])
def menethnic():
    return render_template('menwestern.html')

@app.route('/westernmen',methods=['GET','POST'])
def westernmen():
    return render_template('mentrendy.html')

@app.route('/footwearmen',methods=['GET','POST'])
def footwearmen():
    return render_template('menfoot.html')

@app.route('/perfumesmen',methods=['GET','POST'])
def perfumesmen():
    return render_template('menperfume.html')

@app.route('/watchsmen',methods=['GET','POST'])
def watchsmen():
    return render_template('menwatch.html')

@app.route('/glassesmen',methods=['GET','POST'])
def glassesmen():
    return render_template('mensunglasses.html')

@app.route('/wallet',methods=['GET','POST'])
def wallet():
    return render_template('menwallet.html')

@app.route('/belts',methods=['GET','POST'])
def belts():
    return render_template('menbelt.html')

@app.route('/mencosmetics',methods=['GET','POST'])
def mencosmetics():
    return render_template('mencosmetic.html')

#Kids

@app.route('/girlsclothing',methods=['GET','POST'])
def girlsclothing():
    return render_template('girls.html')

@app.route('/boysclothing',methods=['GET','POST'])
def boysclothing():
    return render_template('boys.html')

@app.route('/kidsfootwear',methods=['GET','POST'])
def kidsfootwear():
    return render_template('kidsfoot.html')

@app.route('/toys',methods=['GET','POST'])
def toys():
    return render_template('toys.html')

@app.route('/infants',methods=['GET','POST'])
def infants():
    return render_template('infant.html')

@app.route('/kidsaccessories',methods=['GET','POST'])
def kidsaccessories():
    return render_template('acces.html')


#Home needs

@app.route('/lamps',methods=['GET','POST'])
def lamps():
    return render_template('lamp.html')

@app.route('/plants',methods=['GET','POST'])
def plants():
    return render_template('plants.html')

@app.route('/statues',methods=['GET','POST'])
def statues():
    return render_template('statues.html')

@app.route('/carpets',methods=['GET','POST'])
def carpets():
    return render_template('carpet.html')

@app.route('/organisers',methods=['GET','POST'])
def organisers():
    return render_template('organisers.html')

@app.route('/clocks',methods=['GET','POST'])
def clocks():
    return render_template('clock.html')

@app.route('/beddingsets',methods=['GET','POST'])
def bedsheetsets():
    return render_template('bedsheets.html')

@app.route('/doormats',methods=['GET','POST'])
def doormats():
    return render_template('doormat.html')

@app.route('/mirrors',methods=['GET','POST'])
def mirrors():
    return render_template('mirror.html')

     
@app.route('/logout')
def logout():
    session['name']=None
    return redirect(url_for('welcome'))        
app.run(debug=True,port='8000')  
