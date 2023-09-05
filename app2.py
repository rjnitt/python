from flask import Flask
import schedule
import time
from instaloader import *

app = Flask(__name__)
username = 'pragg_chess'
L = Instaloader()

# Define a Python method to be triggered by the cron job

def getFollower():
    profile = Profile.from_username(L.context, username)
    print(profile.followers)
    return f'{profile.followers}'

# Schedule the method to run every hour
schedule.every(2).seconds.do(getFollower)

# Create a route to trigger the cron method manually (optional)
@app.route('/')
def trigger_cron():
    print("Cron method triggered manually")
    return getFollower()


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# This code block is executed when the script is run directly
if __name__ == '__main__':
    import threading

    # Start the Flask app in a separate thread
    flask_thread = threading.Thread(target=app.run)
    flask_thread.start()

    # Run the scheduling loop in the main thread
    run_schedule()
