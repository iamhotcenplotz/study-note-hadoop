# study-note-hadoop
- [Hadoop Home](https://hadoop.apache.org/)
- Hadoop Version:3.2.2
- JDK Version:8

# Hadoop Setup 
- HDFS(Hadoop Distributed File System)--->[hdfs-site](/config_files/hdfs-site.md)
- YARN(Yet Another Resource Negotiator) ---> [yarn-site](/config_files/yarn-site.md)
- MapReduce--->[mapred-site](/config_files/mapred-site.md)
- [core-site](/config_files/core-site.md)
- [workers](/config_files/workers.md)


# Start Hadoop Cluster
- For first time start cluster need to initiate the cluster
```shell
hdfs namenode -format
```
- Normal step to start cluster 
  - start namenode
  - start resource manager
  - start history server

# Cluster Websites
- HDFS: http://[namenode server]:9870
- YARN: http://[ResourceManager server]:8088

# Python part
- [Hadoop Python](./HadoopPython/Hadoop_API.md)