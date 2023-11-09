
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

import psutil
app = Flask(__name__)
CORS(app)
api = Api(app)

class CPUUsageResource(Resource):
    def get(self):
        cpu_percent = psutil.cpu_percent()
        return {'cpu_usage': cpu_percent}

class MemoryUsageResource(Resource):
    def get(self):
        memory_info = psutil.virtual_memory()
        mem_percent = memory_info.percent
        return {'memory_usage': mem_percent}

class DiskSpaceResource(Resource):
    def get(self):
        disk_info = psutil.disk_usage('/')
        total = disk_info.total
        used = disk_info.used
        free = disk_info.free
        return {'disk_space': {'total': total, 'used': used, 'free': free}}
    
api.add_resource(CPUUsageResource, '/cpu')
api.add_resource(MemoryUsageResource, '/memory')
api.add_resource(DiskSpaceResource, '/disk')


if __name__ == '__main__':

    app.run()