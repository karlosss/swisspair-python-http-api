from flask import Flask, request
from pydantic import ValidationError

from dtos import RequestDto, ResponseDto

app = Flask(__name__)

@app.route('/pair', methods=["POST"])
def pair_players():  # put application's code here
    try:
        request_dto = RequestDto.model_validate(request.json)
    except ValidationError as e:
        return str(e), 422

    matches = request_dto.to_swisspair_callable()()

    response_dto = ResponseDto.from_swisspair(matches)

    return response_dto.model_dump_json()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
