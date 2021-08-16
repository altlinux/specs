%define        gemname train-aws

Name:          gem-train-aws
Version:       0.2.16
Release:       alt1
Summary:       AWS API Transport for Train
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/inspec/train-aws
Vcs:           https://github.com/inspec/train-aws.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(aws-sdk-apigateway) >= 1.0 gem(aws-sdk-apigateway) < 2
BuildRequires: gem(aws-sdk-apigatewayv2) >= 1.0 gem(aws-sdk-apigatewayv2) < 2
BuildRequires: gem(aws-sdk-applicationautoscaling) >= 1.46 gem(aws-sdk-applicationautoscaling) < 1.52
BuildRequires: gem(aws-sdk-athena) >= 1.0 gem(aws-sdk-athena) < 2
BuildRequires: gem(aws-sdk-autoscaling) >= 1.22 gem(aws-sdk-autoscaling) < 1.64
BuildRequires: gem(aws-sdk-batch) >= 1.36 gem(aws-sdk-batch) < 1.48
BuildRequires: gem(aws-sdk-budgets) >= 1.0 gem(aws-sdk-budgets) < 2
BuildRequires: gem(aws-sdk-cloudformation) >= 1.0 gem(aws-sdk-cloudformation) < 2
BuildRequires: gem(aws-sdk-cloudfront) >= 1.0 gem(aws-sdk-cloudfront) < 2
BuildRequires: gem(aws-sdk-cloudhsm) >= 1.0 gem(aws-sdk-cloudhsm) < 2
BuildRequires: gem(aws-sdk-cloudhsmv2) >= 1.0 gem(aws-sdk-cloudhsmv2) < 2
BuildRequires: gem(aws-sdk-cloudtrail) >= 1.8 gem(aws-sdk-cloudtrail) < 2
BuildRequires: gem(aws-sdk-cloudwatch) >= 1.13 gem(aws-sdk-cloudwatch) < 2
BuildRequires: gem(aws-sdk-cloudwatchevents) >= 1.36 gem(aws-sdk-cloudwatchevents) < 1.47
BuildRequires: gem(aws-sdk-cloudwatchlogs) >= 1.13 gem(aws-sdk-cloudwatchlogs) < 2
BuildRequires: gem(aws-sdk-codecommit) >= 1.0 gem(aws-sdk-codecommit) < 2
BuildRequires: gem(aws-sdk-codedeploy) >= 1.0 gem(aws-sdk-codedeploy) < 2
BuildRequires: gem(aws-sdk-codepipeline) >= 1.0 gem(aws-sdk-codepipeline) < 2
BuildRequires: gem(aws-sdk-cognitoidentity) >= 1.26 gem(aws-sdk-cognitoidentity) < 1.32
BuildRequires: gem(aws-sdk-cognitoidentityprovider) >= 1.46 gem(aws-sdk-cognitoidentityprovider) < 1.54
BuildRequires: gem(aws-sdk-configservice) >= 1.21 gem(aws-sdk-configservice) < 2
BuildRequires: gem(aws-sdk-core) >= 3.0 gem(aws-sdk-core) < 4
BuildRequires: gem(aws-sdk-costandusagereportservice) >= 1.6 gem(aws-sdk-costandusagereportservice) < 2
BuildRequires: gem(aws-sdk-databasemigrationservice) >= 1.42 gem(aws-sdk-databasemigrationservice) < 1.54
BuildRequires: gem(aws-sdk-dynamodb) >= 1.31 gem(aws-sdk-dynamodb) < 2
BuildRequires: gem(aws-sdk-ec2) >= 1.70 gem(aws-sdk-ec2) < 2
BuildRequires: gem(aws-sdk-ecr) >= 1.18 gem(aws-sdk-ecr) < 2
BuildRequires: gem(aws-sdk-ecrpublic) >= 1.3 gem(aws-sdk-ecrpublic) < 2
BuildRequires: gem(aws-sdk-ecs) >= 1.30 gem(aws-sdk-ecs) < 2
BuildRequires: gem(aws-sdk-efs) >= 1.0 gem(aws-sdk-efs) < 2
BuildRequires: gem(aws-sdk-eks) >= 1.9 gem(aws-sdk-eks) < 2
BuildRequires: gem(aws-sdk-elasticache) >= 1.0 gem(aws-sdk-elasticache) < 2
BuildRequires: gem(aws-sdk-elasticbeanstalk) >= 1.0 gem(aws-sdk-elasticbeanstalk) < 2
BuildRequires: gem(aws-sdk-elasticloadbalancing) >= 1.8 gem(aws-sdk-elasticloadbalancing) < 2
BuildRequires: gem(aws-sdk-elasticloadbalancingv2) >= 1.0 gem(aws-sdk-elasticloadbalancingv2) < 2
BuildRequires: gem(aws-sdk-elasticsearchservice) >= 1.0 gem(aws-sdk-elasticsearchservice) < 2
BuildRequires: gem(aws-sdk-eventbridge) >= 1.24.0 gem(aws-sdk-eventbridge) < 1.25
BuildRequires: gem(aws-sdk-firehose) >= 1.0 gem(aws-sdk-firehose) < 2
BuildRequires: gem(aws-sdk-glue) >= 1.71 gem(aws-sdk-glue) < 1.89
BuildRequires: gem(aws-sdk-guardduty) >= 1.31 gem(aws-sdk-guardduty) < 2
BuildRequires: gem(aws-sdk-iam) >= 1.13 gem(aws-sdk-iam) < 2
BuildRequires: gem(aws-sdk-kafka) >= 1.0 gem(aws-sdk-kafka) < 2
BuildRequires: gem(aws-sdk-kinesis) >= 1.0 gem(aws-sdk-kinesis) < 2
BuildRequires: gem(aws-sdk-kms) >= 1.13 gem(aws-sdk-kms) < 2
BuildRequires: gem(aws-sdk-lambda) >= 1.0 gem(aws-sdk-lambda) < 2
BuildRequires: gem(aws-sdk-organizations) >= 1.17 gem(aws-sdk-organizations) < 1.60
BuildRequires: gem(aws-sdk-ram) >= 1.21 gem(aws-sdk-ram) < 1.27
BuildRequires: gem(aws-sdk-rds) >= 1.43 gem(aws-sdk-rds) < 2
BuildRequires: gem(aws-sdk-redshift) >= 1.0 gem(aws-sdk-redshift) < 2
BuildRequires: gem(aws-sdk-route53) >= 1.0 gem(aws-sdk-route53) < 2
BuildRequires: gem(aws-sdk-route53domains) >= 1.0 gem(aws-sdk-route53domains) < 2
BuildRequires: gem(aws-sdk-route53resolver) >= 1.0 gem(aws-sdk-route53resolver) < 2
BuildRequires: gem(aws-sdk-s3) >= 1.30 gem(aws-sdk-s3) < 2
BuildRequires: gem(aws-sdk-secretsmanager) >= 1.42 gem(aws-sdk-secretsmanager) < 1.47
BuildRequires: gem(aws-sdk-securityhub) >= 1.0 gem(aws-sdk-securityhub) < 2
BuildRequires: gem(aws-sdk-servicecatalog) >= 1.48 gem(aws-sdk-servicecatalog) < 1.61
BuildRequires: gem(aws-sdk-ses) >= 1.0 gem(aws-sdk-ses) < 2
BuildRequires: gem(aws-sdk-shield) >= 1.30 gem(aws-sdk-shield) < 2
BuildRequires: gem(aws-sdk-sms) >= 1.0 gem(aws-sdk-sms) < 2
BuildRequires: gem(aws-sdk-sns) >= 1.9 gem(aws-sdk-sns) < 2
BuildRequires: gem(aws-sdk-sqs) >= 1.10 gem(aws-sdk-sqs) < 2
BuildRequires: gem(aws-sdk-ssm) >= 1.0 gem(aws-sdk-ssm) < 2
BuildRequires: gem(aws-sdk-states) >= 1.35 gem(aws-sdk-states) < 1.40
BuildRequires: gem(aws-sdk-transfer) >= 1.26 gem(aws-sdk-transfer) < 1.35

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(aws-sdk-apigateway) >= 1.0 gem(aws-sdk-apigateway) < 2
Requires:      gem(aws-sdk-apigatewayv2) >= 1.0 gem(aws-sdk-apigatewayv2) < 2
Requires:      gem(aws-sdk-applicationautoscaling) >= 1.46 gem(aws-sdk-applicationautoscaling) < 1.52
Requires:      gem(aws-sdk-athena) >= 1.0 gem(aws-sdk-athena) < 2
Requires:      gem(aws-sdk-autoscaling) >= 1.22 gem(aws-sdk-autoscaling) < 1.64
Requires:      gem(aws-sdk-batch) >= 1.36 gem(aws-sdk-batch) < 1.48
Requires:      gem(aws-sdk-budgets) >= 1.0 gem(aws-sdk-budgets) < 2
Requires:      gem(aws-sdk-cloudformation) >= 1.0 gem(aws-sdk-cloudformation) < 2
Requires:      gem(aws-sdk-cloudfront) >= 1.0 gem(aws-sdk-cloudfront) < 2
Requires:      gem(aws-sdk-cloudhsm) >= 1.0 gem(aws-sdk-cloudhsm) < 2
Requires:      gem(aws-sdk-cloudhsmv2) >= 1.0 gem(aws-sdk-cloudhsmv2) < 2
Requires:      gem(aws-sdk-cloudtrail) >= 1.8 gem(aws-sdk-cloudtrail) < 2
Requires:      gem(aws-sdk-cloudwatch) >= 1.13 gem(aws-sdk-cloudwatch) < 2
Requires:      gem(aws-sdk-cloudwatchevents) >= 1.36 gem(aws-sdk-cloudwatchevents) < 1.47
Requires:      gem(aws-sdk-cloudwatchlogs) >= 1.13 gem(aws-sdk-cloudwatchlogs) < 2
Requires:      gem(aws-sdk-codecommit) >= 1.0 gem(aws-sdk-codecommit) < 2
Requires:      gem(aws-sdk-codedeploy) >= 1.0 gem(aws-sdk-codedeploy) < 2
Requires:      gem(aws-sdk-codepipeline) >= 1.0 gem(aws-sdk-codepipeline) < 2
Requires:      gem(aws-sdk-cognitoidentity) >= 1.26 gem(aws-sdk-cognitoidentity) < 1.32
Requires:      gem(aws-sdk-cognitoidentityprovider) >= 1.46 gem(aws-sdk-cognitoidentityprovider) < 1.54
Requires:      gem(aws-sdk-configservice) >= 1.21 gem(aws-sdk-configservice) < 2
Requires:      gem(aws-sdk-core) >= 3.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sdk-costandusagereportservice) >= 1.6 gem(aws-sdk-costandusagereportservice) < 2
Requires:      gem(aws-sdk-databasemigrationservice) >= 1.42 gem(aws-sdk-databasemigrationservice) < 1.54
Requires:      gem(aws-sdk-dynamodb) >= 1.31 gem(aws-sdk-dynamodb) < 2
Requires:      gem(aws-sdk-ec2) >= 1.70 gem(aws-sdk-ec2) < 2
Requires:      gem(aws-sdk-ecr) >= 1.18 gem(aws-sdk-ecr) < 2
Requires:      gem(aws-sdk-ecrpublic) >= 1.3 gem(aws-sdk-ecrpublic) < 2
Requires:      gem(aws-sdk-ecs) >= 1.30 gem(aws-sdk-ecs) < 2
Requires:      gem(aws-sdk-efs) >= 1.0 gem(aws-sdk-efs) < 2
Requires:      gem(aws-sdk-eks) >= 1.9 gem(aws-sdk-eks) < 2
Requires:      gem(aws-sdk-elasticache) >= 1.0 gem(aws-sdk-elasticache) < 2
Requires:      gem(aws-sdk-elasticbeanstalk) >= 1.0 gem(aws-sdk-elasticbeanstalk) < 2
Requires:      gem(aws-sdk-elasticloadbalancing) >= 1.8 gem(aws-sdk-elasticloadbalancing) < 2
Requires:      gem(aws-sdk-elasticloadbalancingv2) >= 1.0 gem(aws-sdk-elasticloadbalancingv2) < 2
Requires:      gem(aws-sdk-elasticsearchservice) >= 1.0 gem(aws-sdk-elasticsearchservice) < 2
Requires:      gem(aws-sdk-eventbridge) >= 1.24.0 gem(aws-sdk-eventbridge) < 1.25
Requires:      gem(aws-sdk-firehose) >= 1.0 gem(aws-sdk-firehose) < 2
Requires:      gem(aws-sdk-glue) >= 1.71 gem(aws-sdk-glue) < 1.89
Requires:      gem(aws-sdk-guardduty) >= 1.31 gem(aws-sdk-guardduty) < 2
Requires:      gem(aws-sdk-iam) >= 1.13 gem(aws-sdk-iam) < 2
Requires:      gem(aws-sdk-kafka) >= 1.0 gem(aws-sdk-kafka) < 2
Requires:      gem(aws-sdk-kinesis) >= 1.0 gem(aws-sdk-kinesis) < 2
Requires:      gem(aws-sdk-kms) >= 1.13 gem(aws-sdk-kms) < 2
Requires:      gem(aws-sdk-lambda) >= 1.0 gem(aws-sdk-lambda) < 2
Requires:      gem(aws-sdk-organizations) >= 1.17 gem(aws-sdk-organizations) < 1.60
Requires:      gem(aws-sdk-ram) >= 1.21 gem(aws-sdk-ram) < 1.27
Requires:      gem(aws-sdk-rds) >= 1.43 gem(aws-sdk-rds) < 2
Requires:      gem(aws-sdk-redshift) >= 1.0 gem(aws-sdk-redshift) < 2
Requires:      gem(aws-sdk-route53) >= 1.0 gem(aws-sdk-route53) < 2
Requires:      gem(aws-sdk-route53domains) >= 1.0 gem(aws-sdk-route53domains) < 2
Requires:      gem(aws-sdk-route53resolver) >= 1.0 gem(aws-sdk-route53resolver) < 2
Requires:      gem(aws-sdk-s3) >= 1.30 gem(aws-sdk-s3) < 2
Requires:      gem(aws-sdk-secretsmanager) >= 1.42 gem(aws-sdk-secretsmanager) < 1.47
Requires:      gem(aws-sdk-securityhub) >= 1.0 gem(aws-sdk-securityhub) < 2
Requires:      gem(aws-sdk-servicecatalog) >= 1.48 gem(aws-sdk-servicecatalog) < 1.61
Requires:      gem(aws-sdk-ses) >= 1.0 gem(aws-sdk-ses) < 2
Requires:      gem(aws-sdk-shield) >= 1.30 gem(aws-sdk-shield) < 2
Requires:      gem(aws-sdk-sms) >= 1.0 gem(aws-sdk-sms) < 2
Requires:      gem(aws-sdk-sns) >= 1.9 gem(aws-sdk-sns) < 2
Requires:      gem(aws-sdk-sqs) >= 1.10 gem(aws-sdk-sqs) < 2
Requires:      gem(aws-sdk-ssm) >= 1.0 gem(aws-sdk-ssm) < 2
Requires:      gem(aws-sdk-states) >= 1.35 gem(aws-sdk-states) < 1.40
Requires:      gem(aws-sdk-transfer) >= 1.26 gem(aws-sdk-transfer) < 1.35
Provides:      gem(train-aws) = 0.2.16


%description
Allows applications using Train to speak to AWS; handles authentication,
cacheing, and SDK dependency management.


%package       -n gem-train-aws-doc
Version:       0.2.16
Release:       alt1
Summary:       AWS API Transport for Train documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train-aws
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train-aws) = 0.2.16

%description   -n gem-train-aws-doc
AWS API Transport for Train documentation files.

Allows applications using Train to speak to AWS; handles authentication,
cacheing, and SDK dependency management.

%description   -n gem-train-aws-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета train-aws.


%package       -n gem-train-aws-devel
Version:       0.2.16
Release:       alt1
Summary:       AWS API Transport for Train development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train-aws
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(train-aws) = 0.2.16

%description   -n gem-train-aws-devel
AWS API Transport for Train development package.

Allows applications using Train to speak to AWS; handles authentication,
cacheing, and SDK dependency management.

%description   -n gem-train-aws-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета train-aws.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-train-aws-doc
%ruby_gemdocdir

%files         -n gem-train-aws-devel


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.16-alt1
- + packaged gem with Ruby Policy 2.0
