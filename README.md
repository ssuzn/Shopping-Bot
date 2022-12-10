# 쇼핑봇 :robot:
## Intro :tophat:
Discord API를 이용한 쇼핑을 도와주는 BOT 개발

사용자가 입력한 명령에 따라 온라인 의류 편집샵인 무신사에서 크롤링하여 의류 추천

## Description :shirt:
* ! (느낌표)를 접두사로 명령어 인식


* 봇이 서버에 입장

![bot_entry](https://user-images.githubusercontent.com/107746547/206863164-8e4354a1-6b36-44f3-bdd0-d5bbd26f0104.PNG)


* 디스코드 서버에 새로운 사용자 입장

![member_join](https://user-images.githubusercontent.com/107746547/206863087-bc6bb3f1-9386-4c2b-b528-f0597304ecb6.PNG)


* 사용자가 서버에서 퇴장
 
![member_out](https://user-images.githubusercontent.com/107746547/206863848-58ef70b0-8efc-46ec-9410-3869b40c8c6f.PNG)


* `!도움말` 입력
 
![help](https://user-images.githubusercontent.com/107746547/206863214-f78ccd6d-38f4-43a9-906d-e83d7e9d9d51.PNG)


* `!쇼핑` 입력
 
![help_shop](https://user-images.githubusercontent.com/107746547/206863226-1efb20a8-02d7-40f2-8106-798000b9fd97.PNG)


* `!쇼핑 스니커즈` 입력
 
![shop](https://user-images.githubusercontent.com/107746547/206864295-999c46a2-b453-4570-9dc8-473982c99ad2.PNG)


* !쇼핑 명령어에 대한 잘못된 카테고리 입력
 
![error_shop](https://user-images.githubusercontent.com/107746547/206863394-37c3f689-e4f2-4a56-9d9e-71e1fe7ac217.PNG)


* `!색상` 입력
 
![help_color](https://user-images.githubusercontent.com/107746547/206863409-83692c9c-e4d7-4b61-ac56-dd3147479728.PNG)


* `!색상 상의 green` 입력
 
![colo](https://user-images.githubusercontent.com/107746547/206864299-09c20e28-b289-4229-b53c-e51f4545d2b2.PNG)


* !색상 명령어에 대한 잘못된 입력
 
  * 카테고리 잘못 입력
   
  ![category_err](https://user-images.githubusercontent.com/107746547/206863484-25b92e80-e875-4c62-b7ed-4aa1758c2b44.PNG)
  
  * 색상 잘못 입력
   
  ![color_err](https://user-images.githubusercontent.com/107746547/206863490-c396310b-98cc-4840-b710-96ed639bdc77.PNG)
  
  * 카테고리, 색상 잘못 입력
   
  ![2err](https://user-images.githubusercontent.com/107746547/206863495-1882ab82-f2f3-4048-9a87-48e7dc2e1833.PNG)
  
  
* `!추천 받기` 입력

![recommend](https://user-images.githubusercontent.com/107746547/206863887-325729c2-249a-496d-b70e-c5fbabc63dec.PNG)


## How to Use  :jeans:
디스코드 서버 생성 후 아래 링크에 접속하여 서버에 봇을 추가하여 이용 가능

https://discord.com/oauth2/authorize?client_id=1042075320930541620&permissions=8&scope=bot

## File  :shoe:
* requirement.txt : 프로젝트 개발 시 사용한 패키지 목록
* main.py : 봇 실행할 최종 파일
* zip.py : 기능에 필요한 크롤링 모음 파일
* data.py : 크롤링에 필요한 url과 dictionary 모음

## License :eyeglasses:
MIT 라이센스 적용


## Reference :handbag:
* [건유1029](https://blog.yhs.kr/9) - 이벤트 함수 작성에 참고
* [므느으르](https://m.blog.naver.com/PostView.naver?blogId=seojune5383&logNo=222335067548&targetKeyword=&targetRecommendationCode=1) - embed 작성에 참고
* [proqk](https://foxtrotin.tistory.com/277) - 추천 기능 작성에 참고
* [코코블루의 다락방](https://m.blog.naver.com/6116949/221949748751) - 사용자 서버 입/퇴장시 메세지 출력에 참고

