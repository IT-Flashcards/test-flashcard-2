import psutil

def kill_processes_by_name(name):
    # Znajdowanie i zamykanie procesów o danej nazwie
    for proc in psutil.process_iter():
        if proc.name().lower() == name.lower():
            proc.kill()

EDGE_PROCESS_NAME = "msedge.exe"
TERMINAL_PROCESS_NAME = "WindowsTerminal.exe"
VSCODE_PROCESS_NAME = "code.exe"

kill_processes_by_name(EDGE_PROCESS_NAME)
kill_processes_by_name(TERMINAL_PROCESS_NAME)
kill_processes_by_name(VSCODE_PROCESS_NAME)

print("Zamknięto Microsoft Edge, Terminal oraz Visual Studio Code.")
