import os
from flask import Flask, render_template, request
import zipfile
import hashlib
import datetime
from werkzeug.utils import secure_filename
import subprocess
import sys
import json

app = Flask(__name__, template_folder = './templates')
app.config['UPLOAD_FOLDER'] = "./uploads"
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 #5MB size_limit files

@app.route("/", methods =["GET","POST"])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        f = request.files["file"]
        filename = f.filename
        
        # check_filename if contains .zip
        if filename[-4:].lower() != ".zip":
            data = {"error": "Only .zip files are accecpted!"}
            return render_template('index.html', data=data)

        new_filename = filename
        # new_filename = secure_filename(filename)
        m = hashlib.sha256()
        m.update(new_filename.encode("utf-8") + str(datetime.datetime.now()).encode("utf-8"))
        new_filename = m.hexdigest()
        new_filepath = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
#        app.new_filepath = new_filepath
        #save file HERE
        f.save(new_filepath + ".zip")
        #-----------------

        os.makedirs(new_filepath, exist_ok=True)        
        try:
            with zipfile.ZipFile(new_filepath + ".zip", 'r') as zip_ref:
                zip_ref.extractall(new_filepath)
        except Exception as e:
            print(e)
            data={"error": "zip is broken, or you are trying to broke me"}
            return render_template('index.html', data=data)

        # ---------------------
        mv = subprocess.run('mv */* .', shell=True, cwd=new_filepath)
        make = subprocess.run('make -f ../../script_test/Makefile re', shell=True, cwd=new_filepath)
        gcc = subprocess.run('gcc -shared -o libft.so *.o', shell=True, cwd=new_filepath)
        #----------------------
        #check for errors in shell operations
        if mv.returncode == 0 and make.returncode == 0 and gcc.returncode == 0:
            data = {"OK": "its all good bruh"}
            data = {"filename": new_filepath}
        else:
            data = {"ERROR": "someting got fu***d"}
            return render_template('index.html', data=data)

    #change working directory to "/script_test"
    sys.path.append('./script_test/.')
    from Moulinette import run_tests
    data ={"OK": run_tests(new_filepath)}
    
   # json output

    return render_template('index.html', data=data)
if __name__== "__main__":
    app.run(host='0.0.0.0')
