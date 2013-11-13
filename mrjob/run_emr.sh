#!/bin/bash
python matrix_multiplication.py -r emr \
	--num-ec2-instances 3 \
	--ec2-master-instance-type m1.small \
	--ec2-instance-type m1.small \
	--s3-scratch-uri s3://zebit-emr-workshop-20131113/jukka/tmp/ \
	--s3-log-uri s3://zebit-emr-workshop-20131113/jukka/logs/ \
	s3://zebit-emr-workshop-20131113/jukka/input_matrix_multiplication.txt \
	--output-dir=s3://zebit-emr-workshop-20131113/jukka/output/
