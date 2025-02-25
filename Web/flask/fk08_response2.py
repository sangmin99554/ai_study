from flask import Flask
app = Flask(__name__)

from flask import Response, make_response
@app.route("/")
def response_test():
    custom_response = Response("Custom Response", 200, {"Program": "Flask Web Application"})
    return make_response(custom_response)

@app.before_first_request
def before_first_request():
    print("랩이 기동되고 나서 첫번째 HTTP 요청에만 응답합니다")

@app.before_request
def before_request():
    print("매 HTTP 요청이 처리되기 전에 실행됩니다.")

@app.after_request
def after_request(response):
    print("매 HTTP 요청이 처리되고나서 실행됩니다")
    return response

@app.teardown_request
def teardown_request(exception):
    print("매 HTTP요칭의 결과가 브라우저에 응답하고 나서 호출됩니다")

@app.teardown_appcontext
def teardown_appcontext(exception):
    print("HTTP요청의 에플리케이션 컨텍스트가 종료될때 실행됩니다.")

    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)