from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])

def hesapla():
    bmi=""
    if request.method=="POST" and "weight" in request.form and "height" in request.form:
        weight=float(request.form.get("weight"))
        height=float(request.form.get("height"))
        bmi=round(weight/((height/100)**2),2)
    return render_template("index.html",bmi=bmi)

""" 
if __name__ == '__main__': 
    app.run(debug = True) """

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
