import platform
import subprocess
import sys
import os

def run_task_without_stdin(command):
    """

    """
    if platform.system() == "Windows":
        subproc = subprocess.Popen((command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = tuple(subproc.stdout)
        error = tuple(subproc.stderr)
        return result, error
    else:
        raise NotImplementedError('Sorry, Windows only for now :(')
