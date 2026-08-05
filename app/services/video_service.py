import uuid 
from pathlib import Path 

from werkzeug.utils import secure_filename

from app.config import UPLOAD_FOLDER

class VideoService:
    """
    Handles video storage operations.
    """
    
    @staticmethod
    def save_video(file):
        
        # Generate unique filename
        video_id = str(uuid.uuid4())
        
        extension = Path(file.filename).suffix
        
        filename = secure_filename(f"{video_id}{extension}")
        
        save_path = UPLOAD_FOLDER / filename
        
        file.save(save_path)
        
        return {
            "video_id": video_id,
            "filename": filename,
            "path": str(save_path)
        }