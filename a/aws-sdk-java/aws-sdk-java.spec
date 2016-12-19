Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global githash 9883b981ab5103cc6944fbf8f3b973994777350f
Name:          aws-sdk-java
Version:       1.11.3
Release:       alt1_2jpp8
Summary:       AWS SDK for Java
# Some source files are without license headers
# reported @ https://github.com/aws/aws-sdk-java/issues/719
# This file aws-java-sdk-core/src/test/java/org/bitpedia/util/Base32.java is under Public Domain license
# http://bitzi.com/publicdomain for more info.
# brazil/src/appgroup/globalPaymentServices/tools/YaUtils/mainline/tst/org/bitpedia/util/Base32.java
License:       ASL 2.0
URL:           http://aws.amazon.com/sdk-for-java/
Source0:       https://github.com/aws/aws-sdk-java/archive/%{githash}/%{name}-%{githash}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-cbor)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(javax.mail:javax.mail-api)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
# code-generator deps
#BuildRequires: mvn(org.eclipse:text:3.3.0-v20070606-0010)
#BuildRequires: mvn(org.eclipse.jdt:org.eclipse.jdt.core:3.10.0)
#BuildRequires: mvn(org.freemarker:freemarker)
# maven-plugin deps
#BuildRequires: mvn(org.apache.maven:maven-plugin-api)
#BuildRequires: mvn(org.apache.maven:maven-project)
#BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
#BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
# swf-libraries deps
# springframework:3.0.7.RELEASE
#BuildRequires: mvn(org.springframework:spring-beans)
#BuildRequires: mvn(org.springframework:spring-context)
#BuildRequires: mvn(org.springframework:spring-core)
#BuildRequires: mvn(org.springframework:spring-test)
#BuildRequires: mvn(org.aspectj:aspectjrt:1.8.2)
#BuildRequires: mvn(org.codehaus.mojo:aspectj-maven-plugin:1.7)

BuildArch:     noarch
Source44: import.info

%description
The AWS SDK for Java enables Java developers to easily work with
Amazon Web Services and build scalable solutions with Amazon S3,
Amazon DynamoDB, Amazon Glacier, and more.

%package acm
Group: Development/Java
Summary:       AWS Java SDK for AWS Certificate Manager

%description acm
The AWS Java SDK for AWS Certificate Manager module
holds the client classes that are used for communicating
with AWS Certificate Manager service.

%package api-gateway
Group: Development/Java
Summary:       AWS Java SDK for Amazon API Gateway

%description api-gateway
The AWS Java SDK for Amazon API Gateway module
holds the client classes that are used for
communicating with Amazon API Gateway.

%package applicationautoscaling
Group: Development/Java
Summary:       AWS Java SDK for AWS Application Auto Scaling

%description applicationautoscaling
The AWS Java SDK for AWS Application Auto Scaling module
holds the client classes that are used for communicating
with AWS Application Auto Scaling service.

%package autoscaling
Group: Development/Java
Summary:       AWS Java SDK for Auto Scaling

%description autoscaling
The AWS Java SDK for Auto Scaling module holds the
client classes that are used for communicating with
Auto Scaling Service.

%package bom
Group: Development/Java
Summary:       AWS SDK for Java - BOM

%description bom
The AWS SDK for Java - BOM module holds the
dependency managements for individual Java clients.

%package cloudformation
Group: Development/Java
Summary:       AWS Java SDK for AWS CloudFormation

%description cloudformation
The AWS Java SDK for AWS CloudFormation module holds the
client classes that are used for communicating with
AWS CloudFormation Service.

%package cloudfront
Group: Development/Java
Summary:       AWS Java SDK for Amazon CloudFront

%description cloudfront
The AWS Java SDK for Amazon CloudFront module holds the
client classes that are used for communicating with
Amazon CloudFront Service.

%package cloudhsm
Group: Development/Java
Summary:       AWS Java SDK for the AWS CloudHSM

%description cloudhsm
The AWS Java SDK for AWS CloudHSM holds the client
classes that are used for communicating with the
AWS CloudHSM Service.

%package cloudsearch
Group: Development/Java
Summary:       AWS Java SDK for Amazon CloudSearch

%description cloudsearch
The AWS Java SDK for Amazon CloudSearch module holds the
client classes that are used for communicating with
Amazon CloudSearch Service.

%package cloudtrail
Group: Development/Java
Summary:       AWS Java SDK for AWS CloudTrail

%description cloudtrail
The AWS Java SDK for AWS CloudTrail module holds the
client classes that are used for communicating with
AWS CloudTrail Service.

%package cloudwatch
Group: Development/Java
Summary:       AWS Java SDK for Amazon CloudWatch

%description cloudwatch
The AWS Java SDK for Amazon CloudWatch module holds the
client classes that are used for communicating with
Amazon CloudWatch Service.

%package cloudwatchmetrics
Group: Development/Java
Summary:       CloudWatch Metrics for AWS Java SDK

%description cloudwatchmetrics
This package holds the classes for uploading the
client side metrics collected from AWS Java SDK to
Amazon CloudWatch.

#%% package code-generator

%package codecommit
Group: Development/Java
Summary:       AWS Java SDK for AWS CodeCommit

%description codecommit
The AWS Java SDK for AWS CodeCommit module
holds the client classes that are used for
communicating with AWS CodeCommit.

%package codedeploy
Group: Development/Java
Summary:       AWS Java SDK for AWS CodeDeploy

%description codedeploy
The AWS Java SDK for AWS CodeDeploy module holds the
client classes that are used for communicating with
AWS CodeDeploy Service.

#%% package codegen-maven-plugin

%package codepipeline
Group: Development/Java
Summary:       AWS Java SDK for AWS CodePipeline

%description codepipeline
The AWS Java SDK for AWS CodePipeline module
holds the client classes that are used for
communicating with AWS CodePipeline.

%package cognitoidentity
Group: Development/Java
Summary:       AWS Java SDK for Amazon Cognito Identity

%description cognitoidentity
The AWS Java SDK for Amazon Cognito Identity module holds the
client classes that are used for communicating with
Amazon Cognito Identity Service.

%package cognitoidp
Group: Development/Java
Summary:       AWS Java SDK for Amazon Cognito Identity Provider Service

%description cognitoidp
The AWS Java SDK for Amazon Cognito Identity Provider Service module
holds the client classes that are used for communicating with
Amazon Cognito Identity Provider Service.

%package cognitosync
Group: Development/Java
Summary:       AWS Java SDK for Amazon Cognito Sync

%description cognitosync
The AWS Java SDK for Amazon Cognito Sync module holds the
client classes that are used for communicating with
Amazon Cognito Sync Service.

%package config
Group: Development/Java
Summary:       AWS Java SDK for AWS Config

%description config
The AWS Java SDK for AWS Config module holds the
client classes that are used for communicating with
AWS Config Service.

%package core
Group: Development/Java
Summary:       AWS SDK for Java - Core

%description core
The AWS SDK for Java - Core module holds the classes that
is used by the individual service clients to interact with
Amazon Web Services. Users need to depend on aws-java-sdk
artifact for accessing individual client classes.

%package datapipeline
Group: Development/Java
Summary:       AWS Java SDK for AWS Data Pipeline

%description datapipeline
The AWS Java SDK for AWS Data Pipeline module holds the
client classes that are used for communicating with
AWS Data Pipeline Service.

%package devicefarm
Group: Development/Java
Summary:       AWS Java SDK for AWS Device Farm

%description devicefarm
The AWS Java SDK for AWS Device Farm module
holds the client classes that are used for
communicating with AWS Device Farm.

%package directconnect
Group: Development/Java
Summary:       AWS Java SDK for AWS Direct Connect

%description directconnect
The AWS Java SDK for AWS Direct Connect module holds the
client classes that are used for communicating with
AWS Direct Connect Service.

%package directory
Group: Development/Java
Summary:       AWS Java SDK for AWS Directory Service

%description directory
The AWS Java SDK for AWS Directory Service module
holds the client classes that is used for
communicating with AWS Directory Service.

%package discovery
Group: Development/Java
Summary:       AWS Java SDK for AWS Application Discovery Service

%description discovery
The AWS Java SDK for AWS Application Discovery Service module
holds the client classes that are used for communicating with
AWS Application Discovery Service.

%package dms
Group: Development/Java
Summary:       AWS Java SDK for AWS Database Migration Service

%description dms
The AWS Java SDK for AWS Database Migration Service module
holds the client classes that are used for communicating
with AWS Database Migration Service.

%package dynamodb
Group: Development/Java
Summary:       AWS Java SDK for Amazon DynamoDB

%description dynamodb
The AWS Java SDK for Amazon DynamoDB module holds the
client classes that are used for communicating with
Amazon DynamoDB Service.

%package ec2
Group: Development/Java
Summary:       AWS Java SDK for Amazon EC2

%description ec2
The AWS Java SDK for Amazon EC2 module holds the
client classes that are used for communicating with
Amazon EC2 Service.

%package ecr
Group: Development/Java
Summary:       AWS Java SDK for the Amazon EC2 Container Registry

%description ecr
The AWS Java SDK for the Amazon EC2 Container Registry
holds the client classes that are used for communicating
with the Amazon EC2 Container Registry Service.

%package ecs
Group: Development/Java
Summary:       AWS Java SDK for the Amazon EC2 Container Service

%description ecs
The AWS Java SDK for the Amazon EC2 Container Service
holds the client classes that are used for communicating
with the Amazon EC2 Container Service.

%package efs
Group: Development/Java
Summary:       AWS Java SDK for Amazon Elastic File System

%description efs
The AWS Java SDK for Amazon Elastic File System module
holds the client classes that are used for communicating
with Amazon Elastic File System.

%package elasticache
Group: Development/Java
Summary:       AWS Java SDK for Amazon ElastiCache

%description elasticache
The AWS Java SDK for Amazon ElastiCache module holds the
client classes that are used for communicating with
Amazon ElastiCache Service.

%package elasticbeanstalk
Group: Development/Java
Summary:       AWS Java SDK for AWS Elastic Beanstalk

%description elasticbeanstalk
The AWS Java SDK for AWS Elastic Beanstalk module holds the
client classes that are used for communicating with
AWS Elastic Beanstalk Service.

%package elasticloadbalancing
Group: Development/Java
Summary:       AWS Java SDK for Elastic Load Balancing

%description elasticloadbalancing
The AWS Java SDK for Elastic Load Balancing module holds the
client classes that are used for communicating with
Elastic Load Balancing Service.

%package elasticsearch
Group: Development/Java
Summary:       AWS Java SDK for Amazon Elasticsearch Service

%description elasticsearch
The AWS Java SDK for Amazon Elasticsearch Service module
holds the client classes that are used for communicating
with Amazon Elasticsearch Service.

%package elastictranscoder
Group: Development/Java
Summary:       AWS Java SDK for Amazon Elastic Transcoder

%description elastictranscoder
The AWS Java SDK for Amazon Elastic Transcoder module
holds the client classes that are used for communicating
with Amazon Elastic Transcoder Service.

%package emr
Group: Development/Java
Summary:       AWS Java SDK for Amazon EMR

%description emr
The AWS Java SDK for Amazon EMR module holds the
client classes that are used for communicating
with Amazon Elastic MapReduce Service.

%package events
Group: Development/Java
Summary:       AWS Java SDK for Amazon CloudWatch Events

%description events
The AWS Java SDK for Amazon CloudWatch Events module
holds the client classes that are used for communicating
with Amazon CloudWatch Events Service.

%package gamelift
Group: Development/Java
Summary:       AWS Java SDK for AWS GameLift

%description gamelift
The AWS Java SDK for AWS GameLift module holds the
client classes that are used for communicating with
AWS GameLift service.

%package glacier
Group: Development/Java
Summary:       AWS Java SDK for Amazon Glacier

%description glacier
The AWS Java SDK for Amazon Glacier module holds the
client classes that are used for communicating with
Amazon Glacier Service.

%package iam
Group: Development/Java
Summary:       AWS Java SDK for AWS IAM

%description iam
The AWS Java SDK for AWS IAM module holds the
client classes that are used for communicating with
AWS Identity and Access Management Service.

%package importexport
Group: Development/Java
Summary:       AWS Java SDK for AWS Import/Export

%description importexport
The AWS Java SDK for AWS Import/Export module
holds the client classes that are used
for communicating with AWS Import/Export Service.

%package inspector
Group: Development/Java
Summary:       AWS Java SDK for Amazon Inspector Service

%description inspector
The AWS Java SDK for Amazon Inspector Service module
holds the client classes that are used for communicating with
Amazon Inspector Service.

%package iot
Group: Development/Java
Summary:       AWS Java SDK for AWS IoT

%description iot
The AWS Java SDK for AWS Iot Service module holds the
client classes that are used for communicating with
AWS IoT Service.

%package kinesis
Group: Development/Java
Summary:       AWS Java SDK for Amazon Kinesis

%description kinesis
The AWS Java SDK for Amazon Kinesis module holds the
client classes that are used for communicating with
Amazon Kinesis Service.

%package kms
Group: Development/Java
Summary:       AWS Java SDK for AWS KMS

%description kms
The AWS Java SDK for AWS KMS module holds the
client classes that are used for communicating with
AWS Key Management Service.

%package lambda
Group: Development/Java
Summary:       AWS Java SDK for AWS Lambda

%description lambda
The AWS Java SDK for AWS Lambda module holds the
client classes that are used for communicating with
AWS Lambda Service.

%package logs
Group: Development/Java
Summary:       AWS Java SDK for Amazon CloudWatch Logs

%description logs
The AWS Java SDK for Amazon CloudWatch Logs module
holds the client classes that are used for communicating
with Amazon CloudWatch Logs Service.

%package machinelearning
Group: Development/Java
Summary:       AWS Java SDK for Amazon Machine Learning

%description machinelearning
The AWS Java SDK for Amazon Machine Learning module
holds the client classes that is used for communicating
with Amazon Machine Learning Service.

%package marketplacecommerceanalytics
Group: Development/Java
Summary:       AWS Java SDK for AWS Marketplace Commerce Analytics

%description marketplacecommerceanalytics
The AWS Java SDK for AWS Marketplace Commerce Analytics Service module
holds the client classes that are used for communicating with
AWS Marketplace Commerce Analytics Service.

%package marketplacemeteringservice
Group: Development/Java
Summary:       AWS Java SDK for AWS Marketplace Metering Service

%description marketplacemeteringservice
The AWS Java SDK for AWS Marketplace Metering Service module
holds the client classes that are used for communicating with
AWS Marketplace Metering Service.

%package opsworks
Group: Development/Java
Summary:       AWS Java SDK for AWS OpsWorks

%description opsworks
The AWS Java SDK for AWS OpsWorks module holds the
client classes that are used for communicating with
AWS OpsWorks Service.

%package pom
Group: Development/Java
Summary:       AWS SDK for Java - Parent POM

%description pom
AWS SDK for Java - Parent POM.

%package rds
Group: Development/Java
Summary:       AWS Java SDK for Amazon RDS

%description rds
The AWS Java SDK for Amazon RDS module holds the
client classes that are used for communicating with
Amazon Relational Database Service.

%package redshift
Group: Development/Java
Summary:       AWS Java SDK for Amazon Redshift

%description redshift
The AWS Java SDK for Amazon Redshift module holds the
client classes that are used for communicating with
Amazon Redshift Service.

%package route53
Group: Development/Java
Summary:       AWS Java SDK for Amazon Route53

%description route53
The AWS Java SDK for Amazon Route53 module holds the
client classes that are used for communicating with
Amazon Route53 Service.

%package s3
Group: Development/Java
Summary:       AWS Java SDK for Amazon S3

%description s3
The AWS Java SDK for Amazon S3 module holds the
client classes that are used for communicating with
Amazon Simple Storage Service.

%package ses
Group: Development/Java
Summary:       AWS Java SDK for Amazon SES

%description ses
The AWS Java SDK for Amazon SES module holds the
client classes that are used for communicating with
Amazon Simple Email Service.

%package simpledb
Group: Development/Java
Summary:       AWS Java SDK for Amazon SimpleDB

%description simpledb
The AWS Java SDK for Amazon SimpleDB module holds the
client classes that are used for communicating with
Amazon SimpleDB Service.

%package simpleworkflow
Group: Development/Java
Summary:       AWS Java SDK for Amazon SWF

%description simpleworkflow
The AWS Java SDK for Amazon SWF module holds the
client classes that are used for communicating with
Amazon Simple Workflow Service.

%package sns
Group: Development/Java
Summary:       AWS Java SDK for Amazon SNS

%description sns
The AWS Java SDK for Amazon SNS module holds the
client classes that are used for communicating with
Amazon Simple Notification Service.

%package sqs
Group: Development/Java
Summary:       AWS Java SDK for Amazon SQS

%description sqs
The AWS Java SDK for Amazon SQS module holds the
client classes that are used for communicating with
Amazon Simple Queue Service.

%package ssm
Group: Development/Java
Summary:       AWS Java SDK for the AWS Simple Systems Management (SSM) Service

%description ssm
The AWS Java SDK for AWS Simple Systems Management Service
holds the client classes that are used for communicating
with the AWS Simple Systems Management Service.

%package storagegateway
Group: Development/Java
Summary:       AWS Java SDK for AWS Storage Gateway

%description storagegateway
The AWS Java SDK for AWS Storage Gateway module holds the
client classes that are used for communicating with
AWS Storage Gateway Service.

%package sts
Group: Development/Java
Summary:       AWS Java SDK for AWS STS

%description sts
The AWS Java SDK for AWS STS module holds the
client classes that are used for communicating with
AWS Security Token Service.

%package support
Group: Development/Java
Summary:       AWS Java SDK for AWS Support

%description support
The AWS Java SDK for AWS Support module holds the
client classes that are used for communicating with
AWS Support Service.

#%% package swf-libraries

%package test-utils
Group: Development/Java
Summary:       AWS SDK for Java - Test Utils

%description test-utils
The AWS SDK for Java - Test Utils module holds the
all the utilities that are used by the tests.

%package waf
Group: Development/Java
Summary:       AWS Java SDK for AWS WAF

%description waf
The AWS Java SDK for AWS WAF Service module holds the
client classes that are used for communicating with
AWS WAF Service.

%package workspaces
Group: Development/Java
Summary:       AWS Java SDK for Amazon WorkSpaces

%description workspaces
The AWS Java SDK for Amazon WorkSpaces module holds the
client classes that are used for communicating with
Amazon WorkSpaces Service.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{githash}

# Remove deprecated httpclient annotations
sed -i '/NotThreadSafe/d' \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/CloudWatchMetricConfig.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/AmazonWebServiceRequest.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/ApacheHttpClientConfig.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/ClientConfiguration.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/DefaultRequest.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/RequestClientOptions.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/ExecutionContext.java \
 aws-java-sdk-core/src/test/java/com/amazonaws/http/response/HttpResponseProxy.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/event/ProgressInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/internal/ReleasableInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/internal/ResettableInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/metrics/ServiceLatencyProvider.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/AWSRequestMetrics.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/AWSRequestMetricsFullSupport.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/LengthCheckInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/TimingInfo.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/TimingInfoFullSupport.java

sed -i '/ThreadSafe/d' \
 aws-java-sdk-autoscaling/src/main/java/com/amazonaws/services/autoscaling/AmazonAutoScalingAsyncClient.java \
 aws-java-sdk-autoscaling/src/main/java/com/amazonaws/services/autoscaling/AmazonAutoScalingClient.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/MetricCollectorSupport.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/PredefinedMetricTransformer.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/RequestMetricCollectorSupport.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/ServiceMetricCollectorSupport.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/provider/transform/DynamoDBRequestMetricTransformer.java \
 aws-java-sdk-codecommit/src/main/java/com/amazonaws/services/codecommit/AWSCodeCommitAsyncClient.java \
 aws-java-sdk-codecommit/src/main/java/com/amazonaws/services/codecommit/AWSCodeCommitClient.java \
 aws-java-sdk-codedeploy/src/main/java/com/amazonaws/services/codedeploy/AmazonCodeDeployAsyncClient.java \
 aws-java-sdk-codedeploy/src/main/java/com/amazonaws/services/codedeploy/AmazonCodeDeployClient.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/AmazonHttpClient.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/conn/ssl/SdkTLSSocketFactory.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/impl/client/HttpRequestNoRetryHandler.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/event/request/Progress.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/event/request/ProgressSupport.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/impl/client/SdkHttpRequestRetryHandler.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/LengthCheckInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/TimingInfoUnmodifiable.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/VersionInfoUtils.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/AmazonDynamoDBAsyncClient.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/AmazonDynamoDBClient.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/AmazonDynamoDBStreamsAsyncClient.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/AmazonDynamoDBStreamsClient.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/DynamoDB.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/Index.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/Table.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/BatchGetItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/BatchWriteItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/DeleteItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/GetItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/ListTablesApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/PutItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/QueryApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/ScanApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/UpdateItemApi.java \
 aws-java-sdk-elasticloadbalancing/src/main/java/com/amazonaws/services/elasticloadbalancing/AmazonElasticLoadBalancingAsyncClient.java \
 aws-java-sdk-elasticloadbalancing/src/main/java/com/amazonaws/services/elasticloadbalancing/AmazonElasticLoadBalancingClient.java \
 aws-java-sdk-elasticsearch/src/main/java/com/amazonaws/services/elasticsearch/AWSElasticsearchAsyncClient.java \
 aws-java-sdk-elasticsearch/src/main/java/com/amazonaws/services/elasticsearch/AWSElasticsearchClient.java \
 aws-java-sdk-elastictranscoder/src/main/java/com/amazonaws/services/elastictranscoder/AmazonElasticTranscoderAsyncClient.java \
 aws-java-sdk-elastictranscoder/src/main/java/com/amazonaws/services/elastictranscoder/AmazonElasticTranscoderClient.java \
 aws-java-sdk-gamelift/src/main/java/com/amazonaws/services/gamelift/AmazonGameLiftAsyncClient.java \
 aws-java-sdk-gamelift/src/main/java/com/amazonaws/services/gamelift/AmazonGameLiftClient.java \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/internal/FileLocks.java \
 aws-java-sdk-ssm/src/main/java/com/amazonaws/services/simplesystemsmanagement/AWSSimpleSystemsManagementAsyncClient.java \
 aws-java-sdk-ssm/src/main/java/com/amazonaws/services/simplesystemsmanagement/AWSSimpleSystemsManagementClient.java \
 aws-java-sdk-storagegateway/src/main/java/com/amazonaws/services/storagegateway/AWSStorageGatewayAsyncClient.java \
 aws-java-sdk-storagegateway/src/main/java/com/amazonaws/services/storagegateway/AWSStorageGatewayClient.java

sed -i '/Immutable/d' \
 aws-java-sdk-cloudfront/src/main/java/com/amazonaws/auth/PEMObject.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/event/ProgressEvent.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/auth/profile/internal/Profile.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/retry/RetryPolicy.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/retry/internal/AuthRetryParameters.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/ArrayIndexElement.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/B.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/BOOL.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/BS.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/GetItemExpressionSpec.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/L.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/M.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/N.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/NamedElement.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/NS.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/NULL.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/Path.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/PathOperand.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/Precedence.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/RemoveAction.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/S.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/SS.java \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/internal/S3V4AuthErrorRetryStrategy.java \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/model/InstructionFileId.java \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/model/S3ObjectId.java

sed -i '/GuardedBy/d' \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/datamodeling/DynamoDBReflector.java \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/internal/crypto/MultipartUploadCryptoContext.java

%pom_remove_plugin -r com.github.siom79.japicmp:japicmp-maven-plugin

# Disable building of super-JAR
%pom_disable_module aws-java-sdk-osgi
# Missing dependency: aspectj{rt,-maven-plugin}
%pom_disable_module aws-java-sdk-swf-libraries
# Missing dependency: org.eclipse:text:3.3.0-v20070606-0010
%pom_disable_module aws-java-sdk-code-generator
# Missing dependency: :aws-java-sdk-code-generator
%pom_disable_module aws-java-sdk-codegen-maven-plugin

%pom_remove_dep :aws-java-sdk-swf-libraries aws-java-sdk

# Convert from dos to unix line ending
for file in src/samples/AmazonEC2SpotInstances-Advanced/CreateSecurityGroupApp.java \
 src/samples/AmazonEC2SpotInstances-Advanced/GettingStartedApp.java \
 src/samples/AmazonEC2SpotInstances-Advanced/InlineGettingStartedCodeSampleApp.java \
 src/samples/AmazonEC2SpotInstances-Advanced/InlineTaggingCodeSampleApp.java \
 src/samples/AmazonEC2SpotInstances-Advanced/Requests.java \
 src/samples/AmazonEC2SpotInstances-GettingStarted/CreateSecurityGroupApp.java \
 src/samples/AmazonEC2SpotInstances-GettingStarted/InlineGettingStartedCodeSampleApp.java \
 src/samples/AmazonEC2SpotInstances-GettingStarted/Requests.java \
 src/samples/AmazonKinesisFirehose/batchPutInput.txt \
 src/samples/AmazonKinesisFirehose/putRecordInput.txt \
 src/samples/AwsCloudFormation/CloudFormationSample.java \
 src/samples/AwsCloudFormation/CloudFormationSample.template; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

%build

# Tests require networking and unavailable test deps:
# com.github.tomakehurst:wiremock:1.55
# nl.jqno.equalsverifier:equalsverifier:1.7.5
%mvn_build -sf

%install
%mvn_install

%files -f .mfiles-aws-java-sdk
%doc src/samples/AmazonKinesis

%files acm -f .mfiles-aws-java-sdk-acm
%files api-gateway -f .mfiles-aws-java-sdk-api-gateway
%files applicationautoscaling -f .mfiles-aws-java-sdk-applicationautoscaling
%files autoscaling -f .mfiles-aws-java-sdk-autoscaling
%files bom -f .mfiles-aws-java-sdk-bom
%doc LICENSE.txt NOTICE.txt

%files cloudformation -f .mfiles-aws-java-sdk-cloudformation
%doc src/samples/AwsCloudFormation

%files cloudfront -f .mfiles-aws-java-sdk-cloudfront
%files cloudhsm -f .mfiles-aws-java-sdk-cloudhsm
%files cloudsearch -f .mfiles-aws-java-sdk-cloudsearch
%files cloudtrail -f .mfiles-aws-java-sdk-cloudtrail
%files cloudwatch -f .mfiles-aws-java-sdk-cloudwatch
%files cloudwatchmetrics -f .mfiles-aws-java-sdk-cloudwatchmetrics
#%% files code-generator -f .mfiles-aws-java-sdk-code-generator
%files codecommit -f .mfiles-aws-java-sdk-codecommit
%files codedeploy -f .mfiles-aws-java-sdk-codedeploy
#%% files codegen-maven-plugin -f .mfiles-aws-java-sdk-codegen-maven-plugin
%files codepipeline -f .mfiles-aws-java-sdk-codepipeline
%files cognitoidentity -f .mfiles-aws-java-sdk-cognitoidentity
%files cognitoidp -f .mfiles-aws-java-sdk-cognitoidp
%files cognitosync -f .mfiles-aws-java-sdk-cognitosync
%files config -f .mfiles-aws-java-sdk-config
%files core -f .mfiles-aws-java-sdk-core
%doc README.md
%doc LICENSE.txt NOTICE.txt

%files datapipeline -f .mfiles-aws-java-sdk-datapipeline
%files devicefarm -f .mfiles-aws-java-sdk-devicefarm
%files directconnect -f .mfiles-aws-java-sdk-directconnect
%files directory -f .mfiles-aws-java-sdk-directory
%files discovery -f .mfiles-aws-java-sdk-discovery
%files dms -f .mfiles-aws-java-sdk-dms
%files dynamodb -f .mfiles-aws-java-sdk-dynamodb
%doc src/samples/AmazonDynamoDB*

%files ec2 -f .mfiles-aws-java-sdk-ec2
%doc src/samples/AmazonEC2*

%files ecr -f .mfiles-aws-java-sdk-ecr
%files ecs -f .mfiles-aws-java-sdk-ecs
%files efs -f .mfiles-aws-java-sdk-efs
%files elasticache -f .mfiles-aws-java-sdk-elasticache
%files elasticbeanstalk -f .mfiles-aws-java-sdk-elasticbeanstalk
%files elasticloadbalancing -f .mfiles-aws-java-sdk-elasticloadbalancing
%files elasticsearch -f .mfiles-aws-java-sdk-elasticsearch
%files elastictranscoder -f .mfiles-aws-java-sdk-elastictranscoder
%files emr -f .mfiles-aws-java-sdk-emr
%files events -f .mfiles-aws-java-sdk-events
%files gamelift -f .mfiles-aws-java-sdk-gamelift
%files glacier -f .mfiles-aws-java-sdk-glacier
%files iam -f .mfiles-aws-java-sdk-iam
%files importexport -f .mfiles-aws-java-sdk-importexport
%files inspector -f .mfiles-aws-java-sdk-inspector
%files iot -f .mfiles-aws-java-sdk-iot
%files kinesis -f .mfiles-aws-java-sdk-kinesis
%doc src/samples/AmazonKinesisFirehose
# src/samples/AmazonKinesis require not available https://github.com/awslabs/amazon-kinesis-client

%files kms -f .mfiles-aws-java-sdk-kms
%files lambda -f .mfiles-aws-java-sdk-lambda
%files logs -f .mfiles-aws-java-sdk-logs
%files machinelearning -f .mfiles-aws-java-sdk-machinelearning
%files marketplacecommerceanalytics -f .mfiles-aws-java-sdk-marketplacecommerceanalytics
%files marketplacemeteringservice -f .mfiles-aws-java-sdk-marketplacemeteringservice
%files opsworks -f .mfiles-aws-java-sdk-opsworks
%files pom -f .mfiles-aws-java-sdk-pom
%doc LICENSE.txt NOTICE.txt

%files rds -f .mfiles-aws-java-sdk-rds
%files redshift -f .mfiles-aws-java-sdk-redshift
%files route53 -f .mfiles-aws-java-sdk-route53
%files s3 -f .mfiles-aws-java-sdk-s3
%doc src/samples/AmazonS3*

%files ses -f .mfiles-aws-java-sdk-ses
%doc src/samples/AmazonSimpleEmailService

%files simpledb -f .mfiles-aws-java-sdk-simpledb
%doc src/samples/AwsConsoleApp

%files simpleworkflow -f .mfiles-aws-java-sdk-simpleworkflow
%files sns -f .mfiles-aws-java-sdk-sns
%files sqs -f .mfiles-aws-java-sdk-sqs
%doc src/samples/AmazonSimpleQueueService

%files ssm -f .mfiles-aws-java-sdk-ssm
%files storagegateway -f .mfiles-aws-java-sdk-storagegateway
%files sts -f .mfiles-aws-java-sdk-sts
%files support -f .mfiles-aws-java-sdk-support
#%% files swf-libraries -f .mfiles-aws-java-sdk-swf-libraries
#%% doc src/samples/AwsFlowFramework
%files test-utils -f .mfiles-aws-java-sdk-test-utils
%files waf -f .mfiles-aws-java-sdk-waf
%files workspaces -f .mfiles-aws-java-sdk-workspaces

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.11.3-alt1_2jpp8
- new version

