# TODO: ____를 학습 요구 사항에 맞게 채우세요.
from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment

# 실행 환경 생성
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

# 입력 데이터: (상품, 수량, 단가)
data = [("apple", 2, 1000), ("banana", 3, 500), ("apple", 1, 1000), ("banana", 2, 500)]
stream = env.from_collection(data, type_info=Types.TUPLE([Types.STRING(), Types.INT(), Types.INT()]))

# 상품별 거래 금액 계산 후 누적
sales = stream.map(lambda x: (x[0], x[1] * x[2]),
                   output_type=Types.TUPLE([Types.STRING(), Types.INT()]))
result_stream = sales.key_by(lambda x: x[0]).sum(1)

# 작업 실행 및 결과 출력
with result_stream.execute_and_collect("Product Sales") as results:
    for value in results:
        print(value, flush=True)
