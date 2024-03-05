from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

"""
class Postform(FlaskForm):
    '''   
    This is in the "/post/new" and  "/post/edit/<int:post_id>" and "/post/delete/<int:post_id>" routes.
    The forms are title and content
    '''
    title = StringField('title', validators=[DataRequired('title is required')],)  
    content = CKEditorField('content', validators=[DataRequired('content is required')]) # need better phrasing then 'content is required'
    submit = SubmitField('Submit')
"""


from flask_wtf import FlaskForm
from flask_wtf.file import DataRequired
from wtforms import StringField, SubmitField


class SearchForm(FlaskForm):
    '''
    This is in the '/search' route.
    The form is searched.
    '''   
    search_input = StringField("search_input", validators=[DataRequired()])
    submit = SubmitField("Submit")


class EmptyForm(FlaskForm):
    pass