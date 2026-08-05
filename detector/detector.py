from ultralytics import YOLO

from app.config import YOLO_MODEL


class Detector:
    """
    YOLO Object Detector.

    Loads the YOLO model only once and reuses it
    for every inference request.
    """

    def __init__(self):
        self.model = YOLO(YOLO_MODEL)

    def detect_video(self, source, **kwargs):
        """
        Run object detection on a video.

        Args:
            source: Path to the input video.
            **kwargs: Additional YOLO prediction parameters.

        Returns:
            Generator of YOLO Results objects.
        """

        return self.model.predict(
            source=source,
            stream=True,
            **kwargs
        )