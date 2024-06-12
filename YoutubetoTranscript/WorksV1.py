import streamlit as st
from pytube import YouTube
import os
import sys
import time
import requests
from zipfile import ZipFile

st.markdown("# 📝 **Transcriber App**")
bar = st.progress(0)


def get_yt(URL):
    video = YouTube(URL)
    yt = video.streams.get_audio_only()
    yt.download()

    bar.progress(10)


def transcribe_yt():
    current_dir = os.getcwd()

    for file in os.listdir(current_dir):
        if file.endswith(".mp4"):
            mp4_file = os.path.join(current_dir, file)

    filename = mp4_file
    bar.progress(20)

    def read_file(filename, chunk_size=5242880):
        with open(filename, "rb") as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    headers = {"authorization": api_key}
    response = requests.post(
        "https://api.assemblyai.com/v2/upload",
        headers=headers,
        data=read_file(filename),
    )
    audio_url = response.json()["upload_url"]

    bar.progress(30)

    endpoint = "https://api.assemblyai.com/v2/transcript"

    json = {"audio_url": audio_url}

    headers = {"authorization": api_key, "content-type": "application/json"}

    transcript_input_response = requests.post(endpoint, json=json, headers=headers)

    bar.progress(40)

    transcript_id = transcript_input_response.json()["id"]

    bar.progress(50)

    endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
    headers = {
        "authorization": api_key,
    }
    transcript_output_response = requests.get(endpoint, headers=headers)

    bar.progress(60)

    from time import sleep

    while transcript_output_response.json()["status"] != "completed":
        sleep(5)
        st.warning("Transcription is processing ...")
        transcript_output_response = requests.get(endpoint, headers=headers)

    bar.progress(100)

    st.header("Output")
    st.success(transcript_output_response.json()["text"])

    yt_txt = open("yt.txt", "w")
    yt_txt.write(transcript_output_response.json()["text"])
    yt_txt.close()

    srt_endpoint = endpoint + "/srt"
    srt_response = requests.get(srt_endpoint, headers=headers)
    with open("yt.srt", "w") as _file:
        _file.write(srt_response.text)

    zip_file = ZipFile("transcription.zip", "w")
    zip_file.write("yt.txt")
    zip_file.write("yt.srt")
    zip_file.close()


api_key = st.secrets["api_key"]


st.warning("Awaiting URL input in the sidebar.")


st.sidebar.header("Input parameter")

with st.sidebar.form(key="my_form"):
    URL = st.text_input("Enter URL of YouTube video:")
    submit_button = st.form_submit_button(label="Go")


if submit_button:
    get_yt(URL)
    transcribe_yt()

    with open("transcription.zip", "rb") as zip_download:
        btn = st.download_button(
            label="Download ZIP",
            data=zip_download,
            file_name="transcription.zip",
            mime="application/zip",
        )
