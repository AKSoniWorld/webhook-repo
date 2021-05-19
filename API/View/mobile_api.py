from API import app
from flask import request, jsonify
from API.model.mobile_util import MobileUtil
from API.model.httpStatus import HTTPStatus


@app.route('/API/mobile/register', methods=['POST'])
def register():
    try:
        payload = request.get_json()
        assert (str(payload) not in ('{}', '[]', " ")), "not a valid payload"
        columns = ['first_name', 'last_name', 'email', 'mobile', 'gender', 'pincode', 'city', 'state']
        for column in columns:
            assert (column in payload.keys()), "{} is required".format(column)

        if MobileUtil().register_user(payload):
            response = jsonify({"status": "success"}), HTTPStatus.OK
        else:
            response = jsonify({"status": "failed"}), HTTPStatus.CONFLICT
    except AssertionError as assert_error:
        response = jsonify({"ERROR": str(assert_error)}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        response = jsonify({"ERROR": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    return response


