# 계층형 디렉토리 자동 생성기 스크립트
# 목표: mkdir, echo, 반복문을 사용해 구조화된 디렉토리와 텍스트 파일을 자동으로 생성한다.

# [Step 1] 오늘 날짜를 YYYYMMDD 형식으로 변수에 저장
DATE=$(date +%Y%m%d)

# [Step 2] 기본 디렉토리 경로 구성
BASE_DIR="/home/ssafy/assignment1/$DATE"

# [Step 3] level_1 ~ level_3 디렉토리 생성 + README.txt 자동 생성
for i in 1 2 3
do
  DIR_PATH="$BASE_DIR/level_$i"
  mkdir -p "$DIR_PATH"
  echo "This is level_$i directory." > "$DIR_PATH/README.txt"
done

# [Step 4] 전체 디렉토리 구조를 트리 형태로 확인
tree /home/ssafy/assignment1/$DATE

# [Step 5] 생성된 README.txt 파일 내용 확인
cat /home/ssafy/assignment1/$DATE/level_1/README.txt
cat /home/ssafy/assignment1/$DATE/level_2/README.txt
cat /home/ssafy/assignment1/$DATE/level_3/README.txt

