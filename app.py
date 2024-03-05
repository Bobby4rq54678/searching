from flask import Flask, flash, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['CKEDITOR_PKG_TYPE'] = 'standard'
app.config['SECRET_KEY'] = 'secret key'

db = SQLAlchemy(app)
ckeditor = CKEditor(app) 


from flask import flash
from flask_login import UserMixin



from forms import SearchForm 


class Posts(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String(120), nullable=False)


    def __repr__(self):
        return f"Posts('{self.title}')"




@app.context_processor
def inject_searchform():
    '''
        Pass Stuff to Navbar such as a form in layout.html from search.html        
        If I don't pass on the form in base function then I will 
        get an error in layout.html because of {{form.csrf_token}} 
    ''' 
    # The variable name is "searchform" and not "form" because in the html I would have 2 "form" variables
    return dict(form=SearchForm()) 






@app.route('/', methods= ['GET', 'POST'])
@app.route('/home', methods= ['GET','POST'])
def home():  
 
    
    # generate unique id to make each title and content unique 
    import uuid
    uniqueid = uuid.uuid1()
    title_form = 'This is the title.' + str(uniqueid)
    content_form = 'This is the content' + str(uniqueid)
    post_db_info = Posts(title=title_form, content=content_form)
    db.session.add(post_db_info)
    db.session.commit()
    
    posts = db.session.scalars(db.select(Posts)).all()
    return render_template('home.html', posts=posts)

 

@app.route('/search', methods= ['GET', 'POST'])
def search():  
    # The variable name is "searchform" and not "form" because in the html I would have 2 "form" variables
    searchform = SearchForm()    
    if searchform.validate_on_submit():

        search_input = searchform.search_input.data
       
        search_results = db.session.query(Posts).filter(Posts.content.ilike(f'%{search_input}%')).all()
        flash(search_results)
        for search_result in search_results:
            flash(search_result)

        return render_template('search.html', searchform=searchform, search_results=search_results)
   
    flash('something has gone wrong')


if __name__ == '__main__':
    app.run(debug=True)
