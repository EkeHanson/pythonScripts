import yt_dlp


def main():
    url = input("Please enter the video URl: ")

    ydl_opts = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Video downloaded Successfully!!!")


if __name__ == "__main__":
    main()
