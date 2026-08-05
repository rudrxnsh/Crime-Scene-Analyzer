from flask import Blueprint

from app.core.responses import success_response

health_bp = Blueprint("health", __name__)


@health_bp.route("/health", methods=["GET"])
def health_check():

    return success_response(
        message="Crime Scene Analyzer Backend is running.",
        data={
            "version": "1.0.0"
        }
    )