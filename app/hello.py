from flask import Flask,render_template,request,url_for
import requests
app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def hello():
    if request.method=='POST':
        preg=request.form['a']
        glc=request.form['b']
        bp=request.form['c']
        skt=request.form['d']
        ins=request.form['e']
        bmi=request.form['f']
        dpf=request.form['g']
        age=request.form['h']
        try:
            preg=int(preg)
            glc=int(glc)
            bp=int(bp)
            skt=int(skt)
            ins=int(ins)
            bmi=float(bmi)
            dpf=float(dpf)
            age=float(age)
        except:
            return render_template('data.html',err_msg='Enter Valid Data')
        url = "https://9cooc0m619.execute-api.us-east-1.amazonaws.com/diabetis/"
        payload = " {\"data\":\"" + str(preg) + ',' + str(glc) + ',' + str(bp) + ',' + str(skt) + ',' + str(ins) + ',' + str(bmi) + ',' + str(dpf) + ',' + str(age) + "\"" + "}"
        print(payload)
        headers = {
            'X-Amz-Content-Sha256': 'beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3',
            'X-Amz-Date': '20200930T095337Z',
            'Authorization': 'AWS4-HMAC-SHA256 Credential=ASIA4KDESJFDUSSQKJSG/20200930/us-east-1/execute-api/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=b81935cc533d5efb8db465da9c12f4a3ed76ca80089dfc3edebdb39df4fe5f7c',
            'Content-Type': 'text/plain'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response=response.text.encode('utf8')
        response=str(response)
        print(response)
        result=response[3]
        print(result)
        if result=='N':
            return render_template('data.html',result=str(0))
        else:
            return render_template('data.html',result=str(1))
    else:
        return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)
