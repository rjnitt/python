from flask import Flask
import schedule
import time

app = Flask(__name__)

# Define a Python method to be triggered by the cron job
def cron_method():
    print("Cron method executed")
    # Add your code here

# Schedule the method to run every hour
schedule.every(2).seconds.do(cron_method)

# Create a route to trigger the cron method manually (optional)
@app.route('/')
def trigger_cron():
    cron_method()
    return "Cron method triggered manually"

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
