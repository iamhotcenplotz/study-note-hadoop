class HadoopConfig:
    url = 'http://47.113.227.185:14000'
    user = 'hadoop'

# hdfs --daemon stop httpfs
#
# curl -sS 'http://server1:14000/webhdfs/v1?op=gethomedirectory&user.name=hdfs'