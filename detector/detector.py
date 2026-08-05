from ultralytics import YOLO

class Detector:
    """
    YOLO Object Detector
    
    Loads the YOLO model only once and resues it for every inference request.
    """
    
    def __init__(self, model_path: str = "yolov8n.pt"):
        self.model = YOLO(model_path)
        
    def predict(self, source, **kwargs):
        """
        Run inference on an image or video.
        
        Args:
        source: image path, video path or webcam
        **kwargs: YOLO inference parameters
        
        Returns: 
            Ultralytics Results object
        
        """
        return self.model.predict(source, **kwargs)
    
    