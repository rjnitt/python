from flask import Flask, request, render_template, send_file

import subprocess
from pytube import YouTube
import datetime


app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     result = None
#
#     if request.method == "POST":
#         user_input = request.form["user_input"]
#         result = execute_python_code(user_input)
#
#
#     return render_template("index.html", result=result)
#
# def execute_python_code(user_input):
#
#     try:
#         # link = input("Please enter video link for download: ")
#         # link = 'https://www.youtube.com/watch?v=LiODU9n_03Y'
#         print("You entered:", user_input)
#         video_download = YouTube(user_input)
#         # for stream in video_download.streams.all():
#         #     print(stream)
#
#     except Exception as e:
#         print("Connection Error: ", str(e))  # to handle exception
#
#     video_stream = video_download.streams.get_lowest_resolution()
#     output_directory = '/Users/jainrohit/Documents/Python/video'
#
#     # Get the current date and time
#     current_datetime = datetime.datetime.now()
#
#     # Format the datetime as a string in a specific format
#     formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
#
#     # Create a dynamic filename using the formatted datetime
#     dynamic_filename = f"video_{formatted_datetime}"
#
#     try:
#         # downloading the video
#         video_stream.download(filename=dynamic_filename + ".mp4")
#     except Exception as e:
#         print("Some Error while downloading: ", str(e))  # to handle exception
#
#     print('Task Completed!')
#     print('Video Downloaded', user_input)
#     return str("download success!")
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
@app.route('/')
def index():
    return send_file('index.html')

@app.route('/download')
def download():
    video_url = request.args.get('videoUrl')
    if not video_url:
        return "Please provide a valid YouTube video URL."

    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(file_extension='mp4').first()
        stream.download(output_path='downloads', filename='video.mp4')
        return "Video download complete."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
