import subprocess
import os

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
# print(script_dir)
# print("C:\\Users\\vagrant\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")


def open_vscode_and_run_ng(directory):
    subprocess.Popen(["C:\\Users\\vagrant\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", directory])

    command = "cmd /C cd /d " + directory + " && npm install --force --yes --no-optional --no-audit && ng s -o"
    process = subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print("Command executed successfully:\n", stdout.decode())
    else:
        print("An error occurred:\n", stderr.decode())

open_vscode_and_run_ng(script_dir)
