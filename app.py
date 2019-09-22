from flask import Flask
from flask import jsonify
from flask import request

from MongoDriver import MongoDriver

app = Flask(__name__)

mongoDriver = MongoDriver("127.0.0.1")


def getDatabaseStatus():
    return True


@app.route('/status')
def status():
    return jsonify({"online": True, "database": getDatabaseStatus()})


@app.route('/sendreport', methods=['POST'])
def send_report():
    requestData = request.get_json()
    product = requestData['product']
    user = requestData['user']
    plugin_version = requestData['plugin_version']
    server_ip = requestData['server_ip']
    server_jar_type = requestData['server_jar_type']
    server_version = requestData['server_version']
    error_message = requestData['error_message']
    steps_to_reproduce = requestData['steps_to_reproduce']
    return mongoDriver.send_report(product, user, plugin_version, server_ip, server_jar_type, server_version,
                                   error_message,
                                   steps_to_reproduce)


if __name__ == '__main__':
    app.run()
