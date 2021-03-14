# Map-Reduce
* A map reduce algorithm that runs on Hadoop file system (HDFS). The algorithm has been implemented in python and the datasets used are from the github project Online-Machine-Learning-for-Cloud-Resource- Provisioning-of-Microservice-Backend-Systems. The aim of the algorithm is to segregate the CPU usage in a step function of 10 and output the number of samples, maximum, minimum, Median and Standard Deviation for the attribute of Memory Utilization Average for each segregation.

* To run the mapper and reducer files developed in python below steps have to be followed.
* 1.Open the command prompt as a administrator and change the directory to the bin folder of hadoop.
* 2.Run the below commands to start the hadoop:
- hdfs namenode -format
- hdfs start-all.cmd
* 3.Create a directory in the hadoop filesystem for storing the csv files using the command:
- hadoop fs -mkdir /inputFiles
* 4.Upload the csv files using the command:
- hadoop fs -put C:\Users\yaswa\Desktop\data\ /inputFiles
* 5.Run the mapper and reducer files using hadoop streaming jar. Go to the location of hadoop streaming jar and run the command:
- hadoop jar hadoop-streaming-3.3.0.jar-file C:\Users\yaswa\Desktop\Mapreduce\mapper.py -mapper "C:\Users\yaswa\AppData\Local\Programs\Python\Python39\python.exe C:\Users\yaswa\Desktop\Mapreduce\mapper.py" -file C:\Users\yaswa\Desktop\Mapreduce\reducer.py 
-reducer "C:\Users\yaswa\AppData\Local\Programs\Python\Python39\python.exe C:\Users\yaswa\Desktop\Mapreduce\reducer.py" -input /inputFiles/ -output /outputFiles3
