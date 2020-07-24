
from django.http import HttpResponse
from openstack import connection
from django.core.paginator import Paginator
from functools import wraps
import json
import datetime

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
                             sk=SK,
                             verify=True)


def timeTest(fun):
    """用于测试指定函数的执行用时"""
    @wraps(fun)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = fun(*args, **kwargs)
        timedelta = (datetime.datetime.now() - start).total_seconds()
        print("{} execution time is {} seconds.".format(fun.__name__, timedelta))
        return result
    return wrapper


@timeTest  # <==> listServers = timeTest(listServers) <==> listServers = wrapper
def listServers(request):
    """获取所有ECS列表"""
    page_number = request.GET.get("page")
    limit = request.GET.get("limit")
    hosts = list(conn.compute.servers())
    # 获取数据总数
    counts = len(hosts)
    # 将数据进行分页实例化
    paginator = Paginator(hosts, limit)
    # 获取前端指定某一页的数据
    page_data = paginator.page(page_number).object_list
    result = []
    for server in page_data:
        data = dict()
        # flavor = findFlavor(server.flavor["id"])
        # vcpus = flavor.vcpus
        # ram = flavor.ram // 1024
        data.update({
            # 名称
            "name": server.name,
            # IP地址
            "ip": [ip["addr"] for addrs in server.addresses.values() for ip in addrs],
            # 可用区
            "zone": server.availability_zone,
            # 电源状态
            "status": server.power_state,
            # 规格
            "flavor": [server.flavor["id"]]
        })
        result.append(data)
    result = json.dumps({"code": 0, "msg": "", "count": counts, "data": result})
    return HttpResponse(result)


def findServers(request):
    """查询指定ECS信息"""
    pass
