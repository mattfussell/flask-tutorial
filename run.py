from flaskBlog import create_app
app = create_app()

if __name__ == '__main__': # only runs if this file is called directly
    app.run(debug=True, port=8000, host='0.0.0.0')