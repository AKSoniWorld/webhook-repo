from API import app

# db.init_app(app) #uncomment this two line to run in local it is commented for server
# app.run()


# if server doesn't run kill the process who is using the port
# fuser 8000/tcp
# fuser -k 8080/tcp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
