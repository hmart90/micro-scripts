import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('climate').getOrCreate()

# rdd = spark.sparkContext.parallelize([1,2,3,4,5,6])
df = spark.read.format("csv").option("header", "true").option("delimiter", ";").load("hdfs:///climate/ta_d.csv")

print(df.count())