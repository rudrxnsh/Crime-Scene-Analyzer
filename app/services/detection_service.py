from pathlib import Path 

from detector import detector 
from app.config import OUTPUT_FOLDER 


class DetectionService:
    """
    Handles object detection using YOLO.
    """
        
    def detect_video(self, video_path: str):
        """
        Run YOLO object detection on the give video.
        
        Args:
            video_path (str): Path to the video file
            
        Returns:
            dict
        
        """
        
        results = detector.predict(
            source = video_path,
            save = True,
            project = str(OUTPUT_FOLDER),
            name = "detections",
            exist_ok = True,
            conf = 0.4,
            verbose = False
        )
        
        return {
            "status": "completed",
            "output_folder": str(OUTPUT_FOLDER / "detections"),
            "frames_processed": len(results)
        }