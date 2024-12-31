from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder.appName("BeginnerProject").getOrCreate()
# Load the dataset
df = spark.read.csv('crop_yield_data.csv', header=True, inferSchema=True)

# Show the first few rows of the dataframe
df.show(5)

