# 자동차 클래스 만들고 사용해보기
class Car:
    def __init__(self,speed,color,model):
        print('자동차 객체를 생성하였습니다.')
        self.speed=speed
        self.color=color
        self.model=model        

    def drive(self):
        print('자동차를 주행합니다.')
        self.speed=60
    
    def __str__(self):
        msg='속도:'+str(self.speed)+' 색상:'+self.color+' 모델:'+self.model
        return msg

myCar=Car(0,'red','e-class')
# print('자동차의 속도는',myCar.speed)
# print('자동차의 색상은',myCar.color)
# print('자동차의 모델은',myCar.model)

# myCar.drive()
# print('자동차의 속도는',myCar.speed)

print(myCar)