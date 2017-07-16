from django.http import HttpResponse
from django.shortcuts import render

''' from django.shortcuts import render에 대한 설명

render를 import하지 않고 3~4줄로 작성하는 것은 오래된 코드 방식이다.
간단히 from django.shortcuts import render 1줄로 작성한다.
'''

def post_list(request):
	#print(request.META['REMOTE_ADDR']) # 웹으로 django 접속시 remote host의 ip를 runserver 콘솔에 출력한다.
	return render(request, 'blog/post_list.html')

def mysum(request, x):
	''' 인자: 정수 1개
    리턴값: URL에 입력한 값(정수 1개)을 리턴하여 웹페이지에 출력한다.
	사용법(예): 웹브라우저의 주소 창에 아래 주소를 입력한다. (999가 출력된다.)
				http://192.168.0.17:8080/blog/sum/999/
	'''
	return HttpResponse(int(x))

def mysum(request, x, y):
	''' 인자: 정수 2개
    리턴값: URL에 입력한 값(정수 2개)을 더한 뒤 리턴하여 웹페이지에 출력한다.
	사용법(예): 웹브라우저의 주소 창에 아래 주소를 입력한다. (1000이 출력된다.)
				http://192.168.0.17:8080/blog/sum/999/1
	'''
	return HttpResponse(int(x) + int(y))

def mysum(request, x, y, z):
	''' 인자: 정수 3개
    리턴값: URL에 입력한 값(정수 3개)을 더한 뒤 리턴하여 웹페이지에 출력한다.
	사용법(예): 웹브라우저의 주소 창에 아래 주소를 입력한다. (1004가 출력된다.)
				http://192.168.0.17:8080/blog/sum/999/1/4
	'''
	return HttpResponse(int(x) + int(y) + int(z))

