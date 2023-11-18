# kyunghee_ticketing
### 경희제 입장객 신청/관리 자동화


경희제 개방을 대비하고 경희제 개방 시에 학생회의 외부인 출입 관리 역량을 실증하기 위해
제작한 경희제 입장객 신청/관리 자동화 프로그램입니다.  

2023-11-16 23:00에 작업 시작하여
2023-11-17 01:40 현재 신청받은 인원들의 인적사항 데이터를 가지고 티켓을 자동으로 생성하는 기능을 구현 완료하였으며, 
빠른 시일 내에 QR 스캔 및 조회 기능도 구현하도록 하겠습니다. 
2023-11-19 02:41 QR스캔 및 신청정보조회 구현 완료, 중복스캔방지기능 및 수기조회기능 구현 예정

다른 분과 협업하여 제작하는 것도 고려하였기 때문에 최대한 깔끔하게 코드를 디자인해 보도록 하겠습니다. 


서울고등학교 77대 학생회 봉사차장 김동건 드림. 

# [사용법]
** 프로토타입용 매뉴얼로, 최종본과 상이할 수 있습니다. **
### 티켓 생성

티켓 생성 시에는 init.py를 이용하여 생성할 수 있습니다. 
신청자들의 이름과 학교를 visitorList.xlsx에 저장하고(구글 스프레드시트와 구글 폼 사용),
init.py를 실행하시면 "savedImg"폴더에 각 신청 인원의 티켓이 제작되어 저장됩니다. 

### QR 스캔하여 입장
입장시 QR 스캔후 사용자 정보를 조회하는 기능은 greeting_main.py를 통해 사용할 수 있습니다. 
실행하면 opencv 카메라 창이 뜨게 되는데, 이때 카메라에 입장권의 QR을 보여주면 인식하여 학교와 이름을 보여줍니다. 

추후 스캔된 명단을 기록으로 남겨 티켓 중복사용을 방지하고, 타 학교 관련하여 문제가 생겼을 때 증빙 자료로 사용할 수 있게 할 계획입니다. 


