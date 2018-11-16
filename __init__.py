from screencapture import screen_record_efficient
from FPS import FPS


frames = FPS().start()
fps_count = screen_record_efficient()

print("MSS:", str(fps_count))
frames.stop()
print('[INFO] elapsed time: {:.2f}'.format(frames.elapsed()))
print('[INFO] approx. FPS: {:.2f}'.format(fps_count / frames.elapsed()))
