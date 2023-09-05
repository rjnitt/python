from flask import Flask, request, render_template
import subprocess
from pytube import YouTube
import datetime


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        user_input = request.form["user_input"]
        result = execute_python_code(user_input)

    return render_template("index.html", result=result)

def execute_python_code(user_input):

    try:
        # link = input("Please enter video link for download: ")
        # link = 'https://www.youtube.com/watch?v=LiODU9n_03Y'
        print("You entered:", user_input)
        video_download = YouTube(user_input)
        # for stream in video_download.streams.all():
        #     print(stream)

    except:
        print("Connection Error")  # to handle exception

    video_stream = video_download.streams.get_lowest_resolution()
    output_directory = '/Users/jainrohit/Documents/Python/video'

    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Format the datetime as a string in a specific format
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

    # Create a dynamic filename using the formatted datetime
    dynamic_filename = f"video_{formatted_datetime}"

    try:
        # downloading the video
        video_stream.download(output_path=output_directory, filename=dynamic_filename + ".mp4")
    except:
        print("Some Error!")

    print('Task Completed!')
    print('Video Downloaded', user_input)
    return str("download success!")


if __name__ == "__main__":
    app.run(debug=True)