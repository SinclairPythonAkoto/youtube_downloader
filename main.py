from flask import Flask
from flaskwebgui import FlaskUI
from pytube import YouTube
from flask import render_template, request, url_for, redirect
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


app = Flask(__name__)

@app.route("/")
def first_page():
    return render_template("landingpage.html")

@app.route("/home")
def home():
    return render_template("homepage.html")

@app.route("/download_video", methods=["GET", "POST"])
def download_vid():
    if request.method == "GET":
        return render_template("downloadVideo.html")
    else:
        link = request.form['youtube_link']
        youtube_object = YouTube(link)
        youtube_object = youtube_object.streams.get_highest_resolution()
        
        try:
            youtube_object.download('static')
        except:
            error = "Something went wrong.  Please check the link and try again."
            return render_template("downloadVideo.html", error=error)

        message = "Your video was downloaded!"
        return render_template("downloadVideo.html", message=message)


@app.route("/view_video")
def view_vid():
    return render_template("viewVideo.html")


if __name__ == "__main__":

    debug = False

    if debug:
        app.run(debug=True)
    else:
        FlaskUI(app, width=500, height=500, start_server="flask").run()
    
   