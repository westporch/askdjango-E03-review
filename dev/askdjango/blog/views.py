from django.shortcuts import render

''' from django.shortcuts import render에 대한 설명

render를 import하지 않고 3~4줄로 작성하는 것은 오래된 코드 방식이다.
간단히 from django.shortcuts import render 1줄로 작성한다.
'''

def post_list(request):
	#print(request.META['REMOTE_ADDR']) # 웹으로 django 접속시 remote host의 ip를 runserver 콘솔에 출력한다.
	return render(request, 'blog/post_list.html')
