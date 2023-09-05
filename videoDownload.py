from pytube import YouTube
import datetime

try:
    link = input("Please enter video link for download: ")
    # link = 'https://www.youtube.com/watch?v=LiODU9n_03Y'
    print("You entered:", link)
    video_download = YouTube(link)
    # for stream in video_download.streams.all():
    #     print(stream)

except:
    print("Connection Error")  # to handle exception

video_stream = video_download.streams.get_lowest_resolution()
output_directory = '/Users/jainrohit/Documents/Python/video'
# video_stream.download(output_path=output_directory)


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
print('Video Downloaded', link)
