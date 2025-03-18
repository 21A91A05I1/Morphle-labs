from flask import Flask,render_template
import os
import subprocess
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    username = os.environ.get('USER') or os.environ.get('USERNAME')

    ist = pytz.timezone('Asia/Kolkata')
    now_ist = datetime.datetime.now(ist)

    top_output = subprocess.check_output(['top','-bn1']).decode()

    full_name = "Rayudu Ramya Sri"

    return render_template('index.html',full_name=full_name,username=username,now_ist=now_ist,top_output=top_output)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
