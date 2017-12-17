---
layout: post
title: Setup Box PITA
---
# 제품요구사항명세서
## 요구사항분석
+ 공용보상금에 관련한 저작권법의 개정으로 인해 소형점포를 위한 서비스의 필요성을 느낌
+ 음악재생용 pc마련이 곤란한 소형점포를 위해 저렴한 제품을 출시 할 필요설을 느낌
## 개념적 설계
+ 독립형 뮤직 셋톱박스에 대한 뮤직 스토리지 서버와 클라이언트로 구성된 MVP를 개발 
+ 뮤직 허그와 라디오의 개념을 활용하여 서버를 생성하여 노래를 재생하고 이를 클라이언트가 일정한     사용료를 내고 공유가능
## 기능요구사항
1. 이름 : 다음곡 재생/ 부팅시 음악이 시작된다. 다음곡 재생 버튼을 클릭하면 재생하던 곡을 멈추고 다음곡의 시작부분 부터 재생한다. LED에는 전곡 이름 대신 다음곡의 이름이 새로 띄워진다.만약 현재 틀고 있는 음악이 채널의 끝부분이라면, 첫번째곡으로 넘어가 재생된다.
2. 이름: 이전 곡 재생 / 부팅시 음악이 시작된다. 이전곡 재생 버튼을 클릭하면 재생하던 곡을 멈추고 전곡을 시작 부분부터 재생한다. LED에는 새로운 곡의 이름이 띄워진다. 만약 현재 틀고 있는 음악이 채널의 첫곡이라면, 이 버튼을 누르면 채널의 가장 마지막 곡이 처음부터 재생된다.
3. 일시 정지 및 다시 재생 / 음악이 재생되고 있는 시점일 때 일시정지 버튼을 클릭하면 음악 재생이 멈춘다. LED에서는 음악이 정지되었다는 메세지가 뜬다. 음악이 멈춘 시점에서 다시 일시정지 버튼을 누르면, 이전에 정지된 시점부터 다시 노래가 재생된다. 이때  LED 에는 음악이 재생된다는 메시지를 띄운다.
4. 채널 넘기기/ 노래가 재생되고 있는 상황에서 채널 넘기기 버튼을 누르면, 그 채널에서 재생하던 음악을 멈추고 다음 채널로 넘어간다. 이후 다음 채널의 첫곡 부터 재생이 시작된다. 이 채널에서도 일시정지, 다음곡, 이전곡 재생 등의 기능이 똑같이 작동해야한다. 만약 플레이리스트의 마지막 채널을 재생하고 있을 때, 채널 변경 버튼을 누르면 첫번째 채널로 넘어가 음악이 재생된다.
5. 전원 끄기./ 노래 재생 상태이거나 정지 상태일때 전원 끄기 버튼을 누르면 음악 재생이 멈춰지고 시스템이 종료된다. LCD는 전원이 꺼진다는 메세지를 남기고 3초후 꺼져야 한다.
## 논리적 설계
+ FTP서버를 셋톱박스의 서버로 활용할 것
+ VLC로 음악재생
+ while true문을 사용하여 노래를 계속 재생시킴
+ if절을 활용하여 버튼을 누르면 버튼 이벤트 실행

#코드

[깃허브 주소](http://github.com/zldzmfoq12/2017013190-)
# 디자인
## 3D 모델링
![](http://)
# 제작
## 3D 프린팅 관련 이미지
케이스 본체
[케이스 본체](https://drive.google.com/open?id=1VtcE5ARmzHchou-dYxlXVYtMR76Z6jSL)
케이스 뚜껑
[케이스 뚜껑](https://drive.google.com/open?id=1-5HJb7LS2lW5aK4_9Dkke7F-4YmLwJyt)
# 데모
##### in 코딩
<iframe width="854" height="480" src="https://www.youtube.com/embed/O5Tso9rf7Yg" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
[영상 링크](https://youtu.be/O5Tso9rf7Yg)

##### in 케이스 제작
<iframe width="640" height="360" src="https://www.youtube.com/embed/NX991LjEQ_U" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
[영상 링크](http://drive.google.com/file/d/1cV2RT-1sB_X4MGgu3--olx46Gp4m-OPT/view?usp=sharing)

##### in 라이노 디자인
<iframe width="640" height="360" src="https://www.youtube.com/embed/VHl3ixYbDjE" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
[영상 링크](http://drive.google.com/file/d/1sa9wysD4j8Yd2UAZaslkLR25RcSd1DEp/view?usp=sharing)

##### 발표 영상1
<iframe width="100%" height="360" src="https://drive.google.com/file/d/1BeynLDFvi7hL3BD_ppiUs8XJsTPm7T-i/view?usp=sharing" frameborder="0" allowfullscreen></iframe>
[영상 링크](http://drive.google.com/file/d/1BeynLDFvi7hL3BD_ppiUs8XJsTPm7T-i/view?usp=sharing)

##### 발표 영상2
<iframe width="100%" height="360" src="https://drive.google.com/file/d/1I-HpcxCCJ5QTuU5uS5H80oQuQ_JcW05A/view?usp=sharing" frameborder="0" allowfullscreen></iframe>
[영상 링크](http://drive.google.com/file/d/1I-HpcxCCJ5QTuU5uS5H80oQuQ_JcW05A/view?usp=sharing)

##### 발표 영상3
<iframe width="100%" height="360" src="https://drive.google.com/file/d/1Mp-6mnz4VBJJSyKxF0AAtrw1KhOea8bW/view?usp=sharing" frameborder="0" allowfullscreen></iframe>
[영상 링크](http://drive.google.com/file/d/1Mp-6mnz4VBJJSyKxF0AAtrw1KhOea8bW/view?usp=sharing)