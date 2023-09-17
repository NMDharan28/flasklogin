from flask import Flask, render_template,request

app1=Flask (__name__)

@app1.route ('/')
@app1.route ('/home')
def home ():
    return render_template('register.html')


@app1.route ("/confirm", methods=['POST','GET'])
def register():
    if request.method=='POST':
        n=request.form.get('username')
        a=request.form.get('password')
       # c=request.form.get('city')
        return render_template('confirm.html',username=n,password=a)

@app1.route ('/sign')
def sign():
    return render_template ('sign.html')

@app1.route ('/signconfirm', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        k=request.form.get('name')
        e=request.form.get('email')

        return render_template('signconfirm.html',name=k,email=e)

if __name__== "__main__":
    app1.run (debug=True)
