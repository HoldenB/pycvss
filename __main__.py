import ffmpeg_py.ffmpeg.ffmpeg_bindings as bindings
import ffmpeg_py.tests.test_ffmpeg_benchmark as tests


if __name__ == "__main__":
    bindings.scale_video_args(tests.SAMPLE_VIDEO_1, '1280:720', 'output.mp4')
