
from subprocess import Popen, PIPE
from node import Node

import shlex
import time
import log


TOPIC_WINDOW_CHANGED = "WindowChanged"


class WatchWindows(Node):

    def __init__(self, deploy, username, display):
        super().__init__(deploy)
        self.username = username
        self.display = display
        self.start()

        # log.debug("Username:", username, "Display:", display)

    def run(self):
        self.done = False

        while not self.done:
            try:
                cmd = shlex.split("su %s -c 'xprop -spy -root _NET_ACTIVE_WINDOW -display %s'" % (self.username, self.display))
                proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
                
                while True:
                    line = proc.stdout.readline().decode("utf-8")

                    if line is None or line == "":
                        error_msg = proc.stderr.readlines()
                        log.error("returncode:", str(proc.returncode), "error_mmsg:", error_msg)
                        break

                    idd = line[40:-1]
                    props = self.get_window_props(idd)

                    if "WM_CLASS(STRING)" in props:
                        wm_class = props["WM_CLASS(STRING)"].replace("\"", "").split(", ")
                        log.info("Changed to window:", wm_class[1])
                        self.core.emit(TOPIC_WINDOW_CHANGED, wm_class)
            except Exception as e:
                log.error("Fail during window manager monitoring, retrying in 3s...", e)
            
            time.sleep(3)

    def get_window_props(self, idd):
        if idd is None or idd == "" or idd == "0x0":
            return {}
        
        cmd = shlex.split("su %s -c 'xprop -display %s -id %s'" % (self.username, self.display, idd))
        proc = Popen(cmd, stdout=PIPE)
        props = {}
        
        lines = proc.stdout.readlines()

        for line in lines:
            line = line.decode("utf-8")
            cells = line.split("=", 1)
        
            if len(cells) != 2:
                cells = line.split(":", 1)
        
            if len(cells) != 2:
                continue
        
            key = cells[0].strip()
            value = cells[1].strip()
            props[key] = value
        
        return props


def on_load(deploy, username, display):
    WatchWindows(deploy, username, display)
