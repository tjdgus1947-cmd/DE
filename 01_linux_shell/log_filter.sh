# 로그 필터링 및 정리 자동화 스크립트
# 목표: 로그 파일에서 특정 키워드를 추출하고, 날짜별 백업 디렉토리에 정리 및 요약 파일을 생성한다.

# [Step 1] 샘플 로그 파일 만들기
cat <<EOF > system.log
[INFO] Start process
[ERROR] Disk read failure
[WARNING] Memory usage high
[INFO] Normal operation
[ERROR] Network timeout
[WARNING] CPU temperature warning
EOF

# [Step 2] 오늘 날짜를 YYYYMMDD 형식으로 저장
DATE=$(date +%Y%m%d)

# [Step 3] 날짜 기반 백업 디렉토리 생성
BACKUP_DIR="./backup_$DATE"
mkdir -p "$BACKUP_DIR"

# [Step 4] 키워드별 로그 추출
grep "ERROR" system.log > "$BACKUP_DIR/error.log"
grep "WARNING" system.log > "$BACKUP_DIR/warning.log"

# [Step 5] 로그 요약 파일 생성 (log_summary.txt)
echo "Log Summary ($DATE)" > "$BACKUP_DIR/log_summary.txt"
echo "ERROR logs:" >> "$BACKUP_DIR/log_summary.txt"
cat "$BACKUP_DIR/error.log" >> "$BACKUP_DIR/log_summary.txt"
echo "" >> "$BACKUP_DIR/log_summary.txt"
echo "WARNING logs:" >> "$BACKUP_DIR/log_summary.txt"
cat "$BACKUP_DIR/warning.log" >> "$BACKUP_DIR/log_summary.txt"

# [Step 6] 결과 확인
cat "$BACKUP_DIR/log_summary.txt"
