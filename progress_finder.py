import platform
import subprocess
import re

class ProgressFinder:

    def __init__(self):
        self.os = platform.system()

    def get_progress_from_window_title(self):        
        """
        Get the task title of the prime95.exe process by running the Windows cmd 'tasklist' command.
        The resulting task title contains the current exponent and percentage done, which are returned as a tuple if successful.
        Reading from the process title means we don't have to fiddle with prime95.exe's files, and make prime95 output to them more frequently.
        Example return - ("95.67%", "M81893803")
        """
        if self.os != "Windows":
            raise NotImplementedError('Sorry, Windows only for now :(')
        else:
            win_title = ""
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
                if not (len(win_title) > 0):
                    raise ValueError('No processes for prime95.exe found - Check the application is actually running')
                else:
                    match_object_percentage = re.search(r'\d+\.\d+%', win_title)
                    match_object_exponent = re.search(r'M\d+', win_title)
                    if (match_object_percentage and match_object_exponent):
                        return (match_object_percentage.group(), match_object_exponent.group())
                    else:
                        raise IndexError("Unable to parse the progress from the window title - Check the application is not paused, and that the prime95.exe worker window is 'maximised' into the main window")