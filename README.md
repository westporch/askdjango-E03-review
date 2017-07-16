# AskDjango Day3 오프라인 강의 복습

## 강의

날짜: 2017.07.15(토) 13:00 ~ 17:00
장소: [하이브아레나](http://map.naver.com/?mapmode=0&lng=687e734cf6adc46f4546562c1bc789da&pinId=35914663&pinType=site&lat=0bbe8c0b1a44b349990e91640f99d74b&dlevel=11&enc=b64)

## 수업 내용

```
장고 MTV 구조 이해하기 (URLConf, 뷰, 템플릿, 모델) : 장고의 MTV는 타 프레임워크의 MVC와 이름만 다를 뿐 동일합니다. 장고의 철학 “Fat Model, Stupid Template, Thin View” 에 대해 이해해봅시다.

뷰의 이해 : 장고의 뷰는 모두 함수입니다. “클래스 기반 뷰 (Class Based View)”는 함수를 만들어주는 클래스 일 뿐입니다. 함수뷰가 Legacy라는 생각은 버리세요.

django-debug-toolbar : 데이터베이스 의존적인 애플리케이션에서 가장 핵심 병목은 DB입니다. DB병목을 줄일려면 DB쿼리갯수를 줄이거나 DB쿼리성능을 향상시켜야하는 데요. 이를 파악할 수 있도록 도와주는 django-debug-toolbar를 써봅시다.
```
## 테스트 환경

| 항목 | 내용 |
| :--: | :--: |
| Django | v1.11.3 |
| Python | v3.5 |
