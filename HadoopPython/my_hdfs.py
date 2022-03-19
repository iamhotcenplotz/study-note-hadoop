import hdfs
from secret import HadoopConfig

"""
Upload 
    - 方法一： 用SSH远程登录然后使用scp命令
        - 需要配置ssh。不靠谱。。。
    - 方法二：使用httpfs
        - 测试。。。成功！

"""


"""
Example config from hdfs home: https://hdfscli.readthedocs.io/en/latest/quickstart.html
client = InsecureClient('http://host:port', user='ann')
"""

config = {
    'url': HadoopConfig.url,
    'user': HadoopConfig.user
}

client = hdfs.InsecureClient(**config)
print(client.makedirs('/test_api2'))
client.upload(hdfs_path='/test_api2/',local_path='./Hadoop_API.md',n_threads=1)

