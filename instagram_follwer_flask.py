from instaloader import *
from schedule import *
from time import *
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("<h1>hello</h1>", users=users)

if __name__ == '__main__':
    app.run()

L = Instaloader()
username = 'pragg_chess'
def getFollowers():
    print("fetching followers")
    profile = Profile.from_username(L.context, username)
    # num = profile.followers
    print(profile.followers)
    # print(f'Number of followers {num}')


def getProfile():
    profile = Profile.from_username(L.context, username)
    # print(profile.biography)
    # print(profile.full_name)
    # print(profile.profile_pic_url)
    print(profile.followers)

# i = 1
# while i<5:
#     getFollowers()
#     i+=1

# getProfile()

every(5).seconds.do(getFollowers)

while True:
    run_pending()
    sleep(1)


# Get the followers
# followers = [follower.username for follower in profile.get_followers()]

# Print the followers
# print(followers)
