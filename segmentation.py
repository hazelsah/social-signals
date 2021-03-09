# Part of code taken from PySceneDetect document
# Feature will be implemented in the future in PySceneDetect
# Standard PySceneDetect imports:
from scenedetect import VideoManager
from scenedetect import SceneManager
from scenedetect import video_splitter

# For content-aware scene detection:
from scenedetect.detectors import ContentDetector


def find_scenes(video_path, threshold=30.0):
    # Create our video & scene managers, then add the detector.
    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager.add_detector(
        ContentDetector(threshold=threshold))

    # Improve processing speed by downscaling before processing.
    video_manager.set_downscale_factor()

    # Start the video manager and perform the scene detection.
    video_manager.start()
    time = scene_manager.detect_scenes(frame_source=video_manager)

    # Each returned scene is a tuple of the (start, end) timecode.

    times = scene_manager.get_scene_list(time)

    video_splitter.split_video_ffmpeg(video_path, times,
                                      '$VIDEO_NAME - Scene $SCENE_NUMBER', video_path,
                                      arg_override='-c:v libx264 -preset fast -crf 21 -c:a aac',
                                      hide_progress=False, suppress_output=False)


if __name__ == '__main__':
    video_path = 'video.mp4'
    scenes = find_scenes(video_path)
    print(scenes)
