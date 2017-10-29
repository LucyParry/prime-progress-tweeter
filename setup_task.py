import platform
import subprocess
import subprocess_wrapper
import sys
import os

def create_or_update_task(frequency_string):
    """
    """
    python_interpreter_path = sys.executable
    app_path = sys.path[0]
    if task_exists():
        task_string = 'schtasks /delete /tn "PrimeProgressTweeterTask" /f'
        subprocess_wrapper.run_task_without_stdin(task_string)
    task_string = 'schtasks /create /tn "PrimeProgressTweeterTask" /tr ' + '"' + python_interpreter_path + '" ' + app_path + ' ' + frequency_string
    result, error = subprocess_wrapper.run_task_without_stdin(task_string)


def task_exists():
    """
    """
    command = 'schtasks /query /tn "PrimeProgressTweeterTask"'
    result, error = subprocess_wrapper.run_task_without_stdin(command)
    if len(error) != 0:
        return False
    else:
        return True