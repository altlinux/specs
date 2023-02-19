%define        gemname aws-sdk

Name:          gem-aws-sdk
Epoch:         1
Version:       3.1.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://aws.amazon.com/ru/sdk-for-ruby/
Vcs:           https://github.com/aws/aws-sdk-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: ragel
BuildRequires: /usr/bin/ruby-ll
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(http-2) >= 0
BuildRequires: gem(jmespath) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(nokogiri) >= 1.6.8.1
BuildRequires: gem(oga) >= 0
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(libxml-ruby) >= 0
BuildRequires: gem(oj) >= 0
BuildRequires: gem(ox) >= 0
BuildRequires: gem(addressable) >= 0
BuildRequires: gem(cucumber) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(multipart-post) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(mustache) >= 0
BuildRequires: gem(rdiscount) >= 0
BuildRequires: gem(yard) >= 0.9.26
BuildRequires: gem(yard-sitemap) >= 1.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rubocop) >= 0.81.0
BuildRequires: gem(jmespath) >= 1.6.1
BuildConflicts: gem(yard-sitemap) >= 2
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(jmespath) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(rake) >= 0
Requires:      gem(http-2) >= 0
Requires:      gem(jmespath) >= 0
Requires:      gem(json) >= 0
Requires:      gem(nokogiri) >= 1.6.8.1
Requires:      gem(oga) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(libxml-ruby) >= 0
Requires:      gem(oj) >= 0
Requires:      gem(ox) >= 0
Requires:      gem(addressable) >= 0
# Requires:      gem(cucumber) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(multipart-post) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(kramdown) >= 0
Requires:      gem(mustache) >= 0
Requires:      gem(rdiscount) >= 0
Requires:      gem(yard) >= 0.9.26
Requires:      gem(yard-sitemap) >= 1.0
Requires:      gem(pry) >= 0
Requires:      gem(rubocop) >= 0.81.0
Requires:      gem(aws-sdk-resources) >= 3
Conflicts:     gem(yard-sitemap) >= 2
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(aws-sdk-resources) >= 4
Obsoletes:     ruby-aws-sdk < %EVR
Provides:      ruby-aws-sdk = %EVR
Provides:      gem(aws-sdk) = 3.1.0


%description
The official AWS SDK for Ruby. Provides both resource oriented interfaces and
API clients for AWS services.


%package       -n gem-aws-sigv2
Version:       1.1.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(aws-sigv2) = 1.1.0

%description   -n gem-aws-sigv2
Amazon Web Services Signature Version 2 signing library. Generates sigv2
signature for HTTP requests.


%package       -n gem-aws-sigv2-doc
Version:       1.1.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sigv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sigv2) = 1.1.0

%description   -n gem-aws-sigv2-doc
The official AWS SDK for Ruby documentation files.

Amazon Web Services Signature Version 2 signing library. Generates sigv2
signature for HTTP requests.

%description   -n gem-aws-sigv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sigv2.


%package       -n gem-aws-sigv2-devel
Version:       1.1.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sigv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sigv2) = 1.1.0

%description   -n gem-aws-sigv2-devel
The official AWS SDK for Ruby development package.

Amazon Web Services Signature Version 2 signing library. Generates sigv2
signature for HTTP requests.

%description   -n gem-aws-sigv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sigv2.


%package       -n gem-aws-sigv4
Version:       1.5.2
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-eventstream) >= 1.0.2
Conflicts:     gem(aws-eventstream) >= 2
Provides:      gem(aws-sigv4) = 1.5.2

%description   -n gem-aws-sigv4
Amazon Web Services Signature Version 4 signing library. Generates sigv4
signature for HTTP requests.


%package       -n gem-aws-sigv4-doc
Version:       1.5.2
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sigv4
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sigv4) = 1.5.2

%description   -n gem-aws-sigv4-doc
The official AWS SDK for Ruby documentation files.

Amazon Web Services Signature Version 4 signing library. Generates sigv4
signature for HTTP requests.

%description   -n gem-aws-sigv4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sigv4.


%package       -n gem-aws-sigv4-devel
Version:       1.5.2
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sigv4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sigv4) = 1.5.2

%description   -n gem-aws-sigv4-devel
The official AWS SDK for Ruby development package.

Amazon Web Services Signature Version 4 signing library. Generates sigv4
signature for HTTP requests.

%description   -n gem-aws-sigv4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sigv4.


%package       -n gem-aws-sdk-mq
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-mq) = 1.49.0

%description   -n gem-aws-sdk-mq
Official AWS Ruby gem for AmazonMQ. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mq-doc
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mq
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mq) = 1.49.0

%description   -n gem-aws-sdk-mq-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AmazonMQ. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mq-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mq.


%package       -n gem-aws-sdk-mq-devel
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mq
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mq) = 1.49.0

%description   -n gem-aws-sdk-mq-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AmazonMQ. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mq-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mq.


%package       -n gem-aws-sdk-pi
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-pi) = 1.42.0

%description   -n gem-aws-sdk-pi
Official AWS Ruby gem for AWS Performance Insights (AWS PI). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-pi-doc
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-pi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-pi) = 1.42.0

%description   -n gem-aws-sdk-pi-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Performance Insights (AWS PI). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-pi.


%package       -n gem-aws-sdk-pi-devel
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-pi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-pi) = 1.42.0

%description   -n gem-aws-sdk-pi-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Performance Insights (AWS PI). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-pi.


%package       -n gem-aws-sdk-s3
Version:       1.119.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kms) >= 1
Requires:      gem(aws-sigv4) >= 1.4
Requires:      gem(aws-sdk-core) >= 3.165.0
Conflicts:     gem(aws-sdk-kms) >= 2
Conflicts:     gem(aws-sigv4) >= 2
Conflicts:     gem(aws-sdk-core) >= 4
Provides:      gem(aws-sdk-s3) = 1.119.0

%description   -n gem-aws-sdk-s3
Official AWS Ruby gem for Amazon Simple Storage Service (Amazon S3). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-s3-doc
Version:       1.119.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-s3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-s3) = 1.119.0

%description   -n gem-aws-sdk-s3-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Simple Storage Service (Amazon S3). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-s3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-s3.


%package       -n gem-aws-sdk-s3-devel
Version:       1.119.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-s3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-s3) = 1.119.0

%description   -n gem-aws-sdk-s3-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Simple Storage Service (Amazon S3). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-s3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-s3.


%package       -n gem-aws-sdk-acm
Version:       1.55.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-acm) = 1.55.0

%description   -n gem-aws-sdk-acm
Official AWS Ruby gem for AWS Certificate Manager (ACM). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-acm-doc
Version:       1.55.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-acm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-acm) = 1.55.0

%description   -n gem-aws-sdk-acm-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-acm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-acm.


%package       -n gem-aws-sdk-acm-devel
Version:       1.55.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-acm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-acm) = 1.55.0

%description   -n gem-aws-sdk-acm-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-acm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-acm.


%package       -n gem-aws-sdk-dax
Version:       1.41.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-dax) = 1.41.0

%description   -n gem-aws-sdk-dax
Official AWS Ruby gem for Amazon DynamoDB Accelerator (DAX) (Amazon DAX). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-dax-doc
Version:       1.41.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-dax
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-dax) = 1.41.0

%description   -n gem-aws-sdk-dax-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon DynamoDB Accelerator (DAX) (Amazon DAX). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-dax-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-dax.


%package       -n gem-aws-sdk-dax-devel
Version:       1.41.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-dax
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-dax) = 1.41.0

%description   -n gem-aws-sdk-dax-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon DynamoDB Accelerator (DAX) (Amazon DAX). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-dax-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-dax.


%package       -n gem-aws-sdk-dlm
Version:       1.54.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-dlm) = 1.54.0

%description   -n gem-aws-sdk-dlm
Official AWS Ruby gem for Amazon Data Lifecycle Manager (Amazon DLM). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-dlm-doc
Version:       1.54.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-dlm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-dlm) = 1.54.0

%description   -n gem-aws-sdk-dlm-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Data Lifecycle Manager (Amazon DLM). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-dlm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-dlm.


%package       -n gem-aws-sdk-dlm-devel
Version:       1.54.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-dlm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-dlm) = 1.54.0

%description   -n gem-aws-sdk-dlm-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Data Lifecycle Manager (Amazon DLM). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-dlm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-dlm.


%package       -n gem-aws-sdk-drs
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - drs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-drs) = 1.10.0

%description   -n gem-aws-sdk-drs
Official AWS Ruby gem for Elastic Disaster Recovery Service (drs). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-drs-doc
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - drs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-drs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-drs) = 1.10.0

%description   -n gem-aws-sdk-drs-doc
AWS SDK for Ruby - drs documentation files.

Official AWS Ruby gem for Elastic Disaster Recovery Service (drs). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-drs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-drs.


%package       -n gem-aws-sdk-drs-devel
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - drs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-drs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-drs) = 1.10.0

%description   -n gem-aws-sdk-drs-devel
AWS SDK for Ruby - drs development package.

Official AWS Ruby gem for Elastic Disaster Recovery Service (drs). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-drs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-drs.


%package       -n gem-aws-sdk-ebs
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ebs) = 1.28.0

%description   -n gem-aws-sdk-ebs
Official AWS Ruby gem for Amazon Elastic Block Store (Amazon EBS). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ebs-doc
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ebs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ebs) = 1.28.0

%description   -n gem-aws-sdk-ebs-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Elastic Block Store (Amazon EBS). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ebs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ebs.


%package       -n gem-aws-sdk-ebs-devel
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ebs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ebs) = 1.28.0

%description   -n gem-aws-sdk-ebs-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Elastic Block Store (Amazon EBS). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ebs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ebs.


%package       -n gem-aws-sdk-ec2
Version:       1.361.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sigv4) >= 1.1
Requires:      gem(aws-sdk-core) >= 3.165.0
Conflicts:     gem(aws-sigv4) >= 2
Conflicts:     gem(aws-sdk-core) >= 4
Provides:      gem(aws-sdk-ec2) = 1.361.0

%description   -n gem-aws-sdk-ec2
Official AWS Ruby gem for Amazon Elastic Compute Cloud (Amazon EC2). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ec2-doc
Version:       1.361.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ec2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ec2) = 1.361.0

%description   -n gem-aws-sdk-ec2-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Elastic Compute Cloud (Amazon EC2). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ec2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ec2.


%package       -n gem-aws-sdk-ec2-devel
Version:       1.361.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ec2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ec2) = 1.361.0

%description   -n gem-aws-sdk-ec2-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Elastic Compute Cloud (Amazon EC2). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ec2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ec2.


%package       -n gem-aws-sdk-ecr
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ecr) = 1.58.0

%description   -n gem-aws-sdk-ecr
Official AWS Ruby gem for Amazon EC2 Container Registry (Amazon ECR). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ecr-doc
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ecr
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ecr) = 1.58.0

%description   -n gem-aws-sdk-ecr-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon EC2 Container Registry (Amazon ECR). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ecr-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ecr.


%package       -n gem-aws-sdk-ecr-devel
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ecr
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ecr) = 1.58.0

%description   -n gem-aws-sdk-ecr-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon EC2 Container Registry (Amazon ECR). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ecr-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ecr.


%package       -n gem-aws-sdk-ecs
Version:       1.110.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ecs) = 1.110.0

%description   -n gem-aws-sdk-ecs
Official AWS Ruby gem for Amazon EC2 Container Service (Amazon ECS). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ecs-doc
Version:       1.110.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ecs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ecs) = 1.110.0

%description   -n gem-aws-sdk-ecs-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon EC2 Container Service (Amazon ECS). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ecs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ecs.


%package       -n gem-aws-sdk-ecs-devel
Version:       1.110.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ecs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ecs) = 1.110.0

%description   -n gem-aws-sdk-ecs-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon EC2 Container Service (Amazon ECS). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ecs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ecs.


%package       -n gem-aws-sdk-efs
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-efs) = 1.58.0

%description   -n gem-aws-sdk-efs
Official AWS Ruby gem for Amazon Elastic File System (EFS). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-efs-doc
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-efs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-efs) = 1.58.0

%description   -n gem-aws-sdk-efs-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Elastic File System (EFS). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-efs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-efs.


%package       -n gem-aws-sdk-efs-devel
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-efs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-efs) = 1.58.0

%description   -n gem-aws-sdk-efs-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Elastic File System (EFS). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-efs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-efs.


%package       -n gem-aws-sdk-eks
Version:       1.83.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-eks) = 1.83.0

%description   -n gem-aws-sdk-eks
Official AWS Ruby gem for Amazon Elastic Kubernetes Service (Amazon EKS). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-eks-doc
Version:       1.83.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-eks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-eks) = 1.83.0

%description   -n gem-aws-sdk-eks-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Elastic Kubernetes Service (Amazon EKS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-eks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-eks.


%package       -n gem-aws-sdk-eks-devel
Version:       1.83.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-eks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-eks) = 1.83.0

%description   -n gem-aws-sdk-eks-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Elastic Kubernetes Service (Amazon EKS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-eks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-eks.


%package       -n gem-aws-sdk-emr
Version:       1.65.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-emr) = 1.65.0

%description   -n gem-aws-sdk-emr
Official AWS Ruby gem for Amazon Elastic MapReduce (Amazon EMR). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-emr-doc
Version:       1.65.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-emr
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-emr) = 1.65.0

%description   -n gem-aws-sdk-emr-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Elastic MapReduce (Amazon EMR). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-emr-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-emr.


%package       -n gem-aws-sdk-emr-devel
Version:       1.65.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-emr
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-emr) = 1.65.0

%description   -n gem-aws-sdk-emr-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Elastic MapReduce (Amazon EMR). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-emr-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-emr.


%package       -n gem-aws-sdk-fis
Version:       1.16.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-fis) = 1.16.0

%description   -n gem-aws-sdk-fis
Official AWS Ruby gem for AWS Fault Injection Simulator (FIS). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-fis-doc
Version:       1.16.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-fis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-fis) = 1.16.0

%description   -n gem-aws-sdk-fis-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Fault Injection Simulator (FIS). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-fis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-fis.


%package       -n gem-aws-sdk-fis-devel
Version:       1.16.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-fis
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-fis) = 1.16.0

%description   -n gem-aws-sdk-fis-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Fault Injection Simulator (FIS). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-fis-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-fis.


%package       -n gem-aws-sdk-fms
Version:       1.55.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-fms) = 1.55.0

%description   -n gem-aws-sdk-fms
Official AWS Ruby gem for Firewall Management Service (FMS). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-fms-doc
Version:       1.55.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-fms
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-fms) = 1.55.0

%description   -n gem-aws-sdk-fms-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Firewall Management Service (FMS). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-fms-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-fms.


%package       -n gem-aws-sdk-fms-devel
Version:       1.55.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-fms
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-fms) = 1.55.0

%description   -n gem-aws-sdk-fms-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Firewall Management Service (FMS). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-fms-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-fms.


%package       -n gem-aws-sdk-fsx
Version:       1.64.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-fsx) = 1.64.0

%description   -n gem-aws-sdk-fsx
Official AWS Ruby gem for Amazon FSx. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-fsx-doc
Version:       1.64.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-fsx
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-fsx) = 1.64.0

%description   -n gem-aws-sdk-fsx-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon FSx. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-fsx-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-fsx.


%package       -n gem-aws-sdk-fsx-devel
Version:       1.64.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-fsx
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-fsx) = 1.64.0

%description   -n gem-aws-sdk-fsx-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon FSx. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-fsx-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-fsx.


%package       -n gem-aws-sdk-iam
Version:       1.74.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iam) = 1.74.0

%description   -n gem-aws-sdk-iam
Official AWS Ruby gem for AWS Identity and Access Management (IAM). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-iam-doc
Version:       1.74.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iam
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iam) = 1.74.0

%description   -n gem-aws-sdk-iam-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Identity and Access Management (IAM). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iam-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iam.


%package       -n gem-aws-sdk-iam-devel
Version:       1.74.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iam
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iam) = 1.74.0

%description   -n gem-aws-sdk-iam-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Identity and Access Management (IAM). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iam-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iam.


%package       -n gem-aws-sdk-iot
Version:       1.99.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iot) = 1.99.0

%description   -n gem-aws-sdk-iot
Official AWS Ruby gem for AWS IoT. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-iot-doc
Version:       1.99.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iot
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iot) = 1.99.0

%description   -n gem-aws-sdk-iot-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS IoT. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iot-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iot.


%package       -n gem-aws-sdk-iot-devel
Version:       1.99.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iot
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iot) = 1.99.0

%description   -n gem-aws-sdk-iot-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS IoT. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iot-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iot.


%package       -n gem-aws-sdk-ivs
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ivs) = 1.26.0

%description   -n gem-aws-sdk-ivs
Official AWS Ruby gem for Amazon Interactive Video Service (Amazon IVS). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ivs-doc
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ivs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ivs) = 1.26.0

%description   -n gem-aws-sdk-ivs-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Interactive Video Service (Amazon IVS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ivs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ivs.


%package       -n gem-aws-sdk-ivs-devel
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ivs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ivs) = 1.26.0

%description   -n gem-aws-sdk-ivs-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Interactive Video Service (Amazon IVS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ivs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ivs.


%package       -n gem-aws-sdk-kms
Version:       1.62.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-kms) = 1.62.0

%description   -n gem-aws-sdk-kms
Official AWS Ruby gem for AWS Key Management Service (KMS). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kms-doc
Version:       1.62.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kms
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kms) = 1.62.0

%description   -n gem-aws-sdk-kms-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Key Management Service (KMS). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kms-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kms.


%package       -n gem-aws-sdk-kms-devel
Version:       1.62.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kms
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kms) = 1.62.0

%description   -n gem-aws-sdk-kms-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Key Management Service (KMS). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kms-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kms.


%package       -n gem-aws-sdk-lex
Version:       1.47.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-lex) = 1.47.0

%description   -n gem-aws-sdk-lex
Official AWS Ruby gem for Amazon Lex Runtime Service. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-lex-doc
Version:       1.47.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lex
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lex) = 1.47.0

%description   -n gem-aws-sdk-lex-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-lex-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lex.


%package       -n gem-aws-sdk-lex-devel
Version:       1.47.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lex
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lex) = 1.47.0

%description   -n gem-aws-sdk-lex-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-lex-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lex.


%package       -n gem-aws-sdk-mgn
Version:       1.17.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-mgn) = 1.17.0

%description   -n gem-aws-sdk-mgn
Official AWS Ruby gem for Application Migration Service (mgn). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mgn-doc
Version:       1.17.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mgn
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mgn) = 1.17.0

%description   -n gem-aws-sdk-mgn-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Application Migration Service (mgn). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mgn-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mgn.


%package       -n gem-aws-sdk-mgn-devel
Version:       1.17.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mgn
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mgn) = 1.17.0

%description   -n gem-aws-sdk-mgn-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Application Migration Service (mgn). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mgn-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mgn.


%package       -n gem-aws-sdk-oam
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudWatch Observability Access Manager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-oam) = 1.1.0

%description   -n gem-aws-sdk-oam
Official AWS Ruby gem for CloudWatch Observability Access Manager. This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-oam-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudWatch Observability Access Manager documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-oam
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-oam) = 1.1.0

%description   -n gem-aws-sdk-oam-doc
AWS SDK for Ruby - CloudWatch Observability Access Manager documentation
files.

Official AWS Ruby gem for CloudWatch Observability Access Manager. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-oam-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-oam.


%package       -n gem-aws-sdk-oam-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudWatch Observability Access Manager development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-oam
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-oam) = 1.1.0

%description   -n gem-aws-sdk-oam-devel
AWS SDK for Ruby - CloudWatch Observability Access Manager development
package.

Official AWS Ruby gem for CloudWatch Observability Access Manager. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-oam-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-oam.


%package       -n gem-aws-sdk-ram
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ram) = 1.42.0

%description   -n gem-aws-sdk-ram
Official AWS Ruby gem for AWS Resource Access Manager (RAM). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ram-doc
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ram
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ram) = 1.42.0

%description   -n gem-aws-sdk-ram-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Resource Access Manager (RAM). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ram-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ram.


%package       -n gem-aws-sdk-ram-devel
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ram
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ram) = 1.42.0

%description   -n gem-aws-sdk-ram-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Resource Access Manager (RAM). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ram-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ram.


%package       -n gem-aws-sdk-rds
Version:       1.171.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sigv4) >= 1.1
Requires:      gem(aws-sdk-core) >= 3.165.0
Conflicts:     gem(aws-sigv4) >= 2
Conflicts:     gem(aws-sdk-core) >= 4
Provides:      gem(aws-sdk-rds) = 1.171.0

%description   -n gem-aws-sdk-rds
Official AWS Ruby gem for Amazon Relational Database Service (Amazon RDS). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-rds-doc
Version:       1.171.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-rds
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-rds) = 1.171.0

%description   -n gem-aws-sdk-rds-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Relational Database Service (Amazon RDS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-rds-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-rds.


%package       -n gem-aws-sdk-rds-devel
Version:       1.171.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-rds
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-rds) = 1.171.0

%description   -n gem-aws-sdk-rds-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Relational Database Service (Amazon RDS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-rds-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-rds.


%package       -n gem-aws-sdk-ses
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ses) = 1.49.0

%description   -n gem-aws-sdk-ses
Official AWS Ruby gem for Amazon Simple Email Service (Amazon SES). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ses-doc
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ses
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ses) = 1.49.0

%description   -n gem-aws-sdk-ses-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Simple Email Service (Amazon SES). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ses-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ses.


%package       -n gem-aws-sdk-ses-devel
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ses
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ses) = 1.49.0

%description   -n gem-aws-sdk-ses-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Simple Email Service (Amazon SES). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ses-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ses.


%package       -n gem-aws-sdk-sms
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-sms) = 1.42.0

%description   -n gem-aws-sdk-sms
Official AWS Ruby gem for AWS Server Migration Service (SMS). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-sms-doc
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sms
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sms) = 1.42.0

%description   -n gem-aws-sdk-sms-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Server Migration Service (SMS). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sms-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sms.


%package       -n gem-aws-sdk-sms-devel
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sms
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sms) = 1.42.0

%description   -n gem-aws-sdk-sms-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Server Migration Service (SMS). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sms-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sms.


%package       -n gem-aws-sdk-sns
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-sns) = 1.58.0

%description   -n gem-aws-sdk-sns
Official AWS Ruby gem for Amazon Simple Notification Service (Amazon SNS). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-sns-doc
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sns
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sns) = 1.58.0

%description   -n gem-aws-sdk-sns-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Simple Notification Service (Amazon SNS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sns-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sns.


%package       -n gem-aws-sdk-sns-devel
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sns
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sns) = 1.58.0

%description   -n gem-aws-sdk-sns-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Simple Notification Service (Amazon SNS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sns-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sns.


%package       -n gem-aws-sdk-sqs
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-sqs) = 1.53.0

%description   -n gem-aws-sdk-sqs
Official AWS Ruby gem for Amazon Simple Queue Service (Amazon SQS). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-sqs-doc
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sqs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sqs) = 1.53.0

%description   -n gem-aws-sdk-sqs-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Simple Queue Service (Amazon SQS). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sqs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sqs.


%package       -n gem-aws-sdk-sqs-devel
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sqs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sqs) = 1.53.0

%description   -n gem-aws-sdk-sqs-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Simple Queue Service (Amazon SQS). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sqs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sqs.


%package       -n gem-aws-sdk-ssm
Version:       1.148.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ssm) = 1.148.0

%description   -n gem-aws-sdk-ssm
Official AWS Ruby gem for Amazon Simple Systems Manager (SSM) (Amazon SSM). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ssm-doc
Version:       1.148.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ssm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ssm) = 1.148.0

%description   -n gem-aws-sdk-ssm-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Simple Systems Manager (SSM) (Amazon SSM). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ssm.


%package       -n gem-aws-sdk-ssm-devel
Version:       1.148.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ssm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ssm) = 1.148.0

%description   -n gem-aws-sdk-ssm-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Simple Systems Manager (SSM) (Amazon SSM). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ssm.


%package       -n gem-aws-sdk-sso
Version:       1.11.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.105.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-sso) = 1.11.0

%description   -n gem-aws-sdk-sso
Official AWS Ruby gem for AWS Single Sign-On (SSO). SSO is included as part of
aws-sdk-core - this gem is an alias for loading aws-sdk-core.


%package       -n gem-aws-sdk-sso-doc
Version:       1.11.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sso
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sso) = 1.11.0

%description   -n gem-aws-sdk-sso-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Single Sign-On (SSO). SSO is included as part of
aws-sdk-core - this gem is an alias for loading aws-sdk-core.

%description   -n gem-aws-sdk-sso-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sso.


%package       -n gem-aws-sdk-sso-devel
Version:       1.11.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sso
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sso) = 1.11.0

%description   -n gem-aws-sdk-sso-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Single Sign-On (SSO). SSO is included as part of
aws-sdk-core - this gem is an alias for loading aws-sdk-core.

%description   -n gem-aws-sdk-sso-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sso.


%package       -n gem-aws-sdk-sts
Version:       1.9.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.110.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-sts) = 1.9.0

%description   -n gem-aws-sdk-sts
Official AWS Ruby gem for AWS Security Token Service (STS). STS is included as
part of aws-sdk-core - this gem is an alias for loading aws-sdk-core.


%package       -n gem-aws-sdk-sts-doc
Version:       1.9.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sts
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sts) = 1.9.0

%description   -n gem-aws-sdk-sts-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Security Token Service (STS). STS is included as
part of aws-sdk-core - this gem is an alias for loading aws-sdk-core.

%description   -n gem-aws-sdk-sts-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sts.


%package       -n gem-aws-sdk-sts-devel
Version:       1.9.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sts
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sts) = 1.9.0

%description   -n gem-aws-sdk-sts-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Security Token Service (STS). STS is included as
part of aws-sdk-core - this gem is an alias for loading aws-sdk-core.

%description   -n gem-aws-sdk-sts-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sts.


%package       -n gem-aws-sdk-swf
Version:       1.38.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-swf) = 1.38.0

%description   -n gem-aws-sdk-swf
Official AWS Ruby gem for Amazon Simple Workflow Service (Amazon SWF). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-swf-doc
Version:       1.38.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-swf
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-swf) = 1.38.0

%description   -n gem-aws-sdk-swf-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Simple Workflow Service (Amazon SWF). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-swf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-swf.


%package       -n gem-aws-sdk-swf-devel
Version:       1.38.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-swf
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-swf) = 1.38.0

%description   -n gem-aws-sdk-swf-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Simple Workflow Service (Amazon SWF). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-swf-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-swf.


%package       -n gem-aws-sdk-waf
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-waf) = 1.49.0

%description   -n gem-aws-sdk-waf
Official AWS Ruby gem for AWS WAF (WAF). This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-waf-doc
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-waf
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-waf) = 1.49.0

%description   -n gem-aws-sdk-waf-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-waf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-waf.


%package       -n gem-aws-sdk-waf-devel
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-waf
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-waf) = 1.49.0

%description   -n gem-aws-sdk-waf-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-waf-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-waf.


%package       -n gem-aws-sdk-core
Version:       3.170.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jmespath) >= 1.6.1
Requires:      gem(aws-partitions) >= 1.651.0
Requires:      gem(aws-sigv4) >= 1.5
Requires:      gem(aws-eventstream) >= 1.0.2
Conflicts:     gem(jmespath) >= 2
Conflicts:     gem(aws-partitions) >= 2
Conflicts:     gem(aws-sigv4) >= 2
Conflicts:     gem(aws-eventstream) >= 2
Obsoletes:     aws-sdk-core < %EVR
Obsoletes:     ruby-aws-sdk-core < %EVR
Provides:      aws-sdk-core = %EVR
Provides:      ruby-aws-sdk-core = %EVR
Provides:      gem(aws-sdk-core) = 3.170.0

%description   -n gem-aws-sdk-core
Provides API clients for AWS. This gem is part of the official AWS SDK for Ruby.


%package       -n gem-aws-sdk-core-doc
Version:       3.170.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-core) = 3.170.0

%description   -n gem-aws-sdk-core-doc
The official AWS SDK for Ruby documentation files.

Provides API clients for AWS. This gem is part of the official AWS SDK for Ruby.

%description   -n gem-aws-sdk-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-core.


%package       -n gem-aws-sdk-core-devel
Version:       3.170.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) = 3.170.0

%description   -n gem-aws-sdk-core-devel
The official AWS SDK for Ruby development package.

Provides API clients for AWS. This gem is part of the official AWS SDK for Ruby.

%description   -n gem-aws-sdk-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-core.


%package       -n gem-aws-sdk-glue
Version:       1.129.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-glue) = 1.129.0

%description   -n gem-aws-sdk-glue
Official AWS Ruby gem for AWS Glue. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-glue-doc
Version:       1.129.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-glue
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-glue) = 1.129.0

%description   -n gem-aws-sdk-glue-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Glue. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-glue-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-glue.


%package       -n gem-aws-sdk-glue-devel
Version:       1.129.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-glue
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-glue) = 1.129.0

%description   -n gem-aws-sdk-glue-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Glue. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-glue-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-glue.


%package       -n gem-aws-sdk-mwaa
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-mwaa) = 1.19.0

%description   -n gem-aws-sdk-mwaa
Official AWS Ruby gem for AmazonMWAA. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mwaa-doc
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mwaa
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mwaa) = 1.19.0

%description   -n gem-aws-sdk-mwaa-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AmazonMWAA. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mwaa-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mwaa.


%package       -n gem-aws-sdk-mwaa-devel
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mwaa
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mwaa) = 1.19.0

%description   -n gem-aws-sdk-mwaa-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AmazonMWAA. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mwaa-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mwaa.


%package       -n gem-aws-sdk-qldb
Version:       1.27.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-qldb) = 1.27.0

%description   -n gem-aws-sdk-qldb
Official AWS Ruby gem for Amazon QLDB (QLDB). This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-qldb-doc
Version:       1.27.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-qldb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-qldb) = 1.27.0

%description   -n gem-aws-sdk-qldb-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-qldb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-qldb.


%package       -n gem-aws-sdk-qldb-devel
Version:       1.27.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-qldb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-qldb) = 1.27.0

%description   -n gem-aws-sdk-qldb-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-qldb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-qldb.


%package       -n gem-aws-sdk-xray
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-xray) = 1.51.0

%description   -n gem-aws-sdk-xray
Official AWS Ruby gem for AWS X-Ray. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-xray-doc
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-xray
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-xray) = 1.51.0

%description   -n gem-aws-sdk-xray-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS X-Ray. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-xray-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-xray.


%package       -n gem-aws-sdk-xray-devel
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-xray
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-xray) = 1.51.0

%description   -n gem-aws-sdk-xray-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS X-Ray. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-xray-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-xray.


%package       -n gem-aws-sdk-batch
Version:       1.67.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-batch) = 1.67.0

%description   -n gem-aws-sdk-batch
Official AWS Ruby gem for AWS Batch. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-batch-doc
Version:       1.67.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-batch
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-batch) = 1.67.0

%description   -n gem-aws-sdk-batch-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Batch. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-batch-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-batch.


%package       -n gem-aws-sdk-batch-devel
Version:       1.67.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-batch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-batch) = 1.67.0

%description   -n gem-aws-sdk-batch-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Batch. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-batch-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-batch.


%package       -n gem-aws-sdk-chime
Version:       1.70.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-chime) = 1.70.0

%description   -n gem-aws-sdk-chime
Official AWS Ruby gem for Amazon Chime. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-chime-doc
Version:       1.70.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-chime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-chime) = 1.70.0

%description   -n gem-aws-sdk-chime-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-chime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-chime.


%package       -n gem-aws-sdk-chime-devel
Version:       1.70.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-chime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-chime) = 1.70.0

%description   -n gem-aws-sdk-chime-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-chime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-chime.


%package       -n gem-aws-sdk-docdb
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-docdb) = 1.46.0

%description   -n gem-aws-sdk-docdb
Official AWS Ruby gem for Amazon DocumentDB with MongoDB compatibility (Amazon
DocDB). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-docdb-doc
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-docdb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-docdb) = 1.46.0

%description   -n gem-aws-sdk-docdb-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon DocumentDB with MongoDB compatibility (Amazon
DocDB). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-docdb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-docdb.


%package       -n gem-aws-sdk-docdb-devel
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-docdb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-docdb) = 1.46.0

%description   -n gem-aws-sdk-docdb-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon DocumentDB with MongoDB compatibility (Amazon
DocDB). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-docdb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-docdb.


%package       -n gem-aws-sdk-kafka
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-kafka) = 1.53.0

%description   -n gem-aws-sdk-kafka
Official AWS Ruby gem for Managed Streaming for Kafka (Kafka). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kafka-doc
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kafka
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kafka) = 1.53.0

%description   -n gem-aws-sdk-kafka-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Managed Streaming for Kafka (Kafka). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kafka-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kafka.


%package       -n gem-aws-sdk-kafka-devel
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kafka
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kafka) = 1.53.0

%description   -n gem-aws-sdk-kafka-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Managed Streaming for Kafka (Kafka). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kafka-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kafka.


%package       -n gem-aws-sdk-macie
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-macie) = 1.40.0

%description   -n gem-aws-sdk-macie
Official AWS Ruby gem for Amazon Macie. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-macie-doc
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-macie
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-macie) = 1.40.0

%description   -n gem-aws-sdk-macie-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-macie-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-macie.


%package       -n gem-aws-sdk-macie-devel
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-macie
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-macie) = 1.40.0

%description   -n gem-aws-sdk-macie-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-macie-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-macie.


%package       -n gem-aws-sdk-mturk
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-mturk) = 1.42.0

%description   -n gem-aws-sdk-mturk
Official AWS Ruby gem for Amazon Mechanical Turk (Amazon MTurk). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mturk-doc
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mturk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mturk) = 1.42.0

%description   -n gem-aws-sdk-mturk-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Mechanical Turk (Amazon MTurk). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mturk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mturk.


%package       -n gem-aws-sdk-mturk-devel
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mturk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mturk) = 1.42.0

%description   -n gem-aws-sdk-mturk-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Mechanical Turk (Amazon MTurk). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mturk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mturk.


%package       -n gem-aws-sdk-omics
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Omics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-omics) = 1.1.0

%description   -n gem-aws-sdk-omics
Official AWS Ruby gem for Amazon Omics. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-omics-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Omics documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-omics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-omics) = 1.1.0

%description   -n gem-aws-sdk-omics-doc
AWS SDK for Ruby - Amazon Omics documentation files.

%description   -n gem-aws-sdk-omics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-omics.


%package       -n gem-aws-sdk-omics-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Omics development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-omics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-omics) = 1.1.0

%description   -n gem-aws-sdk-omics-devel
AWS SDK for Ruby - Amazon Omics development package.

%description   -n gem-aws-sdk-omics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-omics.


%package       -n gem-aws-sdk-pipes
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EventBridge Pipes
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-pipes) = 1.1.0

%description   -n gem-aws-sdk-pipes
Official AWS Ruby gem for Amazon EventBridge Pipes. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-pipes-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EventBridge Pipes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-pipes
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-pipes) = 1.1.0

%description   -n gem-aws-sdk-pipes-doc
AWS SDK for Ruby - Amazon EventBridge Pipes documentation files.

%description   -n gem-aws-sdk-pipes-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-pipes.


%package       -n gem-aws-sdk-pipes-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EventBridge Pipes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-pipes
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-pipes) = 1.1.0

%description   -n gem-aws-sdk-pipes-devel
AWS SDK for Ruby - Amazon EventBridge Pipes development package.

%description   -n gem-aws-sdk-pipes-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-pipes.


%package       -n gem-aws-sdk-polly
Version:       1.64.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-polly) = 1.64.0

%description   -n gem-aws-sdk-polly
Official AWS Ruby gem for Amazon Polly. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-polly-doc
Version:       1.64.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-polly
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-polly) = 1.64.0

%description   -n gem-aws-sdk-polly-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-polly-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-polly.


%package       -n gem-aws-sdk-polly-devel
Version:       1.64.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-polly
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-polly) = 1.64.0

%description   -n gem-aws-sdk-polly-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-polly-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-polly.


%package       -n gem-aws-sdk-sesv2
Version:       1.31.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-sesv2) = 1.31.0

%description   -n gem-aws-sdk-sesv2
Official AWS Ruby gem for Amazon Simple Email Service (Amazon SES V2). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-sesv2-doc
Version:       1.31.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sesv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sesv2) = 1.31.0

%description   -n gem-aws-sdk-sesv2-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Simple Email Service (Amazon SES V2). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sesv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sesv2.


%package       -n gem-aws-sdk-sesv2-devel
Version:       1.31.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sesv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sesv2) = 1.31.0

%description   -n gem-aws-sdk-sesv2-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Simple Email Service (Amazon SES V2). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sesv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sesv2.


%package       -n gem-aws-sdk-wafv2
Version:       1.47.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-wafv2) = 1.47.0

%description   -n gem-aws-sdk-wafv2
Official AWS Ruby gem for AWS WAFV2 (WAFV2). This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-wafv2-doc
Version:       1.47.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-wafv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-wafv2) = 1.47.0

%description   -n gem-aws-sdk-wafv2-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-wafv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-wafv2.


%package       -n gem-aws-sdk-wafv2-devel
Version:       1.47.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-wafv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-wafv2) = 1.47.0

%description   -n gem-aws-sdk-wafv2-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-wafv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-wafv2.


%package       -n gem-aws-partitions
Version:       1.701.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(aws-partitions) = 1.701.0

%description   -n gem-aws-partitions
Provides interfaces to enumerate AWS partitions, regions, and services.


%package       -n gem-aws-partitions-doc
Version:       1.701.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-partitions
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-partitions) = 1.701.0

%description   -n gem-aws-partitions-doc
The official AWS SDK for Ruby documentation files.

Provides interfaces to enumerate AWS partitions, regions, and services.

%description   -n gem-aws-partitions-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-partitions.


%package       -n gem-aws-partitions-devel
Version:       1.701.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-partitions
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-partitions) = 1.701.0

%description   -n gem-aws-partitions-devel
The official AWS SDK for Ruby development package.

Provides interfaces to enumerate AWS partitions, regions, and services.

%description   -n gem-aws-partitions-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-partitions.


%package       -n gem-aws-sdk-acmpca
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-acmpca) = 1.53.0

%description   -n gem-aws-sdk-acmpca
Official AWS Ruby gem for AWS Certificate Manager Private Certificate Authority
(ACM-PCA). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-acmpca-doc
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-acmpca
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-acmpca) = 1.53.0

%description   -n gem-aws-sdk-acmpca-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Certificate Manager Private Certificate Authority
(ACM-PCA). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-acmpca-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-acmpca.


%package       -n gem-aws-sdk-acmpca-devel
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-acmpca
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-acmpca) = 1.53.0

%description   -n gem-aws-sdk-acmpca-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Certificate Manager Private Certificate Authority
(ACM-PCA). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-acmpca-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-acmpca.


%package       -n gem-aws-sdk-athena
Version:       1.61.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-athena) = 1.61.0

%description   -n gem-aws-sdk-athena
Official AWS Ruby gem for Amazon Athena. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-athena-doc
Version:       1.61.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-athena
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-athena) = 1.61.0

%description   -n gem-aws-sdk-athena-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-athena-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-athena.


%package       -n gem-aws-sdk-athena-devel
Version:       1.61.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-athena
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-athena) = 1.61.0

%description   -n gem-aws-sdk-athena-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-athena-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-athena.


%package       -n gem-aws-sdk-backup
Version:       1.48.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-backup) = 1.48.0

%description   -n gem-aws-sdk-backup
Official AWS Ruby gem for AWS Backup. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-backup-doc
Version:       1.48.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-backup
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-backup) = 1.48.0

%description   -n gem-aws-sdk-backup-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Backup. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-backup-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-backup.


%package       -n gem-aws-sdk-backup-devel
Version:       1.48.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-backup
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-backup) = 1.48.0

%description   -n gem-aws-sdk-backup-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Backup. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-backup-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-backup.


%package       -n gem-aws-sdk-braket
Version:       1.21.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-braket) = 1.21.0

%description   -n gem-aws-sdk-braket
Official AWS Ruby gem for Braket. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-braket-doc
Version:       1.21.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-braket
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-braket) = 1.21.0

%description   -n gem-aws-sdk-braket-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Braket. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-braket-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-braket.


%package       -n gem-aws-sdk-braket-devel
Version:       1.21.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-braket
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-braket) = 1.21.0

%description   -n gem-aws-sdk-braket-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Braket. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-braket-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-braket.


%package       -n gem-aws-sdk-cloud9
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cloud9) = 1.49.0

%description   -n gem-aws-sdk-cloud9
Official AWS Ruby gem for AWS Cloud9. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-cloud9-doc
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloud9
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloud9) = 1.49.0

%description   -n gem-aws-sdk-cloud9-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Cloud9. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloud9-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloud9.


%package       -n gem-aws-sdk-cloud9-devel
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloud9
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloud9) = 1.49.0

%description   -n gem-aws-sdk-cloud9-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Cloud9. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloud9-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloud9.


%package       -n gem-aws-sdk-health
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-health) = 1.49.0

%description   -n gem-aws-sdk-health
Official AWS Ruby gem for AWS Health APIs and Notifications (AWSHealth). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-health-doc
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-health
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-health) = 1.49.0

%description   -n gem-aws-sdk-health-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Health APIs and Notifications (AWSHealth). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-health-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-health.


%package       -n gem-aws-sdk-health-devel
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-health
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-health) = 1.49.0

%description   -n gem-aws-sdk-health-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Health APIs and Notifications (AWSHealth). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-health-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-health.


%package       -n gem-aws-sdk-kendra
Version:       1.63.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-kendra) = 1.63.0

%description   -n gem-aws-sdk-kendra
Official AWS Ruby gem for AWSKendraFrontendService (kendra). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kendra-doc
Version:       1.63.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kendra
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kendra) = 1.63.0

%description   -n gem-aws-sdk-kendra-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWSKendraFrontendService (kendra). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kendra-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kendra.


%package       -n gem-aws-sdk-kendra-devel
Version:       1.63.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kendra
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kendra) = 1.63.0

%description   -n gem-aws-sdk-kendra-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWSKendraFrontendService (kendra). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kendra-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kendra.


%package       -n gem-aws-sdk-lambda
Version:       1.91.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-lambda) = 1.91.0

%description   -n gem-aws-sdk-lambda
Official AWS Ruby gem for AWS Lambda. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-lambda-doc
Version:       1.91.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lambda
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lambda) = 1.91.0

%description   -n gem-aws-sdk-lambda-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Lambda. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lambda-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lambda.


%package       -n gem-aws-sdk-lambda-devel
Version:       1.91.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lambda
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lambda) = 1.91.0

%description   -n gem-aws-sdk-lambda-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Lambda. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lambda-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lambda.


%package       -n gem-aws-sdk-macie2
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-macie2) = 1.51.0

%description   -n gem-aws-sdk-macie2
Official AWS Ruby gem for Amazon Macie 2. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-macie2-doc
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-macie2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-macie2) = 1.51.0

%description   -n gem-aws-sdk-macie2-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-macie2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-macie2.


%package       -n gem-aws-sdk-macie2-devel
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-macie2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-macie2) = 1.51.0

%description   -n gem-aws-sdk-macie2-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-macie2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-macie2.


%package       -n gem-aws-sdk-mobile
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-mobile) = 1.37.0

%description   -n gem-aws-sdk-mobile
Official AWS Ruby gem for AWS Mobile. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mobile-doc
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mobile
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mobile) = 1.37.0

%description   -n gem-aws-sdk-mobile-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Mobile. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mobile-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mobile.


%package       -n gem-aws-sdk-mobile-devel
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mobile
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mobile) = 1.37.0

%description   -n gem-aws-sdk-mobile-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Mobile. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mobile-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mobile.


%package       -n gem-aws-sdk-proton
Version:       1.22.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Proton
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-proton) = 1.22.0

%description   -n gem-aws-sdk-proton
Official AWS Ruby gem for AWS Proton. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-proton-doc
Version:       1.22.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Proton documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-proton
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-proton) = 1.22.0

%description   -n gem-aws-sdk-proton-doc
AWS SDK for Ruby - AWS Proton documentation files.

Official AWS Ruby gem for AWS Proton. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-proton-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-proton.


%package       -n gem-aws-sdk-proton-devel
Version:       1.22.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Proton development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-proton
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-proton) = 1.22.0

%description   -n gem-aws-sdk-proton-devel
AWS SDK for Ruby - AWS Proton development package.

Official AWS Ruby gem for AWS Proton. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-proton-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-proton.


%package       -n gem-aws-sdk-shield
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-shield) = 1.51.0

%description   -n gem-aws-sdk-shield
Official AWS Ruby gem for AWS Shield. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-shield-doc
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-shield
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-shield) = 1.51.0

%description   -n gem-aws-sdk-shield-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Shield. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-shield-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-shield.


%package       -n gem-aws-sdk-shield-devel
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-shield
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-shield) = 1.51.0

%description   -n gem-aws-sdk-shield-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Shield. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-shield-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-shield.


%package       -n gem-aws-sdk-signer
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-signer) = 1.40.0

%description   -n gem-aws-sdk-signer
Official AWS Ruby gem for AWS Signer (signer). This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-signer-doc
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-signer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-signer) = 1.40.0

%description   -n gem-aws-sdk-signer-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-signer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-signer.


%package       -n gem-aws-sdk-signer-devel
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-signer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-signer) = 1.40.0

%description   -n gem-aws-sdk-signer-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-signer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-signer.


%package       -n gem-aws-sdk-ssmsap
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - SsmSap
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ssmsap) = 1.3.0

%description   -n gem-aws-sdk-ssmsap
Official AWS Ruby gem for AWS Systems Manager for SAP (SsmSap). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ssmsap-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - SsmSap documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ssmsap
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ssmsap) = 1.3.0

%description   -n gem-aws-sdk-ssmsap-doc
AWS SDK for Ruby - SsmSap documentation files.

Official AWS Ruby gem for AWS Systems Manager for SAP (SsmSap). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssmsap-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ssmsap.


%package       -n gem-aws-sdk-ssmsap-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - SsmSap development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ssmsap
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ssmsap) = 1.3.0

%description   -n gem-aws-sdk-ssmsap-devel
AWS SDK for Ruby - SsmSap development package.

Official AWS Ruby gem for AWS Systems Manager for SAP (SsmSap). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssmsap-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ssmsap.


%package       -n gem-aws-sdk-states
Version:       1.52.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-states) = 1.52.0

%description   -n gem-aws-sdk-states
Official AWS Ruby gem for AWS Step Functions (AWS SFN). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-states-doc
Version:       1.52.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-states
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-states) = 1.52.0

%description   -n gem-aws-sdk-states-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-states-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-states.


%package       -n gem-aws-sdk-states-devel
Version:       1.52.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-states
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-states) = 1.52.0

%description   -n gem-aws-sdk-states-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-states-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-states.


%package       -n gem-aws-eventstream
Version:       1.2.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(aws-eventstream) = 1.2.0

%description   -n gem-aws-eventstream
Amazon Web Services event stream library. Decodes and encodes binary stream
under `vnd.amazon.event-stream` content-type


%package       -n gem-aws-eventstream-doc
Version:       1.2.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-eventstream
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-eventstream) = 1.2.0

%description   -n gem-aws-eventstream-doc
The official AWS SDK for Ruby documentation files.

Amazon Web Services event stream library. Decodes and encodes binary stream
under `vnd.amazon.event-stream` content-type

%description   -n gem-aws-eventstream-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-eventstream.


%package       -n gem-aws-eventstream-devel
Version:       1.2.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-eventstream
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-eventstream) = 1.2.0

%description   -n gem-aws-eventstream-devel
The official AWS SDK for Ruby development package.

Amazon Web Services event stream library. Decodes and encodes binary stream
under `vnd.amazon.event-stream` content-type

%description   -n gem-aws-eventstream-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-eventstream.


%package       -n gem-aws-sdk-account
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Account
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-account) = 1.9.0

%description   -n gem-aws-sdk-account
Official AWS Ruby gem for AWS Account. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-account-doc
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Account documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-account
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-account) = 1.9.0

%description   -n gem-aws-sdk-account-doc
AWS SDK for Ruby - AWS Account documentation files.

Official AWS Ruby gem for AWS Account. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-account-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-account.


%package       -n gem-aws-sdk-account-devel
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Account development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-account
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-account) = 1.9.0

%description   -n gem-aws-sdk-account-devel
AWS SDK for Ruby - AWS Account development package.

Official AWS Ruby gem for AWS Account. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-account-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-account.


%package       -n gem-aws-sdk-amplify
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-amplify) = 1.44.0

%description   -n gem-aws-sdk-amplify
Official AWS Ruby gem for AWS Amplify (Amplify). This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-amplify-doc
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-amplify
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-amplify) = 1.44.0

%description   -n gem-aws-sdk-amplify-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-amplify-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-amplify.


%package       -n gem-aws-sdk-amplify-devel
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-amplify
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-amplify) = 1.44.0

%description   -n gem-aws-sdk-amplify-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-amplify-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-amplify.


%package       -n gem-aws-sdk-appflow
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-appflow) = 1.35.0

%description   -n gem-aws-sdk-appflow
Official AWS Ruby gem for Amazon Appflow. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-appflow-doc
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appflow
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appflow) = 1.35.0

%description   -n gem-aws-sdk-appflow-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-appflow-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appflow.


%package       -n gem-aws-sdk-appflow-devel
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appflow
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appflow) = 1.35.0

%description   -n gem-aws-sdk-appflow-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-appflow-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appflow.


%package       -n gem-aws-sdk-appmesh
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-appmesh) = 1.49.0

%description   -n gem-aws-sdk-appmesh
Official AWS Ruby gem for AWS App Mesh. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-appmesh-doc
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appmesh
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appmesh) = 1.49.0

%description   -n gem-aws-sdk-appmesh-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-appmesh-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appmesh.


%package       -n gem-aws-sdk-appmesh-devel
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appmesh
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appmesh) = 1.49.0

%description   -n gem-aws-sdk-appmesh-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-appmesh-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appmesh.


%package       -n gem-aws-sdk-appsync
Version:       1.57.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-appsync) = 1.57.0

%description   -n gem-aws-sdk-appsync
Official AWS Ruby gem for AWS AppSync (AWSAppSync). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-appsync-doc
Version:       1.57.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appsync
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appsync) = 1.57.0

%description   -n gem-aws-sdk-appsync-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-appsync-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appsync.


%package       -n gem-aws-sdk-appsync-devel
Version:       1.57.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appsync
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appsync) = 1.57.0

%description   -n gem-aws-sdk-appsync-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-appsync-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appsync.


%package       -n gem-aws-sdk-budgets
Version:       1.52.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-budgets) = 1.52.0

%description   -n gem-aws-sdk-budgets
Official AWS Ruby gem for AWS Budgets (AWSBudgets). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-budgets-doc
Version:       1.52.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-budgets
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-budgets) = 1.52.0

%description   -n gem-aws-sdk-budgets-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-budgets-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-budgets.


%package       -n gem-aws-sdk-budgets-devel
Version:       1.52.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-budgets
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-budgets) = 1.52.0

%description   -n gem-aws-sdk-budgets-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-budgets-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-budgets.


%package       -n gem-aws-sdk-connect
Version:       1.94.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-connect) = 1.94.0

%description   -n gem-aws-sdk-connect
Official AWS Ruby gem for Amazon Connect Service (Amazon Connect). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-connect-doc
Version:       1.94.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-connect
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-connect) = 1.94.0

%description   -n gem-aws-sdk-connect-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Connect Service (Amazon Connect). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-connect-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-connect.


%package       -n gem-aws-sdk-connect-devel
Version:       1.94.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-connect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-connect) = 1.94.0

%description   -n gem-aws-sdk-connect-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Connect Service (Amazon Connect). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-connect-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-connect.


%package       -n gem-aws-sdk-glacier
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-glacier) = 1.49.0

%description   -n gem-aws-sdk-glacier
Official AWS Ruby gem for Amazon Glacier. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-glacier-doc
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-glacier
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-glacier) = 1.49.0

%description   -n gem-aws-sdk-glacier-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-glacier-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-glacier.


%package       -n gem-aws-sdk-glacier-devel
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-glacier
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-glacier) = 1.49.0

%description   -n gem-aws-sdk-glacier-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-glacier-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-glacier.


%package       -n gem-aws-sdk-ivschat
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - ivschat
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ivschat) = 1.8.0

%description   -n gem-aws-sdk-ivschat
Official AWS Ruby gem for Amazon Interactive Video Service Chat (ivschat). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ivschat-doc
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - ivschat documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ivschat
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ivschat) = 1.8.0

%description   -n gem-aws-sdk-ivschat-doc
AWS SDK for Ruby - ivschat documentation files.

Official AWS Ruby gem for Amazon Interactive Video Service Chat (ivschat). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ivschat-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ivschat.


%package       -n gem-aws-sdk-ivschat-devel
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - ivschat development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ivschat
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ivschat) = 1.8.0

%description   -n gem-aws-sdk-ivschat-devel
AWS SDK for Ruby - ivschat development package.

Official AWS Ruby gem for Amazon Interactive Video Service Chat (ivschat). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ivschat-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ivschat.


%package       -n gem-aws-sdk-kinesis
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-kinesis) = 1.44.0

%description   -n gem-aws-sdk-kinesis
Official AWS Ruby gem for Amazon Kinesis (Kinesis). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-kinesis-doc
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesis) = 1.44.0

%description   -n gem-aws-sdk-kinesis-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-kinesis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesis.


%package       -n gem-aws-sdk-kinesis-devel
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesis
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesis) = 1.44.0

%description   -n gem-aws-sdk-kinesis-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-kinesis-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesis.


%package       -n gem-aws-sdk-neptune
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-neptune) = 1.49.0

%description   -n gem-aws-sdk-neptune
Official AWS Ruby gem for Amazon Neptune. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-neptune-doc
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-neptune
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-neptune) = 1.49.0

%description   -n gem-aws-sdk-neptune-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-neptune-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-neptune.


%package       -n gem-aws-sdk-neptune-devel
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-neptune
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-neptune) = 1.49.0

%description   -n gem-aws-sdk-neptune-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-neptune-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-neptune.


%package       -n gem-aws-sdk-pricing
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-pricing) = 1.42.0

%description   -n gem-aws-sdk-pricing
Official AWS Ruby gem for AWS Price List Service (AWS Pricing). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-pricing-doc
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-pricing
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-pricing) = 1.42.0

%description   -n gem-aws-sdk-pricing-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Price List Service (AWS Pricing). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pricing-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-pricing.


%package       -n gem-aws-sdk-pricing-devel
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-pricing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-pricing) = 1.42.0

%description   -n gem-aws-sdk-pricing-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Price List Service (AWS Pricing). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pricing-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-pricing.


%package       -n gem-aws-sdk-route53
Version:       1.71.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-route53) = 1.71.0

%description   -n gem-aws-sdk-route53
Official AWS Ruby gem for Amazon Route 53 (Route 53). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-route53-doc
Version:       1.71.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-route53
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-route53) = 1.71.0

%description   -n gem-aws-sdk-route53-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-route53-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-route53.


%package       -n gem-aws-sdk-route53-devel
Version:       1.71.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-route53
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-route53) = 1.71.0

%description   -n gem-aws-sdk-route53-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-route53-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-route53.


%package       -n gem-aws-sdk-schemas
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-schemas) = 1.25.0

%description   -n gem-aws-sdk-schemas
Official AWS Ruby gem for Schemas. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-schemas-doc
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-schemas
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-schemas) = 1.25.0

%description   -n gem-aws-sdk-schemas-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Schemas. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-schemas-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-schemas.


%package       -n gem-aws-sdk-schemas-devel
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-schemas
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-schemas) = 1.25.0

%description   -n gem-aws-sdk-schemas-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Schemas. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-schemas-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-schemas.


%package       -n gem-aws-sdk-ssooidc
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.131.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ssooidc) = 1.23.0

%description   -n gem-aws-sdk-ssooidc
Official AWS Ruby gem for AWS SSO OIDC (SSO OIDC). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-ssooidc-doc
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ssooidc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ssooidc) = 1.23.0

%description   -n gem-aws-sdk-ssooidc-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-ssooidc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ssooidc.


%package       -n gem-aws-sdk-ssooidc-devel
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ssooidc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ssooidc) = 1.23.0

%description   -n gem-aws-sdk-ssooidc-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-ssooidc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ssooidc.


%package       -n gem-aws-sdk-support
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-support) = 1.44.0

%description   -n gem-aws-sdk-support
Official AWS Ruby gem for AWS Support. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-support-doc
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-support
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-support) = 1.44.0

%description   -n gem-aws-sdk-support-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Support. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-support-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-support.


%package       -n gem-aws-sdk-support-devel
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-support
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-support) = 1.44.0

%description   -n gem-aws-sdk-support-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Support. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-support-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-support.


%package       -n gem-aws-sdk-voiceid
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Voice ID
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-voiceid) = 1.11.0

%description   -n gem-aws-sdk-voiceid
Official AWS Ruby gem for Amazon Voice ID. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-voiceid-doc
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Voice ID documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-voiceid
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-voiceid) = 1.11.0

%description   -n gem-aws-sdk-voiceid-doc
AWS SDK for Ruby - Amazon Voice ID documentation files.

%description   -n gem-aws-sdk-voiceid-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-voiceid.


%package       -n gem-aws-sdk-voiceid-devel
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Voice ID development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-voiceid
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-voiceid) = 1.11.0

%description   -n gem-aws-sdk-voiceid-devel
AWS SDK for Ruby - Amazon Voice ID development package.

%description   -n gem-aws-sdk-voiceid-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-voiceid.


%package       -n gem-aws-sdk-cloudhsm
Version:       1.41.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cloudhsm) = 1.41.0

%description   -n gem-aws-sdk-cloudhsm
Official AWS Ruby gem for Amazon CloudHSM (CloudHSM). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-cloudhsm-doc
Version:       1.41.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudhsm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudhsm) = 1.41.0

%description   -n gem-aws-sdk-cloudhsm-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-cloudhsm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudhsm.


%package       -n gem-aws-sdk-cloudhsm-devel
Version:       1.41.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudhsm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudhsm) = 1.41.0

%description   -n gem-aws-sdk-cloudhsm-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-cloudhsm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudhsm.


%package       -n gem-aws-sdk-codestar
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-codestar) = 1.40.0

%description   -n gem-aws-sdk-codestar
Official AWS Ruby gem for AWS CodeStar (CodeStar). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-codestar-doc
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codestar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codestar) = 1.40.0

%description   -n gem-aws-sdk-codestar-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-codestar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codestar.


%package       -n gem-aws-sdk-codestar-devel
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codestar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codestar) = 1.40.0

%description   -n gem-aws-sdk-codestar-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-codestar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codestar.


%package       -n gem-aws-sdk-datasync
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-datasync) = 1.53.0

%description   -n gem-aws-sdk-datasync
Official AWS Ruby gem for AWS DataSync (DataSync). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-datasync-doc
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-datasync
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-datasync) = 1.53.0

%description   -n gem-aws-sdk-datasync-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-datasync-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-datasync.


%package       -n gem-aws-sdk-datasync-devel
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-datasync
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-datasync) = 1.53.0

%description   -n gem-aws-sdk-datasync-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-datasync-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-datasync.


%package       -n gem-aws-sdk-dynamodb
Version:       1.81.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-dynamodb) = 1.81.0

%description   -n gem-aws-sdk-dynamodb
Official AWS Ruby gem for Amazon DynamoDB (DynamoDB). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-dynamodb-doc
Version:       1.81.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-dynamodb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-dynamodb) = 1.81.0

%description   -n gem-aws-sdk-dynamodb-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-dynamodb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-dynamodb.


%package       -n gem-aws-sdk-dynamodb-devel
Version:       1.81.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-dynamodb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-dynamodb) = 1.81.0

%description   -n gem-aws-sdk-dynamodb-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-dynamodb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-dynamodb.


%package       -n gem-aws-sdk-finspace
Version:       1.13.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-finspace) = 1.13.0

%description   -n gem-aws-sdk-finspace
Official AWS Ruby gem for FinSpace User Environment Management service
(finspace). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-finspace-doc
Version:       1.13.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-finspace
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-finspace) = 1.13.0

%description   -n gem-aws-sdk-finspace-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for FinSpace User Environment Management service
(finspace). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-finspace-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-finspace.


%package       -n gem-aws-sdk-finspace-devel
Version:       1.13.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-finspace
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-finspace) = 1.13.0

%description   -n gem-aws-sdk-finspace-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for FinSpace User Environment Management service
(finspace). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-finspace-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-finspace.


%package       -n gem-aws-sdk-firehose
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-firehose) = 1.51.0

%description   -n gem-aws-sdk-firehose
Official AWS Ruby gem for Amazon Kinesis Firehose (Firehose). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-firehose-doc
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-firehose
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-firehose) = 1.51.0

%description   -n gem-aws-sdk-firehose-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Kinesis Firehose (Firehose). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-firehose-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-firehose.


%package       -n gem-aws-sdk-firehose-devel
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-firehose
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-firehose) = 1.51.0

%description   -n gem-aws-sdk-firehose-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Kinesis Firehose (Firehose). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-firehose-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-firehose.


%package       -n gem-aws-sdk-gamelift
Version:       1.61.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-gamelift) = 1.61.0

%description   -n gem-aws-sdk-gamelift
Official AWS Ruby gem for Amazon GameLift. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-gamelift-doc
Version:       1.61.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-gamelift
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-gamelift) = 1.61.0

%description   -n gem-aws-sdk-gamelift-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-gamelift-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-gamelift.


%package       -n gem-aws-sdk-gamelift-devel
Version:       1.61.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-gamelift
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-gamelift) = 1.61.0

%description   -n gem-aws-sdk-gamelift-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-gamelift-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-gamelift.


%package       -n gem-aws-sdk-memorydb
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon MemoryDB
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-memorydb) = 1.12.0

%description   -n gem-aws-sdk-memorydb
Official AWS Ruby gem for Amazon MemoryDB. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-memorydb-doc
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon MemoryDB documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-memorydb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-memorydb) = 1.12.0

%description   -n gem-aws-sdk-memorydb-doc
AWS SDK for Ruby - Amazon MemoryDB documentation files.

%description   -n gem-aws-sdk-memorydb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-memorydb.


%package       -n gem-aws-sdk-memorydb-devel
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon MemoryDB development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-memorydb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-memorydb) = 1.12.0

%description   -n gem-aws-sdk-memorydb-devel
AWS SDK for Ruby - Amazon MemoryDB development package.

%description   -n gem-aws-sdk-memorydb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-memorydb.


%package       -n gem-aws-sdk-opsworks
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-opsworks) = 1.43.0

%description   -n gem-aws-sdk-opsworks
Official AWS Ruby gem for AWS OpsWorks. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-opsworks-doc
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-opsworks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-opsworks) = 1.43.0

%description   -n gem-aws-sdk-opsworks-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-opsworks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-opsworks.


%package       -n gem-aws-sdk-opsworks-devel
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-opsworks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-opsworks) = 1.43.0

%description   -n gem-aws-sdk-opsworks-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-opsworks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-opsworks.


%package       -n gem-aws-sdk-outposts
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-outposts) = 1.40.0

%description   -n gem-aws-sdk-outposts
Official AWS Ruby gem for AWS Outposts (Outposts). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-outposts-doc
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-outposts
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-outposts) = 1.40.0

%description   -n gem-aws-sdk-outposts-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-outposts-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-outposts.


%package       -n gem-aws-sdk-outposts-devel
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-outposts
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-outposts) = 1.40.0

%description   -n gem-aws-sdk-outposts-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-outposts-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-outposts.


%package       -n gem-aws-sdk-panorama
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Panorama
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-panorama) = 1.12.0

%description   -n gem-aws-sdk-panorama
Official AWS Ruby gem for AWS Panorama (Panorama). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-panorama-doc
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Panorama documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-panorama
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-panorama) = 1.12.0

%description   -n gem-aws-sdk-panorama-doc
AWS SDK for Ruby - Panorama documentation files.

%description   -n gem-aws-sdk-panorama-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-panorama.


%package       -n gem-aws-sdk-panorama-devel
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Panorama development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-panorama
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-panorama) = 1.12.0

%description   -n gem-aws-sdk-panorama-devel
AWS SDK for Ruby - Panorama development package.

%description   -n gem-aws-sdk-panorama-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-panorama.


%package       -n gem-aws-sdk-pinpoint
Version:       1.70.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-pinpoint) = 1.70.0

%description   -n gem-aws-sdk-pinpoint
Official AWS Ruby gem for Amazon Pinpoint. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-pinpoint-doc
Version:       1.70.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-pinpoint
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-pinpoint) = 1.70.0

%description   -n gem-aws-sdk-pinpoint-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-pinpoint-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-pinpoint.


%package       -n gem-aws-sdk-pinpoint-devel
Version:       1.70.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-pinpoint
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-pinpoint) = 1.70.0

%description   -n gem-aws-sdk-pinpoint-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-pinpoint-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-pinpoint.


%package       -n gem-aws-sdk-redshift
Version:       1.88.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-redshift) = 1.88.0

%description   -n gem-aws-sdk-redshift
Official AWS Ruby gem for Amazon Redshift. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-redshift-doc
Version:       1.88.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-redshift
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-redshift) = 1.88.0

%description   -n gem-aws-sdk-redshift-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-redshift-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-redshift.


%package       -n gem-aws-sdk-redshift-devel
Version:       1.88.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-redshift
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-redshift) = 1.88.0

%description   -n gem-aws-sdk-redshift-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-redshift-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-redshift.


%package       -n gem-aws-sdk-simpledb
Version:       1.36.1
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv2) >= 1.0
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv2) >= 2
Provides:      gem(aws-sdk-simpledb) = 1.36.1

%description   -n gem-aws-sdk-simpledb
Official AWS Ruby gem for Amazon SimpleDB. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-simpledb-doc
Version:       1.36.1
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-simpledb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-simpledb) = 1.36.1

%description   -n gem-aws-sdk-simpledb-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-simpledb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-simpledb.


%package       -n gem-aws-sdk-simpledb-devel
Version:       1.36.1
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-simpledb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-simpledb) = 1.36.1

%description   -n gem-aws-sdk-simpledb-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-simpledb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-simpledb.


%package       -n gem-aws-sdk-snowball
Version:       1.52.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-snowball) = 1.52.0

%description   -n gem-aws-sdk-snowball
Official AWS Ruby gem for Amazon Import/Export Snowball (Amazon Snowball). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-snowball-doc
Version:       1.52.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-snowball
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-snowball) = 1.52.0

%description   -n gem-aws-sdk-snowball-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Import/Export Snowball (Amazon Snowball). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-snowball-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-snowball.


%package       -n gem-aws-sdk-snowball-devel
Version:       1.52.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-snowball
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-snowball) = 1.52.0

%description   -n gem-aws-sdk-snowball-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Import/Export Snowball (Amazon Snowball). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-snowball-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-snowball.


%package       -n gem-aws-sdk-ssoadmin
Version:       1.22.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ssoadmin) = 1.22.0

%description   -n gem-aws-sdk-ssoadmin
Official AWS Ruby gem for AWS Single Sign-On Admin (SSO Admin). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ssoadmin-doc
Version:       1.22.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ssoadmin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ssoadmin) = 1.22.0

%description   -n gem-aws-sdk-ssoadmin-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Single Sign-On Admin (SSO Admin). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssoadmin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ssoadmin.


%package       -n gem-aws-sdk-ssoadmin-devel
Version:       1.22.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ssoadmin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ssoadmin) = 1.22.0

%description   -n gem-aws-sdk-ssoadmin-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Single Sign-On Admin (SSO Admin). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssoadmin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ssoadmin.


%package       -n gem-aws-sdk-textract
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-textract) = 1.44.0

%description   -n gem-aws-sdk-textract
Official AWS Ruby gem for Amazon Textract. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-textract-doc
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-textract
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-textract) = 1.44.0

%description   -n gem-aws-sdk-textract-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-textract-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-textract.


%package       -n gem-aws-sdk-textract-devel
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-textract
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-textract) = 1.44.0

%description   -n gem-aws-sdk-textract-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-textract-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-textract.


%package       -n gem-aws-sdk-transfer
Version:       1.66.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-transfer) = 1.66.0

%description   -n gem-aws-sdk-transfer
Official AWS Ruby gem for AWS Transfer Family (AWS Transfer). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-transfer-doc
Version:       1.66.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-transfer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-transfer) = 1.66.0

%description   -n gem-aws-sdk-transfer-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Transfer Family (AWS Transfer). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-transfer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-transfer.


%package       -n gem-aws-sdk-transfer-devel
Version:       1.66.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-transfer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-transfer) = 1.66.0

%description   -n gem-aws-sdk-transfer-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Transfer Family (AWS Transfer). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-transfer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-transfer.


%package       -n gem-aws-sdk-workdocs
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-workdocs) = 1.42.0

%description   -n gem-aws-sdk-workdocs
Official AWS Ruby gem for Amazon WorkDocs. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-workdocs-doc
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-workdocs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-workdocs) = 1.42.0

%description   -n gem-aws-sdk-workdocs-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-workdocs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-workdocs.


%package       -n gem-aws-sdk-workdocs-devel
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-workdocs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-workdocs) = 1.42.0

%description   -n gem-aws-sdk-workdocs-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-workdocs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-workdocs.


%package       -n gem-aws-sdk-worklink
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-worklink) = 1.35.0

%description   -n gem-aws-sdk-worklink
Official AWS Ruby gem for Amazon WorkLink (WorkLink). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-worklink-doc
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-worklink
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-worklink) = 1.35.0

%description   -n gem-aws-sdk-worklink-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-worklink-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-worklink.


%package       -n gem-aws-sdk-worklink-devel
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-worklink
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-worklink) = 1.35.0

%description   -n gem-aws-sdk-worklink-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-worklink-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-worklink.


%package       -n gem-aws-sdk-workmail
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-workmail) = 1.53.0

%description   -n gem-aws-sdk-workmail
Official AWS Ruby gem for Amazon WorkMail. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-workmail-doc
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-workmail
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-workmail) = 1.53.0

%description   -n gem-aws-sdk-workmail-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-workmail-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-workmail.


%package       -n gem-aws-sdk-workmail-devel
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-workmail
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-workmail) = 1.53.0

%description   -n gem-aws-sdk-workmail-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-workmail-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-workmail.


%package       -n gem-aws-sdk-appconfig
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-appconfig) = 1.28.0

%description   -n gem-aws-sdk-appconfig
Official AWS Ruby gem for Amazon AppConfig (AppConfig). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-appconfig-doc
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appconfig
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appconfig) = 1.28.0

%description   -n gem-aws-sdk-appconfig-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-appconfig-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appconfig.


%package       -n gem-aws-sdk-appconfig-devel
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appconfig
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appconfig) = 1.28.0

%description   -n gem-aws-sdk-appconfig-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-appconfig-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appconfig.


%package       -n gem-aws-sdk-apprunner
Version:       1.20.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-apprunner) = 1.20.0

%description   -n gem-aws-sdk-apprunner
Official AWS Ruby gem for AWS App Runner. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-apprunner-doc
Version:       1.20.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-apprunner
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-apprunner) = 1.20.0

%description   -n gem-aws-sdk-apprunner-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-apprunner-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-apprunner.


%package       -n gem-aws-sdk-apprunner-devel
Version:       1.20.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-apprunner
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-apprunner) = 1.20.0

%description   -n gem-aws-sdk-apprunner-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-apprunner-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-apprunner.


%package       -n gem-aws-sdk-appstream
Version:       1.70.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-appstream) = 1.70.0

%description   -n gem-aws-sdk-appstream
Official AWS Ruby gem for Amazon AppStream. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-appstream-doc
Version:       1.70.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appstream
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appstream) = 1.70.0

%description   -n gem-aws-sdk-appstream-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-appstream-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appstream.


%package       -n gem-aws-sdk-appstream-devel
Version:       1.70.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appstream
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appstream) = 1.70.0

%description   -n gem-aws-sdk-appstream-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-appstream-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appstream.


%package       -n gem-aws-sdk-codebuild
Version:       1.90.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-codebuild) = 1.90.0

%description   -n gem-aws-sdk-codebuild
Official AWS Ruby gem for AWS CodeBuild. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-codebuild-doc
Version:       1.90.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codebuild
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codebuild) = 1.90.0

%description   -n gem-aws-sdk-codebuild-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-codebuild-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codebuild.


%package       -n gem-aws-sdk-codebuild-devel
Version:       1.90.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codebuild
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codebuild) = 1.90.0

%description   -n gem-aws-sdk-codebuild-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-codebuild-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codebuild.


%package       -n gem-aws-sdk-detective
Version:       1.32.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-detective) = 1.32.0

%description   -n gem-aws-sdk-detective
Official AWS Ruby gem for Amazon Detective. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-detective-doc
Version:       1.32.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-detective
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-detective) = 1.32.0

%description   -n gem-aws-sdk-detective-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-detective-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-detective.


%package       -n gem-aws-sdk-detective-devel
Version:       1.32.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-detective
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-detective) = 1.32.0

%description   -n gem-aws-sdk-detective-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-detective-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-detective.


%package       -n gem-aws-sdk-ecrpublic
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ecrpublic) = 1.15.0

%description   -n gem-aws-sdk-ecrpublic
Official AWS Ruby gem for Amazon Elastic Container Registry Public (Amazon ECR
Public). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ecrpublic-doc
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ecrpublic
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ecrpublic) = 1.15.0

%description   -n gem-aws-sdk-ecrpublic-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Elastic Container Registry Public (Amazon ECR
Public). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ecrpublic-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ecrpublic.


%package       -n gem-aws-sdk-ecrpublic-devel
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ecrpublic
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ecrpublic) = 1.15.0

%description   -n gem-aws-sdk-ecrpublic-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Elastic Container Registry Public (Amazon ECR
Public). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ecrpublic-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ecrpublic.


%package       -n gem-aws-sdk-guardduty
Version:       1.63.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-guardduty) = 1.63.0

%description   -n gem-aws-sdk-guardduty
Official AWS Ruby gem for Amazon GuardDuty. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-guardduty-doc
Version:       1.63.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-guardduty
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-guardduty) = 1.63.0

%description   -n gem-aws-sdk-guardduty-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-guardduty-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-guardduty.


%package       -n gem-aws-sdk-guardduty-devel
Version:       1.63.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-guardduty
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-guardduty) = 1.63.0

%description   -n gem-aws-sdk-guardduty-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-guardduty-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-guardduty.


%package       -n gem-aws-sdk-honeycode
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-honeycode) = 1.19.0

%description   -n gem-aws-sdk-honeycode
Official AWS Ruby gem for Amazon Honeycode (Honeycode). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-honeycode-doc
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-honeycode
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-honeycode) = 1.19.0

%description   -n gem-aws-sdk-honeycode-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-honeycode-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-honeycode.


%package       -n gem-aws-sdk-honeycode-devel
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-honeycode
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-honeycode) = 1.19.0

%description   -n gem-aws-sdk-honeycode-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-honeycode-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-honeycode.


%package       -n gem-aws-sdk-inspector
Version:       1.45.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-inspector) = 1.45.0

%description   -n gem-aws-sdk-inspector
Official AWS Ruby gem for Amazon Inspector. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-inspector-doc
Version:       1.45.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-inspector
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-inspector) = 1.45.0

%description   -n gem-aws-sdk-inspector-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-inspector-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-inspector.


%package       -n gem-aws-sdk-inspector-devel
Version:       1.45.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-inspector
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-inspector) = 1.45.0

%description   -n gem-aws-sdk-inspector-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-inspector-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-inspector.


%package       -n gem-aws-sdk-iotevents
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iotevents) = 1.35.0

%description   -n gem-aws-sdk-iotevents
Official AWS Ruby gem for AWS IoT Events. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-iotevents-doc
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotevents
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotevents) = 1.35.0

%description   -n gem-aws-sdk-iotevents-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-iotevents-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotevents.


%package       -n gem-aws-sdk-iotevents-devel
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotevents
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotevents) = 1.35.0

%description   -n gem-aws-sdk-iotevents-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-iotevents-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotevents.


%package       -n gem-aws-sdk-keyspaces
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Keyspaces
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-keyspaces) = 1.4.0

%description   -n gem-aws-sdk-keyspaces
Official AWS Ruby gem for Amazon Keyspaces. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-keyspaces-doc
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Keyspaces documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-keyspaces
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-keyspaces) = 1.4.0

%description   -n gem-aws-sdk-keyspaces-doc
AWS SDK for Ruby - Amazon Keyspaces documentation files.

%description   -n gem-aws-sdk-keyspaces-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-keyspaces.


%package       -n gem-aws-sdk-keyspaces-devel
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Keyspaces development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-keyspaces
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-keyspaces) = 1.4.0

%description   -n gem-aws-sdk-keyspaces-devel
AWS SDK for Ruby - Amazon Keyspaces development package.

%description   -n gem-aws-sdk-keyspaces-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-keyspaces.


%package       -n gem-aws-sdk-lightsail
Version:       1.73.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-lightsail) = 1.73.0

%description   -n gem-aws-sdk-lightsail
Official AWS Ruby gem for Amazon Lightsail. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-lightsail-doc
Version:       1.73.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lightsail
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lightsail) = 1.73.0

%description   -n gem-aws-sdk-lightsail-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-lightsail-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lightsail.


%package       -n gem-aws-sdk-lightsail-devel
Version:       1.73.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lightsail
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lightsail) = 1.73.0

%description   -n gem-aws-sdk-lightsail-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-lightsail-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lightsail.


%package       -n gem-aws-sdk-medialive
Version:       1.96.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-medialive) = 1.96.0

%description   -n gem-aws-sdk-medialive
Official AWS Ruby gem for AWS Elemental MediaLive (MediaLive). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-medialive-doc
Version:       1.96.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-medialive
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-medialive) = 1.96.0

%description   -n gem-aws-sdk-medialive-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Elemental MediaLive (MediaLive). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-medialive-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-medialive.


%package       -n gem-aws-sdk-medialive-devel
Version:       1.96.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-medialive
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-medialive) = 1.96.0

%description   -n gem-aws-sdk-medialive-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Elemental MediaLive (MediaLive). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-medialive-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-medialive.


%package       -n gem-aws-sdk-resources
Version:       3.157.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-acm) >= 1
Requires:      gem(aws-sdk-acmpca) >= 1
Requires:      gem(aws-sdk-apigateway) >= 1
Requires:      gem(aws-sdk-arczonalshift) >= 1
Requires:      gem(aws-sdk-accessanalyzer) >= 1
Requires:      gem(aws-sdk-account) >= 1
Requires:      gem(aws-sdk-alexaforbusiness) >= 1
Requires:      gem(aws-sdk-amplify) >= 1
Requires:      gem(aws-sdk-amplifybackend) >= 1
Requires:      gem(aws-sdk-amplifyuibuilder) >= 1
Requires:      gem(aws-sdk-apigatewaymanagementapi) >= 1
Requires:      gem(aws-sdk-apigatewayv2) >= 1
Requires:      gem(aws-sdk-appconfig) >= 1
Requires:      gem(aws-sdk-appconfigdata) >= 1
Requires:      gem(aws-sdk-appintegrationsservice) >= 1
Requires:      gem(aws-sdk-appmesh) >= 1
Requires:      gem(aws-sdk-appregistry) >= 1
Requires:      gem(aws-sdk-apprunner) >= 1
Requires:      gem(aws-sdk-appstream) >= 1
Requires:      gem(aws-sdk-appsync) >= 1
Requires:      gem(aws-sdk-appflow) >= 1
Requires:      gem(aws-sdk-applicationautoscaling) >= 1
Requires:      gem(aws-sdk-applicationcostprofiler) >= 1
Requires:      gem(aws-sdk-applicationdiscoveryservice) >= 1
Requires:      gem(aws-sdk-applicationinsights) >= 1
Requires:      gem(aws-sdk-athena) >= 1
Requires:      gem(aws-sdk-auditmanager) >= 1
Requires:      gem(aws-sdk-augmentedairuntime) >= 1
Requires:      gem(aws-sdk-autoscaling) >= 1
Requires:      gem(aws-sdk-autoscalingplans) >= 1
Requires:      gem(aws-sdk-backup) >= 1
Requires:      gem(aws-sdk-backupgateway) >= 1
Requires:      gem(aws-sdk-backupstorage) >= 1
Requires:      gem(aws-sdk-batch) >= 1
Requires:      gem(aws-sdk-billingconductor) >= 1
Requires:      gem(aws-sdk-braket) >= 1
Requires:      gem(aws-sdk-budgets) >= 1
Requires:      gem(aws-sdk-chime) >= 1
Requires:      gem(aws-sdk-chimesdkidentity) >= 1
Requires:      gem(aws-sdk-chimesdkmediapipelines) >= 1
Requires:      gem(aws-sdk-chimesdkmeetings) >= 1
Requires:      gem(aws-sdk-chimesdkmessaging) >= 1
Requires:      gem(aws-sdk-chimesdkvoice) >= 1
Requires:      gem(aws-sdk-cleanrooms) >= 1
Requires:      gem(aws-sdk-cloud9) >= 1
Requires:      gem(aws-sdk-cloudcontrolapi) >= 1
Requires:      gem(aws-sdk-clouddirectory) >= 1
Requires:      gem(aws-sdk-cloudformation) >= 1
Requires:      gem(aws-sdk-cloudfront) >= 1
Requires:      gem(aws-sdk-cloudhsm) >= 1
Requires:      gem(aws-sdk-cloudhsmv2) >= 1
Requires:      gem(aws-sdk-cloudsearch) >= 1
Requires:      gem(aws-sdk-cloudsearchdomain) >= 1
Requires:      gem(aws-sdk-cloudtrail) >= 1
Requires:      gem(aws-sdk-cloudwatch) >= 1
Requires:      gem(aws-sdk-cloudwatchevents) >= 1
Requires:      gem(aws-sdk-cloudwatchevidently) >= 1
Requires:      gem(aws-sdk-cloudwatchlogs) >= 1
Requires:      gem(aws-sdk-cloudwatchrum) >= 1
Requires:      gem(aws-sdk-codeartifact) >= 1
Requires:      gem(aws-sdk-codebuild) >= 1
Requires:      gem(aws-sdk-codecatalyst) >= 1
Requires:      gem(aws-sdk-codecommit) >= 1
Requires:      gem(aws-sdk-codedeploy) >= 1
Requires:      gem(aws-sdk-codeguruprofiler) >= 1
Requires:      gem(aws-sdk-codegurureviewer) >= 1
Requires:      gem(aws-sdk-codepipeline) >= 1
Requires:      gem(aws-sdk-codestar) >= 1
Requires:      gem(aws-sdk-codestarnotifications) >= 1
Requires:      gem(aws-sdk-codestarconnections) >= 1
Requires:      gem(aws-sdk-cognitoidentity) >= 1
Requires:      gem(aws-sdk-cognitoidentityprovider) >= 1
Requires:      gem(aws-sdk-cognitosync) >= 1
Requires:      gem(aws-sdk-comprehend) >= 1
Requires:      gem(aws-sdk-comprehendmedical) >= 1
Requires:      gem(aws-sdk-computeoptimizer) >= 1
Requires:      gem(aws-sdk-configservice) >= 1
Requires:      gem(aws-sdk-connect) >= 1
Requires:      gem(aws-sdk-connectcampaignservice) >= 1
Requires:      gem(aws-sdk-connectcases) >= 1
Requires:      gem(aws-sdk-connectcontactlens) >= 1
Requires:      gem(aws-sdk-connectparticipant) >= 1
Requires:      gem(aws-sdk-connectwisdomservice) >= 1
Requires:      gem(aws-sdk-controltower) >= 1
Requires:      gem(aws-sdk-costexplorer) >= 1
Requires:      gem(aws-sdk-costandusagereportservice) >= 1
Requires:      gem(aws-sdk-customerprofiles) >= 1
Requires:      gem(aws-sdk-dax) >= 1
Requires:      gem(aws-sdk-dlm) >= 1
Requires:      gem(aws-sdk-dataexchange) >= 1
Requires:      gem(aws-sdk-datapipeline) >= 1
Requires:      gem(aws-sdk-datasync) >= 1
Requires:      gem(aws-sdk-databasemigrationservice) >= 1
Requires:      gem(aws-sdk-detective) >= 1
Requires:      gem(aws-sdk-devopsguru) >= 1
Requires:      gem(aws-sdk-devicefarm) >= 1
Requires:      gem(aws-sdk-directconnect) >= 1
Requires:      gem(aws-sdk-directoryservice) >= 1
Requires:      gem(aws-sdk-docdb) >= 1
Requires:      gem(aws-sdk-docdbelastic) >= 1
Requires:      gem(aws-sdk-drs) >= 1
Requires:      gem(aws-sdk-dynamodb) >= 1
Requires:      gem(aws-sdk-dynamodbstreams) >= 1
Requires:      gem(aws-sdk-ebs) >= 1
Requires:      gem(aws-sdk-ec2) >= 1
Requires:      gem(aws-sdk-ec2instanceconnect) >= 1
Requires:      gem(aws-sdk-ecr) >= 1
Requires:      gem(aws-sdk-ecrpublic) >= 1
Requires:      gem(aws-sdk-ecs) >= 1
Requires:      gem(aws-sdk-efs) >= 1
Requires:      gem(aws-sdk-eks) >= 1
Requires:      gem(aws-sdk-emr) >= 1
Requires:      gem(aws-sdk-emrcontainers) >= 1
Requires:      gem(aws-sdk-emrserverless) >= 1
Requires:      gem(aws-sdk-elasticache) >= 1
Requires:      gem(aws-sdk-elasticbeanstalk) >= 1
Requires:      gem(aws-sdk-elasticinference) >= 1
Requires:      gem(aws-sdk-elasticloadbalancing) >= 1
Requires:      gem(aws-sdk-elasticloadbalancingv2) >= 1
Requires:      gem(aws-sdk-elastictranscoder) >= 1
Requires:      gem(aws-sdk-elasticsearchservice) >= 1
Requires:      gem(aws-sdk-eventbridge) >= 1
Requires:      gem(aws-sdk-fis) >= 1
Requires:      gem(aws-sdk-fms) >= 1
Requires:      gem(aws-sdk-fsx) >= 1
Requires:      gem(aws-sdk-finspacedata) >= 1
Requires:      gem(aws-sdk-finspace) >= 1
Requires:      gem(aws-sdk-firehose) >= 1
Requires:      gem(aws-sdk-forecastqueryservice) >= 1
Requires:      gem(aws-sdk-forecastservice) >= 1
Requires:      gem(aws-sdk-frauddetector) >= 1
Requires:      gem(aws-sdk-gamelift) >= 1
Requires:      gem(aws-sdk-gamesparks) >= 1
Requires:      gem(aws-sdk-glacier) >= 1
Requires:      gem(aws-sdk-globalaccelerator) >= 1
Requires:      gem(aws-sdk-glue) >= 1
Requires:      gem(aws-sdk-gluedatabrew) >= 1
Requires:      gem(aws-sdk-greengrass) >= 1
Requires:      gem(aws-sdk-greengrassv2) >= 1
Requires:      gem(aws-sdk-groundstation) >= 1
Requires:      gem(aws-sdk-guardduty) >= 1
Requires:      gem(aws-sdk-health) >= 1
Requires:      gem(aws-sdk-healthlake) >= 1
Requires:      gem(aws-sdk-honeycode) >= 1
Requires:      gem(aws-sdk-iam) >= 1
Requires:      gem(aws-sdk-ivs) >= 1
Requires:      gem(aws-sdk-identitystore) >= 1
Requires:      gem(aws-sdk-imagebuilder) >= 1
Requires:      gem(aws-sdk-importexport) >= 1
Requires:      gem(aws-sdk-inspector) >= 1
Requires:      gem(aws-sdk-inspector2) >= 1
Requires:      gem(aws-sdk-iot) >= 1
Requires:      gem(aws-sdk-iot1clickdevicesservice) >= 1
Requires:      gem(aws-sdk-iot1clickprojects) >= 1
Requires:      gem(aws-sdk-iotanalytics) >= 1
Requires:      gem(aws-sdk-iotdataplane) >= 1
Requires:      gem(aws-sdk-iotdeviceadvisor) >= 1
Requires:      gem(aws-sdk-iotevents) >= 1
Requires:      gem(aws-sdk-ioteventsdata) >= 1
Requires:      gem(aws-sdk-iotfleethub) >= 1
Requires:      gem(aws-sdk-iotfleetwise) >= 1
Requires:      gem(aws-sdk-iotjobsdataplane) >= 1
Requires:      gem(aws-sdk-iotroborunner) >= 1
Requires:      gem(aws-sdk-iotsecuretunneling) >= 1
Requires:      gem(aws-sdk-iotsitewise) >= 1
Requires:      gem(aws-sdk-iotthingsgraph) >= 1
Requires:      gem(aws-sdk-iottwinmaker) >= 1
Requires:      gem(aws-sdk-iotwireless) >= 1
Requires:      gem(aws-sdk-ivschat) >= 1
Requires:      gem(aws-sdk-kms) >= 1
Requires:      gem(aws-sdk-kafka) >= 1
Requires:      gem(aws-sdk-kafkaconnect) >= 1
Requires:      gem(aws-sdk-kendra) >= 1
Requires:      gem(aws-sdk-kendraranking) >= 1
Requires:      gem(aws-sdk-keyspaces) >= 1
Requires:      gem(aws-sdk-kinesis) >= 1
Requires:      gem(aws-sdk-kinesisanalytics) >= 1
Requires:      gem(aws-sdk-kinesisanalyticsv2) >= 1
Requires:      gem(aws-sdk-kinesisvideo) >= 1
Requires:      gem(aws-sdk-kinesisvideoarchivedmedia) >= 1
Requires:      gem(aws-sdk-kinesisvideomedia) >= 1
Requires:      gem(aws-sdk-kinesisvideosignalingchannels) >= 1
Requires:      gem(aws-sdk-kinesisvideowebrtcstorage) >= 1
Requires:      gem(aws-sdk-lakeformation) >= 1
Requires:      gem(aws-sdk-lambda) >= 1
Requires:      gem(aws-sdk-lambdapreview) >= 1
Requires:      gem(aws-sdk-lex) >= 1
Requires:      gem(aws-sdk-lexmodelbuildingservice) >= 1
Requires:      gem(aws-sdk-lexmodelsv2) >= 1
Requires:      gem(aws-sdk-lexruntimev2) >= 1
Requires:      gem(aws-sdk-licensemanager) >= 1
Requires:      gem(aws-sdk-licensemanagerlinuxsubscriptions) >= 1
Requires:      gem(aws-sdk-licensemanagerusersubscriptions) >= 1
Requires:      gem(aws-sdk-lightsail) >= 1
Requires:      gem(aws-sdk-locationservice) >= 1
Requires:      gem(aws-sdk-lookoutequipment) >= 1
Requires:      gem(aws-sdk-lookoutmetrics) >= 1
Requires:      gem(aws-sdk-lookoutforvision) >= 1
Requires:      gem(aws-sdk-mq) >= 1
Requires:      gem(aws-sdk-mturk) >= 1
Requires:      gem(aws-sdk-mwaa) >= 1
Requires:      gem(aws-sdk-machinelearning) >= 1
Requires:      gem(aws-sdk-macie) >= 1
Requires:      gem(aws-sdk-macie2) >= 1
Requires:      gem(aws-sdk-mainframemodernization) >= 1
Requires:      gem(aws-sdk-managedblockchain) >= 1
Requires:      gem(aws-sdk-managedgrafana) >= 1
Requires:      gem(aws-sdk-marketplacecatalog) >= 1
Requires:      gem(aws-sdk-marketplacecommerceanalytics) >= 1
Requires:      gem(aws-sdk-marketplaceentitlementservice) >= 1
Requires:      gem(aws-sdk-marketplacemetering) >= 1
Requires:      gem(aws-sdk-mediaconnect) >= 1
Requires:      gem(aws-sdk-mediaconvert) >= 1
Requires:      gem(aws-sdk-medialive) >= 1
Requires:      gem(aws-sdk-mediapackage) >= 1
Requires:      gem(aws-sdk-mediapackagevod) >= 1
Requires:      gem(aws-sdk-mediastore) >= 1
Requires:      gem(aws-sdk-mediastoredata) >= 1
Requires:      gem(aws-sdk-mediatailor) >= 1
Requires:      gem(aws-sdk-memorydb) >= 1
Requires:      gem(aws-sdk-mgn) >= 1
Requires:      gem(aws-sdk-migrationhub) >= 1
Requires:      gem(aws-sdk-migrationhubconfig) >= 1
Requires:      gem(aws-sdk-migrationhuborchestrator) >= 1
Requires:      gem(aws-sdk-migrationhubrefactorspaces) >= 1
Requires:      gem(aws-sdk-migrationhubstrategyrecommendations) >= 1
Requires:      gem(aws-sdk-mobile) >= 1
Requires:      gem(aws-sdk-neptune) >= 1
Requires:      gem(aws-sdk-networkfirewall) >= 1
Requires:      gem(aws-sdk-networkmanager) >= 1
Requires:      gem(aws-sdk-nimblestudio) >= 1
Requires:      gem(aws-sdk-oam) >= 1
Requires:      gem(aws-sdk-omics) >= 1
Requires:      gem(aws-sdk-opensearchserverless) >= 1
Requires:      gem(aws-sdk-opensearchservice) >= 1
Requires:      gem(aws-sdk-opsworks) >= 1
Requires:      gem(aws-sdk-opsworkscm) >= 1
Requires:      gem(aws-sdk-organizations) >= 1
Requires:      gem(aws-sdk-outposts) >= 1
Requires:      gem(aws-sdk-pi) >= 1
Requires:      gem(aws-sdk-panorama) >= 1
Requires:      gem(aws-sdk-personalize) >= 1
Requires:      gem(aws-sdk-personalizeevents) >= 1
Requires:      gem(aws-sdk-personalizeruntime) >= 1
Requires:      gem(aws-sdk-pinpoint) >= 1
Requires:      gem(aws-sdk-pinpointemail) >= 1
Requires:      gem(aws-sdk-pinpointsmsvoice) >= 1
Requires:      gem(aws-sdk-pinpointsmsvoicev2) >= 1
Requires:      gem(aws-sdk-pipes) >= 1
Requires:      gem(aws-sdk-polly) >= 1
Requires:      gem(aws-sdk-pricing) >= 1
Requires:      gem(aws-sdk-privatenetworks) >= 1
Requires:      gem(aws-sdk-prometheusservice) >= 1
Requires:      gem(aws-sdk-proton) >= 1
Requires:      gem(aws-sdk-qldb) >= 1
Requires:      gem(aws-sdk-qldbsession) >= 1
Requires:      gem(aws-sdk-quicksight) >= 1
Requires:      gem(aws-sdk-ram) >= 1
Requires:      gem(aws-sdk-rds) >= 1
Requires:      gem(aws-sdk-rdsdataservice) >= 1
Requires:      gem(aws-sdk-recyclebin) >= 1
Requires:      gem(aws-sdk-redshift) >= 1
Requires:      gem(aws-sdk-redshiftdataapiservice) >= 1
Requires:      gem(aws-sdk-redshiftserverless) >= 1
Requires:      gem(aws-sdk-rekognition) >= 1
Requires:      gem(aws-sdk-resiliencehub) >= 1
Requires:      gem(aws-sdk-resourceexplorer2) >= 1
Requires:      gem(aws-sdk-resourcegroups) >= 1
Requires:      gem(aws-sdk-resourcegroupstaggingapi) >= 1
Requires:      gem(aws-sdk-robomaker) >= 1
Requires:      gem(aws-sdk-rolesanywhere) >= 1
Requires:      gem(aws-sdk-route53) >= 1
Requires:      gem(aws-sdk-route53domains) >= 1
Requires:      gem(aws-sdk-route53recoverycluster) >= 1
Requires:      gem(aws-sdk-route53recoverycontrolconfig) >= 1
Requires:      gem(aws-sdk-route53recoveryreadiness) >= 1
Requires:      gem(aws-sdk-route53resolver) >= 1
Requires:      gem(aws-sdk-s3) >= 1
Requires:      gem(aws-sdk-s3control) >= 1
Requires:      gem(aws-sdk-s3outposts) >= 1
Requires:      gem(aws-sdk-ses) >= 1
Requires:      gem(aws-sdk-sesv2) >= 1
Requires:      gem(aws-sdk-sms) >= 1
Requires:      gem(aws-sdk-sns) >= 1
Requires:      gem(aws-sdk-sqs) >= 1
Requires:      gem(aws-sdk-ssm) >= 1
Requires:      gem(aws-sdk-ssmcontacts) >= 1
Requires:      gem(aws-sdk-ssmincidents) >= 1
Requires:      gem(aws-sdk-ssoadmin) >= 1
Requires:      gem(aws-sdk-swf) >= 1
Requires:      gem(aws-sdk-sagemaker) >= 1
Requires:      gem(aws-sdk-sagemakerfeaturestoreruntime) >= 1
Requires:      gem(aws-sdk-sagemakergeospatial) >= 1
Requires:      gem(aws-sdk-sagemakermetrics) >= 1
Requires:      gem(aws-sdk-sagemakerruntime) >= 1
Requires:      gem(aws-sdk-sagemakeredgemanager) >= 1
Requires:      gem(aws-sdk-savingsplans) >= 1
Requires:      gem(aws-sdk-scheduler) >= 1
Requires:      gem(aws-sdk-schemas) >= 1
Requires:      gem(aws-sdk-secretsmanager) >= 1
Requires:      gem(aws-sdk-securityhub) >= 1
Requires:      gem(aws-sdk-securitylake) >= 1
Requires:      gem(aws-sdk-serverlessapplicationrepository) >= 1
Requires:      gem(aws-sdk-servicecatalog) >= 1
Requires:      gem(aws-sdk-servicediscovery) >= 1
Requires:      gem(aws-sdk-servicequotas) >= 1
Requires:      gem(aws-sdk-shield) >= 1
Requires:      gem(aws-sdk-signer) >= 1
Requires:      gem(aws-sdk-simspaceweaver) >= 1
Requires:      gem(aws-sdk-simpledb) >= 1
Requires:      gem(aws-sdk-snowdevicemanagement) >= 1
Requires:      gem(aws-sdk-snowball) >= 1
Requires:      gem(aws-sdk-ssmsap) >= 1
Requires:      gem(aws-sdk-states) >= 1
Requires:      gem(aws-sdk-storagegateway) >= 1
Requires:      gem(aws-sdk-support) >= 1
Requires:      gem(aws-sdk-supportapp) >= 1
Requires:      gem(aws-sdk-synthetics) >= 1
Requires:      gem(aws-sdk-textract) >= 1
Requires:      gem(aws-sdk-timestreamquery) >= 1
Requires:      gem(aws-sdk-timestreamwrite) >= 1
Requires:      gem(aws-sdk-transcribeservice) >= 1
Requires:      gem(aws-sdk-transcribestreamingservice) >= 1
Requires:      gem(aws-sdk-transfer) >= 1
Requires:      gem(aws-sdk-translate) >= 1
Requires:      gem(aws-sdk-voiceid) >= 1
Requires:      gem(aws-sdk-waf) >= 1
Requires:      gem(aws-sdk-wafregional) >= 1
Requires:      gem(aws-sdk-wafv2) >= 1
Requires:      gem(aws-sdk-wellarchitected) >= 1
Requires:      gem(aws-sdk-workdocs) >= 1
Requires:      gem(aws-sdk-worklink) >= 1
Requires:      gem(aws-sdk-workmail) >= 1
Requires:      gem(aws-sdk-workmailmessageflow) >= 1
Requires:      gem(aws-sdk-workspaces) >= 1
Requires:      gem(aws-sdk-workspacesweb) >= 1
Requires:      gem(aws-sdk-xray) >= 1
Conflicts:     gem(aws-sdk-acm) >= 2
Conflicts:     gem(aws-sdk-acmpca) >= 2
Conflicts:     gem(aws-sdk-apigateway) >= 2
Conflicts:     gem(aws-sdk-arczonalshift) >= 2
Conflicts:     gem(aws-sdk-accessanalyzer) >= 2
Conflicts:     gem(aws-sdk-account) >= 2
Conflicts:     gem(aws-sdk-alexaforbusiness) >= 2
Conflicts:     gem(aws-sdk-amplify) >= 2
Conflicts:     gem(aws-sdk-amplifybackend) >= 2
Conflicts:     gem(aws-sdk-amplifyuibuilder) >= 2
Conflicts:     gem(aws-sdk-apigatewaymanagementapi) >= 2
Conflicts:     gem(aws-sdk-apigatewayv2) >= 2
Conflicts:     gem(aws-sdk-appconfig) >= 2
Conflicts:     gem(aws-sdk-appconfigdata) >= 2
Conflicts:     gem(aws-sdk-appintegrationsservice) >= 2
Conflicts:     gem(aws-sdk-appmesh) >= 2
Conflicts:     gem(aws-sdk-appregistry) >= 2
Conflicts:     gem(aws-sdk-apprunner) >= 2
Conflicts:     gem(aws-sdk-appstream) >= 2
Conflicts:     gem(aws-sdk-appsync) >= 2
Conflicts:     gem(aws-sdk-appflow) >= 2
Conflicts:     gem(aws-sdk-applicationautoscaling) >= 2
Conflicts:     gem(aws-sdk-applicationcostprofiler) >= 2
Conflicts:     gem(aws-sdk-applicationdiscoveryservice) >= 2
Conflicts:     gem(aws-sdk-applicationinsights) >= 2
Conflicts:     gem(aws-sdk-athena) >= 2
Conflicts:     gem(aws-sdk-auditmanager) >= 2
Conflicts:     gem(aws-sdk-augmentedairuntime) >= 2
Conflicts:     gem(aws-sdk-autoscaling) >= 2
Conflicts:     gem(aws-sdk-autoscalingplans) >= 2
Conflicts:     gem(aws-sdk-backup) >= 2
Conflicts:     gem(aws-sdk-backupgateway) >= 2
Conflicts:     gem(aws-sdk-backupstorage) >= 2
Conflicts:     gem(aws-sdk-batch) >= 2
Conflicts:     gem(aws-sdk-billingconductor) >= 2
Conflicts:     gem(aws-sdk-braket) >= 2
Conflicts:     gem(aws-sdk-budgets) >= 2
Conflicts:     gem(aws-sdk-chime) >= 2
Conflicts:     gem(aws-sdk-chimesdkidentity) >= 2
Conflicts:     gem(aws-sdk-chimesdkmediapipelines) >= 2
Conflicts:     gem(aws-sdk-chimesdkmeetings) >= 2
Conflicts:     gem(aws-sdk-chimesdkmessaging) >= 2
Conflicts:     gem(aws-sdk-chimesdkvoice) >= 2
Conflicts:     gem(aws-sdk-cleanrooms) >= 2
Conflicts:     gem(aws-sdk-cloud9) >= 2
Conflicts:     gem(aws-sdk-cloudcontrolapi) >= 2
Conflicts:     gem(aws-sdk-clouddirectory) >= 2
Conflicts:     gem(aws-sdk-cloudformation) >= 2
Conflicts:     gem(aws-sdk-cloudfront) >= 2
Conflicts:     gem(aws-sdk-cloudhsm) >= 2
Conflicts:     gem(aws-sdk-cloudhsmv2) >= 2
Conflicts:     gem(aws-sdk-cloudsearch) >= 2
Conflicts:     gem(aws-sdk-cloudsearchdomain) >= 2
Conflicts:     gem(aws-sdk-cloudtrail) >= 2
Conflicts:     gem(aws-sdk-cloudwatch) >= 2
Conflicts:     gem(aws-sdk-cloudwatchevents) >= 2
Conflicts:     gem(aws-sdk-cloudwatchevidently) >= 2
Conflicts:     gem(aws-sdk-cloudwatchlogs) >= 2
Conflicts:     gem(aws-sdk-cloudwatchrum) >= 2
Conflicts:     gem(aws-sdk-codeartifact) >= 2
Conflicts:     gem(aws-sdk-codebuild) >= 2
Conflicts:     gem(aws-sdk-codecatalyst) >= 2
Conflicts:     gem(aws-sdk-codecommit) >= 2
Conflicts:     gem(aws-sdk-codedeploy) >= 2
Conflicts:     gem(aws-sdk-codeguruprofiler) >= 2
Conflicts:     gem(aws-sdk-codegurureviewer) >= 2
Conflicts:     gem(aws-sdk-codepipeline) >= 2
Conflicts:     gem(aws-sdk-codestar) >= 2
Conflicts:     gem(aws-sdk-codestarnotifications) >= 2
Conflicts:     gem(aws-sdk-codestarconnections) >= 2
Conflicts:     gem(aws-sdk-cognitoidentity) >= 2
Conflicts:     gem(aws-sdk-cognitoidentityprovider) >= 2
Conflicts:     gem(aws-sdk-cognitosync) >= 2
Conflicts:     gem(aws-sdk-comprehend) >= 2
Conflicts:     gem(aws-sdk-comprehendmedical) >= 2
Conflicts:     gem(aws-sdk-computeoptimizer) >= 2
Conflicts:     gem(aws-sdk-configservice) >= 2
Conflicts:     gem(aws-sdk-connect) >= 2
Conflicts:     gem(aws-sdk-connectcampaignservice) >= 2
Conflicts:     gem(aws-sdk-connectcases) >= 2
Conflicts:     gem(aws-sdk-connectcontactlens) >= 2
Conflicts:     gem(aws-sdk-connectparticipant) >= 2
Conflicts:     gem(aws-sdk-connectwisdomservice) >= 2
Conflicts:     gem(aws-sdk-controltower) >= 2
Conflicts:     gem(aws-sdk-costexplorer) >= 2
Conflicts:     gem(aws-sdk-costandusagereportservice) >= 2
Conflicts:     gem(aws-sdk-customerprofiles) >= 2
Conflicts:     gem(aws-sdk-dax) >= 2
Conflicts:     gem(aws-sdk-dlm) >= 2
Conflicts:     gem(aws-sdk-dataexchange) >= 2
Conflicts:     gem(aws-sdk-datapipeline) >= 2
Conflicts:     gem(aws-sdk-datasync) >= 2
Conflicts:     gem(aws-sdk-databasemigrationservice) >= 2
Conflicts:     gem(aws-sdk-detective) >= 2
Conflicts:     gem(aws-sdk-devopsguru) >= 2
Conflicts:     gem(aws-sdk-devicefarm) >= 2
Conflicts:     gem(aws-sdk-directconnect) >= 2
Conflicts:     gem(aws-sdk-directoryservice) >= 2
Conflicts:     gem(aws-sdk-docdb) >= 2
Conflicts:     gem(aws-sdk-docdbelastic) >= 2
Conflicts:     gem(aws-sdk-drs) >= 2
Conflicts:     gem(aws-sdk-dynamodb) >= 2
Conflicts:     gem(aws-sdk-dynamodbstreams) >= 2
Conflicts:     gem(aws-sdk-ebs) >= 2
Conflicts:     gem(aws-sdk-ec2) >= 2
Conflicts:     gem(aws-sdk-ec2instanceconnect) >= 2
Conflicts:     gem(aws-sdk-ecr) >= 2
Conflicts:     gem(aws-sdk-ecrpublic) >= 2
Conflicts:     gem(aws-sdk-ecs) >= 2
Conflicts:     gem(aws-sdk-efs) >= 2
Conflicts:     gem(aws-sdk-eks) >= 2
Conflicts:     gem(aws-sdk-emr) >= 2
Conflicts:     gem(aws-sdk-emrcontainers) >= 2
Conflicts:     gem(aws-sdk-emrserverless) >= 2
Conflicts:     gem(aws-sdk-elasticache) >= 2
Conflicts:     gem(aws-sdk-elasticbeanstalk) >= 2
Conflicts:     gem(aws-sdk-elasticinference) >= 2
Conflicts:     gem(aws-sdk-elasticloadbalancing) >= 2
Conflicts:     gem(aws-sdk-elasticloadbalancingv2) >= 2
Conflicts:     gem(aws-sdk-elastictranscoder) >= 2
Conflicts:     gem(aws-sdk-elasticsearchservice) >= 2
Conflicts:     gem(aws-sdk-eventbridge) >= 2
Conflicts:     gem(aws-sdk-fis) >= 2
Conflicts:     gem(aws-sdk-fms) >= 2
Conflicts:     gem(aws-sdk-fsx) >= 2
Conflicts:     gem(aws-sdk-finspacedata) >= 2
Conflicts:     gem(aws-sdk-finspace) >= 2
Conflicts:     gem(aws-sdk-firehose) >= 2
Conflicts:     gem(aws-sdk-forecastqueryservice) >= 2
Conflicts:     gem(aws-sdk-forecastservice) >= 2
Conflicts:     gem(aws-sdk-frauddetector) >= 2
Conflicts:     gem(aws-sdk-gamelift) >= 2
Conflicts:     gem(aws-sdk-gamesparks) >= 2
Conflicts:     gem(aws-sdk-glacier) >= 2
Conflicts:     gem(aws-sdk-globalaccelerator) >= 2
Conflicts:     gem(aws-sdk-glue) >= 2
Conflicts:     gem(aws-sdk-gluedatabrew) >= 2
Conflicts:     gem(aws-sdk-greengrass) >= 2
Conflicts:     gem(aws-sdk-greengrassv2) >= 2
Conflicts:     gem(aws-sdk-groundstation) >= 2
Conflicts:     gem(aws-sdk-guardduty) >= 2
Conflicts:     gem(aws-sdk-health) >= 2
Conflicts:     gem(aws-sdk-healthlake) >= 2
Conflicts:     gem(aws-sdk-honeycode) >= 2
Conflicts:     gem(aws-sdk-iam) >= 2
Conflicts:     gem(aws-sdk-ivs) >= 2
Conflicts:     gem(aws-sdk-identitystore) >= 2
Conflicts:     gem(aws-sdk-imagebuilder) >= 2
Conflicts:     gem(aws-sdk-importexport) >= 2
Conflicts:     gem(aws-sdk-inspector) >= 2
Conflicts:     gem(aws-sdk-inspector2) >= 2
Conflicts:     gem(aws-sdk-iot) >= 2
Conflicts:     gem(aws-sdk-iot1clickdevicesservice) >= 2
Conflicts:     gem(aws-sdk-iot1clickprojects) >= 2
Conflicts:     gem(aws-sdk-iotanalytics) >= 2
Conflicts:     gem(aws-sdk-iotdataplane) >= 2
Conflicts:     gem(aws-sdk-iotdeviceadvisor) >= 2
Conflicts:     gem(aws-sdk-iotevents) >= 2
Conflicts:     gem(aws-sdk-ioteventsdata) >= 2
Conflicts:     gem(aws-sdk-iotfleethub) >= 2
Conflicts:     gem(aws-sdk-iotfleetwise) >= 2
Conflicts:     gem(aws-sdk-iotjobsdataplane) >= 2
Conflicts:     gem(aws-sdk-iotroborunner) >= 2
Conflicts:     gem(aws-sdk-iotsecuretunneling) >= 2
Conflicts:     gem(aws-sdk-iotsitewise) >= 2
Conflicts:     gem(aws-sdk-iotthingsgraph) >= 2
Conflicts:     gem(aws-sdk-iottwinmaker) >= 2
Conflicts:     gem(aws-sdk-iotwireless) >= 2
Conflicts:     gem(aws-sdk-ivschat) >= 2
Conflicts:     gem(aws-sdk-kms) >= 2
Conflicts:     gem(aws-sdk-kafka) >= 2
Conflicts:     gem(aws-sdk-kafkaconnect) >= 2
Conflicts:     gem(aws-sdk-kendra) >= 2
Conflicts:     gem(aws-sdk-kendraranking) >= 2
Conflicts:     gem(aws-sdk-keyspaces) >= 2
Conflicts:     gem(aws-sdk-kinesis) >= 2
Conflicts:     gem(aws-sdk-kinesisanalytics) >= 2
Conflicts:     gem(aws-sdk-kinesisanalyticsv2) >= 2
Conflicts:     gem(aws-sdk-kinesisvideo) >= 2
Conflicts:     gem(aws-sdk-kinesisvideoarchivedmedia) >= 2
Conflicts:     gem(aws-sdk-kinesisvideomedia) >= 2
Conflicts:     gem(aws-sdk-kinesisvideosignalingchannels) >= 2
Conflicts:     gem(aws-sdk-kinesisvideowebrtcstorage) >= 2
Conflicts:     gem(aws-sdk-lakeformation) >= 2
Conflicts:     gem(aws-sdk-lambda) >= 2
Conflicts:     gem(aws-sdk-lambdapreview) >= 2
Conflicts:     gem(aws-sdk-lex) >= 2
Conflicts:     gem(aws-sdk-lexmodelbuildingservice) >= 2
Conflicts:     gem(aws-sdk-lexmodelsv2) >= 2
Conflicts:     gem(aws-sdk-lexruntimev2) >= 2
Conflicts:     gem(aws-sdk-licensemanager) >= 2
Conflicts:     gem(aws-sdk-licensemanagerlinuxsubscriptions) >= 2
Conflicts:     gem(aws-sdk-licensemanagerusersubscriptions) >= 2
Conflicts:     gem(aws-sdk-lightsail) >= 2
Conflicts:     gem(aws-sdk-locationservice) >= 2
Conflicts:     gem(aws-sdk-lookoutequipment) >= 2
Conflicts:     gem(aws-sdk-lookoutmetrics) >= 2
Conflicts:     gem(aws-sdk-lookoutforvision) >= 2
Conflicts:     gem(aws-sdk-mq) >= 2
Conflicts:     gem(aws-sdk-mturk) >= 2
Conflicts:     gem(aws-sdk-mwaa) >= 2
Conflicts:     gem(aws-sdk-machinelearning) >= 2
Conflicts:     gem(aws-sdk-macie) >= 2
Conflicts:     gem(aws-sdk-macie2) >= 2
Conflicts:     gem(aws-sdk-mainframemodernization) >= 2
Conflicts:     gem(aws-sdk-managedblockchain) >= 2
Conflicts:     gem(aws-sdk-managedgrafana) >= 2
Conflicts:     gem(aws-sdk-marketplacecatalog) >= 2
Conflicts:     gem(aws-sdk-marketplacecommerceanalytics) >= 2
Conflicts:     gem(aws-sdk-marketplaceentitlementservice) >= 2
Conflicts:     gem(aws-sdk-marketplacemetering) >= 2
Conflicts:     gem(aws-sdk-mediaconnect) >= 2
Conflicts:     gem(aws-sdk-mediaconvert) >= 2
Conflicts:     gem(aws-sdk-medialive) >= 2
Conflicts:     gem(aws-sdk-mediapackage) >= 2
Conflicts:     gem(aws-sdk-mediapackagevod) >= 2
Conflicts:     gem(aws-sdk-mediastore) >= 2
Conflicts:     gem(aws-sdk-mediastoredata) >= 2
Conflicts:     gem(aws-sdk-mediatailor) >= 2
Conflicts:     gem(aws-sdk-memorydb) >= 2
Conflicts:     gem(aws-sdk-mgn) >= 2
Conflicts:     gem(aws-sdk-migrationhub) >= 2
Conflicts:     gem(aws-sdk-migrationhubconfig) >= 2
Conflicts:     gem(aws-sdk-migrationhuborchestrator) >= 2
Conflicts:     gem(aws-sdk-migrationhubrefactorspaces) >= 2
Conflicts:     gem(aws-sdk-migrationhubstrategyrecommendations) >= 2
Conflicts:     gem(aws-sdk-mobile) >= 2
Conflicts:     gem(aws-sdk-neptune) >= 2
Conflicts:     gem(aws-sdk-networkfirewall) >= 2
Conflicts:     gem(aws-sdk-networkmanager) >= 2
Conflicts:     gem(aws-sdk-nimblestudio) >= 2
Conflicts:     gem(aws-sdk-oam) >= 2
Conflicts:     gem(aws-sdk-omics) >= 2
Conflicts:     gem(aws-sdk-opensearchserverless) >= 2
Conflicts:     gem(aws-sdk-opensearchservice) >= 2
Conflicts:     gem(aws-sdk-opsworks) >= 2
Conflicts:     gem(aws-sdk-opsworkscm) >= 2
Conflicts:     gem(aws-sdk-organizations) >= 2
Conflicts:     gem(aws-sdk-outposts) >= 2
Conflicts:     gem(aws-sdk-pi) >= 2
Conflicts:     gem(aws-sdk-panorama) >= 2
Conflicts:     gem(aws-sdk-personalize) >= 2
Conflicts:     gem(aws-sdk-personalizeevents) >= 2
Conflicts:     gem(aws-sdk-personalizeruntime) >= 2
Conflicts:     gem(aws-sdk-pinpoint) >= 2
Conflicts:     gem(aws-sdk-pinpointemail) >= 2
Conflicts:     gem(aws-sdk-pinpointsmsvoice) >= 2
Conflicts:     gem(aws-sdk-pinpointsmsvoicev2) >= 2
Conflicts:     gem(aws-sdk-pipes) >= 2
Conflicts:     gem(aws-sdk-polly) >= 2
Conflicts:     gem(aws-sdk-pricing) >= 2
Conflicts:     gem(aws-sdk-privatenetworks) >= 2
Conflicts:     gem(aws-sdk-prometheusservice) >= 2
Conflicts:     gem(aws-sdk-proton) >= 2
Conflicts:     gem(aws-sdk-qldb) >= 2
Conflicts:     gem(aws-sdk-qldbsession) >= 2
Conflicts:     gem(aws-sdk-quicksight) >= 2
Conflicts:     gem(aws-sdk-ram) >= 2
Conflicts:     gem(aws-sdk-rds) >= 2
Conflicts:     gem(aws-sdk-rdsdataservice) >= 2
Conflicts:     gem(aws-sdk-recyclebin) >= 2
Conflicts:     gem(aws-sdk-redshift) >= 2
Conflicts:     gem(aws-sdk-redshiftdataapiservice) >= 2
Conflicts:     gem(aws-sdk-redshiftserverless) >= 2
Conflicts:     gem(aws-sdk-rekognition) >= 2
Conflicts:     gem(aws-sdk-resiliencehub) >= 2
Conflicts:     gem(aws-sdk-resourceexplorer2) >= 2
Conflicts:     gem(aws-sdk-resourcegroups) >= 2
Conflicts:     gem(aws-sdk-resourcegroupstaggingapi) >= 2
Conflicts:     gem(aws-sdk-robomaker) >= 2
Conflicts:     gem(aws-sdk-rolesanywhere) >= 2
Conflicts:     gem(aws-sdk-route53) >= 2
Conflicts:     gem(aws-sdk-route53domains) >= 2
Conflicts:     gem(aws-sdk-route53recoverycluster) >= 2
Conflicts:     gem(aws-sdk-route53recoverycontrolconfig) >= 2
Conflicts:     gem(aws-sdk-route53recoveryreadiness) >= 2
Conflicts:     gem(aws-sdk-route53resolver) >= 2
Conflicts:     gem(aws-sdk-s3) >= 2
Conflicts:     gem(aws-sdk-s3control) >= 2
Conflicts:     gem(aws-sdk-s3outposts) >= 2
Conflicts:     gem(aws-sdk-ses) >= 2
Conflicts:     gem(aws-sdk-sesv2) >= 2
Conflicts:     gem(aws-sdk-sms) >= 2
Conflicts:     gem(aws-sdk-sns) >= 2
Conflicts:     gem(aws-sdk-sqs) >= 2
Conflicts:     gem(aws-sdk-ssm) >= 2
Conflicts:     gem(aws-sdk-ssmcontacts) >= 2
Conflicts:     gem(aws-sdk-ssmincidents) >= 2
Conflicts:     gem(aws-sdk-ssoadmin) >= 2
Conflicts:     gem(aws-sdk-swf) >= 2
Conflicts:     gem(aws-sdk-sagemaker) >= 2
Conflicts:     gem(aws-sdk-sagemakerfeaturestoreruntime) >= 2
Conflicts:     gem(aws-sdk-sagemakergeospatial) >= 2
Conflicts:     gem(aws-sdk-sagemakermetrics) >= 2
Conflicts:     gem(aws-sdk-sagemakerruntime) >= 2
Conflicts:     gem(aws-sdk-sagemakeredgemanager) >= 2
Conflicts:     gem(aws-sdk-savingsplans) >= 2
Conflicts:     gem(aws-sdk-scheduler) >= 2
Conflicts:     gem(aws-sdk-schemas) >= 2
Conflicts:     gem(aws-sdk-secretsmanager) >= 2
Conflicts:     gem(aws-sdk-securityhub) >= 2
Conflicts:     gem(aws-sdk-securitylake) >= 2
Conflicts:     gem(aws-sdk-serverlessapplicationrepository) >= 2
Conflicts:     gem(aws-sdk-servicecatalog) >= 2
Conflicts:     gem(aws-sdk-servicediscovery) >= 2
Conflicts:     gem(aws-sdk-servicequotas) >= 2
Conflicts:     gem(aws-sdk-shield) >= 2
Conflicts:     gem(aws-sdk-signer) >= 2
Conflicts:     gem(aws-sdk-simspaceweaver) >= 2
Conflicts:     gem(aws-sdk-simpledb) >= 2
Conflicts:     gem(aws-sdk-snowdevicemanagement) >= 2
Conflicts:     gem(aws-sdk-snowball) >= 2
Conflicts:     gem(aws-sdk-ssmsap) >= 2
Conflicts:     gem(aws-sdk-states) >= 2
Conflicts:     gem(aws-sdk-storagegateway) >= 2
Conflicts:     gem(aws-sdk-support) >= 2
Conflicts:     gem(aws-sdk-supportapp) >= 2
Conflicts:     gem(aws-sdk-synthetics) >= 2
Conflicts:     gem(aws-sdk-textract) >= 2
Conflicts:     gem(aws-sdk-timestreamquery) >= 2
Conflicts:     gem(aws-sdk-timestreamwrite) >= 2
Conflicts:     gem(aws-sdk-transcribeservice) >= 2
Conflicts:     gem(aws-sdk-transcribestreamingservice) >= 2
Conflicts:     gem(aws-sdk-transfer) >= 2
Conflicts:     gem(aws-sdk-translate) >= 2
Conflicts:     gem(aws-sdk-voiceid) >= 2
Conflicts:     gem(aws-sdk-waf) >= 2
Conflicts:     gem(aws-sdk-wafregional) >= 2
Conflicts:     gem(aws-sdk-wafv2) >= 2
Conflicts:     gem(aws-sdk-wellarchitected) >= 2
Conflicts:     gem(aws-sdk-workdocs) >= 2
Conflicts:     gem(aws-sdk-worklink) >= 2
Conflicts:     gem(aws-sdk-workmail) >= 2
Conflicts:     gem(aws-sdk-workmailmessageflow) >= 2
Conflicts:     gem(aws-sdk-workspaces) >= 2
Conflicts:     gem(aws-sdk-workspacesweb) >= 2
Conflicts:     gem(aws-sdk-xray) >= 2
Provides:      gem(aws-sdk-resources) = 3.157.0

%description   -n gem-aws-sdk-resources
Provides resource oriented interfaces and other higher-level abstractions for
many AWS services. This gem is part of the official AWS SDK for Ruby.


%package       -n aws-v3-rb
Version:       3.157.0
Release:       alt1
Summary:       The official AWS SDK for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета aws-sdk-resources
Group:         Other
BuildArch:     noarch

Requires:      gem(aws-sdk-resources) = 3.157.0

%description   -n aws-v3-rb
The official AWS SDK for Ruby executable(s).

Provides resource oriented interfaces and other higher-level abstractions for
many AWS services. This gem is part of the official AWS SDK for Ruby.

%description   -n aws-v3-rb -l ru_RU.UTF-8
Исполнямка для самоцвета aws-sdk-resources.


%package       -n gem-aws-sdk-resources-doc
Version:       3.157.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-resources
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-resources) = 3.157.0

%description   -n gem-aws-sdk-resources-doc
The official AWS SDK for Ruby documentation files.

Provides resource oriented interfaces and other higher-level abstractions for
many AWS services. This gem is part of the official AWS SDK for Ruby.

%description   -n gem-aws-sdk-resources-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-resources.


%package       -n gem-aws-sdk-resources-devel
Version:       3.157.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-resources
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-resources) = 3.157.0

%description   -n gem-aws-sdk-resources-devel
The official AWS SDK for Ruby development package.

Provides resource oriented interfaces and other higher-level abstractions for
many AWS services. This gem is part of the official AWS SDK for Ruby.

%description   -n gem-aws-sdk-resources-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-resources.


%package       -n gem-aws-sdk-robomaker
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-robomaker) = 1.53.0

%description   -n gem-aws-sdk-robomaker
Official AWS Ruby gem for AWS RoboMaker (RoboMaker). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-robomaker-doc
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-robomaker
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-robomaker) = 1.53.0

%description   -n gem-aws-sdk-robomaker-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-robomaker-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-robomaker.


%package       -n gem-aws-sdk-robomaker-devel
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-robomaker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-robomaker) = 1.53.0

%description   -n gem-aws-sdk-robomaker-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-robomaker-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-robomaker.


%package       -n gem-aws-sdk-s3control
Version:       1.60.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sigv4) >= 1.1
Requires:      gem(aws-sdk-core) >= 3.165.0
Conflicts:     gem(aws-sigv4) >= 2
Conflicts:     gem(aws-sdk-core) >= 4
Provides:      gem(aws-sdk-s3control) = 1.60.0

%description   -n gem-aws-sdk-s3control
Official AWS Ruby gem for AWS S3 Control. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-s3control-doc
Version:       1.60.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-s3control
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-s3control) = 1.60.0

%description   -n gem-aws-sdk-s3control-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-s3control-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-s3control.


%package       -n gem-aws-sdk-s3control-devel
Version:       1.60.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-s3control
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-s3control) = 1.60.0

%description   -n gem-aws-sdk-s3control-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-s3control-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-s3control.


%package       -n gem-aws-sdk-sagemaker
Version:       1.164.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-sagemaker) = 1.164.0

%description   -n gem-aws-sdk-sagemaker
Official AWS Ruby gem for Amazon SageMaker Service (SageMaker). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-sagemaker-doc
Version:       1.164.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sagemaker
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemaker) = 1.164.0

%description   -n gem-aws-sdk-sagemaker-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon SageMaker Service (SageMaker). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sagemaker-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sagemaker.


%package       -n gem-aws-sdk-sagemaker-devel
Version:       1.164.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sagemaker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemaker) = 1.164.0

%description   -n gem-aws-sdk-sagemaker-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon SageMaker Service (SageMaker). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sagemaker-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sagemaker.


%package       -n gem-aws-sdk-scheduler
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EventBridge Scheduler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-scheduler) = 1.2.0

%description   -n gem-aws-sdk-scheduler
Official AWS Ruby gem for Amazon EventBridge Scheduler. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-scheduler-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EventBridge Scheduler documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-scheduler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-scheduler) = 1.2.0

%description   -n gem-aws-sdk-scheduler-doc
AWS SDK for Ruby - Amazon EventBridge Scheduler documentation files.

%description   -n gem-aws-sdk-scheduler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-scheduler.


%package       -n gem-aws-sdk-scheduler-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EventBridge Scheduler development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-scheduler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-scheduler) = 1.2.0

%description   -n gem-aws-sdk-scheduler-devel
AWS SDK for Ruby - Amazon EventBridge Scheduler development package.

%description   -n gem-aws-sdk-scheduler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-scheduler.


%package       -n gem-aws-sdk-translate
Version:       1.50.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-translate) = 1.50.0

%description   -n gem-aws-sdk-translate
Official AWS Ruby gem for Amazon Translate. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-translate-doc
Version:       1.50.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-translate
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-translate) = 1.50.0

%description   -n gem-aws-sdk-translate-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-translate-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-translate.


%package       -n gem-aws-sdk-translate-devel
Version:       1.50.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-translate
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-translate) = 1.50.0

%description   -n gem-aws-sdk-translate-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-translate-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-translate.


%package       -n gem-aws-sdk-apigateway
Version:       1.81.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-apigateway) = 1.81.0

%description   -n gem-aws-sdk-apigateway
Official AWS Ruby gem for Amazon API Gateway. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-apigateway-doc
Version:       1.81.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-apigateway
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-apigateway) = 1.81.0

%description   -n gem-aws-sdk-apigateway-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-apigateway-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-apigateway.


%package       -n gem-aws-sdk-apigateway-devel
Version:       1.81.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-apigateway
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-apigateway) = 1.81.0

%description   -n gem-aws-sdk-apigateway-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-apigateway-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-apigateway.


%package       -n gem-aws-sdk-cleanrooms
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Clean Rooms Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cleanrooms) = 1.1.0

%description   -n gem-aws-sdk-cleanrooms
Official AWS Ruby gem for AWS Clean Rooms Service. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-cleanrooms-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Clean Rooms Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cleanrooms
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cleanrooms) = 1.1.0

%description   -n gem-aws-sdk-cleanrooms-doc
AWS SDK for Ruby - AWS Clean Rooms Service documentation files.

%description   -n gem-aws-sdk-cleanrooms-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cleanrooms.


%package       -n gem-aws-sdk-cleanrooms-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Clean Rooms Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cleanrooms
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cleanrooms) = 1.1.0

%description   -n gem-aws-sdk-cleanrooms-devel
AWS SDK for Ruby - AWS Clean Rooms Service development package.

%description   -n gem-aws-sdk-cleanrooms-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cleanrooms.


%package       -n gem-aws-sdk-cloudfront
Version:       1.74.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cloudfront) = 1.74.0

%description   -n gem-aws-sdk-cloudfront
Official AWS Ruby gem for Amazon CloudFront (CloudFront). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-cloudfront-doc
Version:       1.74.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudfront
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudfront) = 1.74.0

%description   -n gem-aws-sdk-cloudfront-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon CloudFront (CloudFront). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudfront-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudfront.


%package       -n gem-aws-sdk-cloudfront-devel
Version:       1.74.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudfront
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudfront) = 1.74.0

%description   -n gem-aws-sdk-cloudfront-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon CloudFront (CloudFront). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudfront-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudfront.


%package       -n gem-aws-sdk-cloudhsmv2
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cloudhsmv2) = 1.44.0

%description   -n gem-aws-sdk-cloudhsmv2
Official AWS Ruby gem for AWS CloudHSM V2 (CloudHSM V2). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-cloudhsmv2-doc
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudhsmv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudhsmv2) = 1.44.0

%description   -n gem-aws-sdk-cloudhsmv2-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-cloudhsmv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudhsmv2.


%package       -n gem-aws-sdk-cloudhsmv2-devel
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudhsmv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudhsmv2) = 1.44.0

%description   -n gem-aws-sdk-cloudhsmv2-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-cloudhsmv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudhsmv2.


%package       -n gem-aws-sdk-cloudtrail
Version:       1.56.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cloudtrail) = 1.56.0

%description   -n gem-aws-sdk-cloudtrail
Official AWS Ruby gem for AWS CloudTrail (CloudTrail). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-cloudtrail-doc
Version:       1.56.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudtrail
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudtrail) = 1.56.0

%description   -n gem-aws-sdk-cloudtrail-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-cloudtrail-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudtrail.


%package       -n gem-aws-sdk-cloudtrail-devel
Version:       1.56.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudtrail
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudtrail) = 1.56.0

%description   -n gem-aws-sdk-cloudtrail-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-cloudtrail-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudtrail.


%package       -n gem-aws-sdk-cloudwatch
Version:       1.71.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cloudwatch) = 1.71.0

%description   -n gem-aws-sdk-cloudwatch
Official AWS Ruby gem for Amazon CloudWatch (CloudWatch). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-cloudwatch-doc
Version:       1.71.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudwatch
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatch) = 1.71.0

%description   -n gem-aws-sdk-cloudwatch-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon CloudWatch (CloudWatch). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudwatch-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudwatch.


%package       -n gem-aws-sdk-cloudwatch-devel
Version:       1.71.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudwatch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatch) = 1.71.0

%description   -n gem-aws-sdk-cloudwatch-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon CloudWatch (CloudWatch). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudwatch-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudwatch.


%package       -n gem-aws-sdk-codecommit
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-codecommit) = 1.53.0

%description   -n gem-aws-sdk-codecommit
Official AWS Ruby gem for AWS CodeCommit (CodeCommit). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-codecommit-doc
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codecommit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codecommit) = 1.53.0

%description   -n gem-aws-sdk-codecommit-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-codecommit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codecommit.


%package       -n gem-aws-sdk-codecommit-devel
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codecommit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codecommit) = 1.53.0

%description   -n gem-aws-sdk-codecommit-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-codecommit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codecommit.


%package       -n gem-aws-sdk-codedeploy
Version:       1.52.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-codedeploy) = 1.52.0

%description   -n gem-aws-sdk-codedeploy
Official AWS Ruby gem for AWS CodeDeploy (CodeDeploy). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-codedeploy-doc
Version:       1.52.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codedeploy
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codedeploy) = 1.52.0

%description   -n gem-aws-sdk-codedeploy-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-codedeploy-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codedeploy.


%package       -n gem-aws-sdk-codedeploy-devel
Version:       1.52.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codedeploy
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codedeploy) = 1.52.0

%description   -n gem-aws-sdk-codedeploy-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-codedeploy-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codedeploy.


%package       -n gem-aws-sdk-comprehend
Version:       1.65.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-comprehend) = 1.65.0

%description   -n gem-aws-sdk-comprehend
Official AWS Ruby gem for Amazon Comprehend. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-comprehend-doc
Version:       1.65.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-comprehend
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-comprehend) = 1.65.0

%description   -n gem-aws-sdk-comprehend-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-comprehend-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-comprehend.


%package       -n gem-aws-sdk-comprehend-devel
Version:       1.65.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-comprehend
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-comprehend) = 1.65.0

%description   -n gem-aws-sdk-comprehend-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-comprehend-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-comprehend.


%package       -n gem-aws-sdk-devicefarm
Version:       1.54.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-devicefarm) = 1.54.0

%description   -n gem-aws-sdk-devicefarm
Official AWS Ruby gem for AWS Device Farm. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-devicefarm-doc
Version:       1.54.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-devicefarm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-devicefarm) = 1.54.0

%description   -n gem-aws-sdk-devicefarm-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-devicefarm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-devicefarm.


%package       -n gem-aws-sdk-devicefarm-devel
Version:       1.54.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-devicefarm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-devicefarm) = 1.54.0

%description   -n gem-aws-sdk-devicefarm-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-devicefarm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-devicefarm.


%package       -n gem-aws-sdk-devopsguru
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-devopsguru) = 1.28.0

%description   -n gem-aws-sdk-devopsguru
Official AWS Ruby gem for Amazon DevOps Guru. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-devopsguru-doc
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-devopsguru
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-devopsguru) = 1.28.0

%description   -n gem-aws-sdk-devopsguru-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-devopsguru-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-devopsguru.


%package       -n gem-aws-sdk-devopsguru-devel
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-devopsguru
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-devopsguru) = 1.28.0

%description   -n gem-aws-sdk-devopsguru-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-devopsguru-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-devopsguru.


%package       -n gem-aws-sdk-gamesparks
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - GameSparks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-gamesparks) = 1.4.0

%description   -n gem-aws-sdk-gamesparks
Official AWS Ruby gem for GameSparks. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-gamesparks-doc
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - GameSparks documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-gamesparks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-gamesparks) = 1.4.0

%description   -n gem-aws-sdk-gamesparks-doc
AWS SDK for Ruby - GameSparks documentation files.

Official AWS Ruby gem for GameSparks. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-gamesparks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-gamesparks.


%package       -n gem-aws-sdk-gamesparks-devel
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - GameSparks development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-gamesparks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-gamesparks) = 1.4.0

%description   -n gem-aws-sdk-gamesparks-devel
AWS SDK for Ruby - GameSparks development package.

Official AWS Ruby gem for GameSparks. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-gamesparks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-gamesparks.


%package       -n gem-aws-sdk-greengrass
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-greengrass) = 1.53.0

%description   -n gem-aws-sdk-greengrass
Official AWS Ruby gem for AWS Greengrass. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-greengrass-doc
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-greengrass
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-greengrass) = 1.53.0

%description   -n gem-aws-sdk-greengrass-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-greengrass-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-greengrass.


%package       -n gem-aws-sdk-greengrass-devel
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-greengrass
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-greengrass) = 1.53.0

%description   -n gem-aws-sdk-greengrass-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-greengrass-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-greengrass.


%package       -n gem-aws-sdk-healthlake
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-healthlake) = 1.15.0

%description   -n gem-aws-sdk-healthlake
Official AWS Ruby gem for Amazon HealthLake (HealthLake). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-healthlake-doc
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-healthlake
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-healthlake) = 1.15.0

%description   -n gem-aws-sdk-healthlake-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon HealthLake (HealthLake). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-healthlake-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-healthlake.


%package       -n gem-aws-sdk-healthlake-devel
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-healthlake
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-healthlake) = 1.15.0

%description   -n gem-aws-sdk-healthlake-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon HealthLake (HealthLake). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-healthlake-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-healthlake.


%package       -n gem-aws-sdk-inspector2
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - Inspector2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-inspector2) = 1.10.0

%description   -n gem-aws-sdk-inspector2
Official AWS Ruby gem for Inspector2. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-inspector2-doc
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - Inspector2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-inspector2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-inspector2) = 1.10.0

%description   -n gem-aws-sdk-inspector2-doc
AWS SDK for Ruby - Inspector2 documentation files.

Official AWS Ruby gem for Inspector2. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-inspector2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-inspector2.


%package       -n gem-aws-sdk-inspector2-devel
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - Inspector2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-inspector2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-inspector2) = 1.10.0

%description   -n gem-aws-sdk-inspector2-devel
AWS SDK for Ruby - Inspector2 development package.

Official AWS Ruby gem for Inspector2. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-inspector2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-inspector2.


%package       -n gem-aws-sdk-mediastore
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-mediastore) = 1.43.0

%description   -n gem-aws-sdk-mediastore
Official AWS Ruby gem for AWS Elemental MediaStore (MediaStore). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mediastore-doc
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mediastore
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mediastore) = 1.43.0

%description   -n gem-aws-sdk-mediastore-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Elemental MediaStore (MediaStore). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediastore-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mediastore.


%package       -n gem-aws-sdk-mediastore-devel
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mediastore
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mediastore) = 1.43.0

%description   -n gem-aws-sdk-mediastore-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Elemental MediaStore (MediaStore). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediastore-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mediastore.


%package       -n gem-aws-sdk-opsworkscm
Version:       1.54.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-opsworkscm) = 1.54.0

%description   -n gem-aws-sdk-opsworkscm
Official AWS Ruby gem for AWS OpsWorks CM (OpsWorksCM). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-opsworkscm-doc
Version:       1.54.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-opsworkscm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-opsworkscm) = 1.54.0

%description   -n gem-aws-sdk-opsworkscm-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-opsworkscm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-opsworkscm.


%package       -n gem-aws-sdk-opsworkscm-devel
Version:       1.54.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-opsworkscm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-opsworkscm) = 1.54.0

%description   -n gem-aws-sdk-opsworkscm-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-opsworkscm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-opsworkscm.


%package       -n gem-aws-sdk-quicksight
Version:       1.74.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-quicksight) = 1.74.0

%description   -n gem-aws-sdk-quicksight
Official AWS Ruby gem for Amazon QuickSight. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-quicksight-doc
Version:       1.74.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-quicksight
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-quicksight) = 1.74.0

%description   -n gem-aws-sdk-quicksight-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-quicksight-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-quicksight.


%package       -n gem-aws-sdk-quicksight-devel
Version:       1.74.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-quicksight
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-quicksight) = 1.74.0

%description   -n gem-aws-sdk-quicksight-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-quicksight-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-quicksight.


%package       -n gem-aws-sdk-recyclebin
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Recycle Bin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-recyclebin) = 1.8.0

%description   -n gem-aws-sdk-recyclebin
Official AWS Ruby gem for Amazon Recycle Bin. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-recyclebin-doc
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Recycle Bin documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-recyclebin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-recyclebin) = 1.8.0

%description   -n gem-aws-sdk-recyclebin-doc
AWS SDK for Ruby - Amazon Recycle Bin documentation files.

%description   -n gem-aws-sdk-recyclebin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-recyclebin.


%package       -n gem-aws-sdk-recyclebin-devel
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Recycle Bin development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-recyclebin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-recyclebin) = 1.8.0

%description   -n gem-aws-sdk-recyclebin-devel
AWS SDK for Ruby - Amazon Recycle Bin development package.

%description   -n gem-aws-sdk-recyclebin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-recyclebin.


%package       -n gem-aws-sdk-s3outposts
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-s3outposts) = 1.15.0

%description   -n gem-aws-sdk-s3outposts
Official AWS Ruby gem for Amazon S3 on Outposts (Amazon S3 Outposts). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-s3outposts-doc
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-s3outposts
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-s3outposts) = 1.15.0

%description   -n gem-aws-sdk-s3outposts-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon S3 on Outposts (Amazon S3 Outposts). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-s3outposts-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-s3outposts.


%package       -n gem-aws-sdk-s3outposts-devel
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-s3outposts
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-s3outposts) = 1.15.0

%description   -n gem-aws-sdk-s3outposts-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon S3 on Outposts (Amazon S3 Outposts). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-s3outposts-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-s3outposts.


%package       -n gem-aws-sdk-supportapp
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - SupportApp
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-supportapp) = 1.4.0

%description   -n gem-aws-sdk-supportapp
Official AWS Ruby gem for AWS Support App (SupportApp). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-supportapp-doc
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - SupportApp documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-supportapp
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-supportapp) = 1.4.0

%description   -n gem-aws-sdk-supportapp-doc
AWS SDK for Ruby - SupportApp documentation files.

%description   -n gem-aws-sdk-supportapp-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-supportapp.


%package       -n gem-aws-sdk-supportapp-devel
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - SupportApp development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-supportapp
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-supportapp) = 1.4.0

%description   -n gem-aws-sdk-supportapp-devel
AWS SDK for Ruby - SupportApp development package.

%description   -n gem-aws-sdk-supportapp-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-supportapp.


%package       -n gem-aws-sdk-synthetics
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-synthetics) = 1.30.0

%description   -n gem-aws-sdk-synthetics
Official AWS Ruby gem for Synthetics. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-synthetics-doc
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-synthetics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-synthetics) = 1.30.0

%description   -n gem-aws-sdk-synthetics-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Synthetics. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-synthetics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-synthetics.


%package       -n gem-aws-sdk-synthetics-devel
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-synthetics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-synthetics) = 1.30.0

%description   -n gem-aws-sdk-synthetics-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Synthetics. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-synthetics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-synthetics.


%package       -n gem-aws-sdk-workspaces
Version:       1.78.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-workspaces) = 1.78.0

%description   -n gem-aws-sdk-workspaces
Official AWS Ruby gem for Amazon WorkSpaces. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-workspaces-doc
Version:       1.78.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-workspaces
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-workspaces) = 1.78.0

%description   -n gem-aws-sdk-workspaces-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-workspaces-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-workspaces.


%package       -n gem-aws-sdk-workspaces-devel
Version:       1.78.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-workspaces
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-workspaces) = 1.78.0

%description   -n gem-aws-sdk-workspaces-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-workspaces-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-workspaces.


%package       -n gem-aws-sdk-appregistry
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-appregistry) = 1.19.0

%description   -n gem-aws-sdk-appregistry
Official AWS Ruby gem for AWS Service Catalog App Registry (AppRegistry). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-appregistry-doc
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appregistry
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appregistry) = 1.19.0

%description   -n gem-aws-sdk-appregistry-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Service Catalog App Registry (AppRegistry). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-appregistry-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appregistry.


%package       -n gem-aws-sdk-appregistry-devel
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appregistry
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appregistry) = 1.19.0

%description   -n gem-aws-sdk-appregistry-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Service Catalog App Registry (AppRegistry). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-appregistry-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appregistry.


%package       -n gem-aws-sdk-autoscaling
Version:       1.85.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-autoscaling) = 1.85.0

%description   -n gem-aws-sdk-autoscaling
Official AWS Ruby gem for Auto Scaling. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-autoscaling-doc
Version:       1.85.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-autoscaling
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-autoscaling) = 1.85.0

%description   -n gem-aws-sdk-autoscaling-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-autoscaling-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-autoscaling.


%package       -n gem-aws-sdk-autoscaling-devel
Version:       1.85.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-autoscaling
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-autoscaling) = 1.85.0

%description   -n gem-aws-sdk-autoscaling-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-autoscaling-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-autoscaling.


%package       -n gem-aws-sdk-cloudsearch
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cloudsearch) = 1.42.0

%description   -n gem-aws-sdk-cloudsearch
Official AWS Ruby gem for Amazon CloudSearch. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-cloudsearch-doc
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudsearch
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudsearch) = 1.42.0

%description   -n gem-aws-sdk-cloudsearch-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-cloudsearch-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudsearch.


%package       -n gem-aws-sdk-cloudsearch-devel
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudsearch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudsearch) = 1.42.0

%description   -n gem-aws-sdk-cloudsearch-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-cloudsearch-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudsearch.


%package       -n gem-aws-sdk-cognitosync
Version:       1.38.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cognitosync) = 1.38.0

%description   -n gem-aws-sdk-cognitosync
Official AWS Ruby gem for Amazon Cognito Sync. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-cognitosync-doc
Version:       1.38.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cognitosync
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cognitosync) = 1.38.0

%description   -n gem-aws-sdk-cognitosync-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-cognitosync-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cognitosync.


%package       -n gem-aws-sdk-cognitosync-devel
Version:       1.38.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cognitosync
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cognitosync) = 1.38.0

%description   -n gem-aws-sdk-cognitosync-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-cognitosync-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cognitosync.


%package       -n gem-aws-sdk-elasticache
Version:       1.84.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-elasticache) = 1.84.0

%description   -n gem-aws-sdk-elasticache
Official AWS Ruby gem for Amazon ElastiCache. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-elasticache-doc
Version:       1.84.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-elasticache
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticache) = 1.84.0

%description   -n gem-aws-sdk-elasticache-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-elasticache-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-elasticache.


%package       -n gem-aws-sdk-elasticache-devel
Version:       1.84.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-elasticache
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticache) = 1.84.0

%description   -n gem-aws-sdk-elasticache-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-elasticache-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-elasticache.


%package       -n gem-aws-sdk-eventbridge
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-eventbridge) = 1.42.0

%description   -n gem-aws-sdk-eventbridge
Official AWS Ruby gem for Amazon EventBridge. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-eventbridge-doc
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-eventbridge
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-eventbridge) = 1.42.0

%description   -n gem-aws-sdk-eventbridge-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-eventbridge-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-eventbridge.


%package       -n gem-aws-sdk-eventbridge-devel
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-eventbridge
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-eventbridge) = 1.42.0

%description   -n gem-aws-sdk-eventbridge-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-eventbridge-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-eventbridge.


%package       -n gem-aws-sdk-iotfleethub
Version:       1.13.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iotfleethub) = 1.13.0

%description   -n gem-aws-sdk-iotfleethub
Official AWS Ruby gem for AWS IoT Fleet Hub. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-iotfleethub-doc
Version:       1.13.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotfleethub
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotfleethub) = 1.13.0

%description   -n gem-aws-sdk-iotfleethub-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-iotfleethub-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotfleethub.


%package       -n gem-aws-sdk-iotfleethub-devel
Version:       1.13.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotfleethub
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotfleethub) = 1.13.0

%description   -n gem-aws-sdk-iotfleethub-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-iotfleethub-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotfleethub.


%package       -n gem-aws-sdk-iotsitewise
Version:       1.48.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iotsitewise) = 1.48.0

%description   -n gem-aws-sdk-iotsitewise
Official AWS Ruby gem for AWS IoT SiteWise. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-iotsitewise-doc
Version:       1.48.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotsitewise
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotsitewise) = 1.48.0

%description   -n gem-aws-sdk-iotsitewise-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-iotsitewise-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotsitewise.


%package       -n gem-aws-sdk-iotsitewise-devel
Version:       1.48.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotsitewise
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotsitewise) = 1.48.0

%description   -n gem-aws-sdk-iotsitewise-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-iotsitewise-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotsitewise.


%package       -n gem-aws-sdk-iotwireless
Version:       1.29.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iotwireless) = 1.29.0

%description   -n gem-aws-sdk-iotwireless
Official AWS Ruby gem for AWS IoT Wireless. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-iotwireless-doc
Version:       1.29.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotwireless
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotwireless) = 1.29.0

%description   -n gem-aws-sdk-iotwireless-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-iotwireless-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotwireless.


%package       -n gem-aws-sdk-iotwireless-devel
Version:       1.29.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotwireless
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotwireless) = 1.29.0

%description   -n gem-aws-sdk-iotwireless-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-iotwireless-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotwireless.


%package       -n gem-aws-sdk-lexmodelsv2
Version:       1.31.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-lexmodelsv2) = 1.31.0

%description   -n gem-aws-sdk-lexmodelsv2
Official AWS Ruby gem for Amazon Lex Model Building V2 (Lex Models V2). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-lexmodelsv2-doc
Version:       1.31.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lexmodelsv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lexmodelsv2) = 1.31.0

%description   -n gem-aws-sdk-lexmodelsv2-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Lex Model Building V2 (Lex Models V2). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lexmodelsv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lexmodelsv2.


%package       -n gem-aws-sdk-lexmodelsv2-devel
Version:       1.31.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lexmodelsv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lexmodelsv2) = 1.31.0

%description   -n gem-aws-sdk-lexmodelsv2-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Lex Model Building V2 (Lex Models V2). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lexmodelsv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lexmodelsv2.


%package       -n gem-aws-sdk-mediatailor
Version:       1.59.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-mediatailor) = 1.59.0

%description   -n gem-aws-sdk-mediatailor
Official AWS Ruby gem for AWS MediaTailor (MediaTailor). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-mediatailor-doc
Version:       1.59.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mediatailor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mediatailor) = 1.59.0

%description   -n gem-aws-sdk-mediatailor-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-mediatailor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mediatailor.


%package       -n gem-aws-sdk-mediatailor-devel
Version:       1.59.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mediatailor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mediatailor) = 1.59.0

%description   -n gem-aws-sdk-mediatailor-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-mediatailor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mediatailor.


%package       -n gem-aws-sdk-personalize
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-personalize) = 1.46.0

%description   -n gem-aws-sdk-personalize
Official AWS Ruby gem for Amazon Personalize. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-personalize-doc
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-personalize
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-personalize) = 1.46.0

%description   -n gem-aws-sdk-personalize-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-personalize-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-personalize.


%package       -n gem-aws-sdk-personalize-devel
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-personalize
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-personalize) = 1.46.0

%description   -n gem-aws-sdk-personalize-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-personalize-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-personalize.


%package       -n gem-aws-sdk-qldbsession
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-qldbsession) = 1.24.0

%description   -n gem-aws-sdk-qldbsession
Official AWS Ruby gem for Amazon QLDB Session (QLDB Session). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-qldbsession-doc
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-qldbsession
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-qldbsession) = 1.24.0

%description   -n gem-aws-sdk-qldbsession-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon QLDB Session (QLDB Session). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-qldbsession-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-qldbsession.


%package       -n gem-aws-sdk-qldbsession-devel
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-qldbsession
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-qldbsession) = 1.24.0

%description   -n gem-aws-sdk-qldbsession-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon QLDB Session (QLDB Session). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-qldbsession-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-qldbsession.


%package       -n gem-aws-sdk-rekognition
Version:       1.74.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-rekognition) = 1.74.0

%description   -n gem-aws-sdk-rekognition
Official AWS Ruby gem for Amazon Rekognition. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-rekognition-doc
Version:       1.74.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-rekognition
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-rekognition) = 1.74.0

%description   -n gem-aws-sdk-rekognition-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-rekognition-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-rekognition.


%package       -n gem-aws-sdk-rekognition-devel
Version:       1.74.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-rekognition
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-rekognition) = 1.74.0

%description   -n gem-aws-sdk-rekognition-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-rekognition-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-rekognition.


%package       -n gem-aws-sdk-securityhub
Version:       1.75.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-securityhub) = 1.75.0

%description   -n gem-aws-sdk-securityhub
Official AWS Ruby gem for AWS SecurityHub. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-securityhub-doc
Version:       1.75.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-securityhub
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-securityhub) = 1.75.0

%description   -n gem-aws-sdk-securityhub-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-securityhub-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-securityhub.


%package       -n gem-aws-sdk-securityhub-devel
Version:       1.75.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-securityhub
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-securityhub) = 1.75.0

%description   -n gem-aws-sdk-securityhub-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-securityhub-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-securityhub.


%package       -n gem-aws-sdk-ssmcontacts
Version:       1.16.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ssmcontacts) = 1.16.0

%description   -n gem-aws-sdk-ssmcontacts
Official AWS Ruby gem for AWS Systems Manager Incident Manager Contacts (SSM
Contacts). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ssmcontacts-doc
Version:       1.16.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ssmcontacts
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ssmcontacts) = 1.16.0

%description   -n gem-aws-sdk-ssmcontacts-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Systems Manager Incident Manager Contacts (SSM
Contacts). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssmcontacts-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ssmcontacts.


%package       -n gem-aws-sdk-ssmcontacts-devel
Version:       1.16.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ssmcontacts
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ssmcontacts) = 1.16.0

%description   -n gem-aws-sdk-ssmcontacts-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Systems Manager Incident Manager Contacts (SSM
Contacts). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssmcontacts-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ssmcontacts.


%package       -n gem-aws-sdk-wafregional
Version:       1.50.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-wafregional) = 1.50.0

%description   -n gem-aws-sdk-wafregional
Official AWS Ruby gem for AWS WAF Regional (WAF Regional). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-wafregional-doc
Version:       1.50.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-wafregional
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-wafregional) = 1.50.0

%description   -n gem-aws-sdk-wafregional-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS WAF Regional (WAF Regional). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-wafregional-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-wafregional.


%package       -n gem-aws-sdk-wafregional-devel
Version:       1.50.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-wafregional
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-wafregional) = 1.50.0

%description   -n gem-aws-sdk-wafregional-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS WAF Regional (WAF Regional). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-wafregional-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-wafregional.


%package       -n gem-aws-sdk-apigatewayv2
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-apigatewayv2) = 1.44.0

%description   -n gem-aws-sdk-apigatewayv2
Official AWS Ruby gem for AmazonApiGatewayV2. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-apigatewayv2-doc
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-apigatewayv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-apigatewayv2) = 1.44.0

%description   -n gem-aws-sdk-apigatewayv2-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-apigatewayv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-apigatewayv2.


%package       -n gem-aws-sdk-apigatewayv2-devel
Version:       1.44.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-apigatewayv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-apigatewayv2) = 1.44.0

%description   -n gem-aws-sdk-apigatewayv2-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-apigatewayv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-apigatewayv2.


%package       -n gem-aws-sdk-auditmanager
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-auditmanager) = 1.30.0

%description   -n gem-aws-sdk-auditmanager
Official AWS Ruby gem for AWS Audit Manager. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-auditmanager-doc
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-auditmanager
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-auditmanager) = 1.30.0

%description   -n gem-aws-sdk-auditmanager-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-auditmanager-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-auditmanager.


%package       -n gem-aws-sdk-auditmanager-devel
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-auditmanager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-auditmanager) = 1.30.0

%description   -n gem-aws-sdk-auditmanager-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-auditmanager-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-auditmanager.


%package       -n gem-aws-sdk-codeartifact
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-codeartifact) = 1.24.0

%description   -n gem-aws-sdk-codeartifact
Official AWS Ruby gem for CodeArtifact. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-codeartifact-doc
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codeartifact
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codeartifact) = 1.24.0

%description   -n gem-aws-sdk-codeartifact-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-codeartifact-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codeartifact.


%package       -n gem-aws-sdk-codeartifact-devel
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codeartifact
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codeartifact) = 1.24.0

%description   -n gem-aws-sdk-codeartifact-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-codeartifact-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codeartifact.


%package       -n gem-aws-sdk-codecatalyst
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CodeCatalyst
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Conflicts:     gem(aws-sdk-core) >= 4
Provides:      gem(aws-sdk-codecatalyst) = 1.1.0

%description   -n gem-aws-sdk-codecatalyst
Official AWS Ruby gem for Amazon CodeCatalyst. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-codecatalyst-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CodeCatalyst documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codecatalyst
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codecatalyst) = 1.1.0

%description   -n gem-aws-sdk-codecatalyst-doc
AWS SDK for Ruby - Amazon CodeCatalyst documentation files.

%description   -n gem-aws-sdk-codecatalyst-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codecatalyst.


%package       -n gem-aws-sdk-codecatalyst-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CodeCatalyst development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codecatalyst
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codecatalyst) = 1.1.0

%description   -n gem-aws-sdk-codecatalyst-devel
AWS SDK for Ruby - Amazon CodeCatalyst development package.

%description   -n gem-aws-sdk-codecatalyst-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codecatalyst.


%package       -n gem-aws-sdk-codepipeline
Version:       1.55.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-codepipeline) = 1.55.0

%description   -n gem-aws-sdk-codepipeline
Official AWS Ruby gem for AWS CodePipeline (CodePipeline). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-codepipeline-doc
Version:       1.55.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codepipeline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codepipeline) = 1.55.0

%description   -n gem-aws-sdk-codepipeline-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS CodePipeline (CodePipeline). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-codepipeline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codepipeline.


%package       -n gem-aws-sdk-codepipeline-devel
Version:       1.55.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codepipeline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codepipeline) = 1.55.0

%description   -n gem-aws-sdk-codepipeline-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS CodePipeline (CodePipeline). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-codepipeline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codepipeline.


%package       -n gem-aws-sdk-connectcases
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - ConnectCases
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-connectcases) = 1.3.0

%description   -n gem-aws-sdk-connectcases
Official AWS Ruby gem for Amazon Connect Cases (ConnectCases). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-connectcases-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - ConnectCases documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-connectcases
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-connectcases) = 1.3.0

%description   -n gem-aws-sdk-connectcases-doc
AWS SDK for Ruby - ConnectCases documentation files.

Official AWS Ruby gem for Amazon Connect Cases (ConnectCases). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-connectcases-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-connectcases.


%package       -n gem-aws-sdk-connectcases-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - ConnectCases development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-connectcases
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-connectcases) = 1.3.0

%description   -n gem-aws-sdk-connectcases-devel
AWS SDK for Ruby - ConnectCases development package.

Official AWS Ruby gem for Amazon Connect Cases (ConnectCases). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-connectcases-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-connectcases.


%package       -n gem-aws-sdk-controltower
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Control Tower
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-controltower) = 1.2.0

%description   -n gem-aws-sdk-controltower
Official AWS Ruby gem for AWS Control Tower. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-controltower-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Control Tower documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-controltower
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-controltower) = 1.2.0

%description   -n gem-aws-sdk-controltower-doc
AWS SDK for Ruby - AWS Control Tower documentation files.

%description   -n gem-aws-sdk-controltower-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-controltower.


%package       -n gem-aws-sdk-controltower-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Control Tower development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-controltower
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-controltower) = 1.2.0

%description   -n gem-aws-sdk-controltower-devel
AWS SDK for Ruby - AWS Control Tower development package.

%description   -n gem-aws-sdk-controltower-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-controltower.


%package       -n gem-aws-sdk-costexplorer
Version:       1.83.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-costexplorer) = 1.83.0

%description   -n gem-aws-sdk-costexplorer
Official AWS Ruby gem for AWS Cost Explorer Service (AWS Cost Explorer). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-costexplorer-doc
Version:       1.83.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-costexplorer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-costexplorer) = 1.83.0

%description   -n gem-aws-sdk-costexplorer-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Cost Explorer Service (AWS Cost Explorer). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-costexplorer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-costexplorer.


%package       -n gem-aws-sdk-costexplorer-devel
Version:       1.83.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-costexplorer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-costexplorer) = 1.83.0

%description   -n gem-aws-sdk-costexplorer-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Cost Explorer Service (AWS Cost Explorer). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-costexplorer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-costexplorer.


%package       -n gem-aws-sdk-dataexchange
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-dataexchange) = 1.30.0

%description   -n gem-aws-sdk-dataexchange
Official AWS Ruby gem for AWS Data Exchange. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-dataexchange-doc
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-dataexchange
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-dataexchange) = 1.30.0

%description   -n gem-aws-sdk-dataexchange-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-dataexchange-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-dataexchange.


%package       -n gem-aws-sdk-dataexchange-devel
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-dataexchange
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-dataexchange) = 1.30.0

%description   -n gem-aws-sdk-dataexchange-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-dataexchange-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-dataexchange.


%package       -n gem-aws-sdk-datapipeline
Version:       1.38.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-datapipeline) = 1.38.0

%description   -n gem-aws-sdk-datapipeline
Official AWS Ruby gem for AWS Data Pipeline. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-datapipeline-doc
Version:       1.38.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-datapipeline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-datapipeline) = 1.38.0

%description   -n gem-aws-sdk-datapipeline-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-datapipeline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-datapipeline.


%package       -n gem-aws-sdk-datapipeline-devel
Version:       1.38.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-datapipeline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-datapipeline) = 1.38.0

%description   -n gem-aws-sdk-datapipeline-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-datapipeline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-datapipeline.


%package       -n gem-aws-sdk-docdbelastic
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - DocDB Elastic
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-docdbelastic) = 1.1.0

%description   -n gem-aws-sdk-docdbelastic
Official AWS Ruby gem for Amazon DocumentDB Elastic Clusters (DocDB Elastic).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-docdbelastic-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - DocDB Elastic documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-docdbelastic
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-docdbelastic) = 1.1.0

%description   -n gem-aws-sdk-docdbelastic-doc
AWS SDK for Ruby - DocDB Elastic documentation files.

Official AWS Ruby gem for Amazon DocumentDB Elastic Clusters (DocDB Elastic).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-docdbelastic-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-docdbelastic.


%package       -n gem-aws-sdk-docdbelastic-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - DocDB Elastic development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-docdbelastic
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-docdbelastic) = 1.1.0

%description   -n gem-aws-sdk-docdbelastic-devel
AWS SDK for Ruby - DocDB Elastic development package.

Official AWS Ruby gem for Amazon DocumentDB Elastic Clusters (DocDB Elastic).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-docdbelastic-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-docdbelastic.


%package       -n gem-aws-sdk-finspacedata
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-finspacedata) = 1.19.0

%description   -n gem-aws-sdk-finspacedata
Official AWS Ruby gem for FinSpace Public API (FinSpace Data). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-finspacedata-doc
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-finspacedata
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-finspacedata) = 1.19.0

%description   -n gem-aws-sdk-finspacedata-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for FinSpace Public API (FinSpace Data). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-finspacedata-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-finspacedata.


%package       -n gem-aws-sdk-finspacedata-devel
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-finspacedata
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-finspacedata) = 1.19.0

%description   -n gem-aws-sdk-finspacedata-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for FinSpace Public API (FinSpace Data). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-finspacedata-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-finspacedata.


%package       -n gem-aws-sdk-gluedatabrew
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-gluedatabrew) = 1.25.0

%description   -n gem-aws-sdk-gluedatabrew
Official AWS Ruby gem for AWS Glue DataBrew. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-gluedatabrew-doc
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-gluedatabrew
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-gluedatabrew) = 1.25.0

%description   -n gem-aws-sdk-gluedatabrew-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-gluedatabrew-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-gluedatabrew.


%package       -n gem-aws-sdk-gluedatabrew-devel
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-gluedatabrew
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-gluedatabrew) = 1.25.0

%description   -n gem-aws-sdk-gluedatabrew-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-gluedatabrew-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-gluedatabrew.


%package       -n gem-aws-sdk-greengrassv2
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-greengrassv2) = 1.24.0

%description   -n gem-aws-sdk-greengrassv2
Official AWS Ruby gem for AWS IoT Greengrass V2 (AWS GreengrassV2). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-greengrassv2-doc
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-greengrassv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-greengrassv2) = 1.24.0

%description   -n gem-aws-sdk-greengrassv2-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS IoT Greengrass V2 (AWS GreengrassV2). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-greengrassv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-greengrassv2.


%package       -n gem-aws-sdk-greengrassv2-devel
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-greengrassv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-greengrassv2) = 1.24.0

%description   -n gem-aws-sdk-greengrassv2-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS IoT Greengrass V2 (AWS GreengrassV2). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-greengrassv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-greengrassv2.


%package       -n gem-aws-sdk-imagebuilder
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-imagebuilder) = 1.43.0

%description   -n gem-aws-sdk-imagebuilder
Official AWS Ruby gem for EC2 Image Builder (imagebuilder). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-imagebuilder-doc
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-imagebuilder
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-imagebuilder) = 1.43.0

%description   -n gem-aws-sdk-imagebuilder-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for EC2 Image Builder (imagebuilder). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-imagebuilder-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-imagebuilder.


%package       -n gem-aws-sdk-imagebuilder-devel
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-imagebuilder
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-imagebuilder) = 1.43.0

%description   -n gem-aws-sdk-imagebuilder-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for EC2 Image Builder (imagebuilder). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-imagebuilder-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-imagebuilder.


%package       -n gem-aws-sdk-importexport
Version:       1.36.1
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv2) >= 1.0
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv2) >= 2
Provides:      gem(aws-sdk-importexport) = 1.36.1

%description   -n gem-aws-sdk-importexport
Official AWS Ruby gem for AWS Import/Export. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-importexport-doc
Version:       1.36.1
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-importexport
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-importexport) = 1.36.1

%description   -n gem-aws-sdk-importexport-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-importexport-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-importexport.


%package       -n gem-aws-sdk-importexport-devel
Version:       1.36.1
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-importexport
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-importexport) = 1.36.1

%description   -n gem-aws-sdk-importexport-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-importexport-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-importexport.


%package       -n gem-aws-sdk-iotanalytics
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iotanalytics) = 1.51.0

%description   -n gem-aws-sdk-iotanalytics
Official AWS Ruby gem for AWS IoT Analytics. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-iotanalytics-doc
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotanalytics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotanalytics) = 1.51.0

%description   -n gem-aws-sdk-iotanalytics-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-iotanalytics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotanalytics.


%package       -n gem-aws-sdk-iotanalytics-devel
Version:       1.51.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotanalytics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotanalytics) = 1.51.0

%description   -n gem-aws-sdk-iotanalytics-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-iotanalytics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotanalytics.


%package       -n gem-aws-sdk-iotdataplane
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iotdataplane) = 1.42.0

%description   -n gem-aws-sdk-iotdataplane
Official AWS Ruby gem for AWS IoT Data Plane. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-iotdataplane-doc
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotdataplane
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotdataplane) = 1.42.0

%description   -n gem-aws-sdk-iotdataplane-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-iotdataplane-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotdataplane.


%package       -n gem-aws-sdk-iotdataplane-devel
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotdataplane
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotdataplane) = 1.42.0

%description   -n gem-aws-sdk-iotdataplane-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-iotdataplane-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotdataplane.


%package       -n gem-aws-sdk-iotfleetwise
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT FleetWise
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iotfleetwise) = 1.7.0

%description   -n gem-aws-sdk-iotfleetwise
Official AWS Ruby gem for AWS IoT FleetWise. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-iotfleetwise-doc
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT FleetWise documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotfleetwise
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotfleetwise) = 1.7.0

%description   -n gem-aws-sdk-iotfleetwise-doc
AWS SDK for Ruby - AWS IoT FleetWise documentation files.

%description   -n gem-aws-sdk-iotfleetwise-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotfleetwise.


%package       -n gem-aws-sdk-iotfleetwise-devel
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT FleetWise development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotfleetwise
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotfleetwise) = 1.7.0

%description   -n gem-aws-sdk-iotfleetwise-devel
AWS SDK for Ruby - AWS IoT FleetWise development package.

%description   -n gem-aws-sdk-iotfleetwise-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotfleetwise.


%package       -n gem-aws-sdk-iottwinmaker
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT TwinMaker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iottwinmaker) = 1.9.0

%description   -n gem-aws-sdk-iottwinmaker
Official AWS Ruby gem for AWS IoT TwinMaker. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-iottwinmaker-doc
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT TwinMaker documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iottwinmaker
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iottwinmaker) = 1.9.0

%description   -n gem-aws-sdk-iottwinmaker-doc
AWS SDK for Ruby - AWS IoT TwinMaker documentation files.

%description   -n gem-aws-sdk-iottwinmaker-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iottwinmaker.


%package       -n gem-aws-sdk-iottwinmaker-devel
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT TwinMaker development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iottwinmaker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iottwinmaker) = 1.9.0

%description   -n gem-aws-sdk-iottwinmaker-devel
AWS SDK for Ruby - AWS IoT TwinMaker development package.

%description   -n gem-aws-sdk-iottwinmaker-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iottwinmaker.


%package       -n gem-aws-sdk-kafkaconnect
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kafka Connect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-kafkaconnect) = 1.9.0

%description   -n gem-aws-sdk-kafkaconnect
Official AWS Ruby gem for Managed Streaming for Kafka Connect (Kafka Connect).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kafkaconnect-doc
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kafka Connect documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kafkaconnect
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kafkaconnect) = 1.9.0

%description   -n gem-aws-sdk-kafkaconnect-doc
AWS SDK for Ruby - Kafka Connect documentation files.

Official AWS Ruby gem for Managed Streaming for Kafka Connect (Kafka Connect).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kafkaconnect-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kafkaconnect.


%package       -n gem-aws-sdk-kafkaconnect-devel
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kafka Connect development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kafkaconnect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kafkaconnect) = 1.9.0

%description   -n gem-aws-sdk-kafkaconnect-devel
AWS SDK for Ruby - Kafka Connect development package.

Official AWS Ruby gem for Managed Streaming for Kafka Connect (Kafka Connect).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kafkaconnect-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kafkaconnect.


%package       -n gem-aws-sdk-kinesisvideo
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-kinesisvideo) = 1.46.0

%description   -n gem-aws-sdk-kinesisvideo
Official AWS Ruby gem for Amazon Kinesis Video Streams (Kinesis Video). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kinesisvideo-doc
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesisvideo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideo) = 1.46.0

%description   -n gem-aws-sdk-kinesisvideo-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Kinesis Video Streams (Kinesis Video). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesisvideo.


%package       -n gem-aws-sdk-kinesisvideo-devel
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesisvideo
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideo) = 1.46.0

%description   -n gem-aws-sdk-kinesisvideo-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Kinesis Video Streams (Kinesis Video). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideo-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesisvideo.


%package       -n gem-aws-sdk-lexruntimev2
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-lexruntimev2) = 1.18.0

%description   -n gem-aws-sdk-lexruntimev2
Official AWS Ruby gem for Amazon Lex Runtime V2 (Lex Runtime V2). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-lexruntimev2-doc
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lexruntimev2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lexruntimev2) = 1.18.0

%description   -n gem-aws-sdk-lexruntimev2-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Lex Runtime V2 (Lex Runtime V2). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lexruntimev2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lexruntimev2.


%package       -n gem-aws-sdk-lexruntimev2-devel
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lexruntimev2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lexruntimev2) = 1.18.0

%description   -n gem-aws-sdk-lexruntimev2-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Lex Runtime V2 (Lex Runtime V2). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lexruntimev2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lexruntimev2.


%package       -n gem-aws-sdk-mediaconnect
Version:       1.47.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-mediaconnect) = 1.47.0

%description   -n gem-aws-sdk-mediaconnect
Official AWS Ruby gem for AWS MediaConnect. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-mediaconnect-doc
Version:       1.47.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mediaconnect
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mediaconnect) = 1.47.0

%description   -n gem-aws-sdk-mediaconnect-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-mediaconnect-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mediaconnect.


%package       -n gem-aws-sdk-mediaconnect-devel
Version:       1.47.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mediaconnect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mediaconnect) = 1.47.0

%description   -n gem-aws-sdk-mediaconnect-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-mediaconnect-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mediaconnect.


%package       -n gem-aws-sdk-mediaconvert
Version:       1.98.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-mediaconvert) = 1.98.0

%description   -n gem-aws-sdk-mediaconvert
Official AWS Ruby gem for AWS Elemental MediaConvert (MediaConvert). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mediaconvert-doc
Version:       1.98.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mediaconvert
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mediaconvert) = 1.98.0

%description   -n gem-aws-sdk-mediaconvert-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Elemental MediaConvert (MediaConvert). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediaconvert-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mediaconvert.


%package       -n gem-aws-sdk-mediaconvert-devel
Version:       1.98.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mediaconvert
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mediaconvert) = 1.98.0

%description   -n gem-aws-sdk-mediaconvert-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Elemental MediaConvert (MediaConvert). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediaconvert-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mediaconvert.


%package       -n gem-aws-sdk-mediapackage
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-mediapackage) = 1.58.0

%description   -n gem-aws-sdk-mediapackage
Official AWS Ruby gem for AWS Elemental MediaPackage (MediaPackage). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mediapackage-doc
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mediapackage
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mediapackage) = 1.58.0

%description   -n gem-aws-sdk-mediapackage-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Elemental MediaPackage (MediaPackage). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediapackage-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mediapackage.


%package       -n gem-aws-sdk-mediapackage-devel
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mediapackage
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mediapackage) = 1.58.0

%description   -n gem-aws-sdk-mediapackage-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Elemental MediaPackage (MediaPackage). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediapackage-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mediapackage.


%package       -n gem-aws-sdk-migrationhub
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-migrationhub) = 1.42.0

%description   -n gem-aws-sdk-migrationhub
Official AWS Ruby gem for AWS Migration Hub. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-migrationhub-doc
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-migrationhub
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-migrationhub) = 1.42.0

%description   -n gem-aws-sdk-migrationhub-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-migrationhub-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-migrationhub.


%package       -n gem-aws-sdk-migrationhub-devel
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-migrationhub
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-migrationhub) = 1.42.0

%description   -n gem-aws-sdk-migrationhub-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-migrationhub-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-migrationhub.


%package       -n gem-aws-sdk-nimblestudio
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-nimblestudio) = 1.18.0

%description   -n gem-aws-sdk-nimblestudio
Official AWS Ruby gem for AmazonNimbleStudio. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-nimblestudio-doc
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-nimblestudio
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-nimblestudio) = 1.18.0

%description   -n gem-aws-sdk-nimblestudio-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-nimblestudio-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-nimblestudio.


%package       -n gem-aws-sdk-nimblestudio-devel
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-nimblestudio
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-nimblestudio) = 1.18.0

%description   -n gem-aws-sdk-nimblestudio-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-nimblestudio-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-nimblestudio.


%package       -n gem-aws-sdk-savingsplans
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-savingsplans) = 1.28.0

%description   -n gem-aws-sdk-savingsplans
Official AWS Ruby gem for AWS Savings Plans (AWSSavingsPlans). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-savingsplans-doc
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-savingsplans
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-savingsplans) = 1.28.0

%description   -n gem-aws-sdk-savingsplans-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Savings Plans (AWSSavingsPlans). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-savingsplans-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-savingsplans.


%package       -n gem-aws-sdk-savingsplans-devel
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-savingsplans
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-savingsplans) = 1.28.0

%description   -n gem-aws-sdk-savingsplans-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Savings Plans (AWSSavingsPlans). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-savingsplans-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-savingsplans.


%package       -n gem-aws-sdk-securitylake
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Security Lake
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-securitylake) = 1.2.0

%description   -n gem-aws-sdk-securitylake
Official AWS Ruby gem for Amazon Security Lake. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-securitylake-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Security Lake documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-securitylake
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-securitylake) = 1.2.0

%description   -n gem-aws-sdk-securitylake-doc
AWS SDK for Ruby - Amazon Security Lake documentation files.

%description   -n gem-aws-sdk-securitylake-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-securitylake.


%package       -n gem-aws-sdk-securitylake-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Security Lake development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-securitylake
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-securitylake) = 1.2.0

%description   -n gem-aws-sdk-securitylake-devel
AWS SDK for Ruby - Amazon Security Lake development package.

%description   -n gem-aws-sdk-securitylake-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-securitylake.


%package       -n gem-aws-sdk-ssmincidents
Version:       1.21.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ssmincidents) = 1.21.0

%description   -n gem-aws-sdk-ssmincidents
Official AWS Ruby gem for AWS Systems Manager Incident Manager (SSM Incidents).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ssmincidents-doc
Version:       1.21.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ssmincidents
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ssmincidents) = 1.21.0

%description   -n gem-aws-sdk-ssmincidents-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Systems Manager Incident Manager (SSM Incidents).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssmincidents-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ssmincidents.


%package       -n gem-aws-sdk-ssmincidents-devel
Version:       1.21.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ssmincidents
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ssmincidents) = 1.21.0

%description   -n gem-aws-sdk-ssmincidents-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Systems Manager Incident Manager (SSM Incidents).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssmincidents-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ssmincidents.


%package       -n gem-aws-sdk-appconfigdata
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS AppConfig Data
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-appconfigdata) = 1.7.0

%description   -n gem-aws-sdk-appconfigdata
Official AWS Ruby gem for AWS AppConfig Data. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-appconfigdata-doc
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS AppConfig Data documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appconfigdata
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appconfigdata) = 1.7.0

%description   -n gem-aws-sdk-appconfigdata-doc
AWS SDK for Ruby - AWS AppConfig Data documentation files.

%description   -n gem-aws-sdk-appconfigdata-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appconfigdata.


%package       -n gem-aws-sdk-appconfigdata-devel
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS AppConfig Data development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appconfigdata
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appconfigdata) = 1.7.0

%description   -n gem-aws-sdk-appconfigdata-devel
AWS SDK for Ruby - AWS AppConfig Data development package.

%description   -n gem-aws-sdk-appconfigdata-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appconfigdata.


%package       -n gem-aws-sdk-arczonalshift
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS ARC - Zonal Shift
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-arczonalshift) = 1.1.0

%description   -n gem-aws-sdk-arczonalshift
Official AWS Ruby gem for AWS ARC - Zonal Shift. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-arczonalshift-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS ARC - Zonal Shift documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-arczonalshift
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-arczonalshift) = 1.1.0

%description   -n gem-aws-sdk-arczonalshift-doc
AWS SDK for Ruby - AWS ARC - Zonal Shift documentation files.

%description   -n gem-aws-sdk-arczonalshift-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-arczonalshift.


%package       -n gem-aws-sdk-arczonalshift-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS ARC - Zonal Shift development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-arczonalshift
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-arczonalshift) = 1.1.0

%description   -n gem-aws-sdk-arczonalshift-devel
AWS SDK for Ruby - AWS ARC - Zonal Shift development package.

%description   -n gem-aws-sdk-arczonalshift-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-arczonalshift.


%package       -n gem-aws-sdk-backupgateway
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Backup Gateway
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-backupgateway) = 1.8.0

%description   -n gem-aws-sdk-backupgateway
Official AWS Ruby gem for AWS Backup Gateway. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-backupgateway-doc
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Backup Gateway documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-backupgateway
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-backupgateway) = 1.8.0

%description   -n gem-aws-sdk-backupgateway-doc
AWS SDK for Ruby - AWS Backup Gateway documentation files.

%description   -n gem-aws-sdk-backupgateway-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-backupgateway.


%package       -n gem-aws-sdk-backupgateway-devel
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Backup Gateway development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-backupgateway
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-backupgateway) = 1.8.0

%description   -n gem-aws-sdk-backupgateway-devel
AWS SDK for Ruby - AWS Backup Gateway development package.

%description   -n gem-aws-sdk-backupgateway-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-backupgateway.


%package       -n gem-aws-sdk-backupstorage
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Backup Storage
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-backupstorage) = 1.2.0

%description   -n gem-aws-sdk-backupstorage
Official AWS Ruby gem for AWS Backup Storage. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-backupstorage-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Backup Storage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-backupstorage
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-backupstorage) = 1.2.0

%description   -n gem-aws-sdk-backupstorage-doc
AWS SDK for Ruby - AWS Backup Storage documentation files.

%description   -n gem-aws-sdk-backupstorage-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-backupstorage.


%package       -n gem-aws-sdk-backupstorage-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Backup Storage development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-backupstorage
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-backupstorage) = 1.2.0

%description   -n gem-aws-sdk-backupstorage-devel
AWS SDK for Ruby - AWS Backup Storage development package.

%description   -n gem-aws-sdk-backupstorage-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-backupstorage.


%package       -n gem-aws-sdk-chimesdkvoice
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Voice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-chimesdkvoice) = 1.1.0

%description   -n gem-aws-sdk-chimesdkvoice
Official AWS Ruby gem for Amazon Chime SDK Voice. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-chimesdkvoice-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Voice documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-chimesdkvoice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-chimesdkvoice) = 1.1.0

%description   -n gem-aws-sdk-chimesdkvoice-doc
AWS SDK for Ruby - Amazon Chime SDK Voice documentation files.

%description   -n gem-aws-sdk-chimesdkvoice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-chimesdkvoice.


%package       -n gem-aws-sdk-chimesdkvoice-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Voice development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-chimesdkvoice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-chimesdkvoice) = 1.1.0

%description   -n gem-aws-sdk-chimesdkvoice-devel
AWS SDK for Ruby - Amazon Chime SDK Voice development package.

%description   -n gem-aws-sdk-chimesdkvoice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-chimesdkvoice.


%package       -n gem-aws-sdk-cloudwatchrum
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudWatch RUM
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cloudwatchrum) = 1.8.0

%description   -n gem-aws-sdk-cloudwatchrum
Official AWS Ruby gem for CloudWatch RUM. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-cloudwatchrum-doc
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudWatch RUM documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudwatchrum
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatchrum) = 1.8.0

%description   -n gem-aws-sdk-cloudwatchrum-doc
AWS SDK for Ruby - CloudWatch RUM documentation files.

%description   -n gem-aws-sdk-cloudwatchrum-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudwatchrum.


%package       -n gem-aws-sdk-cloudwatchrum-devel
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudWatch RUM development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudwatchrum
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatchrum) = 1.8.0

%description   -n gem-aws-sdk-cloudwatchrum-devel
AWS SDK for Ruby - CloudWatch RUM development package.

%description   -n gem-aws-sdk-cloudwatchrum-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudwatchrum.


%package       -n gem-aws-sdk-configservice
Version:       1.87.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-configservice) = 1.87.0

%description   -n gem-aws-sdk-configservice
Official AWS Ruby gem for AWS Config (Config Service). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-configservice-doc
Version:       1.87.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-configservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-configservice) = 1.87.0

%description   -n gem-aws-sdk-configservice-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-configservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-configservice.


%package       -n gem-aws-sdk-configservice-devel
Version:       1.87.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-configservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-configservice) = 1.87.0

%description   -n gem-aws-sdk-configservice-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-configservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-configservice.


%package       -n gem-aws-sdk-directconnect
Version:       1.56.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-directconnect) = 1.56.0

%description   -n gem-aws-sdk-directconnect
Official AWS Ruby gem for AWS Direct Connect. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-directconnect-doc
Version:       1.56.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-directconnect
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-directconnect) = 1.56.0

%description   -n gem-aws-sdk-directconnect-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-directconnect-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-directconnect.


%package       -n gem-aws-sdk-directconnect-devel
Version:       1.56.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-directconnect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-directconnect) = 1.56.0

%description   -n gem-aws-sdk-directconnect-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-directconnect-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-directconnect.


%package       -n gem-aws-sdk-emrcontainers
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-emrcontainers) = 1.18.0

%description   -n gem-aws-sdk-emrcontainers
Official AWS Ruby gem for Amazon EMR Containers. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-emrcontainers-doc
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-emrcontainers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-emrcontainers) = 1.18.0

%description   -n gem-aws-sdk-emrcontainers-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-emrcontainers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-emrcontainers.


%package       -n gem-aws-sdk-emrcontainers-devel
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-emrcontainers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-emrcontainers) = 1.18.0

%description   -n gem-aws-sdk-emrcontainers-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-emrcontainers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-emrcontainers.


%package       -n gem-aws-sdk-emrserverless
Version:       1.5.0
Release:       alt1
Summary:       AWS SDK for Ruby - EMR Serverless
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-emrserverless) = 1.5.0

%description   -n gem-aws-sdk-emrserverless
Official AWS Ruby gem for EMR Serverless. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-emrserverless-doc
Version:       1.5.0
Release:       alt1
Summary:       AWS SDK for Ruby - EMR Serverless documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-emrserverless
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-emrserverless) = 1.5.0

%description   -n gem-aws-sdk-emrserverless-doc
AWS SDK for Ruby - EMR Serverless documentation files.

%description   -n gem-aws-sdk-emrserverless-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-emrserverless.


%package       -n gem-aws-sdk-emrserverless-devel
Version:       1.5.0
Release:       alt1
Summary:       AWS SDK for Ruby - EMR Serverless development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-emrserverless
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-emrserverless) = 1.5.0

%description   -n gem-aws-sdk-emrserverless-devel
AWS SDK for Ruby - EMR Serverless development package.

%description   -n gem-aws-sdk-emrserverless-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-emrserverless.


%package       -n gem-aws-sdk-frauddetector
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-frauddetector) = 1.37.0

%description   -n gem-aws-sdk-frauddetector
Official AWS Ruby gem for Amazon Fraud Detector. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-frauddetector-doc
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-frauddetector
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-frauddetector) = 1.37.0

%description   -n gem-aws-sdk-frauddetector-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-frauddetector-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-frauddetector.


%package       -n gem-aws-sdk-frauddetector-devel
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-frauddetector
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-frauddetector) = 1.37.0

%description   -n gem-aws-sdk-frauddetector-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-frauddetector-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-frauddetector.


%package       -n gem-aws-sdk-groundstation
Version:       1.31.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-groundstation) = 1.31.0

%description   -n gem-aws-sdk-groundstation
Official AWS Ruby gem for AWS Ground Station. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-groundstation-doc
Version:       1.31.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-groundstation
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-groundstation) = 1.31.0

%description   -n gem-aws-sdk-groundstation-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-groundstation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-groundstation.


%package       -n gem-aws-sdk-groundstation-devel
Version:       1.31.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-groundstation
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-groundstation) = 1.31.0

%description   -n gem-aws-sdk-groundstation-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-groundstation-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-groundstation.


%package       -n gem-aws-sdk-identitystore
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-identitystore) = 1.23.0

%description   -n gem-aws-sdk-identitystore
Official AWS Ruby gem for AWS SSO Identity Store (IdentityStore). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-identitystore-doc
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-identitystore
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-identitystore) = 1.23.0

%description   -n gem-aws-sdk-identitystore-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS SSO Identity Store (IdentityStore). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-identitystore-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-identitystore.


%package       -n gem-aws-sdk-identitystore-devel
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-identitystore
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-identitystore) = 1.23.0

%description   -n gem-aws-sdk-identitystore-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS SSO Identity Store (IdentityStore). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-identitystore-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-identitystore.


%package       -n gem-aws-sdk-ioteventsdata
Version:       1.29.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ioteventsdata) = 1.29.0

%description   -n gem-aws-sdk-ioteventsdata
Official AWS Ruby gem for AWS IoT Events Data. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-ioteventsdata-doc
Version:       1.29.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ioteventsdata
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ioteventsdata) = 1.29.0

%description   -n gem-aws-sdk-ioteventsdata-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-ioteventsdata-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ioteventsdata.


%package       -n gem-aws-sdk-ioteventsdata-devel
Version:       1.29.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ioteventsdata
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ioteventsdata) = 1.29.0

%description   -n gem-aws-sdk-ioteventsdata-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-ioteventsdata-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ioteventsdata.


%package       -n gem-aws-sdk-iotroborunner
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT RoboRunner
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iotroborunner) = 1.1.0

%description   -n gem-aws-sdk-iotroborunner
Official AWS Ruby gem for AWS IoT RoboRunner. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-iotroborunner-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT RoboRunner documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotroborunner
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotroborunner) = 1.1.0

%description   -n gem-aws-sdk-iotroborunner-doc
AWS SDK for Ruby - AWS IoT RoboRunner documentation files.

%description   -n gem-aws-sdk-iotroborunner-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotroborunner.


%package       -n gem-aws-sdk-iotroborunner-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT RoboRunner development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotroborunner
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotroborunner) = 1.1.0

%description   -n gem-aws-sdk-iotroborunner-devel
AWS SDK for Ruby - AWS IoT RoboRunner development package.

%description   -n gem-aws-sdk-iotroborunner-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotroborunner.


%package       -n gem-aws-sdk-kendraranking
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kendra Ranking
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-kendraranking) = 1.1.0

%description   -n gem-aws-sdk-kendraranking
Official AWS Ruby gem for Amazon Kendra Intelligent Ranking (Kendra Ranking).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kendraranking-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kendra Ranking documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kendraranking
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kendraranking) = 1.1.0

%description   -n gem-aws-sdk-kendraranking-doc
AWS SDK for Ruby - Kendra Ranking documentation files.

Official AWS Ruby gem for Amazon Kendra Intelligent Ranking (Kendra Ranking).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kendraranking-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kendraranking.


%package       -n gem-aws-sdk-kendraranking-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kendra Ranking development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kendraranking
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kendraranking) = 1.1.0

%description   -n gem-aws-sdk-kendraranking-devel
AWS SDK for Ruby - Kendra Ranking development package.

Official AWS Ruby gem for Amazon Kendra Intelligent Ranking (Kendra Ranking).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kendraranking-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kendraranking.


%package       -n gem-aws-sdk-lakeformation
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-lakeformation) = 1.30.0

%description   -n gem-aws-sdk-lakeformation
Official AWS Ruby gem for AWS Lake Formation. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-lakeformation-doc
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lakeformation
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lakeformation) = 1.30.0

%description   -n gem-aws-sdk-lakeformation-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-lakeformation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lakeformation.


%package       -n gem-aws-sdk-lakeformation-devel
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lakeformation
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lakeformation) = 1.30.0

%description   -n gem-aws-sdk-lakeformation-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-lakeformation-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lakeformation.


%package       -n gem-aws-sdk-lambdapreview
Version:       1.36.1
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-lambdapreview) = 1.36.1

%description   -n gem-aws-sdk-lambdapreview
Official AWS Ruby gem for AWS Lambda. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-lambdapreview-doc
Version:       1.36.1
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lambdapreview
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lambdapreview) = 1.36.1

%description   -n gem-aws-sdk-lambdapreview-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Lambda. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lambdapreview-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lambdapreview.


%package       -n gem-aws-sdk-lambdapreview-devel
Version:       1.36.1
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lambdapreview
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lambdapreview) = 1.36.1

%description   -n gem-aws-sdk-lambdapreview-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Lambda. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lambdapreview-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lambdapreview.


%package       -n gem-aws-sdk-organizations
Version:       1.73.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-organizations) = 1.73.0

%description   -n gem-aws-sdk-organizations
Official AWS Ruby gem for AWS Organizations (Organizations). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-organizations-doc
Version:       1.73.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-organizations
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-organizations) = 1.73.0

%description   -n gem-aws-sdk-organizations-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Organizations (Organizations). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-organizations-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-organizations.


%package       -n gem-aws-sdk-organizations-devel
Version:       1.73.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-organizations
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-organizations) = 1.73.0

%description   -n gem-aws-sdk-organizations-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Organizations (Organizations). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-organizations-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-organizations.


%package       -n gem-aws-sdk-pinpointemail
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-pinpointemail) = 1.37.0

%description   -n gem-aws-sdk-pinpointemail
Official AWS Ruby gem for Amazon Pinpoint Email Service (Pinpoint Email). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-pinpointemail-doc
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-pinpointemail
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-pinpointemail) = 1.37.0

%description   -n gem-aws-sdk-pinpointemail-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Pinpoint Email Service (Pinpoint Email). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pinpointemail-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-pinpointemail.


%package       -n gem-aws-sdk-pinpointemail-devel
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-pinpointemail
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-pinpointemail) = 1.37.0

%description   -n gem-aws-sdk-pinpointemail-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Pinpoint Email Service (Pinpoint Email). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pinpointemail-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-pinpointemail.


%package       -n gem-aws-sdk-resiliencehub
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Resilience Hub
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-resiliencehub) = 1.9.0

%description   -n gem-aws-sdk-resiliencehub
Official AWS Ruby gem for AWS Resilience Hub. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-resiliencehub-doc
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Resilience Hub documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-resiliencehub
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-resiliencehub) = 1.9.0

%description   -n gem-aws-sdk-resiliencehub-doc
AWS SDK for Ruby - AWS Resilience Hub documentation files.

%description   -n gem-aws-sdk-resiliencehub-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-resiliencehub.


%package       -n gem-aws-sdk-resiliencehub-devel
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Resilience Hub development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-resiliencehub
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-resiliencehub) = 1.9.0

%description   -n gem-aws-sdk-resiliencehub-devel
AWS SDK for Ruby - AWS Resilience Hub development package.

%description   -n gem-aws-sdk-resiliencehub-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-resiliencehub.


%package       -n gem-aws-sdk-rolesanywhere
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - IAM Roles Anywhere
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-rolesanywhere) = 1.2.0

%description   -n gem-aws-sdk-rolesanywhere
Official AWS Ruby gem for IAM Roles Anywhere. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-rolesanywhere-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - IAM Roles Anywhere documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-rolesanywhere
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-rolesanywhere) = 1.2.0

%description   -n gem-aws-sdk-rolesanywhere-doc
AWS SDK for Ruby - IAM Roles Anywhere documentation files.

%description   -n gem-aws-sdk-rolesanywhere-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-rolesanywhere.


%package       -n gem-aws-sdk-rolesanywhere-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - IAM Roles Anywhere development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-rolesanywhere
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-rolesanywhere) = 1.2.0

%description   -n gem-aws-sdk-rolesanywhere-devel
AWS SDK for Ruby - IAM Roles Anywhere development package.

%description   -n gem-aws-sdk-rolesanywhere-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-rolesanywhere.


%package       -n gem-aws-sdk-servicequotas
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-servicequotas) = 1.25.0

%description   -n gem-aws-sdk-servicequotas
Official AWS Ruby gem for Service Quotas. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-servicequotas-doc
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-servicequotas
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-servicequotas) = 1.25.0

%description   -n gem-aws-sdk-servicequotas-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-servicequotas-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-servicequotas.


%package       -n gem-aws-sdk-servicequotas-devel
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-servicequotas
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-servicequotas) = 1.25.0

%description   -n gem-aws-sdk-servicequotas-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-servicequotas-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-servicequotas.


%package       -n gem-aws-sdk-workspacesweb
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkSpaces Web
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-workspacesweb) = 1.8.0

%description   -n gem-aws-sdk-workspacesweb
Official AWS Ruby gem for Amazon WorkSpaces Web. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-workspacesweb-doc
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkSpaces Web documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-workspacesweb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-workspacesweb) = 1.8.0

%description   -n gem-aws-sdk-workspacesweb-doc
AWS SDK for Ruby - Amazon WorkSpaces Web documentation files.

%description   -n gem-aws-sdk-workspacesweb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-workspacesweb.


%package       -n gem-aws-sdk-workspacesweb-devel
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkSpaces Web development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-workspacesweb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-workspacesweb) = 1.8.0

%description   -n gem-aws-sdk-workspacesweb-devel
AWS SDK for Ruby - Amazon WorkSpaces Web development package.

%description   -n gem-aws-sdk-workspacesweb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-workspacesweb.


%package       -n gem-aws-sdk-accessanalyzer
Version:       1.33.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-accessanalyzer) = 1.33.0

%description   -n gem-aws-sdk-accessanalyzer
Official AWS Ruby gem for Access Analyzer. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-accessanalyzer-doc
Version:       1.33.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-accessanalyzer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-accessanalyzer) = 1.33.0

%description   -n gem-aws-sdk-accessanalyzer-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-accessanalyzer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-accessanalyzer.


%package       -n gem-aws-sdk-accessanalyzer-devel
Version:       1.33.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-accessanalyzer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-accessanalyzer) = 1.33.0

%description   -n gem-aws-sdk-accessanalyzer-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-accessanalyzer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-accessanalyzer.


%package       -n gem-aws-sdk-amplifybackend
Version:       1.20.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-amplifybackend) = 1.20.0

%description   -n gem-aws-sdk-amplifybackend
Official AWS Ruby gem for AmplifyBackend. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-amplifybackend-doc
Version:       1.20.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-amplifybackend
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-amplifybackend) = 1.20.0

%description   -n gem-aws-sdk-amplifybackend-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-amplifybackend-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-amplifybackend.


%package       -n gem-aws-sdk-amplifybackend-devel
Version:       1.20.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-amplifybackend
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-amplifybackend) = 1.20.0

%description   -n gem-aws-sdk-amplifybackend-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-amplifybackend-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-amplifybackend.


%package       -n gem-aws-sdk-clouddirectory
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-clouddirectory) = 1.43.0

%description   -n gem-aws-sdk-clouddirectory
Official AWS Ruby gem for Amazon CloudDirectory. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-clouddirectory-doc
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-clouddirectory
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-clouddirectory) = 1.43.0

%description   -n gem-aws-sdk-clouddirectory-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-clouddirectory-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-clouddirectory.


%package       -n gem-aws-sdk-clouddirectory-devel
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-clouddirectory
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-clouddirectory) = 1.43.0

%description   -n gem-aws-sdk-clouddirectory-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-clouddirectory-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-clouddirectory.


%package       -n gem-aws-sdk-cloudformation
Version:       1.75.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cloudformation) = 1.75.0

%description   -n gem-aws-sdk-cloudformation
Official AWS Ruby gem for AWS CloudFormation. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-cloudformation-doc
Version:       1.75.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudformation
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudformation) = 1.75.0

%description   -n gem-aws-sdk-cloudformation-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-cloudformation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudformation.


%package       -n gem-aws-sdk-cloudformation-devel
Version:       1.75.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudformation
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudformation) = 1.75.0

%description   -n gem-aws-sdk-cloudformation-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-cloudformation-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudformation.


%package       -n gem-aws-sdk-cloudwatchlogs
Version:       1.62.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cloudwatchlogs) = 1.62.0

%description   -n gem-aws-sdk-cloudwatchlogs
Official AWS Ruby gem for Amazon CloudWatch Logs. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-cloudwatchlogs-doc
Version:       1.62.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudwatchlogs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatchlogs) = 1.62.0

%description   -n gem-aws-sdk-cloudwatchlogs-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-cloudwatchlogs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudwatchlogs.


%package       -n gem-aws-sdk-cloudwatchlogs-devel
Version:       1.62.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudwatchlogs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatchlogs) = 1.62.0

%description   -n gem-aws-sdk-cloudwatchlogs-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-cloudwatchlogs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudwatchlogs.


%package       -n gem-aws-sdk-iotthingsgraph
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iotthingsgraph) = 1.26.0

%description   -n gem-aws-sdk-iotthingsgraph
Official AWS Ruby gem for AWS IoT Things Graph. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-iotthingsgraph-doc
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotthingsgraph
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotthingsgraph) = 1.26.0

%description   -n gem-aws-sdk-iotthingsgraph-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-iotthingsgraph-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotthingsgraph.


%package       -n gem-aws-sdk-iotthingsgraph-devel
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotthingsgraph
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotthingsgraph) = 1.26.0

%description   -n gem-aws-sdk-iotthingsgraph-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-iotthingsgraph-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotthingsgraph.


%package       -n gem-aws-sdk-licensemanager
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-licensemanager) = 1.43.0

%description   -n gem-aws-sdk-licensemanager
Official AWS Ruby gem for AWS License Manager. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-licensemanager-doc
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-licensemanager
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-licensemanager) = 1.43.0

%description   -n gem-aws-sdk-licensemanager-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-licensemanager-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-licensemanager.


%package       -n gem-aws-sdk-licensemanager-devel
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-licensemanager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-licensemanager) = 1.43.0

%description   -n gem-aws-sdk-licensemanager-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-licensemanager-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-licensemanager.


%package       -n gem-aws-sdk-lookoutmetrics
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-lookoutmetrics) = 1.24.0

%description   -n gem-aws-sdk-lookoutmetrics
Official AWS Ruby gem for Amazon Lookout for Metrics (LookoutMetrics). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-lookoutmetrics-doc
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lookoutmetrics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lookoutmetrics) = 1.24.0

%description   -n gem-aws-sdk-lookoutmetrics-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Lookout for Metrics (LookoutMetrics). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lookoutmetrics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lookoutmetrics.


%package       -n gem-aws-sdk-lookoutmetrics-devel
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lookoutmetrics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lookoutmetrics) = 1.24.0

%description   -n gem-aws-sdk-lookoutmetrics-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Lookout for Metrics (LookoutMetrics). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lookoutmetrics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lookoutmetrics.


%package       -n gem-aws-sdk-managedgrafana
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Managed Grafana
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-managedgrafana) = 1.11.0

%description   -n gem-aws-sdk-managedgrafana
Official AWS Ruby gem for Amazon Managed Grafana. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-managedgrafana-doc
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Managed Grafana documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-managedgrafana
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-managedgrafana) = 1.11.0

%description   -n gem-aws-sdk-managedgrafana-doc
AWS SDK for Ruby - Amazon Managed Grafana documentation files.

%description   -n gem-aws-sdk-managedgrafana-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-managedgrafana.


%package       -n gem-aws-sdk-managedgrafana-devel
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Managed Grafana development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-managedgrafana
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-managedgrafana) = 1.11.0

%description   -n gem-aws-sdk-managedgrafana-devel
AWS SDK for Ruby - Amazon Managed Grafana development package.

%description   -n gem-aws-sdk-managedgrafana-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-managedgrafana.


%package       -n gem-aws-sdk-mediastoredata
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-mediastoredata) = 1.40.0

%description   -n gem-aws-sdk-mediastoredata
Official AWS Ruby gem for AWS Elemental MediaStore Data Plane (MediaStore Data).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mediastoredata-doc
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mediastoredata
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mediastoredata) = 1.40.0

%description   -n gem-aws-sdk-mediastoredata-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Elemental MediaStore Data Plane (MediaStore Data).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediastoredata-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mediastoredata.


%package       -n gem-aws-sdk-mediastoredata-devel
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mediastoredata
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mediastoredata) = 1.40.0

%description   -n gem-aws-sdk-mediastoredata-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Elemental MediaStore Data Plane (MediaStore Data).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediastoredata-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mediastoredata.


%package       -n gem-aws-sdk-networkmanager
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-networkmanager) = 1.28.0

%description   -n gem-aws-sdk-networkmanager
Official AWS Ruby gem for AWS Network Manager (NetworkManager). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-networkmanager-doc
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-networkmanager
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-networkmanager) = 1.28.0

%description   -n gem-aws-sdk-networkmanager-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Network Manager (NetworkManager). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-networkmanager-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-networkmanager.


%package       -n gem-aws-sdk-networkmanager-devel
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-networkmanager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-networkmanager) = 1.28.0

%description   -n gem-aws-sdk-networkmanager-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Network Manager (NetworkManager). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-networkmanager-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-networkmanager.


%package       -n gem-aws-sdk-rdsdataservice
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-rdsdataservice) = 1.40.0

%description   -n gem-aws-sdk-rdsdataservice
Official AWS Ruby gem for AWS RDS DataService. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-rdsdataservice-doc
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-rdsdataservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-rdsdataservice) = 1.40.0

%description   -n gem-aws-sdk-rdsdataservice-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-rdsdataservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-rdsdataservice.


%package       -n gem-aws-sdk-rdsdataservice-devel
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-rdsdataservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-rdsdataservice) = 1.40.0

%description   -n gem-aws-sdk-rdsdataservice-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-rdsdataservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-rdsdataservice.


%package       -n gem-aws-sdk-resourcegroups
Version:       1.48.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-resourcegroups) = 1.48.0

%description   -n gem-aws-sdk-resourcegroups
Official AWS Ruby gem for AWS Resource Groups (Resource Groups). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-resourcegroups-doc
Version:       1.48.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-resourcegroups
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-resourcegroups) = 1.48.0

%description   -n gem-aws-sdk-resourcegroups-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Resource Groups (Resource Groups). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-resourcegroups-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-resourcegroups.


%package       -n gem-aws-sdk-resourcegroups-devel
Version:       1.48.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-resourcegroups
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-resourcegroups) = 1.48.0

%description   -n gem-aws-sdk-resourcegroups-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Resource Groups (Resource Groups). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-resourcegroups-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-resourcegroups.


%package       -n gem-aws-sdk-route53domains
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-route53domains) = 1.43.0

%description   -n gem-aws-sdk-route53domains
Official AWS Ruby gem for Amazon Route 53 Domains. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-route53domains-doc
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-route53domains
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-route53domains) = 1.43.0

%description   -n gem-aws-sdk-route53domains-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-route53domains-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-route53domains.


%package       -n gem-aws-sdk-route53domains-devel
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-route53domains
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-route53domains) = 1.43.0

%description   -n gem-aws-sdk-route53domains-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-route53domains-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-route53domains.


%package       -n gem-aws-sdk-secretsmanager
Version:       1.72.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-secretsmanager) = 1.72.0

%description   -n gem-aws-sdk-secretsmanager
Official AWS Ruby gem for AWS Secrets Manager. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-secretsmanager-doc
Version:       1.72.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-secretsmanager
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-secretsmanager) = 1.72.0

%description   -n gem-aws-sdk-secretsmanager-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-secretsmanager-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-secretsmanager.


%package       -n gem-aws-sdk-secretsmanager-devel
Version:       1.72.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-secretsmanager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-secretsmanager) = 1.72.0

%description   -n gem-aws-sdk-secretsmanager-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-secretsmanager-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-secretsmanager.


%package       -n gem-aws-sdk-servicecatalog
Version:       1.75.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-servicecatalog) = 1.75.0

%description   -n gem-aws-sdk-servicecatalog
Official AWS Ruby gem for AWS Service Catalog. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-servicecatalog-doc
Version:       1.75.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-servicecatalog
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-servicecatalog) = 1.75.0

%description   -n gem-aws-sdk-servicecatalog-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-servicecatalog-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-servicecatalog.


%package       -n gem-aws-sdk-servicecatalog-devel
Version:       1.75.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-servicecatalog
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-servicecatalog) = 1.75.0

%description   -n gem-aws-sdk-servicecatalog-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-servicecatalog-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-servicecatalog.


%package       -n gem-aws-sdk-simspaceweaver
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS SimSpace Weaver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-simspaceweaver) = 1.1.0

%description   -n gem-aws-sdk-simspaceweaver
Official AWS Ruby gem for AWS SimSpace Weaver. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-simspaceweaver-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS SimSpace Weaver documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-simspaceweaver
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-simspaceweaver) = 1.1.0

%description   -n gem-aws-sdk-simspaceweaver-doc
AWS SDK for Ruby - AWS SimSpace Weaver documentation files.

%description   -n gem-aws-sdk-simspaceweaver-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-simspaceweaver.


%package       -n gem-aws-sdk-simspaceweaver-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS SimSpace Weaver development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-simspaceweaver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-simspaceweaver) = 1.1.0

%description   -n gem-aws-sdk-simspaceweaver-devel
AWS SDK for Ruby - AWS SimSpace Weaver development package.

%description   -n gem-aws-sdk-simspaceweaver-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-simspaceweaver.


%package       -n gem-aws-sdk-storagegateway
Version:       1.70.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-storagegateway) = 1.70.0

%description   -n gem-aws-sdk-storagegateway
Official AWS Ruby gem for AWS Storage Gateway. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-storagegateway-doc
Version:       1.70.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-storagegateway
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-storagegateway) = 1.70.0

%description   -n gem-aws-sdk-storagegateway-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-storagegateway-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-storagegateway.


%package       -n gem-aws-sdk-storagegateway-devel
Version:       1.70.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-storagegateway
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-storagegateway) = 1.70.0

%description   -n gem-aws-sdk-storagegateway-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-storagegateway-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-storagegateway.


%package       -n gem-aws-sdk-cloudcontrolapi
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudControlApi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cloudcontrolapi) = 1.10.0

%description   -n gem-aws-sdk-cloudcontrolapi
Official AWS Ruby gem for AWS Cloud Control API (CloudControlApi). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-cloudcontrolapi-doc
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudControlApi documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudcontrolapi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudcontrolapi) = 1.10.0

%description   -n gem-aws-sdk-cloudcontrolapi-doc
AWS SDK for Ruby - CloudControlApi documentation files.

Official AWS Ruby gem for AWS Cloud Control API (CloudControlApi). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudcontrolapi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudcontrolapi.


%package       -n gem-aws-sdk-cloudcontrolapi-devel
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudControlApi development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudcontrolapi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudcontrolapi) = 1.10.0

%description   -n gem-aws-sdk-cloudcontrolapi-devel
AWS SDK for Ruby - CloudControlApi development package.

Official AWS Ruby gem for AWS Cloud Control API (CloudControlApi). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudcontrolapi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudcontrolapi.


%package       -n gem-aws-sdk-cognitoidentity
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cognitoidentity) = 1.42.0

%description   -n gem-aws-sdk-cognitoidentity
Official AWS Ruby gem for Amazon Cognito Identity. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-cognitoidentity-doc
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cognitoidentity
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cognitoidentity) = 1.42.0

%description   -n gem-aws-sdk-cognitoidentity-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-cognitoidentity-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cognitoidentity.


%package       -n gem-aws-sdk-cognitoidentity-devel
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cognitoidentity
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cognitoidentity) = 1.42.0

%description   -n gem-aws-sdk-cognitoidentity-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-cognitoidentity-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cognitoidentity.


%package       -n gem-aws-sdk-dynamodbstreams
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-dynamodbstreams) = 1.43.0

%description   -n gem-aws-sdk-dynamodbstreams
Official AWS Ruby gem for Amazon DynamoDB Streams. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-dynamodbstreams-doc
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-dynamodbstreams
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-dynamodbstreams) = 1.43.0

%description   -n gem-aws-sdk-dynamodbstreams-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-dynamodbstreams-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-dynamodbstreams.


%package       -n gem-aws-sdk-dynamodbstreams-devel
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-dynamodbstreams
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-dynamodbstreams) = 1.43.0

%description   -n gem-aws-sdk-dynamodbstreams-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-dynamodbstreams-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-dynamodbstreams.


%package       -n gem-aws-sdk-forecastservice
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-forecastservice) = 1.39.0

%description   -n gem-aws-sdk-forecastservice
Official AWS Ruby gem for Amazon Forecast Service. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-forecastservice-doc
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-forecastservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-forecastservice) = 1.39.0

%description   -n gem-aws-sdk-forecastservice-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-forecastservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-forecastservice.


%package       -n gem-aws-sdk-forecastservice-devel
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-forecastservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-forecastservice) = 1.39.0

%description   -n gem-aws-sdk-forecastservice-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-forecastservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-forecastservice.


%package       -n gem-aws-sdk-locationservice
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-locationservice) = 1.28.0

%description   -n gem-aws-sdk-locationservice
Official AWS Ruby gem for Amazon Location Service. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-locationservice-doc
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-locationservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-locationservice) = 1.28.0

%description   -n gem-aws-sdk-locationservice-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-locationservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-locationservice.


%package       -n gem-aws-sdk-locationservice-devel
Version:       1.28.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-locationservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-locationservice) = 1.28.0

%description   -n gem-aws-sdk-locationservice-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-locationservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-locationservice.


%package       -n gem-aws-sdk-machinelearning
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-machinelearning) = 1.39.0

%description   -n gem-aws-sdk-machinelearning
Official AWS Ruby gem for Amazon Machine Learning. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-machinelearning-doc
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-machinelearning
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-machinelearning) = 1.39.0

%description   -n gem-aws-sdk-machinelearning-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-machinelearning-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-machinelearning.


%package       -n gem-aws-sdk-machinelearning-devel
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-machinelearning
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-machinelearning) = 1.39.0

%description   -n gem-aws-sdk-machinelearning-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-machinelearning-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-machinelearning.


%package       -n gem-aws-sdk-mediapackagevod
Version:       1.41.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-mediapackagevod) = 1.41.0

%description   -n gem-aws-sdk-mediapackagevod
Official AWS Ruby gem for AWS Elemental MediaPackage VOD (MediaPackage Vod).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mediapackagevod-doc
Version:       1.41.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mediapackagevod
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mediapackagevod) = 1.41.0

%description   -n gem-aws-sdk-mediapackagevod-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Elemental MediaPackage VOD (MediaPackage Vod).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediapackagevod-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mediapackagevod.


%package       -n gem-aws-sdk-mediapackagevod-devel
Version:       1.41.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mediapackagevod
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mediapackagevod) = 1.41.0

%description   -n gem-aws-sdk-mediapackagevod-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Elemental MediaPackage VOD (MediaPackage Vod).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediapackagevod-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mediapackagevod.


%package       -n gem-aws-sdk-networkfirewall
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-networkfirewall) = 1.24.0

%description   -n gem-aws-sdk-networkfirewall
Official AWS Ruby gem for AWS Network Firewall (Network Firewall). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-networkfirewall-doc
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-networkfirewall
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-networkfirewall) = 1.24.0

%description   -n gem-aws-sdk-networkfirewall-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Network Firewall (Network Firewall). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-networkfirewall-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-networkfirewall.


%package       -n gem-aws-sdk-networkfirewall-devel
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-networkfirewall
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-networkfirewall) = 1.24.0

%description   -n gem-aws-sdk-networkfirewall-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Network Firewall (Network Firewall). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-networkfirewall-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-networkfirewall.


%package       -n gem-aws-sdk-privatenetworks
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Private 5G
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-privatenetworks) = 1.3.0

%description   -n gem-aws-sdk-privatenetworks
Official AWS Ruby gem for AWS Private 5G. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-privatenetworks-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Private 5G documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-privatenetworks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-privatenetworks) = 1.3.0

%description   -n gem-aws-sdk-privatenetworks-doc
AWS SDK for Ruby - AWS Private 5G documentation files.

%description   -n gem-aws-sdk-privatenetworks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-privatenetworks.


%package       -n gem-aws-sdk-privatenetworks-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Private 5G development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-privatenetworks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-privatenetworks) = 1.3.0

%description   -n gem-aws-sdk-privatenetworks-devel
AWS SDK for Ruby - AWS Private 5G development package.

%description   -n gem-aws-sdk-privatenetworks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-privatenetworks.


%package       -n gem-aws-sdk-route53resolver
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-route53resolver) = 1.39.0

%description   -n gem-aws-sdk-route53resolver
Official AWS Ruby gem for Amazon Route 53 Resolver (Route53Resolver). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-route53resolver-doc
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-route53resolver
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-route53resolver) = 1.39.0

%description   -n gem-aws-sdk-route53resolver-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Route 53 Resolver (Route53Resolver). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-route53resolver-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-route53resolver.


%package       -n gem-aws-sdk-route53resolver-devel
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-route53resolver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-route53resolver) = 1.39.0

%description   -n gem-aws-sdk-route53resolver-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Route 53 Resolver (Route53Resolver). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-route53resolver-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-route53resolver.


%package       -n gem-aws-sdk-timestreamquery
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-timestreamquery) = 1.18.0

%description   -n gem-aws-sdk-timestreamquery
Official AWS Ruby gem for Amazon Timestream Query (Timestream Query). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-timestreamquery-doc
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-timestreamquery
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-timestreamquery) = 1.18.0

%description   -n gem-aws-sdk-timestreamquery-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Timestream Query (Timestream Query). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-timestreamquery-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-timestreamquery.


%package       -n gem-aws-sdk-timestreamquery-devel
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-timestreamquery
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-timestreamquery) = 1.18.0

%description   -n gem-aws-sdk-timestreamquery-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Timestream Query (Timestream Query). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-timestreamquery-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-timestreamquery.


%package       -n gem-aws-sdk-timestreamwrite
Version:       1.16.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-timestreamwrite) = 1.16.0

%description   -n gem-aws-sdk-timestreamwrite
Official AWS Ruby gem for Amazon Timestream Write (Timestream Write). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-timestreamwrite-doc
Version:       1.16.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-timestreamwrite
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-timestreamwrite) = 1.16.0

%description   -n gem-aws-sdk-timestreamwrite-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Timestream Write (Timestream Write). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-timestreamwrite-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-timestreamwrite.


%package       -n gem-aws-sdk-timestreamwrite-devel
Version:       1.16.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-timestreamwrite
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-timestreamwrite) = 1.16.0

%description   -n gem-aws-sdk-timestreamwrite-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Timestream Write (Timestream Write). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-timestreamwrite-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-timestreamwrite.


%package       -n gem-aws-sdk-wellarchitected
Version:       1.20.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-wellarchitected) = 1.20.0

%description   -n gem-aws-sdk-wellarchitected
Official AWS Ruby gem for AWS Well-Architected Tool (Well-Architected). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-wellarchitected-doc
Version:       1.20.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-wellarchitected
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-wellarchitected) = 1.20.0

%description   -n gem-aws-sdk-wellarchitected-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Well-Architected Tool (Well-Architected). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-wellarchitected-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-wellarchitected.


%package       -n gem-aws-sdk-wellarchitected-devel
Version:       1.20.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-wellarchitected
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-wellarchitected) = 1.20.0

%description   -n gem-aws-sdk-wellarchitected-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Well-Architected Tool (Well-Architected). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-wellarchitected-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-wellarchitected.


%package       -n gem-aws-sdk-alexaforbusiness
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-alexaforbusiness) = 1.58.0

%description   -n gem-aws-sdk-alexaforbusiness
Official AWS Ruby gem for Alexa For Business. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-alexaforbusiness-doc
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-alexaforbusiness
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-alexaforbusiness) = 1.58.0

%description   -n gem-aws-sdk-alexaforbusiness-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-alexaforbusiness-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-alexaforbusiness.


%package       -n gem-aws-sdk-alexaforbusiness-devel
Version:       1.58.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-alexaforbusiness
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-alexaforbusiness) = 1.58.0

%description   -n gem-aws-sdk-alexaforbusiness-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-alexaforbusiness-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-alexaforbusiness.


%package       -n gem-aws-sdk-amplifyuibuilder
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Amplify UI Builder
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-amplifyuibuilder) = 1.9.0

%description   -n gem-aws-sdk-amplifyuibuilder
Official AWS Ruby gem for AWS Amplify UI Builder. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-amplifyuibuilder-doc
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Amplify UI Builder documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-amplifyuibuilder
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-amplifyuibuilder) = 1.9.0

%description   -n gem-aws-sdk-amplifyuibuilder-doc
AWS SDK for Ruby - AWS Amplify UI Builder documentation files.

%description   -n gem-aws-sdk-amplifyuibuilder-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-amplifyuibuilder.


%package       -n gem-aws-sdk-amplifyuibuilder-devel
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Amplify UI Builder development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-amplifyuibuilder
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-amplifyuibuilder) = 1.9.0

%description   -n gem-aws-sdk-amplifyuibuilder-devel
AWS SDK for Ruby - AWS Amplify UI Builder development package.

%description   -n gem-aws-sdk-amplifyuibuilder-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-amplifyuibuilder.


%package       -n gem-aws-sdk-autoscalingplans
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-autoscalingplans) = 1.42.0

%description   -n gem-aws-sdk-autoscalingplans
Official AWS Ruby gem for AWS Auto Scaling Plans. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-autoscalingplans-doc
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-autoscalingplans
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-autoscalingplans) = 1.42.0

%description   -n gem-aws-sdk-autoscalingplans-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-autoscalingplans-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-autoscalingplans.


%package       -n gem-aws-sdk-autoscalingplans-devel
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-autoscalingplans
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-autoscalingplans) = 1.42.0

%description   -n gem-aws-sdk-autoscalingplans-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-autoscalingplans-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-autoscalingplans.


%package       -n gem-aws-sdk-billingconductor
Version:       1.6.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSBillingConductor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-billingconductor) = 1.6.0

%description   -n gem-aws-sdk-billingconductor
Official AWS Ruby gem for AWSBillingConductor. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-billingconductor-doc
Version:       1.6.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSBillingConductor documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-billingconductor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-billingconductor) = 1.6.0

%description   -n gem-aws-sdk-billingconductor-doc
AWS SDK for Ruby - AWSBillingConductor documentation files.

%description   -n gem-aws-sdk-billingconductor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-billingconductor.


%package       -n gem-aws-sdk-billingconductor-devel
Version:       1.6.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSBillingConductor development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-billingconductor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-billingconductor) = 1.6.0

%description   -n gem-aws-sdk-billingconductor-devel
AWS SDK for Ruby - AWSBillingConductor development package.

%description   -n gem-aws-sdk-billingconductor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-billingconductor.


%package       -n gem-aws-sdk-chimesdkidentity
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Identity
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-chimesdkidentity) = 1.11.0

%description   -n gem-aws-sdk-chimesdkidentity
Official AWS Ruby gem for Amazon Chime SDK Identity. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-chimesdkidentity-doc
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Identity documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-chimesdkidentity
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-chimesdkidentity) = 1.11.0

%description   -n gem-aws-sdk-chimesdkidentity-doc
AWS SDK for Ruby - Amazon Chime SDK Identity documentation files.

%description   -n gem-aws-sdk-chimesdkidentity-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-chimesdkidentity.


%package       -n gem-aws-sdk-chimesdkidentity-devel
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Identity development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-chimesdkidentity
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-chimesdkidentity) = 1.11.0

%description   -n gem-aws-sdk-chimesdkidentity-devel
AWS SDK for Ruby - Amazon Chime SDK Identity development package.

%description   -n gem-aws-sdk-chimesdkidentity-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-chimesdkidentity.


%package       -n gem-aws-sdk-chimesdkmeetings
Version:       1.16.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Meetings
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-chimesdkmeetings) = 1.16.0

%description   -n gem-aws-sdk-chimesdkmeetings
Official AWS Ruby gem for Amazon Chime SDK Meetings. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-chimesdkmeetings-doc
Version:       1.16.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Meetings documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-chimesdkmeetings
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-chimesdkmeetings) = 1.16.0

%description   -n gem-aws-sdk-chimesdkmeetings-doc
AWS SDK for Ruby - Amazon Chime SDK Meetings documentation files.

%description   -n gem-aws-sdk-chimesdkmeetings-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-chimesdkmeetings.


%package       -n gem-aws-sdk-chimesdkmeetings-devel
Version:       1.16.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Meetings development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-chimesdkmeetings
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-chimesdkmeetings) = 1.16.0

%description   -n gem-aws-sdk-chimesdkmeetings-devel
AWS SDK for Ruby - Amazon Chime SDK Meetings development package.

%description   -n gem-aws-sdk-chimesdkmeetings-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-chimesdkmeetings.


%package       -n gem-aws-sdk-cloudwatchevents
Version:       1.59.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cloudwatchevents) = 1.59.0

%description   -n gem-aws-sdk-cloudwatchevents
Official AWS Ruby gem for Amazon CloudWatch Events. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-cloudwatchevents-doc
Version:       1.59.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudwatchevents
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatchevents) = 1.59.0

%description   -n gem-aws-sdk-cloudwatchevents-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-cloudwatchevents-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudwatchevents.


%package       -n gem-aws-sdk-cloudwatchevents-devel
Version:       1.59.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudwatchevents
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatchevents) = 1.59.0

%description   -n gem-aws-sdk-cloudwatchevents-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-cloudwatchevents-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudwatchevents.


%package       -n gem-aws-sdk-codeguruprofiler
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-codeguruprofiler) = 1.26.0

%description   -n gem-aws-sdk-codeguruprofiler
Official AWS Ruby gem for Amazon CodeGuru Profiler. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-codeguruprofiler-doc
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codeguruprofiler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codeguruprofiler) = 1.26.0

%description   -n gem-aws-sdk-codeguruprofiler-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-codeguruprofiler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codeguruprofiler.


%package       -n gem-aws-sdk-codeguruprofiler-devel
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codeguruprofiler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codeguruprofiler) = 1.26.0

%description   -n gem-aws-sdk-codeguruprofiler-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-codeguruprofiler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codeguruprofiler.


%package       -n gem-aws-sdk-codegurureviewer
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-codegurureviewer) = 1.35.0

%description   -n gem-aws-sdk-codegurureviewer
Official AWS Ruby gem for Amazon CodeGuru Reviewer (CodeGuruReviewer). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-codegurureviewer-doc
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codegurureviewer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codegurureviewer) = 1.35.0

%description   -n gem-aws-sdk-codegurureviewer-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon CodeGuru Reviewer (CodeGuruReviewer). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-codegurureviewer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codegurureviewer.


%package       -n gem-aws-sdk-codegurureviewer-devel
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codegurureviewer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codegurureviewer) = 1.35.0

%description   -n gem-aws-sdk-codegurureviewer-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon CodeGuru Reviewer (CodeGuruReviewer). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-codegurureviewer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codegurureviewer.


%package       -n gem-aws-sdk-computeoptimizer
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-computeoptimizer) = 1.37.0

%description   -n gem-aws-sdk-computeoptimizer
Official AWS Ruby gem for AWS Compute Optimizer. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-computeoptimizer-doc
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-computeoptimizer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-computeoptimizer) = 1.37.0

%description   -n gem-aws-sdk-computeoptimizer-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-computeoptimizer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-computeoptimizer.


%package       -n gem-aws-sdk-computeoptimizer-devel
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-computeoptimizer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-computeoptimizer) = 1.37.0

%description   -n gem-aws-sdk-computeoptimizer-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-computeoptimizer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-computeoptimizer.


%package       -n gem-aws-sdk-customerprofiles
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-customerprofiles) = 1.26.0

%description   -n gem-aws-sdk-customerprofiles
Official AWS Ruby gem for Amazon Connect Customer Profiles (Customer Profiles).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-customerprofiles-doc
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-customerprofiles
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-customerprofiles) = 1.26.0

%description   -n gem-aws-sdk-customerprofiles-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Connect Customer Profiles (Customer Profiles).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-customerprofiles-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-customerprofiles.


%package       -n gem-aws-sdk-customerprofiles-devel
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-customerprofiles
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-customerprofiles) = 1.26.0

%description   -n gem-aws-sdk-customerprofiles-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Connect Customer Profiles (Customer Profiles).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-customerprofiles-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-customerprofiles.


%package       -n gem-aws-sdk-directoryservice
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-directoryservice) = 1.53.0

%description   -n gem-aws-sdk-directoryservice
Official AWS Ruby gem for AWS Directory Service (Directory Service). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-directoryservice-doc
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-directoryservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-directoryservice) = 1.53.0

%description   -n gem-aws-sdk-directoryservice-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Directory Service (Directory Service). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-directoryservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-directoryservice.


%package       -n gem-aws-sdk-directoryservice-devel
Version:       1.53.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-directoryservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-directoryservice) = 1.53.0

%description   -n gem-aws-sdk-directoryservice-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Directory Service (Directory Service). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-directoryservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-directoryservice.


%package       -n gem-aws-sdk-elasticbeanstalk
Version:       1.54.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-elasticbeanstalk) = 1.54.0

%description   -n gem-aws-sdk-elasticbeanstalk
Official AWS Ruby gem for AWS Elastic Beanstalk (Elastic Beanstalk). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-elasticbeanstalk-doc
Version:       1.54.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-elasticbeanstalk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticbeanstalk) = 1.54.0

%description   -n gem-aws-sdk-elasticbeanstalk-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Elastic Beanstalk (Elastic Beanstalk). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-elasticbeanstalk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-elasticbeanstalk.


%package       -n gem-aws-sdk-elasticbeanstalk-devel
Version:       1.54.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-elasticbeanstalk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticbeanstalk) = 1.54.0

%description   -n gem-aws-sdk-elasticbeanstalk-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Elastic Beanstalk (Elastic Beanstalk). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-elasticbeanstalk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-elasticbeanstalk.


%package       -n gem-aws-sdk-elasticinference
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-elasticinference) = 1.23.0

%description   -n gem-aws-sdk-elasticinference
Official AWS Ruby gem for Amazon Elastic Inference (Amazon Elastic Inference).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-elasticinference-doc
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-elasticinference
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticinference) = 1.23.0

%description   -n gem-aws-sdk-elasticinference-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Elastic Inference (Amazon Elastic Inference).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-elasticinference-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-elasticinference.


%package       -n gem-aws-sdk-elasticinference-devel
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-elasticinference
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticinference) = 1.23.0

%description   -n gem-aws-sdk-elasticinference-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Elastic Inference (Amazon Elastic Inference).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-elasticinference-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-elasticinference.


%package       -n gem-aws-sdk-iotdeviceadvisor
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iotdeviceadvisor) = 1.18.0

%description   -n gem-aws-sdk-iotdeviceadvisor
Official AWS Ruby gem for AWS IoT Core Device Advisor (AWSIoTDeviceAdvisor).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-iotdeviceadvisor-doc
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotdeviceadvisor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotdeviceadvisor) = 1.18.0

%description   -n gem-aws-sdk-iotdeviceadvisor-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS IoT Core Device Advisor (AWSIoTDeviceAdvisor).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iotdeviceadvisor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotdeviceadvisor.


%package       -n gem-aws-sdk-iotdeviceadvisor-devel
Version:       1.18.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotdeviceadvisor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotdeviceadvisor) = 1.18.0

%description   -n gem-aws-sdk-iotdeviceadvisor-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS IoT Core Device Advisor (AWSIoTDeviceAdvisor).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iotdeviceadvisor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotdeviceadvisor.


%package       -n gem-aws-sdk-iotjobsdataplane
Version:       1.38.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iotjobsdataplane) = 1.38.0

%description   -n gem-aws-sdk-iotjobsdataplane
Official AWS Ruby gem for AWS IoT Jobs Data Plane. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-iotjobsdataplane-doc
Version:       1.38.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotjobsdataplane
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotjobsdataplane) = 1.38.0

%description   -n gem-aws-sdk-iotjobsdataplane-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-iotjobsdataplane-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotjobsdataplane.


%package       -n gem-aws-sdk-iotjobsdataplane-devel
Version:       1.38.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotjobsdataplane
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotjobsdataplane) = 1.38.0

%description   -n gem-aws-sdk-iotjobsdataplane-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-iotjobsdataplane-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotjobsdataplane.


%package       -n gem-aws-sdk-kinesisanalytics
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-kinesisanalytics) = 1.42.0

%description   -n gem-aws-sdk-kinesisanalytics
Official AWS Ruby gem for Amazon Kinesis Analytics (Kinesis Analytics). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kinesisanalytics-doc
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesisanalytics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisanalytics) = 1.42.0

%description   -n gem-aws-sdk-kinesisanalytics-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Kinesis Analytics (Kinesis Analytics). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisanalytics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesisanalytics.


%package       -n gem-aws-sdk-kinesisanalytics-devel
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesisanalytics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisanalytics) = 1.42.0

%description   -n gem-aws-sdk-kinesisanalytics-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Kinesis Analytics (Kinesis Analytics). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisanalytics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesisanalytics.


%package       -n gem-aws-sdk-lookoutequipment
Version:       1.16.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-lookoutequipment) = 1.16.0

%description   -n gem-aws-sdk-lookoutequipment
Official AWS Ruby gem for Amazon Lookout for Equipment (LookoutEquipment). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-lookoutequipment-doc
Version:       1.16.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lookoutequipment
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lookoutequipment) = 1.16.0

%description   -n gem-aws-sdk-lookoutequipment-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Lookout for Equipment (LookoutEquipment). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lookoutequipment-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lookoutequipment.


%package       -n gem-aws-sdk-lookoutequipment-devel
Version:       1.16.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lookoutequipment
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lookoutequipment) = 1.16.0

%description   -n gem-aws-sdk-lookoutequipment-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Lookout for Equipment (LookoutEquipment). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lookoutequipment-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lookoutequipment.


%package       -n gem-aws-sdk-lookoutforvision
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-lookoutforvision) = 1.19.0

%description   -n gem-aws-sdk-lookoutforvision
Official AWS Ruby gem for Amazon Lookout for Vision. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-lookoutforvision-doc
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lookoutforvision
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lookoutforvision) = 1.19.0

%description   -n gem-aws-sdk-lookoutforvision-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-lookoutforvision-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lookoutforvision.


%package       -n gem-aws-sdk-lookoutforvision-devel
Version:       1.19.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lookoutforvision
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lookoutforvision) = 1.19.0

%description   -n gem-aws-sdk-lookoutforvision-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-lookoutforvision-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lookoutforvision.


%package       -n gem-aws-sdk-pinpointsmsvoice
Version:       1.34.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-pinpointsmsvoice) = 1.34.0

%description   -n gem-aws-sdk-pinpointsmsvoice
Official AWS Ruby gem for Amazon Pinpoint SMS and Voice Service (Pinpoint SMS
Voice). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-pinpointsmsvoice-doc
Version:       1.34.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-pinpointsmsvoice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-pinpointsmsvoice) = 1.34.0

%description   -n gem-aws-sdk-pinpointsmsvoice-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Pinpoint SMS and Voice Service (Pinpoint SMS
Voice). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pinpointsmsvoice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-pinpointsmsvoice.


%package       -n gem-aws-sdk-pinpointsmsvoice-devel
Version:       1.34.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-pinpointsmsvoice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-pinpointsmsvoice) = 1.34.0

%description   -n gem-aws-sdk-pinpointsmsvoice-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Pinpoint SMS and Voice Service (Pinpoint SMS
Voice). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pinpointsmsvoice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-pinpointsmsvoice.


%package       -n gem-aws-sdk-sagemakermetrics
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - SageMaker Metrics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-sagemakermetrics) = 1.2.0

%description   -n gem-aws-sdk-sagemakermetrics
Official AWS Ruby gem for Amazon SageMaker Metrics Service (SageMaker Metrics).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-sagemakermetrics-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - SageMaker Metrics documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sagemakermetrics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakermetrics) = 1.2.0

%description   -n gem-aws-sdk-sagemakermetrics-doc
AWS SDK for Ruby - SageMaker Metrics documentation files.

Official AWS Ruby gem for Amazon SageMaker Metrics Service (SageMaker Metrics).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sagemakermetrics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sagemakermetrics.


%package       -n gem-aws-sdk-sagemakermetrics-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - SageMaker Metrics development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sagemakermetrics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakermetrics) = 1.2.0

%description   -n gem-aws-sdk-sagemakermetrics-devel
AWS SDK for Ruby - SageMaker Metrics development package.

Official AWS Ruby gem for Amazon SageMaker Metrics Service (SageMaker Metrics).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sagemakermetrics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sagemakermetrics.


%package       -n gem-aws-sdk-sagemakerruntime
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-sagemakerruntime) = 1.46.0

%description   -n gem-aws-sdk-sagemakerruntime
Official AWS Ruby gem for Amazon SageMaker Runtime. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-sagemakerruntime-doc
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sagemakerruntime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakerruntime) = 1.46.0

%description   -n gem-aws-sdk-sagemakerruntime-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-sagemakerruntime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sagemakerruntime.


%package       -n gem-aws-sdk-sagemakerruntime-devel
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sagemakerruntime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakerruntime) = 1.46.0

%description   -n gem-aws-sdk-sagemakerruntime-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-sagemakerruntime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sagemakerruntime.


%package       -n gem-aws-sdk-servicediscovery
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-servicediscovery) = 1.49.0

%description   -n gem-aws-sdk-servicediscovery
Official AWS Ruby gem for AWS Cloud Map (ServiceDiscovery). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-servicediscovery-doc
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-servicediscovery
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-servicediscovery) = 1.49.0

%description   -n gem-aws-sdk-servicediscovery-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Cloud Map (ServiceDiscovery). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-servicediscovery-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-servicediscovery.


%package       -n gem-aws-sdk-servicediscovery-devel
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-servicediscovery
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-servicediscovery) = 1.49.0

%description   -n gem-aws-sdk-servicediscovery-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Cloud Map (ServiceDiscovery). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-servicediscovery-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-servicediscovery.


%package       -n gem-aws-sdk-chimesdkmessaging
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Messaging
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-chimesdkmessaging) = 1.15.0

%description   -n gem-aws-sdk-chimesdkmessaging
Official AWS Ruby gem for Amazon Chime SDK Messaging. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-chimesdkmessaging-doc
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Messaging documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-chimesdkmessaging
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-chimesdkmessaging) = 1.15.0

%description   -n gem-aws-sdk-chimesdkmessaging-doc
AWS SDK for Ruby - Amazon Chime SDK Messaging documentation files.

%description   -n gem-aws-sdk-chimesdkmessaging-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-chimesdkmessaging.


%package       -n gem-aws-sdk-chimesdkmessaging-devel
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Messaging development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-chimesdkmessaging
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-chimesdkmessaging) = 1.15.0

%description   -n gem-aws-sdk-chimesdkmessaging-devel
AWS SDK for Ruby - Amazon Chime SDK Messaging development package.

%description   -n gem-aws-sdk-chimesdkmessaging-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-chimesdkmessaging.


%package       -n gem-aws-sdk-cloudsearchdomain
Version:       1.34.1
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cloudsearchdomain) = 1.34.1

%description   -n gem-aws-sdk-cloudsearchdomain
Official AWS Ruby gem for Amazon CloudSearch Domain. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-cloudsearchdomain-doc
Version:       1.34.1
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudsearchdomain
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudsearchdomain) = 1.34.1

%description   -n gem-aws-sdk-cloudsearchdomain-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-cloudsearchdomain-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudsearchdomain.


%package       -n gem-aws-sdk-cloudsearchdomain-devel
Version:       1.34.1
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudsearchdomain
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudsearchdomain) = 1.34.1

%description   -n gem-aws-sdk-cloudsearchdomain-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-cloudsearchdomain-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudsearchdomain.


%package       -n gem-aws-sdk-comprehendmedical
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-comprehendmedical) = 1.39.0

%description   -n gem-aws-sdk-comprehendmedical
Official AWS Ruby gem for AWS Comprehend Medical (ComprehendMedical). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-comprehendmedical-doc
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-comprehendmedical
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-comprehendmedical) = 1.39.0

%description   -n gem-aws-sdk-comprehendmedical-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Comprehend Medical (ComprehendMedical). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-comprehendmedical-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-comprehendmedical.


%package       -n gem-aws-sdk-comprehendmedical-devel
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-comprehendmedical
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-comprehendmedical) = 1.39.0

%description   -n gem-aws-sdk-comprehendmedical-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Comprehend Medical (ComprehendMedical). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-comprehendmedical-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-comprehendmedical.


%package       -n gem-aws-sdk-elastictranscoder
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-elastictranscoder) = 1.40.0

%description   -n gem-aws-sdk-elastictranscoder
Official AWS Ruby gem for Amazon Elastic Transcoder. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-elastictranscoder-doc
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-elastictranscoder
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-elastictranscoder) = 1.40.0

%description   -n gem-aws-sdk-elastictranscoder-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-elastictranscoder-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-elastictranscoder.


%package       -n gem-aws-sdk-elastictranscoder-devel
Version:       1.40.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-elastictranscoder
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-elastictranscoder) = 1.40.0

%description   -n gem-aws-sdk-elastictranscoder-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-elastictranscoder-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-elastictranscoder.


%package       -n gem-aws-sdk-globalaccelerator
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-globalaccelerator) = 1.43.0

%description   -n gem-aws-sdk-globalaccelerator
Official AWS Ruby gem for AWS Global Accelerator. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-globalaccelerator-doc
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-globalaccelerator
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-globalaccelerator) = 1.43.0

%description   -n gem-aws-sdk-globalaccelerator-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-globalaccelerator-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-globalaccelerator.


%package       -n gem-aws-sdk-globalaccelerator-devel
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-globalaccelerator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-globalaccelerator) = 1.43.0

%description   -n gem-aws-sdk-globalaccelerator-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-globalaccelerator-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-globalaccelerator.


%package       -n gem-aws-sdk-iot1clickprojects
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iot1clickprojects) = 1.39.0

%description   -n gem-aws-sdk-iot1clickprojects
Official AWS Ruby gem for AWS IoT 1-Click Projects Service (AWS IoT 1-Click
Projects). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-iot1clickprojects-doc
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iot1clickprojects
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iot1clickprojects) = 1.39.0

%description   -n gem-aws-sdk-iot1clickprojects-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS IoT 1-Click Projects Service (AWS IoT 1-Click
Projects). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iot1clickprojects-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iot1clickprojects.


%package       -n gem-aws-sdk-iot1clickprojects-devel
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iot1clickprojects
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iot1clickprojects) = 1.39.0

%description   -n gem-aws-sdk-iot1clickprojects-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS IoT 1-Click Projects Service (AWS IoT 1-Click
Projects). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iot1clickprojects-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iot1clickprojects.


%package       -n gem-aws-sdk-kinesisvideomedia
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-kinesisvideomedia) = 1.39.0

%description   -n gem-aws-sdk-kinesisvideomedia
Official AWS Ruby gem for Amazon Kinesis Video Streams Media (Kinesis Video
Media). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kinesisvideomedia-doc
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesisvideomedia
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideomedia) = 1.39.0

%description   -n gem-aws-sdk-kinesisvideomedia-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Kinesis Video Streams Media (Kinesis Video
Media). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideomedia-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesisvideomedia.


%package       -n gem-aws-sdk-kinesisvideomedia-devel
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesisvideomedia
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideomedia) = 1.39.0

%description   -n gem-aws-sdk-kinesisvideomedia-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Kinesis Video Streams Media (Kinesis Video
Media). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideomedia-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesisvideomedia.


%package       -n gem-aws-sdk-managedblockchain
Version:       1.36.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-managedblockchain) = 1.36.0

%description   -n gem-aws-sdk-managedblockchain
Official AWS Ruby gem for Amazon Managed Blockchain (ManagedBlockchain). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-managedblockchain-doc
Version:       1.36.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-managedblockchain
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-managedblockchain) = 1.36.0

%description   -n gem-aws-sdk-managedblockchain-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Managed Blockchain (ManagedBlockchain). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-managedblockchain-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-managedblockchain.


%package       -n gem-aws-sdk-managedblockchain-devel
Version:       1.36.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-managedblockchain
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-managedblockchain) = 1.36.0

%description   -n gem-aws-sdk-managedblockchain-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Managed Blockchain (ManagedBlockchain). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-managedblockchain-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-managedblockchain.


%package       -n gem-aws-sdk-opensearchservice
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon OpenSearch Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-opensearchservice) = 1.15.0

%description   -n gem-aws-sdk-opensearchservice
Official AWS Ruby gem for Amazon OpenSearch Service. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-opensearchservice-doc
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon OpenSearch Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-opensearchservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-opensearchservice) = 1.15.0

%description   -n gem-aws-sdk-opensearchservice-doc
AWS SDK for Ruby - Amazon OpenSearch Service documentation files.

%description   -n gem-aws-sdk-opensearchservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-opensearchservice.


%package       -n gem-aws-sdk-opensearchservice-devel
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon OpenSearch Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-opensearchservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-opensearchservice) = 1.15.0

%description   -n gem-aws-sdk-opensearchservice-devel
AWS SDK for Ruby - Amazon OpenSearch Service development package.

%description   -n gem-aws-sdk-opensearchservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-opensearchservice.


%package       -n gem-aws-sdk-personalizeevents
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-personalizeevents) = 1.30.0

%description   -n gem-aws-sdk-personalizeevents
Official AWS Ruby gem for Amazon Personalize Events. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-personalizeevents-doc
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-personalizeevents
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-personalizeevents) = 1.30.0

%description   -n gem-aws-sdk-personalizeevents-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-personalizeevents-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-personalizeevents.


%package       -n gem-aws-sdk-personalizeevents-devel
Version:       1.30.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-personalizeevents
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-personalizeevents) = 1.30.0

%description   -n gem-aws-sdk-personalizeevents-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-personalizeevents-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-personalizeevents.


%package       -n gem-aws-sdk-prometheusservice
Version:       1.17.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-prometheusservice) = 1.17.0

%description   -n gem-aws-sdk-prometheusservice
Official AWS Ruby gem for Amazon Prometheus Service. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-prometheusservice-doc
Version:       1.17.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-prometheusservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-prometheusservice) = 1.17.0

%description   -n gem-aws-sdk-prometheusservice-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-prometheusservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-prometheusservice.


%package       -n gem-aws-sdk-prometheusservice-devel
Version:       1.17.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-prometheusservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-prometheusservice) = 1.17.0

%description   -n gem-aws-sdk-prometheusservice-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-prometheusservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-prometheusservice.


%package       -n gem-aws-sdk-resourceexplorer2
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Resource Explorer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-resourceexplorer2) = 1.3.0

%description   -n gem-aws-sdk-resourceexplorer2
Official AWS Ruby gem for AWS Resource Explorer. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-resourceexplorer2-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Resource Explorer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-resourceexplorer2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-resourceexplorer2) = 1.3.0

%description   -n gem-aws-sdk-resourceexplorer2-doc
AWS SDK for Ruby - AWS Resource Explorer documentation files.

%description   -n gem-aws-sdk-resourceexplorer2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-resourceexplorer2.


%package       -n gem-aws-sdk-resourceexplorer2-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Resource Explorer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-resourceexplorer2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-resourceexplorer2) = 1.3.0

%description   -n gem-aws-sdk-resourceexplorer2-devel
AWS SDK for Ruby - AWS Resource Explorer development package.

%description   -n gem-aws-sdk-resourceexplorer2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-resourceexplorer2.


%package       -n gem-aws-sdk-transcribeservice
Version:       1.81.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-transcribeservice) = 1.81.0

%description   -n gem-aws-sdk-transcribeservice
Official AWS Ruby gem for Amazon Transcribe Service. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-transcribeservice-doc
Version:       1.81.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-transcribeservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-transcribeservice) = 1.81.0

%description   -n gem-aws-sdk-transcribeservice-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-transcribeservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-transcribeservice.


%package       -n gem-aws-sdk-transcribeservice-devel
Version:       1.81.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-transcribeservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-transcribeservice) = 1.81.0

%description   -n gem-aws-sdk-transcribeservice-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-transcribeservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-transcribeservice.


%package       -n gem-aws-sdk-augmentedairuntime
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-augmentedairuntime) = 1.25.0

%description   -n gem-aws-sdk-augmentedairuntime
Official AWS Ruby gem for Amazon Augmented AI Runtime. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-augmentedairuntime-doc
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-augmentedairuntime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-augmentedairuntime) = 1.25.0

%description   -n gem-aws-sdk-augmentedairuntime-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-augmentedairuntime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-augmentedairuntime.


%package       -n gem-aws-sdk-augmentedairuntime-devel
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-augmentedairuntime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-augmentedairuntime) = 1.25.0

%description   -n gem-aws-sdk-augmentedairuntime-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-augmentedairuntime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-augmentedairuntime.


%package       -n gem-aws-sdk-connectcontactlens
Version:       1.13.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-connectcontactlens) = 1.13.0

%description   -n gem-aws-sdk-connectcontactlens
Official AWS Ruby gem for Amazon Connect Contact Lens. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-connectcontactlens-doc
Version:       1.13.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-connectcontactlens
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-connectcontactlens) = 1.13.0

%description   -n gem-aws-sdk-connectcontactlens-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-connectcontactlens-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-connectcontactlens.


%package       -n gem-aws-sdk-connectcontactlens-devel
Version:       1.13.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-connectcontactlens
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-connectcontactlens) = 1.13.0

%description   -n gem-aws-sdk-connectcontactlens-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-connectcontactlens-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-connectcontactlens.


%package       -n gem-aws-sdk-connectparticipant
Version:       1.27.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-connectparticipant) = 1.27.0

%description   -n gem-aws-sdk-connectparticipant
Official AWS Ruby gem for Amazon Connect Participant Service (Amazon Connect
Participant). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-connectparticipant-doc
Version:       1.27.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-connectparticipant
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-connectparticipant) = 1.27.0

%description   -n gem-aws-sdk-connectparticipant-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Connect Participant Service (Amazon Connect
Participant). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-connectparticipant-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-connectparticipant.


%package       -n gem-aws-sdk-connectparticipant-devel
Version:       1.27.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-connectparticipant
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-connectparticipant) = 1.27.0

%description   -n gem-aws-sdk-connectparticipant-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Connect Participant Service (Amazon Connect
Participant). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-connectparticipant-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-connectparticipant.


%package       -n gem-aws-sdk-ec2instanceconnect
Version:       1.27.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-ec2instanceconnect) = 1.27.0

%description   -n gem-aws-sdk-ec2instanceconnect
Official AWS Ruby gem for AWS EC2 Instance Connect (EC2 Instance Connect). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ec2instanceconnect-doc
Version:       1.27.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ec2instanceconnect
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ec2instanceconnect) = 1.27.0

%description   -n gem-aws-sdk-ec2instanceconnect-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS EC2 Instance Connect (EC2 Instance Connect). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ec2instanceconnect-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ec2instanceconnect.


%package       -n gem-aws-sdk-ec2instanceconnect-devel
Version:       1.27.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ec2instanceconnect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ec2instanceconnect) = 1.27.0

%description   -n gem-aws-sdk-ec2instanceconnect-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS EC2 Instance Connect (EC2 Instance Connect). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ec2instanceconnect-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ec2instanceconnect.


%package       -n gem-aws-sdk-iotsecuretunneling
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iotsecuretunneling) = 1.23.0

%description   -n gem-aws-sdk-iotsecuretunneling
Official AWS Ruby gem for AWS IoT Secure Tunneling. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-iotsecuretunneling-doc
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotsecuretunneling
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotsecuretunneling) = 1.23.0

%description   -n gem-aws-sdk-iotsecuretunneling-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-iotsecuretunneling-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotsecuretunneling.


%package       -n gem-aws-sdk-iotsecuretunneling-devel
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotsecuretunneling
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotsecuretunneling) = 1.23.0

%description   -n gem-aws-sdk-iotsecuretunneling-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-iotsecuretunneling-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotsecuretunneling.


%package       -n gem-aws-sdk-kinesisanalyticsv2
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-kinesisanalyticsv2) = 1.43.0

%description   -n gem-aws-sdk-kinesisanalyticsv2
Official AWS Ruby gem for Amazon Kinesis Analytics (Kinesis Analytics V2). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kinesisanalyticsv2-doc
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesisanalyticsv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisanalyticsv2) = 1.43.0

%description   -n gem-aws-sdk-kinesisanalyticsv2-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Kinesis Analytics (Kinesis Analytics V2). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisanalyticsv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesisanalyticsv2.


%package       -n gem-aws-sdk-kinesisanalyticsv2-devel
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesisanalyticsv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisanalyticsv2) = 1.43.0

%description   -n gem-aws-sdk-kinesisanalyticsv2-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Kinesis Analytics (Kinesis Analytics V2). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisanalyticsv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesisanalyticsv2.


%package       -n gem-aws-sdk-marketplacecatalog
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-marketplacecatalog) = 1.25.0

%description   -n gem-aws-sdk-marketplacecatalog
Official AWS Ruby gem for AWS Marketplace Catalog Service (AWS Marketplace
Catalog). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-marketplacecatalog-doc
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-marketplacecatalog
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplacecatalog) = 1.25.0

%description   -n gem-aws-sdk-marketplacecatalog-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Marketplace Catalog Service (AWS Marketplace
Catalog). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-marketplacecatalog-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-marketplacecatalog.


%package       -n gem-aws-sdk-marketplacecatalog-devel
Version:       1.25.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-marketplacecatalog
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplacecatalog) = 1.25.0

%description   -n gem-aws-sdk-marketplacecatalog-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Marketplace Catalog Service (AWS Marketplace
Catalog). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-marketplacecatalog-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-marketplacecatalog.


%package       -n gem-aws-sdk-migrationhubconfig
Version:       1.22.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-migrationhubconfig) = 1.22.0

%description   -n gem-aws-sdk-migrationhubconfig
Official AWS Ruby gem for AWS Migration Hub Config. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-migrationhubconfig-doc
Version:       1.22.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-migrationhubconfig
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-migrationhubconfig) = 1.22.0

%description   -n gem-aws-sdk-migrationhubconfig-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-migrationhubconfig-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-migrationhubconfig.


%package       -n gem-aws-sdk-migrationhubconfig-devel
Version:       1.22.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-migrationhubconfig
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-migrationhubconfig) = 1.22.0

%description   -n gem-aws-sdk-migrationhubconfig-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-migrationhubconfig-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-migrationhubconfig.


%package       -n gem-aws-sdk-personalizeruntime
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-personalizeruntime) = 1.35.0

%description   -n gem-aws-sdk-personalizeruntime
Official AWS Ruby gem for Amazon Personalize Runtime. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-personalizeruntime-doc
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-personalizeruntime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-personalizeruntime) = 1.35.0

%description   -n gem-aws-sdk-personalizeruntime-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-personalizeruntime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-personalizeruntime.


%package       -n gem-aws-sdk-personalizeruntime-devel
Version:       1.35.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-personalizeruntime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-personalizeruntime) = 1.35.0

%description   -n gem-aws-sdk-personalizeruntime-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-personalizeruntime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-personalizeruntime.


%package       -n gem-aws-sdk-pinpointsmsvoicev2
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Pinpoint SMS Voice V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-pinpointsmsvoicev2) = 1.2.0

%description   -n gem-aws-sdk-pinpointsmsvoicev2
Official AWS Ruby gem for Amazon Pinpoint SMS Voice V2. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-pinpointsmsvoicev2-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Pinpoint SMS Voice V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-pinpointsmsvoicev2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-pinpointsmsvoicev2) = 1.2.0

%description   -n gem-aws-sdk-pinpointsmsvoicev2-doc
AWS SDK for Ruby - Amazon Pinpoint SMS Voice V2 documentation files.

%description   -n gem-aws-sdk-pinpointsmsvoicev2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-pinpointsmsvoicev2.


%package       -n gem-aws-sdk-pinpointsmsvoicev2-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Pinpoint SMS Voice V2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-pinpointsmsvoicev2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-pinpointsmsvoicev2) = 1.2.0

%description   -n gem-aws-sdk-pinpointsmsvoicev2-devel
AWS SDK for Ruby - Amazon Pinpoint SMS Voice V2 development package.

%description   -n gem-aws-sdk-pinpointsmsvoicev2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-pinpointsmsvoicev2.


%package       -n gem-aws-sdk-redshiftserverless
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - Redshift Serverless
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-redshiftserverless) = 1.7.0

%description   -n gem-aws-sdk-redshiftserverless
Official AWS Ruby gem for Redshift Serverless. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-redshiftserverless-doc
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - Redshift Serverless documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-redshiftserverless
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-redshiftserverless) = 1.7.0

%description   -n gem-aws-sdk-redshiftserverless-doc
AWS SDK for Ruby - Redshift Serverless documentation files.

%description   -n gem-aws-sdk-redshiftserverless-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-redshiftserverless.


%package       -n gem-aws-sdk-redshiftserverless-devel
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - Redshift Serverless development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-redshiftserverless
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-redshiftserverless) = 1.7.0

%description   -n gem-aws-sdk-redshiftserverless-devel
AWS SDK for Ruby - Redshift Serverless development package.

%description   -n gem-aws-sdk-redshiftserverless-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-redshiftserverless.


%package       -n gem-aws-sdk-applicationinsights
Version:       1.33.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-applicationinsights) = 1.33.0

%description   -n gem-aws-sdk-applicationinsights
Official AWS Ruby gem for Amazon CloudWatch Application Insights (Application
Insights). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-applicationinsights-doc
Version:       1.33.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-applicationinsights
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationinsights) = 1.33.0

%description   -n gem-aws-sdk-applicationinsights-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon CloudWatch Application Insights (Application
Insights). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-applicationinsights-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-applicationinsights.


%package       -n gem-aws-sdk-applicationinsights-devel
Version:       1.33.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-applicationinsights
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationinsights) = 1.33.0

%description   -n gem-aws-sdk-applicationinsights-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon CloudWatch Application Insights (Application
Insights). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-applicationinsights-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-applicationinsights.


%package       -n gem-aws-sdk-cloudwatchevidently
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudWatch Evidently
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cloudwatchevidently) = 1.10.0

%description   -n gem-aws-sdk-cloudwatchevidently
Official AWS Ruby gem for Amazon CloudWatch Evidently. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-cloudwatchevidently-doc
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudWatch Evidently documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudwatchevidently
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatchevidently) = 1.10.0

%description   -n gem-aws-sdk-cloudwatchevidently-doc
AWS SDK for Ruby - Amazon CloudWatch Evidently documentation files.

%description   -n gem-aws-sdk-cloudwatchevidently-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudwatchevidently.


%package       -n gem-aws-sdk-cloudwatchevidently-devel
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudWatch Evidently development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudwatchevidently
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatchevidently) = 1.10.0

%description   -n gem-aws-sdk-cloudwatchevidently-devel
AWS SDK for Ruby - Amazon CloudWatch Evidently development package.

%description   -n gem-aws-sdk-cloudwatchevidently-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudwatchevidently.


%package       -n gem-aws-sdk-codestarconnections
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-codestarconnections) = 1.26.0

%description   -n gem-aws-sdk-codestarconnections
Official AWS Ruby gem for AWS CodeStar connections. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-codestarconnections-doc
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codestarconnections
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codestarconnections) = 1.26.0

%description   -n gem-aws-sdk-codestarconnections-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-codestarconnections-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codestarconnections.


%package       -n gem-aws-sdk-codestarconnections-devel
Version:       1.26.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codestarconnections
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codestarconnections) = 1.26.0

%description   -n gem-aws-sdk-codestarconnections-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-codestarconnections-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codestarconnections.


%package       -n gem-aws-sdk-marketplacemetering
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-marketplacemetering) = 1.46.0

%description   -n gem-aws-sdk-marketplacemetering
Official AWS Ruby gem for AWSMarketplace Metering. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-marketplacemetering-doc
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-marketplacemetering
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplacemetering) = 1.46.0

%description   -n gem-aws-sdk-marketplacemetering-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-marketplacemetering-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-marketplacemetering.


%package       -n gem-aws-sdk-marketplacemetering-devel
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-marketplacemetering
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplacemetering) = 1.46.0

%description   -n gem-aws-sdk-marketplacemetering-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-marketplacemetering-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-marketplacemetering.


%package       -n gem-aws-sdk-sagemakergeospatial
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SageMaker geospatial capabilities
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-sagemakergeospatial) = 1.1.0

%description   -n gem-aws-sdk-sagemakergeospatial
Official AWS Ruby gem for Amazon SageMaker geospatial capabilities. This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-sagemakergeospatial-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SageMaker geospatial capabilities documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sagemakergeospatial
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakergeospatial) = 1.1.0

%description   -n gem-aws-sdk-sagemakergeospatial-doc
AWS SDK for Ruby - Amazon SageMaker geospatial capabilities documentation
files.

Official AWS Ruby gem for Amazon SageMaker geospatial capabilities. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sagemakergeospatial-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sagemakergeospatial.


%package       -n gem-aws-sdk-sagemakergeospatial-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SageMaker geospatial capabilities development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sagemakergeospatial
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakergeospatial) = 1.1.0

%description   -n gem-aws-sdk-sagemakergeospatial-devel
AWS SDK for Ruby - Amazon SageMaker geospatial capabilities development
package.

Official AWS Ruby gem for Amazon SageMaker geospatial capabilities. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sagemakergeospatial-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sagemakergeospatial.


%package       -n gem-aws-sdk-workmailmessageflow
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-workmailmessageflow) = 1.23.0

%description   -n gem-aws-sdk-workmailmessageflow
Official AWS Ruby gem for Amazon WorkMail Message Flow. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-workmailmessageflow-doc
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-workmailmessageflow
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-workmailmessageflow) = 1.23.0

%description   -n gem-aws-sdk-workmailmessageflow-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-workmailmessageflow-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-workmailmessageflow.


%package       -n gem-aws-sdk-workmailmessageflow-devel
Version:       1.23.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-workmailmessageflow
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-workmailmessageflow) = 1.23.0

%description   -n gem-aws-sdk-workmailmessageflow-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-workmailmessageflow-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-workmailmessageflow.


%package       -n gem-aws-sdk-connectwisdomservice
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Connect Wisdom Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-connectwisdomservice) = 1.12.0

%description   -n gem-aws-sdk-connectwisdomservice
Official AWS Ruby gem for Amazon Connect Wisdom Service. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-connectwisdomservice-doc
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Connect Wisdom Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-connectwisdomservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-connectwisdomservice) = 1.12.0

%description   -n gem-aws-sdk-connectwisdomservice-doc
AWS SDK for Ruby - Amazon Connect Wisdom Service documentation files.

%description   -n gem-aws-sdk-connectwisdomservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-connectwisdomservice.


%package       -n gem-aws-sdk-connectwisdomservice-devel
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Connect Wisdom Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-connectwisdomservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-connectwisdomservice) = 1.12.0

%description   -n gem-aws-sdk-connectwisdomservice-devel
AWS SDK for Ruby - Amazon Connect Wisdom Service development package.

%description   -n gem-aws-sdk-connectwisdomservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-connectwisdomservice.


%package       -n gem-aws-sdk-elasticloadbalancing
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-elasticloadbalancing) = 1.42.0

%description   -n gem-aws-sdk-elasticloadbalancing
Official AWS Ruby gem for Elastic Load Balancing. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-elasticloadbalancing-doc
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-elasticloadbalancing
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticloadbalancing) = 1.42.0

%description   -n gem-aws-sdk-elasticloadbalancing-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-elasticloadbalancing-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-elasticloadbalancing.


%package       -n gem-aws-sdk-elasticloadbalancing-devel
Version:       1.42.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-elasticloadbalancing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticloadbalancing) = 1.42.0

%description   -n gem-aws-sdk-elasticloadbalancing-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-elasticloadbalancing-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-elasticloadbalancing.


%package       -n gem-aws-sdk-elasticsearchservice
Version:       1.69.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-elasticsearchservice) = 1.69.0

%description   -n gem-aws-sdk-elasticsearchservice
Official AWS Ruby gem for Amazon Elasticsearch Service. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-elasticsearchservice-doc
Version:       1.69.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-elasticsearchservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticsearchservice) = 1.69.0

%description   -n gem-aws-sdk-elasticsearchservice-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-elasticsearchservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-elasticsearchservice.


%package       -n gem-aws-sdk-elasticsearchservice-devel
Version:       1.69.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-elasticsearchservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticsearchservice) = 1.69.0

%description   -n gem-aws-sdk-elasticsearchservice-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-elasticsearchservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-elasticsearchservice.


%package       -n gem-aws-sdk-forecastqueryservice
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-forecastqueryservice) = 1.24.0

%description   -n gem-aws-sdk-forecastqueryservice
Official AWS Ruby gem for Amazon Forecast Query Service. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-forecastqueryservice-doc
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-forecastqueryservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-forecastqueryservice) = 1.24.0

%description   -n gem-aws-sdk-forecastqueryservice-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-forecastqueryservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-forecastqueryservice.


%package       -n gem-aws-sdk-forecastqueryservice-devel
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-forecastqueryservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-forecastqueryservice) = 1.24.0

%description   -n gem-aws-sdk-forecastqueryservice-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-forecastqueryservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-forecastqueryservice.


%package       -n gem-aws-sdk-opensearchserverless
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - OpenSearch Service Serverless
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-opensearchserverless) = 1.1.0

%description   -n gem-aws-sdk-opensearchserverless
Official AWS Ruby gem for OpenSearch Service Serverless. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-opensearchserverless-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - OpenSearch Service Serverless documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-opensearchserverless
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-opensearchserverless) = 1.1.0

%description   -n gem-aws-sdk-opensearchserverless-doc
AWS SDK for Ruby - OpenSearch Service Serverless documentation files.

%description   -n gem-aws-sdk-opensearchserverless-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-opensearchserverless.


%package       -n gem-aws-sdk-opensearchserverless-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - OpenSearch Service Serverless development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-opensearchserverless
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-opensearchserverless) = 1.1.0

%description   -n gem-aws-sdk-opensearchserverless-devel
AWS SDK for Ruby - OpenSearch Service Serverless development package.

%description   -n gem-aws-sdk-opensearchserverless-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-opensearchserverless.


%package       -n gem-aws-sdk-sagemakeredgemanager
Version:       1.14.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-sagemakeredgemanager) = 1.14.0

%description   -n gem-aws-sdk-sagemakeredgemanager
Official AWS Ruby gem for Amazon Sagemaker Edge Manager. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-sagemakeredgemanager-doc
Version:       1.14.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sagemakeredgemanager
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakeredgemanager) = 1.14.0

%description   -n gem-aws-sdk-sagemakeredgemanager-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-sagemakeredgemanager-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sagemakeredgemanager.


%package       -n gem-aws-sdk-sagemakeredgemanager-devel
Version:       1.14.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sagemakeredgemanager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakeredgemanager) = 1.14.0

%description   -n gem-aws-sdk-sagemakeredgemanager-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-sagemakeredgemanager-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sagemakeredgemanager.


%package       -n gem-aws-sdk-snowdevicemanagement
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Snow Device Management
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-snowdevicemanagement) = 1.9.0

%description   -n gem-aws-sdk-snowdevicemanagement
Official AWS Ruby gem for AWS Snow Device Management. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-snowdevicemanagement-doc
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Snow Device Management documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-snowdevicemanagement
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-snowdevicemanagement) = 1.9.0

%description   -n gem-aws-sdk-snowdevicemanagement-doc
AWS SDK for Ruby - AWS Snow Device Management documentation files.

%description   -n gem-aws-sdk-snowdevicemanagement-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-snowdevicemanagement.


%package       -n gem-aws-sdk-snowdevicemanagement-devel
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Snow Device Management development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-snowdevicemanagement
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-snowdevicemanagement) = 1.9.0

%description   -n gem-aws-sdk-snowdevicemanagement-devel
AWS SDK for Ruby - AWS Snow Device Management development package.

%description   -n gem-aws-sdk-snowdevicemanagement-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-snowdevicemanagement.


%package       -n gem-aws-sdk-code-generator
Version:       0.4.0.pre
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(kramdown) >= 0
Requires:      gem(mustache) >= 0
Provides:      gem(aws-sdk-code-generator) = 0.4.0

%description   -n gem-aws-sdk-code-generator
Generates the service code for the AWS SDK for Ruby


%package       -n gem-aws-sdk-code-generator-doc
Version:       0.4.0.pre
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-code-generator
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-code-generator) = 0.4.0

%description   -n gem-aws-sdk-code-generator-doc
The official AWS SDK for Ruby documentation files.

Generates the service code for the AWS SDK for Ruby

%description   -n gem-aws-sdk-code-generator-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-code-generator.


%package       -n gem-aws-sdk-code-generator-devel
Version:       0.4.0.pre
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-code-generator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-code-generator) = 0.4.0

%description   -n gem-aws-sdk-code-generator-devel
The official AWS SDK for Ruby development package.

Generates the service code for the AWS SDK for Ruby

%description   -n gem-aws-sdk-code-generator-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-code-generator.


%package       -n gem-aws-sdk-codestarnotifications
Version:       1.22.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-codestarnotifications) = 1.22.0

%description   -n gem-aws-sdk-codestarnotifications
Official AWS Ruby gem for AWS CodeStar Notifications. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-codestarnotifications-doc
Version:       1.22.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codestarnotifications
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codestarnotifications) = 1.22.0

%description   -n gem-aws-sdk-codestarnotifications-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-codestarnotifications-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codestarnotifications.


%package       -n gem-aws-sdk-codestarnotifications-devel
Version:       1.22.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codestarnotifications
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codestarnotifications) = 1.22.0

%description   -n gem-aws-sdk-codestarnotifications-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-codestarnotifications-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codestarnotifications.


%package       -n gem-aws-sdk-appintegrationsservice
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-appintegrationsservice) = 1.15.0

%description   -n gem-aws-sdk-appintegrationsservice
Official AWS Ruby gem for Amazon AppIntegrations Service. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-appintegrationsservice-doc
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appintegrationsservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appintegrationsservice) = 1.15.0

%description   -n gem-aws-sdk-appintegrationsservice-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon AppIntegrations Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-appintegrationsservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appintegrationsservice.


%package       -n gem-aws-sdk-appintegrationsservice-devel
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appintegrationsservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appintegrationsservice) = 1.15.0

%description   -n gem-aws-sdk-appintegrationsservice-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon AppIntegrations Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-appintegrationsservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appintegrationsservice.


%package       -n gem-aws-sdk-applicationautoscaling
Version:       1.66.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-applicationautoscaling) = 1.66.0

%description   -n gem-aws-sdk-applicationautoscaling
Official AWS Ruby gem for Application Auto Scaling. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-applicationautoscaling-doc
Version:       1.66.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-applicationautoscaling
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationautoscaling) = 1.66.0

%description   -n gem-aws-sdk-applicationautoscaling-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-applicationautoscaling-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-applicationautoscaling.


%package       -n gem-aws-sdk-applicationautoscaling-devel
Version:       1.66.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-applicationautoscaling
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationautoscaling) = 1.66.0

%description   -n gem-aws-sdk-applicationautoscaling-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-applicationautoscaling-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-applicationautoscaling.


%package       -n gem-aws-sdk-chimesdkmediapipelines
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Media Pipelines
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-chimesdkmediapipelines) = 1.3.0

%description   -n gem-aws-sdk-chimesdkmediapipelines
Official AWS Ruby gem for Amazon Chime SDK Media Pipelines. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-chimesdkmediapipelines-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Media Pipelines documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-chimesdkmediapipelines
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-chimesdkmediapipelines) = 1.3.0

%description   -n gem-aws-sdk-chimesdkmediapipelines-doc
AWS SDK for Ruby - Amazon Chime SDK Media Pipelines documentation
files.

Official AWS Ruby gem for Amazon Chime SDK Media Pipelines. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-chimesdkmediapipelines-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-chimesdkmediapipelines.


%package       -n gem-aws-sdk-chimesdkmediapipelines-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime SDK Media Pipelines development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-chimesdkmediapipelines
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-chimesdkmediapipelines) = 1.3.0

%description   -n gem-aws-sdk-chimesdkmediapipelines-devel
AWS SDK for Ruby - Amazon Chime SDK Media Pipelines development
package.

Official AWS Ruby gem for Amazon Chime SDK Media Pipelines. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-chimesdkmediapipelines-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-chimesdkmediapipelines.


%package       -n gem-aws-sdk-connectcampaignservice
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonConnectCampaignService
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-connectcampaignservice) = 1.3.0

%description   -n gem-aws-sdk-connectcampaignservice
Official AWS Ruby gem for AmazonConnectCampaignService. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-connectcampaignservice-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonConnectCampaignService documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-connectcampaignservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-connectcampaignservice) = 1.3.0

%description   -n gem-aws-sdk-connectcampaignservice-doc
AWS SDK for Ruby - AmazonConnectCampaignService documentation files.

%description   -n gem-aws-sdk-connectcampaignservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-connectcampaignservice.


%package       -n gem-aws-sdk-connectcampaignservice-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonConnectCampaignService development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-connectcampaignservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-connectcampaignservice) = 1.3.0

%description   -n gem-aws-sdk-connectcampaignservice-devel
AWS SDK for Ruby - AmazonConnectCampaignService development package.

%description   -n gem-aws-sdk-connectcampaignservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-connectcampaignservice.


%package       -n gem-aws-sdk-elasticloadbalancingv2
Version:       1.83.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-elasticloadbalancingv2) = 1.83.0

%description   -n gem-aws-sdk-elasticloadbalancingv2
Official AWS Ruby gem for Elastic Load Balancing (Elastic Load Balancing v2).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-elasticloadbalancingv2-doc
Version:       1.83.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-elasticloadbalancingv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticloadbalancingv2) = 1.83.0

%description   -n gem-aws-sdk-elasticloadbalancingv2-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Elastic Load Balancing (Elastic Load Balancing v2).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-elasticloadbalancingv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-elasticloadbalancingv2.


%package       -n gem-aws-sdk-elasticloadbalancingv2-devel
Version:       1.83.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-elasticloadbalancingv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticloadbalancingv2) = 1.83.0

%description   -n gem-aws-sdk-elasticloadbalancingv2-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Elastic Load Balancing (Elastic Load Balancing v2).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-elasticloadbalancingv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-elasticloadbalancingv2.


%package       -n gem-aws-sdk-mainframemodernization
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSMainframeModernization
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-mainframemodernization) = 1.4.0

%description   -n gem-aws-sdk-mainframemodernization
Official AWS Ruby gem for AWSMainframeModernization. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-mainframemodernization-doc
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSMainframeModernization documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mainframemodernization
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mainframemodernization) = 1.4.0

%description   -n gem-aws-sdk-mainframemodernization-doc
AWS SDK for Ruby - AWSMainframeModernization documentation files.

%description   -n gem-aws-sdk-mainframemodernization-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mainframemodernization.


%package       -n gem-aws-sdk-mainframemodernization-devel
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSMainframeModernization development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mainframemodernization
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mainframemodernization) = 1.4.0

%description   -n gem-aws-sdk-mainframemodernization-devel
AWS SDK for Ruby - AWSMainframeModernization development package.

%description   -n gem-aws-sdk-mainframemodernization-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mainframemodernization.


%package       -n gem-aws-sdk-redshiftdataapiservice
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-redshiftdataapiservice) = 1.24.0

%description   -n gem-aws-sdk-redshiftdataapiservice
Official AWS Ruby gem for Redshift Data API Service. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-redshiftdataapiservice-doc
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-redshiftdataapiservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-redshiftdataapiservice) = 1.24.0

%description   -n gem-aws-sdk-redshiftdataapiservice-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-redshiftdataapiservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-redshiftdataapiservice.


%package       -n gem-aws-sdk-redshiftdataapiservice-devel
Version:       1.24.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-redshiftdataapiservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-redshiftdataapiservice) = 1.24.0

%description   -n gem-aws-sdk-redshiftdataapiservice-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-redshiftdataapiservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-redshiftdataapiservice.


%package       -n gem-aws-sdk-route53recoverycluster
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - Route53 Recovery Cluster
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-route53recoverycluster) = 1.13.0

%description   -n gem-aws-sdk-route53recoverycluster
Official AWS Ruby gem for Route53 Recovery Cluster. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-route53recoverycluster-doc
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - Route53 Recovery Cluster documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-route53recoverycluster
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-route53recoverycluster) = 1.13.0

%description   -n gem-aws-sdk-route53recoverycluster-doc
AWS SDK for Ruby - Route53 Recovery Cluster documentation files.

%description   -n gem-aws-sdk-route53recoverycluster-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-route53recoverycluster.


%package       -n gem-aws-sdk-route53recoverycluster-devel
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - Route53 Recovery Cluster development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-route53recoverycluster
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-route53recoverycluster) = 1.13.0

%description   -n gem-aws-sdk-route53recoverycluster-devel
AWS SDK for Ruby - Route53 Recovery Cluster development package.

%description   -n gem-aws-sdk-route53recoverycluster-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-route53recoverycluster.


%package       -n gem-aws-sdk-apigatewaymanagementapi
Version:       1.32.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-apigatewaymanagementapi) = 1.32.0

%description   -n gem-aws-sdk-apigatewaymanagementapi
Official AWS Ruby gem for AmazonApiGatewayManagementApi. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-apigatewaymanagementapi-doc
Version:       1.32.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-apigatewaymanagementapi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-apigatewaymanagementapi) = 1.32.0

%description   -n gem-aws-sdk-apigatewaymanagementapi-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-apigatewaymanagementapi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-apigatewaymanagementapi.


%package       -n gem-aws-sdk-apigatewaymanagementapi-devel
Version:       1.32.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-apigatewaymanagementapi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-apigatewaymanagementapi) = 1.32.0

%description   -n gem-aws-sdk-apigatewaymanagementapi-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-apigatewaymanagementapi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-apigatewaymanagementapi.


%package       -n gem-aws-sdk-applicationcostprofiler
Version:       1.11.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-applicationcostprofiler) = 1.11.0

%description   -n gem-aws-sdk-applicationcostprofiler
Official AWS Ruby gem for AWS Application Cost Profiler. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-applicationcostprofiler-doc
Version:       1.11.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-applicationcostprofiler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationcostprofiler) = 1.11.0

%description   -n gem-aws-sdk-applicationcostprofiler-doc
The official AWS SDK for Ruby documentation files.

%description   -n gem-aws-sdk-applicationcostprofiler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-applicationcostprofiler.


%package       -n gem-aws-sdk-applicationcostprofiler-devel
Version:       1.11.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-applicationcostprofiler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationcostprofiler) = 1.11.0

%description   -n gem-aws-sdk-applicationcostprofiler-devel
The official AWS SDK for Ruby development package.

%description   -n gem-aws-sdk-applicationcostprofiler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-applicationcostprofiler.


%package       -n gem-aws-sdk-cognitoidentityprovider
Version:       1.73.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-cognitoidentityprovider) = 1.73.0

%description   -n gem-aws-sdk-cognitoidentityprovider
Official AWS Ruby gem for Amazon Cognito Identity Provider. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-cognitoidentityprovider-doc
Version:       1.73.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cognitoidentityprovider
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cognitoidentityprovider) = 1.73.0

%description   -n gem-aws-sdk-cognitoidentityprovider-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Cognito Identity Provider. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cognitoidentityprovider-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cognitoidentityprovider.


%package       -n gem-aws-sdk-cognitoidentityprovider-devel
Version:       1.73.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cognitoidentityprovider
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cognitoidentityprovider) = 1.73.0

%description   -n gem-aws-sdk-cognitoidentityprovider-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Cognito Identity Provider. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cognitoidentityprovider-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cognitoidentityprovider.


%package       -n gem-aws-sdk-iot1clickdevicesservice
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-iot1clickdevicesservice) = 1.39.0

%description   -n gem-aws-sdk-iot1clickdevicesservice
Official AWS Ruby gem for AWS IoT 1-Click Devices Service. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-iot1clickdevicesservice-doc
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iot1clickdevicesservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iot1clickdevicesservice) = 1.39.0

%description   -n gem-aws-sdk-iot1clickdevicesservice-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS IoT 1-Click Devices Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iot1clickdevicesservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iot1clickdevicesservice.


%package       -n gem-aws-sdk-iot1clickdevicesservice-devel
Version:       1.39.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iot1clickdevicesservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iot1clickdevicesservice) = 1.39.0

%description   -n gem-aws-sdk-iot1clickdevicesservice-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS IoT 1-Click Devices Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iot1clickdevicesservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iot1clickdevicesservice.


%package       -n gem-aws-sdk-lexmodelbuildingservice
Version:       1.59.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-lexmodelbuildingservice) = 1.59.0

%description   -n gem-aws-sdk-lexmodelbuildingservice
Official AWS Ruby gem for Amazon Lex Model Building Service. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-lexmodelbuildingservice-doc
Version:       1.59.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lexmodelbuildingservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lexmodelbuildingservice) = 1.59.0

%description   -n gem-aws-sdk-lexmodelbuildingservice-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Lex Model Building Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lexmodelbuildingservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lexmodelbuildingservice.


%package       -n gem-aws-sdk-lexmodelbuildingservice-devel
Version:       1.59.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lexmodelbuildingservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lexmodelbuildingservice) = 1.59.0

%description   -n gem-aws-sdk-lexmodelbuildingservice-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Lex Model Building Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lexmodelbuildingservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lexmodelbuildingservice.


%package       -n gem-aws-sdk-databasemigrationservice
Version:       1.75.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-databasemigrationservice) = 1.75.0

%description   -n gem-aws-sdk-databasemigrationservice
Official AWS Ruby gem for AWS Database Migration Service. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-databasemigrationservice-doc
Version:       1.75.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-databasemigrationservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-databasemigrationservice) = 1.75.0

%description   -n gem-aws-sdk-databasemigrationservice-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Database Migration Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-databasemigrationservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-databasemigrationservice.


%package       -n gem-aws-sdk-databasemigrationservice-devel
Version:       1.75.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-databasemigrationservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-databasemigrationservice) = 1.75.0

%description   -n gem-aws-sdk-databasemigrationservice-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Database Migration Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-databasemigrationservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-databasemigrationservice.


%package       -n gem-aws-sdk-migrationhuborchestrator
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Migration Hub Orchestrator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-migrationhuborchestrator) = 1.2.0

%description   -n gem-aws-sdk-migrationhuborchestrator
Official AWS Ruby gem for AWS Migration Hub Orchestrator. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-migrationhuborchestrator-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Migration Hub Orchestrator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-migrationhuborchestrator
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-migrationhuborchestrator) = 1.2.0

%description   -n gem-aws-sdk-migrationhuborchestrator-doc
AWS SDK for Ruby - AWS Migration Hub Orchestrator documentation files.

Official AWS Ruby gem for AWS Migration Hub Orchestrator. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-migrationhuborchestrator-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-migrationhuborchestrator.


%package       -n gem-aws-sdk-migrationhuborchestrator-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Migration Hub Orchestrator development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-migrationhuborchestrator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-migrationhuborchestrator) = 1.2.0

%description   -n gem-aws-sdk-migrationhuborchestrator-devel
AWS SDK for Ruby - AWS Migration Hub Orchestrator development package.

Official AWS Ruby gem for AWS Migration Hub Orchestrator. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-migrationhuborchestrator-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-migrationhuborchestrator.


%package       -n gem-aws-sdk-resourcegroupstaggingapi
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-resourcegroupstaggingapi) = 1.49.0

%description   -n gem-aws-sdk-resourcegroupstaggingapi
Official AWS Ruby gem for AWS Resource Groups Tagging API. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-resourcegroupstaggingapi-doc
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-resourcegroupstaggingapi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-resourcegroupstaggingapi) = 1.49.0

%description   -n gem-aws-sdk-resourcegroupstaggingapi-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Resource Groups Tagging API. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-resourcegroupstaggingapi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-resourcegroupstaggingapi.


%package       -n gem-aws-sdk-resourcegroupstaggingapi-devel
Version:       1.49.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-resourcegroupstaggingapi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-resourcegroupstaggingapi) = 1.49.0

%description   -n gem-aws-sdk-resourcegroupstaggingapi-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Resource Groups Tagging API. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-resourcegroupstaggingapi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-resourcegroupstaggingapi.


%package       -n gem-aws-sdk-route53recoveryreadiness
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Route53 Recovery Readiness
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-route53recoveryreadiness) = 1.12.0

%description   -n gem-aws-sdk-route53recoveryreadiness
Official AWS Ruby gem for AWS Route53 Recovery Readiness. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-route53recoveryreadiness-doc
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Route53 Recovery Readiness documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-route53recoveryreadiness
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-route53recoveryreadiness) = 1.12.0

%description   -n gem-aws-sdk-route53recoveryreadiness-doc
AWS SDK for Ruby - AWS Route53 Recovery Readiness documentation files.

Official AWS Ruby gem for AWS Route53 Recovery Readiness. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-route53recoveryreadiness-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-route53recoveryreadiness.


%package       -n gem-aws-sdk-route53recoveryreadiness-devel
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Route53 Recovery Readiness development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-route53recoveryreadiness
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-route53recoveryreadiness) = 1.12.0

%description   -n gem-aws-sdk-route53recoveryreadiness-devel
AWS SDK for Ruby - AWS Route53 Recovery Readiness development package.

Official AWS Ruby gem for AWS Route53 Recovery Readiness. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-route53recoveryreadiness-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-route53recoveryreadiness.


%package       -n gem-aws-sdk-costandusagereportservice
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-costandusagereportservice) = 1.43.0

%description   -n gem-aws-sdk-costandusagereportservice
Official AWS Ruby gem for AWS Cost and Usage Report Service. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-costandusagereportservice-doc
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-costandusagereportservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-costandusagereportservice) = 1.43.0

%description   -n gem-aws-sdk-costandusagereportservice-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Cost and Usage Report Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-costandusagereportservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-costandusagereportservice.


%package       -n gem-aws-sdk-costandusagereportservice-devel
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-costandusagereportservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-costandusagereportservice) = 1.43.0

%description   -n gem-aws-sdk-costandusagereportservice-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Cost and Usage Report Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-costandusagereportservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-costandusagereportservice.


%package       -n gem-aws-sdk-kinesisvideoarchivedmedia
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-kinesisvideoarchivedmedia) = 1.46.0

%description   -n gem-aws-sdk-kinesisvideoarchivedmedia
Official AWS Ruby gem for Amazon Kinesis Video Streams Archived Media (Kinesis
Video Archived Media). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kinesisvideoarchivedmedia-doc
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesisvideoarchivedmedia
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideoarchivedmedia) = 1.46.0

%description   -n gem-aws-sdk-kinesisvideoarchivedmedia-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Kinesis Video Streams Archived Media (Kinesis
Video Archived Media). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideoarchivedmedia-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesisvideoarchivedmedia.


%package       -n gem-aws-sdk-kinesisvideoarchivedmedia-devel
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesisvideoarchivedmedia
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideoarchivedmedia) = 1.46.0

%description   -n gem-aws-sdk-kinesisvideoarchivedmedia-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Kinesis Video Streams Archived Media (Kinesis
Video Archived Media). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideoarchivedmedia-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesisvideoarchivedmedia.


%package       -n gem-aws-sdk-kinesisvideowebrtcstorage
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Kinesis Video WebRTC Storage
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-kinesisvideowebrtcstorage) = 1.2.0

%description   -n gem-aws-sdk-kinesisvideowebrtcstorage
Official AWS Ruby gem for Amazon Kinesis Video WebRTC Storage. This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kinesisvideowebrtcstorage-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Kinesis Video WebRTC Storage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesisvideowebrtcstorage
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideowebrtcstorage) = 1.2.0

%description   -n gem-aws-sdk-kinesisvideowebrtcstorage-doc
AWS SDK for Ruby - Amazon Kinesis Video WebRTC Storage documentation
files.

Official AWS Ruby gem for Amazon Kinesis Video WebRTC Storage. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideowebrtcstorage-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesisvideowebrtcstorage.


%package       -n gem-aws-sdk-kinesisvideowebrtcstorage-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Kinesis Video WebRTC Storage development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesisvideowebrtcstorage
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideowebrtcstorage) = 1.2.0

%description   -n gem-aws-sdk-kinesisvideowebrtcstorage-devel
AWS SDK for Ruby - Amazon Kinesis Video WebRTC Storage development
package.

Official AWS Ruby gem for Amazon Kinesis Video WebRTC Storage. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideowebrtcstorage-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesisvideowebrtcstorage.


%package       -n gem-aws-sdk-migrationhubrefactorspaces
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Migration Hub Refactor Spaces
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-migrationhubrefactorspaces) = 1.10.0

%description   -n gem-aws-sdk-migrationhubrefactorspaces
Official AWS Ruby gem for AWS Migration Hub Refactor Spaces. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-migrationhubrefactorspaces-doc
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Migration Hub Refactor Spaces documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-migrationhubrefactorspaces
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-migrationhubrefactorspaces) = 1.10.0

%description   -n gem-aws-sdk-migrationhubrefactorspaces-doc
AWS SDK for Ruby - AWS Migration Hub Refactor Spaces documentation
files.

Official AWS Ruby gem for AWS Migration Hub Refactor Spaces. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-migrationhubrefactorspaces-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-migrationhubrefactorspaces.


%package       -n gem-aws-sdk-migrationhubrefactorspaces-devel
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Migration Hub Refactor Spaces development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-migrationhubrefactorspaces
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-migrationhubrefactorspaces) = 1.10.0

%description   -n gem-aws-sdk-migrationhubrefactorspaces-devel
AWS SDK for Ruby - AWS Migration Hub Refactor Spaces development
package.

Official AWS Ruby gem for AWS Migration Hub Refactor Spaces. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-migrationhubrefactorspaces-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-migrationhubrefactorspaces.


%package       -n gem-aws-sdk-transcribestreamingservice
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-transcribestreamingservice) = 1.46.0

%description   -n gem-aws-sdk-transcribestreamingservice
Official AWS Ruby gem for Amazon Transcribe Streaming Service. This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-transcribestreamingservice-doc
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-transcribestreamingservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-transcribestreamingservice) = 1.46.0

%description   -n gem-aws-sdk-transcribestreamingservice-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Transcribe Streaming Service. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-transcribestreamingservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-transcribestreamingservice.


%package       -n gem-aws-sdk-transcribestreamingservice-devel
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-transcribestreamingservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-transcribestreamingservice) = 1.46.0

%description   -n gem-aws-sdk-transcribestreamingservice-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Transcribe Streaming Service. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-transcribestreamingservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-transcribestreamingservice.


%package       -n gem-aws-sdk-applicationdiscoveryservice
Version:       1.48.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-applicationdiscoveryservice) = 1.48.0

%description   -n gem-aws-sdk-applicationdiscoveryservice
Official AWS Ruby gem for AWS Application Discovery Service. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-applicationdiscoveryservice-doc
Version:       1.48.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-applicationdiscoveryservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationdiscoveryservice) = 1.48.0

%description   -n gem-aws-sdk-applicationdiscoveryservice-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Application Discovery Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-applicationdiscoveryservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-applicationdiscoveryservice.


%package       -n gem-aws-sdk-applicationdiscoveryservice-devel
Version:       1.48.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-applicationdiscoveryservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationdiscoveryservice) = 1.48.0

%description   -n gem-aws-sdk-applicationdiscoveryservice-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Application Discovery Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-applicationdiscoveryservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-applicationdiscoveryservice.


%package       -n gem-aws-sdk-marketplacecommerceanalytics
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-marketplacecommerceanalytics) = 1.43.0

%description   -n gem-aws-sdk-marketplacecommerceanalytics
Official AWS Ruby gem for AWS Marketplace Commerce Analytics. This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-marketplacecommerceanalytics-doc
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-marketplacecommerceanalytics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplacecommerceanalytics) = 1.43.0

%description   -n gem-aws-sdk-marketplacecommerceanalytics-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Marketplace Commerce Analytics. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-marketplacecommerceanalytics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-marketplacecommerceanalytics.


%package       -n gem-aws-sdk-marketplacecommerceanalytics-devel
Version:       1.43.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-marketplacecommerceanalytics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplacecommerceanalytics) = 1.43.0

%description   -n gem-aws-sdk-marketplacecommerceanalytics-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Marketplace Commerce Analytics. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-marketplacecommerceanalytics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-marketplacecommerceanalytics.


%package       -n gem-aws-sdk-route53recoverycontrolconfig
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Route53 Recovery Control Config
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-route53recoverycontrolconfig) = 1.13.0

%description   -n gem-aws-sdk-route53recoverycontrolconfig
Official AWS Ruby gem for AWS Route53 Recovery Control Config. This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-route53recoverycontrolconfig-doc
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Route53 Recovery Control Config documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-route53recoverycontrolconfig
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-route53recoverycontrolconfig) = 1.13.0

%description   -n gem-aws-sdk-route53recoverycontrolconfig-doc
AWS SDK for Ruby - AWS Route53 Recovery Control Config documentation
files.

Official AWS Ruby gem for AWS Route53 Recovery Control Config. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-route53recoverycontrolconfig-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-route53recoverycontrolconfig.


%package       -n gem-aws-sdk-route53recoverycontrolconfig-devel
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Route53 Recovery Control Config development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-route53recoverycontrolconfig
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-route53recoverycontrolconfig) = 1.13.0

%description   -n gem-aws-sdk-route53recoverycontrolconfig-devel
AWS SDK for Ruby - AWS Route53 Recovery Control Config development
package.

Official AWS Ruby gem for AWS Route53 Recovery Control Config. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-route53recoverycontrolconfig-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-route53recoverycontrolconfig.


%package       -n gem-aws-sdk-sagemakerfeaturestoreruntime
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-sagemakerfeaturestoreruntime) = 1.15.0

%description   -n gem-aws-sdk-sagemakerfeaturestoreruntime
Official AWS Ruby gem for Amazon SageMaker Feature Store Runtime. This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-sagemakerfeaturestoreruntime-doc
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sagemakerfeaturestoreruntime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakerfeaturestoreruntime) = 1.15.0

%description   -n gem-aws-sdk-sagemakerfeaturestoreruntime-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon SageMaker Feature Store Runtime. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sagemakerfeaturestoreruntime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sagemakerfeaturestoreruntime.


%package       -n gem-aws-sdk-sagemakerfeaturestoreruntime-devel
Version:       1.15.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sagemakerfeaturestoreruntime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakerfeaturestoreruntime) = 1.15.0

%description   -n gem-aws-sdk-sagemakerfeaturestoreruntime-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon SageMaker Feature Store Runtime. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sagemakerfeaturestoreruntime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sagemakerfeaturestoreruntime.


%package       -n gem-aws-sdk-kinesisvideosignalingchannels
Version:       1.21.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-kinesisvideosignalingchannels) = 1.21.0

%description   -n gem-aws-sdk-kinesisvideosignalingchannels
Official AWS Ruby gem for Amazon Kinesis Video Signaling Channels. This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kinesisvideosignalingchannels-doc
Version:       1.21.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesisvideosignalingchannels
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideosignalingchannels) = 1.21.0

%description   -n gem-aws-sdk-kinesisvideosignalingchannels-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for Amazon Kinesis Video Signaling Channels. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideosignalingchannels-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesisvideosignalingchannels.


%package       -n gem-aws-sdk-kinesisvideosignalingchannels-devel
Version:       1.21.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesisvideosignalingchannels
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideosignalingchannels) = 1.21.0

%description   -n gem-aws-sdk-kinesisvideosignalingchannels-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for Amazon Kinesis Video Signaling Channels. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideosignalingchannels-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesisvideosignalingchannels.


%package       -n gem-aws-sdk-marketplaceentitlementservice
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-marketplaceentitlementservice) = 1.37.0

%description   -n gem-aws-sdk-marketplaceentitlementservice
Official AWS Ruby gem for AWS Marketplace Entitlement Service. This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-marketplaceentitlementservice-doc
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-marketplaceentitlementservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplaceentitlementservice) = 1.37.0

%description   -n gem-aws-sdk-marketplaceentitlementservice-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWS Marketplace Entitlement Service. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-marketplaceentitlementservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-marketplaceentitlementservice.


%package       -n gem-aws-sdk-marketplaceentitlementservice-devel
Version:       1.37.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-marketplaceentitlementservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplaceentitlementservice) = 1.37.0

%description   -n gem-aws-sdk-marketplaceentitlementservice-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWS Marketplace Entitlement Service. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-marketplaceentitlementservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-marketplaceentitlementservice.


%package       -n gem-aws-sdk-licensemanagerusersubscriptions
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS License Manager User Subscriptions
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-licensemanagerusersubscriptions) = 1.3.0

%description   -n gem-aws-sdk-licensemanagerusersubscriptions
Official AWS Ruby gem for AWS License Manager User Subscriptions. This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-licensemanagerusersubscriptions-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS License Manager User Subscriptions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-licensemanagerusersubscriptions
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-licensemanagerusersubscriptions) = 1.3.0

%description   -n gem-aws-sdk-licensemanagerusersubscriptions-doc
AWS SDK for Ruby - AWS License Manager User Subscriptions documentation
files.

Official AWS Ruby gem for AWS License Manager User Subscriptions. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-licensemanagerusersubscriptions-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-licensemanagerusersubscriptions.


%package       -n gem-aws-sdk-licensemanagerusersubscriptions-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS License Manager User Subscriptions development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-licensemanagerusersubscriptions
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-licensemanagerusersubscriptions) = 1.3.0

%description   -n gem-aws-sdk-licensemanagerusersubscriptions-devel
AWS SDK for Ruby - AWS License Manager User Subscriptions development
package.

Official AWS Ruby gem for AWS License Manager User Subscriptions. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-licensemanagerusersubscriptions-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-licensemanagerusersubscriptions.


%package       -n gem-aws-sdk-serverlessapplicationrepository
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-serverlessapplicationrepository) = 1.46.0

%description   -n gem-aws-sdk-serverlessapplicationrepository
Official AWS Ruby gem for AWSServerlessApplicationRepository. This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-serverlessapplicationrepository-doc
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-serverlessapplicationrepository
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-serverlessapplicationrepository) = 1.46.0

%description   -n gem-aws-sdk-serverlessapplicationrepository-doc
The official AWS SDK for Ruby documentation files.

Official AWS Ruby gem for AWSServerlessApplicationRepository. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-serverlessapplicationrepository-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-serverlessapplicationrepository.


%package       -n gem-aws-sdk-serverlessapplicationrepository-devel
Version:       1.46.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-serverlessapplicationrepository
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-serverlessapplicationrepository) = 1.46.0

%description   -n gem-aws-sdk-serverlessapplicationrepository-devel
The official AWS SDK for Ruby development package.

Official AWS Ruby gem for AWSServerlessApplicationRepository. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-serverlessapplicationrepository-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-serverlessapplicationrepository.


%package       -n gem-aws-sdk-licensemanagerlinuxsubscriptions
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS License Manager Linux Subscriptions
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-licensemanagerlinuxsubscriptions) = 1.1.0

%description   -n gem-aws-sdk-licensemanagerlinuxsubscriptions
Official AWS Ruby gem for AWS License Manager Linux Subscriptions. This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-licensemanagerlinuxsubscriptions-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS License Manager Linux Subscriptions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-licensemanagerlinuxsubscriptions
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-licensemanagerlinuxsubscriptions) = 1.1.0

%description   -n gem-aws-sdk-licensemanagerlinuxsubscriptions-doc
AWS SDK for Ruby - AWS License Manager Linux Subscriptions documentation
files.

Official AWS Ruby gem for AWS License Manager Linux Subscriptions. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-licensemanagerlinuxsubscriptions-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-licensemanagerlinuxsubscriptions.


%package       -n gem-aws-sdk-licensemanagerlinuxsubscriptions-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS License Manager Linux Subscriptions development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-licensemanagerlinuxsubscriptions
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-licensemanagerlinuxsubscriptions) = 1.1.0

%description   -n gem-aws-sdk-licensemanagerlinuxsubscriptions-devel
AWS SDK for Ruby - AWS License Manager Linux Subscriptions development
package.

Official AWS Ruby gem for AWS License Manager Linux Subscriptions. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-licensemanagerlinuxsubscriptions-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-licensemanagerlinuxsubscriptions.


%package       -n gem-aws-sdk-migrationhubstrategyrecommendations
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - Migration Hub Strategy Recommendations
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.165.0
Requires:      gem(aws-sigv4) >= 1.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Provides:      gem(aws-sdk-migrationhubstrategyrecommendations) = 1.7.0

%description   -n gem-aws-sdk-migrationhubstrategyrecommendations
Official AWS Ruby gem for Migration Hub Strategy Recommendations. This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-migrationhubstrategyrecommendations-doc
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - Migration Hub Strategy Recommendations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-migrationhubstrategyrecommendations
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-migrationhubstrategyrecommendations) = 1.7.0

%description   -n gem-aws-sdk-migrationhubstrategyrecommendations-doc
AWS SDK for Ruby - Migration Hub Strategy Recommendations documentation
files.

Official AWS Ruby gem for Migration Hub Strategy Recommendations. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-migrationhubstrategyrecommendations-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-migrationhubstrategyrecommendations.


%package       -n gem-aws-sdk-migrationhubstrategyrecommendations-devel
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - Migration Hub Strategy Recommendations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-migrationhubstrategyrecommendations
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-migrationhubstrategyrecommendations) = 1.7.0

%description   -n gem-aws-sdk-migrationhubstrategyrecommendations-devel
AWS SDK for Ruby - Migration Hub Strategy Recommendations development
package.

Official AWS Ruby gem for Migration Hub Strategy Recommendations. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-migrationhubstrategyrecommendations-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-migrationhubstrategyrecommendations.


%package       -n gem-aws-sdk-doc
Version:       3.1.0
Release:       alt1
Summary:       The official AWS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk) = 3.1.0

%description   -n gem-aws-sdk-doc
The official AWS SDK for Ruby documentation files.

The official AWS SDK for Ruby. Provides both resource oriented interfaces and
API clients for AWS services.

%description   -n gem-aws-sdk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk.


%package       -n gem-aws-sdk-devel
Version:       3.1.0
Release:       alt1
Summary:       The official AWS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk) = 3.1.0

%description   -n gem-aws-sdk-devel
The official AWS SDK for Ruby development package.

The official AWS SDK for Ruby. Provides both resource oriented interfaces and
API clients for AWS services.

%description   -n gem-aws-sdk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-aws-sigv2
%ruby_gemspecdir/aws-sigv2-1.1.0.gemspec
%ruby_gemslibdir/aws-sigv2-1.1.0

%files         -n gem-aws-sigv2-doc
%ruby_gemsdocdir/aws-sigv2-1.1.0

%files         -n gem-aws-sigv2-devel

%files         -n gem-aws-sigv4
%ruby_gemspecdir/aws-sigv4-1.5.2.gemspec
%ruby_gemslibdir/aws-sigv4-1.5.2

%files         -n gem-aws-sigv4-doc
%ruby_gemsdocdir/aws-sigv4-1.5.2

%files         -n gem-aws-sigv4-devel

%files         -n gem-aws-sdk-mq
%ruby_gemspecdir/aws-sdk-mq-1.49.0.gemspec
%ruby_gemslibdir/aws-sdk-mq-1.49.0

%files         -n gem-aws-sdk-mq-doc
%ruby_gemsdocdir/aws-sdk-mq-1.49.0

%files         -n gem-aws-sdk-mq-devel

%files         -n gem-aws-sdk-pi
%ruby_gemspecdir/aws-sdk-pi-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-pi-1.42.0

%files         -n gem-aws-sdk-pi-doc
%ruby_gemsdocdir/aws-sdk-pi-1.42.0

%files         -n gem-aws-sdk-pi-devel

%files         -n gem-aws-sdk-s3
%ruby_gemspecdir/aws-sdk-s3-1.119.0.gemspec
%ruby_gemslibdir/aws-sdk-s3-1.119.0

%files         -n gem-aws-sdk-s3-doc
%ruby_gemsdocdir/aws-sdk-s3-1.119.0

%files         -n gem-aws-sdk-s3-devel

%files         -n gem-aws-sdk-acm
%ruby_gemspecdir/aws-sdk-acm-1.55.0.gemspec
%ruby_gemslibdir/aws-sdk-acm-1.55.0

%files         -n gem-aws-sdk-acm-doc
%ruby_gemsdocdir/aws-sdk-acm-1.55.0

%files         -n gem-aws-sdk-acm-devel

%files         -n gem-aws-sdk-dax
%ruby_gemspecdir/aws-sdk-dax-1.41.0.gemspec
%ruby_gemslibdir/aws-sdk-dax-1.41.0

%files         -n gem-aws-sdk-dax-doc
%ruby_gemsdocdir/aws-sdk-dax-1.41.0

%files         -n gem-aws-sdk-dax-devel

%files         -n gem-aws-sdk-dlm
%ruby_gemspecdir/aws-sdk-dlm-1.54.0.gemspec
%ruby_gemslibdir/aws-sdk-dlm-1.54.0

%files         -n gem-aws-sdk-dlm-doc
%ruby_gemsdocdir/aws-sdk-dlm-1.54.0

%files         -n gem-aws-sdk-dlm-devel

%files         -n gem-aws-sdk-drs
%ruby_gemspecdir/aws-sdk-drs-1.10.0.gemspec
%ruby_gemslibdir/aws-sdk-drs-1.10.0

%files         -n gem-aws-sdk-drs-doc
%ruby_gemsdocdir/aws-sdk-drs-1.10.0

%files         -n gem-aws-sdk-drs-devel

%files         -n gem-aws-sdk-ebs
%ruby_gemspecdir/aws-sdk-ebs-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-ebs-1.28.0

%files         -n gem-aws-sdk-ebs-doc
%ruby_gemsdocdir/aws-sdk-ebs-1.28.0

%files         -n gem-aws-sdk-ebs-devel

%files         -n gem-aws-sdk-ec2
%ruby_gemspecdir/aws-sdk-ec2-1.361.0.gemspec
%ruby_gemslibdir/aws-sdk-ec2-1.361.0

%files         -n gem-aws-sdk-ec2-doc
%ruby_gemsdocdir/aws-sdk-ec2-1.361.0

%files         -n gem-aws-sdk-ec2-devel

%files         -n gem-aws-sdk-ecr
%ruby_gemspecdir/aws-sdk-ecr-1.58.0.gemspec
%ruby_gemslibdir/aws-sdk-ecr-1.58.0

%files         -n gem-aws-sdk-ecr-doc
%ruby_gemsdocdir/aws-sdk-ecr-1.58.0

%files         -n gem-aws-sdk-ecr-devel

%files         -n gem-aws-sdk-ecs
%ruby_gemspecdir/aws-sdk-ecs-1.110.0.gemspec
%ruby_gemslibdir/aws-sdk-ecs-1.110.0

%files         -n gem-aws-sdk-ecs-doc
%ruby_gemsdocdir/aws-sdk-ecs-1.110.0

%files         -n gem-aws-sdk-ecs-devel

%files         -n gem-aws-sdk-efs
%ruby_gemspecdir/aws-sdk-efs-1.58.0.gemspec
%ruby_gemslibdir/aws-sdk-efs-1.58.0

%files         -n gem-aws-sdk-efs-doc
%ruby_gemsdocdir/aws-sdk-efs-1.58.0

%files         -n gem-aws-sdk-efs-devel

%files         -n gem-aws-sdk-eks
%ruby_gemspecdir/aws-sdk-eks-1.83.0.gemspec
%ruby_gemslibdir/aws-sdk-eks-1.83.0

%files         -n gem-aws-sdk-eks-doc
%ruby_gemsdocdir/aws-sdk-eks-1.83.0

%files         -n gem-aws-sdk-eks-devel

%files         -n gem-aws-sdk-emr
%ruby_gemspecdir/aws-sdk-emr-1.65.0.gemspec
%ruby_gemslibdir/aws-sdk-emr-1.65.0

%files         -n gem-aws-sdk-emr-doc
%ruby_gemsdocdir/aws-sdk-emr-1.65.0

%files         -n gem-aws-sdk-emr-devel

%files         -n gem-aws-sdk-fis
%ruby_gemspecdir/aws-sdk-fis-1.16.0.gemspec
%ruby_gemslibdir/aws-sdk-fis-1.16.0

%files         -n gem-aws-sdk-fis-doc
%ruby_gemsdocdir/aws-sdk-fis-1.16.0

%files         -n gem-aws-sdk-fis-devel

%files         -n gem-aws-sdk-fms
%ruby_gemspecdir/aws-sdk-fms-1.55.0.gemspec
%ruby_gemslibdir/aws-sdk-fms-1.55.0

%files         -n gem-aws-sdk-fms-doc
%ruby_gemsdocdir/aws-sdk-fms-1.55.0

%files         -n gem-aws-sdk-fms-devel

%files         -n gem-aws-sdk-fsx
%ruby_gemspecdir/aws-sdk-fsx-1.64.0.gemspec
%ruby_gemslibdir/aws-sdk-fsx-1.64.0

%files         -n gem-aws-sdk-fsx-doc
%ruby_gemsdocdir/aws-sdk-fsx-1.64.0

%files         -n gem-aws-sdk-fsx-devel

%files         -n gem-aws-sdk-iam
%ruby_gemspecdir/aws-sdk-iam-1.74.0.gemspec
%ruby_gemslibdir/aws-sdk-iam-1.74.0

%files         -n gem-aws-sdk-iam-doc
%ruby_gemsdocdir/aws-sdk-iam-1.74.0

%files         -n gem-aws-sdk-iam-devel

%files         -n gem-aws-sdk-iot
%ruby_gemspecdir/aws-sdk-iot-1.99.0.gemspec
%ruby_gemslibdir/aws-sdk-iot-1.99.0

%files         -n gem-aws-sdk-iot-doc
%ruby_gemsdocdir/aws-sdk-iot-1.99.0

%files         -n gem-aws-sdk-iot-devel

%files         -n gem-aws-sdk-ivs
%ruby_gemspecdir/aws-sdk-ivs-1.26.0.gemspec
%ruby_gemslibdir/aws-sdk-ivs-1.26.0

%files         -n gem-aws-sdk-ivs-doc
%ruby_gemsdocdir/aws-sdk-ivs-1.26.0

%files         -n gem-aws-sdk-ivs-devel

%files         -n gem-aws-sdk-kms
%ruby_gemspecdir/aws-sdk-kms-1.62.0.gemspec
%ruby_gemslibdir/aws-sdk-kms-1.62.0

%files         -n gem-aws-sdk-kms-doc
%ruby_gemsdocdir/aws-sdk-kms-1.62.0

%files         -n gem-aws-sdk-kms-devel

%files         -n gem-aws-sdk-lex
%ruby_gemspecdir/aws-sdk-lex-1.47.0.gemspec
%ruby_gemslibdir/aws-sdk-lex-1.47.0

%files         -n gem-aws-sdk-lex-doc
%ruby_gemsdocdir/aws-sdk-lex-1.47.0

%files         -n gem-aws-sdk-lex-devel

%files         -n gem-aws-sdk-mgn
%ruby_gemspecdir/aws-sdk-mgn-1.17.0.gemspec
%ruby_gemslibdir/aws-sdk-mgn-1.17.0

%files         -n gem-aws-sdk-mgn-doc
%ruby_gemsdocdir/aws-sdk-mgn-1.17.0

%files         -n gem-aws-sdk-mgn-devel

%files         -n gem-aws-sdk-oam
%ruby_gemspecdir/aws-sdk-oam-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-oam-1.1.0

%files         -n gem-aws-sdk-oam-doc
%ruby_gemsdocdir/aws-sdk-oam-1.1.0

%files         -n gem-aws-sdk-oam-devel

%files         -n gem-aws-sdk-ram
%ruby_gemspecdir/aws-sdk-ram-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-ram-1.42.0

%files         -n gem-aws-sdk-ram-doc
%ruby_gemsdocdir/aws-sdk-ram-1.42.0

%files         -n gem-aws-sdk-ram-devel

%files         -n gem-aws-sdk-rds
%ruby_gemspecdir/aws-sdk-rds-1.171.0.gemspec
%ruby_gemslibdir/aws-sdk-rds-1.171.0

%files         -n gem-aws-sdk-rds-doc
%ruby_gemsdocdir/aws-sdk-rds-1.171.0

%files         -n gem-aws-sdk-rds-devel

%files         -n gem-aws-sdk-ses
%ruby_gemspecdir/aws-sdk-ses-1.49.0.gemspec
%ruby_gemslibdir/aws-sdk-ses-1.49.0

%files         -n gem-aws-sdk-ses-doc
%ruby_gemsdocdir/aws-sdk-ses-1.49.0

%files         -n gem-aws-sdk-ses-devel

%files         -n gem-aws-sdk-sms
%ruby_gemspecdir/aws-sdk-sms-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-sms-1.42.0

%files         -n gem-aws-sdk-sms-doc
%ruby_gemsdocdir/aws-sdk-sms-1.42.0

%files         -n gem-aws-sdk-sms-devel

%files         -n gem-aws-sdk-sns
%ruby_gemspecdir/aws-sdk-sns-1.58.0.gemspec
%ruby_gemslibdir/aws-sdk-sns-1.58.0

%files         -n gem-aws-sdk-sns-doc
%ruby_gemsdocdir/aws-sdk-sns-1.58.0

%files         -n gem-aws-sdk-sns-devel

%files         -n gem-aws-sdk-sqs
%ruby_gemspecdir/aws-sdk-sqs-1.53.0.gemspec
%ruby_gemslibdir/aws-sdk-sqs-1.53.0

%files         -n gem-aws-sdk-sqs-doc
%ruby_gemsdocdir/aws-sdk-sqs-1.53.0

%files         -n gem-aws-sdk-sqs-devel

%files         -n gem-aws-sdk-ssm
%ruby_gemspecdir/aws-sdk-ssm-1.148.0.gemspec
%ruby_gemslibdir/aws-sdk-ssm-1.148.0

%files         -n gem-aws-sdk-ssm-doc
%ruby_gemsdocdir/aws-sdk-ssm-1.148.0

%files         -n gem-aws-sdk-ssm-devel

%files         -n gem-aws-sdk-sso
%ruby_gemspecdir/aws-sdk-sso-1.11.0.gemspec
%ruby_gemslibdir/aws-sdk-sso-1.11.0

%files         -n gem-aws-sdk-sso-doc
%ruby_gemsdocdir/aws-sdk-sso-1.11.0

%files         -n gem-aws-sdk-sso-devel

%files         -n gem-aws-sdk-sts
%ruby_gemspecdir/aws-sdk-sts-1.9.0.gemspec
%ruby_gemslibdir/aws-sdk-sts-1.9.0

%files         -n gem-aws-sdk-sts-doc
%ruby_gemsdocdir/aws-sdk-sts-1.9.0

%files         -n gem-aws-sdk-sts-devel

%files         -n gem-aws-sdk-swf
%ruby_gemspecdir/aws-sdk-swf-1.38.0.gemspec
%ruby_gemslibdir/aws-sdk-swf-1.38.0

%files         -n gem-aws-sdk-swf-doc
%ruby_gemsdocdir/aws-sdk-swf-1.38.0

%files         -n gem-aws-sdk-swf-devel

%files         -n gem-aws-sdk-waf
%ruby_gemspecdir/aws-sdk-waf-1.49.0.gemspec
%ruby_gemslibdir/aws-sdk-waf-1.49.0

%files         -n gem-aws-sdk-waf-doc
%ruby_gemsdocdir/aws-sdk-waf-1.49.0

%files         -n gem-aws-sdk-waf-devel

%files         -n gem-aws-sdk-core
%ruby_gemspecdir/aws-sdk-core-3.170.0.gemspec
%ruby_gemslibdir/aws-sdk-core-3.170.0

%files         -n gem-aws-sdk-core-doc
%ruby_gemsdocdir/aws-sdk-core-3.170.0

%files         -n gem-aws-sdk-core-devel

%files         -n gem-aws-sdk-glue
%ruby_gemspecdir/aws-sdk-glue-1.129.0.gemspec
%ruby_gemslibdir/aws-sdk-glue-1.129.0

%files         -n gem-aws-sdk-glue-doc
%ruby_gemsdocdir/aws-sdk-glue-1.129.0

%files         -n gem-aws-sdk-glue-devel

%files         -n gem-aws-sdk-mwaa
%ruby_gemspecdir/aws-sdk-mwaa-1.19.0.gemspec
%ruby_gemslibdir/aws-sdk-mwaa-1.19.0

%files         -n gem-aws-sdk-mwaa-doc
%ruby_gemsdocdir/aws-sdk-mwaa-1.19.0

%files         -n gem-aws-sdk-mwaa-devel

%files         -n gem-aws-sdk-qldb
%ruby_gemspecdir/aws-sdk-qldb-1.27.0.gemspec
%ruby_gemslibdir/aws-sdk-qldb-1.27.0

%files         -n gem-aws-sdk-qldb-doc
%ruby_gemsdocdir/aws-sdk-qldb-1.27.0

%files         -n gem-aws-sdk-qldb-devel

%files         -n gem-aws-sdk-xray
%ruby_gemspecdir/aws-sdk-xray-1.51.0.gemspec
%ruby_gemslibdir/aws-sdk-xray-1.51.0

%files         -n gem-aws-sdk-xray-doc
%ruby_gemsdocdir/aws-sdk-xray-1.51.0

%files         -n gem-aws-sdk-xray-devel

%files         -n gem-aws-sdk-batch
%ruby_gemspecdir/aws-sdk-batch-1.67.0.gemspec
%ruby_gemslibdir/aws-sdk-batch-1.67.0

%files         -n gem-aws-sdk-batch-doc
%ruby_gemsdocdir/aws-sdk-batch-1.67.0

%files         -n gem-aws-sdk-batch-devel

%files         -n gem-aws-sdk-chime
%ruby_gemspecdir/aws-sdk-chime-1.70.0.gemspec
%ruby_gemslibdir/aws-sdk-chime-1.70.0

%files         -n gem-aws-sdk-chime-doc
%ruby_gemsdocdir/aws-sdk-chime-1.70.0

%files         -n gem-aws-sdk-chime-devel

%files         -n gem-aws-sdk-docdb
%ruby_gemspecdir/aws-sdk-docdb-1.46.0.gemspec
%ruby_gemslibdir/aws-sdk-docdb-1.46.0

%files         -n gem-aws-sdk-docdb-doc
%ruby_gemsdocdir/aws-sdk-docdb-1.46.0

%files         -n gem-aws-sdk-docdb-devel

%files         -n gem-aws-sdk-kafka
%ruby_gemspecdir/aws-sdk-kafka-1.53.0.gemspec
%ruby_gemslibdir/aws-sdk-kafka-1.53.0

%files         -n gem-aws-sdk-kafka-doc
%ruby_gemsdocdir/aws-sdk-kafka-1.53.0

%files         -n gem-aws-sdk-kafka-devel

%files         -n gem-aws-sdk-macie
%ruby_gemspecdir/aws-sdk-macie-1.40.0.gemspec
%ruby_gemslibdir/aws-sdk-macie-1.40.0

%files         -n gem-aws-sdk-macie-doc
%ruby_gemsdocdir/aws-sdk-macie-1.40.0

%files         -n gem-aws-sdk-macie-devel

%files         -n gem-aws-sdk-mturk
%ruby_gemspecdir/aws-sdk-mturk-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-mturk-1.42.0

%files         -n gem-aws-sdk-mturk-doc
%ruby_gemsdocdir/aws-sdk-mturk-1.42.0

%files         -n gem-aws-sdk-mturk-devel

%files         -n gem-aws-sdk-omics
%ruby_gemspecdir/aws-sdk-omics-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-omics-1.1.0

%files         -n gem-aws-sdk-omics-doc
%ruby_gemsdocdir/aws-sdk-omics-1.1.0

%files         -n gem-aws-sdk-omics-devel

%files         -n gem-aws-sdk-pipes
%ruby_gemspecdir/aws-sdk-pipes-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-pipes-1.1.0

%files         -n gem-aws-sdk-pipes-doc
%ruby_gemsdocdir/aws-sdk-pipes-1.1.0

%files         -n gem-aws-sdk-pipes-devel

%files         -n gem-aws-sdk-polly
%ruby_gemspecdir/aws-sdk-polly-1.64.0.gemspec
%ruby_gemslibdir/aws-sdk-polly-1.64.0

%files         -n gem-aws-sdk-polly-doc
%ruby_gemsdocdir/aws-sdk-polly-1.64.0

%files         -n gem-aws-sdk-polly-devel

%files         -n gem-aws-sdk-sesv2
%ruby_gemspecdir/aws-sdk-sesv2-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-sesv2-1.31.0

%files         -n gem-aws-sdk-sesv2-doc
%ruby_gemsdocdir/aws-sdk-sesv2-1.31.0

%files         -n gem-aws-sdk-sesv2-devel

%files         -n gem-aws-sdk-wafv2
%ruby_gemspecdir/aws-sdk-wafv2-1.47.0.gemspec
%ruby_gemslibdir/aws-sdk-wafv2-1.47.0

%files         -n gem-aws-sdk-wafv2-doc
%ruby_gemsdocdir/aws-sdk-wafv2-1.47.0

%files         -n gem-aws-sdk-wafv2-devel

%files         -n gem-aws-partitions
%ruby_gemspecdir/aws-partitions-1.701.0.gemspec
%ruby_gemslibdir/aws-partitions-1.701.0

%files         -n gem-aws-partitions-doc
%ruby_gemsdocdir/aws-partitions-1.701.0

%files         -n gem-aws-partitions-devel

%files         -n gem-aws-sdk-acmpca
%ruby_gemspecdir/aws-sdk-acmpca-1.53.0.gemspec
%ruby_gemslibdir/aws-sdk-acmpca-1.53.0

%files         -n gem-aws-sdk-acmpca-doc
%ruby_gemsdocdir/aws-sdk-acmpca-1.53.0

%files         -n gem-aws-sdk-acmpca-devel

%files         -n gem-aws-sdk-athena
%ruby_gemspecdir/aws-sdk-athena-1.61.0.gemspec
%ruby_gemslibdir/aws-sdk-athena-1.61.0

%files         -n gem-aws-sdk-athena-doc
%ruby_gemsdocdir/aws-sdk-athena-1.61.0

%files         -n gem-aws-sdk-athena-devel

%files         -n gem-aws-sdk-backup
%ruby_gemspecdir/aws-sdk-backup-1.48.0.gemspec
%ruby_gemslibdir/aws-sdk-backup-1.48.0

%files         -n gem-aws-sdk-backup-doc
%ruby_gemsdocdir/aws-sdk-backup-1.48.0

%files         -n gem-aws-sdk-backup-devel

%files         -n gem-aws-sdk-braket
%ruby_gemspecdir/aws-sdk-braket-1.21.0.gemspec
%ruby_gemslibdir/aws-sdk-braket-1.21.0

%files         -n gem-aws-sdk-braket-doc
%ruby_gemsdocdir/aws-sdk-braket-1.21.0

%files         -n gem-aws-sdk-braket-devel

%files         -n gem-aws-sdk-cloud9
%ruby_gemspecdir/aws-sdk-cloud9-1.49.0.gemspec
%ruby_gemslibdir/aws-sdk-cloud9-1.49.0

%files         -n gem-aws-sdk-cloud9-doc
%ruby_gemsdocdir/aws-sdk-cloud9-1.49.0

%files         -n gem-aws-sdk-cloud9-devel

%files         -n gem-aws-sdk-health
%ruby_gemspecdir/aws-sdk-health-1.49.0.gemspec
%ruby_gemslibdir/aws-sdk-health-1.49.0

%files         -n gem-aws-sdk-health-doc
%ruby_gemsdocdir/aws-sdk-health-1.49.0

%files         -n gem-aws-sdk-health-devel

%files         -n gem-aws-sdk-kendra
%ruby_gemspecdir/aws-sdk-kendra-1.63.0.gemspec
%ruby_gemslibdir/aws-sdk-kendra-1.63.0

%files         -n gem-aws-sdk-kendra-doc
%ruby_gemsdocdir/aws-sdk-kendra-1.63.0

%files         -n gem-aws-sdk-kendra-devel

%files         -n gem-aws-sdk-lambda
%ruby_gemspecdir/aws-sdk-lambda-1.91.0.gemspec
%ruby_gemslibdir/aws-sdk-lambda-1.91.0

%files         -n gem-aws-sdk-lambda-doc
%ruby_gemsdocdir/aws-sdk-lambda-1.91.0

%files         -n gem-aws-sdk-lambda-devel

%files         -n gem-aws-sdk-macie2
%ruby_gemspecdir/aws-sdk-macie2-1.51.0.gemspec
%ruby_gemslibdir/aws-sdk-macie2-1.51.0

%files         -n gem-aws-sdk-macie2-doc
%ruby_gemsdocdir/aws-sdk-macie2-1.51.0

%files         -n gem-aws-sdk-macie2-devel

%files         -n gem-aws-sdk-mobile
%ruby_gemspecdir/aws-sdk-mobile-1.37.0.gemspec
%ruby_gemslibdir/aws-sdk-mobile-1.37.0

%files         -n gem-aws-sdk-mobile-doc
%ruby_gemsdocdir/aws-sdk-mobile-1.37.0

%files         -n gem-aws-sdk-mobile-devel

%files         -n gem-aws-sdk-proton
%ruby_gemspecdir/aws-sdk-proton-1.22.0.gemspec
%ruby_gemslibdir/aws-sdk-proton-1.22.0

%files         -n gem-aws-sdk-proton-doc
%ruby_gemsdocdir/aws-sdk-proton-1.22.0

%files         -n gem-aws-sdk-proton-devel

%files         -n gem-aws-sdk-shield
%ruby_gemspecdir/aws-sdk-shield-1.51.0.gemspec
%ruby_gemslibdir/aws-sdk-shield-1.51.0

%files         -n gem-aws-sdk-shield-doc
%ruby_gemsdocdir/aws-sdk-shield-1.51.0

%files         -n gem-aws-sdk-shield-devel

%files         -n gem-aws-sdk-signer
%ruby_gemspecdir/aws-sdk-signer-1.40.0.gemspec
%ruby_gemslibdir/aws-sdk-signer-1.40.0

%files         -n gem-aws-sdk-signer-doc
%ruby_gemsdocdir/aws-sdk-signer-1.40.0

%files         -n gem-aws-sdk-signer-devel

%files         -n gem-aws-sdk-ssmsap
%ruby_gemspecdir/aws-sdk-ssmsap-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-ssmsap-1.3.0

%files         -n gem-aws-sdk-ssmsap-doc
%ruby_gemsdocdir/aws-sdk-ssmsap-1.3.0

%files         -n gem-aws-sdk-ssmsap-devel

%files         -n gem-aws-sdk-states
%ruby_gemspecdir/aws-sdk-states-1.52.0.gemspec
%ruby_gemslibdir/aws-sdk-states-1.52.0

%files         -n gem-aws-sdk-states-doc
%ruby_gemsdocdir/aws-sdk-states-1.52.0

%files         -n gem-aws-sdk-states-devel

%files         -n gem-aws-eventstream
%ruby_gemspecdir/aws-eventstream-1.2.0.gemspec
%ruby_gemslibdir/aws-eventstream-1.2.0

%files         -n gem-aws-eventstream-doc
%ruby_gemsdocdir/aws-eventstream-1.2.0

%files         -n gem-aws-eventstream-devel

%files         -n gem-aws-sdk-account
%ruby_gemspecdir/aws-sdk-account-1.9.0.gemspec
%ruby_gemslibdir/aws-sdk-account-1.9.0

%files         -n gem-aws-sdk-account-doc
%ruby_gemsdocdir/aws-sdk-account-1.9.0

%files         -n gem-aws-sdk-account-devel

%files         -n gem-aws-sdk-amplify
%ruby_gemspecdir/aws-sdk-amplify-1.44.0.gemspec
%ruby_gemslibdir/aws-sdk-amplify-1.44.0

%files         -n gem-aws-sdk-amplify-doc
%ruby_gemsdocdir/aws-sdk-amplify-1.44.0

%files         -n gem-aws-sdk-amplify-devel

%files         -n gem-aws-sdk-appflow
%ruby_gemspecdir/aws-sdk-appflow-1.35.0.gemspec
%ruby_gemslibdir/aws-sdk-appflow-1.35.0

%files         -n gem-aws-sdk-appflow-doc
%ruby_gemsdocdir/aws-sdk-appflow-1.35.0

%files         -n gem-aws-sdk-appflow-devel

%files         -n gem-aws-sdk-appmesh
%ruby_gemspecdir/aws-sdk-appmesh-1.49.0.gemspec
%ruby_gemslibdir/aws-sdk-appmesh-1.49.0

%files         -n gem-aws-sdk-appmesh-doc
%ruby_gemsdocdir/aws-sdk-appmesh-1.49.0

%files         -n gem-aws-sdk-appmesh-devel

%files         -n gem-aws-sdk-appsync
%ruby_gemspecdir/aws-sdk-appsync-1.57.0.gemspec
%ruby_gemslibdir/aws-sdk-appsync-1.57.0

%files         -n gem-aws-sdk-appsync-doc
%ruby_gemsdocdir/aws-sdk-appsync-1.57.0

%files         -n gem-aws-sdk-appsync-devel

%files         -n gem-aws-sdk-budgets
%ruby_gemspecdir/aws-sdk-budgets-1.52.0.gemspec
%ruby_gemslibdir/aws-sdk-budgets-1.52.0

%files         -n gem-aws-sdk-budgets-doc
%ruby_gemsdocdir/aws-sdk-budgets-1.52.0

%files         -n gem-aws-sdk-budgets-devel

%files         -n gem-aws-sdk-connect
%ruby_gemspecdir/aws-sdk-connect-1.94.0.gemspec
%ruby_gemslibdir/aws-sdk-connect-1.94.0

%files         -n gem-aws-sdk-connect-doc
%ruby_gemsdocdir/aws-sdk-connect-1.94.0

%files         -n gem-aws-sdk-connect-devel

%files         -n gem-aws-sdk-glacier
%ruby_gemspecdir/aws-sdk-glacier-1.49.0.gemspec
%ruby_gemslibdir/aws-sdk-glacier-1.49.0

%files         -n gem-aws-sdk-glacier-doc
%ruby_gemsdocdir/aws-sdk-glacier-1.49.0

%files         -n gem-aws-sdk-glacier-devel

%files         -n gem-aws-sdk-ivschat
%ruby_gemspecdir/aws-sdk-ivschat-1.8.0.gemspec
%ruby_gemslibdir/aws-sdk-ivschat-1.8.0

%files         -n gem-aws-sdk-ivschat-doc
%ruby_gemsdocdir/aws-sdk-ivschat-1.8.0

%files         -n gem-aws-sdk-ivschat-devel

%files         -n gem-aws-sdk-kinesis
%ruby_gemspecdir/aws-sdk-kinesis-1.44.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesis-1.44.0

%files         -n gem-aws-sdk-kinesis-doc
%ruby_gemsdocdir/aws-sdk-kinesis-1.44.0

%files         -n gem-aws-sdk-kinesis-devel

%files         -n gem-aws-sdk-neptune
%ruby_gemspecdir/aws-sdk-neptune-1.49.0.gemspec
%ruby_gemslibdir/aws-sdk-neptune-1.49.0

%files         -n gem-aws-sdk-neptune-doc
%ruby_gemsdocdir/aws-sdk-neptune-1.49.0

%files         -n gem-aws-sdk-neptune-devel

%files         -n gem-aws-sdk-pricing
%ruby_gemspecdir/aws-sdk-pricing-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-pricing-1.42.0

%files         -n gem-aws-sdk-pricing-doc
%ruby_gemsdocdir/aws-sdk-pricing-1.42.0

%files         -n gem-aws-sdk-pricing-devel

%files         -n gem-aws-sdk-route53
%ruby_gemspecdir/aws-sdk-route53-1.71.0.gemspec
%ruby_gemslibdir/aws-sdk-route53-1.71.0

%files         -n gem-aws-sdk-route53-doc
%ruby_gemsdocdir/aws-sdk-route53-1.71.0

%files         -n gem-aws-sdk-route53-devel

%files         -n gem-aws-sdk-schemas
%ruby_gemspecdir/aws-sdk-schemas-1.25.0.gemspec
%ruby_gemslibdir/aws-sdk-schemas-1.25.0

%files         -n gem-aws-sdk-schemas-doc
%ruby_gemsdocdir/aws-sdk-schemas-1.25.0

%files         -n gem-aws-sdk-schemas-devel

%files         -n gem-aws-sdk-ssooidc
%ruby_gemspecdir/aws-sdk-ssooidc-1.23.0.gemspec
%ruby_gemslibdir/aws-sdk-ssooidc-1.23.0

%files         -n gem-aws-sdk-ssooidc-doc
%ruby_gemsdocdir/aws-sdk-ssooidc-1.23.0

%files         -n gem-aws-sdk-ssooidc-devel

%files         -n gem-aws-sdk-support
%ruby_gemspecdir/aws-sdk-support-1.44.0.gemspec
%ruby_gemslibdir/aws-sdk-support-1.44.0

%files         -n gem-aws-sdk-support-doc
%ruby_gemsdocdir/aws-sdk-support-1.44.0

%files         -n gem-aws-sdk-support-devel

%files         -n gem-aws-sdk-voiceid
%ruby_gemspecdir/aws-sdk-voiceid-1.11.0.gemspec
%ruby_gemslibdir/aws-sdk-voiceid-1.11.0

%files         -n gem-aws-sdk-voiceid-doc
%ruby_gemsdocdir/aws-sdk-voiceid-1.11.0

%files         -n gem-aws-sdk-voiceid-devel

%files         -n gem-aws-sdk-cloudhsm
%ruby_gemspecdir/aws-sdk-cloudhsm-1.41.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudhsm-1.41.0

%files         -n gem-aws-sdk-cloudhsm-doc
%ruby_gemsdocdir/aws-sdk-cloudhsm-1.41.0

%files         -n gem-aws-sdk-cloudhsm-devel

%files         -n gem-aws-sdk-codestar
%ruby_gemspecdir/aws-sdk-codestar-1.40.0.gemspec
%ruby_gemslibdir/aws-sdk-codestar-1.40.0

%files         -n gem-aws-sdk-codestar-doc
%ruby_gemsdocdir/aws-sdk-codestar-1.40.0

%files         -n gem-aws-sdk-codestar-devel

%files         -n gem-aws-sdk-datasync
%ruby_gemspecdir/aws-sdk-datasync-1.53.0.gemspec
%ruby_gemslibdir/aws-sdk-datasync-1.53.0

%files         -n gem-aws-sdk-datasync-doc
%ruby_gemsdocdir/aws-sdk-datasync-1.53.0

%files         -n gem-aws-sdk-datasync-devel

%files         -n gem-aws-sdk-dynamodb
%ruby_gemspecdir/aws-sdk-dynamodb-1.81.0.gemspec
%ruby_gemslibdir/aws-sdk-dynamodb-1.81.0

%files         -n gem-aws-sdk-dynamodb-doc
%ruby_gemsdocdir/aws-sdk-dynamodb-1.81.0

%files         -n gem-aws-sdk-dynamodb-devel

%files         -n gem-aws-sdk-finspace
%ruby_gemspecdir/aws-sdk-finspace-1.13.0.gemspec
%ruby_gemslibdir/aws-sdk-finspace-1.13.0

%files         -n gem-aws-sdk-finspace-doc
%ruby_gemsdocdir/aws-sdk-finspace-1.13.0

%files         -n gem-aws-sdk-finspace-devel

%files         -n gem-aws-sdk-firehose
%ruby_gemspecdir/aws-sdk-firehose-1.51.0.gemspec
%ruby_gemslibdir/aws-sdk-firehose-1.51.0

%files         -n gem-aws-sdk-firehose-doc
%ruby_gemsdocdir/aws-sdk-firehose-1.51.0

%files         -n gem-aws-sdk-firehose-devel

%files         -n gem-aws-sdk-gamelift
%ruby_gemspecdir/aws-sdk-gamelift-1.61.0.gemspec
%ruby_gemslibdir/aws-sdk-gamelift-1.61.0

%files         -n gem-aws-sdk-gamelift-doc
%ruby_gemsdocdir/aws-sdk-gamelift-1.61.0

%files         -n gem-aws-sdk-gamelift-devel

%files         -n gem-aws-sdk-memorydb
%ruby_gemspecdir/aws-sdk-memorydb-1.12.0.gemspec
%ruby_gemslibdir/aws-sdk-memorydb-1.12.0

%files         -n gem-aws-sdk-memorydb-doc
%ruby_gemsdocdir/aws-sdk-memorydb-1.12.0

%files         -n gem-aws-sdk-memorydb-devel

%files         -n gem-aws-sdk-opsworks
%ruby_gemspecdir/aws-sdk-opsworks-1.43.0.gemspec
%ruby_gemslibdir/aws-sdk-opsworks-1.43.0

%files         -n gem-aws-sdk-opsworks-doc
%ruby_gemsdocdir/aws-sdk-opsworks-1.43.0

%files         -n gem-aws-sdk-opsworks-devel

%files         -n gem-aws-sdk-outposts
%ruby_gemspecdir/aws-sdk-outposts-1.40.0.gemspec
%ruby_gemslibdir/aws-sdk-outposts-1.40.0

%files         -n gem-aws-sdk-outposts-doc
%ruby_gemsdocdir/aws-sdk-outposts-1.40.0

%files         -n gem-aws-sdk-outposts-devel

%files         -n gem-aws-sdk-panorama
%ruby_gemspecdir/aws-sdk-panorama-1.12.0.gemspec
%ruby_gemslibdir/aws-sdk-panorama-1.12.0

%files         -n gem-aws-sdk-panorama-doc
%ruby_gemsdocdir/aws-sdk-panorama-1.12.0

%files         -n gem-aws-sdk-panorama-devel

%files         -n gem-aws-sdk-pinpoint
%ruby_gemspecdir/aws-sdk-pinpoint-1.70.0.gemspec
%ruby_gemslibdir/aws-sdk-pinpoint-1.70.0

%files         -n gem-aws-sdk-pinpoint-doc
%ruby_gemsdocdir/aws-sdk-pinpoint-1.70.0

%files         -n gem-aws-sdk-pinpoint-devel

%files         -n gem-aws-sdk-redshift
%ruby_gemspecdir/aws-sdk-redshift-1.88.0.gemspec
%ruby_gemslibdir/aws-sdk-redshift-1.88.0

%files         -n gem-aws-sdk-redshift-doc
%ruby_gemsdocdir/aws-sdk-redshift-1.88.0

%files         -n gem-aws-sdk-redshift-devel

%files         -n gem-aws-sdk-simpledb
%ruby_gemspecdir/aws-sdk-simpledb-1.36.1.gemspec
%ruby_gemslibdir/aws-sdk-simpledb-1.36.1

%files         -n gem-aws-sdk-simpledb-doc
%ruby_gemsdocdir/aws-sdk-simpledb-1.36.1

%files         -n gem-aws-sdk-simpledb-devel

%files         -n gem-aws-sdk-snowball
%ruby_gemspecdir/aws-sdk-snowball-1.52.0.gemspec
%ruby_gemslibdir/aws-sdk-snowball-1.52.0

%files         -n gem-aws-sdk-snowball-doc
%ruby_gemsdocdir/aws-sdk-snowball-1.52.0

%files         -n gem-aws-sdk-snowball-devel

%files         -n gem-aws-sdk-ssoadmin
%ruby_gemspecdir/aws-sdk-ssoadmin-1.22.0.gemspec
%ruby_gemslibdir/aws-sdk-ssoadmin-1.22.0

%files         -n gem-aws-sdk-ssoadmin-doc
%ruby_gemsdocdir/aws-sdk-ssoadmin-1.22.0

%files         -n gem-aws-sdk-ssoadmin-devel

%files         -n gem-aws-sdk-textract
%ruby_gemspecdir/aws-sdk-textract-1.44.0.gemspec
%ruby_gemslibdir/aws-sdk-textract-1.44.0

%files         -n gem-aws-sdk-textract-doc
%ruby_gemsdocdir/aws-sdk-textract-1.44.0

%files         -n gem-aws-sdk-textract-devel

%files         -n gem-aws-sdk-transfer
%ruby_gemspecdir/aws-sdk-transfer-1.66.0.gemspec
%ruby_gemslibdir/aws-sdk-transfer-1.66.0

%files         -n gem-aws-sdk-transfer-doc
%ruby_gemsdocdir/aws-sdk-transfer-1.66.0

%files         -n gem-aws-sdk-transfer-devel

%files         -n gem-aws-sdk-workdocs
%ruby_gemspecdir/aws-sdk-workdocs-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-workdocs-1.42.0

%files         -n gem-aws-sdk-workdocs-doc
%ruby_gemsdocdir/aws-sdk-workdocs-1.42.0

%files         -n gem-aws-sdk-workdocs-devel

%files         -n gem-aws-sdk-worklink
%ruby_gemspecdir/aws-sdk-worklink-1.35.0.gemspec
%ruby_gemslibdir/aws-sdk-worklink-1.35.0

%files         -n gem-aws-sdk-worklink-doc
%ruby_gemsdocdir/aws-sdk-worklink-1.35.0

%files         -n gem-aws-sdk-worklink-devel

%files         -n gem-aws-sdk-workmail
%ruby_gemspecdir/aws-sdk-workmail-1.53.0.gemspec
%ruby_gemslibdir/aws-sdk-workmail-1.53.0

%files         -n gem-aws-sdk-workmail-doc
%ruby_gemsdocdir/aws-sdk-workmail-1.53.0

%files         -n gem-aws-sdk-workmail-devel

%files         -n gem-aws-sdk-appconfig
%ruby_gemspecdir/aws-sdk-appconfig-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-appconfig-1.28.0

%files         -n gem-aws-sdk-appconfig-doc
%ruby_gemsdocdir/aws-sdk-appconfig-1.28.0

%files         -n gem-aws-sdk-appconfig-devel

%files         -n gem-aws-sdk-apprunner
%ruby_gemspecdir/aws-sdk-apprunner-1.20.0.gemspec
%ruby_gemslibdir/aws-sdk-apprunner-1.20.0

%files         -n gem-aws-sdk-apprunner-doc
%ruby_gemsdocdir/aws-sdk-apprunner-1.20.0

%files         -n gem-aws-sdk-apprunner-devel

%files         -n gem-aws-sdk-appstream
%ruby_gemspecdir/aws-sdk-appstream-1.70.0.gemspec
%ruby_gemslibdir/aws-sdk-appstream-1.70.0

%files         -n gem-aws-sdk-appstream-doc
%ruby_gemsdocdir/aws-sdk-appstream-1.70.0

%files         -n gem-aws-sdk-appstream-devel

%files         -n gem-aws-sdk-codebuild
%ruby_gemspecdir/aws-sdk-codebuild-1.90.0.gemspec
%ruby_gemslibdir/aws-sdk-codebuild-1.90.0

%files         -n gem-aws-sdk-codebuild-doc
%ruby_gemsdocdir/aws-sdk-codebuild-1.90.0

%files         -n gem-aws-sdk-codebuild-devel

%files         -n gem-aws-sdk-detective
%ruby_gemspecdir/aws-sdk-detective-1.32.0.gemspec
%ruby_gemslibdir/aws-sdk-detective-1.32.0

%files         -n gem-aws-sdk-detective-doc
%ruby_gemsdocdir/aws-sdk-detective-1.32.0

%files         -n gem-aws-sdk-detective-devel

%files         -n gem-aws-sdk-ecrpublic
%ruby_gemspecdir/aws-sdk-ecrpublic-1.15.0.gemspec
%ruby_gemslibdir/aws-sdk-ecrpublic-1.15.0

%files         -n gem-aws-sdk-ecrpublic-doc
%ruby_gemsdocdir/aws-sdk-ecrpublic-1.15.0

%files         -n gem-aws-sdk-ecrpublic-devel

%files         -n gem-aws-sdk-guardduty
%ruby_gemspecdir/aws-sdk-guardduty-1.63.0.gemspec
%ruby_gemslibdir/aws-sdk-guardduty-1.63.0

%files         -n gem-aws-sdk-guardduty-doc
%ruby_gemsdocdir/aws-sdk-guardduty-1.63.0

%files         -n gem-aws-sdk-guardduty-devel

%files         -n gem-aws-sdk-honeycode
%ruby_gemspecdir/aws-sdk-honeycode-1.19.0.gemspec
%ruby_gemslibdir/aws-sdk-honeycode-1.19.0

%files         -n gem-aws-sdk-honeycode-doc
%ruby_gemsdocdir/aws-sdk-honeycode-1.19.0

%files         -n gem-aws-sdk-honeycode-devel

%files         -n gem-aws-sdk-inspector
%ruby_gemspecdir/aws-sdk-inspector-1.45.0.gemspec
%ruby_gemslibdir/aws-sdk-inspector-1.45.0

%files         -n gem-aws-sdk-inspector-doc
%ruby_gemsdocdir/aws-sdk-inspector-1.45.0

%files         -n gem-aws-sdk-inspector-devel

%files         -n gem-aws-sdk-iotevents
%ruby_gemspecdir/aws-sdk-iotevents-1.35.0.gemspec
%ruby_gemslibdir/aws-sdk-iotevents-1.35.0

%files         -n gem-aws-sdk-iotevents-doc
%ruby_gemsdocdir/aws-sdk-iotevents-1.35.0

%files         -n gem-aws-sdk-iotevents-devel

%files         -n gem-aws-sdk-keyspaces
%ruby_gemspecdir/aws-sdk-keyspaces-1.4.0.gemspec
%ruby_gemslibdir/aws-sdk-keyspaces-1.4.0

%files         -n gem-aws-sdk-keyspaces-doc
%ruby_gemsdocdir/aws-sdk-keyspaces-1.4.0

%files         -n gem-aws-sdk-keyspaces-devel

%files         -n gem-aws-sdk-lightsail
%ruby_gemspecdir/aws-sdk-lightsail-1.73.0.gemspec
%ruby_gemslibdir/aws-sdk-lightsail-1.73.0

%files         -n gem-aws-sdk-lightsail-doc
%ruby_gemsdocdir/aws-sdk-lightsail-1.73.0

%files         -n gem-aws-sdk-lightsail-devel

%files         -n gem-aws-sdk-medialive
%ruby_gemspecdir/aws-sdk-medialive-1.96.0.gemspec
%ruby_gemslibdir/aws-sdk-medialive-1.96.0

%files         -n gem-aws-sdk-medialive-doc
%ruby_gemsdocdir/aws-sdk-medialive-1.96.0

%files         -n gem-aws-sdk-medialive-devel

%files         -n gem-aws-sdk-resources
%ruby_gemspecdir/aws-sdk-resources-3.157.0.gemspec
%ruby_gemslibdir/aws-sdk-resources-3.157.0

%files         -n aws-v3-rb
%_bindir/aws-v3.rb

%files         -n gem-aws-sdk-resources-doc
%ruby_gemsdocdir/aws-sdk-resources-3.157.0

%files         -n gem-aws-sdk-resources-devel

%files         -n gem-aws-sdk-robomaker
%ruby_gemspecdir/aws-sdk-robomaker-1.53.0.gemspec
%ruby_gemslibdir/aws-sdk-robomaker-1.53.0

%files         -n gem-aws-sdk-robomaker-doc
%ruby_gemsdocdir/aws-sdk-robomaker-1.53.0

%files         -n gem-aws-sdk-robomaker-devel

%files         -n gem-aws-sdk-s3control
%ruby_gemspecdir/aws-sdk-s3control-1.60.0.gemspec
%ruby_gemslibdir/aws-sdk-s3control-1.60.0

%files         -n gem-aws-sdk-s3control-doc
%ruby_gemsdocdir/aws-sdk-s3control-1.60.0

%files         -n gem-aws-sdk-s3control-devel

%files         -n gem-aws-sdk-sagemaker
%ruby_gemspecdir/aws-sdk-sagemaker-1.164.0.gemspec
%ruby_gemslibdir/aws-sdk-sagemaker-1.164.0

%files         -n gem-aws-sdk-sagemaker-doc
%ruby_gemsdocdir/aws-sdk-sagemaker-1.164.0

%files         -n gem-aws-sdk-sagemaker-devel

%files         -n gem-aws-sdk-scheduler
%ruby_gemspecdir/aws-sdk-scheduler-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-scheduler-1.2.0

%files         -n gem-aws-sdk-scheduler-doc
%ruby_gemsdocdir/aws-sdk-scheduler-1.2.0

%files         -n gem-aws-sdk-scheduler-devel

%files         -n gem-aws-sdk-translate
%ruby_gemspecdir/aws-sdk-translate-1.50.0.gemspec
%ruby_gemslibdir/aws-sdk-translate-1.50.0

%files         -n gem-aws-sdk-translate-doc
%ruby_gemsdocdir/aws-sdk-translate-1.50.0

%files         -n gem-aws-sdk-translate-devel

%files         -n gem-aws-sdk-apigateway
%ruby_gemspecdir/aws-sdk-apigateway-1.81.0.gemspec
%ruby_gemslibdir/aws-sdk-apigateway-1.81.0

%files         -n gem-aws-sdk-apigateway-doc
%ruby_gemsdocdir/aws-sdk-apigateway-1.81.0

%files         -n gem-aws-sdk-apigateway-devel

%files         -n gem-aws-sdk-cleanrooms
%ruby_gemspecdir/aws-sdk-cleanrooms-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-cleanrooms-1.1.0

%files         -n gem-aws-sdk-cleanrooms-doc
%ruby_gemsdocdir/aws-sdk-cleanrooms-1.1.0

%files         -n gem-aws-sdk-cleanrooms-devel

%files         -n gem-aws-sdk-cloudfront
%ruby_gemspecdir/aws-sdk-cloudfront-1.74.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudfront-1.74.0

%files         -n gem-aws-sdk-cloudfront-doc
%ruby_gemsdocdir/aws-sdk-cloudfront-1.74.0

%files         -n gem-aws-sdk-cloudfront-devel

%files         -n gem-aws-sdk-cloudhsmv2
%ruby_gemspecdir/aws-sdk-cloudhsmv2-1.44.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudhsmv2-1.44.0

%files         -n gem-aws-sdk-cloudhsmv2-doc
%ruby_gemsdocdir/aws-sdk-cloudhsmv2-1.44.0

%files         -n gem-aws-sdk-cloudhsmv2-devel

%files         -n gem-aws-sdk-cloudtrail
%ruby_gemspecdir/aws-sdk-cloudtrail-1.56.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudtrail-1.56.0

%files         -n gem-aws-sdk-cloudtrail-doc
%ruby_gemsdocdir/aws-sdk-cloudtrail-1.56.0

%files         -n gem-aws-sdk-cloudtrail-devel

%files         -n gem-aws-sdk-cloudwatch
%ruby_gemspecdir/aws-sdk-cloudwatch-1.71.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudwatch-1.71.0

%files         -n gem-aws-sdk-cloudwatch-doc
%ruby_gemsdocdir/aws-sdk-cloudwatch-1.71.0

%files         -n gem-aws-sdk-cloudwatch-devel

%files         -n gem-aws-sdk-codecommit
%ruby_gemspecdir/aws-sdk-codecommit-1.53.0.gemspec
%ruby_gemslibdir/aws-sdk-codecommit-1.53.0

%files         -n gem-aws-sdk-codecommit-doc
%ruby_gemsdocdir/aws-sdk-codecommit-1.53.0

%files         -n gem-aws-sdk-codecommit-devel

%files         -n gem-aws-sdk-codedeploy
%ruby_gemspecdir/aws-sdk-codedeploy-1.52.0.gemspec
%ruby_gemslibdir/aws-sdk-codedeploy-1.52.0

%files         -n gem-aws-sdk-codedeploy-doc
%ruby_gemsdocdir/aws-sdk-codedeploy-1.52.0

%files         -n gem-aws-sdk-codedeploy-devel

%files         -n gem-aws-sdk-comprehend
%ruby_gemspecdir/aws-sdk-comprehend-1.65.0.gemspec
%ruby_gemslibdir/aws-sdk-comprehend-1.65.0

%files         -n gem-aws-sdk-comprehend-doc
%ruby_gemsdocdir/aws-sdk-comprehend-1.65.0

%files         -n gem-aws-sdk-comprehend-devel

%files         -n gem-aws-sdk-devicefarm
%ruby_gemspecdir/aws-sdk-devicefarm-1.54.0.gemspec
%ruby_gemslibdir/aws-sdk-devicefarm-1.54.0

%files         -n gem-aws-sdk-devicefarm-doc
%ruby_gemsdocdir/aws-sdk-devicefarm-1.54.0

%files         -n gem-aws-sdk-devicefarm-devel

%files         -n gem-aws-sdk-devopsguru
%ruby_gemspecdir/aws-sdk-devopsguru-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-devopsguru-1.28.0

%files         -n gem-aws-sdk-devopsguru-doc
%ruby_gemsdocdir/aws-sdk-devopsguru-1.28.0

%files         -n gem-aws-sdk-devopsguru-devel

%files         -n gem-aws-sdk-gamesparks
%ruby_gemspecdir/aws-sdk-gamesparks-1.4.0.gemspec
%ruby_gemslibdir/aws-sdk-gamesparks-1.4.0

%files         -n gem-aws-sdk-gamesparks-doc
%ruby_gemsdocdir/aws-sdk-gamesparks-1.4.0

%files         -n gem-aws-sdk-gamesparks-devel

%files         -n gem-aws-sdk-greengrass
%ruby_gemspecdir/aws-sdk-greengrass-1.53.0.gemspec
%ruby_gemslibdir/aws-sdk-greengrass-1.53.0

%files         -n gem-aws-sdk-greengrass-doc
%ruby_gemsdocdir/aws-sdk-greengrass-1.53.0

%files         -n gem-aws-sdk-greengrass-devel

%files         -n gem-aws-sdk-healthlake
%ruby_gemspecdir/aws-sdk-healthlake-1.15.0.gemspec
%ruby_gemslibdir/aws-sdk-healthlake-1.15.0

%files         -n gem-aws-sdk-healthlake-doc
%ruby_gemsdocdir/aws-sdk-healthlake-1.15.0

%files         -n gem-aws-sdk-healthlake-devel

%files         -n gem-aws-sdk-inspector2
%ruby_gemspecdir/aws-sdk-inspector2-1.10.0.gemspec
%ruby_gemslibdir/aws-sdk-inspector2-1.10.0

%files         -n gem-aws-sdk-inspector2-doc
%ruby_gemsdocdir/aws-sdk-inspector2-1.10.0

%files         -n gem-aws-sdk-inspector2-devel

%files         -n gem-aws-sdk-mediastore
%ruby_gemspecdir/aws-sdk-mediastore-1.43.0.gemspec
%ruby_gemslibdir/aws-sdk-mediastore-1.43.0

%files         -n gem-aws-sdk-mediastore-doc
%ruby_gemsdocdir/aws-sdk-mediastore-1.43.0

%files         -n gem-aws-sdk-mediastore-devel

%files         -n gem-aws-sdk-opsworkscm
%ruby_gemspecdir/aws-sdk-opsworkscm-1.54.0.gemspec
%ruby_gemslibdir/aws-sdk-opsworkscm-1.54.0

%files         -n gem-aws-sdk-opsworkscm-doc
%ruby_gemsdocdir/aws-sdk-opsworkscm-1.54.0

%files         -n gem-aws-sdk-opsworkscm-devel

%files         -n gem-aws-sdk-quicksight
%ruby_gemspecdir/aws-sdk-quicksight-1.74.0.gemspec
%ruby_gemslibdir/aws-sdk-quicksight-1.74.0

%files         -n gem-aws-sdk-quicksight-doc
%ruby_gemsdocdir/aws-sdk-quicksight-1.74.0

%files         -n gem-aws-sdk-quicksight-devel

%files         -n gem-aws-sdk-recyclebin
%ruby_gemspecdir/aws-sdk-recyclebin-1.8.0.gemspec
%ruby_gemslibdir/aws-sdk-recyclebin-1.8.0

%files         -n gem-aws-sdk-recyclebin-doc
%ruby_gemsdocdir/aws-sdk-recyclebin-1.8.0

%files         -n gem-aws-sdk-recyclebin-devel

%files         -n gem-aws-sdk-s3outposts
%ruby_gemspecdir/aws-sdk-s3outposts-1.15.0.gemspec
%ruby_gemslibdir/aws-sdk-s3outposts-1.15.0

%files         -n gem-aws-sdk-s3outposts-doc
%ruby_gemsdocdir/aws-sdk-s3outposts-1.15.0

%files         -n gem-aws-sdk-s3outposts-devel

%files         -n gem-aws-sdk-supportapp
%ruby_gemspecdir/aws-sdk-supportapp-1.4.0.gemspec
%ruby_gemslibdir/aws-sdk-supportapp-1.4.0

%files         -n gem-aws-sdk-supportapp-doc
%ruby_gemsdocdir/aws-sdk-supportapp-1.4.0

%files         -n gem-aws-sdk-supportapp-devel

%files         -n gem-aws-sdk-synthetics
%ruby_gemspecdir/aws-sdk-synthetics-1.30.0.gemspec
%ruby_gemslibdir/aws-sdk-synthetics-1.30.0

%files         -n gem-aws-sdk-synthetics-doc
%ruby_gemsdocdir/aws-sdk-synthetics-1.30.0

%files         -n gem-aws-sdk-synthetics-devel

%files         -n gem-aws-sdk-workspaces
%ruby_gemspecdir/aws-sdk-workspaces-1.78.0.gemspec
%ruby_gemslibdir/aws-sdk-workspaces-1.78.0

%files         -n gem-aws-sdk-workspaces-doc
%ruby_gemsdocdir/aws-sdk-workspaces-1.78.0

%files         -n gem-aws-sdk-workspaces-devel

%files         -n gem-aws-sdk-appregistry
%ruby_gemspecdir/aws-sdk-appregistry-1.19.0.gemspec
%ruby_gemslibdir/aws-sdk-appregistry-1.19.0

%files         -n gem-aws-sdk-appregistry-doc
%ruby_gemsdocdir/aws-sdk-appregistry-1.19.0

%files         -n gem-aws-sdk-appregistry-devel

%files         -n gem-aws-sdk-autoscaling
%ruby_gemspecdir/aws-sdk-autoscaling-1.85.0.gemspec
%ruby_gemslibdir/aws-sdk-autoscaling-1.85.0

%files         -n gem-aws-sdk-autoscaling-doc
%ruby_gemsdocdir/aws-sdk-autoscaling-1.85.0

%files         -n gem-aws-sdk-autoscaling-devel

%files         -n gem-aws-sdk-cloudsearch
%ruby_gemspecdir/aws-sdk-cloudsearch-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudsearch-1.42.0

%files         -n gem-aws-sdk-cloudsearch-doc
%ruby_gemsdocdir/aws-sdk-cloudsearch-1.42.0

%files         -n gem-aws-sdk-cloudsearch-devel

%files         -n gem-aws-sdk-cognitosync
%ruby_gemspecdir/aws-sdk-cognitosync-1.38.0.gemspec
%ruby_gemslibdir/aws-sdk-cognitosync-1.38.0

%files         -n gem-aws-sdk-cognitosync-doc
%ruby_gemsdocdir/aws-sdk-cognitosync-1.38.0

%files         -n gem-aws-sdk-cognitosync-devel

%files         -n gem-aws-sdk-elasticache
%ruby_gemspecdir/aws-sdk-elasticache-1.84.0.gemspec
%ruby_gemslibdir/aws-sdk-elasticache-1.84.0

%files         -n gem-aws-sdk-elasticache-doc
%ruby_gemsdocdir/aws-sdk-elasticache-1.84.0

%files         -n gem-aws-sdk-elasticache-devel

%files         -n gem-aws-sdk-eventbridge
%ruby_gemspecdir/aws-sdk-eventbridge-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-eventbridge-1.42.0

%files         -n gem-aws-sdk-eventbridge-doc
%ruby_gemsdocdir/aws-sdk-eventbridge-1.42.0

%files         -n gem-aws-sdk-eventbridge-devel

%files         -n gem-aws-sdk-iotfleethub
%ruby_gemspecdir/aws-sdk-iotfleethub-1.13.0.gemspec
%ruby_gemslibdir/aws-sdk-iotfleethub-1.13.0

%files         -n gem-aws-sdk-iotfleethub-doc
%ruby_gemsdocdir/aws-sdk-iotfleethub-1.13.0

%files         -n gem-aws-sdk-iotfleethub-devel

%files         -n gem-aws-sdk-iotsitewise
%ruby_gemspecdir/aws-sdk-iotsitewise-1.48.0.gemspec
%ruby_gemslibdir/aws-sdk-iotsitewise-1.48.0

%files         -n gem-aws-sdk-iotsitewise-doc
%ruby_gemsdocdir/aws-sdk-iotsitewise-1.48.0

%files         -n gem-aws-sdk-iotsitewise-devel

%files         -n gem-aws-sdk-iotwireless
%ruby_gemspecdir/aws-sdk-iotwireless-1.29.0.gemspec
%ruby_gemslibdir/aws-sdk-iotwireless-1.29.0

%files         -n gem-aws-sdk-iotwireless-doc
%ruby_gemsdocdir/aws-sdk-iotwireless-1.29.0

%files         -n gem-aws-sdk-iotwireless-devel

%files         -n gem-aws-sdk-lexmodelsv2
%ruby_gemspecdir/aws-sdk-lexmodelsv2-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-lexmodelsv2-1.31.0

%files         -n gem-aws-sdk-lexmodelsv2-doc
%ruby_gemsdocdir/aws-sdk-lexmodelsv2-1.31.0

%files         -n gem-aws-sdk-lexmodelsv2-devel

%files         -n gem-aws-sdk-mediatailor
%ruby_gemspecdir/aws-sdk-mediatailor-1.59.0.gemspec
%ruby_gemslibdir/aws-sdk-mediatailor-1.59.0

%files         -n gem-aws-sdk-mediatailor-doc
%ruby_gemsdocdir/aws-sdk-mediatailor-1.59.0

%files         -n gem-aws-sdk-mediatailor-devel

%files         -n gem-aws-sdk-personalize
%ruby_gemspecdir/aws-sdk-personalize-1.46.0.gemspec
%ruby_gemslibdir/aws-sdk-personalize-1.46.0

%files         -n gem-aws-sdk-personalize-doc
%ruby_gemsdocdir/aws-sdk-personalize-1.46.0

%files         -n gem-aws-sdk-personalize-devel

%files         -n gem-aws-sdk-qldbsession
%ruby_gemspecdir/aws-sdk-qldbsession-1.24.0.gemspec
%ruby_gemslibdir/aws-sdk-qldbsession-1.24.0

%files         -n gem-aws-sdk-qldbsession-doc
%ruby_gemsdocdir/aws-sdk-qldbsession-1.24.0

%files         -n gem-aws-sdk-qldbsession-devel

%files         -n gem-aws-sdk-rekognition
%ruby_gemspecdir/aws-sdk-rekognition-1.74.0.gemspec
%ruby_gemslibdir/aws-sdk-rekognition-1.74.0

%files         -n gem-aws-sdk-rekognition-doc
%ruby_gemsdocdir/aws-sdk-rekognition-1.74.0

%files         -n gem-aws-sdk-rekognition-devel

%files         -n gem-aws-sdk-securityhub
%ruby_gemspecdir/aws-sdk-securityhub-1.75.0.gemspec
%ruby_gemslibdir/aws-sdk-securityhub-1.75.0

%files         -n gem-aws-sdk-securityhub-doc
%ruby_gemsdocdir/aws-sdk-securityhub-1.75.0

%files         -n gem-aws-sdk-securityhub-devel

%files         -n gem-aws-sdk-ssmcontacts
%ruby_gemspecdir/aws-sdk-ssmcontacts-1.16.0.gemspec
%ruby_gemslibdir/aws-sdk-ssmcontacts-1.16.0

%files         -n gem-aws-sdk-ssmcontacts-doc
%ruby_gemsdocdir/aws-sdk-ssmcontacts-1.16.0

%files         -n gem-aws-sdk-ssmcontacts-devel

%files         -n gem-aws-sdk-wafregional
%ruby_gemspecdir/aws-sdk-wafregional-1.50.0.gemspec
%ruby_gemslibdir/aws-sdk-wafregional-1.50.0

%files         -n gem-aws-sdk-wafregional-doc
%ruby_gemsdocdir/aws-sdk-wafregional-1.50.0

%files         -n gem-aws-sdk-wafregional-devel

%files         -n gem-aws-sdk-apigatewayv2
%ruby_gemspecdir/aws-sdk-apigatewayv2-1.44.0.gemspec
%ruby_gemslibdir/aws-sdk-apigatewayv2-1.44.0

%files         -n gem-aws-sdk-apigatewayv2-doc
%ruby_gemsdocdir/aws-sdk-apigatewayv2-1.44.0

%files         -n gem-aws-sdk-apigatewayv2-devel

%files         -n gem-aws-sdk-auditmanager
%ruby_gemspecdir/aws-sdk-auditmanager-1.30.0.gemspec
%ruby_gemslibdir/aws-sdk-auditmanager-1.30.0

%files         -n gem-aws-sdk-auditmanager-doc
%ruby_gemsdocdir/aws-sdk-auditmanager-1.30.0

%files         -n gem-aws-sdk-auditmanager-devel

%files         -n gem-aws-sdk-codeartifact
%ruby_gemspecdir/aws-sdk-codeartifact-1.24.0.gemspec
%ruby_gemslibdir/aws-sdk-codeartifact-1.24.0

%files         -n gem-aws-sdk-codeartifact-doc
%ruby_gemsdocdir/aws-sdk-codeartifact-1.24.0

%files         -n gem-aws-sdk-codeartifact-devel

%files         -n gem-aws-sdk-codecatalyst
%ruby_gemspecdir/aws-sdk-codecatalyst-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-codecatalyst-1.1.0

%files         -n gem-aws-sdk-codecatalyst-doc
%ruby_gemsdocdir/aws-sdk-codecatalyst-1.1.0

%files         -n gem-aws-sdk-codecatalyst-devel

%files         -n gem-aws-sdk-codepipeline
%ruby_gemspecdir/aws-sdk-codepipeline-1.55.0.gemspec
%ruby_gemslibdir/aws-sdk-codepipeline-1.55.0

%files         -n gem-aws-sdk-codepipeline-doc
%ruby_gemsdocdir/aws-sdk-codepipeline-1.55.0

%files         -n gem-aws-sdk-codepipeline-devel

%files         -n gem-aws-sdk-connectcases
%ruby_gemspecdir/aws-sdk-connectcases-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-connectcases-1.3.0

%files         -n gem-aws-sdk-connectcases-doc
%ruby_gemsdocdir/aws-sdk-connectcases-1.3.0

%files         -n gem-aws-sdk-connectcases-devel

%files         -n gem-aws-sdk-controltower
%ruby_gemspecdir/aws-sdk-controltower-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-controltower-1.2.0

%files         -n gem-aws-sdk-controltower-doc
%ruby_gemsdocdir/aws-sdk-controltower-1.2.0

%files         -n gem-aws-sdk-controltower-devel

%files         -n gem-aws-sdk-costexplorer
%ruby_gemspecdir/aws-sdk-costexplorer-1.83.0.gemspec
%ruby_gemslibdir/aws-sdk-costexplorer-1.83.0

%files         -n gem-aws-sdk-costexplorer-doc
%ruby_gemsdocdir/aws-sdk-costexplorer-1.83.0

%files         -n gem-aws-sdk-costexplorer-devel

%files         -n gem-aws-sdk-dataexchange
%ruby_gemspecdir/aws-sdk-dataexchange-1.30.0.gemspec
%ruby_gemslibdir/aws-sdk-dataexchange-1.30.0

%files         -n gem-aws-sdk-dataexchange-doc
%ruby_gemsdocdir/aws-sdk-dataexchange-1.30.0

%files         -n gem-aws-sdk-dataexchange-devel

%files         -n gem-aws-sdk-datapipeline
%ruby_gemspecdir/aws-sdk-datapipeline-1.38.0.gemspec
%ruby_gemslibdir/aws-sdk-datapipeline-1.38.0

%files         -n gem-aws-sdk-datapipeline-doc
%ruby_gemsdocdir/aws-sdk-datapipeline-1.38.0

%files         -n gem-aws-sdk-datapipeline-devel

%files         -n gem-aws-sdk-docdbelastic
%ruby_gemspecdir/aws-sdk-docdbelastic-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-docdbelastic-1.1.0

%files         -n gem-aws-sdk-docdbelastic-doc
%ruby_gemsdocdir/aws-sdk-docdbelastic-1.1.0

%files         -n gem-aws-sdk-docdbelastic-devel

%files         -n gem-aws-sdk-finspacedata
%ruby_gemspecdir/aws-sdk-finspacedata-1.19.0.gemspec
%ruby_gemslibdir/aws-sdk-finspacedata-1.19.0

%files         -n gem-aws-sdk-finspacedata-doc
%ruby_gemsdocdir/aws-sdk-finspacedata-1.19.0

%files         -n gem-aws-sdk-finspacedata-devel

%files         -n gem-aws-sdk-gluedatabrew
%ruby_gemspecdir/aws-sdk-gluedatabrew-1.25.0.gemspec
%ruby_gemslibdir/aws-sdk-gluedatabrew-1.25.0

%files         -n gem-aws-sdk-gluedatabrew-doc
%ruby_gemsdocdir/aws-sdk-gluedatabrew-1.25.0

%files         -n gem-aws-sdk-gluedatabrew-devel

%files         -n gem-aws-sdk-greengrassv2
%ruby_gemspecdir/aws-sdk-greengrassv2-1.24.0.gemspec
%ruby_gemslibdir/aws-sdk-greengrassv2-1.24.0

%files         -n gem-aws-sdk-greengrassv2-doc
%ruby_gemsdocdir/aws-sdk-greengrassv2-1.24.0

%files         -n gem-aws-sdk-greengrassv2-devel

%files         -n gem-aws-sdk-imagebuilder
%ruby_gemspecdir/aws-sdk-imagebuilder-1.43.0.gemspec
%ruby_gemslibdir/aws-sdk-imagebuilder-1.43.0

%files         -n gem-aws-sdk-imagebuilder-doc
%ruby_gemsdocdir/aws-sdk-imagebuilder-1.43.0

%files         -n gem-aws-sdk-imagebuilder-devel

%files         -n gem-aws-sdk-importexport
%ruby_gemspecdir/aws-sdk-importexport-1.36.1.gemspec
%ruby_gemslibdir/aws-sdk-importexport-1.36.1

%files         -n gem-aws-sdk-importexport-doc
%ruby_gemsdocdir/aws-sdk-importexport-1.36.1

%files         -n gem-aws-sdk-importexport-devel

%files         -n gem-aws-sdk-iotanalytics
%ruby_gemspecdir/aws-sdk-iotanalytics-1.51.0.gemspec
%ruby_gemslibdir/aws-sdk-iotanalytics-1.51.0

%files         -n gem-aws-sdk-iotanalytics-doc
%ruby_gemsdocdir/aws-sdk-iotanalytics-1.51.0

%files         -n gem-aws-sdk-iotanalytics-devel

%files         -n gem-aws-sdk-iotdataplane
%ruby_gemspecdir/aws-sdk-iotdataplane-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-iotdataplane-1.42.0

%files         -n gem-aws-sdk-iotdataplane-doc
%ruby_gemsdocdir/aws-sdk-iotdataplane-1.42.0

%files         -n gem-aws-sdk-iotdataplane-devel

%files         -n gem-aws-sdk-iotfleetwise
%ruby_gemspecdir/aws-sdk-iotfleetwise-1.7.0.gemspec
%ruby_gemslibdir/aws-sdk-iotfleetwise-1.7.0

%files         -n gem-aws-sdk-iotfleetwise-doc
%ruby_gemsdocdir/aws-sdk-iotfleetwise-1.7.0

%files         -n gem-aws-sdk-iotfleetwise-devel

%files         -n gem-aws-sdk-iottwinmaker
%ruby_gemspecdir/aws-sdk-iottwinmaker-1.9.0.gemspec
%ruby_gemslibdir/aws-sdk-iottwinmaker-1.9.0

%files         -n gem-aws-sdk-iottwinmaker-doc
%ruby_gemsdocdir/aws-sdk-iottwinmaker-1.9.0

%files         -n gem-aws-sdk-iottwinmaker-devel

%files         -n gem-aws-sdk-kafkaconnect
%ruby_gemspecdir/aws-sdk-kafkaconnect-1.9.0.gemspec
%ruby_gemslibdir/aws-sdk-kafkaconnect-1.9.0

%files         -n gem-aws-sdk-kafkaconnect-doc
%ruby_gemsdocdir/aws-sdk-kafkaconnect-1.9.0

%files         -n gem-aws-sdk-kafkaconnect-devel

%files         -n gem-aws-sdk-kinesisvideo
%ruby_gemspecdir/aws-sdk-kinesisvideo-1.46.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesisvideo-1.46.0

%files         -n gem-aws-sdk-kinesisvideo-doc
%ruby_gemsdocdir/aws-sdk-kinesisvideo-1.46.0

%files         -n gem-aws-sdk-kinesisvideo-devel

%files         -n gem-aws-sdk-lexruntimev2
%ruby_gemspecdir/aws-sdk-lexruntimev2-1.18.0.gemspec
%ruby_gemslibdir/aws-sdk-lexruntimev2-1.18.0

%files         -n gem-aws-sdk-lexruntimev2-doc
%ruby_gemsdocdir/aws-sdk-lexruntimev2-1.18.0

%files         -n gem-aws-sdk-lexruntimev2-devel

%files         -n gem-aws-sdk-mediaconnect
%ruby_gemspecdir/aws-sdk-mediaconnect-1.47.0.gemspec
%ruby_gemslibdir/aws-sdk-mediaconnect-1.47.0

%files         -n gem-aws-sdk-mediaconnect-doc
%ruby_gemsdocdir/aws-sdk-mediaconnect-1.47.0

%files         -n gem-aws-sdk-mediaconnect-devel

%files         -n gem-aws-sdk-mediaconvert
%ruby_gemspecdir/aws-sdk-mediaconvert-1.98.0.gemspec
%ruby_gemslibdir/aws-sdk-mediaconvert-1.98.0

%files         -n gem-aws-sdk-mediaconvert-doc
%ruby_gemsdocdir/aws-sdk-mediaconvert-1.98.0

%files         -n gem-aws-sdk-mediaconvert-devel

%files         -n gem-aws-sdk-mediapackage
%ruby_gemspecdir/aws-sdk-mediapackage-1.58.0.gemspec
%ruby_gemslibdir/aws-sdk-mediapackage-1.58.0

%files         -n gem-aws-sdk-mediapackage-doc
%ruby_gemsdocdir/aws-sdk-mediapackage-1.58.0

%files         -n gem-aws-sdk-mediapackage-devel

%files         -n gem-aws-sdk-migrationhub
%ruby_gemspecdir/aws-sdk-migrationhub-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-migrationhub-1.42.0

%files         -n gem-aws-sdk-migrationhub-doc
%ruby_gemsdocdir/aws-sdk-migrationhub-1.42.0

%files         -n gem-aws-sdk-migrationhub-devel

%files         -n gem-aws-sdk-nimblestudio
%ruby_gemspecdir/aws-sdk-nimblestudio-1.18.0.gemspec
%ruby_gemslibdir/aws-sdk-nimblestudio-1.18.0

%files         -n gem-aws-sdk-nimblestudio-doc
%ruby_gemsdocdir/aws-sdk-nimblestudio-1.18.0

%files         -n gem-aws-sdk-nimblestudio-devel

%files         -n gem-aws-sdk-savingsplans
%ruby_gemspecdir/aws-sdk-savingsplans-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-savingsplans-1.28.0

%files         -n gem-aws-sdk-savingsplans-doc
%ruby_gemsdocdir/aws-sdk-savingsplans-1.28.0

%files         -n gem-aws-sdk-savingsplans-devel

%files         -n gem-aws-sdk-securitylake
%ruby_gemspecdir/aws-sdk-securitylake-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-securitylake-1.2.0

%files         -n gem-aws-sdk-securitylake-doc
%ruby_gemsdocdir/aws-sdk-securitylake-1.2.0

%files         -n gem-aws-sdk-securitylake-devel

%files         -n gem-aws-sdk-ssmincidents
%ruby_gemspecdir/aws-sdk-ssmincidents-1.21.0.gemspec
%ruby_gemslibdir/aws-sdk-ssmincidents-1.21.0

%files         -n gem-aws-sdk-ssmincidents-doc
%ruby_gemsdocdir/aws-sdk-ssmincidents-1.21.0

%files         -n gem-aws-sdk-ssmincidents-devel

%files         -n gem-aws-sdk-appconfigdata
%ruby_gemspecdir/aws-sdk-appconfigdata-1.7.0.gemspec
%ruby_gemslibdir/aws-sdk-appconfigdata-1.7.0

%files         -n gem-aws-sdk-appconfigdata-doc
%ruby_gemsdocdir/aws-sdk-appconfigdata-1.7.0

%files         -n gem-aws-sdk-appconfigdata-devel

%files         -n gem-aws-sdk-arczonalshift
%ruby_gemspecdir/aws-sdk-arczonalshift-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-arczonalshift-1.1.0

%files         -n gem-aws-sdk-arczonalshift-doc
%ruby_gemsdocdir/aws-sdk-arczonalshift-1.1.0

%files         -n gem-aws-sdk-arczonalshift-devel

%files         -n gem-aws-sdk-backupgateway
%ruby_gemspecdir/aws-sdk-backupgateway-1.8.0.gemspec
%ruby_gemslibdir/aws-sdk-backupgateway-1.8.0

%files         -n gem-aws-sdk-backupgateway-doc
%ruby_gemsdocdir/aws-sdk-backupgateway-1.8.0

%files         -n gem-aws-sdk-backupgateway-devel

%files         -n gem-aws-sdk-backupstorage
%ruby_gemspecdir/aws-sdk-backupstorage-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-backupstorage-1.2.0

%files         -n gem-aws-sdk-backupstorage-doc
%ruby_gemsdocdir/aws-sdk-backupstorage-1.2.0

%files         -n gem-aws-sdk-backupstorage-devel

%files         -n gem-aws-sdk-chimesdkvoice
%ruby_gemspecdir/aws-sdk-chimesdkvoice-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-chimesdkvoice-1.1.0

%files         -n gem-aws-sdk-chimesdkvoice-doc
%ruby_gemsdocdir/aws-sdk-chimesdkvoice-1.1.0

%files         -n gem-aws-sdk-chimesdkvoice-devel

%files         -n gem-aws-sdk-cloudwatchrum
%ruby_gemspecdir/aws-sdk-cloudwatchrum-1.8.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudwatchrum-1.8.0

%files         -n gem-aws-sdk-cloudwatchrum-doc
%ruby_gemsdocdir/aws-sdk-cloudwatchrum-1.8.0

%files         -n gem-aws-sdk-cloudwatchrum-devel

%files         -n gem-aws-sdk-configservice
%ruby_gemspecdir/aws-sdk-configservice-1.87.0.gemspec
%ruby_gemslibdir/aws-sdk-configservice-1.87.0

%files         -n gem-aws-sdk-configservice-doc
%ruby_gemsdocdir/aws-sdk-configservice-1.87.0

%files         -n gem-aws-sdk-configservice-devel

%files         -n gem-aws-sdk-directconnect
%ruby_gemspecdir/aws-sdk-directconnect-1.56.0.gemspec
%ruby_gemslibdir/aws-sdk-directconnect-1.56.0

%files         -n gem-aws-sdk-directconnect-doc
%ruby_gemsdocdir/aws-sdk-directconnect-1.56.0

%files         -n gem-aws-sdk-directconnect-devel

%files         -n gem-aws-sdk-emrcontainers
%ruby_gemspecdir/aws-sdk-emrcontainers-1.18.0.gemspec
%ruby_gemslibdir/aws-sdk-emrcontainers-1.18.0

%files         -n gem-aws-sdk-emrcontainers-doc
%ruby_gemsdocdir/aws-sdk-emrcontainers-1.18.0

%files         -n gem-aws-sdk-emrcontainers-devel

%files         -n gem-aws-sdk-emrserverless
%ruby_gemspecdir/aws-sdk-emrserverless-1.5.0.gemspec
%ruby_gemslibdir/aws-sdk-emrserverless-1.5.0

%files         -n gem-aws-sdk-emrserverless-doc
%ruby_gemsdocdir/aws-sdk-emrserverless-1.5.0

%files         -n gem-aws-sdk-emrserverless-devel

%files         -n gem-aws-sdk-frauddetector
%ruby_gemspecdir/aws-sdk-frauddetector-1.37.0.gemspec
%ruby_gemslibdir/aws-sdk-frauddetector-1.37.0

%files         -n gem-aws-sdk-frauddetector-doc
%ruby_gemsdocdir/aws-sdk-frauddetector-1.37.0

%files         -n gem-aws-sdk-frauddetector-devel

%files         -n gem-aws-sdk-groundstation
%ruby_gemspecdir/aws-sdk-groundstation-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-groundstation-1.31.0

%files         -n gem-aws-sdk-groundstation-doc
%ruby_gemsdocdir/aws-sdk-groundstation-1.31.0

%files         -n gem-aws-sdk-groundstation-devel

%files         -n gem-aws-sdk-identitystore
%ruby_gemspecdir/aws-sdk-identitystore-1.23.0.gemspec
%ruby_gemslibdir/aws-sdk-identitystore-1.23.0

%files         -n gem-aws-sdk-identitystore-doc
%ruby_gemsdocdir/aws-sdk-identitystore-1.23.0

%files         -n gem-aws-sdk-identitystore-devel

%files         -n gem-aws-sdk-ioteventsdata
%ruby_gemspecdir/aws-sdk-ioteventsdata-1.29.0.gemspec
%ruby_gemslibdir/aws-sdk-ioteventsdata-1.29.0

%files         -n gem-aws-sdk-ioteventsdata-doc
%ruby_gemsdocdir/aws-sdk-ioteventsdata-1.29.0

%files         -n gem-aws-sdk-ioteventsdata-devel

%files         -n gem-aws-sdk-iotroborunner
%ruby_gemspecdir/aws-sdk-iotroborunner-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-iotroborunner-1.1.0

%files         -n gem-aws-sdk-iotroborunner-doc
%ruby_gemsdocdir/aws-sdk-iotroborunner-1.1.0

%files         -n gem-aws-sdk-iotroborunner-devel

%files         -n gem-aws-sdk-kendraranking
%ruby_gemspecdir/aws-sdk-kendraranking-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-kendraranking-1.1.0

%files         -n gem-aws-sdk-kendraranking-doc
%ruby_gemsdocdir/aws-sdk-kendraranking-1.1.0

%files         -n gem-aws-sdk-kendraranking-devel

%files         -n gem-aws-sdk-lakeformation
%ruby_gemspecdir/aws-sdk-lakeformation-1.30.0.gemspec
%ruby_gemslibdir/aws-sdk-lakeformation-1.30.0

%files         -n gem-aws-sdk-lakeformation-doc
%ruby_gemsdocdir/aws-sdk-lakeformation-1.30.0

%files         -n gem-aws-sdk-lakeformation-devel

%files         -n gem-aws-sdk-lambdapreview
%ruby_gemspecdir/aws-sdk-lambdapreview-1.36.1.gemspec
%ruby_gemslibdir/aws-sdk-lambdapreview-1.36.1

%files         -n gem-aws-sdk-lambdapreview-doc
%ruby_gemsdocdir/aws-sdk-lambdapreview-1.36.1

%files         -n gem-aws-sdk-lambdapreview-devel

%files         -n gem-aws-sdk-organizations
%ruby_gemspecdir/aws-sdk-organizations-1.73.0.gemspec
%ruby_gemslibdir/aws-sdk-organizations-1.73.0

%files         -n gem-aws-sdk-organizations-doc
%ruby_gemsdocdir/aws-sdk-organizations-1.73.0

%files         -n gem-aws-sdk-organizations-devel

%files         -n gem-aws-sdk-pinpointemail
%ruby_gemspecdir/aws-sdk-pinpointemail-1.37.0.gemspec
%ruby_gemslibdir/aws-sdk-pinpointemail-1.37.0

%files         -n gem-aws-sdk-pinpointemail-doc
%ruby_gemsdocdir/aws-sdk-pinpointemail-1.37.0

%files         -n gem-aws-sdk-pinpointemail-devel

%files         -n gem-aws-sdk-resiliencehub
%ruby_gemspecdir/aws-sdk-resiliencehub-1.9.0.gemspec
%ruby_gemslibdir/aws-sdk-resiliencehub-1.9.0

%files         -n gem-aws-sdk-resiliencehub-doc
%ruby_gemsdocdir/aws-sdk-resiliencehub-1.9.0

%files         -n gem-aws-sdk-resiliencehub-devel

%files         -n gem-aws-sdk-rolesanywhere
%ruby_gemspecdir/aws-sdk-rolesanywhere-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-rolesanywhere-1.2.0

%files         -n gem-aws-sdk-rolesanywhere-doc
%ruby_gemsdocdir/aws-sdk-rolesanywhere-1.2.0

%files         -n gem-aws-sdk-rolesanywhere-devel

%files         -n gem-aws-sdk-servicequotas
%ruby_gemspecdir/aws-sdk-servicequotas-1.25.0.gemspec
%ruby_gemslibdir/aws-sdk-servicequotas-1.25.0

%files         -n gem-aws-sdk-servicequotas-doc
%ruby_gemsdocdir/aws-sdk-servicequotas-1.25.0

%files         -n gem-aws-sdk-servicequotas-devel

%files         -n gem-aws-sdk-workspacesweb
%ruby_gemspecdir/aws-sdk-workspacesweb-1.8.0.gemspec
%ruby_gemslibdir/aws-sdk-workspacesweb-1.8.0

%files         -n gem-aws-sdk-workspacesweb-doc
%ruby_gemsdocdir/aws-sdk-workspacesweb-1.8.0

%files         -n gem-aws-sdk-workspacesweb-devel

%files         -n gem-aws-sdk-accessanalyzer
%ruby_gemspecdir/aws-sdk-accessanalyzer-1.33.0.gemspec
%ruby_gemslibdir/aws-sdk-accessanalyzer-1.33.0

%files         -n gem-aws-sdk-accessanalyzer-doc
%ruby_gemsdocdir/aws-sdk-accessanalyzer-1.33.0

%files         -n gem-aws-sdk-accessanalyzer-devel

%files         -n gem-aws-sdk-amplifybackend
%ruby_gemspecdir/aws-sdk-amplifybackend-1.20.0.gemspec
%ruby_gemslibdir/aws-sdk-amplifybackend-1.20.0

%files         -n gem-aws-sdk-amplifybackend-doc
%ruby_gemsdocdir/aws-sdk-amplifybackend-1.20.0

%files         -n gem-aws-sdk-amplifybackend-devel

%files         -n gem-aws-sdk-clouddirectory
%ruby_gemspecdir/aws-sdk-clouddirectory-1.43.0.gemspec
%ruby_gemslibdir/aws-sdk-clouddirectory-1.43.0

%files         -n gem-aws-sdk-clouddirectory-doc
%ruby_gemsdocdir/aws-sdk-clouddirectory-1.43.0

%files         -n gem-aws-sdk-clouddirectory-devel

%files         -n gem-aws-sdk-cloudformation
%ruby_gemspecdir/aws-sdk-cloudformation-1.75.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudformation-1.75.0

%files         -n gem-aws-sdk-cloudformation-doc
%ruby_gemsdocdir/aws-sdk-cloudformation-1.75.0

%files         -n gem-aws-sdk-cloudformation-devel

%files         -n gem-aws-sdk-cloudwatchlogs
%ruby_gemspecdir/aws-sdk-cloudwatchlogs-1.62.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudwatchlogs-1.62.0

%files         -n gem-aws-sdk-cloudwatchlogs-doc
%ruby_gemsdocdir/aws-sdk-cloudwatchlogs-1.62.0

%files         -n gem-aws-sdk-cloudwatchlogs-devel

%files         -n gem-aws-sdk-iotthingsgraph
%ruby_gemspecdir/aws-sdk-iotthingsgraph-1.26.0.gemspec
%ruby_gemslibdir/aws-sdk-iotthingsgraph-1.26.0

%files         -n gem-aws-sdk-iotthingsgraph-doc
%ruby_gemsdocdir/aws-sdk-iotthingsgraph-1.26.0

%files         -n gem-aws-sdk-iotthingsgraph-devel

%files         -n gem-aws-sdk-licensemanager
%ruby_gemspecdir/aws-sdk-licensemanager-1.43.0.gemspec
%ruby_gemslibdir/aws-sdk-licensemanager-1.43.0

%files         -n gem-aws-sdk-licensemanager-doc
%ruby_gemsdocdir/aws-sdk-licensemanager-1.43.0

%files         -n gem-aws-sdk-licensemanager-devel

%files         -n gem-aws-sdk-lookoutmetrics
%ruby_gemspecdir/aws-sdk-lookoutmetrics-1.24.0.gemspec
%ruby_gemslibdir/aws-sdk-lookoutmetrics-1.24.0

%files         -n gem-aws-sdk-lookoutmetrics-doc
%ruby_gemsdocdir/aws-sdk-lookoutmetrics-1.24.0

%files         -n gem-aws-sdk-lookoutmetrics-devel

%files         -n gem-aws-sdk-managedgrafana
%ruby_gemspecdir/aws-sdk-managedgrafana-1.11.0.gemspec
%ruby_gemslibdir/aws-sdk-managedgrafana-1.11.0

%files         -n gem-aws-sdk-managedgrafana-doc
%ruby_gemsdocdir/aws-sdk-managedgrafana-1.11.0

%files         -n gem-aws-sdk-managedgrafana-devel

%files         -n gem-aws-sdk-mediastoredata
%ruby_gemspecdir/aws-sdk-mediastoredata-1.40.0.gemspec
%ruby_gemslibdir/aws-sdk-mediastoredata-1.40.0

%files         -n gem-aws-sdk-mediastoredata-doc
%ruby_gemsdocdir/aws-sdk-mediastoredata-1.40.0

%files         -n gem-aws-sdk-mediastoredata-devel

%files         -n gem-aws-sdk-networkmanager
%ruby_gemspecdir/aws-sdk-networkmanager-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-networkmanager-1.28.0

%files         -n gem-aws-sdk-networkmanager-doc
%ruby_gemsdocdir/aws-sdk-networkmanager-1.28.0

%files         -n gem-aws-sdk-networkmanager-devel

%files         -n gem-aws-sdk-rdsdataservice
%ruby_gemspecdir/aws-sdk-rdsdataservice-1.40.0.gemspec
%ruby_gemslibdir/aws-sdk-rdsdataservice-1.40.0

%files         -n gem-aws-sdk-rdsdataservice-doc
%ruby_gemsdocdir/aws-sdk-rdsdataservice-1.40.0

%files         -n gem-aws-sdk-rdsdataservice-devel

%files         -n gem-aws-sdk-resourcegroups
%ruby_gemspecdir/aws-sdk-resourcegroups-1.48.0.gemspec
%ruby_gemslibdir/aws-sdk-resourcegroups-1.48.0

%files         -n gem-aws-sdk-resourcegroups-doc
%ruby_gemsdocdir/aws-sdk-resourcegroups-1.48.0

%files         -n gem-aws-sdk-resourcegroups-devel

%files         -n gem-aws-sdk-route53domains
%ruby_gemspecdir/aws-sdk-route53domains-1.43.0.gemspec
%ruby_gemslibdir/aws-sdk-route53domains-1.43.0

%files         -n gem-aws-sdk-route53domains-doc
%ruby_gemsdocdir/aws-sdk-route53domains-1.43.0

%files         -n gem-aws-sdk-route53domains-devel

%files         -n gem-aws-sdk-secretsmanager
%ruby_gemspecdir/aws-sdk-secretsmanager-1.72.0.gemspec
%ruby_gemslibdir/aws-sdk-secretsmanager-1.72.0

%files         -n gem-aws-sdk-secretsmanager-doc
%ruby_gemsdocdir/aws-sdk-secretsmanager-1.72.0

%files         -n gem-aws-sdk-secretsmanager-devel

%files         -n gem-aws-sdk-servicecatalog
%ruby_gemspecdir/aws-sdk-servicecatalog-1.75.0.gemspec
%ruby_gemslibdir/aws-sdk-servicecatalog-1.75.0

%files         -n gem-aws-sdk-servicecatalog-doc
%ruby_gemsdocdir/aws-sdk-servicecatalog-1.75.0

%files         -n gem-aws-sdk-servicecatalog-devel

%files         -n gem-aws-sdk-simspaceweaver
%ruby_gemspecdir/aws-sdk-simspaceweaver-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-simspaceweaver-1.1.0

%files         -n gem-aws-sdk-simspaceweaver-doc
%ruby_gemsdocdir/aws-sdk-simspaceweaver-1.1.0

%files         -n gem-aws-sdk-simspaceweaver-devel

%files         -n gem-aws-sdk-storagegateway
%ruby_gemspecdir/aws-sdk-storagegateway-1.70.0.gemspec
%ruby_gemslibdir/aws-sdk-storagegateway-1.70.0

%files         -n gem-aws-sdk-storagegateway-doc
%ruby_gemsdocdir/aws-sdk-storagegateway-1.70.0

%files         -n gem-aws-sdk-storagegateway-devel

%files         -n gem-aws-sdk-cloudcontrolapi
%ruby_gemspecdir/aws-sdk-cloudcontrolapi-1.10.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudcontrolapi-1.10.0

%files         -n gem-aws-sdk-cloudcontrolapi-doc
%ruby_gemsdocdir/aws-sdk-cloudcontrolapi-1.10.0

%files         -n gem-aws-sdk-cloudcontrolapi-devel

%files         -n gem-aws-sdk-cognitoidentity
%ruby_gemspecdir/aws-sdk-cognitoidentity-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-cognitoidentity-1.42.0

%files         -n gem-aws-sdk-cognitoidentity-doc
%ruby_gemsdocdir/aws-sdk-cognitoidentity-1.42.0

%files         -n gem-aws-sdk-cognitoidentity-devel

%files         -n gem-aws-sdk-dynamodbstreams
%ruby_gemspecdir/aws-sdk-dynamodbstreams-1.43.0.gemspec
%ruby_gemslibdir/aws-sdk-dynamodbstreams-1.43.0

%files         -n gem-aws-sdk-dynamodbstreams-doc
%ruby_gemsdocdir/aws-sdk-dynamodbstreams-1.43.0

%files         -n gem-aws-sdk-dynamodbstreams-devel

%files         -n gem-aws-sdk-forecastservice
%ruby_gemspecdir/aws-sdk-forecastservice-1.39.0.gemspec
%ruby_gemslibdir/aws-sdk-forecastservice-1.39.0

%files         -n gem-aws-sdk-forecastservice-doc
%ruby_gemsdocdir/aws-sdk-forecastservice-1.39.0

%files         -n gem-aws-sdk-forecastservice-devel

%files         -n gem-aws-sdk-locationservice
%ruby_gemspecdir/aws-sdk-locationservice-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-locationservice-1.28.0

%files         -n gem-aws-sdk-locationservice-doc
%ruby_gemsdocdir/aws-sdk-locationservice-1.28.0

%files         -n gem-aws-sdk-locationservice-devel

%files         -n gem-aws-sdk-machinelearning
%ruby_gemspecdir/aws-sdk-machinelearning-1.39.0.gemspec
%ruby_gemslibdir/aws-sdk-machinelearning-1.39.0

%files         -n gem-aws-sdk-machinelearning-doc
%ruby_gemsdocdir/aws-sdk-machinelearning-1.39.0

%files         -n gem-aws-sdk-machinelearning-devel

%files         -n gem-aws-sdk-mediapackagevod
%ruby_gemspecdir/aws-sdk-mediapackagevod-1.41.0.gemspec
%ruby_gemslibdir/aws-sdk-mediapackagevod-1.41.0

%files         -n gem-aws-sdk-mediapackagevod-doc
%ruby_gemsdocdir/aws-sdk-mediapackagevod-1.41.0

%files         -n gem-aws-sdk-mediapackagevod-devel

%files         -n gem-aws-sdk-networkfirewall
%ruby_gemspecdir/aws-sdk-networkfirewall-1.24.0.gemspec
%ruby_gemslibdir/aws-sdk-networkfirewall-1.24.0

%files         -n gem-aws-sdk-networkfirewall-doc
%ruby_gemsdocdir/aws-sdk-networkfirewall-1.24.0

%files         -n gem-aws-sdk-networkfirewall-devel

%files         -n gem-aws-sdk-privatenetworks
%ruby_gemspecdir/aws-sdk-privatenetworks-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-privatenetworks-1.3.0

%files         -n gem-aws-sdk-privatenetworks-doc
%ruby_gemsdocdir/aws-sdk-privatenetworks-1.3.0

%files         -n gem-aws-sdk-privatenetworks-devel

%files         -n gem-aws-sdk-route53resolver
%ruby_gemspecdir/aws-sdk-route53resolver-1.39.0.gemspec
%ruby_gemslibdir/aws-sdk-route53resolver-1.39.0

%files         -n gem-aws-sdk-route53resolver-doc
%ruby_gemsdocdir/aws-sdk-route53resolver-1.39.0

%files         -n gem-aws-sdk-route53resolver-devel

%files         -n gem-aws-sdk-timestreamquery
%ruby_gemspecdir/aws-sdk-timestreamquery-1.18.0.gemspec
%ruby_gemslibdir/aws-sdk-timestreamquery-1.18.0

%files         -n gem-aws-sdk-timestreamquery-doc
%ruby_gemsdocdir/aws-sdk-timestreamquery-1.18.0

%files         -n gem-aws-sdk-timestreamquery-devel

%files         -n gem-aws-sdk-timestreamwrite
%ruby_gemspecdir/aws-sdk-timestreamwrite-1.16.0.gemspec
%ruby_gemslibdir/aws-sdk-timestreamwrite-1.16.0

%files         -n gem-aws-sdk-timestreamwrite-doc
%ruby_gemsdocdir/aws-sdk-timestreamwrite-1.16.0

%files         -n gem-aws-sdk-timestreamwrite-devel

%files         -n gem-aws-sdk-wellarchitected
%ruby_gemspecdir/aws-sdk-wellarchitected-1.20.0.gemspec
%ruby_gemslibdir/aws-sdk-wellarchitected-1.20.0

%files         -n gem-aws-sdk-wellarchitected-doc
%ruby_gemsdocdir/aws-sdk-wellarchitected-1.20.0

%files         -n gem-aws-sdk-wellarchitected-devel

%files         -n gem-aws-sdk-alexaforbusiness
%ruby_gemspecdir/aws-sdk-alexaforbusiness-1.58.0.gemspec
%ruby_gemslibdir/aws-sdk-alexaforbusiness-1.58.0

%files         -n gem-aws-sdk-alexaforbusiness-doc
%ruby_gemsdocdir/aws-sdk-alexaforbusiness-1.58.0

%files         -n gem-aws-sdk-alexaforbusiness-devel

%files         -n gem-aws-sdk-amplifyuibuilder
%ruby_gemspecdir/aws-sdk-amplifyuibuilder-1.9.0.gemspec
%ruby_gemslibdir/aws-sdk-amplifyuibuilder-1.9.0

%files         -n gem-aws-sdk-amplifyuibuilder-doc
%ruby_gemsdocdir/aws-sdk-amplifyuibuilder-1.9.0

%files         -n gem-aws-sdk-amplifyuibuilder-devel

%files         -n gem-aws-sdk-autoscalingplans
%ruby_gemspecdir/aws-sdk-autoscalingplans-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-autoscalingplans-1.42.0

%files         -n gem-aws-sdk-autoscalingplans-doc
%ruby_gemsdocdir/aws-sdk-autoscalingplans-1.42.0

%files         -n gem-aws-sdk-autoscalingplans-devel

%files         -n gem-aws-sdk-billingconductor
%ruby_gemspecdir/aws-sdk-billingconductor-1.6.0.gemspec
%ruby_gemslibdir/aws-sdk-billingconductor-1.6.0

%files         -n gem-aws-sdk-billingconductor-doc
%ruby_gemsdocdir/aws-sdk-billingconductor-1.6.0

%files         -n gem-aws-sdk-billingconductor-devel

%files         -n gem-aws-sdk-chimesdkidentity
%ruby_gemspecdir/aws-sdk-chimesdkidentity-1.11.0.gemspec
%ruby_gemslibdir/aws-sdk-chimesdkidentity-1.11.0

%files         -n gem-aws-sdk-chimesdkidentity-doc
%ruby_gemsdocdir/aws-sdk-chimesdkidentity-1.11.0

%files         -n gem-aws-sdk-chimesdkidentity-devel

%files         -n gem-aws-sdk-chimesdkmeetings
%ruby_gemspecdir/aws-sdk-chimesdkmeetings-1.16.0.gemspec
%ruby_gemslibdir/aws-sdk-chimesdkmeetings-1.16.0

%files         -n gem-aws-sdk-chimesdkmeetings-doc
%ruby_gemsdocdir/aws-sdk-chimesdkmeetings-1.16.0

%files         -n gem-aws-sdk-chimesdkmeetings-devel

%files         -n gem-aws-sdk-cloudwatchevents
%ruby_gemspecdir/aws-sdk-cloudwatchevents-1.59.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudwatchevents-1.59.0

%files         -n gem-aws-sdk-cloudwatchevents-doc
%ruby_gemsdocdir/aws-sdk-cloudwatchevents-1.59.0

%files         -n gem-aws-sdk-cloudwatchevents-devel

%files         -n gem-aws-sdk-codeguruprofiler
%ruby_gemspecdir/aws-sdk-codeguruprofiler-1.26.0.gemspec
%ruby_gemslibdir/aws-sdk-codeguruprofiler-1.26.0

%files         -n gem-aws-sdk-codeguruprofiler-doc
%ruby_gemsdocdir/aws-sdk-codeguruprofiler-1.26.0

%files         -n gem-aws-sdk-codeguruprofiler-devel

%files         -n gem-aws-sdk-codegurureviewer
%ruby_gemspecdir/aws-sdk-codegurureviewer-1.35.0.gemspec
%ruby_gemslibdir/aws-sdk-codegurureviewer-1.35.0

%files         -n gem-aws-sdk-codegurureviewer-doc
%ruby_gemsdocdir/aws-sdk-codegurureviewer-1.35.0

%files         -n gem-aws-sdk-codegurureviewer-devel

%files         -n gem-aws-sdk-computeoptimizer
%ruby_gemspecdir/aws-sdk-computeoptimizer-1.37.0.gemspec
%ruby_gemslibdir/aws-sdk-computeoptimizer-1.37.0

%files         -n gem-aws-sdk-computeoptimizer-doc
%ruby_gemsdocdir/aws-sdk-computeoptimizer-1.37.0

%files         -n gem-aws-sdk-computeoptimizer-devel

%files         -n gem-aws-sdk-customerprofiles
%ruby_gemspecdir/aws-sdk-customerprofiles-1.26.0.gemspec
%ruby_gemslibdir/aws-sdk-customerprofiles-1.26.0

%files         -n gem-aws-sdk-customerprofiles-doc
%ruby_gemsdocdir/aws-sdk-customerprofiles-1.26.0

%files         -n gem-aws-sdk-customerprofiles-devel

%files         -n gem-aws-sdk-directoryservice
%ruby_gemspecdir/aws-sdk-directoryservice-1.53.0.gemspec
%ruby_gemslibdir/aws-sdk-directoryservice-1.53.0

%files         -n gem-aws-sdk-directoryservice-doc
%ruby_gemsdocdir/aws-sdk-directoryservice-1.53.0

%files         -n gem-aws-sdk-directoryservice-devel

%files         -n gem-aws-sdk-elasticbeanstalk
%ruby_gemspecdir/aws-sdk-elasticbeanstalk-1.54.0.gemspec
%ruby_gemslibdir/aws-sdk-elasticbeanstalk-1.54.0

%files         -n gem-aws-sdk-elasticbeanstalk-doc
%ruby_gemsdocdir/aws-sdk-elasticbeanstalk-1.54.0

%files         -n gem-aws-sdk-elasticbeanstalk-devel

%files         -n gem-aws-sdk-elasticinference
%ruby_gemspecdir/aws-sdk-elasticinference-1.23.0.gemspec
%ruby_gemslibdir/aws-sdk-elasticinference-1.23.0

%files         -n gem-aws-sdk-elasticinference-doc
%ruby_gemsdocdir/aws-sdk-elasticinference-1.23.0

%files         -n gem-aws-sdk-elasticinference-devel

%files         -n gem-aws-sdk-iotdeviceadvisor
%ruby_gemspecdir/aws-sdk-iotdeviceadvisor-1.18.0.gemspec
%ruby_gemslibdir/aws-sdk-iotdeviceadvisor-1.18.0

%files         -n gem-aws-sdk-iotdeviceadvisor-doc
%ruby_gemsdocdir/aws-sdk-iotdeviceadvisor-1.18.0

%files         -n gem-aws-sdk-iotdeviceadvisor-devel

%files         -n gem-aws-sdk-iotjobsdataplane
%ruby_gemspecdir/aws-sdk-iotjobsdataplane-1.38.0.gemspec
%ruby_gemslibdir/aws-sdk-iotjobsdataplane-1.38.0

%files         -n gem-aws-sdk-iotjobsdataplane-doc
%ruby_gemsdocdir/aws-sdk-iotjobsdataplane-1.38.0

%files         -n gem-aws-sdk-iotjobsdataplane-devel

%files         -n gem-aws-sdk-kinesisanalytics
%ruby_gemspecdir/aws-sdk-kinesisanalytics-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesisanalytics-1.42.0

%files         -n gem-aws-sdk-kinesisanalytics-doc
%ruby_gemsdocdir/aws-sdk-kinesisanalytics-1.42.0

%files         -n gem-aws-sdk-kinesisanalytics-devel

%files         -n gem-aws-sdk-lookoutequipment
%ruby_gemspecdir/aws-sdk-lookoutequipment-1.16.0.gemspec
%ruby_gemslibdir/aws-sdk-lookoutequipment-1.16.0

%files         -n gem-aws-sdk-lookoutequipment-doc
%ruby_gemsdocdir/aws-sdk-lookoutequipment-1.16.0

%files         -n gem-aws-sdk-lookoutequipment-devel

%files         -n gem-aws-sdk-lookoutforvision
%ruby_gemspecdir/aws-sdk-lookoutforvision-1.19.0.gemspec
%ruby_gemslibdir/aws-sdk-lookoutforvision-1.19.0

%files         -n gem-aws-sdk-lookoutforvision-doc
%ruby_gemsdocdir/aws-sdk-lookoutforvision-1.19.0

%files         -n gem-aws-sdk-lookoutforvision-devel

%files         -n gem-aws-sdk-pinpointsmsvoice
%ruby_gemspecdir/aws-sdk-pinpointsmsvoice-1.34.0.gemspec
%ruby_gemslibdir/aws-sdk-pinpointsmsvoice-1.34.0

%files         -n gem-aws-sdk-pinpointsmsvoice-doc
%ruby_gemsdocdir/aws-sdk-pinpointsmsvoice-1.34.0

%files         -n gem-aws-sdk-pinpointsmsvoice-devel

%files         -n gem-aws-sdk-sagemakermetrics
%ruby_gemspecdir/aws-sdk-sagemakermetrics-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-sagemakermetrics-1.2.0

%files         -n gem-aws-sdk-sagemakermetrics-doc
%ruby_gemsdocdir/aws-sdk-sagemakermetrics-1.2.0

%files         -n gem-aws-sdk-sagemakermetrics-devel

%files         -n gem-aws-sdk-sagemakerruntime
%ruby_gemspecdir/aws-sdk-sagemakerruntime-1.46.0.gemspec
%ruby_gemslibdir/aws-sdk-sagemakerruntime-1.46.0

%files         -n gem-aws-sdk-sagemakerruntime-doc
%ruby_gemsdocdir/aws-sdk-sagemakerruntime-1.46.0

%files         -n gem-aws-sdk-sagemakerruntime-devel

%files         -n gem-aws-sdk-servicediscovery
%ruby_gemspecdir/aws-sdk-servicediscovery-1.49.0.gemspec
%ruby_gemslibdir/aws-sdk-servicediscovery-1.49.0

%files         -n gem-aws-sdk-servicediscovery-doc
%ruby_gemsdocdir/aws-sdk-servicediscovery-1.49.0

%files         -n gem-aws-sdk-servicediscovery-devel

%files         -n gem-aws-sdk-chimesdkmessaging
%ruby_gemspecdir/aws-sdk-chimesdkmessaging-1.15.0.gemspec
%ruby_gemslibdir/aws-sdk-chimesdkmessaging-1.15.0

%files         -n gem-aws-sdk-chimesdkmessaging-doc
%ruby_gemsdocdir/aws-sdk-chimesdkmessaging-1.15.0

%files         -n gem-aws-sdk-chimesdkmessaging-devel

%files         -n gem-aws-sdk-cloudsearchdomain
%ruby_gemspecdir/aws-sdk-cloudsearchdomain-1.34.1.gemspec
%ruby_gemslibdir/aws-sdk-cloudsearchdomain-1.34.1

%files         -n gem-aws-sdk-cloudsearchdomain-doc
%ruby_gemsdocdir/aws-sdk-cloudsearchdomain-1.34.1

%files         -n gem-aws-sdk-cloudsearchdomain-devel

%files         -n gem-aws-sdk-comprehendmedical
%ruby_gemspecdir/aws-sdk-comprehendmedical-1.39.0.gemspec
%ruby_gemslibdir/aws-sdk-comprehendmedical-1.39.0

%files         -n gem-aws-sdk-comprehendmedical-doc
%ruby_gemsdocdir/aws-sdk-comprehendmedical-1.39.0

%files         -n gem-aws-sdk-comprehendmedical-devel

%files         -n gem-aws-sdk-elastictranscoder
%ruby_gemspecdir/aws-sdk-elastictranscoder-1.40.0.gemspec
%ruby_gemslibdir/aws-sdk-elastictranscoder-1.40.0

%files         -n gem-aws-sdk-elastictranscoder-doc
%ruby_gemsdocdir/aws-sdk-elastictranscoder-1.40.0

%files         -n gem-aws-sdk-elastictranscoder-devel

%files         -n gem-aws-sdk-globalaccelerator
%ruby_gemspecdir/aws-sdk-globalaccelerator-1.43.0.gemspec
%ruby_gemslibdir/aws-sdk-globalaccelerator-1.43.0

%files         -n gem-aws-sdk-globalaccelerator-doc
%ruby_gemsdocdir/aws-sdk-globalaccelerator-1.43.0

%files         -n gem-aws-sdk-globalaccelerator-devel

%files         -n gem-aws-sdk-iot1clickprojects
%ruby_gemspecdir/aws-sdk-iot1clickprojects-1.39.0.gemspec
%ruby_gemslibdir/aws-sdk-iot1clickprojects-1.39.0

%files         -n gem-aws-sdk-iot1clickprojects-doc
%ruby_gemsdocdir/aws-sdk-iot1clickprojects-1.39.0

%files         -n gem-aws-sdk-iot1clickprojects-devel

%files         -n gem-aws-sdk-kinesisvideomedia
%ruby_gemspecdir/aws-sdk-kinesisvideomedia-1.39.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesisvideomedia-1.39.0

%files         -n gem-aws-sdk-kinesisvideomedia-doc
%ruby_gemsdocdir/aws-sdk-kinesisvideomedia-1.39.0

%files         -n gem-aws-sdk-kinesisvideomedia-devel

%files         -n gem-aws-sdk-managedblockchain
%ruby_gemspecdir/aws-sdk-managedblockchain-1.36.0.gemspec
%ruby_gemslibdir/aws-sdk-managedblockchain-1.36.0

%files         -n gem-aws-sdk-managedblockchain-doc
%ruby_gemsdocdir/aws-sdk-managedblockchain-1.36.0

%files         -n gem-aws-sdk-managedblockchain-devel

%files         -n gem-aws-sdk-opensearchservice
%ruby_gemspecdir/aws-sdk-opensearchservice-1.15.0.gemspec
%ruby_gemslibdir/aws-sdk-opensearchservice-1.15.0

%files         -n gem-aws-sdk-opensearchservice-doc
%ruby_gemsdocdir/aws-sdk-opensearchservice-1.15.0

%files         -n gem-aws-sdk-opensearchservice-devel

%files         -n gem-aws-sdk-personalizeevents
%ruby_gemspecdir/aws-sdk-personalizeevents-1.30.0.gemspec
%ruby_gemslibdir/aws-sdk-personalizeevents-1.30.0

%files         -n gem-aws-sdk-personalizeevents-doc
%ruby_gemsdocdir/aws-sdk-personalizeevents-1.30.0

%files         -n gem-aws-sdk-personalizeevents-devel

%files         -n gem-aws-sdk-prometheusservice
%ruby_gemspecdir/aws-sdk-prometheusservice-1.17.0.gemspec
%ruby_gemslibdir/aws-sdk-prometheusservice-1.17.0

%files         -n gem-aws-sdk-prometheusservice-doc
%ruby_gemsdocdir/aws-sdk-prometheusservice-1.17.0

%files         -n gem-aws-sdk-prometheusservice-devel

%files         -n gem-aws-sdk-resourceexplorer2
%ruby_gemspecdir/aws-sdk-resourceexplorer2-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-resourceexplorer2-1.3.0

%files         -n gem-aws-sdk-resourceexplorer2-doc
%ruby_gemsdocdir/aws-sdk-resourceexplorer2-1.3.0

%files         -n gem-aws-sdk-resourceexplorer2-devel

%files         -n gem-aws-sdk-transcribeservice
%ruby_gemspecdir/aws-sdk-transcribeservice-1.81.0.gemspec
%ruby_gemslibdir/aws-sdk-transcribeservice-1.81.0

%files         -n gem-aws-sdk-transcribeservice-doc
%ruby_gemsdocdir/aws-sdk-transcribeservice-1.81.0

%files         -n gem-aws-sdk-transcribeservice-devel

%files         -n gem-aws-sdk-augmentedairuntime
%ruby_gemspecdir/aws-sdk-augmentedairuntime-1.25.0.gemspec
%ruby_gemslibdir/aws-sdk-augmentedairuntime-1.25.0

%files         -n gem-aws-sdk-augmentedairuntime-doc
%ruby_gemsdocdir/aws-sdk-augmentedairuntime-1.25.0

%files         -n gem-aws-sdk-augmentedairuntime-devel

%files         -n gem-aws-sdk-connectcontactlens
%ruby_gemspecdir/aws-sdk-connectcontactlens-1.13.0.gemspec
%ruby_gemslibdir/aws-sdk-connectcontactlens-1.13.0

%files         -n gem-aws-sdk-connectcontactlens-doc
%ruby_gemsdocdir/aws-sdk-connectcontactlens-1.13.0

%files         -n gem-aws-sdk-connectcontactlens-devel

%files         -n gem-aws-sdk-connectparticipant
%ruby_gemspecdir/aws-sdk-connectparticipant-1.27.0.gemspec
%ruby_gemslibdir/aws-sdk-connectparticipant-1.27.0

%files         -n gem-aws-sdk-connectparticipant-doc
%ruby_gemsdocdir/aws-sdk-connectparticipant-1.27.0

%files         -n gem-aws-sdk-connectparticipant-devel

%files         -n gem-aws-sdk-ec2instanceconnect
%ruby_gemspecdir/aws-sdk-ec2instanceconnect-1.27.0.gemspec
%ruby_gemslibdir/aws-sdk-ec2instanceconnect-1.27.0

%files         -n gem-aws-sdk-ec2instanceconnect-doc
%ruby_gemsdocdir/aws-sdk-ec2instanceconnect-1.27.0

%files         -n gem-aws-sdk-ec2instanceconnect-devel

%files         -n gem-aws-sdk-iotsecuretunneling
%ruby_gemspecdir/aws-sdk-iotsecuretunneling-1.23.0.gemspec
%ruby_gemslibdir/aws-sdk-iotsecuretunneling-1.23.0

%files         -n gem-aws-sdk-iotsecuretunneling-doc
%ruby_gemsdocdir/aws-sdk-iotsecuretunneling-1.23.0

%files         -n gem-aws-sdk-iotsecuretunneling-devel

%files         -n gem-aws-sdk-kinesisanalyticsv2
%ruby_gemspecdir/aws-sdk-kinesisanalyticsv2-1.43.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesisanalyticsv2-1.43.0

%files         -n gem-aws-sdk-kinesisanalyticsv2-doc
%ruby_gemsdocdir/aws-sdk-kinesisanalyticsv2-1.43.0

%files         -n gem-aws-sdk-kinesisanalyticsv2-devel

%files         -n gem-aws-sdk-marketplacecatalog
%ruby_gemspecdir/aws-sdk-marketplacecatalog-1.25.0.gemspec
%ruby_gemslibdir/aws-sdk-marketplacecatalog-1.25.0

%files         -n gem-aws-sdk-marketplacecatalog-doc
%ruby_gemsdocdir/aws-sdk-marketplacecatalog-1.25.0

%files         -n gem-aws-sdk-marketplacecatalog-devel

%files         -n gem-aws-sdk-migrationhubconfig
%ruby_gemspecdir/aws-sdk-migrationhubconfig-1.22.0.gemspec
%ruby_gemslibdir/aws-sdk-migrationhubconfig-1.22.0

%files         -n gem-aws-sdk-migrationhubconfig-doc
%ruby_gemsdocdir/aws-sdk-migrationhubconfig-1.22.0

%files         -n gem-aws-sdk-migrationhubconfig-devel

%files         -n gem-aws-sdk-personalizeruntime
%ruby_gemspecdir/aws-sdk-personalizeruntime-1.35.0.gemspec
%ruby_gemslibdir/aws-sdk-personalizeruntime-1.35.0

%files         -n gem-aws-sdk-personalizeruntime-doc
%ruby_gemsdocdir/aws-sdk-personalizeruntime-1.35.0

%files         -n gem-aws-sdk-personalizeruntime-devel

%files         -n gem-aws-sdk-pinpointsmsvoicev2
%ruby_gemspecdir/aws-sdk-pinpointsmsvoicev2-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-pinpointsmsvoicev2-1.2.0

%files         -n gem-aws-sdk-pinpointsmsvoicev2-doc
%ruby_gemsdocdir/aws-sdk-pinpointsmsvoicev2-1.2.0

%files         -n gem-aws-sdk-pinpointsmsvoicev2-devel

%files         -n gem-aws-sdk-redshiftserverless
%ruby_gemspecdir/aws-sdk-redshiftserverless-1.7.0.gemspec
%ruby_gemslibdir/aws-sdk-redshiftserverless-1.7.0

%files         -n gem-aws-sdk-redshiftserverless-doc
%ruby_gemsdocdir/aws-sdk-redshiftserverless-1.7.0

%files         -n gem-aws-sdk-redshiftserverless-devel

%files         -n gem-aws-sdk-applicationinsights
%ruby_gemspecdir/aws-sdk-applicationinsights-1.33.0.gemspec
%ruby_gemslibdir/aws-sdk-applicationinsights-1.33.0

%files         -n gem-aws-sdk-applicationinsights-doc
%ruby_gemsdocdir/aws-sdk-applicationinsights-1.33.0

%files         -n gem-aws-sdk-applicationinsights-devel

%files         -n gem-aws-sdk-cloudwatchevidently
%ruby_gemspecdir/aws-sdk-cloudwatchevidently-1.10.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudwatchevidently-1.10.0

%files         -n gem-aws-sdk-cloudwatchevidently-doc
%ruby_gemsdocdir/aws-sdk-cloudwatchevidently-1.10.0

%files         -n gem-aws-sdk-cloudwatchevidently-devel

%files         -n gem-aws-sdk-codestarconnections
%ruby_gemspecdir/aws-sdk-codestarconnections-1.26.0.gemspec
%ruby_gemslibdir/aws-sdk-codestarconnections-1.26.0

%files         -n gem-aws-sdk-codestarconnections-doc
%ruby_gemsdocdir/aws-sdk-codestarconnections-1.26.0

%files         -n gem-aws-sdk-codestarconnections-devel

%files         -n gem-aws-sdk-marketplacemetering
%ruby_gemspecdir/aws-sdk-marketplacemetering-1.46.0.gemspec
%ruby_gemslibdir/aws-sdk-marketplacemetering-1.46.0

%files         -n gem-aws-sdk-marketplacemetering-doc
%ruby_gemsdocdir/aws-sdk-marketplacemetering-1.46.0

%files         -n gem-aws-sdk-marketplacemetering-devel

%files         -n gem-aws-sdk-sagemakergeospatial
%ruby_gemspecdir/aws-sdk-sagemakergeospatial-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-sagemakergeospatial-1.1.0

%files         -n gem-aws-sdk-sagemakergeospatial-doc
%ruby_gemsdocdir/aws-sdk-sagemakergeospatial-1.1.0

%files         -n gem-aws-sdk-sagemakergeospatial-devel

%files         -n gem-aws-sdk-workmailmessageflow
%ruby_gemspecdir/aws-sdk-workmailmessageflow-1.23.0.gemspec
%ruby_gemslibdir/aws-sdk-workmailmessageflow-1.23.0

%files         -n gem-aws-sdk-workmailmessageflow-doc
%ruby_gemsdocdir/aws-sdk-workmailmessageflow-1.23.0

%files         -n gem-aws-sdk-workmailmessageflow-devel

%files         -n gem-aws-sdk-connectwisdomservice
%ruby_gemspecdir/aws-sdk-connectwisdomservice-1.12.0.gemspec
%ruby_gemslibdir/aws-sdk-connectwisdomservice-1.12.0

%files         -n gem-aws-sdk-connectwisdomservice-doc
%ruby_gemsdocdir/aws-sdk-connectwisdomservice-1.12.0

%files         -n gem-aws-sdk-connectwisdomservice-devel

%files         -n gem-aws-sdk-elasticloadbalancing
%ruby_gemspecdir/aws-sdk-elasticloadbalancing-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-elasticloadbalancing-1.42.0

%files         -n gem-aws-sdk-elasticloadbalancing-doc
%ruby_gemsdocdir/aws-sdk-elasticloadbalancing-1.42.0

%files         -n gem-aws-sdk-elasticloadbalancing-devel

%files         -n gem-aws-sdk-elasticsearchservice
%ruby_gemspecdir/aws-sdk-elasticsearchservice-1.69.0.gemspec
%ruby_gemslibdir/aws-sdk-elasticsearchservice-1.69.0

%files         -n gem-aws-sdk-elasticsearchservice-doc
%ruby_gemsdocdir/aws-sdk-elasticsearchservice-1.69.0

%files         -n gem-aws-sdk-elasticsearchservice-devel

%files         -n gem-aws-sdk-forecastqueryservice
%ruby_gemspecdir/aws-sdk-forecastqueryservice-1.24.0.gemspec
%ruby_gemslibdir/aws-sdk-forecastqueryservice-1.24.0

%files         -n gem-aws-sdk-forecastqueryservice-doc
%ruby_gemsdocdir/aws-sdk-forecastqueryservice-1.24.0

%files         -n gem-aws-sdk-forecastqueryservice-devel

%files         -n gem-aws-sdk-opensearchserverless
%ruby_gemspecdir/aws-sdk-opensearchserverless-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-opensearchserverless-1.1.0

%files         -n gem-aws-sdk-opensearchserverless-doc
%ruby_gemsdocdir/aws-sdk-opensearchserverless-1.1.0

%files         -n gem-aws-sdk-opensearchserverless-devel

%files         -n gem-aws-sdk-sagemakeredgemanager
%ruby_gemspecdir/aws-sdk-sagemakeredgemanager-1.14.0.gemspec
%ruby_gemslibdir/aws-sdk-sagemakeredgemanager-1.14.0

%files         -n gem-aws-sdk-sagemakeredgemanager-doc
%ruby_gemsdocdir/aws-sdk-sagemakeredgemanager-1.14.0

%files         -n gem-aws-sdk-sagemakeredgemanager-devel

%files         -n gem-aws-sdk-snowdevicemanagement
%ruby_gemspecdir/aws-sdk-snowdevicemanagement-1.9.0.gemspec
%ruby_gemslibdir/aws-sdk-snowdevicemanagement-1.9.0

%files         -n gem-aws-sdk-snowdevicemanagement-doc
%ruby_gemsdocdir/aws-sdk-snowdevicemanagement-1.9.0

%files         -n gem-aws-sdk-snowdevicemanagement-devel

%files         -n gem-aws-sdk-code-generator
%ruby_gemspecdir/aws-sdk-code-generator-0.4.0.pre.gemspec
%ruby_gemslibdir/aws-sdk-code-generator-0.4.0.pre

%files         -n gem-aws-sdk-code-generator-doc
%ruby_gemsdocdir/aws-sdk-code-generator-0.4.0.pre

%files         -n gem-aws-sdk-code-generator-devel

%files         -n gem-aws-sdk-codestarnotifications
%ruby_gemspecdir/aws-sdk-codestarnotifications-1.22.0.gemspec
%ruby_gemslibdir/aws-sdk-codestarnotifications-1.22.0

%files         -n gem-aws-sdk-codestarnotifications-doc
%ruby_gemsdocdir/aws-sdk-codestarnotifications-1.22.0

%files         -n gem-aws-sdk-codestarnotifications-devel

%files         -n gem-aws-sdk-appintegrationsservice
%ruby_gemspecdir/aws-sdk-appintegrationsservice-1.15.0.gemspec
%ruby_gemslibdir/aws-sdk-appintegrationsservice-1.15.0

%files         -n gem-aws-sdk-appintegrationsservice-doc
%ruby_gemsdocdir/aws-sdk-appintegrationsservice-1.15.0

%files         -n gem-aws-sdk-appintegrationsservice-devel

%files         -n gem-aws-sdk-applicationautoscaling
%ruby_gemspecdir/aws-sdk-applicationautoscaling-1.66.0.gemspec
%ruby_gemslibdir/aws-sdk-applicationautoscaling-1.66.0

%files         -n gem-aws-sdk-applicationautoscaling-doc
%ruby_gemsdocdir/aws-sdk-applicationautoscaling-1.66.0

%files         -n gem-aws-sdk-applicationautoscaling-devel

%files         -n gem-aws-sdk-chimesdkmediapipelines
%ruby_gemspecdir/aws-sdk-chimesdkmediapipelines-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-chimesdkmediapipelines-1.3.0

%files         -n gem-aws-sdk-chimesdkmediapipelines-doc
%ruby_gemsdocdir/aws-sdk-chimesdkmediapipelines-1.3.0

%files         -n gem-aws-sdk-chimesdkmediapipelines-devel

%files         -n gem-aws-sdk-connectcampaignservice
%ruby_gemspecdir/aws-sdk-connectcampaignservice-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-connectcampaignservice-1.3.0

%files         -n gem-aws-sdk-connectcampaignservice-doc
%ruby_gemsdocdir/aws-sdk-connectcampaignservice-1.3.0

%files         -n gem-aws-sdk-connectcampaignservice-devel

%files         -n gem-aws-sdk-elasticloadbalancingv2
%ruby_gemspecdir/aws-sdk-elasticloadbalancingv2-1.83.0.gemspec
%ruby_gemslibdir/aws-sdk-elasticloadbalancingv2-1.83.0

%files         -n gem-aws-sdk-elasticloadbalancingv2-doc
%ruby_gemsdocdir/aws-sdk-elasticloadbalancingv2-1.83.0

%files         -n gem-aws-sdk-elasticloadbalancingv2-devel

%files         -n gem-aws-sdk-mainframemodernization
%ruby_gemspecdir/aws-sdk-mainframemodernization-1.4.0.gemspec
%ruby_gemslibdir/aws-sdk-mainframemodernization-1.4.0

%files         -n gem-aws-sdk-mainframemodernization-doc
%ruby_gemsdocdir/aws-sdk-mainframemodernization-1.4.0

%files         -n gem-aws-sdk-mainframemodernization-devel

%files         -n gem-aws-sdk-redshiftdataapiservice
%ruby_gemspecdir/aws-sdk-redshiftdataapiservice-1.24.0.gemspec
%ruby_gemslibdir/aws-sdk-redshiftdataapiservice-1.24.0

%files         -n gem-aws-sdk-redshiftdataapiservice-doc
%ruby_gemsdocdir/aws-sdk-redshiftdataapiservice-1.24.0

%files         -n gem-aws-sdk-redshiftdataapiservice-devel

%files         -n gem-aws-sdk-route53recoverycluster
%ruby_gemspecdir/aws-sdk-route53recoverycluster-1.13.0.gemspec
%ruby_gemslibdir/aws-sdk-route53recoverycluster-1.13.0

%files         -n gem-aws-sdk-route53recoverycluster-doc
%ruby_gemsdocdir/aws-sdk-route53recoverycluster-1.13.0

%files         -n gem-aws-sdk-route53recoverycluster-devel

%files         -n gem-aws-sdk-apigatewaymanagementapi
%ruby_gemspecdir/aws-sdk-apigatewaymanagementapi-1.32.0.gemspec
%ruby_gemslibdir/aws-sdk-apigatewaymanagementapi-1.32.0

%files         -n gem-aws-sdk-apigatewaymanagementapi-doc
%ruby_gemsdocdir/aws-sdk-apigatewaymanagementapi-1.32.0

%files         -n gem-aws-sdk-apigatewaymanagementapi-devel

%files         -n gem-aws-sdk-applicationcostprofiler
%ruby_gemspecdir/aws-sdk-applicationcostprofiler-1.11.0.gemspec
%ruby_gemslibdir/aws-sdk-applicationcostprofiler-1.11.0

%files         -n gem-aws-sdk-applicationcostprofiler-doc
%ruby_gemsdocdir/aws-sdk-applicationcostprofiler-1.11.0

%files         -n gem-aws-sdk-applicationcostprofiler-devel

%files         -n gem-aws-sdk-cognitoidentityprovider
%ruby_gemspecdir/aws-sdk-cognitoidentityprovider-1.73.0.gemspec
%ruby_gemslibdir/aws-sdk-cognitoidentityprovider-1.73.0

%files         -n gem-aws-sdk-cognitoidentityprovider-doc
%ruby_gemsdocdir/aws-sdk-cognitoidentityprovider-1.73.0

%files         -n gem-aws-sdk-cognitoidentityprovider-devel

%files         -n gem-aws-sdk-iot1clickdevicesservice
%ruby_gemspecdir/aws-sdk-iot1clickdevicesservice-1.39.0.gemspec
%ruby_gemslibdir/aws-sdk-iot1clickdevicesservice-1.39.0

%files         -n gem-aws-sdk-iot1clickdevicesservice-doc
%ruby_gemsdocdir/aws-sdk-iot1clickdevicesservice-1.39.0

%files         -n gem-aws-sdk-iot1clickdevicesservice-devel

%files         -n gem-aws-sdk-lexmodelbuildingservice
%ruby_gemspecdir/aws-sdk-lexmodelbuildingservice-1.59.0.gemspec
%ruby_gemslibdir/aws-sdk-lexmodelbuildingservice-1.59.0

%files         -n gem-aws-sdk-lexmodelbuildingservice-doc
%ruby_gemsdocdir/aws-sdk-lexmodelbuildingservice-1.59.0

%files         -n gem-aws-sdk-lexmodelbuildingservice-devel

%files         -n gem-aws-sdk-databasemigrationservice
%ruby_gemspecdir/aws-sdk-databasemigrationservice-1.75.0.gemspec
%ruby_gemslibdir/aws-sdk-databasemigrationservice-1.75.0

%files         -n gem-aws-sdk-databasemigrationservice-doc
%ruby_gemsdocdir/aws-sdk-databasemigrationservice-1.75.0

%files         -n gem-aws-sdk-databasemigrationservice-devel

%files         -n gem-aws-sdk-migrationhuborchestrator
%ruby_gemspecdir/aws-sdk-migrationhuborchestrator-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-migrationhuborchestrator-1.2.0

%files         -n gem-aws-sdk-migrationhuborchestrator-doc
%ruby_gemsdocdir/aws-sdk-migrationhuborchestrator-1.2.0

%files         -n gem-aws-sdk-migrationhuborchestrator-devel

%files         -n gem-aws-sdk-resourcegroupstaggingapi
%ruby_gemspecdir/aws-sdk-resourcegroupstaggingapi-1.49.0.gemspec
%ruby_gemslibdir/aws-sdk-resourcegroupstaggingapi-1.49.0

%files         -n gem-aws-sdk-resourcegroupstaggingapi-doc
%ruby_gemsdocdir/aws-sdk-resourcegroupstaggingapi-1.49.0

%files         -n gem-aws-sdk-resourcegroupstaggingapi-devel

%files         -n gem-aws-sdk-route53recoveryreadiness
%ruby_gemspecdir/aws-sdk-route53recoveryreadiness-1.12.0.gemspec
%ruby_gemslibdir/aws-sdk-route53recoveryreadiness-1.12.0

%files         -n gem-aws-sdk-route53recoveryreadiness-doc
%ruby_gemsdocdir/aws-sdk-route53recoveryreadiness-1.12.0

%files         -n gem-aws-sdk-route53recoveryreadiness-devel

%files         -n gem-aws-sdk-costandusagereportservice
%ruby_gemspecdir/aws-sdk-costandusagereportservice-1.43.0.gemspec
%ruby_gemslibdir/aws-sdk-costandusagereportservice-1.43.0

%files         -n gem-aws-sdk-costandusagereportservice-doc
%ruby_gemsdocdir/aws-sdk-costandusagereportservice-1.43.0

%files         -n gem-aws-sdk-costandusagereportservice-devel

%files         -n gem-aws-sdk-kinesisvideoarchivedmedia
%ruby_gemspecdir/aws-sdk-kinesisvideoarchivedmedia-1.46.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesisvideoarchivedmedia-1.46.0

%files         -n gem-aws-sdk-kinesisvideoarchivedmedia-doc
%ruby_gemsdocdir/aws-sdk-kinesisvideoarchivedmedia-1.46.0

%files         -n gem-aws-sdk-kinesisvideoarchivedmedia-devel

%files         -n gem-aws-sdk-kinesisvideowebrtcstorage
%ruby_gemspecdir/aws-sdk-kinesisvideowebrtcstorage-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesisvideowebrtcstorage-1.2.0

%files         -n gem-aws-sdk-kinesisvideowebrtcstorage-doc
%ruby_gemsdocdir/aws-sdk-kinesisvideowebrtcstorage-1.2.0

%files         -n gem-aws-sdk-kinesisvideowebrtcstorage-devel

%files         -n gem-aws-sdk-migrationhubrefactorspaces
%ruby_gemspecdir/aws-sdk-migrationhubrefactorspaces-1.10.0.gemspec
%ruby_gemslibdir/aws-sdk-migrationhubrefactorspaces-1.10.0

%files         -n gem-aws-sdk-migrationhubrefactorspaces-doc
%ruby_gemsdocdir/aws-sdk-migrationhubrefactorspaces-1.10.0

%files         -n gem-aws-sdk-migrationhubrefactorspaces-devel

%files         -n gem-aws-sdk-transcribestreamingservice
%ruby_gemspecdir/aws-sdk-transcribestreamingservice-1.46.0.gemspec
%ruby_gemslibdir/aws-sdk-transcribestreamingservice-1.46.0

%files         -n gem-aws-sdk-transcribestreamingservice-doc
%ruby_gemsdocdir/aws-sdk-transcribestreamingservice-1.46.0

%files         -n gem-aws-sdk-transcribestreamingservice-devel

%files         -n gem-aws-sdk-applicationdiscoveryservice
%ruby_gemspecdir/aws-sdk-applicationdiscoveryservice-1.48.0.gemspec
%ruby_gemslibdir/aws-sdk-applicationdiscoveryservice-1.48.0

%files         -n gem-aws-sdk-applicationdiscoveryservice-doc
%ruby_gemsdocdir/aws-sdk-applicationdiscoveryservice-1.48.0

%files         -n gem-aws-sdk-applicationdiscoveryservice-devel

%files         -n gem-aws-sdk-marketplacecommerceanalytics
%ruby_gemspecdir/aws-sdk-marketplacecommerceanalytics-1.43.0.gemspec
%ruby_gemslibdir/aws-sdk-marketplacecommerceanalytics-1.43.0

%files         -n gem-aws-sdk-marketplacecommerceanalytics-doc
%ruby_gemsdocdir/aws-sdk-marketplacecommerceanalytics-1.43.0

%files         -n gem-aws-sdk-marketplacecommerceanalytics-devel

%files         -n gem-aws-sdk-route53recoverycontrolconfig
%ruby_gemspecdir/aws-sdk-route53recoverycontrolconfig-1.13.0.gemspec
%ruby_gemslibdir/aws-sdk-route53recoverycontrolconfig-1.13.0

%files         -n gem-aws-sdk-route53recoverycontrolconfig-doc
%ruby_gemsdocdir/aws-sdk-route53recoverycontrolconfig-1.13.0

%files         -n gem-aws-sdk-route53recoverycontrolconfig-devel

%files         -n gem-aws-sdk-sagemakerfeaturestoreruntime
%ruby_gemspecdir/aws-sdk-sagemakerfeaturestoreruntime-1.15.0.gemspec
%ruby_gemslibdir/aws-sdk-sagemakerfeaturestoreruntime-1.15.0

%files         -n gem-aws-sdk-sagemakerfeaturestoreruntime-doc
%ruby_gemsdocdir/aws-sdk-sagemakerfeaturestoreruntime-1.15.0

%files         -n gem-aws-sdk-sagemakerfeaturestoreruntime-devel

%files         -n gem-aws-sdk-kinesisvideosignalingchannels
%ruby_gemspecdir/aws-sdk-kinesisvideosignalingchannels-1.21.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesisvideosignalingchannels-1.21.0

%files         -n gem-aws-sdk-kinesisvideosignalingchannels-doc
%ruby_gemsdocdir/aws-sdk-kinesisvideosignalingchannels-1.21.0

%files         -n gem-aws-sdk-kinesisvideosignalingchannels-devel

%files         -n gem-aws-sdk-marketplaceentitlementservice
%ruby_gemspecdir/aws-sdk-marketplaceentitlementservice-1.37.0.gemspec
%ruby_gemslibdir/aws-sdk-marketplaceentitlementservice-1.37.0

%files         -n gem-aws-sdk-marketplaceentitlementservice-doc
%ruby_gemsdocdir/aws-sdk-marketplaceentitlementservice-1.37.0

%files         -n gem-aws-sdk-marketplaceentitlementservice-devel

%files         -n gem-aws-sdk-licensemanagerusersubscriptions
%ruby_gemspecdir/aws-sdk-licensemanagerusersubscriptions-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-licensemanagerusersubscriptions-1.3.0

%files         -n gem-aws-sdk-licensemanagerusersubscriptions-doc
%ruby_gemsdocdir/aws-sdk-licensemanagerusersubscriptions-1.3.0

%files         -n gem-aws-sdk-licensemanagerusersubscriptions-devel

%files         -n gem-aws-sdk-serverlessapplicationrepository
%ruby_gemspecdir/aws-sdk-serverlessapplicationrepository-1.46.0.gemspec
%ruby_gemslibdir/aws-sdk-serverlessapplicationrepository-1.46.0

%files         -n gem-aws-sdk-serverlessapplicationrepository-doc
%ruby_gemsdocdir/aws-sdk-serverlessapplicationrepository-1.46.0

%files         -n gem-aws-sdk-serverlessapplicationrepository-devel

%files         -n gem-aws-sdk-licensemanagerlinuxsubscriptions
%ruby_gemspecdir/aws-sdk-licensemanagerlinuxsubscriptions-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-licensemanagerlinuxsubscriptions-1.1.0

%files         -n gem-aws-sdk-licensemanagerlinuxsubscriptions-doc
%ruby_gemsdocdir/aws-sdk-licensemanagerlinuxsubscriptions-1.1.0

%files         -n gem-aws-sdk-licensemanagerlinuxsubscriptions-devel

%files         -n gem-aws-sdk-migrationhubstrategyrecommendations
%ruby_gemspecdir/aws-sdk-migrationhubstrategyrecommendations-1.7.0.gemspec
%ruby_gemslibdir/aws-sdk-migrationhubstrategyrecommendations-1.7.0

%files         -n gem-aws-sdk-migrationhubstrategyrecommendations-doc
%ruby_gemsdocdir/aws-sdk-migrationhubstrategyrecommendations-1.7.0

%files         -n gem-aws-sdk-migrationhubstrategyrecommendations-devel

%files         -n gem-aws-sdk-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-3.1.0

%files         -n gem-aws-sdk-devel
%doc README.md


%changelog
* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 1:3.1.0-alt1
- ^ 20210608 -> 3.1.0 with epoch change

* Tue Jun 08 2021 Pavel Skrylev <majioa@altlinux.org> 20210608-alt1
- ^ 2.11.632 -> 20210608
- ^ -> version-3
- ! spec

* Sun Nov 22 2020 Pavel Skrylev <majioa@altlinux.org> 2.11.632-alt1
- ^ 2.11.478 -> 2.11.632

* Mon Mar 30 2020 Pavel Skrylev <majioa@altlinux.org> 2.11.478-alt1
- ^ 2.11.478 -> 2.11.478
- * moving code from %%_libdir -> %%_libexecdir

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 2.11.460-alt1
- updated (^) 2.11.354 -> 2.11.460
- fixed (!) spec

* Tue Sep 17 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.354-alt1
- updated (^) 2.11.351 -> 2.11.354
- added (+) obsoletes/provides on ruby-aws-sdk-code for gem-aws-sdk-code

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.351-alt1
- updated (^) 2.11.345 -> 2.11.351
- fixed (!) spec according to changelog rules

* Tue Sep 03 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.345-alt1
- updated (^) 2.11.317 -> 2.11.345
- fixed (!) spec
- added (+) obsoletes/provides for aws-sdk-core

* Wed Aug 07 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.317-alt1
- used (^) Ruby Policy 2.0
- updated (^) 2.11.262 -> 2.11.317

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 2.11.262-alt1
- New version.

* Mon Dec 10 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.188-alt1
- New version.

* Wed Dec 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.185-alt1
- New version.

* Tue Nov 20 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.174-alt1
- New version.

* Fri Oct 19 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.153-alt1
- New version.

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.142-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.132-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.130-alt1
- New version.

* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.83-alt1.1
- Rebuild for new Ruby autorequirements.

* Sat Jul 07 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.83-alt1
- New version.

* Fri Jun 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.78-alt1
- New version.

* Mon Jun 25 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.75-alt1
- New version.

* Fri Jun 22 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.74-alt1
- New version.

* Thu Jun 21 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.72-alt1
- New version.

* Sat Jun 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.70-alt1
- New version.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.69-alt1
- New version.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.68-alt1
- New version.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.67-alt1
- New version.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.65-alt1
- New version.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.64-alt1
- New version.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.63-alt1
- New version.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.62-alt1
- New version.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.61-alt1
- New version.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.58-alt1
- New version.

* Sat May 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.57-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.56-alt1
- New version.

* Wed May 23 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.55-alt1
- New version.

* Tue May 22 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.54-alt1
- New version.

* Sat May 19 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.53-alt1
- New version.

* Fri May 18 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.52-alt1
- New version.

* Thu May 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.51-alt1
- New version.

* Wed May 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.50-alt1
- New version.

* Tue May 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.49-alt1
- New version.

* Fri May 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.48-alt1
- New version.

* Thu May 10 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.46-alt1
- New version.

* Tue May 08 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.45-alt1
- New version.

* Tue May 08 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.44-alt1
- New version.

* Sat May 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.43-alt1
- New version.

* Fri May 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.42-alt1
- New version.

* Thu May 03 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.41-alt1
- New version.

* Tue May 01 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.40-alt1
- New version.

* Fri Apr 27 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.39-alt1
- New version.

* Wed Apr 25 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.37-alt1
- New version.

* Sun Apr 22 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.35-alt1
- New version.

* Wed Apr 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.33-alt1
- New version.

* Tue Apr 10 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.32-alt1
- New version.

* Mon Apr 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.31-alt1
- New version.

* Fri Apr 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.30-alt1
- New version.

* Thu Apr 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.29-alt1
- New version.

* Wed Apr 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.28-alt1
- New version.

* Tue Apr 03 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.27-alt1
- New version.

* Sun Apr 01 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.26-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.25-alt1
- New version.

* Thu Mar 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.24-alt1
- New version.

* Wed Mar 28 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.23-alt1
- New version.

* Tue Mar 27 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.22-alt1
- New version.

* Sat Mar 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.21-alt1
- New version.

* Fri Mar 23 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.20-alt1
- New version.

* Thu Mar 22 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.19-alt1
- New version.

* Wed Mar 21 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.18-alt1
- New version.

* Sat Mar 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.17-alt1
- New version.

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.16-alt1
- New version.

* Thu Mar 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.15-alt1
- New version.

* Wed Mar 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.14-alt1
- New version.

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.13-alt1
- New version.

* Fri Mar 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.12-alt1
- New version.

* Thu Mar 08 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.10-alt1
- New version.

* Wed Mar 07 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.9-alt1
- New version.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.8-alt1
- New version.

* Wed Feb 28 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.6-alt1
- New version.

* Tue Feb 27 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.5-alt1
- New version.

* Sat Feb 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.4-alt1
- New version.

* Fri Feb 23 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.3-alt1
- New version.

* Thu Feb 22 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1
- New version.

* Wed Feb 21 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.1-alt1
- New version.

* Mon Feb 19 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.134-alt1
- New version.

* Fri Feb 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.133-alt1
- New version.

* Thu Feb 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.132-alt1
- New version.

* Wed Feb 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.131-alt1
- New version.

* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.130-alt1
- New version.

* Mon Feb 12 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.129-alt1
- New version.

* Fri Feb 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.128-alt1
- New version.

* Thu Feb 08 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.127-alt1
- New version.

* Tue Feb 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.126-alt1
- New version.

* Mon Jan 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.125-alt1
- New version.

* Fri Jan 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.124-alt1
- New version.

* Wed Jan 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.123-alt1
- New version.

* Sun Jan 21 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.122-alt1
- New version.

* Thu Jan 18 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.121-alt1
- New version.

* Wed Jan 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.119-alt1
- New version.

* Tue Jan 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.118-alt1
- New version.

* Mon Jan 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.117-alt1
- New version.

* Thu Jan 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.115-alt1
- New version.

* Tue Jan 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.113-alt1
- New version.

* Thu Jan 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.111-alt1
- New version.

* Mon Jan 01 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.110-alt1
- New version.

* Sun Dec 24 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.109-alt1
- New version.

* Thu Dec 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.107-alt1
- New version.

* Wed Dec 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.106-alt1
- New version.

* Tue Dec 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.104-alt1
- New version.

* Fri Dec 15 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.103-alt1
- New version.

* Wed Dec 13 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.102-alt1
- New version.

* Sat Dec 09 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.100-alt1
- New version.

* Fri Dec 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.99-alt1
- New version.

* Thu Dec 07 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.98-alt1
- New version.

* Wed Dec 06 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.97-alt1
- New version.

* Tue Dec 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.96-alt1
- New version.

* Sat Dec 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.95-alt1
- New version.

* Tue Nov 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.90-alt1
- New version.

* Fri Nov 24 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.89-alt1
- New version.

* Wed Nov 22 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.88-alt1
- New version.

* Tue Nov 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.87-alt1
- New version.

* Sun Nov 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.86-alt1
- New version.

* Fri Nov 17 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.85-alt1
- New version.

* Thu Nov 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.84-alt1
- New version.

* Wed Nov 15 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.83-alt1
- New version.

* Fri Nov 10 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.82-alt1
- New version

* Thu Nov 09 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.81-alt1
- New version

* Wed Nov 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.80-alt1
- New version

* Tue Nov 07 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.79-alt1
- New version

* Sat Nov 04 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.78-alt1
- New version

* Fri Nov 03 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.77-alt1
- New version

* Thu Nov 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.76-alt1
- New version

* Fri Oct 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.74-alt1
- New version

* Wed Oct 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.71-alt1
- New version

* Tue Oct 24 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.70-alt1
- New version

* Sat Oct 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.69-alt1
- New version

* Fri Oct 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.68-alt1
- New version

* Thu Oct 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.67-alt1
- New version

* Wed Oct 18 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.66-alt1
- New version

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.65-alt1
- New version

* Fri Oct 13 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.64-alt1
- New version

* Wed Oct 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.62-alt1
- New version

* Sat Oct 07 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.61-alt1
- New version

* Fri Oct 06 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.59-alt1
- New version

* Thu Oct 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.58-alt1
- New version

* Wed Oct 04 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.57-alt1
- New version

* Tue Oct 03 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.56-alt1
- New version

* Sat Sep 30 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.55-alt1
- New version

* Thu Sep 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.54-alt1
- New version

* Wed Sep 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.53-alt1
- New version

* Sat Sep 23 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.52-alt1
- New version

* Thu Sep 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.50-alt1
- New version

* Wed Sep 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.49-alt1
- New version

* Tue Sep 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.48-alt1
- New version

* Sat Sep 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.47-alt1
- New version

* Fri Sep 15 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.46-alt1
- New version

* Thu Sep 14 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.45-alt1
- New version

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.44-alt1
- New version

* Thu Sep 07 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.40-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.38-alt1.1
- Rebuild with Ruby 2.4.1

* Sat Sep 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.38-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.37-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.21-alt1
- Initial build for Sisyphus
