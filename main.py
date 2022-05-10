from website import create_app

# call function of script __init__.py to create app
app = create_app()

if __name__=='__main__':
    # launch app if main launched
    app.run(debug=True)