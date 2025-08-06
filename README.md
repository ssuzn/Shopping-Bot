# 🤖 쇼핑봇 (Discord Shopping Bot)

## 📌 Intro
사용자가 입력한 명령에 따라 온라인 의류 편집샵 **무신사(Musinsa)**에서 데이터를 실시간 크롤링해  
디스코드 채널에서 의류를 추천해주는 **자동화 봇**입니다.


## 🚀 주요 기능

| 명령어 | 설명 |
|--------|------|
| `!도움말` | 사용 가능한 명령어 안내 |
| `!쇼핑 상의` | 특정 카테고리(상의, 바지 등)의 상품 추천 |
| `!색상 상의 green` | 특정 카테고리 + 색상의 상품 추천 |
| `!추천받기` | 투표 기능 포함된 추천 임베드 메시지 출력 |

## 📸 기능 예시

| 명령어 | 동작 예시 |
|--------|-----------|
| `!도움말` | ![help](https://user-images.githubusercontent.com/107746547/206870108-7c80d9a1-50a9-46a3-a4dc-26e4aa8e15d3.PNG) |
| `!쇼핑` | ![help_shop](https://user-images.githubusercontent.com/107746547/206863226-1efb20a8-02d7-40f2-8106-798000b9fd97.PNG) |
| `!쇼핑 스니커즈` | ![shop](https://user-images.githubusercontent.com/107746547/206864295-999c46a2-b453-4570-9dc8-473982c99ad2.PNG) |
| `!색상` | ![help_color](https://user-images.githubusercontent.com/107746547/206863409-83692c9c-e4d7-4b61-ac56-dd3147479728.PNG) |
| `!색상 상의 green` | ![color](https://user-images.githubusercontent.com/107746547/206864299-09c20e28-b289-4229-b53c-e51f4545d2b2.PNG) |
| 카테고리 잘못 입력 | ![category_err](https://user-images.githubusercontent.com/107746547/206863484-25b92e80-e875-4c62-b7ed-4aa1758c2b44.PNG) |
| 색상 잘못 입력 | ![color_err](https://user-images.githubusercontent.com/107746547/206863490-c396310b-98cc-4840-b710-96ed639bdc77.PNG) |
| 카테고리, 색상 잘못 입력 | ![2err](https://user-images.githubusercontent.com/107746547/206863495-1882ab82-f2f3-4048-9a87-48e7dc2e1833.PNG) |
| `!추천받기` | ![recommend](https://user-images.githubusercontent.com/107746547/206870155-bdbd25c1-aeac-4d03-8adb-9c1e3d7408b3.PNG) |

## 🧱 프로젝트 구조

```
shopping-bot/
├── bot/                 # 봇 명령어 및 이벤트 핸들러
│   ├── commands.py
│   └── events.py
├── crawler/             # 무신사 크롤링 로직
│   ├── musinsa.py
│   └── data.py
├── utils/               # 공통 유틸 함수
│   └── embed.py
├── .env                 # Discord Bot Token
├── .gitignore
├── main.py              # 봇 실행 파일
├── requirements.txt     # 의존성 패키지 목록
└── README.md
```

## ⚙️ 실행 방법

### 1. Python 가상환경 생성 및 의존성 설치

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```

### 2. `.env` 파일 생성 (토큰 입력)

```env
DISCORD_TOKEN=your_discord_token_here
```

### 3. 봇 실행

```bash
python3 main.py
```

### 4. 디스코드 서버에서 테스트

```text
!쇼핑 상의
!색상 스커트 pink
!추천받기
```

## 💻 사용법
디스코드 서버 생성 후 아래 링크에 접속하여 서버에 봇을 추가하여 이용 가능

https://discord.com/oauth2/authorize?client_id=1042075320930541620&permissions=8&scope=bot

## 🔐 .gitignore

```gitignore
.env
__pycache__/
*.pyc
.idea/
venv/
```

## 📦 의존성

```txt
discord
discord.py
beautifulsoup4
requests
python-dotenv
```

## 📝 License

This project is licensed under the **MIT License**.  
© 2022 ssuzn

## 🙏 참고 자료

- [무신사 카테고리 페이지](https://www.musinsa.com/categories/item/)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [BeautifulSoup 문서](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [건유1029](https://blog.yhs.kr/9) - 이벤트 함수 작성에 참고
- [므느으르](https://m.blog.naver.com/PostView.naver?blogId=seojune5383&logNo=222335067548&targetKeyword=&targetRecommendationCode=1) - embed 작성에 참고
- [proqk](https://foxtrotin.tistory.com/277) - 추천 기능 작성에 참고
- [코코블루의 다락방](https://m.blog.naver.com/6116949/221949748751) - 사용자 서버 입/퇴장시 메세지 출력에 참고
