%define        gemname train-aws

Name:          gem-train-aws
Version:       0.2.25
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
%if_with check
BuildRequires: gem(train-core) >= 3.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(m) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(chefstyle) >= 0
BuildRequires: gem(aws-sdk-alexaforbusiness) >= 1.0
BuildRequires: gem(aws-sdk-amplify) >= 1.32.0
BuildRequires: gem(aws-sdk-apigateway) >= 1.0
BuildRequires: gem(aws-sdk-apigatewayv2) >= 1.0
BuildRequires: gem(aws-sdk-applicationautoscaling) >= 1.46
BuildRequires: gem(aws-sdk-athena) >= 1.0
BuildRequires: gem(aws-sdk-autoscaling) >= 1.22
BuildRequires: gem(aws-sdk-batch) >= 1.36
BuildRequires: gem(aws-sdk-budgets) >= 1.0
BuildRequires: gem(aws-sdk-cloudformation) >= 1.0
BuildRequires: gem(aws-sdk-cloudfront) >= 1.0
BuildRequires: gem(aws-sdk-cloudhsm) >= 1.0
BuildRequires: gem(aws-sdk-cloudhsmv2) >= 1.0
BuildRequires: gem(aws-sdk-cloudtrail) >= 1.8
BuildRequires: gem(aws-sdk-cloudwatch) >= 1.13
BuildRequires: gem(aws-sdk-cloudwatchevents) >= 1.36
BuildRequires: gem(aws-sdk-cloudwatchlogs) >= 1.13
BuildRequires: gem(aws-sdk-codecommit) >= 1.0
BuildRequires: gem(aws-sdk-codedeploy) >= 1.0
BuildRequires: gem(aws-sdk-codepipeline) >= 1.0
BuildRequires: gem(aws-sdk-cognitoidentity) >= 1.26
BuildRequires: gem(aws-sdk-cognitoidentityprovider) >= 1.46
BuildRequires: gem(aws-sdk-configservice) >= 1.21
BuildRequires: gem(aws-sdk-core) >= 3.0
BuildRequires: gem(aws-sdk-costandusagereportservice) >= 1.6
BuildRequires: gem(aws-sdk-databasemigrationservice) >= 1.42
BuildRequires: gem(aws-sdk-dynamodb) >= 1.31
BuildRequires: gem(aws-sdk-ec2) >= 1.70
BuildRequires: gem(aws-sdk-ecr) >= 1.18
BuildRequires: gem(aws-sdk-ecrpublic) >= 1.3
BuildRequires: gem(aws-sdk-ecs) >= 1.30
BuildRequires: gem(aws-sdk-efs) >= 1.0
BuildRequires: gem(aws-sdk-eks) >= 1.9
BuildRequires: gem(aws-sdk-elasticache) >= 1.0
BuildRequires: gem(aws-sdk-elasticbeanstalk) >= 1.0
BuildRequires: gem(aws-sdk-elasticloadbalancing) >= 1.8
BuildRequires: gem(aws-sdk-elasticloadbalancingv2) >= 1.0
BuildRequires: gem(aws-sdk-elasticsearchservice) >= 1.0
BuildRequires: gem(aws-sdk-emr) >= 1.53.0
BuildRequires: gem(aws-sdk-eventbridge) >= 1.24.0
BuildRequires: gem(aws-sdk-firehose) >= 1.0
BuildRequires: gem(aws-sdk-glue) >= 1.71
BuildRequires: gem(aws-sdk-guardduty) >= 1.31
BuildRequires: gem(aws-sdk-iam) >= 1.13
BuildRequires: gem(aws-sdk-kafka) >= 1.0
BuildRequires: gem(aws-sdk-kinesis) >= 1.0
BuildRequires: gem(aws-sdk-kms) >= 1.13
BuildRequires: gem(aws-sdk-lambda) >= 1.0
BuildRequires: gem(aws-sdk-mq) >= 1.40.0
BuildRequires: gem(aws-sdk-organizations) >= 1.17
BuildRequires: gem(aws-sdk-networkmanager) >= 1.13.0
BuildRequires: gem(aws-sdk-networkfirewall) >= 1.6.0
BuildRequires: gem(aws-sdk-ram) >= 1.21
BuildRequires: gem(aws-sdk-rds) >= 1.43
BuildRequires: gem(aws-sdk-redshift) >= 1.0
BuildRequires: gem(aws-sdk-route53) >= 1.0
BuildRequires: gem(aws-sdk-route53domains) >= 1.0
BuildRequires: gem(aws-sdk-route53resolver) >= 1.0
BuildRequires: gem(aws-sdk-s3) >= 1.30
BuildRequires: gem(aws-sdk-s3control) >= 1.43.0
BuildRequires: gem(aws-sdk-secretsmanager) >= 1.42
BuildRequires: gem(aws-sdk-securityhub) >= 1.0
BuildRequires: gem(aws-sdk-servicecatalog) >= 1.48
BuildRequires: gem(aws-sdk-ses) >= 1.41.0
BuildRequires: gem(aws-sdk-shield) >= 1.30
BuildRequires: gem(aws-sdk-signer) >= 1.32.0
BuildRequires: gem(aws-sdk-simpledb) >= 1.29.0
BuildRequires: gem(aws-sdk-sms) >= 1.0
BuildRequires: gem(aws-sdk-sns) >= 1.9
BuildRequires: gem(aws-sdk-sqs) >= 1.10
BuildRequires: gem(aws-sdk-ssm) >= 1.0
BuildRequires: gem(aws-sdk-states) >= 1.35
BuildRequires: gem(aws-sdk-synthetics) >= 1.19.0
BuildRequires: gem(aws-sdk-transfer) >= 1.26
BuildRequires: gem(aws-sdk-waf) >= 1.43.0
BuildConflicts: gem(train-core) >= 4
BuildConflicts: gem(aws-sdk-alexaforbusiness) >= 2
BuildConflicts: gem(aws-sdk-amplify) >= 2
BuildConflicts: gem(aws-sdk-apigateway) >= 2
BuildConflicts: gem(aws-sdk-apigatewayv2) >= 2
BuildConflicts: gem(aws-sdk-applicationautoscaling) >= 2
BuildConflicts: gem(aws-sdk-athena) >= 2
BuildConflicts: gem(aws-sdk-autoscaling) >= 2
BuildConflicts: gem(aws-sdk-batch) >= 2
BuildConflicts: gem(aws-sdk-budgets) >= 2
BuildConflicts: gem(aws-sdk-cloudformation) >= 2
BuildConflicts: gem(aws-sdk-cloudfront) >= 2
BuildConflicts: gem(aws-sdk-cloudhsm) >= 2
BuildConflicts: gem(aws-sdk-cloudhsmv2) >= 2
BuildConflicts: gem(aws-sdk-cloudtrail) >= 2
BuildConflicts: gem(aws-sdk-cloudwatch) >= 2
BuildConflicts: gem(aws-sdk-cloudwatchevents) >= 2
BuildConflicts: gem(aws-sdk-cloudwatchlogs) >= 2
BuildConflicts: gem(aws-sdk-codecommit) >= 2
BuildConflicts: gem(aws-sdk-codedeploy) >= 2
BuildConflicts: gem(aws-sdk-codepipeline) >= 2
BuildConflicts: gem(aws-sdk-cognitoidentity) >= 2
BuildConflicts: gem(aws-sdk-cognitoidentityprovider) >= 2
BuildConflicts: gem(aws-sdk-configservice) >= 2
BuildConflicts: gem(aws-sdk-core) >= 4
BuildConflicts: gem(aws-sdk-costandusagereportservice) >= 2
BuildConflicts: gem(aws-sdk-databasemigrationservice) >= 2
BuildConflicts: gem(aws-sdk-dynamodb) >= 2
BuildConflicts: gem(aws-sdk-ec2) >= 2
BuildConflicts: gem(aws-sdk-ecr) >= 2
BuildConflicts: gem(aws-sdk-ecrpublic) >= 2
BuildConflicts: gem(aws-sdk-ecs) >= 2
BuildConflicts: gem(aws-sdk-efs) >= 2
BuildConflicts: gem(aws-sdk-eks) >= 2
BuildConflicts: gem(aws-sdk-elasticache) >= 2
BuildConflicts: gem(aws-sdk-elasticbeanstalk) >= 2
BuildConflicts: gem(aws-sdk-elasticloadbalancing) >= 2
BuildConflicts: gem(aws-sdk-elasticloadbalancingv2) >= 2
BuildConflicts: gem(aws-sdk-elasticsearchservice) >= 2
BuildConflicts: gem(aws-sdk-emr) >= 2
BuildConflicts: gem(aws-sdk-eventbridge) >= 2
BuildConflicts: gem(aws-sdk-firehose) >= 2
BuildConflicts: gem(aws-sdk-glue) >= 2
BuildConflicts: gem(aws-sdk-guardduty) >= 2
BuildConflicts: gem(aws-sdk-iam) >= 2
BuildConflicts: gem(aws-sdk-kafka) >= 2
BuildConflicts: gem(aws-sdk-kinesis) >= 2
BuildConflicts: gem(aws-sdk-kms) >= 2
BuildConflicts: gem(aws-sdk-lambda) >= 2
BuildConflicts: gem(aws-sdk-mq) >= 2
BuildConflicts: gem(aws-sdk-organizations) >= 2
BuildConflicts: gem(aws-sdk-ram) >= 2
BuildConflicts: gem(aws-sdk-rds) >= 2
BuildConflicts: gem(aws-sdk-redshift) >= 2
BuildConflicts: gem(aws-sdk-route53) >= 2
BuildConflicts: gem(aws-sdk-route53domains) >= 2
BuildConflicts: gem(aws-sdk-route53resolver) >= 2
BuildConflicts: gem(aws-sdk-s3) >= 2
BuildConflicts: gem(aws-sdk-s3control) >= 2
BuildConflicts: gem(aws-sdk-secretsmanager) >= 2
BuildConflicts: gem(aws-sdk-securityhub) >= 2
BuildConflicts: gem(aws-sdk-servicecatalog) >= 2
BuildConflicts: gem(aws-sdk-ses) >= 2
BuildConflicts: gem(aws-sdk-shield) >= 2
BuildConflicts: gem(aws-sdk-signer) >= 2
BuildConflicts: gem(aws-sdk-simpledb) >= 2
BuildConflicts: gem(aws-sdk-sms) >= 2
BuildConflicts: gem(aws-sdk-sns) >= 2
BuildConflicts: gem(aws-sdk-sqs) >= 2
BuildConflicts: gem(aws-sdk-ssm) >= 2
BuildConflicts: gem(aws-sdk-states) >= 2
BuildConflicts: gem(aws-sdk-synthetics) >= 2
BuildConflicts: gem(aws-sdk-transfer) >= 2
BuildConflicts: gem(aws-sdk-waf) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency aws-sdk-amplify >= 1.33,aws-sdk-amplify < 2
%ruby_use_gem_dependency aws-sdk-applicationautoscaling >= 1.52,aws-sdk-applicationautoscaling < 2
%ruby_use_gem_dependency aws-sdk-autoscaling >= 1.64,aws-sdk-autoscaling < 2
%ruby_use_gem_dependency aws-sdk-batch >= 1.48,aws-sdk-batch < 2
%ruby_use_gem_dependency aws-sdk-cloudwatchevents >= 1.47,aws-sdk-cloudwatchevents < 2
%ruby_use_gem_dependency aws-sdk-cognitoidentity >= 1.32,aws-sdk-cognitoidentity < 2
%ruby_use_gem_dependency aws-sdk-cognitoidentityprovider >= 1.54,aws-sdk-cognitoidentityprovider < 2
%ruby_use_gem_dependency aws-sdk-databasemigrationservice >= 1.54,aws-sdk-databasemigrationservice < 2
%ruby_use_gem_dependency aws-sdk-emr >= 1.54,aws-sdk-emr < 2
%ruby_use_gem_dependency aws-sdk-eventbridge >= 1.25,aws-sdk-eventbridge < 2
%ruby_use_gem_dependency aws-sdk-glue >= 1.89,aws-sdk-glue < 2
%ruby_use_gem_dependency aws-sdk-mq >= 1.41,aws-sdk-mq < 2
%ruby_use_gem_dependency aws-sdk-organizations >= 1.60,aws-sdk-organizations < 2
%ruby_use_gem_dependency aws-sdk-ram >= 1.27,aws-sdk-ram < 2
%ruby_use_gem_dependency aws-sdk-s3control >= 1.44,aws-sdk-s3control < 2
%ruby_use_gem_dependency aws-sdk-secretsmanager >= 1.47,aws-sdk-secretsmanager < 2
%ruby_use_gem_dependency aws-sdk-servicecatalog >= 1.61,aws-sdk-servicecatalog < 2
%ruby_use_gem_dependency aws-sdk-ses >= 1.42,aws-sdk-ses < 2
%ruby_use_gem_dependency aws-sdk-signer >= 1.33,aws-sdk-signer < 2
%ruby_use_gem_dependency aws-sdk-simpledb >= 1.30,aws-sdk-simpledb < 2
%ruby_use_gem_dependency aws-sdk-states >= 1.40,aws-sdk-states < 2
%ruby_use_gem_dependency aws-sdk-synthetics >= 1.20,aws-sdk-synthetics < 2
%ruby_use_gem_dependency aws-sdk-transfer >= 1.35,aws-sdk-transfer < 2
%ruby_use_gem_dependency aws-sdk-waf >= 1.44,aws-sdk-waf < 2
Requires:      gem(aws-sdk-alexaforbusiness) >= 1.0
Requires:      gem(aws-sdk-amplify) >= 1.32.0
Requires:      gem(aws-sdk-apigateway) >= 1.0
Requires:      gem(aws-sdk-apigatewayv2) >= 1.0
Requires:      gem(aws-sdk-applicationautoscaling) >= 1.46
Requires:      gem(aws-sdk-athena) >= 1.0
Requires:      gem(aws-sdk-autoscaling) >= 1.22
Requires:      gem(aws-sdk-batch) >= 1.36
Requires:      gem(aws-sdk-budgets) >= 1.0
Requires:      gem(aws-sdk-cloudformation) >= 1.0
Requires:      gem(aws-sdk-cloudfront) >= 1.0
Requires:      gem(aws-sdk-cloudhsm) >= 1.0
Requires:      gem(aws-sdk-cloudhsmv2) >= 1.0
Requires:      gem(aws-sdk-cloudtrail) >= 1.8
Requires:      gem(aws-sdk-cloudwatch) >= 1.13
Requires:      gem(aws-sdk-cloudwatchevents) >= 1.36
Requires:      gem(aws-sdk-cloudwatchlogs) >= 1.13
Requires:      gem(aws-sdk-codecommit) >= 1.0
Requires:      gem(aws-sdk-codedeploy) >= 1.0
Requires:      gem(aws-sdk-codepipeline) >= 1.0
Requires:      gem(aws-sdk-cognitoidentity) >= 1.26
Requires:      gem(aws-sdk-cognitoidentityprovider) >= 1.46
Requires:      gem(aws-sdk-configservice) >= 1.21
Requires:      gem(aws-sdk-core) >= 3.0
Requires:      gem(aws-sdk-costandusagereportservice) >= 1.6
Requires:      gem(aws-sdk-databasemigrationservice) >= 1.42
Requires:      gem(aws-sdk-dynamodb) >= 1.31
Requires:      gem(aws-sdk-ec2) >= 1.70
Requires:      gem(aws-sdk-ecr) >= 1.18
Requires:      gem(aws-sdk-ecrpublic) >= 1.3
Requires:      gem(aws-sdk-ecs) >= 1.30
Requires:      gem(aws-sdk-efs) >= 1.0
Requires:      gem(aws-sdk-eks) >= 1.9
Requires:      gem(aws-sdk-elasticache) >= 1.0
Requires:      gem(aws-sdk-elasticbeanstalk) >= 1.0
Requires:      gem(aws-sdk-elasticloadbalancing) >= 1.8
Requires:      gem(aws-sdk-elasticloadbalancingv2) >= 1.0
Requires:      gem(aws-sdk-elasticsearchservice) >= 1.0
Requires:      gem(aws-sdk-emr) >= 1.53.0
Requires:      gem(aws-sdk-eventbridge) >= 1.24.0
Requires:      gem(aws-sdk-firehose) >= 1.0
Requires:      gem(aws-sdk-glue) >= 1.71
Requires:      gem(aws-sdk-guardduty) >= 1.31
Requires:      gem(aws-sdk-iam) >= 1.13
Requires:      gem(aws-sdk-kafka) >= 1.0
Requires:      gem(aws-sdk-kinesis) >= 1.0
Requires:      gem(aws-sdk-kms) >= 1.13
Requires:      gem(aws-sdk-lambda) >= 1.0
Requires:      gem(aws-sdk-mq) >= 1.40.0
Requires:      gem(aws-sdk-organizations) >= 1.17
Requires:      gem(aws-sdk-networkmanager) >= 1.13.0
Requires:      gem(aws-sdk-networkfirewall) >= 1.6.0
Requires:      gem(aws-sdk-ram) >= 1.21
Requires:      gem(aws-sdk-rds) >= 1.43
Requires:      gem(aws-sdk-redshift) >= 1.0
Requires:      gem(aws-sdk-route53) >= 1.0
Requires:      gem(aws-sdk-route53domains) >= 1.0
Requires:      gem(aws-sdk-route53resolver) >= 1.0
Requires:      gem(aws-sdk-s3) >= 1.30
Requires:      gem(aws-sdk-s3control) >= 1.43.0
Requires:      gem(aws-sdk-secretsmanager) >= 1.42
Requires:      gem(aws-sdk-securityhub) >= 1.0
Requires:      gem(aws-sdk-servicecatalog) >= 1.48
Requires:      gem(aws-sdk-ses) >= 1.41.0
Requires:      gem(aws-sdk-shield) >= 1.30
Requires:      gem(aws-sdk-signer) >= 1.32.0
Requires:      gem(aws-sdk-simpledb) >= 1.29.0
Requires:      gem(aws-sdk-sms) >= 1.0
Requires:      gem(aws-sdk-sns) >= 1.9
Requires:      gem(aws-sdk-sqs) >= 1.10
Requires:      gem(aws-sdk-ssm) >= 1.0
Requires:      gem(aws-sdk-states) >= 1.35
Requires:      gem(aws-sdk-synthetics) >= 1.19.0
Requires:      gem(aws-sdk-transfer) >= 1.26
Requires:      gem(aws-sdk-waf) >= 1.43.0
Conflicts:     gem(aws-sdk-alexaforbusiness) >= 2
Conflicts:     gem(aws-sdk-amplify) >= 2
Conflicts:     gem(aws-sdk-apigateway) >= 2
Conflicts:     gem(aws-sdk-apigatewayv2) >= 2
Conflicts:     gem(aws-sdk-applicationautoscaling) >= 2
Conflicts:     gem(aws-sdk-athena) >= 2
Conflicts:     gem(aws-sdk-autoscaling) >= 2
Conflicts:     gem(aws-sdk-batch) >= 2
Conflicts:     gem(aws-sdk-budgets) >= 2
Conflicts:     gem(aws-sdk-cloudformation) >= 2
Conflicts:     gem(aws-sdk-cloudfront) >= 2
Conflicts:     gem(aws-sdk-cloudhsm) >= 2
Conflicts:     gem(aws-sdk-cloudhsmv2) >= 2
Conflicts:     gem(aws-sdk-cloudtrail) >= 2
Conflicts:     gem(aws-sdk-cloudwatch) >= 2
Conflicts:     gem(aws-sdk-cloudwatchevents) >= 2
Conflicts:     gem(aws-sdk-cloudwatchlogs) >= 2
Conflicts:     gem(aws-sdk-codecommit) >= 2
Conflicts:     gem(aws-sdk-codedeploy) >= 2
Conflicts:     gem(aws-sdk-codepipeline) >= 2
Conflicts:     gem(aws-sdk-cognitoidentity) >= 2
Conflicts:     gem(aws-sdk-cognitoidentityprovider) >= 2
Conflicts:     gem(aws-sdk-configservice) >= 2
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sdk-costandusagereportservice) >= 2
Conflicts:     gem(aws-sdk-databasemigrationservice) >= 2
Conflicts:     gem(aws-sdk-dynamodb) >= 2
Conflicts:     gem(aws-sdk-ec2) >= 2
Conflicts:     gem(aws-sdk-ecr) >= 2
Conflicts:     gem(aws-sdk-ecrpublic) >= 2
Conflicts:     gem(aws-sdk-ecs) >= 2
Conflicts:     gem(aws-sdk-efs) >= 2
Conflicts:     gem(aws-sdk-eks) >= 2
Conflicts:     gem(aws-sdk-elasticache) >= 2
Conflicts:     gem(aws-sdk-elasticbeanstalk) >= 2
Conflicts:     gem(aws-sdk-elasticloadbalancing) >= 2
Conflicts:     gem(aws-sdk-elasticloadbalancingv2) >= 2
Conflicts:     gem(aws-sdk-elasticsearchservice) >= 2
Conflicts:     gem(aws-sdk-emr) >= 2
Conflicts:     gem(aws-sdk-eventbridge) >= 2
Conflicts:     gem(aws-sdk-firehose) >= 2
Conflicts:     gem(aws-sdk-glue) >= 2
Conflicts:     gem(aws-sdk-guardduty) >= 2
Conflicts:     gem(aws-sdk-iam) >= 2
Conflicts:     gem(aws-sdk-kafka) >= 2
Conflicts:     gem(aws-sdk-kinesis) >= 2
Conflicts:     gem(aws-sdk-kms) >= 2
Conflicts:     gem(aws-sdk-lambda) >= 2
Conflicts:     gem(aws-sdk-mq) >= 2
Conflicts:     gem(aws-sdk-organizations) >= 2
Conflicts:     gem(aws-sdk-ram) >= 2
Conflicts:     gem(aws-sdk-rds) >= 2
Conflicts:     gem(aws-sdk-redshift) >= 2
Conflicts:     gem(aws-sdk-route53) >= 2
Conflicts:     gem(aws-sdk-route53domains) >= 2
Conflicts:     gem(aws-sdk-route53resolver) >= 2
Conflicts:     gem(aws-sdk-s3) >= 2
Conflicts:     gem(aws-sdk-s3control) >= 2
Conflicts:     gem(aws-sdk-secretsmanager) >= 2
Conflicts:     gem(aws-sdk-securityhub) >= 2
Conflicts:     gem(aws-sdk-servicecatalog) >= 2
Conflicts:     gem(aws-sdk-ses) >= 2
Conflicts:     gem(aws-sdk-shield) >= 2
Conflicts:     gem(aws-sdk-signer) >= 2
Conflicts:     gem(aws-sdk-simpledb) >= 2
Conflicts:     gem(aws-sdk-sms) >= 2
Conflicts:     gem(aws-sdk-sns) >= 2
Conflicts:     gem(aws-sdk-sqs) >= 2
Conflicts:     gem(aws-sdk-ssm) >= 2
Conflicts:     gem(aws-sdk-states) >= 2
Conflicts:     gem(aws-sdk-synthetics) >= 2
Conflicts:     gem(aws-sdk-transfer) >= 2
Conflicts:     gem(aws-sdk-waf) >= 2
Provides:      gem(train-aws) = 0.2.25


%description
Allows applications using Train to speak to AWS; handles authentication,
cacheing, and SDK dependency management.


%package       -n gem-train-aws-doc
Version:       0.2.25
Release:       alt1
Summary:       AWS API Transport for Train documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train-aws
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train-aws) = 0.2.25

%description   -n gem-train-aws-doc
AWS API Transport for Train documentation files.

Allows applications using Train to speak to AWS; handles authentication,
cacheing, and SDK dependency management.

%description   -n gem-train-aws-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета train-aws.


%package       -n gem-train-aws-devel
Version:       0.2.25
Release:       alt1
Summary:       AWS API Transport for Train development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train-aws
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(train-aws) = 0.2.25
Requires:      gem(train-core) >= 3.0
Requires:      gem(pry) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(m) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(chefstyle) >= 0
Conflicts:     gem(train-core) >= 4

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
* Wed Feb 15 2023 Pavel Skrylev <majioa@altlinux.org> 0.2.25-alt1
- ^ 0.2.16 -> 0.2.25

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.16-alt1
- + packaged gem with Ruby Policy 2.0
