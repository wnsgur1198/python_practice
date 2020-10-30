# 파일을 읽어 데이터 분리해서 출력하기
infile=open("test.txt","r")
for line in infile:
    line=line.rstrip()
    word_list=line.split()
    for word in word_list:
        print(word)
infile.close()