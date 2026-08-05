from flask import Blueprint, request

from app.core.responses import success_response, error_response
from app.services.pipeline_service import PipelineService

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
    pipeline = PipelineService()

    result = pipeline.process_video(file)

    return success_response(
        message="Video processed successfully.",
        data=result,
        status_code=201
    )