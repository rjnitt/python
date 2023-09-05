from flask import Flask
from instaloader import *
from schedule import *
from time import *

app = Flask(__name__)
username = 'pragg_chess'
L = Instaloader()

@app.route('/')
def getFollower():
    profile = Profile.from_username(L.context, username)
    print(profile.followers)
    return f'{profile.followers}'

def getFollowerTask():
    response = app.test_client().get('/')
    print(response.get_data(as_text=True))

# @app.route('/')
# def scheduled_task():
#     return "Scheduled task is running..."

every(1).seconds.do(getFollowerTask)

if __name__ == '__main__':
    app.run()




