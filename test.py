# mock能做什么：
# 1.前后端联调，解放依赖，独立开发。
# 2.单元测试，解决函数或方法依赖关系。
# 3.接口自动化，第三方接口或者接口未完成时。

import requests
from unittest.mock import Mock

def sendUrl():
    # 下面的url为伪接口，访问不通
    url = "http://127.0.0.1/login"
    return requests.get(url=url)

#1.创建Mock对象，名称与调用的函数名一致
sendUrl = Mock(return_value={"code": 0, "msg": "登陆成功"})
response = sendUrl()
print('Mock1:%s\n' % response)

#2.使用Mock模拟引发异常:side_effect-引发异常,AssertionError-异常类型
sendUrl = Mock(side_effect=AssertionError('地址错误'))
response = sendUrl()
print(response)
