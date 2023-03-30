

from flaskBlog import app


if __name__ == '__main__': # only runs if this file is called directly
    app.run(debug=True, port=8000)