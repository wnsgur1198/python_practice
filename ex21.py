# 객체 쓰기
import pickle

gameOption={
    'Sound':8,
    'VideoQuality':'HIGH',
    'Money':100000,
    'WeaponList':['gun','missile','knife']
}

# 이진파일 오픈
file=open('save.p','wb')

# 딕셔너리를 피클파일에 저장
pickle.dump(gameOption,file)

file.close()