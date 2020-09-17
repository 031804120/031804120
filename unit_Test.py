from __future__ import division
from main import Similarity

t11=open(r"C:\Users\hyh\Desktop\sim_0.8\orig.txt",'r',encoding='UTF-8').read()
t12=open(r"C:\Users\hyh\Desktop\sim_0.8\orig_0.8_del.txt",'r',encoding='UTF-8').read()
s13 = Similarity(t11, t12, 10)
s14 = s13.similar()    


t21="春花秋月何时了"
t22="春天到了花儿开了"
topK=10
s23 = Similarity(t21,t22,topK)
s24 = s23.similar()

t31=open(r"C:\Users\hyh\Desktop\sim_0.8\orig.txt",'r',encoding='UTF-8').read()
t32=open(r"C:\Users\hyh\Desktop\sim_0.8\orig_0.8_rep.txt",'r',encoding='UTF-8').read()
s33 = Similarity(t31, t32, 10)
s34 = s33.similar()


t41=open(r"C:\Users\hyh\Desktop\sim_0.8\orig.txt",'r',encoding='UTF-8').read()
t42=open(r"C:\Users\hyh\Desktop\sim_0.8\orig_0.8_mix.txt",'r',encoding='UTF-8').read()
s43 = Similarity(t41, t42, 10)
s44 = s43.similar()

t51=open(r"C:\Users\hyh\Desktop\sim_0.8\orig.txt",'r',encoding='UTF-8').read()
t52=open(r"C:\Users\hyh\Desktop\sim_0.8\orig_0.8_dis_1.txt",'r',encoding='UTF-8').read()
s53 = Similarity(t51, t52, 10)
s54 = s53.similar()

t61=open(r"C:\Users\hyh\Desktop\sim_0.8\orig.txt",'r',encoding='UTF-8').read()
t62=open(r"C:\Users\hyh\Desktop\sim_0.8\orig_0.8_dis_3.txt",'r',encoding='UTF-8').read()
s63 = Similarity(t61, t62, 10)
s64 = s63.similar()


t71=open(r"C:\Users\hyh\Desktop\sim_0.8\orig.txt",'r',encoding='UTF-8').read()
t72=open(r"C:\Users\hyh\Desktop\sim_0.8\orig_0.8_dis_7.txt",'r',encoding='UTF-8').read()
s73 = Similarity(t71, t72, 10)
s74 = s73.similar()

t81="春天来了，春天来了"
t82="春花秋月何时了"
s83 = Similarity(t81, t82, 10)
s84 = s83.similar()

t91="我喜欢看电影，也喜欢看电视剧"
t92="我喜欢看电影，不喜欢看电视剧"
s93 = Similarity(t91, t92, 10)
s94 = s93.similar()

t01="苹果非常的好吃，闻起来也很香"
t02="苹果极其的好吃，闻起来不知道什么味道"
s03 = Similarity(t01, t02, 10)
s04 = s03.similar()
    
print("余弦相似度:%.2f"%s14)
print('\n')
print("余弦相似度:%.2f"%s24)
print('\n')
print("余弦相似度:%.2f"%s34)
print('\n')
print("余弦相似度:%.2f"%s44)
print('\n')
print("余弦相似度:%.2f"%s54)
print('\n')
print("余弦相似度:%.2f"%s64)
print('\n')
print("余弦相似度:%.2f"%s74)
print('\n')
print("余弦相似度:%.2f"%s84)
print('\n')
print("余弦相似度:%.2f"%s94)
print('\n')
print("余弦相似度:%.2f"%s04)
print('\n')

    

