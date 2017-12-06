'''
@author：KongWeiKun
@file: upload_total.py
@time: 17-12-6 下午9:15
@contact: 836242657@qq.com
'''
import os
from flask import Flask,render_template
from flask_uploads import UploadSet,configure_uploads,IMAGES,patch_request_class
from flask_wtf import FlaskForm
from  flask_wtf.file import FileAllowed,FileField,FileRequired
from wtforms import SubmitField

app=Flask(__name__)
app.config['SECRET_KEY']='Hello World'
app.config['UPLOADED_PHOTOS_DEST']=os.getcwd()

photos=UploadSet('photos',IMAGES)
configure_uploads(app, photos)
patch_request_class(app)



class UploadForm(FlaskForm):
    photo =FileField(validators=[FileAllowed(photos,u'只能上传图片'),
                                 FileRequired(u'文件未选择！')])
    submit=SubmitField(u'上传')

@app.route('/',methods=['GET','POST'])
def upload_file():
    form=UploadForm()
    if form.validate_on_submit():
        filename=photos.save(form.photo.data)
        file_url=photos.url(filename)
    else:
        file_url=None

    return render_template('index.html',form=form,file_url=file_url)

if __name__ == '__main__':
    app.run(debug=True)