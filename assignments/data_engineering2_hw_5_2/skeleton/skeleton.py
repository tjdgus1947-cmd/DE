# 아래 빈칸을 채워 상품별 주문 금액을 계산하세요.
from pyspark.sql import SparkSession


# 1. 상품별 단가와 주문 수량을 Pair RDD로 생성합니다.
spark = (
    SparkSession.builder
    .appName("ProductOrderJoin")
    .getOrCreate()
)
sc = spark.sparkContext
prices = sc.parallelize([("A", 1000), ("B", 2000), ("C", 3000)], 2)
orders = sc.parallelize([("A", 2), ("B", 1), ("A", 3), ("C", 2), ("D", 4)], 2)
print("상품 단가:", prices.collect())
print("주문 수량:", orders.collect())
print("원본 주문 수:", orders.count())


# 2. 공통 상품 키로 (수량, 단가)를 연결합니다.
joined = orders.join(prices)
print("조인 결과:", sorted(joined.collect()))
print("조인 결과 수:", joined.count())


# 3. 각 주문의 수량과 단가를 곱해 금액을 계산합니다.
amounts = joined.map(lambda pair: (pair[0], pair[1][0] * pair[1][1]))
print("주문별 금액:", sorted(amounts.collect()))


# 4. 상품별 주문 금액과 전체 금액을 집계합니다.
totals = amounts.reduceByKey(lambda a, b: a + b)
summary = sorted(totals.collect())
print("상품별 합계:", summary)
grand_total = amounts.map(lambda pair: pair[1]).sum()
print("전체 주문 금액:", grand_total)


# 5. 단가가 없는 상품의 제외와 집계 결과를 출력합니다.
print("D는 단가 RDD에 없으므로 조인 결과에 포함되지 않습니다.")
spark.stop()
