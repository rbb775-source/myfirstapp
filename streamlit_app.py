import streamlit as st

st.title("🎈 태영이의 100번째 앱")
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
st.image("https://cdnweb01.wikitree.co.kr/webdata/editor/202112/06/img_20211206220519_7390a79c.webp")

# st.markdown(): 마크다운 문법 지원 (굵게, 기울임, 목록 등)
st.markdown("**굵은 텍스트**, *기울임 텍스트*")
st.markdown("""- 첫 번째 항목
- 두 번째 항목
- 여러 줄을 쓸 때""")

# 페이지 구조용 제목 출력
st.title("저녁 메뉴 추천")
st.header("오늘의 메뉴를 추천합니다")
st.subheader("맘스터치")

# 수평선 (구분선) 출력
st.markdown("---")  # 또는
st.divider()        # Streamlit >= 1.22 이상에서 가능
# 정보성 메시지 박스
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메세지입니다.")

# st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용

st.link_button("연결할 url을 이 다음 변수에 써주세요!", 'https://www.youtube.com/watch?v=4rKeGsHa0lE&list=RDMvLSfIB8w90&index=2')
# st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
st.sidebar.title("📌 사이드바 메뉴")
option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
st.write("안녕?", option)

# 정수 혹은 실수 입력
age = st.number_input("나이를 입력하세요",step=1 )

st.write(2025- age)
st.write("2***년에 태어나셨군요", age)


# 여러 옵션 중 하나 선택
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("선택한 성별:", gender)
# 드롭다운에서 하나 선택
color = st.selectbox("좋아하는 색을 선택하세요", ["빨강", "초록", "파랑"])
st.write("선택한 색상:", color)



# 여러 개 선택
subjects = st.multiselect("관심 있는 과목을 선택하세요", ["수학", "영어", "과학"])
st.write("선택한 과목:", subjects)

# 범위 내 숫자 슬라이드 선택
level = st.slider("난이도를 선택하세요", 1, 10, 5)
st.write("선택한 난이도:", level)

# 날짜 입력
date = st.date_input("날짜를 선택하세요")
st.write("선택한 날짜:", date)

# 시간 입력
time = st.time_input("시간을 선택하세요")
st.write("선택한 시간:", time)

# 카메라로 사진 촬영
image_data = st.camera_input("사진을 찍어보세요")
if image_data:
    st.image(image_data)