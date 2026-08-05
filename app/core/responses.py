from flask import jsonify


def success_response(
    message= "Success",
    data=None,
    status_code=200
):
    """
    Standardized Success Response
    """
    response = {
        "success": True,
        "message": message,
        "data": data
    }
    
    return jsonify(response), status_code

def error_response(
    message = "Something went wrong",
    errors = None,
    status_code = 400
):
    """
    Standardized Error Response
    """
    response = {
        "success": False,
        "message": message,
        "errors": errors if errors is not None else {}
        
    }
    
    return jsonify(response), status_code
    
