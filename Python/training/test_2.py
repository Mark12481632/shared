import pyspark.sql.functions as F
from pyspark.sql.types import StructField, StructType, StringType, DateType
from pyspark.sql import Row
import datetime

def create_frame(spark):
	schema = StructType([
		StructField('COL_1',  StringType(), True),
		StructField('PKEY_1', StringType(), True),
		StructField('FKEY_1', StringType(), True),
		StructField('NAME_1', StringType(), True)
		])

	row_1 = Row('ID_A','12345', None,    "Name-1")
	row_2 = Row('ID_B','12365', "12345", "Name-2")
	row_3 = Row('ID_C','12366', "12345", "Name-3")
	row_4 = Row('ID_D','12375', "12366", "Name-4")
	row_5 = Row('ID_E','12376', "12366", "Name-5")
	row_6 = Row('ID_F','12390', "12365", "Name-6")
	row_7 = Row('ID_G','12391', "12390", "Name-7")
	row_8 = Row('ID_H','1231A', "12391", "Name-8")
	row_9 = Row('ID_I','12381', "12375", "Name-9")
	row_A = Row('ID_J','12382', "12375", "Name-A")
	row_B = Row('ID_K','12385', "12376", "Name-B")
	row_C = Row('ID_L','12386', "12376", "Name-C")
	row_D = Row('ID_M','12398', "12381", "Name-D")
	row_E = Row('ID_N','12399', "12398", "Name-E")

	rows = [row_1, row_2, row_3, row_4, row_5, row_6, row_7,
		row_8, row_9, row_A, row_B, row_C, row_D, row_E]

	df = spark.createDataFrame(rows, schema)
	return df

spark = SparkSession.builder.master("local").appName("Testing") \
                    .config("spark.some.config.option", "some-value") \
                    .getOrCreate()

df_1 = create_frame(spark)
df_2 = df_1.withColumnRenamed("COL_1", "COL_2").withColumnRenamed("PKEY_1", "PKEY_2") \
           .withColumnRenamed("FKEY_1", "FKEY_2").withColumnRenamed("NAME_1", "NAME_2")
df_3 = df_1.withColumnRenamed("COL_1", "COL_3").withColumnRenamed("PKEY_1", "PKEY_3") \
           .withColumnRenamed("FKEY_1", "FKEY_3").withColumnRenamed("NAME_1", "NAME_3")
df_4 = df_1.withColumnRenamed("COL_1", "COL_4").withColumnRenamed("PKEY_1", "PKEY_4") \
           .withColumnRenamed("FKEY_1", "FKEY_4").withColumnRenamed("NAME_1", "NAME_4")
df_5 = df_1.withColumnRenamed("COL_1", "COL_5").withColumnRenamed("PKEY_1", "PKEY_5") \
           .withColumnRenamed("FKEY_1", "FKEY_5").withColumnRenamed("NAME_1", "NAME_5")
df_6 = df_1.withColumnRenamed("COL_1", "COL_6").withColumnRenamed("PKEY_1", "PKEY_6") \
           .withColumnRenamed("FKEY_1", "FKEY_6").withColumnRenamed("NAME_1", "NAME_6")
df_7 = df_1.withColumnRenamed("COL_1", "COL_7").withColumnRenamed("PKEY_1", "PKEY_7") \
           .withColumnRenamed("FKEY_1", "FKEY_7").withColumnRenamed("NAME_1", "NAME_7")

join_1 = (F.column("FKEY_2") == F.column("PKEY_1"))
join_2 = (F.column("FKEY_3") == F.column("PKEY_2"))
join_3 = (F.column("FKEY_4") == F.column("PKEY_3"))
join_4 = (F.column("FKEY_5") == F.column("PKEY_4"))
join_5 = (F.column("FKEY_6") == F.column("PKEY_5"))

result = df_1.filter("FKEY_1 is null").join(df_2, join_1, "left")
result = result.join(df_3, join_2, "left")
result = result.join(df_4, join_3, "left")
result = result.join(df_5, join_4, "left")

result.show()
