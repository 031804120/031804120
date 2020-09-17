from __future__ import division
import jieba.analyse
#用于分词
from math import sqrt
from functools import reduce

import sys
#用于读取命令行参数

'''
file1 = sys.argv[1] #原文文件路径
file2 = sys.argv[2] #对比文件路径
file3 = sys.argv[3] #答案输出文件路径

'''


class Similarity():
    def __init__(self, target1, target2, topK=10):
        self.target1 = target1
        self.target2 = target2
        self.topK = topK
 
    def vector(self):
        self.vdict1 = {}
        self.vdict2 = {}
        #分词
        top_keywords1 = jieba.analyse.extract_tags(self.target1, topK=self.topK, withWeight=True)
        top_keywords2 = jieba.analyse.extract_tags(self.target2, topK=self.topK, withWeight=True)
        for k, v in top_keywords1:
            self.vdict1[k] = v
        for k, v in top_keywords2:
            self.vdict2[k] = v
 
    def mix(self):
        for key in self.vdict1:
            self.vdict2[key] = self.vdict2.get(key, 0)
        for key in self.vdict2:
            self.vdict1[key] = self.vdict1.get(key, 0)
 
        def mapminmax(vdict):
            #计算相对词频
            _min = min(vdict.values())
            _max = max(vdict.values())
            _mid = _max - _min
            #print _min, _max, _mid
            for key in vdict:
                vdict[key] = (vdict[key] - _min)/_mid
            return vdict
 
        self.vdict1 = mapminmax(self.vdict1)
        self.vdict2 = mapminmax(self.vdict2)
 
    def similar(self):
        self.vector()
        self.mix()
        sum = 0
        #余弦夹角和相似度的计算
        for key in self.vdict1:
            sum += self.vdict1[key] * self.vdict2[key]
        A = sqrt(reduce(lambda x,y: x+y, map(lambda x: x*x, self.vdict1.values())))
        B = sqrt(reduce(lambda x,y: x+y, map(lambda x: x*x, self.vdict2.values())))
        return sum/(A*B)#返回相似度
 
if __name__ == '__main__':
    #读取文件
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    file3 = sys.argv[3]
    try:
        t1 = open(file1,'r',encoding='UTF-8').read()
        t2 = open(file2,'r',encoding='UTF-8').read()
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    except IOError as e:
        print(e)
        
    topK = 10
    s3 = Similarity(t1, t2, topK)#调用函数
    c = s3.similar()
    data=open(file3,'w+') 
    print("余弦相似度为：%.2f"%c,file=data)
    data.close() 
    print ("余弦相似度为：%.2f"%c)
    







    
