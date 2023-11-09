
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import psutil

app = Flask(__name__)
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

# class ProcessesResource(Resource):
#     def get(self):
#         processes = psutil.process_iter()
#         process_info = []
#         for process in processes:
#             process_info.append({'process_id': process.pid, 'cpu_percent': process.cpu_percent(),
#                                   'memory_info': process.virtual_memory().as_dict(),
#                                   'disk_usage': process.disk_usage().as_dict()})
#         return {'processes': process_info}

# class ThreadsResource(Resource):
#     def get(self):
#         threads = psutil.threads_iter()
#         thread_info = []
#         for thread in threads:
#             thread_info.append({'thread_id': thread.ident, 'cpu_percent': thread.cpu_percent(),
#                                   'priority': thread.priority})
#         return {'threads': thread_info}

# class FileOpenStatsResource(Resource):
#     def get(self):
#         file_stats = psutil.disk_usage('/').as_dict()
#         return {'file_open_stats': file_stats['used'] / 1024 / 1024 / 1024}
    
    
    

api.add_resource(CPUUsageResource, '/cpu')
api.add_resource(MemoryUsageResource, '/memory')
api.add_resource(DiskSpaceResource, '/disk')
#api.add_resource(FileOpenStatsResource,'/files')
#api.add_resource(ThreadsResource,'/threads')
#api.add_resource(ProcessesResource,'/processes')

if __name__ == '__main__':
    app.run()
