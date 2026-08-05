from flask import Blueprint, request

from app.core.responses import success_response, error_response
from app.services.detection_service import DetectionService
from app.services.video_service import VideoService

upload_bp = Blueprint("upload", __name__)


@upload_bp.route("/upload", methods=["POST"])
def upload_video():

    if "video" not in request.files:
        return error_response(
            message="No video file provided.",
            status_code=400
        )

    file = request.files["video"]

    if file.filename == "":
        return error_response(
            message="No selected file.",
            status_code=400
        )

    # Save uploaded video
    video = VideoService.save_video(file)
    
    
    # Run YOLO detection
    detection = DetectionService().detect_video(
        video["path"]
    )

    return success_response(
        message="Video uploaded and processed successfully.",
        data={
            "video": video,
            "detection": detection
        },
        status_code=201
    )