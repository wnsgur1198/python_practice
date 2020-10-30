# 파일에서 한 줄씩 읽기
infile=open("test.txt","r")
for line in infile:
    line=line.rstrip()
    print(line)
infile.close()