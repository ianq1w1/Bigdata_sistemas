
from pyspark.sql import SparkSession
import time 

start_time = time.time()
spark = SparkSession.builder \
    .appName("Exemplo CSV PySpark") \
    .getOrCreate()
# Lendo um arquivo CSV e criando um DataFrame
df = spark.read.csv("C:/Users/ianpe/Desktop/planilhateste.csv", header=True, inferSchema=True)
#insira o caminho de algum arquivo CSV  para leitura 

#faltam possiveis analises e tomadas de decisão em relação á o arquivo que for enviado aqui 


# Mostrar o esquema e as primeiras linhas do DataFrame
df.printSchema()
df.show()
end_time = time.time()
execution_time =  end_time - start_time 
print(execution_time)
spark.stop()

