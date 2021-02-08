import os
from os import path
from os.path import expanduser
from glob import glob
import subprocess

HOME_DIR = expanduser("~")
WORK_DIR = path.join(HOME_DIR, "Downloads")  # 変換対象のディレクトリ
RESULT_DIR = path.join(HOME_DIR, "Downloads/heictojpg")  # JPEGに変換したファイルを格納するディレクトリ

os.makedirs(RESULT_DIR, exist_ok=True)

files = [path.split(r)[1] for r in glob(path.join(WORK_DIR, "*.HEIC"))]

for f in files:
    inputFile = path.join(WORK_DIR, f)
    outputFile = path.join(RESULT_DIR, f.replace(".HEIC", ".jpg"))

    command = (
        "sips -Z 1024 --setProperty format jpeg " + inputFile + " --out " + outputFile
    )
    print(command)
    subprocess.call(command, shell=True)
