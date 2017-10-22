import platform
import subprocess

class ProgressFinder:
    """
    """
    def __init__(self):
        self.os = platform.system()

    def get_progress_from_window_title(self):
        if self.os == "Windows":
            """
            Get the task title of the prime95.exe process by running the Windows cmd 'tasklist' command.
            The resulting task title contains the current exponent and percentage done, which are returned as a tuple if successful.
            Reading from the process title means we don't have to fiddle with prime95.exe's files, and make prime95 output to them more frequently.
            """
            win_title = ""
            # Windows cmd command to get the running task list
            command = 'tasklist /v /fi "IMAGENAME eq prime95.exe" /fo LIST'
            subproc = subprocess.Popen((command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            result = tuple(subproc.stdout)
            error = subproc.returncode
            if error is not None:
                raise IOError('An error occurred executing the tasklist command, the output was: ' + ''.join(result))
            else:
                for line in result:
                    if "Error" in str(line):
                        raise IOError('The script reported the following error: ' + str(line))
                    if "Window Title" in str(line):
                        win_title = str(line)

                if (len(win_title) > 0):  
                    process_title = (win_title.split(" - ", 1)[1])
                    percentage = process_title.split(" of ", 1)[0]
                    exponent = process_title.split(" of ", 1)[1]
                    exponent = exponent.split("\\", 1)[0]
                    return (percentage, exponent)
                else:
                    raise ValueError('No processes for prime95.exe found - Check the application is running')
        else:
            raise NotImplementedError('Sorry, Windows only for now :(')