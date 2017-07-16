from django.conf.urls import url	# 참고: https://github.com/django/django/blob/1.11.3/django/conf/urls/__init__.py#L77-L85
from . import views

''' 1. r'^$'에서 r에 대한 설명

r은 정규표현식이 아니다.
r은 Raw의 약자이다.

\n --> 1글자
\d --> 2글자(\, d) ==> \\d로 사용해야 한다.

\ 를 적게 사용하는 방법으로 r을 사용하면 된다.

'\\d'는 r'\d'와 같은 표현이다.
r을 써주면 escaping을 해준다.
'''

''' 2. urlpatterns에 대한 설명

urls.py 파일에는 항상 urlpatterns 리스트(순서가 있는 자료구조)가 있어야한다.
정의할 항목이 없다면 빈 리스트라도 만들어야 한다.

리스트는 순서가 있으므로 맨 위에서 부터 matching을 시작한다.
모든 url 정의가 유니크할 필요는 없다.
매칭되는 url이 없다면 404 not found 메시지가 발생한다.
'''


urlpatterns = [
	url(r'^$', views.post_list),	# ^$는 아무것도 없는 정규표현식을 의미함, r은 Raw의 약자이다.
    url(r'^sum/(?P<x>\d+)/$', views.mysum),
]