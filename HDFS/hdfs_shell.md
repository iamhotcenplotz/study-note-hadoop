# HDFS SHELL COMMANDS

- hadoop fs == hdfs dfs
  - upload file
    ```shell
    hadoop fs -mkdir /<folder name>
    
    hadoop fs -moveFromLocal <from> <to> 
    hadoop fs -moveFromLocal /home/hadoop/ods_news_snowball.txt /ods_news
    
    hadoop fs -copyFromLocal <from> <to>
    hadoop fs -copyFromLocal /home/hadoop/ods_news_21jingji.txt /ods_news
    
    hadoop fs -put <from> <to>
    hadoop fs -put /home/hadoop/ods_news_east.txt /ods_news
    
    hadoop fs -appendToFile <from> <to>
    hadoop fs -appendToFile ./fake_news.txt /ods_news/news.txt
    ```
  - download 
    ```shell
    hadoop fs -copyToLocal <from> <to> 
    hadoop fs -copyToLocal /ods_news/ods_news_east /home/hadoop/
    
    hadoop fs -get <from> <to/new name> 
    hadoop fs -get /ods_news/ods_news_east /home/hadoop/east2.txt
    ```
  - operation
    ```shell
    hadoop fs -ls 
    hadoop fs -cat <file name>
    hadoop fs -mkdir
    hadoop fs -cp <from> <to>
    hadoop fs -mv <from> <to>
    hadoop fs -tail
    hadoop fs -rm -r
    hadoop fs -du -h ## file size
    hadoop fs -setrep <file name> ## set replication; max replication size equal to number of server.
    ```
  - balancer
    ```shell
    sbin/start-balancer.sh -threshold 5
    ```