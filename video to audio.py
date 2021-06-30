import moviepy.editor


video=moviepy.editor.VideoFileClip("121.mp4")
audio=video.audio
audio.write_audiofile("sample11.mp3")
print("completed")
