from pymongo import MongoClient
import datetime
from flask import jsonify


class MongoDriver:

    def __init__(self, url):
        self.client = MongoClient(url)
        self.db = self.client.issues
        print("Connected to mongodb server!")
        self.client.admin.connections.insert_one({'connected': datetime.datetime.now()})

    def send_report(self, product, user, plugin_version, server_ip, server_jar_type, server_version, error_message,
                    steps_to_reproduce):
        self.db[product].insert_one({'product': product, 'plugin_version': plugin_version, 'server_ip': server_ip,
                                     'server_jar_type': server_jar_type, 'server_version': server_version,
                                     'error_message': error_message, 'steps_to_reproduce': steps_to_reproduce,
                                     'user': user})
        print("Inserted error for {} under the user {}".format(product, user))
        return jsonify({'success': True})
