import subprocess
import os

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
# print(script_dir)
# print("C:\\Users\\vagrant\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")


def open_vscode_and_run_ng(directory):
    subprocess.Popen(["C:\\Users\\vagrant\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", directory])
    subprocess.Popen(["cmd", "/K", "cd /d " + directory + " && npm install && ng s -o"], creationflags=subprocess.CREATE_NEW_CONSOLE)

open_vscode_and_run_ng(script_dir)