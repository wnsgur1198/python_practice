# 리스트를 이용한 오늘의 속담 프로그램
import random

quotes = []
quotes.append("꿈을 지녀라")
quotes.append("분노는 바보들의 가슴 속에서만 살아간다")
quotes.append("고생없이 얻을 수 없는 진실은 없다")
quotes.append("사람은 사랑할 때 시인이 된다")
quotes.append("시작이 반이다")

dailyQuote = random.choice(quotes)
print('##########################')
print('# 오늘의 속담 #')
print('##########################')
print('')
print(dailyQuote)