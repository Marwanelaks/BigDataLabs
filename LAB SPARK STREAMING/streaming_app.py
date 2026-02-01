from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Création du SparkContext
sc = SparkContext(
    appName="SparkStreamingWordCount"
)

# Création du StreamingContext (batch de 5 secondes)
ssc = StreamingContext(sc, 5)

# Lecture du flux socket
lines = ssc.socketTextStream("localhost", 9999)

# Transformation WordCount
words = lines.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word, 1))
word_counts = pairs.reduceByKey(lambda a, b: a + b)

# Affichage des résultats
word_counts.pprint()

# Démarrage du streaming
ssc.start()
ssc.awaitTermination()