import pyspark.sql.functions as F
from pyspark.sql.types import StructField, StructType, StringType, DateType
from pyspark.sql import Row
import datetime

def create_rows(init_key, depth = 10):
        rows = []
        fkey = None
        for index in range(depth):
                pkey = fkey
                fkey = init_key + str(index)
                name = "Name-" + fkey
                row = Row(pkey, fkey, name)
                rows.append(row)
        return rows


def create_frame(spark, count):
        schema = StructType([
                StructField('PKEY', StringType(), True),
                StructField('FKEY', StringType(), True),
                StructField('NAME', StringType(), True)
                ])

        rows = []
        for index in range(count):
                rows.extend(create_rows("111" + str(index),5))
                rows.extend(create_rows("222" + str(index),6))
                rows.extend(create_rows("333" + str(index),7))

        df = spark.createDataFrame(rows, schema)
        return df

spark = SparkSession.builder.master("local").appName("Testing") \
                    .config("spark.some.config.option", "some-value") \
                    .getOrCreate()

df_1 = create_frame(spark, 2result = df_1.filter("PKEY is null").join(df_2, join_1, "left")
5000)
df_2 = df_1.withColumnRenamed("PKEY", "PKEY_1").withColumnRenamed("FKEY", "FKEY_1").withColumnRenamed("NAME", "NAME_1")
df_3 = df_1.withColumnRenamed("PKEY", "PKEY_2").withColumnRenamed("FKEY", "FKEY_2").withColumnRenamed("NAME", "NAME_2")
df_4 = df_1.withColumnRenamed("PKEY", "PKEY_3").withColumnRenamed("FKEY", "FKEY_3").withColumnRenamed("NAME", "NAME_3")
df_5 = df_1.withColumnRenamed("PKEY", "PKEY_4").withColumnRenamed("FKEY", "FKEY_4").withColumnRenamed("NAME", "NAME_4")
df_6 = df_1.withColumnRenamed("PKEY", "PKEY_5").withColumnRenamed("FKEY", "FKEY_5").withColumnRenamed("NAME", "NAME_5")
df_7 = df_1.withColumnRenamed("PKEY", "PKEY_6").withColumnRenamed("FKEY", "FKEY_6").withColumnRenamed("NAME", "NAME_6")
df_8 = df_1.withColumnRenamed("PKEY", "PKEY_7").withColumnRenamed("FKEY", "FKEY_7").withColumnRenamed("NAME", "NAME_7")
df_9 = df_1.withColumnRenamed("PKEY", "PKEY_8").withColumnRenamed("FKEY", "FKEY_8").withColumnRenamed("NAME", "NAME_8")

join_1 = (F.column("PKEY_1") == F.column("FKEY"))
join_2 = (F.column("PKEY_2") == F.column("FKEY_1"))
join_3 = (F.column("PKEY_3") == F.column("FKEY_2"))
join_4 = (F.column("PKEY_4") == F.column("FKEY_3"))
join_5 = (F.column("PKEY_5") == F.column("FKEY_4"))
join_6 = (F.column("PKEY_6") == F.column("FKEY_5"))
join_7 = (F.column("PKEY_7") == F.column("FKEY_6"))

result = df_1.filter("PKEY is null").join(df_2, join_1, "left")
result = result.join(df_3, join_2, "left")
result = result.join(df_4, join_3, "left")
result = result.join(df_5, join_4, "left")
result = result.join(df_6, join_5, "left")
result = result.join(df_7, join_6, "left")
result = result.join(df_8, join_7, "left")

result.show()


join_1 = (F.column("PKEY") == F.column("FKEY_1"))
join_2 = (F.column("PKEY_1") == F.column("FKEY_2"))
join_3 = (F.column("PKEY_2") == F.column("FKEY_3"))
join_4 = (F.column("PKEY_3") == F.column("FKEY_4"))
join_5 = (F.column("PKEY_4") == F.column("FKEY_5"))
join_6 = (F.column("PKEY_5") == F.column("FKEY_6"))
join_7 = (F.column("PKEY_6") == F.column("FKEY_7"))
