from PySpark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("SpotfyPlaylist").getOrCreate()

# Load dataset
df = spark.read.csv("data/dataset.csv", header=True, inferSchema=True)

# Perform transformations
df_transformed = df.filter(df['Artist Name(s)'] > 100)

# Show results
df_transformed.show()

spark.stop()

