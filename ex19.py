# 파일 복사하기
# infilename=input("입력파일명: ")
# outfilename=input("출력파일명: ")
infilename='test.txt'
outfilename='text-copy.txt'

infile=open(infilename,'r')
outfile=open(outfilename,'w')

s=infile.read()
outfile.write(s)

infile.close()
outfile.close()