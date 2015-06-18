from flask import Flask

def run():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'hello world!'

    app.run()

def main():
    #I have a haunting feeling this is not the correct way of doing things
    print 'Starting Main'
    run()

if __name__ == "__main__":
    main()

'''
To be clear, this works with pex. Install this package and run the following:
sudo pex flask spack -o out.pex -e spack:main

'''