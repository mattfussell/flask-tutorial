from flaskBlog import app, db

# This will create the database in a folder called 'instance'; copy pasta as necessary
app.app_context().push()
db.create_all()