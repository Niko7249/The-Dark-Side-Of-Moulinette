import os
from flask import Flask, render_template, request, jsonify
import zipfile
import hashlib
import datetime
from werkzeug.utils import secure_filename
import subprocess
import sys
import json

ALL_FILES = []

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
        if mv.returncode == 0:
            data = {"OK": "its all good bruh"}
            data = {"filename": new_filepath}
        else:
            data = {"ERROR": "MV got fu***d"}
            return render_template('index.html', data=data)

        make = subprocess.run('make -f ../../script_test/Makefile re', shell=True, cwd=new_filepath)
        if make.returncode == 0:
            data = {"OK": "its all good bruh"}
            data = {"filename": new_filepath}
        else:
            data = {"ERROR": "make got fu***d"}
            return render_template('index.html', data=data)

        gcc = subprocess.run('gcc -shared -o libft.so *.o', shell=True, cwd=new_filepath)
        if gcc.returncode == 0:
            data = {"OK": "its all good bruh"}
            data = {"filename": new_filepath}
        else:
            data = {"ERROR": "gcc got fu***d"}
            return render_template('index.html', data=data)
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
    try:
        from Moulinette import run_tests
        data ={"OK": run_tests(new_filepath)}
        data ={"OK": "test ok"}
    except Exception as e:
        print(e)
        data={"error": "zip is broken, or you are trying to broke me 89"}
        return render_template('index.html', data=data)

    json_path = new_filepath + "/tmp/"
    for filename in os.listdir(json_path):
        if filename.endswith('.json'):
            with open(os.path.join(json_path, filename)) as f:
                data = json.load(f)
                ALL_FILES.append(data)

    #nome variabile json_out
    # parsare tutti i file json e inviare sul frontend
    
   # json output

    return render_template('index.html', data=data)

@app.route('/api/result')
def get_result():
    # if (!ALL_FILES):
    #     return ("NOT YET BRUH")
    return jsonify(ALL_FILES)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
