from detector import detector

from app.config import (
    OUTPUT_FOLDER,
    YOLO_CONFIDENCE,
    YOLO_IOU,
)


class DetectionService:
    """
    Handles object detection using YOLO.
    """

    def detect_video(self, video_path: str):
        """
        Run YOLO object detection on the given video.

        Args:
            video_path (str): Path to the uploaded video.

        Returns:
            dict
        """

        results = detector.detect_video(
            source=video_path,
            save=True,
            project=str(OUTPUT_FOLDER),
            name="detections",
            exist_ok=True,
            conf=YOLO_CONFIDENCE,
            iou=YOLO_IOU,
            verbose=False,
        )

        processed_frames = 0
        detection_frequency = {}
        
        for result in results:
            processed_frames += 1
            
            for box in result.boxes:
                
                class_id = int(box.cls)
                class_name = result.names[class_id]
                detection_frequency[class_name] = (
                    detection_frequency.get(class_name, 0) + 1
                    
                )

        return {
            "status": "completed",
            "output_folder": str(OUTPUT_FOLDER / "detections"),
            "frames_processed": processed_frames,
            "detection_frequency": detection_frequency,
        }