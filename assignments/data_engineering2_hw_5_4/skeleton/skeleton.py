# 빈칸(____)을 채워 아래 데이터 처리 단계를 구현하세요.
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("RDDTransformMethods")
    .getOrCreate()
)
sc = spark.sparkContext
rdd = sc.parallelize(range(1, 21), 4)
print("입력:", rdd.collect())

# 원소 단위로 짝수를 선택한 뒤 2배로 변환합니다.
filtered_mapped = (
    rdd
    .filter(lambda x: x % 2 == 0)
    .map(lambda x: x * 2)
)
print("filter + map:", filtered_mapped.collect())

# 각 원소에서 0개 또는 1개의 값을 반환합니다.
flattened = rdd.flatMap(lambda x: [x * 2] if x % 2 == 0 else [])
print("flatMap:", flattened.collect())


# 파티션 iterator를 받아 변환한 원소들을 반환합니다.
def transform_partition(iterator):
    return (x * 2 for x in iterator if x % 2 == 0)


partitioned = rdd.mapPartitions(transform_partition)
print("mapPartitions:", partitioned.collect())
spark.stop()
