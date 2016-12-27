

from pyspark import SparkConf, SparkContext
from datetime import datetime
import json
from operator import add
import os


path=os.path.dirname(os.path.abspath(__file__))
ouptput_file=path+"/out_count.json"
def main(hdfs_uri):
    """Divolte Spark Example.

    This example processes published Divolte log files at a given location.

    It displays:

     1. The total number of events in the log files.
     2. An arbitrary event.
     3. The ID of the session with the most events, along with the first 10
        events in that session.

    This is equivalent to the scala example.
    """
    sc = SparkContext()
    events_rdd = sc.newAPIHadoopFile(
        hdfs_uri,
        'org.apache.avro.mapreduce.AvroKeyInputFormat',
        'org.apache.avro.mapred.AvroKey',
        'org.apache.hadoop.io.NullWritable',
        keyConverter='io.divolte.spark.pyspark.avro.AvroWrapperToJavaConverter').map(lambda (k,v): k)

    
    events_rdd.cache()

    total_event_count = events_rdd.count()

    # Get the first event in our dataset (which isn't ordered yet).
    an_event = events_rdd.take(1)

    # Find the session with the most events.
    

    distinct_events = events_rdd \
        .map(lambda event: (event['eventType'],1)).reduceByKey(add).collect()
    #.map(lambda event: (event['eventType'], event['timestamp'])) \
    # Simple function for rendering timestamps.
    def timestamp_to_string(ts):
        return datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M:%S')

    # Print the results we accumulated, with some whitespace at the
    # front to separate this from the logging.
    distinct_events= dict(distinct_events)
    with open(ouptput_file,"w") as h:
        h.write(json.dumps(distinct_events, indent=2))
        h.close()

if __name__ == "__main__":
    import sys
    if (len(sys.argv) >= 2):
        main(*sys.argv[1:])
    else:
        print >> sys.stderr, "Usage: spark-submit [...] divolte_spark_example.py PATH_TO_DIVOLTE_LOGS"
