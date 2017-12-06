'''
@author：KongWeiKun
@file: upload.py
@time: 17-12-6 下午4:33
@contact: 836242657@qq.com
'''
import os
from flask import Flask,request,url_for,send_from_directory
# from flask_uploads import UploadSet,configure_uploads,IMAGES,patch_request_class
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/kongweikun/PycharmProjects/flask_uplaod/picture'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app=Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.getcwd() #返回当前工作目录
app.config['MAX_CONTENT_LENGTH']=16*1024*1024
# photos=UploadSet('photos',IMAGES)
# configure_uploads(app, photos)
# patch_request_class(app) # set maximum file size, default is 16MB



html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>Photo Upload</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=photo>
         <input type=submit value=Upload>
    </form>
    '''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS #以最右边的点分割开 得到文件后缀名 并判断是否符合要求

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/',methods=['POST','GET'])
def upload_file():
    if request.method=='POST' and 'photo' in request.files:
        file=request.files['file']
        if file and allowed_file(file.filename): #判断文件是否符合上传要求
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            file_url=url_for('uploaded_file',filename=filename)
        # filename=photos.save(request.files['photo'])
        # file_url=photos.url(filename)
            return html+'<br><img src='+file_url+'>'
    return html




if __name__ == '__main__':
    app.run(port=9006,debug=True)

    # s=allowed_file('fssf.jpg')
    # print(s)