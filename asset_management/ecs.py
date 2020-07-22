
from django.http import HttpResponse
from openstack import connection
from django.core.paginator import Paginator
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


def findFlavor(flavor_id):
    flavor = conn.compute.find_flavor(flavor_id)
    return flavor


def listServers(request):
    page_number = request.GET.get("page")
    limit = request.GET.get("limit")
    hosts_generator = conn.compute.servers()
    hosts = list(hosts_generator)
    # 总数
    counts = len(hosts)
    # 分页实例化
    paginator = Paginator(hosts, limit)
    # 指定页数据查询集
    page_data = paginator.page(page_number).object_list
    result = []
    for server in page_data:
        server_data = data = dict()
        flavor = findFlavor(server.flavor["id"])
        vcpus = flavor.vcpus
        ram = flavor.ram // 1024
        data.update({
            # 名称
            "name": server.name,
            # IP地址
            "ip": [ip["addr"] for addrs in server.addresses.values() for ip in addrs],
            # 可用区
            "zone": server.availability_zone,
            # 运行状态
            "status": server.status,
            # 规格
            "flavor": [server.flavor["id"], vcpus, ram]
        })
        result.append(server_data)
    result = json.dumps({"code": 0, "msg": "", "count": counts, "data": result})
    return HttpResponse(result)
