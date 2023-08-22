import subprocess

class StreamCreate:
    def __init__(self, url, height, width, fps=30):
        super(StreamCreate, self).__init__()
        size = (int(width), int(height))
        sizeStr = str(size[0]) + 'x' + str(size[1])
        command = ['ffmpeg',
                   # '-y',
                   '-an',
                   '-f', 'rawvideo',
                   '-vcodec', 'rawvideo',
                   '-pix_fmt', 'bgr24',
                   '-s', sizeStr,
                   '-r', str(fps),
                   '-i', '-',
                   '-c:v', 'h264',
                   '-pix_fmt', 'yuv420p',
                   '-preset', 'ultrafast',
                   '-f', 'flv',
                   url]
        self.pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
        self.pushing = True
    def push(self, frame):
        if self.pushing:
            self.pipe.stdin.write(frame.tobytes())
    def stop_push(self):
        self.pushing = False
    def start_push(self):
        self.pushing = True
    def __del__(self):
        self.pipe.terminate()
