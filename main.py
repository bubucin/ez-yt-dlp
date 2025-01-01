from os import system
_input = 0
while _input == 0:
    vid_or_aud = input('Select "audio" or "video:\n>')
    if vid_or_aud == "audio":
        print("audio")
        _input = 1
        _format = input('Pick an audio format (default is "mp3"):\n("list" for formats)\n>')
        if _format == "":
            _format = "mp3"
        elif _format == "list":
            print("-aac\n-alac\n-aiff\n-flac\n-m4a\n-mp3\n-opus\n-vorbis\n-wav")
            break
        link = input("Paste the link here:\n>")
        if format != "list":
            system(f"yt-dlp -x --audio-format {_format} {link}")
    elif vid_or_aud == "video":
        print("video")
        _input = 1
        _format = input('Pick a video format (default is "mp4"):\n("list" for formats)\n>')
        if _format == "":
            _format = "mp4"
        elif _format == "list":
            print("-avi\n-flv\n-gif\n-mkv\n-mov\n-mp4\n-webm")
            break
        link = input("Paste the link here:\n>")
        if format != "list":
            system(f"yt-dlp --format {_format} {link}")
    else:
        print("Please, pick a valid choice")