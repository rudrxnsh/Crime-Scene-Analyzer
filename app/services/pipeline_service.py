from app.services.video_service import VideoService
from app.services.detection_service import DetectionService


class PipelineService:
    """
    Coordinates the complete video processing pipeline.
    """
    
    def process_video(self, file):
        
        # Step 1: Save the uploaded video
        video = VideoService.save_video(file)
        
        # Step 2: Run object detection
        detection = DetectionService().detect_video(video["path"])
        
        return {
            "video": video,
            "detection": detection
        }
        