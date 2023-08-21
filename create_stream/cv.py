import cv2 as cv
from ffmpeg import StreamCreate
def main():
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter.fourcc(*"avc1"))
    # cv.namedWindow("1", cv.WINDOW_AUTOSIZE)
    if not cap.isOpened(): return
    height, width = cap.get(cv.CAP_PROP_FRAME_HEIGHT), cap.get(cv.CAP_PROP_FRAME_WIDTH)
    try:
        create_stream = StreamCreate(height=height, width=width, fps=45)
        # create_stream2 = StreamCreate(url='rtmp://localhost:1935/live/make2', height=height, width=width, fps=60)
        # 多路推流
        while True:
            flag, img = cap.read()
            if not flag: break
            img = cv.flip(img, 1)
            cv.circle(img, (200, 200), 5, (255, 255, 0), -1)
            create_stream.push(img)
            # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            # create_stream2.push(img)  # 多路推流
            cv.waitKey(1)
    finally:
        cap.release()
        cv.destroyAllWindows()
if __name__ == '__main__':
    main()
