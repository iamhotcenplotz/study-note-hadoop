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
"""
sample config
config = {
    'url':'http://host:14000', # must be NameNode host
    'user':'user'
}
"""

client = hdfs.InsecureClient(**config)
# Make folder
client.makedirs('/test_api2')

# upload file
client.upload(hdfs_path='/test_api2/', local_path='./Hadoop_API.md', n_threads=1)

# download file
client.download(hdfs_path='/ods_news/ods_news_east.txt', local_path='./', n_threads=3)

# check hdfs folders
client.list(hdfs_path='/')

# Delete
client.delete(hdfs_path='/test_api2', recursive=True)

