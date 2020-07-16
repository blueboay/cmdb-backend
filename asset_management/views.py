from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from openstack import connection
import json

# 创建华为云连接
AK = "5PNEWTSPMO6TZSV4OZD7"
SK = "58ZZmJfpIEhJpfLPZ5Ykd78fO9uiuPe2Hi5OHM7e"
region = "cn-east-2"
projectId = "f2a253f7ba2e4d339e5240a5e67e6e3d"
cloud = "myhuaweicloud.com"
conn = connection.Connection(project_id=projectId,
                             cloud=cloud,
                             region=region,
                             ak=AK,
                             sk=SK,)


def list_servers():
    servers = conn.compute.servers(limit=10)
    for server in servers:
        server_name = server.name
        ipaddress = server.addresses
        flavor = server.flavor
        status = server.status
        print(status)


def hello(request):
    data = {"code": 0,
            "msg": "",
            "count": 256,
            "data": [{"name": "sh2-03-k8s_test-01",
                      "ip": "192.168.81.183",
                      "status": "运行中",
                      "zone": "可用区3",
                      "mode": "按量付费",
                      "kind": "32vCPUs | 64GB | c6.8xlarge.2"
                      }]
            }
    data = json.dumps(data)
    return HttpResponse(data)
