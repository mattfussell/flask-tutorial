from flaskBlog import db
from flask import current_app as app

# This will create the database in a folder called 'instance'; copy pasta as necessary
app.app_context().push()
db.create_all()