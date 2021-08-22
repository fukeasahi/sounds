# step0　動画をダウンロードして/Users/asahi/Desktop/works/{}/movie/におく
# step1　/Users/asahi/Desktop/works/{}/movie/にある動画をwavに変換する。
import glob
from natsort import natsorted
import os
import subprocess

title = "skills"
url = "/Users/asahi/Documents/python-practice/sounds"

mp4_files = natsorted(glob.glob(url + "/{}/movie/*".format(title)))
print(mp4_files)
for i, mp4_file in enumerate(mp4_files):
    os.rename(mp4_file, url + "/{}/movie/{}{}.mp4".format(title,title,str(i+1)))

movies = natsorted(glob.glob(url + "/{}/movie/*".format(title)))
print(movies)
for movie in movies:
    file_name_without_ext = os.path.basename(movie).split(".")[0]
    print(file_name_without_ext)
    output_movie = movie.replace(".mp4",".wav").replace("movie/","voice/")
    print(output_movie)
    cmd = 'ffmpeg -i ' + movie + ' ' + "-y " + output_movie
    print(cmd)
    subprocess.call(cmd,shell=True)

    # step2　wavからテキストデータに変換する
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.AudioFile(output_movie) as source:
        audio = r.record(source)
        text = r.recognize_google(audio,language="ja")
        print(text,"取得完了")

        # step3　テキストデータを修正
        # step4　テキストデータをワードに出力
        from docx import Document
        word_write_file_name = file_name_without_ext + ".docx"
        document = Document()
        document.add_paragraph(text)
        document.save(word_write_file_name)
        print("ワードに出力完了")
