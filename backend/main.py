from init.app import init_app


app = init_app()


if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG'), host='0.0.0.0', port=8080)
