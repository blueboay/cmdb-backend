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


class ECS:

    def listServers(self):
        hosts = conn.compute.servers(limit=10)
        result = []
        for s in hosts:
            data = dict()
            data.update({
                # 名称
                "name": s.name,
                # IP地址
                "ip": [ip["addr"] for addrs in s.addresses.values() for ip in addrs],
                # 可用区
                "zone": s.availability_zone,
                # 运行状态
                "status": s.status,
                # 规格
                "flavor": s.flavor["id"]
            })
            result.append(data)
        result = json.dumps({"code": 0, "msg": "", "count": 500, "data": result})
        return HttpResponse(result)


if __name__ == '__main__':
    pass
