#!/bin/sh

#pa log dir
log_hadoop="/log/1130/sumeru_page_analyzer_worker_log/*/0000/*/*"

root_dir_hadoop="/app/st/wise-tc/xxxxxxxx"
output_dir="sitetype6_url"
output_dir_hadoop="${root_dir_hadoop}/${output_dir}"

mapper_prog="mapper.py"
reducer_prog="reduce.py"

#$HADOOP_HOME/bin/hadoop fs -rmr ${output_dir_hadoop}
/home/work/hadoop/bin/hadoop fs -rmr ${output_dir_hadoop}


echo ${output_dir_hadoop}
echo ${log_hadoop}

#$HADOOP_HOME/bin/hadoop streaming -input ${tckernel_log_hadoop} \
/home/work/hadoop/bin/hadoop streaming -input ${log_hadoop} \
-output ${output_dir_hadoop} \
-mapper "python ${mapper_prog}" \
-reducer "python ${reducer_prog}" \
-file "${mapper_prog}" \
-file "${reducer_prog}" \
-jobconf mapred.job.name="sitetype6"
#-jobconf mapred.reduce.tasks=1 \
