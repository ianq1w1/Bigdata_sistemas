from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import time

# Iniciar a contagem de tempo
start_time = time.time()

# Criar a sessão Spark
spark = SparkSession.builder \
    .appName("Big Data") \
    .getOrCreate()

# Ler o arquivo CSV e criar um DataFrame
# Substitua o caminho do arquivo
df = spark.read.csv("C:/Users/ianpe/Downloads/Crimes_-_2001_to_Present.csv", header=True, inferSchema=True)
spark.conf.set("spark.sql.repl.eagerEval.enabled", "true")


# Solicitar ao usuário o ano dos crimes
ano = input("Digite o ano dos crimes que deseja visualizar: ")

# Filtrar o DataFrame com base no ano inserido
df_filtered = df.filter(col("Year") == int(ano))


# Filtrando os crimes com descrição "THEFT"
# depoooois df_filtered = df.filter(col("Description") == "THEFT")


# Mostrar o esquema e as linhas do DataFrame filtrado
df_filtered.printSchema()
df_filtered.show()

# Encerrar a contagem de tempo e calcular o tempo de execução
end_time = time.time()
execution_time = end_time - start_time
print("Tempo de execução:", execution_time)

# Encerrar a sessão Spark
spark.stop()
