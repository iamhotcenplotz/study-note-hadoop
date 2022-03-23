import jieba
from mrjob.job import MRJob


class JiebaMapReduce(MRJob):

    def mapper(self, _, data):
        line = jieba.lcut(data)
        for word in line:
            yield word, 1

    def reducer(self, key, value):
        yield key, sum(value)


if __name__ == '__main__':
    JiebaMapReduce.run()


"""
run mapreduce program using one of following commands:
    - inline:python my_mapreduce.py ./ods_news_east.txt
    - local: python my_mapreduce.py -r local ./ods_news_east.txt ./tmp
    - hadoop cluster: python my_mapreduce.py -r hadoop hdfs:///ods_news/ods_news_east.txt  --output hdfs:///temp_result
"""
