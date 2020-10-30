# 객체 읽기
import pickle

file=open('save.p','rb')
obj=pickle.load(open('save.p','rb'))
print(obj)
file.close()