import subprocess as process
from config import config as conn 

def amr_player(file_name):
    process.call(["ffplay", "-nodisp", "-autoexit",conn.NEEED_VOICE_PATH + conn.ROOT  +file_name])

def wav_player(file_name):
    process.call(["ffplay", "-nodisp", "-autoexit", file_name])

def amr_to_wav(file_name):
    process.call(["ffmpeg", "-i", file_name + '.amr',"-", "22050",file_name + ".wav"])




