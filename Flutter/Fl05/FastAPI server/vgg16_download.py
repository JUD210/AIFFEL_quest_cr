# 모델 다운받기

#사전학습 모델 불러오기 : 케라스에서 클래스 형태로 제공함
from tensorflow.keras.applications.vgg16 import VGG16

#weight, include_top 파라미터 설정
model = VGG16(weights='imagenet', include_top=True)
model.summary()

#save model
model.save('vgg16.h5')