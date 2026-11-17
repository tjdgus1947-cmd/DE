# TODO: ____를 학습 요구 사항에 맞게 채우세요.
from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment

# 실행 환경 생성
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(2)

# 입력 데이터: (키, 값)
data = [("A", 10), ("B", 20), ("A", 30), ("B", 40)]
stream = env.from_collection(data, type_info=Types.TUPLE([Types.STRING(), Types.INT()]))

# 값을 두 배로 변환한 뒤 키별 누적
mapped = stream.map(lambda x: (x[0], x[1] * 2),
                    output_type=Types.TUPLE([Types.STRING(), Types.INT()]))
result_stream = mapped.key_by(lambda x: x[0]).sum(1)

# 병렬 실행할 작업의 실행 계획 확인
print("DAG Execution Plan:\n", env.get_execution_plan())

# 작업 실행 및 결과 출력
with result_stream.execute_and_collect("Parallel Keyed Sum") as results:
    for value in results:
        print(value, flush=True)
