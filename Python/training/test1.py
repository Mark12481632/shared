import pyspark.sql.functions as F

def convert_column(df, col_name, col_type_str):
	new_col = col_name + "_tmp"
	df = df.withColumn(new_col, F.column(col_name).cast(col_type_str)).drop(col_name).withColumnRenamed(new_col, col_name).drop(new_col)
	return df

data = spark.read.csv("/Users/markroberts/Development/training_data/weatherAUS.csv", header=True)

data = convert_column(data, "WindDir9am", "int")
data = convert_column(data, "WindSpeed9am", "int")
data = convert_column(data, "WindSpeed3pm", "int")
data = convert_column(data, "Humidity9am", "int")
data = convert_column(data, "Humidity3pm", "int")
data = convert_column(data, "Pressure9am", "int")
data = convert_column(data, "Pressure3pm", "int")
data = convert_column(data, "Temp9am", "int")
data = convert_column(data, "Temp3pm", "int")
data = convert_column(data, "RISK_MM", "float")
data = convert_column(data, "MaxTemp", "int")
data = convert_column(data, "MinTemp", "int")
data = convert_column(data, "Rainfall", "int")



