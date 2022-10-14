# 프로젝트 이름
<br>

    - 프로젝트 소개
    
    Github 협업으로 멀티캠퍼스 선물 리뷰 게시판 구현

    - 궁금하신 점
    [목표-서비스](#✨-1-목표-서비스)
    [프로젝트 진행 과정](#✏-3-프로젝트-진행과정)
    [실제 구현 화면](#🖥-4-실제-구현-화면)
    [느낀점&배운점](#5-프로젝트를-통해-배운-점-및-느낀점)

<hr>
<br>

## 🧰 사용 기술

<br>

<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=ffffff"/> 　<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> 　<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=ffffff"/> 　<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=ffffff"/> 　<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=ffffff"/> 　<img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=ffffff"/>

<br>

<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>

<br>

## 📅 프로젝트 기간

### 		2022.10.14



## 👩🏻‍💻 Members 

<br>

<a href="https://github.com/kleenex1/fourth_pair/graphs/contributors">

| <img src="https://contrib.rocks/image?repo=kleenex1/fourth_pair" /> |      |
| ------------------------------------------------------------ | ---- |
|                                                              | </a> |



## 💻 역할

- 깃 설정, 장고 개발 환경 설정, 회원 가입 : 변규탁
- 로그인, 회원 목록 조회, 회원 정보 수정, 로그아웃, 네비게이션 바 : 조병진
- 리뷰 생성, 목록 조회, 정보 수정, 삭제 : 노은빈

<br>

<hr>
<br>

## ✨ 1. 목표 서비스
<br>

## 목표

- **CRUD** 구현
- **Staticfiles** 활용 정적 파일(이미지, CSS, JS) 다루기
- Django **Auth** 활용 회원 관리(회원 가입 / 회원 조회 / 로그인 / 로그아웃)



### 1.1 회원 관리

<br>

1. 회원 가입 창 및 로그인/ 로그아웃
2. 회원 정보 수정
3. 회원 정보 삭제(탈퇴)



### 1.2 선물 리뷰 게시판

<br>

1. 선물 리뷰 생성, 조회, 삭제, 수정 기능
2. 별점을 이용한 평점 기능



## ✨ 2. 실제 구현 정도
<br>

### 2.1 회원 관리

1. 회원 가입 후 로그인, 로그아웃 기능
2. 회원 목록 페이지
3. 회원 정보 수정
4. 회원 탈퇴 기능

<br>

### 2.2 선물 리뷰 게시판

<br>

1. 게시판 글 생성, 목록, 수정, 삭제 기능
2. 로그인 한 상태에서 본인의 글만 수정 및 삭제 가능
3. 글쓰기 할 때 사진 첨부 기능

<br>

<hr>
<br>

## ✏ 3. 프로젝트 진행과정

<br>

### 3.1 깃허브 협업 과정

> 각각의 기능을 넣을 때마다 branch를 바꿔서 하기

<br>

#### 3.1.1 깃 협업 준비(branch 각각 만들어 관리하고 master로 병합)

1. [local/driver] master branch에서 개발 토픽에 해당하는 branch 생성 및 branch 전환

```bash
$ git checkout -b [토픽 브랜치명]
```

2. [local/driver] 토픽 개발
3. [local/driver] 토픽 개발 후 동일한 이름의 원격 저장소 branch에 Commit&Push

```bash
$ git add .

$ git commit -m '커밋 메세지'

$ git push origin [토픽 브랜치명]
```

4. [local/driver] 토픽 branch 병합(github 에서)
5. [local/driver] master branch 전환 후 Pull

```bash
# main 브랜치로 전환
$ git checkout main

# main 브랜치 Pull
$ git pull origin main
```

6. [local/driver] 토픽 branch 삭제

```bash
# 토픽 브랜치 삭제
$ git branch -d [토픽 브랜치명]
```

7. driver 변경 후 새 branch를 만들어서 다시 시작

<br>

### 📢참고 git branch 명령어

```bash
# 브랜치 생성 & 전환
git checkout -b [브랜치명]

# 브랜치 전환
git checkout [브랜치명]

# 브랜치 삭제
git branch -d [브랜치명]

# 브랜치 이름 변경
git branch -m [기존 브랜치명] [변경할 브랜치명]
```



#### 3.1.2 git 설정

- 원격 저장소 생성
- collaborator 초대

```bash
# branch master에서

# 로컬 저장소 git 초기화
$ git init

# 로컬 저장소 .gitignore 생성 
$ touch .gitigngit ore
```

- gitignore 작성

  [gitignore 사이트](https://www.toptal.com/developers/gitignore/)



### 3.2 장고 개발환경 설정



#### 3.2.1 가상 환경(venv) 생성 및 실행

```bash
# venv 생성
$ python -m venv venv

# venv 실행(Scripts 파일 있는 곳에서)
$ source venv/Scripts/activate
(venv)
```



#### 3.2.2 Django, Bootstrap5 설치 및 기록

```bash
# Django 설치
$ pip install django==3.2.13

# Bootstrap5 설치
$ pip install django-bootstrap5

# 패키지 목록 저장
$ pip freeze > requirements.txt

# Django 프로젝트 생성
$ django-admin startproject config .
```



### 3.3 회원 가입 

> branch accounts/signup



#### 3.3.1 accounts App 만들기

*app_name = 'accounts'*



#### 3.3.2 모델 Model

*모델 이름 : User*

- Django **AbstractUser** 모델 상속



#### 3.3.3 폼 Form

- Django 내장 회원 가입 폼 UserCreationForm을 상속 받아서 CustomUserCreationForm 작성

  해당 폼은 아래 필드만 출력

  - username
  - password1
  - password2



#### 3.3.4 기능 View

`회원 가입`

- `POST` http://127.0.0.1:8000/accounts/signup/

- CustomUserCreationForm을 활용해서 회원 가입 구현



#### 3.3.5 화면 Template

`회원 가입 페이지`

- `GET` http://127.0.0.1:8000/accounts/signup/

- 회원 가입 폼



### 3. 4 로그인

> branch accounts/login



#### 3.4.1 폼 Form

- Django 내장 로그인 폼 **AuthenticationForm 활용**



#### 3.4.2 기능 View

`로그인`

- `POST` http://127.0.0.1:8000/accounts/login/

- **AuthenticationForm**를 활용해서 로그인 구현



#### 3.4.2 화면 Template

`로그인 페이지`

- `GET` http://127.0.0.1:8000/accounts/login/

- 로그인 폼

- 회원 가입 페이지 이동 버튼



### 3.5 회원 목록 조회

> branch accounts/index



#### 3.5.1 **기능 View**

`회원 목록 조회`

- `GET` http://127.0.0.1:8000/accounts/



#### 3.5.2 화면 Template

`회원 목록 페이지	`

- `GET` http://127.0.0.1:8000/accounts/

- 회원 목록 출력

- 회원 아이디를 클릭하면 해당 회원 조회 페이지로 이동



### 3.6 회원 정보 조회

> branch accounts/detail



#### 3.6.1 기능 View

`회원 정보 조회`

- `GET` http://127.0.0.1:8000/accounts/[int:user_pk](int:user_pk)/



#### 3.6.2 화면 Template

`회원 조회 페이지(프로필 페이지)`

- `GET` http://127.0.0.1:8000/accounts/[int:user_pk](int:user_pk)/



### 3.7 회원 정보 수정

> branch accounts/update



#### 3.7.1 폼 Form

`회원 정보 수정`

- Django 내장 회원 수정 폼 UserChangeForm을 상속 받아서 **CustomUserChangeForm** 작성

  해당 폼은 아래 필드만 출력합니다.

  - first_name
  - last_name
  - email



#### 3.7.2 기능 View

`회원 정보 수정`

- `POST` http://127.0.0.1:8000/accounts/update/



#### 3.7.3 화면 Template

`회원 정보 수정 페이지	`

- `GET` http://127.0.0.1:8000/accounts/update/



### 3.8 로그아웃

> branch accounts/logout



#### 3.8.1 기능 View

`로그아웃`

- `POST` http://127.0.0.1:8000/accounts/logout/



### 3.9 네비게이션 바

>  branch template/navbar



#### 3.9.1 화면 Template

**네비게이션바**

- 리뷰 목록 페이지 이동 버튼
- 리뷰 작성 페이지 이동 버튼
- 비 로그인 유저는 작성 버튼 출력 X
- 로그인 상태에 따라 다른 화면 출력
  1. 로그인 상태
     - 로그인 한 사용자의 `username` 출력
       - `username`을 클릭하면 회원 조회 페이지로 이동
     - 로그아웃 버튼
  2. 비 로그인 상태
     - 로그인 페이지 이동 버튼
     - 회원가입 페이지 이동 버튼



#### 3.10 리뷰 생성

> branch reviews/create



#### 3.10.1 Reviews app 만들기

app_name = ' reviews'



#### 3.10.2 모델 Model

모델 이름 : Review

- 모델 필드

  | 이름       | 역할          | 필드     | 속성              |
  | ---------- | ------------- | -------- | ----------------- |
  | title      | 리뷰 제목     |          |                   |
  | content    | 리뷰 내용     |          |                   |
  | movie_name | 영화 이름     |          |                   |
  | grade      | 영화 평점     |          |                   |
  | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True |
  | updated_at | 리뷰 수정시간 | DateTime | auto_now = True   |



#### 3.10.3 기능 View

`데이터 생성`

- `POST` http://127.0.0.1:8000/reviews/create/



#### 3.10.4 화면 Template

`리뷰 작성 페이지`

- `GET` http://127.0.0.1:8000/reviews/create/
- 리뷰 작성 폼



### 3.11 리뷰 목록 조회

> branch reviews/index



### 3.11.1 **기능 View**

`데이터 목록 조회`

- `POST` http://127.0.0.1:8000/reviews/



#### 3.11.2 화면 Template

`리뷰 목록 페이지`

- `GET` http://127.0.0.1:8000/reviews/
- 리뷰 목록 출력
- 제목을 클릭하면 해당 리뷰의 정보 페이지로 이동



### 3.12 리뷰 정보 조회

> branch reviews/detail



#### 3.12.1 **기능 View**

`데이터 정보 조회`

- `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/



#### 3.12.2 화면 Template

`리뷰 정보 페이지`

- `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/
- 해당 리뷰 정보 출력
- 수정 / 삭제 버튼



### 3.13 리뷰 정보 수정

> branch reviews/update



#### 3.13.1 기능 View

`데이터 수정`

- `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/



#### 3.13.2 화면 Template

`리뷰 수정 페이지`

- `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/
- 리뷰 수정 폼



#### 3.14 리뷰 삭제

> branch reviews/delete



#### 3.14.1 기능 View

`데이터 삭제`

- `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/delete/



## 🖥 4. 실제 구현 화면

<br>

### 4.1 메인 페이지

<br>


    1. 메인 화면에서 '리뷰쓰기' 누르면 '로그인' 창으로 넘어감
    2. '로그인', '회원가입' 버튼 선택 가능
    3. '로그인' 시 리뷰 작성 가능

<br>

### 4.2 회원 가입 페이지

<br>

```
1. 이름, 비밀번호, 비밀번호 확인 작성 폼
2. 'save' 누르면 회원가입 완료
```

<br>

### 4.3 로그인 페이지

<br>

```
회원가입 후 로그인 성공하면 회원 이름의 표기와 함께 로그아웃 버튼 생성된 페이지로 이동
```

<br>

### 4.4 리뷰 작성 페이지

<br>

```
1. '리뷰 쓰기' 누르면 작성 페이지로 넘어감
2. 제목, 내용, 평점, 사진으로 구성// 수정, 삭제, 목록으로 버튼
3. 저장 시 제목, 평점, 사진, 내용 출력
```

<br>

### 4.5 리뷰 목록 페이지

<br>

```
'목록으로 이동' 누르면 리뷰 목록 페이지로 넘어감
```

<br>

### 4.6 로그아웃 페이지

<br>

```
'로그아웃'을 누르면 '메인' 페이지로 넘어옴
```



<br>

<hr>
<br>

## 5. 프로젝트를 통해 배운 점 및 느낀점

<br>

    

<br>


