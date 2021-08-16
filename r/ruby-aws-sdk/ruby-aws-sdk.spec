Name:          ruby-aws-sdk
Version:       20210608
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
BuildRequires: gem(kramdown) >= 0 gem(kramdown) < 3
BuildRequires: gem(mustache) >= 0
BuildRequires: gem(jmespath) >= 1.0 gem(jmespath) < 2
BuildRequires: gem(nokogiri) >= 1.10
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(oga) >= 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
%ruby_use_gem_dependency mustache >= 0.99.8,mustache < 2


%description
The official AWS SDK for Ruby. Provides both resource oriented interfaces and
API clients for AWS services.


%package       -n gem-aws-sdk-code-generator
Version:       0.2.3.pre
Release:       alt1
Summary:       AWS SDK for Ruby - Code Generator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(kramdown) >= 0 gem(kramdown) < 3
Requires:      gem(mustache) >= 0
Provides:      gem(aws-sdk-code-generator) = 0.2.3.pre

%description   -n gem-aws-sdk-code-generator
Generates the service code for the AWS SDK for Ruby


%package       -n gem-aws-sdk-code-generator-doc
Version:       0.2.3.pre
Release:       alt1
Summary:       AWS SDK for Ruby - Code Generator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-code-generator
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-code-generator) = 0.2.3.pre

%description   -n gem-aws-sdk-code-generator-doc
AWS SDK for Ruby - Code Generator documentation files.

Generates the service code for the AWS SDK for Ruby

%description   -n gem-aws-sdk-code-generator-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-code-generator.


%package       -n gem-aws-sdk-code-generator-devel
Version:       0.2.3.pre
Release:       alt1
Summary:       AWS SDK for Ruby - Code Generator development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-code-generator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-code-generator) = 0.2.3.pre
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-code-generator-devel
AWS SDK for Ruby - Code Generator development package.

Generates the service code for the AWS SDK for Ruby

%description   -n gem-aws-sdk-code-generator-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-code-generator.


%package       -n gem-aws-sdk-s3outposts
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon S3 Outposts
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-s3outposts) = 1.2.0

%description   -n gem-aws-sdk-s3outposts
Official AWS Ruby gem for Amazon S3 on Outposts (Amazon S3 Outposts). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-s3outposts-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon S3 Outposts documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-s3outposts
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-s3outposts) = 1.2.0

%description   -n gem-aws-sdk-s3outposts-doc
AWS SDK for Ruby - Amazon S3 Outposts documentation files.

Official AWS Ruby gem for Amazon S3 on Outposts (Amazon S3 Outposts). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-s3outposts-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-s3outposts.


%package       -n gem-aws-sdk-s3outposts-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon S3 Outposts development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-s3outposts
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-s3outposts) = 1.2.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-s3outposts-devel
AWS SDK for Ruby - Amazon S3 Outposts development package.

Official AWS Ruby gem for Amazon S3 on Outposts (Amazon S3 Outposts). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-s3outposts-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-s3outposts.


%package       -n gem-aws-sdk-elasticloadbalancing
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Elastic Load Balancing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-elasticloadbalancing) = 1.31.0

%description   -n gem-aws-sdk-elasticloadbalancing
Official AWS Ruby gem for Elastic Load Balancing. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-elasticloadbalancing-doc
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Elastic Load Balancing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-elasticloadbalancing
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticloadbalancing) = 1.31.0

%description   -n gem-aws-sdk-elasticloadbalancing-doc
AWS SDK for Ruby - Elastic Load Balancing documentation files.

Official AWS Ruby gem for Elastic Load Balancing. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-elasticloadbalancing-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-elasticloadbalancing.


%package       -n gem-aws-sdk-elasticloadbalancing-devel
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Elastic Load Balancing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-elasticloadbalancing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticloadbalancing) = 1.31.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-elasticloadbalancing-devel
AWS SDK for Ruby - Elastic Load Balancing development package.

Official AWS Ruby gem for Elastic Load Balancing. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-elasticloadbalancing-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-elasticloadbalancing.


%package       -n gem-aws-sdk-swf
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SWF
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-swf) = 1.27.0

%description   -n gem-aws-sdk-swf
Official AWS Ruby gem for Amazon Simple Workflow Service (Amazon SWF). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-swf-doc
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SWF documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-swf
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-swf) = 1.27.0

%description   -n gem-aws-sdk-swf-doc
AWS SDK for Ruby - Amazon SWF documentation files.

Official AWS Ruby gem for Amazon Simple Workflow Service (Amazon SWF). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-swf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-swf.


%package       -n gem-aws-sdk-swf-devel
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SWF development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-swf
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-swf) = 1.27.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-swf-devel
AWS SDK for Ruby - Amazon SWF development package.

Official AWS Ruby gem for Amazon Simple Workflow Service (Amazon SWF). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-swf-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-swf.


%package       -n gem-aws-sdk-alexaforbusiness
Version:       1.47.0
Release:       alt1
Summary:       AWS SDK for Ruby - Alexa For Business
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-alexaforbusiness) = 1.47.0

%description   -n gem-aws-sdk-alexaforbusiness
Official AWS Ruby gem for Alexa For Business. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-alexaforbusiness-doc
Version:       1.47.0
Release:       alt1
Summary:       AWS SDK for Ruby - Alexa For Business documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-alexaforbusiness
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-alexaforbusiness) = 1.47.0

%description   -n gem-aws-sdk-alexaforbusiness-doc
AWS SDK for Ruby - Alexa For Business documentation files.

Official AWS Ruby gem for Alexa For Business. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-alexaforbusiness-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-alexaforbusiness.


%package       -n gem-aws-sdk-alexaforbusiness-devel
Version:       1.47.0
Release:       alt1
Summary:       AWS SDK for Ruby - Alexa For Business development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-alexaforbusiness
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-alexaforbusiness) = 1.47.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-alexaforbusiness-devel
AWS SDK for Ruby - Alexa For Business development package.

Official AWS Ruby gem for Alexa For Business. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-alexaforbusiness-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-alexaforbusiness.


%package       -n gem-aws-sdk-ecrpublic
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon ECR Public
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-ecrpublic) = 1.3.0

%description   -n gem-aws-sdk-ecrpublic
Official AWS Ruby gem for Amazon Elastic Container Registry Public (Amazon ECR
Public). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ecrpublic-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon ECR Public documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ecrpublic
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ecrpublic) = 1.3.0

%description   -n gem-aws-sdk-ecrpublic-doc
AWS SDK for Ruby - Amazon ECR Public documentation files.

Official AWS Ruby gem for Amazon Elastic Container Registry Public (Amazon ECR
Public). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ecrpublic-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ecrpublic.


%package       -n gem-aws-sdk-ecrpublic-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon ECR Public development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ecrpublic
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ecrpublic) = 1.3.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ecrpublic-devel
AWS SDK for Ruby - Amazon ECR Public development package.

Official AWS Ruby gem for Amazon Elastic Container Registry Public (Amazon ECR
Public). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ecrpublic-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ecrpublic.


%package       -n gem-aws-sdk-route53resolver
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - Route53Resolver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-route53resolver) = 1.26.0

%description   -n gem-aws-sdk-route53resolver
Official AWS Ruby gem for Amazon Route 53 Resolver (Route53Resolver). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-route53resolver-doc
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - Route53Resolver documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-route53resolver
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-route53resolver) = 1.26.0

%description   -n gem-aws-sdk-route53resolver-doc
AWS SDK for Ruby - Route53Resolver documentation files.

Official AWS Ruby gem for Amazon Route 53 Resolver (Route53Resolver). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-route53resolver-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-route53resolver.


%package       -n gem-aws-sdk-route53resolver-devel
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - Route53Resolver development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-route53resolver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-route53resolver) = 1.26.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-route53resolver-devel
AWS SDK for Ruby - Route53Resolver development package.

Official AWS Ruby gem for Amazon Route 53 Resolver (Route53Resolver). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-route53resolver-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-route53resolver.


%package       -n gem-aws-sdk-ssmcontacts
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - SSM Contacts
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-ssmcontacts) = 1.0.0

%description   -n gem-aws-sdk-ssmcontacts
Official AWS Ruby gem for AWS Systems Manager Incident Manager Contacts (SSM
Contacts). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ssmcontacts-doc
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - SSM Contacts documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ssmcontacts
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ssmcontacts) = 1.0.0

%description   -n gem-aws-sdk-ssmcontacts-doc
AWS SDK for Ruby - SSM Contacts documentation files.

Official AWS Ruby gem for AWS Systems Manager Incident Manager Contacts (SSM
Contacts). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssmcontacts-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ssmcontacts.


%package       -n gem-aws-sdk-ssmcontacts-devel
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - SSM Contacts development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ssmcontacts
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ssmcontacts) = 1.0.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ssmcontacts-devel
AWS SDK for Ruby - SSM Contacts development package.

Official AWS Ruby gem for AWS Systems Manager Incident Manager Contacts (SSM
Contacts). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssmcontacts-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ssmcontacts.


%package       -n gem-aws-sdk-eventbridge
Version:       1.24.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EventBridge
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-eventbridge) = 1.24.0

%description   -n gem-aws-sdk-eventbridge
Official AWS Ruby gem for Amazon EventBridge. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-eventbridge-doc
Version:       1.24.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EventBridge documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-eventbridge
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-eventbridge) = 1.24.0

%description   -n gem-aws-sdk-eventbridge-doc
AWS SDK for Ruby - Amazon EventBridge documentation files.

Official AWS Ruby gem for Amazon EventBridge. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-eventbridge-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-eventbridge.


%package       -n gem-aws-sdk-eventbridge-devel
Version:       1.24.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EventBridge development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-eventbridge
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-eventbridge) = 1.24.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-eventbridge-devel
AWS SDK for Ruby - Amazon EventBridge development package.

Official AWS Ruby gem for Amazon EventBridge. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-eventbridge-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-eventbridge.


%package       -n gem-aws-sdk-wellarchitected
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Well-Architected
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-wellarchitected) = 1.4.0

%description   -n gem-aws-sdk-wellarchitected
Official AWS Ruby gem for AWS Well-Architected Tool (Well-Architected). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-wellarchitected-doc
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Well-Architected documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-wellarchitected
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-wellarchitected) = 1.4.0

%description   -n gem-aws-sdk-wellarchitected-doc
AWS SDK for Ruby - Well-Architected documentation files.

Official AWS Ruby gem for AWS Well-Architected Tool (Well-Architected). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-wellarchitected-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-wellarchitected.


%package       -n gem-aws-sdk-wellarchitected-devel
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Well-Architected development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-wellarchitected
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-wellarchitected) = 1.4.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-wellarchitected-devel
AWS SDK for Ruby - Well-Architected development package.

Official AWS Ruby gem for AWS Well-Architected Tool (Well-Architected). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-wellarchitected-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-wellarchitected.


%package       -n gem-aws-sdk-appregistry
Version:       1.5.0
Release:       alt1
Summary:       AWS SDK for Ruby - AppRegistry
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-appregistry) = 1.5.0

%description   -n gem-aws-sdk-appregistry
Official AWS Ruby gem for AWS Service Catalog App Registry (AppRegistry). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-appregistry-doc
Version:       1.5.0
Release:       alt1
Summary:       AWS SDK for Ruby - AppRegistry documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appregistry
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appregistry) = 1.5.0

%description   -n gem-aws-sdk-appregistry-doc
AWS SDK for Ruby - AppRegistry documentation files.

Official AWS Ruby gem for AWS Service Catalog App Registry (AppRegistry). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-appregistry-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appregistry.


%package       -n gem-aws-sdk-appregistry-devel
Version:       1.5.0
Release:       alt1
Summary:       AWS SDK for Ruby - AppRegistry development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appregistry
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appregistry) = 1.5.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-appregistry-devel
AWS SDK for Ruby - AppRegistry development package.

Official AWS Ruby gem for AWS Service Catalog App Registry (AppRegistry). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-appregistry-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appregistry.


%package       -n gem-aws-sdk-networkfirewall
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Network Firewall
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-networkfirewall) = 1.4.0

%description   -n gem-aws-sdk-networkfirewall
Official AWS Ruby gem for AWS Network Firewall (Network Firewall). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-networkfirewall-doc
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Network Firewall documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-networkfirewall
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-networkfirewall) = 1.4.0

%description   -n gem-aws-sdk-networkfirewall-doc
AWS SDK for Ruby - Network Firewall documentation files.

Official AWS Ruby gem for AWS Network Firewall (Network Firewall). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-networkfirewall-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-networkfirewall.


%package       -n gem-aws-sdk-networkfirewall-devel
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Network Firewall development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-networkfirewall
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-networkfirewall) = 1.4.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-networkfirewall-devel
AWS SDK for Ruby - Network Firewall development package.

Official AWS Ruby gem for AWS Network Firewall (Network Firewall). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-networkfirewall-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-networkfirewall.


%package       -n gem-aws-sdk-codebuild
Version:       1.72.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS CodeBuild
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-codebuild) = 1.72.0

%description   -n gem-aws-sdk-codebuild
Official AWS Ruby gem for AWS CodeBuild. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-codebuild-doc
Version:       1.72.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS CodeBuild documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codebuild
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codebuild) = 1.72.0

%description   -n gem-aws-sdk-codebuild-doc
AWS SDK for Ruby - AWS CodeBuild documentation files.

Official AWS Ruby gem for AWS CodeBuild. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-codebuild-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codebuild.


%package       -n gem-aws-sdk-codebuild-devel
Version:       1.72.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS CodeBuild development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codebuild
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codebuild) = 1.72.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-codebuild-devel
AWS SDK for Ruby - AWS CodeBuild development package.

Official AWS Ruby gem for AWS CodeBuild. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-codebuild-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codebuild.


%package       -n gem-aws-sdk-marketplacecommerceanalytics
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Marketplace Commerce Analytics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-marketplacecommerceanalytics) = 1.32.0

%description   -n gem-aws-sdk-marketplacecommerceanalytics
Official AWS Ruby gem for AWS Marketplace Commerce Analytics. This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-marketplacecommerceanalytics-doc
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Marketplace Commerce Analytics documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-marketplacecommerceanalytics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplacecommerceanalytics) = 1.32.0

%description   -n gem-aws-sdk-marketplacecommerceanalytics-doc
AWS SDK for Ruby - AWS Marketplace Commerce Analytics documentation
files.

Official AWS Ruby gem for AWS Marketplace Commerce Analytics. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-marketplacecommerceanalytics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-marketplacecommerceanalytics.


%package       -n gem-aws-sdk-marketplacecommerceanalytics-devel
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Marketplace Commerce Analytics development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-marketplacecommerceanalytics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplacecommerceanalytics) = 1.32.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-marketplacecommerceanalytics-devel
AWS SDK for Ruby - AWS Marketplace Commerce Analytics development
package.

Official AWS Ruby gem for AWS Marketplace Commerce Analytics. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-marketplacecommerceanalytics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-marketplacecommerceanalytics.


%package       -n gem-aws-sdk-personalize
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Personalize
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-personalize) = 1.27.0

%description   -n gem-aws-sdk-personalize
Official AWS Ruby gem for Amazon Personalize. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-personalize-doc
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Personalize documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-personalize
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-personalize) = 1.27.0

%description   -n gem-aws-sdk-personalize-doc
AWS SDK for Ruby - Amazon Personalize documentation files.

Official AWS Ruby gem for Amazon Personalize. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-personalize-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-personalize.


%package       -n gem-aws-sdk-personalize-devel
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Personalize development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-personalize
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-personalize) = 1.27.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-personalize-devel
AWS SDK for Ruby - Amazon Personalize development package.

Official AWS Ruby gem for Amazon Personalize. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-personalize-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-personalize.


%package       -n gem-aws-sdk-lookoutequipment
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - LookoutEquipment
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-lookoutequipment) = 1.0.0

%description   -n gem-aws-sdk-lookoutequipment
Official AWS Ruby gem for Amazon Lookout for Equipment (LookoutEquipment). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-lookoutequipment-doc
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - LookoutEquipment documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lookoutequipment
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lookoutequipment) = 1.0.0

%description   -n gem-aws-sdk-lookoutequipment-doc
AWS SDK for Ruby - LookoutEquipment documentation files.

Official AWS Ruby gem for Amazon Lookout for Equipment (LookoutEquipment). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lookoutequipment-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lookoutequipment.


%package       -n gem-aws-sdk-lookoutequipment-devel
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - LookoutEquipment development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lookoutequipment
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lookoutequipment) = 1.0.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-lookoutequipment-devel
AWS SDK for Ruby - LookoutEquipment development package.

Official AWS Ruby gem for Amazon Lookout for Equipment (LookoutEquipment). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lookoutequipment-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lookoutequipment.


%package       -n gem-aws-sdk-rdsdataservice
Version:       1.25.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS RDS DataService
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-rdsdataservice) = 1.25.0

%description   -n gem-aws-sdk-rdsdataservice
Official AWS Ruby gem for AWS RDS DataService. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-rdsdataservice-doc
Version:       1.25.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS RDS DataService documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-rdsdataservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-rdsdataservice) = 1.25.0

%description   -n gem-aws-sdk-rdsdataservice-doc
AWS SDK for Ruby - AWS RDS DataService documentation files.

Official AWS Ruby gem for AWS RDS DataService. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-rdsdataservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-rdsdataservice.


%package       -n gem-aws-sdk-rdsdataservice-devel
Version:       1.25.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS RDS DataService development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-rdsdataservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-rdsdataservice) = 1.25.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-rdsdataservice-devel
AWS SDK for Ruby - AWS RDS DataService development package.

Official AWS Ruby gem for AWS RDS DataService. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-rdsdataservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-rdsdataservice.


%package       -n gem-aws-sdk-accessanalyzer
Version:       1.19.0
Release:       alt1
Summary:       AWS SDK for Ruby - Access Analyzer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-accessanalyzer) = 1.19.0

%description   -n gem-aws-sdk-accessanalyzer
Official AWS Ruby gem for Access Analyzer. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-accessanalyzer-doc
Version:       1.19.0
Release:       alt1
Summary:       AWS SDK for Ruby - Access Analyzer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-accessanalyzer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-accessanalyzer) = 1.19.0

%description   -n gem-aws-sdk-accessanalyzer-doc
AWS SDK for Ruby - Access Analyzer documentation files.

Official AWS Ruby gem for Access Analyzer. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-accessanalyzer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-accessanalyzer.


%package       -n gem-aws-sdk-accessanalyzer-devel
Version:       1.19.0
Release:       alt1
Summary:       AWS SDK for Ruby - Access Analyzer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-accessanalyzer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-accessanalyzer) = 1.19.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-accessanalyzer-devel
AWS SDK for Ruby - Access Analyzer development package.

Official AWS Ruby gem for Access Analyzer. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-accessanalyzer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-accessanalyzer.


%package       -n gem-aws-sdk-codestarnotifications
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS CodeStar Notifications
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-codestarnotifications) = 1.10.0

%description   -n gem-aws-sdk-codestarnotifications
Official AWS Ruby gem for AWS CodeStar Notifications. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-codestarnotifications-doc
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS CodeStar Notifications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codestarnotifications
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codestarnotifications) = 1.10.0

%description   -n gem-aws-sdk-codestarnotifications-doc
AWS SDK for Ruby - AWS CodeStar Notifications documentation files.

Official AWS Ruby gem for AWS CodeStar Notifications. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-codestarnotifications-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codestarnotifications.


%package       -n gem-aws-sdk-codestarnotifications-devel
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS CodeStar Notifications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codestarnotifications
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codestarnotifications) = 1.10.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-codestarnotifications-devel
AWS SDK for Ruby - AWS CodeStar Notifications development package.

Official AWS Ruby gem for AWS CodeStar Notifications. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-codestarnotifications-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codestarnotifications.


%package       -n gem-aws-sdk-fis
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - FIS
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-fis) = 1.1.0

%description   -n gem-aws-sdk-fis
Official AWS Ruby gem for AWS Fault Injection Simulator (FIS). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-fis-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - FIS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-fis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-fis) = 1.1.0

%description   -n gem-aws-sdk-fis-doc
AWS SDK for Ruby - FIS documentation files.

Official AWS Ruby gem for AWS Fault Injection Simulator (FIS). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-fis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-fis.


%package       -n gem-aws-sdk-fis-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - FIS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-fis
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-fis) = 1.1.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-fis-devel
AWS SDK for Ruby - FIS development package.

Official AWS Ruby gem for AWS Fault Injection Simulator (FIS). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-fis-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-fis.


%package       -n gem-aws-sdk-firehose
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Firehose
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-firehose) = 1.37.0

%description   -n gem-aws-sdk-firehose
Official AWS Ruby gem for Amazon Kinesis Firehose (Firehose). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-firehose-doc
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Firehose documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-firehose
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-firehose) = 1.37.0

%description   -n gem-aws-sdk-firehose-doc
AWS SDK for Ruby - Firehose documentation files.

Official AWS Ruby gem for Amazon Kinesis Firehose (Firehose). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-firehose-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-firehose.


%package       -n gem-aws-sdk-firehose-devel
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Firehose development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-firehose
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-firehose) = 1.37.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-firehose-devel
AWS SDK for Ruby - Firehose development package.

Official AWS Ruby gem for Amazon Kinesis Firehose (Firehose). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-firehose-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-firehose.


%package       -n gem-aws-sdk-pinpointsmsvoice
Version:       1.23.0
Release:       alt1
Summary:       AWS SDK for Ruby - Pinpoint SMS Voice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-pinpointsmsvoice) = 1.23.0

%description   -n gem-aws-sdk-pinpointsmsvoice
Official AWS Ruby gem for Amazon Pinpoint SMS and Voice Service (Pinpoint SMS
Voice). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-pinpointsmsvoice-doc
Version:       1.23.0
Release:       alt1
Summary:       AWS SDK for Ruby - Pinpoint SMS Voice documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-pinpointsmsvoice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-pinpointsmsvoice) = 1.23.0

%description   -n gem-aws-sdk-pinpointsmsvoice-doc
AWS SDK for Ruby - Pinpoint SMS Voice documentation files.

Official AWS Ruby gem for Amazon Pinpoint SMS and Voice Service (Pinpoint SMS
Voice). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pinpointsmsvoice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-pinpointsmsvoice.


%package       -n gem-aws-sdk-pinpointsmsvoice-devel
Version:       1.23.0
Release:       alt1
Summary:       AWS SDK for Ruby - Pinpoint SMS Voice development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-pinpointsmsvoice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-pinpointsmsvoice) = 1.23.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-pinpointsmsvoice-devel
AWS SDK for Ruby - Pinpoint SMS Voice development package.

Official AWS Ruby gem for Amazon Pinpoint SMS and Voice Service (Pinpoint SMS
Voice). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pinpointsmsvoice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-pinpointsmsvoice.


%package       -n gem-aws-sdk-codecommit
Version:       1.42.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeCommit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-codecommit) = 1.42.0

%description   -n gem-aws-sdk-codecommit
Official AWS Ruby gem for AWS CodeCommit (CodeCommit). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-codecommit-doc
Version:       1.42.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeCommit documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codecommit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codecommit) = 1.42.0

%description   -n gem-aws-sdk-codecommit-doc
AWS SDK for Ruby - CodeCommit documentation files.

Official AWS Ruby gem for AWS CodeCommit (CodeCommit). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-codecommit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codecommit.


%package       -n gem-aws-sdk-codecommit-devel
Version:       1.42.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeCommit development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codecommit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codecommit) = 1.42.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-codecommit-devel
AWS SDK for Ruby - CodeCommit development package.

Official AWS Ruby gem for AWS CodeCommit (CodeCommit). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-codecommit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codecommit.


%package       -n gem-aws-sdk-lookoutmetrics
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - LookoutMetrics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-lookoutmetrics) = 1.3.0

%description   -n gem-aws-sdk-lookoutmetrics
Official AWS Ruby gem for Amazon Lookout for Metrics (LookoutMetrics). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-lookoutmetrics-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - LookoutMetrics documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lookoutmetrics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lookoutmetrics) = 1.3.0

%description   -n gem-aws-sdk-lookoutmetrics-doc
AWS SDK for Ruby - LookoutMetrics documentation files.

Official AWS Ruby gem for Amazon Lookout for Metrics (LookoutMetrics). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lookoutmetrics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lookoutmetrics.


%package       -n gem-aws-sdk-lookoutmetrics-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - LookoutMetrics development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lookoutmetrics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lookoutmetrics) = 1.3.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-lookoutmetrics-devel
AWS SDK for Ruby - LookoutMetrics development package.

Official AWS Ruby gem for Amazon Lookout for Metrics (LookoutMetrics). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lookoutmetrics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lookoutmetrics.


%package       -n gem-aws-sdk-customerprofiles
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - Customer Profiles
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-customerprofiles) = 1.7.0

%description   -n gem-aws-sdk-customerprofiles
Official AWS Ruby gem for Amazon Connect Customer Profiles (Customer Profiles).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-customerprofiles-doc
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - Customer Profiles documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-customerprofiles
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-customerprofiles) = 1.7.0

%description   -n gem-aws-sdk-customerprofiles-doc
AWS SDK for Ruby - Customer Profiles documentation files.

Official AWS Ruby gem for Amazon Connect Customer Profiles (Customer Profiles).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-customerprofiles-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-customerprofiles.


%package       -n gem-aws-sdk-customerprofiles-devel
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - Customer Profiles development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-customerprofiles
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-customerprofiles) = 1.7.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-customerprofiles-devel
AWS SDK for Ruby - Customer Profiles development package.

Official AWS Ruby gem for Amazon Connect Customer Profiles (Customer Profiles).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-customerprofiles-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-customerprofiles.


%package       -n gem-aws-sdk-ssoadmin
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - SSO Admin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-ssoadmin) = 1.7.0

%description   -n gem-aws-sdk-ssoadmin
Official AWS Ruby gem for AWS Single Sign-On Admin (SSO Admin). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ssoadmin-doc
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - SSO Admin documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ssoadmin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ssoadmin) = 1.7.0

%description   -n gem-aws-sdk-ssoadmin-doc
AWS SDK for Ruby - SSO Admin documentation files.

Official AWS Ruby gem for AWS Single Sign-On Admin (SSO Admin). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssoadmin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ssoadmin.


%package       -n gem-aws-sdk-ssoadmin-devel
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - SSO Admin development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ssoadmin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ssoadmin) = 1.7.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ssoadmin-devel
AWS SDK for Ruby - SSO Admin development package.

Official AWS Ruby gem for AWS Single Sign-On Admin (SSO Admin). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssoadmin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ssoadmin.


%package       -n gem-aws-sdk-wafregional
Version:       1.39.0
Release:       alt1
Summary:       AWS SDK for Ruby - WAF Regional
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-wafregional) = 1.39.0

%description   -n gem-aws-sdk-wafregional
Official AWS Ruby gem for AWS WAF Regional (WAF Regional). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-wafregional-doc
Version:       1.39.0
Release:       alt1
Summary:       AWS SDK for Ruby - WAF Regional documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-wafregional
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-wafregional) = 1.39.0

%description   -n gem-aws-sdk-wafregional-doc
AWS SDK for Ruby - WAF Regional documentation files.

Official AWS Ruby gem for AWS WAF Regional (WAF Regional). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-wafregional-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-wafregional.


%package       -n gem-aws-sdk-wafregional-devel
Version:       1.39.0
Release:       alt1
Summary:       AWS SDK for Ruby - WAF Regional development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-wafregional
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-wafregional) = 1.39.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-wafregional-devel
AWS SDK for Ruby - WAF Regional development package.

Official AWS Ruby gem for AWS WAF Regional (WAF Regional). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-wafregional-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-wafregional.


%package       -n gem-aws-sdk-mediaconvert
Version:       1.67.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaConvert
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-mediaconvert) = 1.67.0

%description   -n gem-aws-sdk-mediaconvert
Official AWS Ruby gem for AWS Elemental MediaConvert (MediaConvert). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mediaconvert-doc
Version:       1.67.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaConvert documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mediaconvert
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mediaconvert) = 1.67.0

%description   -n gem-aws-sdk-mediaconvert-doc
AWS SDK for Ruby - MediaConvert documentation files.

Official AWS Ruby gem for AWS Elemental MediaConvert (MediaConvert). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediaconvert-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mediaconvert.


%package       -n gem-aws-sdk-mediaconvert-devel
Version:       1.67.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaConvert development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mediaconvert
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mediaconvert) = 1.67.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-mediaconvert-devel
AWS SDK for Ruby - MediaConvert development package.

Official AWS Ruby gem for AWS Elemental MediaConvert (MediaConvert). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediaconvert-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mediaconvert.


%package       -n gem-aws-sdk-finspace
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - finspace
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-finspace) = 1.2.0

%description   -n gem-aws-sdk-finspace
Official AWS Ruby gem for FinSpace User Environment Management service
(finspace). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-finspace-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - finspace documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-finspace
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-finspace) = 1.2.0

%description   -n gem-aws-sdk-finspace-doc
AWS SDK for Ruby - finspace documentation files.

Official AWS Ruby gem for FinSpace User Environment Management service
(finspace). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-finspace-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-finspace.


%package       -n gem-aws-sdk-finspace-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - finspace development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-finspace
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-finspace) = 1.2.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-finspace-devel
AWS SDK for Ruby - finspace development package.

Official AWS Ruby gem for FinSpace User Environment Management service
(finspace). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-finspace-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-finspace.


%package       -n gem-aws-sdk-iot
Version:       1.69.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-iot) = 1.69.0

%description   -n gem-aws-sdk-iot
Official AWS Ruby gem for AWS IoT. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-iot-doc
Version:       1.69.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iot
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iot) = 1.69.0

%description   -n gem-aws-sdk-iot-doc
AWS SDK for Ruby - AWS IoT documentation files.

Official AWS Ruby gem for AWS IoT. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iot-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iot.


%package       -n gem-aws-sdk-iot-devel
Version:       1.69.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iot
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iot) = 1.69.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-iot-devel
AWS SDK for Ruby - AWS IoT development package.

Official AWS Ruby gem for AWS IoT. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iot-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iot.


%package       -n gem-aws-sdk-importexport
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Import/Export
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv2) >= 1.0 gem(aws-sigv2) < 2
Provides:      gem(aws-sdk-importexport) = 1.26.0

%description   -n gem-aws-sdk-importexport
Official AWS Ruby gem for AWS Import/Export. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-importexport-doc
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Import/Export documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-importexport
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-importexport) = 1.26.0

%description   -n gem-aws-sdk-importexport-doc
AWS SDK for Ruby - AWS Import/Export documentation files.

Official AWS Ruby gem for AWS Import/Export. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-importexport-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-importexport.


%package       -n gem-aws-sdk-importexport-devel
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Import/Export development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-importexport
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-importexport) = 1.26.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-importexport-devel
AWS SDK for Ruby - AWS Import/Export development package.

Official AWS Ruby gem for AWS Import/Export. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-importexport-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-importexport.


%package       -n gem-aws-sdk-codestar
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeStar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-codestar) = 1.29.0

%description   -n gem-aws-sdk-codestar
Official AWS Ruby gem for AWS CodeStar (CodeStar). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-codestar-doc
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeStar documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codestar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codestar) = 1.29.0

%description   -n gem-aws-sdk-codestar-doc
AWS SDK for Ruby - CodeStar documentation files.

Official AWS Ruby gem for AWS CodeStar (CodeStar). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-codestar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codestar.


%package       -n gem-aws-sdk-codestar-devel
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeStar development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codestar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codestar) = 1.29.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-codestar-devel
AWS SDK for Ruby - CodeStar development package.

Official AWS Ruby gem for AWS CodeStar (CodeStar). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-codestar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codestar.


%package       -n gem-aws-sdk-iotfleethub
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Fleet Hub
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-iotfleethub) = 1.2.0

%description   -n gem-aws-sdk-iotfleethub
Official AWS Ruby gem for AWS IoT Fleet Hub. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-iotfleethub-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Fleet Hub documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotfleethub
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotfleethub) = 1.2.0

%description   -n gem-aws-sdk-iotfleethub-doc
AWS SDK for Ruby - AWS IoT Fleet Hub documentation files.

Official AWS Ruby gem for AWS IoT Fleet Hub. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-iotfleethub-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotfleethub.


%package       -n gem-aws-sdk-iotfleethub-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Fleet Hub development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotfleethub
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotfleethub) = 1.2.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-iotfleethub-devel
AWS SDK for Ruby - AWS IoT Fleet Hub development package.

Official AWS Ruby gem for AWS IoT Fleet Hub. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-iotfleethub-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotfleethub.


%package       -n gem-aws-sdk-sso
Version:       1.7.1
Release:       alt1
Summary:       AWS SDK for Ruby - SSO
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.105.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-sso) = 1.7.1

%description   -n gem-aws-sdk-sso
Official AWS Ruby gem for AWS Single Sign-On (SSO). SSO is included as part of
aws-sdk-core - this gem is an alias for loading aws-sdk-core.


%package       -n gem-aws-sdk-sso-doc
Version:       1.7.1
Release:       alt1
Summary:       AWS SDK for Ruby - SSO documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sso
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sso) = 1.7.1

%description   -n gem-aws-sdk-sso-doc
AWS SDK for Ruby - SSO documentation files.

Official AWS Ruby gem for AWS Single Sign-On (SSO). SSO is included as part of
aws-sdk-core - this gem is an alias for loading aws-sdk-core.

%description   -n gem-aws-sdk-sso-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sso.


%package       -n gem-aws-sdk-sso-devel
Version:       1.7.1
Release:       alt1
Summary:       AWS SDK for Ruby - SSO development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sso
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sso) = 1.7.1
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-sso-devel
AWS SDK for Ruby - SSO development package.

Official AWS Ruby gem for AWS Single Sign-On (SSO). SSO is included as part of
aws-sdk-core - this gem is an alias for loading aws-sdk-core.

%description   -n gem-aws-sdk-sso-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sso.


%package       -n gem-aws-sdk-cloudfront
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudFront
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-cloudfront) = 1.51.0

%description   -n gem-aws-sdk-cloudfront
Official AWS Ruby gem for Amazon CloudFront (CloudFront). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-cloudfront-doc
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudFront documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudfront
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudfront) = 1.51.0

%description   -n gem-aws-sdk-cloudfront-doc
AWS SDK for Ruby - CloudFront documentation files.

Official AWS Ruby gem for Amazon CloudFront (CloudFront). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudfront-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudfront.


%package       -n gem-aws-sdk-cloudfront-devel
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudFront development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudfront
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudfront) = 1.51.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-cloudfront-devel
AWS SDK for Ruby - CloudFront development package.

Official AWS Ruby gem for Amazon CloudFront (CloudFront). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudfront-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudfront.


%package       -n gem-aws-sdk-configservice
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - Config Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-configservice) = 1.62.0

%description   -n gem-aws-sdk-configservice
Official AWS Ruby gem for AWS Config (Config Service). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-configservice-doc
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - Config Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-configservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-configservice) = 1.62.0

%description   -n gem-aws-sdk-configservice-doc
AWS SDK for Ruby - Config Service documentation files.

Official AWS Ruby gem for AWS Config (Config Service). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-configservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-configservice.


%package       -n gem-aws-sdk-configservice-devel
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - Config Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-configservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-configservice) = 1.62.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-configservice-devel
AWS SDK for Ruby - Config Service development package.

Official AWS Ruby gem for AWS Config (Config Service). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-configservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-configservice.


%package       -n gem-aws-sdk-athena
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Athena
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-athena) = 1.37.0

%description   -n gem-aws-sdk-athena
Official AWS Ruby gem for Amazon Athena. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-athena-doc
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Athena documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-athena
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-athena) = 1.37.0

%description   -n gem-aws-sdk-athena-doc
AWS SDK for Ruby - Amazon Athena documentation files.

Official AWS Ruby gem for Amazon Athena. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-athena-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-athena.


%package       -n gem-aws-sdk-athena-devel
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Athena development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-athena
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-athena) = 1.37.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-athena-devel
AWS SDK for Ruby - Amazon Athena development package.

Official AWS Ruby gem for Amazon Athena. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-athena-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-athena.


%package       -n gem-aws-sdk-iot1clickdevicesservice
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT 1-Click Devices Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-iot1clickdevicesservice) = 1.28.0

%description   -n gem-aws-sdk-iot1clickdevicesservice
Official AWS Ruby gem for AWS IoT 1-Click Devices Service. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-iot1clickdevicesservice-doc
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT 1-Click Devices Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iot1clickdevicesservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iot1clickdevicesservice) = 1.28.0

%description   -n gem-aws-sdk-iot1clickdevicesservice-doc
AWS SDK for Ruby - AWS IoT 1-Click Devices Service documentation
files.

Official AWS Ruby gem for AWS IoT 1-Click Devices Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iot1clickdevicesservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iot1clickdevicesservice.


%package       -n gem-aws-sdk-iot1clickdevicesservice-devel
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT 1-Click Devices Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iot1clickdevicesservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iot1clickdevicesservice) = 1.28.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-iot1clickdevicesservice-devel
AWS SDK for Ruby - AWS IoT 1-Click Devices Service development
package.

Official AWS Ruby gem for AWS IoT 1-Click Devices Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iot1clickdevicesservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iot1clickdevicesservice.


%package       -n gem-aws-sdk-worklink
Version:       1.23.0
Release:       alt1
Summary:       AWS SDK for Ruby - WorkLink
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-worklink) = 1.23.0

%description   -n gem-aws-sdk-worklink
Official AWS Ruby gem for Amazon WorkLink (WorkLink). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-worklink-doc
Version:       1.23.0
Release:       alt1
Summary:       AWS SDK for Ruby - WorkLink documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-worklink
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-worklink) = 1.23.0

%description   -n gem-aws-sdk-worklink-doc
AWS SDK for Ruby - WorkLink documentation files.

Official AWS Ruby gem for Amazon WorkLink (WorkLink). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-worklink-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-worklink.


%package       -n gem-aws-sdk-worklink-devel
Version:       1.23.0
Release:       alt1
Summary:       AWS SDK for Ruby - WorkLink development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-worklink
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-worklink) = 1.23.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-worklink-devel
AWS SDK for Ruby - WorkLink development package.

Official AWS Ruby gem for Amazon WorkLink (WorkLink). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-worklink-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-worklink.


%package       -n gem-aws-sdk-snowball
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Snowball
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-snowball) = 1.38.0

%description   -n gem-aws-sdk-snowball
Official AWS Ruby gem for Amazon Import/Export Snowball (Amazon Snowball). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-snowball-doc
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Snowball documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-snowball
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-snowball) = 1.38.0

%description   -n gem-aws-sdk-snowball-doc
AWS SDK for Ruby - Amazon Snowball documentation files.

Official AWS Ruby gem for Amazon Import/Export Snowball (Amazon Snowball). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-snowball-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-snowball.


%package       -n gem-aws-sdk-snowball-devel
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Snowball development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-snowball
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-snowball) = 1.38.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-snowball-devel
AWS SDK for Ruby - Amazon Snowball development package.

Official AWS Ruby gem for Amazon Import/Export Snowball (Amazon Snowball). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-snowball-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-snowball.


%package       -n gem-aws-sdk-sagemakerruntime
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SageMaker Runtime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-sagemakerruntime) = 1.31.0

%description   -n gem-aws-sdk-sagemakerruntime
Official AWS Ruby gem for Amazon SageMaker Runtime. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-sagemakerruntime-doc
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SageMaker Runtime documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sagemakerruntime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakerruntime) = 1.31.0

%description   -n gem-aws-sdk-sagemakerruntime-doc
AWS SDK for Ruby - Amazon SageMaker Runtime documentation files.

Official AWS Ruby gem for Amazon SageMaker Runtime. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-sagemakerruntime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sagemakerruntime.


%package       -n gem-aws-sdk-sagemakerruntime-devel
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SageMaker Runtime development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sagemakerruntime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakerruntime) = 1.31.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-sagemakerruntime-devel
AWS SDK for Ruby - Amazon SageMaker Runtime development package.

Official AWS Ruby gem for Amazon SageMaker Runtime. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-sagemakerruntime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sagemakerruntime.


%package       -n gem-aws-sdk-nimblestudio
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonNimbleStudio
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-nimblestudio) = 1.1.0

%description   -n gem-aws-sdk-nimblestudio
Official AWS Ruby gem for AmazonNimbleStudio. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-nimblestudio-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonNimbleStudio documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-nimblestudio
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-nimblestudio) = 1.1.0

%description   -n gem-aws-sdk-nimblestudio-doc
AWS SDK for Ruby - AmazonNimbleStudio documentation files.

Official AWS Ruby gem for AmazonNimbleStudio. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-nimblestudio-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-nimblestudio.


%package       -n gem-aws-sdk-nimblestudio-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonNimbleStudio development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-nimblestudio
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-nimblestudio) = 1.1.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-nimblestudio-devel
AWS SDK for Ruby - AmazonNimbleStudio development package.

Official AWS Ruby gem for AmazonNimbleStudio. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-nimblestudio-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-nimblestudio.


%package       -n gem-aws-sdk-route53domains
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Route 53 Domains
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-route53domains) = 1.30.0

%description   -n gem-aws-sdk-route53domains
Official AWS Ruby gem for Amazon Route 53 Domains. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-route53domains-doc
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Route 53 Domains documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-route53domains
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-route53domains) = 1.30.0

%description   -n gem-aws-sdk-route53domains-doc
AWS SDK for Ruby - Amazon Route 53 Domains documentation files.

Official AWS Ruby gem for Amazon Route 53 Domains. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-route53domains-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-route53domains.


%package       -n gem-aws-sdk-route53domains-devel
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Route 53 Domains development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-route53domains
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-route53domains) = 1.30.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-route53domains-devel
AWS SDK for Ruby - Amazon Route 53 Domains development package.

Official AWS Ruby gem for Amazon Route 53 Domains. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-route53domains-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-route53domains.


%package       -n gem-aws-sdk-transcribeservice
Version:       1.55.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Transcribe Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-transcribeservice) = 1.55.0

%description   -n gem-aws-sdk-transcribeservice
Official AWS Ruby gem for Amazon Transcribe Service. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-transcribeservice-doc
Version:       1.55.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Transcribe Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-transcribeservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-transcribeservice) = 1.55.0

%description   -n gem-aws-sdk-transcribeservice-doc
AWS SDK for Ruby - Amazon Transcribe Service documentation files.

Official AWS Ruby gem for Amazon Transcribe Service. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-transcribeservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-transcribeservice.


%package       -n gem-aws-sdk-transcribeservice-devel
Version:       1.55.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Transcribe Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-transcribeservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-transcribeservice) = 1.55.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-transcribeservice-devel
AWS SDK for Ruby - Amazon Transcribe Service development package.

Official AWS Ruby gem for Amazon Transcribe Service. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-transcribeservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-transcribeservice.


%package       -n gem-aws-sdk-databasemigrationservice
Version:       1.53.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Database Migration Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-databasemigrationservice) = 1.53.0

%description   -n gem-aws-sdk-databasemigrationservice
Official AWS Ruby gem for AWS Database Migration Service. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-databasemigrationservice-doc
Version:       1.53.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Database Migration Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-databasemigrationservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-databasemigrationservice) = 1.53.0

%description   -n gem-aws-sdk-databasemigrationservice-doc
AWS SDK for Ruby - AWS Database Migration Service documentation files.

Official AWS Ruby gem for AWS Database Migration Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-databasemigrationservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-databasemigrationservice.


%package       -n gem-aws-sdk-databasemigrationservice-devel
Version:       1.53.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Database Migration Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-databasemigrationservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-databasemigrationservice) = 1.53.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-databasemigrationservice-devel
AWS SDK for Ruby - AWS Database Migration Service development package.

Official AWS Ruby gem for AWS Database Migration Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-databasemigrationservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-databasemigrationservice.


%package       -n gem-aws-sdk-ec2instanceconnect
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - EC2 Instance Connect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-ec2instanceconnect) = 1.14.0

%description   -n gem-aws-sdk-ec2instanceconnect
Official AWS Ruby gem for AWS EC2 Instance Connect (EC2 Instance Connect). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ec2instanceconnect-doc
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - EC2 Instance Connect documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ec2instanceconnect
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ec2instanceconnect) = 1.14.0

%description   -n gem-aws-sdk-ec2instanceconnect-doc
AWS SDK for Ruby - EC2 Instance Connect documentation files.

Official AWS Ruby gem for AWS EC2 Instance Connect (EC2 Instance Connect). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ec2instanceconnect-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ec2instanceconnect.


%package       -n gem-aws-sdk-ec2instanceconnect-devel
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - EC2 Instance Connect development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ec2instanceconnect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ec2instanceconnect) = 1.14.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ec2instanceconnect-devel
AWS SDK for Ruby - EC2 Instance Connect development package.

Official AWS Ruby gem for AWS EC2 Instance Connect (EC2 Instance Connect). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ec2instanceconnect-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ec2instanceconnect.


%package       -n gem-aws-sdk-amplifybackend
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmplifyBackend
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-amplifybackend) = 1.3.0

%description   -n gem-aws-sdk-amplifybackend
Official AWS Ruby gem for AmplifyBackend. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-amplifybackend-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmplifyBackend documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-amplifybackend
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-amplifybackend) = 1.3.0

%description   -n gem-aws-sdk-amplifybackend-doc
AWS SDK for Ruby - AmplifyBackend documentation files.

Official AWS Ruby gem for AmplifyBackend. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-amplifybackend-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-amplifybackend.


%package       -n gem-aws-sdk-amplifybackend-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmplifyBackend development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-amplifybackend
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-amplifybackend) = 1.3.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-amplifybackend-devel
AWS SDK for Ruby - AmplifyBackend development package.

Official AWS Ruby gem for AmplifyBackend. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-amplifybackend-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-amplifybackend.


%package       -n gem-aws-sdk-appsync
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSAppSync
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-appsync) = 1.40.0

%description   -n gem-aws-sdk-appsync
Official AWS Ruby gem for AWS AppSync (AWSAppSync). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-appsync-doc
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSAppSync documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appsync
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appsync) = 1.40.0

%description   -n gem-aws-sdk-appsync-doc
AWS SDK for Ruby - AWSAppSync documentation files.

Official AWS Ruby gem for AWS AppSync (AWSAppSync). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-appsync-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appsync.


%package       -n gem-aws-sdk-appsync-devel
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSAppSync development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appsync
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appsync) = 1.40.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-appsync-devel
AWS SDK for Ruby - AWSAppSync development package.

Official AWS Ruby gem for AWS AppSync (AWSAppSync). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-appsync-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appsync.


%package       -n gem-aws-sdk-appconfig
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - AppConfig
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-appconfig) = 1.14.0

%description   -n gem-aws-sdk-appconfig
Official AWS Ruby gem for Amazon AppConfig (AppConfig). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-appconfig-doc
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - AppConfig documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appconfig
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appconfig) = 1.14.0

%description   -n gem-aws-sdk-appconfig-doc
AWS SDK for Ruby - AppConfig documentation files.

Official AWS Ruby gem for Amazon AppConfig (AppConfig). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-appconfig-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appconfig.


%package       -n gem-aws-sdk-appconfig-devel
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - AppConfig development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appconfig
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appconfig) = 1.14.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-appconfig-devel
AWS SDK for Ruby - AppConfig development package.

Official AWS Ruby gem for Amazon AppConfig (AppConfig). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-appconfig-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appconfig.


%package       -n gem-aws-sdk-quicksight
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon QuickSight
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-quicksight) = 1.46.0

%description   -n gem-aws-sdk-quicksight
Official AWS Ruby gem for Amazon QuickSight. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-quicksight-doc
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon QuickSight documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-quicksight
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-quicksight) = 1.46.0

%description   -n gem-aws-sdk-quicksight-doc
AWS SDK for Ruby - Amazon QuickSight documentation files.

Official AWS Ruby gem for Amazon QuickSight. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-quicksight-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-quicksight.


%package       -n gem-aws-sdk-quicksight-devel
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon QuickSight development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-quicksight
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-quicksight) = 1.46.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-quicksight-devel
AWS SDK for Ruby - Amazon QuickSight development package.

Official AWS Ruby gem for Amazon QuickSight. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-quicksight-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-quicksight.


%package       -n gem-aws-sdk-kinesisvideoarchivedmedia
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Video Archived Media
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-kinesisvideoarchivedmedia) = 1.34.0

%description   -n gem-aws-sdk-kinesisvideoarchivedmedia
Official AWS Ruby gem for Amazon Kinesis Video Streams Archived Media (Kinesis
Video Archived Media). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kinesisvideoarchivedmedia-doc
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Video Archived Media documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesisvideoarchivedmedia
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideoarchivedmedia) = 1.34.0

%description   -n gem-aws-sdk-kinesisvideoarchivedmedia-doc
AWS SDK for Ruby - Kinesis Video Archived Media documentation files.

Official AWS Ruby gem for Amazon Kinesis Video Streams Archived Media (Kinesis
Video Archived Media). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideoarchivedmedia-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesisvideoarchivedmedia.


%package       -n gem-aws-sdk-kinesisvideoarchivedmedia-devel
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Video Archived Media development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesisvideoarchivedmedia
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideoarchivedmedia) = 1.34.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-kinesisvideoarchivedmedia-devel
AWS SDK for Ruby - Kinesis Video Archived Media development package.

Official AWS Ruby gem for Amazon Kinesis Video Streams Archived Media (Kinesis
Video Archived Media). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideoarchivedmedia-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesisvideoarchivedmedia.


%package       -n gem-aws-sdk-kendra
Version:       1.25.0
Release:       alt1
Summary:       AWS SDK for Ruby - kendra
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-kendra) = 1.25.0

%description   -n gem-aws-sdk-kendra
Official AWS Ruby gem for AWSKendraFrontendService (kendra). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kendra-doc
Version:       1.25.0
Release:       alt1
Summary:       AWS SDK for Ruby - kendra documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kendra
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kendra) = 1.25.0

%description   -n gem-aws-sdk-kendra-doc
AWS SDK for Ruby - kendra documentation files.

Official AWS Ruby gem for AWSKendraFrontendService (kendra). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kendra-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kendra.


%package       -n gem-aws-sdk-kendra-devel
Version:       1.25.0
Release:       alt1
Summary:       AWS SDK for Ruby - kendra development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kendra
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kendra) = 1.25.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-kendra-devel
AWS SDK for Ruby - kendra development package.

Official AWS Ruby gem for AWSKendraFrontendService (kendra). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kendra-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kendra.


%package       -n gem-aws-sdk-sesv2
Version:       1.17.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SES V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-sesv2) = 1.17.0

%description   -n gem-aws-sdk-sesv2
Official AWS Ruby gem for Amazon Simple Email Service (Amazon SES V2). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-sesv2-doc
Version:       1.17.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SES V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sesv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sesv2) = 1.17.0

%description   -n gem-aws-sdk-sesv2-doc
AWS SDK for Ruby - Amazon SES V2 documentation files.

Official AWS Ruby gem for Amazon Simple Email Service (Amazon SES V2). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sesv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sesv2.


%package       -n gem-aws-sdk-sesv2-devel
Version:       1.17.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SES V2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sesv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sesv2) = 1.17.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-sesv2-devel
AWS SDK for Ruby - Amazon SES V2 development package.

Official AWS Ruby gem for Amazon Simple Email Service (Amazon SES V2). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sesv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sesv2.


%package       -n gem-aws-sdk-xray
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS X-Ray
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-xray) = 1.37.0

%description   -n gem-aws-sdk-xray
Official AWS Ruby gem for AWS X-Ray. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-xray-doc
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS X-Ray documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-xray
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-xray) = 1.37.0

%description   -n gem-aws-sdk-xray-doc
AWS SDK for Ruby - AWS X-Ray documentation files.

Official AWS Ruby gem for AWS X-Ray. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-xray-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-xray.


%package       -n gem-aws-sdk-xray-devel
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS X-Ray development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-xray
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-xray) = 1.37.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-xray-devel
AWS SDK for Ruby - AWS X-Ray development package.

Official AWS Ruby gem for AWS X-Ray. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-xray-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-xray.


%package       -n gem-aws-sdk-docdb
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DocDB
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-docdb) = 1.31.0

%description   -n gem-aws-sdk-docdb
Official AWS Ruby gem for Amazon DocumentDB with MongoDB compatibility (Amazon
DocDB). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-docdb-doc
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DocDB documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-docdb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-docdb) = 1.31.0

%description   -n gem-aws-sdk-docdb-doc
AWS SDK for Ruby - Amazon DocDB documentation files.

Official AWS Ruby gem for Amazon DocumentDB with MongoDB compatibility (Amazon
DocDB). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-docdb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-docdb.


%package       -n gem-aws-sdk-docdb-devel
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DocDB development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-docdb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-docdb) = 1.31.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-docdb-devel
AWS SDK for Ruby - Amazon DocDB development package.

Official AWS Ruby gem for Amazon DocumentDB with MongoDB compatibility (Amazon
DocDB). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-docdb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-docdb.


%package       -n gem-aws-sdk-machinelearning
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Machine Learning
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-machinelearning) = 1.28.0

%description   -n gem-aws-sdk-machinelearning
Official AWS Ruby gem for Amazon Machine Learning. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-machinelearning-doc
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Machine Learning documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-machinelearning
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-machinelearning) = 1.28.0

%description   -n gem-aws-sdk-machinelearning-doc
AWS SDK for Ruby - Amazon Machine Learning documentation files.

Official AWS Ruby gem for Amazon Machine Learning. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-machinelearning-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-machinelearning.


%package       -n gem-aws-sdk-machinelearning-devel
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Machine Learning development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-machinelearning
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-machinelearning) = 1.28.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-machinelearning-devel
AWS SDK for Ruby - Amazon Machine Learning development package.

Official AWS Ruby gem for Amazon Machine Learning. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-machinelearning-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-machinelearning.


%package       -n gem-aws-sdk-synthetics
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Synthetics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-synthetics) = 1.12.0

%description   -n gem-aws-sdk-synthetics
Official AWS Ruby gem for Synthetics. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-synthetics-doc
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Synthetics documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-synthetics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-synthetics) = 1.12.0

%description   -n gem-aws-sdk-synthetics-doc
AWS SDK for Ruby - Synthetics documentation files.

Official AWS Ruby gem for Synthetics. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-synthetics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-synthetics.


%package       -n gem-aws-sdk-synthetics-devel
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Synthetics development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-synthetics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-synthetics) = 1.12.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-synthetics-devel
AWS SDK for Ruby - Synthetics development package.

Official AWS Ruby gem for Synthetics. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-synthetics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-synthetics.


%package       -n gem-aws-sdk-sns
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SNS
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-sns) = 1.41.0

%description   -n gem-aws-sdk-sns
Official AWS Ruby gem for Amazon Simple Notification Service (Amazon SNS). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-sns-doc
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SNS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sns
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sns) = 1.41.0

%description   -n gem-aws-sdk-sns-doc
AWS SDK for Ruby - Amazon SNS documentation files.

Official AWS Ruby gem for Amazon Simple Notification Service (Amazon SNS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sns-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sns.


%package       -n gem-aws-sdk-sns-devel
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SNS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sns
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sns) = 1.41.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-sns-devel
AWS SDK for Ruby - Amazon SNS development package.

Official AWS Ruby gem for Amazon Simple Notification Service (Amazon SNS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sns-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sns.


%package       -n gem-aws-sdk-servicequotas
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - Service Quotas
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-servicequotas) = 1.14.0

%description   -n gem-aws-sdk-servicequotas
Official AWS Ruby gem for Service Quotas. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-servicequotas-doc
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - Service Quotas documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-servicequotas
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-servicequotas) = 1.14.0

%description   -n gem-aws-sdk-servicequotas-doc
AWS SDK for Ruby - Service Quotas documentation files.

Official AWS Ruby gem for Service Quotas. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-servicequotas-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-servicequotas.


%package       -n gem-aws-sdk-servicequotas-devel
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - Service Quotas development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-servicequotas
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-servicequotas) = 1.14.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-servicequotas-devel
AWS SDK for Ruby - Service Quotas development package.

Official AWS Ruby gem for Service Quotas. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-servicequotas-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-servicequotas.


%package       -n gem-aws-sdk-pinpointemail
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - Pinpoint Email
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-pinpointemail) = 1.26.0

%description   -n gem-aws-sdk-pinpointemail
Official AWS Ruby gem for Amazon Pinpoint Email Service (Pinpoint Email). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-pinpointemail-doc
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - Pinpoint Email documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-pinpointemail
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-pinpointemail) = 1.26.0

%description   -n gem-aws-sdk-pinpointemail-doc
AWS SDK for Ruby - Pinpoint Email documentation files.

Official AWS Ruby gem for Amazon Pinpoint Email Service (Pinpoint Email). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pinpointemail-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-pinpointemail.


%package       -n gem-aws-sdk-pinpointemail-devel
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - Pinpoint Email development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-pinpointemail
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-pinpointemail) = 1.26.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-pinpointemail-devel
AWS SDK for Ruby - Pinpoint Email development package.

Official AWS Ruby gem for Amazon Pinpoint Email Service (Pinpoint Email). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pinpointemail-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-pinpointemail.


%package       -n gem-aws-sdk-mwaa
Version:       1.5.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonMWAA
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-mwaa) = 1.5.0

%description   -n gem-aws-sdk-mwaa
Official AWS Ruby gem for AmazonMWAA. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mwaa-doc
Version:       1.5.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonMWAA documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mwaa
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mwaa) = 1.5.0

%description   -n gem-aws-sdk-mwaa-doc
AWS SDK for Ruby - AmazonMWAA documentation files.

Official AWS Ruby gem for AmazonMWAA. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mwaa-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mwaa.


%package       -n gem-aws-sdk-mwaa-devel
Version:       1.5.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonMWAA development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mwaa
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mwaa) = 1.5.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-mwaa-devel
AWS SDK for Ruby - AmazonMWAA development package.

Official AWS Ruby gem for AmazonMWAA. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mwaa-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mwaa.


%package       -n gem-aws-sdk-opsworkscm
Version:       1.43.0
Release:       alt1
Summary:       AWS SDK for Ruby - OpsWorksCM
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-opsworkscm) = 1.43.0

%description   -n gem-aws-sdk-opsworkscm
Official AWS Ruby gem for AWS OpsWorks CM (OpsWorksCM). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-opsworkscm-doc
Version:       1.43.0
Release:       alt1
Summary:       AWS SDK for Ruby - OpsWorksCM documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-opsworkscm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-opsworkscm) = 1.43.0

%description   -n gem-aws-sdk-opsworkscm-doc
AWS SDK for Ruby - OpsWorksCM documentation files.

Official AWS Ruby gem for AWS OpsWorks CM (OpsWorksCM). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-opsworkscm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-opsworkscm.


%package       -n gem-aws-sdk-opsworkscm-devel
Version:       1.43.0
Release:       alt1
Summary:       AWS SDK for Ruby - OpsWorksCM development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-opsworkscm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-opsworkscm) = 1.43.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-opsworkscm-devel
AWS SDK for Ruby - OpsWorksCM development package.

Official AWS Ruby gem for AWS OpsWorks CM (OpsWorksCM). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-opsworkscm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-opsworkscm.


%package       -n gem-aws-sdk-codedeploy
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeDeploy
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-codedeploy) = 1.40.0

%description   -n gem-aws-sdk-codedeploy
Official AWS Ruby gem for AWS CodeDeploy (CodeDeploy). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-codedeploy-doc
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeDeploy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codedeploy
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codedeploy) = 1.40.0

%description   -n gem-aws-sdk-codedeploy-doc
AWS SDK for Ruby - CodeDeploy documentation files.

Official AWS Ruby gem for AWS CodeDeploy (CodeDeploy). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-codedeploy-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codedeploy.


%package       -n gem-aws-sdk-codedeploy-devel
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeDeploy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codedeploy
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codedeploy) = 1.40.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-codedeploy-devel
AWS SDK for Ruby - CodeDeploy development package.

Official AWS Ruby gem for AWS CodeDeploy (CodeDeploy). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-codedeploy-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codedeploy.


%package       -n gem-aws-sdk-managedblockchain
Version:       1.22.0
Release:       alt1
Summary:       AWS SDK for Ruby - ManagedBlockchain
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-managedblockchain) = 1.22.0

%description   -n gem-aws-sdk-managedblockchain
Official AWS Ruby gem for Amazon Managed Blockchain (ManagedBlockchain). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-managedblockchain-doc
Version:       1.22.0
Release:       alt1
Summary:       AWS SDK for Ruby - ManagedBlockchain documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-managedblockchain
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-managedblockchain) = 1.22.0

%description   -n gem-aws-sdk-managedblockchain-doc
AWS SDK for Ruby - ManagedBlockchain documentation files.

Official AWS Ruby gem for Amazon Managed Blockchain (ManagedBlockchain). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-managedblockchain-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-managedblockchain.


%package       -n gem-aws-sdk-managedblockchain-devel
Version:       1.22.0
Release:       alt1
Summary:       AWS SDK for Ruby - ManagedBlockchain development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-managedblockchain
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-managedblockchain) = 1.22.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-managedblockchain-devel
AWS SDK for Ruby - ManagedBlockchain development package.

Official AWS Ruby gem for Amazon Managed Blockchain (ManagedBlockchain). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-managedblockchain-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-managedblockchain.


%package       -n gem-aws-sdk-ec2
Version:       1.240.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EC2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Provides:      gem(aws-sdk-ec2) = 1.240.0

%description   -n gem-aws-sdk-ec2
Official AWS Ruby gem for Amazon Elastic Compute Cloud (Amazon EC2). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ec2-doc
Version:       1.240.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EC2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ec2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ec2) = 1.240.0

%description   -n gem-aws-sdk-ec2-doc
AWS SDK for Ruby - Amazon EC2 documentation files.

Official AWS Ruby gem for Amazon Elastic Compute Cloud (Amazon EC2). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ec2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ec2.


%package       -n gem-aws-sdk-ec2-devel
Version:       1.240.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EC2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ec2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ec2) = 1.240.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ec2-devel
AWS SDK for Ruby - Amazon EC2 development package.

Official AWS Ruby gem for Amazon Elastic Compute Cloud (Amazon EC2). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ec2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ec2.


%package       -n gem-aws-sdk-iotevents
Version:       1.24.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Events
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-iotevents) = 1.24.0

%description   -n gem-aws-sdk-iotevents
Official AWS Ruby gem for AWS IoT Events. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-iotevents-doc
Version:       1.24.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Events documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotevents
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotevents) = 1.24.0

%description   -n gem-aws-sdk-iotevents-doc
AWS SDK for Ruby - AWS IoT Events documentation files.

Official AWS Ruby gem for AWS IoT Events. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-iotevents-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotevents.


%package       -n gem-aws-sdk-iotevents-devel
Version:       1.24.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Events development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotevents
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotevents) = 1.24.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-iotevents-devel
AWS SDK for Ruby - AWS IoT Events development package.

Official AWS Ruby gem for AWS IoT Events. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-iotevents-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotevents.


%package       -n gem-aws-sdk-budgets
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSBudgets
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-budgets) = 1.38.0

%description   -n gem-aws-sdk-budgets
Official AWS Ruby gem for AWS Budgets (AWSBudgets). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-budgets-doc
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSBudgets documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-budgets
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-budgets) = 1.38.0

%description   -n gem-aws-sdk-budgets-doc
AWS SDK for Ruby - AWSBudgets documentation files.

Official AWS Ruby gem for AWS Budgets (AWSBudgets). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-budgets-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-budgets.


%package       -n gem-aws-sdk-budgets-devel
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSBudgets development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-budgets
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-budgets) = 1.38.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-budgets-devel
AWS SDK for Ruby - AWSBudgets development package.

Official AWS Ruby gem for AWS Budgets (AWSBudgets). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-budgets-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-budgets.


%package       -n gem-aws-sdk-apigateway
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon API Gateway
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-apigateway) = 1.62.0

%description   -n gem-aws-sdk-apigateway
Official AWS Ruby gem for Amazon API Gateway. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-apigateway-doc
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon API Gateway documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-apigateway
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-apigateway) = 1.62.0

%description   -n gem-aws-sdk-apigateway-doc
AWS SDK for Ruby - Amazon API Gateway documentation files.

Official AWS Ruby gem for Amazon API Gateway. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-apigateway-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-apigateway.


%package       -n gem-aws-sdk-apigateway-devel
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon API Gateway development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-apigateway
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-apigateway) = 1.62.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-apigateway-devel
AWS SDK for Ruby - Amazon API Gateway development package.

Official AWS Ruby gem for Amazon API Gateway. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-apigateway-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-apigateway.


%package       -n gem-aws-sdk-timestreamwrite
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Timestream Write
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-timestreamwrite) = 1.4.0

%description   -n gem-aws-sdk-timestreamwrite
Official AWS Ruby gem for Amazon Timestream Write (Timestream Write). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-timestreamwrite-doc
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Timestream Write documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-timestreamwrite
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-timestreamwrite) = 1.4.0

%description   -n gem-aws-sdk-timestreamwrite-doc
AWS SDK for Ruby - Timestream Write documentation files.

Official AWS Ruby gem for Amazon Timestream Write (Timestream Write). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-timestreamwrite-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-timestreamwrite.


%package       -n gem-aws-sdk-timestreamwrite-devel
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Timestream Write development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-timestreamwrite
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-timestreamwrite) = 1.4.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-timestreamwrite-devel
AWS SDK for Ruby - Timestream Write development package.

Official AWS Ruby gem for Amazon Timestream Write (Timestream Write). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-timestreamwrite-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-timestreamwrite.


%package       -n gem-aws-sdk-braket
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - Braket
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-braket) = 1.8.0

%description   -n gem-aws-sdk-braket
Official AWS Ruby gem for Braket. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-braket-doc
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - Braket documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-braket
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-braket) = 1.8.0

%description   -n gem-aws-sdk-braket-doc
AWS SDK for Ruby - Braket documentation files.

Official AWS Ruby gem for Braket. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-braket-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-braket.


%package       -n gem-aws-sdk-braket-devel
Version:       1.8.0
Release:       alt1
Summary:       AWS SDK for Ruby - Braket development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-braket
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-braket) = 1.8.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-braket-devel
AWS SDK for Ruby - Braket development package.

Official AWS Ruby gem for Braket. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-braket-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-braket.


%package       -n gem-aws-eventstream
Version:       1.1.1
Release:       alt1
Summary:       AWS Event Stream Library
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(aws-eventstream) = 1.1.1

%description   -n gem-aws-eventstream
Amazon Web Services event stream library. Decodes and encodes binary stream
under `vnd.amazon.event-stream` content-type


%package       -n gem-aws-eventstream-doc
Version:       1.1.1
Release:       alt1
Summary:       AWS Event Stream Library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-eventstream
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-eventstream) = 1.1.1

%description   -n gem-aws-eventstream-doc
AWS Event Stream Library documentation files.

Amazon Web Services event stream library. Decodes and encodes binary stream
under `vnd.amazon.event-stream` content-type

%description   -n gem-aws-eventstream-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-eventstream.


%package       -n gem-aws-sdk-acm
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - ACM
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-acm) = 1.41.0

%description   -n gem-aws-sdk-acm
Official AWS Ruby gem for AWS Certificate Manager (ACM). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-acm-doc
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - ACM documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-acm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-acm) = 1.41.0

%description   -n gem-aws-sdk-acm-doc
AWS SDK for Ruby - ACM documentation files.

Official AWS Ruby gem for AWS Certificate Manager (ACM). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-acm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-acm.


%package       -n gem-aws-sdk-acm-devel
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - ACM development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-acm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-acm) = 1.41.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-acm-devel
AWS SDK for Ruby - ACM development package.

Official AWS Ruby gem for AWS Certificate Manager (ACM). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-acm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-acm.


%package       -n gem-aws-sdk-macie2
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Macie 2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-macie2) = 1.28.0

%description   -n gem-aws-sdk-macie2
Official AWS Ruby gem for Amazon Macie 2. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-macie2-doc
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Macie 2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-macie2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-macie2) = 1.28.0

%description   -n gem-aws-sdk-macie2-doc
AWS SDK for Ruby - Amazon Macie 2 documentation files.

Official AWS Ruby gem for Amazon Macie 2. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-macie2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-macie2.


%package       -n gem-aws-sdk-macie2-devel
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Macie 2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-macie2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-macie2) = 1.28.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-macie2-devel
AWS SDK for Ruby - Amazon Macie 2 development package.

Official AWS Ruby gem for Amazon Macie 2. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-macie2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-macie2.


%package       -n gem-aws-sdk-apigatewayv2
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonApiGatewayV2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-apigatewayv2) = 1.32.0

%description   -n gem-aws-sdk-apigatewayv2
Official AWS Ruby gem for AmazonApiGatewayV2. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-apigatewayv2-doc
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonApiGatewayV2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-apigatewayv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-apigatewayv2) = 1.32.0

%description   -n gem-aws-sdk-apigatewayv2-doc
AWS SDK for Ruby - AmazonApiGatewayV2 documentation files.

Official AWS Ruby gem for AmazonApiGatewayV2. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-apigatewayv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-apigatewayv2.


%package       -n gem-aws-sdk-apigatewayv2-devel
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonApiGatewayV2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-apigatewayv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-apigatewayv2) = 1.32.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-apigatewayv2-devel
AWS SDK for Ruby - AmazonApiGatewayV2 development package.

Official AWS Ruby gem for AmazonApiGatewayV2. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-apigatewayv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-apigatewayv2.


%package       -n gem-aws-sdk-autoscaling
Version:       1.63.0
Release:       alt1
Summary:       AWS SDK for Ruby - Auto Scaling
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-autoscaling) = 1.63.0

%description   -n gem-aws-sdk-autoscaling
Official AWS Ruby gem for Auto Scaling. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-autoscaling-doc
Version:       1.63.0
Release:       alt1
Summary:       AWS SDK for Ruby - Auto Scaling documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-autoscaling
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-autoscaling) = 1.63.0

%description   -n gem-aws-sdk-autoscaling-doc
AWS SDK for Ruby - Auto Scaling documentation files.

Official AWS Ruby gem for Auto Scaling. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-autoscaling-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-autoscaling.


%package       -n gem-aws-sdk-autoscaling-devel
Version:       1.63.0
Release:       alt1
Summary:       AWS SDK for Ruby - Auto Scaling development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-autoscaling
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-autoscaling) = 1.63.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-autoscaling-devel
AWS SDK for Ruby - Auto Scaling development package.

Official AWS Ruby gem for Auto Scaling. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-autoscaling-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-autoscaling.


%package       -n gem-aws-sdk-secretsmanager
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Secrets Manager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-secretsmanager) = 1.46.0

%description   -n gem-aws-sdk-secretsmanager
Official AWS Ruby gem for AWS Secrets Manager. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-secretsmanager-doc
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Secrets Manager documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-secretsmanager
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-secretsmanager) = 1.46.0

%description   -n gem-aws-sdk-secretsmanager-doc
AWS SDK for Ruby - AWS Secrets Manager documentation files.

Official AWS Ruby gem for AWS Secrets Manager. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-secretsmanager-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-secretsmanager.


%package       -n gem-aws-sdk-secretsmanager-devel
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Secrets Manager development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-secretsmanager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-secretsmanager) = 1.46.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-secretsmanager-devel
AWS SDK for Ruby - AWS Secrets Manager development package.

Official AWS Ruby gem for AWS Secrets Manager. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-secretsmanager-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-secretsmanager.


%package       -n gem-aws-sdk-cloudhsm
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudHSM
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-cloudhsm) = 1.30.0

%description   -n gem-aws-sdk-cloudhsm
Official AWS Ruby gem for Amazon CloudHSM (CloudHSM). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-cloudhsm-doc
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudHSM documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudhsm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudhsm) = 1.30.0

%description   -n gem-aws-sdk-cloudhsm-doc
AWS SDK for Ruby - CloudHSM documentation files.

Official AWS Ruby gem for Amazon CloudHSM (CloudHSM). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudhsm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudhsm.


%package       -n gem-aws-sdk-cloudhsm-devel
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudHSM development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudhsm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudhsm) = 1.30.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-cloudhsm-devel
AWS SDK for Ruby - CloudHSM development package.

Official AWS Ruby gem for Amazon CloudHSM (CloudHSM). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudhsm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudhsm.


%package       -n gem-aws-sdk-mediastoredata
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaStore Data
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-mediastoredata) = 1.29.0

%description   -n gem-aws-sdk-mediastoredata
Official AWS Ruby gem for AWS Elemental MediaStore Data Plane (MediaStore Data).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mediastoredata-doc
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaStore Data documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mediastoredata
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mediastoredata) = 1.29.0

%description   -n gem-aws-sdk-mediastoredata-doc
AWS SDK for Ruby - MediaStore Data documentation files.

Official AWS Ruby gem for AWS Elemental MediaStore Data Plane (MediaStore Data).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediastoredata-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mediastoredata.


%package       -n gem-aws-sdk-mediastoredata-devel
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaStore Data development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mediastoredata
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mediastoredata) = 1.29.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-mediastoredata-devel
AWS SDK for Ruby - MediaStore Data development package.

Official AWS Ruby gem for AWS Elemental MediaStore Data Plane (MediaStore Data).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediastoredata-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mediastoredata.


%package       -n gem-aws-sdk-augmentedairuntime
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Augmented AI Runtime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-augmentedairuntime) = 1.13.0

%description   -n gem-aws-sdk-augmentedairuntime
Official AWS Ruby gem for Amazon Augmented AI Runtime. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-augmentedairuntime-doc
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Augmented AI Runtime documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-augmentedairuntime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-augmentedairuntime) = 1.13.0

%description   -n gem-aws-sdk-augmentedairuntime-doc
AWS SDK for Ruby - Amazon Augmented AI Runtime documentation files.

Official AWS Ruby gem for Amazon Augmented AI Runtime. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-augmentedairuntime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-augmentedairuntime.


%package       -n gem-aws-sdk-augmentedairuntime-devel
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Augmented AI Runtime development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-augmentedairuntime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-augmentedairuntime) = 1.13.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-augmentedairuntime-devel
AWS SDK for Ruby - Amazon Augmented AI Runtime development package.

Official AWS Ruby gem for Amazon Augmented AI Runtime. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-augmentedairuntime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-augmentedairuntime.


%package       -n gem-aws-sdk-transcribestreamingservice
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Transcribe Streaming Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-transcribestreamingservice) = 1.29.0

%description   -n gem-aws-sdk-transcribestreamingservice
Official AWS Ruby gem for Amazon Transcribe Streaming Service. This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-transcribestreamingservice-doc
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Transcribe Streaming Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-transcribestreamingservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-transcribestreamingservice) = 1.29.0

%description   -n gem-aws-sdk-transcribestreamingservice-doc
AWS SDK for Ruby - Amazon Transcribe Streaming Service documentation
files.

Official AWS Ruby gem for Amazon Transcribe Streaming Service. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-transcribestreamingservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-transcribestreamingservice.


%package       -n gem-aws-sdk-transcribestreamingservice-devel
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Transcribe Streaming Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-transcribestreamingservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-transcribestreamingservice) = 1.29.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-transcribestreamingservice-devel
AWS SDK for Ruby - Amazon Transcribe Streaming Service development
package.

Official AWS Ruby gem for Amazon Transcribe Streaming Service. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-transcribestreamingservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-transcribestreamingservice.


%package       -n gem-aws-sdk-cloudsearchdomain
Version:       1.24.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudSearch Domain
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-cloudsearchdomain) = 1.24.0

%description   -n gem-aws-sdk-cloudsearchdomain
Official AWS Ruby gem for Amazon CloudSearch Domain. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-cloudsearchdomain-doc
Version:       1.24.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudSearch Domain documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudsearchdomain
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudsearchdomain) = 1.24.0

%description   -n gem-aws-sdk-cloudsearchdomain-doc
AWS SDK for Ruby - Amazon CloudSearch Domain documentation files.

Official AWS Ruby gem for Amazon CloudSearch Domain. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-cloudsearchdomain-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudsearchdomain.


%package       -n gem-aws-sdk-cloudsearchdomain-devel
Version:       1.24.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudSearch Domain development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudsearchdomain
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudsearchdomain) = 1.24.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-cloudsearchdomain-devel
AWS SDK for Ruby - Amazon CloudSearch Domain development package.

Official AWS Ruby gem for Amazon CloudSearch Domain. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-cloudsearchdomain-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudsearchdomain.


%package       -n gem-aws-sdk-sms
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - SMS
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-sms) = 1.29.0

%description   -n gem-aws-sdk-sms
Official AWS Ruby gem for AWS Server Migration Service (SMS). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-sms-doc
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - SMS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sms
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sms) = 1.29.0

%description   -n gem-aws-sdk-sms-doc
AWS SDK for Ruby - SMS documentation files.

Official AWS Ruby gem for AWS Server Migration Service (SMS). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sms-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sms.


%package       -n gem-aws-sdk-sms-devel
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - SMS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sms
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sms) = 1.29.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-sms-devel
AWS SDK for Ruby - SMS development package.

Official AWS Ruby gem for AWS Server Migration Service (SMS). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sms-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sms.


%package       -n gem-aws-sdk-sqs
Version:       1.39.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SQS
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-sqs) = 1.39.0

%description   -n gem-aws-sdk-sqs
Official AWS Ruby gem for Amazon Simple Queue Service (Amazon SQS). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-sqs-doc
Version:       1.39.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SQS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sqs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sqs) = 1.39.0

%description   -n gem-aws-sdk-sqs-doc
AWS SDK for Ruby - Amazon SQS documentation files.

Official AWS Ruby gem for Amazon Simple Queue Service (Amazon SQS). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sqs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sqs.


%package       -n gem-aws-sdk-sqs-devel
Version:       1.39.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SQS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sqs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sqs) = 1.39.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-sqs-devel
AWS SDK for Ruby - Amazon SQS development package.

Official AWS Ruby gem for Amazon Simple Queue Service (Amazon SQS). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sqs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sqs.


%package       -n gem-aws-sdk-devopsguru
Version:       1.6.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DevOps Guru
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-devopsguru) = 1.6.0

%description   -n gem-aws-sdk-devopsguru
Official AWS Ruby gem for Amazon DevOps Guru. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-devopsguru-doc
Version:       1.6.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DevOps Guru documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-devopsguru
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-devopsguru) = 1.6.0

%description   -n gem-aws-sdk-devopsguru-doc
AWS SDK for Ruby - Amazon DevOps Guru documentation files.

Official AWS Ruby gem for Amazon DevOps Guru. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-devopsguru-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-devopsguru.


%package       -n gem-aws-sdk-devopsguru-devel
Version:       1.6.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DevOps Guru development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-devopsguru
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-devopsguru) = 1.6.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-devopsguru-devel
AWS SDK for Ruby - Amazon DevOps Guru development package.

Official AWS Ruby gem for Amazon DevOps Guru. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-devopsguru-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-devopsguru.


%package       -n gem-aws-sdk-ram
Version:       1.25.0
Release:       alt1
Summary:       AWS SDK for Ruby - RAM
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-ram) = 1.25.0

%description   -n gem-aws-sdk-ram
Official AWS Ruby gem for AWS Resource Access Manager (RAM). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ram-doc
Version:       1.25.0
Release:       alt1
Summary:       AWS SDK for Ruby - RAM documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ram
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ram) = 1.25.0

%description   -n gem-aws-sdk-ram-doc
AWS SDK for Ruby - RAM documentation files.

Official AWS Ruby gem for AWS Resource Access Manager (RAM). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ram-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ram.


%package       -n gem-aws-sdk-ram-devel
Version:       1.25.0
Release:       alt1
Summary:       AWS SDK for Ruby - RAM development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ram
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ram) = 1.25.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ram-devel
AWS SDK for Ruby - RAM development package.

Official AWS Ruby gem for AWS Resource Access Manager (RAM). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ram-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ram.


%package       -n gem-aws-sdk-kafka
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kafka
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-kafka) = 1.36.0

%description   -n gem-aws-sdk-kafka
Official AWS Ruby gem for Managed Streaming for Kafka (Kafka). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kafka-doc
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kafka documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kafka
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kafka) = 1.36.0

%description   -n gem-aws-sdk-kafka-doc
AWS SDK for Ruby - Kafka documentation files.

Official AWS Ruby gem for Managed Streaming for Kafka (Kafka). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kafka-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kafka.


%package       -n gem-aws-sdk-kafka-devel
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kafka development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kafka
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kafka) = 1.36.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-kafka-devel
AWS SDK for Ruby - Kafka development package.

Official AWS Ruby gem for Managed Streaming for Kafka (Kafka). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kafka-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kafka.


%package       -n gem-aws-sdk-datasync
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - DataSync
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-datasync) = 1.32.0

%description   -n gem-aws-sdk-datasync
Official AWS Ruby gem for AWS DataSync (DataSync). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-datasync-doc
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - DataSync documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-datasync
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-datasync) = 1.32.0

%description   -n gem-aws-sdk-datasync-doc
AWS SDK for Ruby - DataSync documentation files.

Official AWS Ruby gem for AWS DataSync (DataSync). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-datasync-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-datasync.


%package       -n gem-aws-sdk-datasync-devel
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - DataSync development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-datasync
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-datasync) = 1.32.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-datasync-devel
AWS SDK for Ruby - DataSync development package.

Official AWS Ruby gem for AWS DataSync (DataSync). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-datasync-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-datasync.


%package       -n gem-aws-sdk-kinesisvideosignalingchannels
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Kinesis Video Signaling Channels
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-kinesisvideosignalingchannels) = 1.10.0

%description   -n gem-aws-sdk-kinesisvideosignalingchannels
Official AWS Ruby gem for Amazon Kinesis Video Signaling Channels. This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kinesisvideosignalingchannels-doc
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Kinesis Video Signaling Channels documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesisvideosignalingchannels
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideosignalingchannels) = 1.10.0

%description   -n gem-aws-sdk-kinesisvideosignalingchannels-doc
AWS SDK for Ruby - Amazon Kinesis Video Signaling Channels documentation
files.

Official AWS Ruby gem for Amazon Kinesis Video Signaling Channels. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideosignalingchannels-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesisvideosignalingchannels.


%package       -n gem-aws-sdk-kinesisvideosignalingchannels-devel
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Kinesis Video Signaling Channels development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesisvideosignalingchannels
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideosignalingchannels) = 1.10.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-kinesisvideosignalingchannels-devel
AWS SDK for Ruby - Amazon Kinesis Video Signaling Channels development
package.

Official AWS Ruby gem for Amazon Kinesis Video Signaling Channels. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideosignalingchannels-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesisvideosignalingchannels.


%package       -n gem-aws-sdk-applicationdiscoveryservice
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Application Discovery Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-applicationdiscoveryservice) = 1.35.0

%description   -n gem-aws-sdk-applicationdiscoveryservice
Official AWS Ruby gem for AWS Application Discovery Service. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-applicationdiscoveryservice-doc
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Application Discovery Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-applicationdiscoveryservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationdiscoveryservice) = 1.35.0

%description   -n gem-aws-sdk-applicationdiscoveryservice-doc
AWS SDK for Ruby - AWS Application Discovery Service documentation
files.

Official AWS Ruby gem for AWS Application Discovery Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-applicationdiscoveryservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-applicationdiscoveryservice.


%package       -n gem-aws-sdk-applicationdiscoveryservice-devel
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Application Discovery Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-applicationdiscoveryservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationdiscoveryservice) = 1.35.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-applicationdiscoveryservice-devel
AWS SDK for Ruby - AWS Application Discovery Service development
package.

Official AWS Ruby gem for AWS Application Discovery Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-applicationdiscoveryservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-applicationdiscoveryservice.


%package       -n gem-aws-sdk-glue
Version:       1.88.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Glue
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-glue) = 1.88.0

%description   -n gem-aws-sdk-glue
Official AWS Ruby gem for AWS Glue. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-glue-doc
Version:       1.88.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Glue documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-glue
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-glue) = 1.88.0

%description   -n gem-aws-sdk-glue-doc
AWS SDK for Ruby - AWS Glue documentation files.

Official AWS Ruby gem for AWS Glue. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-glue-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-glue.


%package       -n gem-aws-sdk-glue-devel
Version:       1.88.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Glue development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-glue
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-glue) = 1.88.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-glue-devel
AWS SDK for Ruby - AWS Glue development package.

Official AWS Ruby gem for AWS Glue. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-glue-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-glue.


%package       -n gem-aws-sdk-mediapackage
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaPackage
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-mediapackage) = 1.40.0

%description   -n gem-aws-sdk-mediapackage
Official AWS Ruby gem for AWS Elemental MediaPackage (MediaPackage). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mediapackage-doc
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaPackage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mediapackage
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mediapackage) = 1.40.0

%description   -n gem-aws-sdk-mediapackage-doc
AWS SDK for Ruby - MediaPackage documentation files.

Official AWS Ruby gem for AWS Elemental MediaPackage (MediaPackage). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediapackage-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mediapackage.


%package       -n gem-aws-sdk-mediapackage-devel
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaPackage development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mediapackage
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mediapackage) = 1.40.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-mediapackage-devel
AWS SDK for Ruby - MediaPackage development package.

Official AWS Ruby gem for AWS Elemental MediaPackage (MediaPackage). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediapackage-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mediapackage.


%package       -n gem-aws-sdk-identitystore
Version:       1.5.0
Release:       alt1
Summary:       AWS SDK for Ruby - IdentityStore
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-identitystore) = 1.5.0

%description   -n gem-aws-sdk-identitystore
Official AWS Ruby gem for AWS SSO Identity Store (IdentityStore). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-identitystore-doc
Version:       1.5.0
Release:       alt1
Summary:       AWS SDK for Ruby - IdentityStore documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-identitystore
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-identitystore) = 1.5.0

%description   -n gem-aws-sdk-identitystore-doc
AWS SDK for Ruby - IdentityStore documentation files.

Official AWS Ruby gem for AWS SSO Identity Store (IdentityStore). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-identitystore-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-identitystore.


%package       -n gem-aws-sdk-identitystore-devel
Version:       1.5.0
Release:       alt1
Summary:       AWS SDK for Ruby - IdentityStore development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-identitystore
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-identitystore) = 1.5.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-identitystore-devel
AWS SDK for Ruby - IdentityStore development package.

Official AWS Ruby gem for AWS SSO Identity Store (IdentityStore). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-identitystore-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-identitystore.


%package       -n gem-aws-sdk-elasticache
Version:       1.57.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon ElastiCache
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-elasticache) = 1.57.0

%description   -n gem-aws-sdk-elasticache
Official AWS Ruby gem for Amazon ElastiCache. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-elasticache-doc
Version:       1.57.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon ElastiCache documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-elasticache
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticache) = 1.57.0

%description   -n gem-aws-sdk-elasticache-doc
AWS SDK for Ruby - Amazon ElastiCache documentation files.

Official AWS Ruby gem for Amazon ElastiCache. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-elasticache-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-elasticache.


%package       -n gem-aws-sdk-elasticache-devel
Version:       1.57.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon ElastiCache development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-elasticache
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticache) = 1.57.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-elasticache-devel
AWS SDK for Ruby - Amazon ElastiCache development package.

Official AWS Ruby gem for Amazon ElastiCache. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-elasticache-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-elasticache.


%package       -n gem-aws-sdk-emrcontainers
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EMR Containers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-emrcontainers) = 1.3.0

%description   -n gem-aws-sdk-emrcontainers
Official AWS Ruby gem for Amazon EMR Containers. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-emrcontainers-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EMR Containers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-emrcontainers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-emrcontainers) = 1.3.0

%description   -n gem-aws-sdk-emrcontainers-doc
AWS SDK for Ruby - Amazon EMR Containers documentation files.

Official AWS Ruby gem for Amazon EMR Containers. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-emrcontainers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-emrcontainers.


%package       -n gem-aws-sdk-emrcontainers-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EMR Containers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-emrcontainers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-emrcontainers) = 1.3.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-emrcontainers-devel
AWS SDK for Ruby - Amazon EMR Containers development package.

Official AWS Ruby gem for Amazon EMR Containers. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-emrcontainers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-emrcontainers.


%package       -n gem-aws-sdk-shield
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Shield
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-shield) = 1.37.0

%description   -n gem-aws-sdk-shield
Official AWS Ruby gem for AWS Shield. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-shield-doc
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Shield documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-shield
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-shield) = 1.37.0

%description   -n gem-aws-sdk-shield-doc
AWS SDK for Ruby - AWS Shield documentation files.

Official AWS Ruby gem for AWS Shield. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-shield-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-shield.


%package       -n gem-aws-sdk-shield-devel
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Shield development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-shield
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-shield) = 1.37.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-shield-devel
AWS SDK for Ruby - AWS Shield development package.

Official AWS Ruby gem for AWS Shield. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-shield-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-shield.


%package       -n gem-aws-sdk-neptune
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Neptune
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-neptune) = 1.35.0

%description   -n gem-aws-sdk-neptune
Official AWS Ruby gem for Amazon Neptune. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-neptune-doc
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Neptune documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-neptune
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-neptune) = 1.35.0

%description   -n gem-aws-sdk-neptune-doc
AWS SDK for Ruby - Amazon Neptune documentation files.

Official AWS Ruby gem for Amazon Neptune. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-neptune-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-neptune.


%package       -n gem-aws-sdk-neptune-devel
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Neptune development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-neptune
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-neptune) = 1.35.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-neptune-devel
AWS SDK for Ruby - Amazon Neptune development package.

Official AWS Ruby gem for Amazon Neptune. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-neptune-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-neptune.


%package       -n gem-aws-sdk-robomaker
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - RoboMaker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-robomaker) = 1.36.0

%description   -n gem-aws-sdk-robomaker
Official AWS Ruby gem for AWS RoboMaker (RoboMaker). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-robomaker-doc
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - RoboMaker documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-robomaker
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-robomaker) = 1.36.0

%description   -n gem-aws-sdk-robomaker-doc
AWS SDK for Ruby - RoboMaker documentation files.

Official AWS Ruby gem for AWS RoboMaker (RoboMaker). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-robomaker-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-robomaker.


%package       -n gem-aws-sdk-robomaker-devel
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - RoboMaker development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-robomaker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-robomaker) = 1.36.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-robomaker-devel
AWS SDK for Ruby - RoboMaker development package.

Official AWS Ruby gem for AWS RoboMaker (RoboMaker). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-robomaker-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-robomaker.


%package       -n gem-aws-sdk-comprehend
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Comprehend
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-comprehend) = 1.46.0

%description   -n gem-aws-sdk-comprehend
Official AWS Ruby gem for Amazon Comprehend. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-comprehend-doc
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Comprehend documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-comprehend
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-comprehend) = 1.46.0

%description   -n gem-aws-sdk-comprehend-doc
AWS SDK for Ruby - Amazon Comprehend documentation files.

Official AWS Ruby gem for Amazon Comprehend. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-comprehend-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-comprehend.


%package       -n gem-aws-sdk-comprehend-devel
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Comprehend development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-comprehend
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-comprehend) = 1.46.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-comprehend-devel
AWS SDK for Ruby - Amazon Comprehend development package.

Official AWS Ruby gem for Amazon Comprehend. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-comprehend-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-comprehend.


%package       -n gem-aws-sdk-rds
Version:       1.119.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon RDS
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Provides:      gem(aws-sdk-rds) = 1.119.0

%description   -n gem-aws-sdk-rds
Official AWS Ruby gem for Amazon Relational Database Service (Amazon RDS). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-rds-doc
Version:       1.119.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon RDS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-rds
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-rds) = 1.119.0

%description   -n gem-aws-sdk-rds-doc
AWS SDK for Ruby - Amazon RDS documentation files.

Official AWS Ruby gem for Amazon Relational Database Service (Amazon RDS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-rds-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-rds.


%package       -n gem-aws-sdk-rds-devel
Version:       1.119.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon RDS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-rds
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-rds) = 1.119.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-rds-devel
AWS SDK for Ruby - Amazon RDS development package.

Official AWS Ruby gem for Amazon Relational Database Service (Amazon RDS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-rds-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-rds.


%package       -n gem-aws-sdk-iam
Version:       1.55.0
Release:       alt1
Summary:       AWS SDK for Ruby - IAM
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-iam) = 1.55.0

%description   -n gem-aws-sdk-iam
Official AWS Ruby gem for AWS Identity and Access Management (IAM). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-iam-doc
Version:       1.55.0
Release:       alt1
Summary:       AWS SDK for Ruby - IAM documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iam
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iam) = 1.55.0

%description   -n gem-aws-sdk-iam-doc
AWS SDK for Ruby - IAM documentation files.

Official AWS Ruby gem for AWS Identity and Access Management (IAM). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iam-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iam.


%package       -n gem-aws-sdk-iam-devel
Version:       1.55.0
Release:       alt1
Summary:       AWS SDK for Ruby - IAM development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iam
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iam) = 1.55.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-iam-devel
AWS SDK for Ruby - IAM development package.

Official AWS Ruby gem for AWS Identity and Access Management (IAM). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iam-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iam.


%package       -n gem-aws-sdk-storagegateway
Version:       1.55.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Storage Gateway
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-storagegateway) = 1.55.0

%description   -n gem-aws-sdk-storagegateway
Official AWS Ruby gem for AWS Storage Gateway. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-storagegateway-doc
Version:       1.55.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Storage Gateway documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-storagegateway
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-storagegateway) = 1.55.0

%description   -n gem-aws-sdk-storagegateway-doc
AWS SDK for Ruby - AWS Storage Gateway documentation files.

Official AWS Ruby gem for AWS Storage Gateway. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-storagegateway-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-storagegateway.


%package       -n gem-aws-sdk-storagegateway-devel
Version:       1.55.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Storage Gateway development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-storagegateway
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-storagegateway) = 1.55.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-storagegateway-devel
AWS SDK for Ruby - AWS Storage Gateway development package.

Official AWS Ruby gem for AWS Storage Gateway. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-storagegateway-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-storagegateway.


%package       -n gem-aws-sdk-cloudwatch
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudWatch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-cloudwatch) = 1.51.0

%description   -n gem-aws-sdk-cloudwatch
Official AWS Ruby gem for Amazon CloudWatch (CloudWatch). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-cloudwatch-doc
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudWatch documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudwatch
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatch) = 1.51.0

%description   -n gem-aws-sdk-cloudwatch-doc
AWS SDK for Ruby - CloudWatch documentation files.

Official AWS Ruby gem for Amazon CloudWatch (CloudWatch). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudwatch-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudwatch.


%package       -n gem-aws-sdk-cloudwatch-devel
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudWatch development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudwatch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatch) = 1.51.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-cloudwatch-devel
AWS SDK for Ruby - CloudWatch development package.

Official AWS Ruby gem for Amazon CloudWatch (CloudWatch). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudwatch-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudwatch.


%package       -n gem-aws-sdk-iotwireless
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Wireless
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-iotwireless) = 1.10.0

%description   -n gem-aws-sdk-iotwireless
Official AWS Ruby gem for AWS IoT Wireless. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-iotwireless-doc
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Wireless documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotwireless
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotwireless) = 1.10.0

%description   -n gem-aws-sdk-iotwireless-doc
AWS SDK for Ruby - AWS IoT Wireless documentation files.

Official AWS Ruby gem for AWS IoT Wireless. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-iotwireless-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotwireless.


%package       -n gem-aws-sdk-iotwireless-devel
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Wireless development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotwireless
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotwireless) = 1.10.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-iotwireless-devel
AWS SDK for Ruby - AWS IoT Wireless development package.

Official AWS Ruby gem for AWS IoT Wireless. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-iotwireless-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotwireless.


%package       -n gem-aws-partitions
Version:       1.465.0
Release:       alt1
Summary:       Provides information about AWS partitions, regions, and services
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(aws-partitions) = 1.465.0

%description   -n gem-aws-partitions
Provides interfaces to enumerate AWS partitions, regions, and services.


%package       -n gem-aws-partitions-doc
Version:       1.465.0
Release:       alt1
Summary:       Provides information about AWS partitions, regions, and services documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-partitions
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-partitions) = 1.465.0

%description   -n gem-aws-partitions-doc
Provides information about AWS partitions, regions, and services documentation
files.

Provides interfaces to enumerate AWS partitions, regions, and services.

%description   -n gem-aws-partitions-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-partitions.


%package       -n gem-aws-sdk-eks
Version:       1.55.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EKS
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-eks) = 1.55.0

%description   -n gem-aws-sdk-eks
Official AWS Ruby gem for Amazon Elastic Kubernetes Service (Amazon EKS). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-eks-doc
Version:       1.55.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EKS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-eks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-eks) = 1.55.0

%description   -n gem-aws-sdk-eks-doc
AWS SDK for Ruby - Amazon EKS documentation files.

Official AWS Ruby gem for Amazon Elastic Kubernetes Service (Amazon EKS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-eks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-eks.


%package       -n gem-aws-sdk-eks-devel
Version:       1.55.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EKS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-eks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-eks) = 1.55.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-eks-devel
AWS SDK for Ruby - Amazon EKS development package.

Official AWS Ruby gem for Amazon Elastic Kubernetes Service (Amazon EKS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-eks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-eks.


%package       -n gem-aws-sdk-iotanalytics
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Analytics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-iotanalytics) = 1.38.0

%description   -n gem-aws-sdk-iotanalytics
Official AWS Ruby gem for AWS IoT Analytics. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-iotanalytics-doc
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Analytics documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotanalytics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotanalytics) = 1.38.0

%description   -n gem-aws-sdk-iotanalytics-doc
AWS SDK for Ruby - AWS IoT Analytics documentation files.

Official AWS Ruby gem for AWS IoT Analytics. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-iotanalytics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotanalytics.


%package       -n gem-aws-sdk-iotanalytics-devel
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Analytics development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotanalytics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotanalytics) = 1.38.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-iotanalytics-devel
AWS SDK for Ruby - AWS IoT Analytics development package.

Official AWS Ruby gem for AWS IoT Analytics. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-iotanalytics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotanalytics.


%package       -n gem-aws-sdk-mturk
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon MTurk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-mturk) = 1.31.0

%description   -n gem-aws-sdk-mturk
Official AWS Ruby gem for Amazon Mechanical Turk (Amazon MTurk). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mturk-doc
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon MTurk documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mturk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mturk) = 1.31.0

%description   -n gem-aws-sdk-mturk-doc
AWS SDK for Ruby - Amazon MTurk documentation files.

Official AWS Ruby gem for Amazon Mechanical Turk (Amazon MTurk). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mturk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mturk.


%package       -n gem-aws-sdk-mturk-devel
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon MTurk development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mturk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mturk) = 1.31.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-mturk-devel
AWS SDK for Ruby - Amazon MTurk development package.

Official AWS Ruby gem for Amazon Mechanical Turk (Amazon MTurk). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mturk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mturk.


%package       -n gem-aws-sdk-cognitoidentityprovider
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Cognito Identity Provider
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-cognitoidentityprovider) = 1.51.0

%description   -n gem-aws-sdk-cognitoidentityprovider
Official AWS Ruby gem for Amazon Cognito Identity Provider. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-cognitoidentityprovider-doc
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Cognito Identity Provider documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cognitoidentityprovider
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cognitoidentityprovider) = 1.51.0

%description   -n gem-aws-sdk-cognitoidentityprovider-doc
AWS SDK for Ruby - Amazon Cognito Identity Provider documentation
files.

Official AWS Ruby gem for Amazon Cognito Identity Provider. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cognitoidentityprovider-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cognitoidentityprovider.


%package       -n gem-aws-sdk-cognitoidentityprovider-devel
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Cognito Identity Provider development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cognitoidentityprovider
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cognitoidentityprovider) = 1.51.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-cognitoidentityprovider-devel
AWS SDK for Ruby - Amazon Cognito Identity Provider development
package.

Official AWS Ruby gem for Amazon Cognito Identity Provider. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cognitoidentityprovider-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cognitoidentityprovider.


%package       -n gem-aws-sdk-elasticbeanstalk
Version:       1.42.0
Release:       alt1
Summary:       AWS SDK for Ruby - Elastic Beanstalk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-elasticbeanstalk) = 1.42.0

%description   -n gem-aws-sdk-elasticbeanstalk
Official AWS Ruby gem for AWS Elastic Beanstalk (Elastic Beanstalk). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-elasticbeanstalk-doc
Version:       1.42.0
Release:       alt1
Summary:       AWS SDK for Ruby - Elastic Beanstalk documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-elasticbeanstalk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticbeanstalk) = 1.42.0

%description   -n gem-aws-sdk-elasticbeanstalk-doc
AWS SDK for Ruby - Elastic Beanstalk documentation files.

Official AWS Ruby gem for AWS Elastic Beanstalk (Elastic Beanstalk). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-elasticbeanstalk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-elasticbeanstalk.


%package       -n gem-aws-sdk-elasticbeanstalk-devel
Version:       1.42.0
Release:       alt1
Summary:       AWS SDK for Ruby - Elastic Beanstalk development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-elasticbeanstalk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticbeanstalk) = 1.42.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-elasticbeanstalk-devel
AWS SDK for Ruby - Elastic Beanstalk development package.

Official AWS Ruby gem for AWS Elastic Beanstalk (Elastic Beanstalk). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-elasticbeanstalk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-elasticbeanstalk.


%package       -n gem-aws-sdk-fsx
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon FSx
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-fsx) = 1.37.0

%description   -n gem-aws-sdk-fsx
Official AWS Ruby gem for Amazon FSx. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-fsx-doc
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon FSx documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-fsx
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-fsx) = 1.37.0

%description   -n gem-aws-sdk-fsx-doc
AWS SDK for Ruby - Amazon FSx documentation files.

Official AWS Ruby gem for Amazon FSx. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-fsx-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-fsx.


%package       -n gem-aws-sdk-fsx-devel
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon FSx development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-fsx
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-fsx) = 1.37.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-fsx-devel
AWS SDK for Ruby - Amazon FSx development package.

Official AWS Ruby gem for Amazon FSx. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-fsx-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-fsx.


%package       -n gem-aws-sdk-clouddirectory
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudDirectory
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-clouddirectory) = 1.31.0

%description   -n gem-aws-sdk-clouddirectory
Official AWS Ruby gem for Amazon CloudDirectory. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-clouddirectory-doc
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudDirectory documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-clouddirectory
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-clouddirectory) = 1.31.0

%description   -n gem-aws-sdk-clouddirectory-doc
AWS SDK for Ruby - Amazon CloudDirectory documentation files.

Official AWS Ruby gem for Amazon CloudDirectory. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-clouddirectory-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-clouddirectory.


%package       -n gem-aws-sdk-clouddirectory-devel
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudDirectory development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-clouddirectory
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-clouddirectory) = 1.31.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-clouddirectory-devel
AWS SDK for Ruby - Amazon CloudDirectory development package.

Official AWS Ruby gem for Amazon CloudDirectory. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-clouddirectory-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-clouddirectory.


%package       -n gem-aws-sdk-efs
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - EFS
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-efs) = 1.40.0

%description   -n gem-aws-sdk-efs
Official AWS Ruby gem for Amazon Elastic File System (EFS). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-efs-doc
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - EFS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-efs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-efs) = 1.40.0

%description   -n gem-aws-sdk-efs-doc
AWS SDK for Ruby - EFS documentation files.

Official AWS Ruby gem for Amazon Elastic File System (EFS). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-efs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-efs.


%package       -n gem-aws-sdk-efs-devel
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - EFS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-efs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-efs) = 1.40.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-efs-devel
AWS SDK for Ruby - EFS development package.

Official AWS Ruby gem for Amazon Elastic File System (EFS). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-efs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-efs.


%package       -n gem-aws-sdk-sagemakerfeaturestoreruntime
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SageMaker Feature Store Runtime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-sagemakerfeaturestoreruntime) = 1.2.0

%description   -n gem-aws-sdk-sagemakerfeaturestoreruntime
Official AWS Ruby gem for Amazon SageMaker Feature Store Runtime. This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-sagemakerfeaturestoreruntime-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SageMaker Feature Store Runtime documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sagemakerfeaturestoreruntime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakerfeaturestoreruntime) = 1.2.0

%description   -n gem-aws-sdk-sagemakerfeaturestoreruntime-doc
AWS SDK for Ruby - Amazon SageMaker Feature Store Runtime documentation
files.

Official AWS Ruby gem for Amazon SageMaker Feature Store Runtime. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sagemakerfeaturestoreruntime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sagemakerfeaturestoreruntime.


%package       -n gem-aws-sdk-sagemakerfeaturestoreruntime-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SageMaker Feature Store Runtime development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sagemakerfeaturestoreruntime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakerfeaturestoreruntime) = 1.2.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-sagemakerfeaturestoreruntime-devel
AWS SDK for Ruby - Amazon SageMaker Feature Store Runtime development
package.

Official AWS Ruby gem for Amazon SageMaker Feature Store Runtime. This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sagemakerfeaturestoreruntime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sagemakerfeaturestoreruntime.


%package       -n gem-aws-sdk-lookoutforvision
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Lookout for Vision
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-lookoutforvision) = 1.3.0

%description   -n gem-aws-sdk-lookoutforvision
Official AWS Ruby gem for Amazon Lookout for Vision. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-lookoutforvision-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Lookout for Vision documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lookoutforvision
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lookoutforvision) = 1.3.0

%description   -n gem-aws-sdk-lookoutforvision-doc
AWS SDK for Ruby - Amazon Lookout for Vision documentation files.

Official AWS Ruby gem for Amazon Lookout for Vision. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-lookoutforvision-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lookoutforvision.


%package       -n gem-aws-sdk-lookoutforvision-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Lookout for Vision development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lookoutforvision
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lookoutforvision) = 1.3.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-lookoutforvision-devel
AWS SDK for Ruby - Amazon Lookout for Vision development package.

Official AWS Ruby gem for Amazon Lookout for Vision. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-lookoutforvision-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lookoutforvision.


%package       -n gem-aws-sdk-mgn
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - mgn
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-mgn) = 1.0.0

%description   -n gem-aws-sdk-mgn
Official AWS Ruby gem for Application Migration Service (mgn). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mgn-doc
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - mgn documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mgn
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mgn) = 1.0.0

%description   -n gem-aws-sdk-mgn-doc
AWS SDK for Ruby - mgn documentation files.

Official AWS Ruby gem for Application Migration Service (mgn). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mgn-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mgn.


%package       -n gem-aws-sdk-mgn-devel
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - mgn development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mgn
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mgn) = 1.0.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-mgn-devel
AWS SDK for Ruby - mgn development package.

Official AWS Ruby gem for Application Migration Service (mgn). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mgn-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mgn.


%package       -n gem-aws-sdk-honeycode
Version:       1.6.0
Release:       alt1
Summary:       AWS SDK for Ruby - Honeycode
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-honeycode) = 1.6.0

%description   -n gem-aws-sdk-honeycode
Official AWS Ruby gem for Amazon Honeycode (Honeycode). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-honeycode-doc
Version:       1.6.0
Release:       alt1
Summary:       AWS SDK for Ruby - Honeycode documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-honeycode
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-honeycode) = 1.6.0

%description   -n gem-aws-sdk-honeycode-doc
AWS SDK for Ruby - Honeycode documentation files.

Official AWS Ruby gem for Amazon Honeycode (Honeycode). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-honeycode-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-honeycode.


%package       -n gem-aws-sdk-honeycode-devel
Version:       1.6.0
Release:       alt1
Summary:       AWS SDK for Ruby - Honeycode development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-honeycode
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-honeycode) = 1.6.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-honeycode-devel
AWS SDK for Ruby - Honeycode development package.

Official AWS Ruby gem for Amazon Honeycode (Honeycode). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-honeycode-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-honeycode.


%package       -n gem-aws-sdk-marketplacecatalog
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Marketplace Catalog
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-marketplacecatalog) = 1.12.0

%description   -n gem-aws-sdk-marketplacecatalog
Official AWS Ruby gem for AWS Marketplace Catalog Service (AWS Marketplace
Catalog). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-marketplacecatalog-doc
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Marketplace Catalog documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-marketplacecatalog
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplacecatalog) = 1.12.0

%description   -n gem-aws-sdk-marketplacecatalog-doc
AWS SDK for Ruby - AWS Marketplace Catalog documentation files.

Official AWS Ruby gem for AWS Marketplace Catalog Service (AWS Marketplace
Catalog). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-marketplacecatalog-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-marketplacecatalog.


%package       -n gem-aws-sdk-marketplacecatalog-devel
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Marketplace Catalog development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-marketplacecatalog
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplacecatalog) = 1.12.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-marketplacecatalog-devel
AWS SDK for Ruby - AWS Marketplace Catalog development package.

Official AWS Ruby gem for AWS Marketplace Catalog Service (AWS Marketplace
Catalog). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-marketplacecatalog-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-marketplacecatalog.


%package       -n gem-aws-sdk-appintegrationsservice
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon AppIntegrations Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-appintegrationsservice) = 1.2.0

%description   -n gem-aws-sdk-appintegrationsservice
Official AWS Ruby gem for Amazon AppIntegrations Service. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-appintegrationsservice-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon AppIntegrations Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appintegrationsservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appintegrationsservice) = 1.2.0

%description   -n gem-aws-sdk-appintegrationsservice-doc
AWS SDK for Ruby - Amazon AppIntegrations Service documentation files.

Official AWS Ruby gem for Amazon AppIntegrations Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-appintegrationsservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appintegrationsservice.


%package       -n gem-aws-sdk-appintegrationsservice-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon AppIntegrations Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appintegrationsservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appintegrationsservice) = 1.2.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-appintegrationsservice-devel
AWS SDK for Ruby - Amazon AppIntegrations Service development package.

Official AWS Ruby gem for Amazon AppIntegrations Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-appintegrationsservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appintegrationsservice.


%package       -n gem-aws-sdk-cloudsearch
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudSearch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-cloudsearch) = 1.29.0

%description   -n gem-aws-sdk-cloudsearch
Official AWS Ruby gem for Amazon CloudSearch. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-cloudsearch-doc
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudSearch documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudsearch
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudsearch) = 1.29.0

%description   -n gem-aws-sdk-cloudsearch-doc
AWS SDK for Ruby - Amazon CloudSearch documentation files.

Official AWS Ruby gem for Amazon CloudSearch. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-cloudsearch-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudsearch.


%package       -n gem-aws-sdk-cloudsearch-devel
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudSearch development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudsearch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudsearch) = 1.29.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-cloudsearch-devel
AWS SDK for Ruby - Amazon CloudSearch development package.

Official AWS Ruby gem for Amazon CloudSearch. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-cloudsearch-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudsearch.


%package       -n gem-aws-sigv4
Version:       1.2.3
Release:       alt1
Summary:       AWS Signature Version 4 library
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-eventstream) >= 1.0.2 gem(aws-eventstream) < 2
Provides:      gem(aws-sigv4) = 1.2.3

%description   -n gem-aws-sigv4
Amazon Web Services Signature Version 4 signing library. Generates sigv4
signature for HTTP requests.


%package       -n gem-aws-sigv4-doc
Version:       1.2.3
Release:       alt1
Summary:       AWS Signature Version 4 library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sigv4
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sigv4) = 1.2.3

%description   -n gem-aws-sigv4-doc
AWS Signature Version 4 library documentation files.

Amazon Web Services Signature Version 4 signing library. Generates sigv4
signature for HTTP requests.

%description   -n gem-aws-sigv4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sigv4.


%package       -n gem-aws-sigv4-devel
Version:       1.2.3
Release:       alt1
Summary:       AWS Signature Version 4 library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sigv4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sigv4) = 1.2.3
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sigv4-devel
AWS Signature Version 4 library development package.

Amazon Web Services Signature Version 4 signing library. Generates sigv4
signature for HTTP requests.

%description   -n gem-aws-sigv4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sigv4.


%package       -n gem-aws-sdk-codeguruprofiler
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CodeGuru Profiler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-codeguruprofiler) = 1.15.0

%description   -n gem-aws-sdk-codeguruprofiler
Official AWS Ruby gem for Amazon CodeGuru Profiler. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-codeguruprofiler-doc
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CodeGuru Profiler documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codeguruprofiler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codeguruprofiler) = 1.15.0

%description   -n gem-aws-sdk-codeguruprofiler-doc
AWS SDK for Ruby - Amazon CodeGuru Profiler documentation files.

Official AWS Ruby gem for Amazon CodeGuru Profiler. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-codeguruprofiler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codeguruprofiler.


%package       -n gem-aws-sdk-codeguruprofiler-devel
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CodeGuru Profiler development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codeguruprofiler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codeguruprofiler) = 1.15.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-codeguruprofiler-devel
AWS SDK for Ruby - Amazon CodeGuru Profiler development package.

Official AWS Ruby gem for Amazon CodeGuru Profiler. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-codeguruprofiler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codeguruprofiler.


%package       -n gem-aws-sdk-states
Version:       1.39.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS SFN
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-states) = 1.39.0

%description   -n gem-aws-sdk-states
Official AWS Ruby gem for AWS Step Functions (AWS SFN). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-states-doc
Version:       1.39.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS SFN documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-states
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-states) = 1.39.0

%description   -n gem-aws-sdk-states-doc
AWS SDK for Ruby - AWS SFN documentation files.

Official AWS Ruby gem for AWS Step Functions (AWS SFN). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-states-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-states.


%package       -n gem-aws-sdk-states-devel
Version:       1.39.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS SFN development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-states
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-states) = 1.39.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-states-devel
AWS SDK for Ruby - AWS SFN development package.

Official AWS Ruby gem for AWS Step Functions (AWS SFN). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-states-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-states.


%package       -n gem-aws-sdk-cloud9
Version:       1.33.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Cloud9
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-cloud9) = 1.33.0

%description   -n gem-aws-sdk-cloud9
Official AWS Ruby gem for AWS Cloud9. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-cloud9-doc
Version:       1.33.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Cloud9 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloud9
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloud9) = 1.33.0

%description   -n gem-aws-sdk-cloud9-doc
AWS SDK for Ruby - AWS Cloud9 documentation files.

Official AWS Ruby gem for AWS Cloud9. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloud9-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloud9.


%package       -n gem-aws-sdk-cloud9-devel
Version:       1.33.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Cloud9 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloud9
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloud9) = 1.33.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-cloud9-devel
AWS SDK for Ruby - AWS Cloud9 development package.

Official AWS Ruby gem for AWS Cloud9. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloud9-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloud9.


%package       -n gem-aws-sdk-codestarconnections
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS CodeStar connections
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-codestarconnections) = 1.15.0

%description   -n gem-aws-sdk-codestarconnections
Official AWS Ruby gem for AWS CodeStar connections. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-codestarconnections-doc
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS CodeStar connections documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codestarconnections
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codestarconnections) = 1.15.0

%description   -n gem-aws-sdk-codestarconnections-doc
AWS SDK for Ruby - AWS CodeStar connections documentation files.

Official AWS Ruby gem for AWS CodeStar connections. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-codestarconnections-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codestarconnections.


%package       -n gem-aws-sdk-codestarconnections-devel
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS CodeStar connections development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codestarconnections
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codestarconnections) = 1.15.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-codestarconnections-devel
AWS SDK for Ruby - AWS CodeStar connections development package.

Official AWS Ruby gem for AWS CodeStar connections. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-codestarconnections-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codestarconnections.


%package       -n gem-aws-sdk-codegurureviewer
Version:       1.17.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeGuruReviewer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-codegurureviewer) = 1.17.0

%description   -n gem-aws-sdk-codegurureviewer
Official AWS Ruby gem for Amazon CodeGuru Reviewer (CodeGuruReviewer). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-codegurureviewer-doc
Version:       1.17.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeGuruReviewer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codegurureviewer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codegurureviewer) = 1.17.0

%description   -n gem-aws-sdk-codegurureviewer-doc
AWS SDK for Ruby - CodeGuruReviewer documentation files.

Official AWS Ruby gem for Amazon CodeGuru Reviewer (CodeGuruReviewer). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-codegurureviewer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codegurureviewer.


%package       -n gem-aws-sdk-codegurureviewer-devel
Version:       1.17.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeGuruReviewer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codegurureviewer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codegurureviewer) = 1.17.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-codegurureviewer-devel
AWS SDK for Ruby - CodeGuruReviewer development package.

Official AWS Ruby gem for Amazon CodeGuru Reviewer (CodeGuruReviewer). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-codegurureviewer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codegurureviewer.


%package       -n gem-aws-sdk-iotdeviceadvisor
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSIoTDeviceAdvisor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-iotdeviceadvisor) = 1.3.0

%description   -n gem-aws-sdk-iotdeviceadvisor
Official AWS Ruby gem for AWS IoT Core Device Advisor (AWSIoTDeviceAdvisor).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-iotdeviceadvisor-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSIoTDeviceAdvisor documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotdeviceadvisor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotdeviceadvisor) = 1.3.0

%description   -n gem-aws-sdk-iotdeviceadvisor-doc
AWS SDK for Ruby - AWSIoTDeviceAdvisor documentation files.

Official AWS Ruby gem for AWS IoT Core Device Advisor (AWSIoTDeviceAdvisor).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iotdeviceadvisor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotdeviceadvisor.


%package       -n gem-aws-sdk-iotdeviceadvisor-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSIoTDeviceAdvisor development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotdeviceadvisor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotdeviceadvisor) = 1.3.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-iotdeviceadvisor-devel
AWS SDK for Ruby - AWSIoTDeviceAdvisor development package.

Official AWS Ruby gem for AWS IoT Core Device Advisor (AWSIoTDeviceAdvisor).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iotdeviceadvisor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotdeviceadvisor.


%package       -n gem-aws-sdk-cloudhsmv2
Version:       1.33.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudHSM V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-cloudhsmv2) = 1.33.0

%description   -n gem-aws-sdk-cloudhsmv2
Official AWS Ruby gem for AWS CloudHSM V2 (CloudHSM V2). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-cloudhsmv2-doc
Version:       1.33.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudHSM V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudhsmv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudhsmv2) = 1.33.0

%description   -n gem-aws-sdk-cloudhsmv2-doc
AWS SDK for Ruby - CloudHSM V2 documentation files.

Official AWS Ruby gem for AWS CloudHSM V2 (CloudHSM V2). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudhsmv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudhsmv2.


%package       -n gem-aws-sdk-cloudhsmv2-devel
Version:       1.33.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudHSM V2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudhsmv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudhsmv2) = 1.33.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-cloudhsmv2-devel
AWS SDK for Ruby - CloudHSM V2 development package.

Official AWS Ruby gem for AWS CloudHSM V2 (CloudHSM V2). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudhsmv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudhsmv2.


%package       -n gem-aws-sdk-opsworks
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS OpsWorks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-opsworks) = 1.32.0

%description   -n gem-aws-sdk-opsworks
Official AWS Ruby gem for AWS OpsWorks. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-opsworks-doc
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS OpsWorks documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-opsworks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-opsworks) = 1.32.0

%description   -n gem-aws-sdk-opsworks-doc
AWS SDK for Ruby - AWS OpsWorks documentation files.

Official AWS Ruby gem for AWS OpsWorks. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-opsworks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-opsworks.


%package       -n gem-aws-sdk-opsworks-devel
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS OpsWorks development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-opsworks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-opsworks) = 1.32.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-opsworks-devel
AWS SDK for Ruby - AWS OpsWorks development package.

Official AWS Ruby gem for AWS OpsWorks. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-opsworks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-opsworks.


%package       -n gem-aws-sdk-iotdataplane
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Data Plane
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-iotdataplane) = 1.28.0

%description   -n gem-aws-sdk-iotdataplane
Official AWS Ruby gem for AWS IoT Data Plane. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-iotdataplane-doc
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Data Plane documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotdataplane
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotdataplane) = 1.28.0

%description   -n gem-aws-sdk-iotdataplane-doc
AWS SDK for Ruby - AWS IoT Data Plane documentation files.

Official AWS Ruby gem for AWS IoT Data Plane. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-iotdataplane-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotdataplane.


%package       -n gem-aws-sdk-iotdataplane-devel
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Data Plane development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotdataplane
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotdataplane) = 1.28.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-iotdataplane-devel
AWS SDK for Ruby - AWS IoT Data Plane development package.

Official AWS Ruby gem for AWS IoT Data Plane. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-iotdataplane-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotdataplane.


%package       -n gem-aws-sdk-dataexchange
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Data Exchange
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-dataexchange) = 1.13.0

%description   -n gem-aws-sdk-dataexchange
Official AWS Ruby gem for AWS Data Exchange. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-dataexchange-doc
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Data Exchange documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-dataexchange
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-dataexchange) = 1.13.0

%description   -n gem-aws-sdk-dataexchange-doc
AWS SDK for Ruby - AWS Data Exchange documentation files.

Official AWS Ruby gem for AWS Data Exchange. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-dataexchange-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-dataexchange.


%package       -n gem-aws-sdk-dataexchange-devel
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Data Exchange development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-dataexchange
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-dataexchange) = 1.13.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-dataexchange-devel
AWS SDK for Ruby - AWS Data Exchange development package.

Official AWS Ruby gem for AWS Data Exchange. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-dataexchange-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-dataexchange.


%package       -n gem-aws-sdk-qldbsession
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - QLDB Session
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-qldbsession) = 1.13.0

%description   -n gem-aws-sdk-qldbsession
Official AWS Ruby gem for Amazon QLDB Session (QLDB Session). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-qldbsession-doc
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - QLDB Session documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-qldbsession
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-qldbsession) = 1.13.0

%description   -n gem-aws-sdk-qldbsession-doc
AWS SDK for Ruby - QLDB Session documentation files.

Official AWS Ruby gem for Amazon QLDB Session (QLDB Session). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-qldbsession-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-qldbsession.


%package       -n gem-aws-sdk-qldbsession-devel
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - QLDB Session development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-qldbsession
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-qldbsession) = 1.13.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-qldbsession-devel
AWS SDK for Ruby - QLDB Session development package.

Official AWS Ruby gem for Amazon QLDB Session (QLDB Session). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-qldbsession-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-qldbsession.


%package       -n gem-aws-sdk-mediatailor
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaTailor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-mediatailor) = 1.38.0

%description   -n gem-aws-sdk-mediatailor
Official AWS Ruby gem for AWS MediaTailor (MediaTailor). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-mediatailor-doc
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaTailor documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mediatailor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mediatailor) = 1.38.0

%description   -n gem-aws-sdk-mediatailor-doc
AWS SDK for Ruby - MediaTailor documentation files.

Official AWS Ruby gem for AWS MediaTailor (MediaTailor). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediatailor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mediatailor.


%package       -n gem-aws-sdk-mediatailor-devel
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaTailor development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mediatailor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mediatailor) = 1.38.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-mediatailor-devel
AWS SDK for Ruby - MediaTailor development package.

Official AWS Ruby gem for AWS MediaTailor (MediaTailor). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediatailor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mediatailor.


%package       -n gem-aws-sdk-timestreamquery
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Timestream Query
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-timestreamquery) = 1.4.0

%description   -n gem-aws-sdk-timestreamquery
Official AWS Ruby gem for Amazon Timestream Query (Timestream Query). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-timestreamquery-doc
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Timestream Query documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-timestreamquery
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-timestreamquery) = 1.4.0

%description   -n gem-aws-sdk-timestreamquery-doc
AWS SDK for Ruby - Timestream Query documentation files.

Official AWS Ruby gem for Amazon Timestream Query (Timestream Query). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-timestreamquery-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-timestreamquery.


%package       -n gem-aws-sdk-timestreamquery-devel
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Timestream Query development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-timestreamquery
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-timestreamquery) = 1.4.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-timestreamquery-devel
AWS SDK for Ruby - Timestream Query development package.

Official AWS Ruby gem for Amazon Timestream Query (Timestream Query). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-timestreamquery-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-timestreamquery.


%package       -n gem-aws-sdk-translate
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Translate
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-translate) = 1.31.0

%description   -n gem-aws-sdk-translate
Official AWS Ruby gem for Amazon Translate. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-translate-doc
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Translate documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-translate
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-translate) = 1.31.0

%description   -n gem-aws-sdk-translate-doc
AWS SDK for Ruby - Amazon Translate documentation files.

Official AWS Ruby gem for Amazon Translate. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-translate-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-translate.


%package       -n gem-aws-sdk-translate-devel
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Translate development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-translate
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-translate) = 1.31.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-translate-devel
AWS SDK for Ruby - Amazon Translate development package.

Official AWS Ruby gem for Amazon Translate. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-translate-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-translate.


%package       -n gem-aws-sdk-workmail
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkMail
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-workmail) = 1.37.0

%description   -n gem-aws-sdk-workmail
Official AWS Ruby gem for Amazon WorkMail. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-workmail-doc
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkMail documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-workmail
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-workmail) = 1.37.0

%description   -n gem-aws-sdk-workmail-doc
AWS SDK for Ruby - Amazon WorkMail documentation files.

Official AWS Ruby gem for Amazon WorkMail. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-workmail-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-workmail.


%package       -n gem-aws-sdk-workmail-devel
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkMail development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-workmail
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-workmail) = 1.37.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-workmail-devel
AWS SDK for Ruby - Amazon WorkMail development package.

Official AWS Ruby gem for Amazon WorkMail. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-workmail-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-workmail.


%package       -n gem-aws-sdk-transfer
Version:       1.33.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Transfer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-transfer) = 1.33.0

%description   -n gem-aws-sdk-transfer
Official AWS Ruby gem for AWS Transfer Family (AWS Transfer). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-transfer-doc
Version:       1.33.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Transfer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-transfer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-transfer) = 1.33.0

%description   -n gem-aws-sdk-transfer-doc
AWS SDK for Ruby - AWS Transfer documentation files.

Official AWS Ruby gem for AWS Transfer Family (AWS Transfer). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-transfer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-transfer.


%package       -n gem-aws-sdk-transfer-devel
Version:       1.33.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Transfer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-transfer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-transfer) = 1.33.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-transfer-devel
AWS SDK for Ruby - AWS Transfer development package.

Official AWS Ruby gem for AWS Transfer Family (AWS Transfer). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-transfer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-transfer.


%package       -n gem-aws-sdk-ioteventsdata
Version:       1.16.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Events Data
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-ioteventsdata) = 1.16.0

%description   -n gem-aws-sdk-ioteventsdata
Official AWS Ruby gem for AWS IoT Events Data. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-ioteventsdata-doc
Version:       1.16.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Events Data documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ioteventsdata
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ioteventsdata) = 1.16.0

%description   -n gem-aws-sdk-ioteventsdata-doc
AWS SDK for Ruby - AWS IoT Events Data documentation files.

Official AWS Ruby gem for AWS IoT Events Data. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-ioteventsdata-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ioteventsdata.


%package       -n gem-aws-sdk-ioteventsdata-devel
Version:       1.16.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Events Data development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ioteventsdata
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ioteventsdata) = 1.16.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ioteventsdata-devel
AWS SDK for Ruby - AWS IoT Events Data development package.

Official AWS Ruby gem for AWS IoT Events Data. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-ioteventsdata-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ioteventsdata.


%package       -n gem-aws-sdk-kms
Version:       1.43.0
Release:       alt1
Summary:       AWS SDK for Ruby - KMS
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-kms) = 1.43.0

%description   -n gem-aws-sdk-kms
Official AWS Ruby gem for AWS Key Management Service (KMS). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kms-doc
Version:       1.43.0
Release:       alt1
Summary:       AWS SDK for Ruby - KMS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kms
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kms) = 1.43.0

%description   -n gem-aws-sdk-kms-doc
AWS SDK for Ruby - KMS documentation files.

Official AWS Ruby gem for AWS Key Management Service (KMS). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kms-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kms.


%package       -n gem-aws-sdk-kms-devel
Version:       1.43.0
Release:       alt1
Summary:       AWS SDK for Ruby - KMS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kms
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kms) = 1.43.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-kms-devel
AWS SDK for Ruby - KMS development package.

Official AWS Ruby gem for AWS Key Management Service (KMS). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kms-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kms.


%package       -n gem-aws-sdk-frauddetector
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Fraud Detector
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-frauddetector) = 1.18.0

%description   -n gem-aws-sdk-frauddetector
Official AWS Ruby gem for Amazon Fraud Detector. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-frauddetector-doc
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Fraud Detector documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-frauddetector
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-frauddetector) = 1.18.0

%description   -n gem-aws-sdk-frauddetector-doc
AWS SDK for Ruby - Amazon Fraud Detector documentation files.

Official AWS Ruby gem for Amazon Fraud Detector. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-frauddetector-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-frauddetector.


%package       -n gem-aws-sdk-frauddetector-devel
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Fraud Detector development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-frauddetector
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-frauddetector) = 1.18.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-frauddetector-devel
AWS SDK for Ruby - Amazon Fraud Detector development package.

Official AWS Ruby gem for Amazon Fraud Detector. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-frauddetector-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-frauddetector.


%package       -n gem-aws-sdk-lexmodelsv2
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Lex Models V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-lexmodelsv2) = 1.4.0

%description   -n gem-aws-sdk-lexmodelsv2
Official AWS Ruby gem for Amazon Lex Model Building V2 (Lex Models V2). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-lexmodelsv2-doc
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Lex Models V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lexmodelsv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lexmodelsv2) = 1.4.0

%description   -n gem-aws-sdk-lexmodelsv2-doc
AWS SDK for Ruby - Lex Models V2 documentation files.

Official AWS Ruby gem for Amazon Lex Model Building V2 (Lex Models V2). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lexmodelsv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lexmodelsv2.


%package       -n gem-aws-sdk-lexmodelsv2-devel
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Lex Models V2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lexmodelsv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lexmodelsv2) = 1.4.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-lexmodelsv2-devel
AWS SDK for Ruby - Lex Models V2 development package.

Official AWS Ruby gem for Amazon Lex Model Building V2 (Lex Models V2). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lexmodelsv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lexmodelsv2.


%package       -n gem-aws-sdk-healthlake
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - HealthLake
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-healthlake) = 1.3.0

%description   -n gem-aws-sdk-healthlake
Official AWS Ruby gem for Amazon HealthLake (HealthLake). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-healthlake-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - HealthLake documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-healthlake
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-healthlake) = 1.3.0

%description   -n gem-aws-sdk-healthlake-doc
AWS SDK for Ruby - HealthLake documentation files.

Official AWS Ruby gem for Amazon HealthLake (HealthLake). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-healthlake-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-healthlake.


%package       -n gem-aws-sdk-healthlake-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - HealthLake development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-healthlake
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-healthlake) = 1.3.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-healthlake-devel
AWS SDK for Ruby - HealthLake development package.

Official AWS Ruby gem for Amazon HealthLake (HealthLake). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-healthlake-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-healthlake.


%package       -n gem-aws-sdk-gluedatabrew
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Glue DataBrew
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-gluedatabrew) = 1.7.0

%description   -n gem-aws-sdk-gluedatabrew
Official AWS Ruby gem for AWS Glue DataBrew. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-gluedatabrew-doc
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Glue DataBrew documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-gluedatabrew
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-gluedatabrew) = 1.7.0

%description   -n gem-aws-sdk-gluedatabrew-doc
AWS SDK for Ruby - AWS Glue DataBrew documentation files.

Official AWS Ruby gem for AWS Glue DataBrew. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-gluedatabrew-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-gluedatabrew.


%package       -n gem-aws-sdk-gluedatabrew-devel
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Glue DataBrew development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-gluedatabrew
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-gluedatabrew) = 1.7.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-gluedatabrew-devel
AWS SDK for Ruby - AWS Glue DataBrew development package.

Official AWS Ruby gem for AWS Glue DataBrew. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-gluedatabrew-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-gluedatabrew.


%package       -n gem-aws-sdk-migrationhubconfig
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Migration Hub Config
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-migrationhubconfig) = 1.11.0

%description   -n gem-aws-sdk-migrationhubconfig
Official AWS Ruby gem for AWS Migration Hub Config. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-migrationhubconfig-doc
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Migration Hub Config documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-migrationhubconfig
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-migrationhubconfig) = 1.11.0

%description   -n gem-aws-sdk-migrationhubconfig-doc
AWS SDK for Ruby - AWS Migration Hub Config documentation files.

Official AWS Ruby gem for AWS Migration Hub Config. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-migrationhubconfig-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-migrationhubconfig.


%package       -n gem-aws-sdk-migrationhubconfig-devel
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Migration Hub Config development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-migrationhubconfig
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-migrationhubconfig) = 1.11.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-migrationhubconfig-devel
AWS SDK for Ruby - AWS Migration Hub Config development package.

Official AWS Ruby gem for AWS Migration Hub Config. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-migrationhubconfig-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-migrationhubconfig.


%package       -n gem-aws-sdk-networkmanager
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - NetworkManager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-networkmanager) = 1.11.0

%description   -n gem-aws-sdk-networkmanager
Official AWS Ruby gem for AWS Network Manager (NetworkManager). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-networkmanager-doc
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - NetworkManager documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-networkmanager
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-networkmanager) = 1.11.0

%description   -n gem-aws-sdk-networkmanager-doc
AWS SDK for Ruby - NetworkManager documentation files.

Official AWS Ruby gem for AWS Network Manager (NetworkManager). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-networkmanager-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-networkmanager.


%package       -n gem-aws-sdk-networkmanager-devel
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - NetworkManager development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-networkmanager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-networkmanager) = 1.11.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-networkmanager-devel
AWS SDK for Ruby - NetworkManager development package.

Official AWS Ruby gem for AWS Network Manager (NetworkManager). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-networkmanager-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-networkmanager.


%package       -n gem-aws-sdk-kinesisanalytics
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Analytics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-kinesisanalytics) = 1.31.0

%description   -n gem-aws-sdk-kinesisanalytics
Official AWS Ruby gem for Amazon Kinesis Analytics (Kinesis Analytics). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kinesisanalytics-doc
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Analytics documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesisanalytics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisanalytics) = 1.31.0

%description   -n gem-aws-sdk-kinesisanalytics-doc
AWS SDK for Ruby - Kinesis Analytics documentation files.

Official AWS Ruby gem for Amazon Kinesis Analytics (Kinesis Analytics). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisanalytics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesisanalytics.


%package       -n gem-aws-sdk-kinesisanalytics-devel
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Analytics development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesisanalytics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisanalytics) = 1.31.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-kinesisanalytics-devel
AWS SDK for Ruby - Kinesis Analytics development package.

Official AWS Ruby gem for Amazon Kinesis Analytics (Kinesis Analytics). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisanalytics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesisanalytics.


%package       -n gem-aws-sdk-redshiftdataapiservice
Version:       1.6.0
Release:       alt1
Summary:       AWS SDK for Ruby - Redshift Data API Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-redshiftdataapiservice) = 1.6.0

%description   -n gem-aws-sdk-redshiftdataapiservice
Official AWS Ruby gem for Redshift Data API Service. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-redshiftdataapiservice-doc
Version:       1.6.0
Release:       alt1
Summary:       AWS SDK for Ruby - Redshift Data API Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-redshiftdataapiservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-redshiftdataapiservice) = 1.6.0

%description   -n gem-aws-sdk-redshiftdataapiservice-doc
AWS SDK for Ruby - Redshift Data API Service documentation files.

Official AWS Ruby gem for Redshift Data API Service. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-redshiftdataapiservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-redshiftdataapiservice.


%package       -n gem-aws-sdk-redshiftdataapiservice-devel
Version:       1.6.0
Release:       alt1
Summary:       AWS SDK for Ruby - Redshift Data API Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-redshiftdataapiservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-redshiftdataapiservice) = 1.6.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-redshiftdataapiservice-devel
AWS SDK for Ruby - Redshift Data API Service development package.

Official AWS Ruby gem for Redshift Data API Service. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-redshiftdataapiservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-redshiftdataapiservice.


%package       -n gem-aws-sdk-personalizeevents
Version:       1.17.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Personalize Events
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-personalizeevents) = 1.17.0

%description   -n gem-aws-sdk-personalizeevents
Official AWS Ruby gem for Amazon Personalize Events. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-personalizeevents-doc
Version:       1.17.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Personalize Events documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-personalizeevents
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-personalizeevents) = 1.17.0

%description   -n gem-aws-sdk-personalizeevents-doc
AWS SDK for Ruby - Amazon Personalize Events documentation files.

Official AWS Ruby gem for Amazon Personalize Events. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-personalizeevents-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-personalizeevents.


%package       -n gem-aws-sdk-personalizeevents-devel
Version:       1.17.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Personalize Events development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-personalizeevents
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-personalizeevents) = 1.17.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-personalizeevents-devel
AWS SDK for Ruby - Amazon Personalize Events development package.

Official AWS Ruby gem for Amazon Personalize Events. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-personalizeevents-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-personalizeevents.


%package       -n gem-aws-sdk-appmesh
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS App Mesh
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-appmesh) = 1.35.0

%description   -n gem-aws-sdk-appmesh
Official AWS Ruby gem for AWS App Mesh. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-appmesh-doc
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS App Mesh documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appmesh
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appmesh) = 1.35.0

%description   -n gem-aws-sdk-appmesh-doc
AWS SDK for Ruby - AWS App Mesh documentation files.

Official AWS Ruby gem for AWS App Mesh. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-appmesh-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appmesh.


%package       -n gem-aws-sdk-appmesh-devel
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS App Mesh development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appmesh
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appmesh) = 1.35.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-appmesh-devel
AWS SDK for Ruby - AWS App Mesh development package.

Official AWS Ruby gem for AWS App Mesh. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-appmesh-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appmesh.


%package       -n gem-aws-sdk-savingsplans
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSSavingsPlans
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-savingsplans) = 1.15.0

%description   -n gem-aws-sdk-savingsplans
Official AWS Ruby gem for AWS Savings Plans (AWSSavingsPlans). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-savingsplans-doc
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSSavingsPlans documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-savingsplans
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-savingsplans) = 1.15.0

%description   -n gem-aws-sdk-savingsplans-doc
AWS SDK for Ruby - AWSSavingsPlans documentation files.

Official AWS Ruby gem for AWS Savings Plans (AWSSavingsPlans). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-savingsplans-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-savingsplans.


%package       -n gem-aws-sdk-savingsplans-devel
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSSavingsPlans development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-savingsplans
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-savingsplans) = 1.15.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-savingsplans-devel
AWS SDK for Ruby - AWSSavingsPlans development package.

Official AWS Ruby gem for AWS Savings Plans (AWSSavingsPlans). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-savingsplans-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-savingsplans.


%package       -n gem-aws-sdk-mobile
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Mobile
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-mobile) = 1.26.0

%description   -n gem-aws-sdk-mobile
Official AWS Ruby gem for AWS Mobile. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mobile-doc
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Mobile documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mobile
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mobile) = 1.26.0

%description   -n gem-aws-sdk-mobile-doc
AWS SDK for Ruby - AWS Mobile documentation files.

Official AWS Ruby gem for AWS Mobile. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mobile-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mobile.


%package       -n gem-aws-sdk-mobile-devel
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Mobile development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mobile
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mobile) = 1.26.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-mobile-devel
AWS SDK for Ruby - AWS Mobile development package.

Official AWS Ruby gem for AWS Mobile. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mobile-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mobile.


%package       -n gem-aws-sdk-core
Version:       3.114.1
Release:       alt1
Summary:       AWS SDK for Ruby - Core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jmespath) >= 1.0 gem(jmespath) < 2
Requires:      gem(aws-partitions) >= 1.239.0 gem(aws-partitions) < 2
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Requires:      gem(aws-eventstream) >= 1.0.2 gem(aws-eventstream) < 2
Obsoletes:     aws-sdk-core
Obsoletes:     ruby-aws-sdk-core
Provides:      aws-sdk-core
Provides:      ruby-aws-sdk-core
Provides:      gem(aws-sdk-core) = 3.114.1

%description   -n gem-aws-sdk-core
Provides API clients for AWS. This gem is part of the official AWS SDK for Ruby.


%package       -n gem-aws-sdk-core-doc
Version:       3.114.1
Release:       alt1
Summary:       AWS SDK for Ruby - Core documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-core) = 3.114.1

%description   -n gem-aws-sdk-core-doc
AWS SDK for Ruby - Core documentation files.

Provides API clients for AWS. This gem is part of the official AWS SDK for Ruby.

%description   -n gem-aws-sdk-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-core.


%package       -n gem-aws-sdk-core-devel
Version:       3.114.1
Release:       alt1
Summary:       AWS SDK for Ruby - Core development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) = 3.114.1
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-core-devel
AWS SDK for Ruby - Core development package.

Provides API clients for AWS. This gem is part of the official AWS SDK for Ruby.

%description   -n gem-aws-sdk-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-core.


%package       -n gem-aws-sdk-forecastservice
Version:       1.21.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Forecast Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-forecastservice) = 1.21.0

%description   -n gem-aws-sdk-forecastservice
Official AWS Ruby gem for Amazon Forecast Service. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-forecastservice-doc
Version:       1.21.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Forecast Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-forecastservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-forecastservice) = 1.21.0

%description   -n gem-aws-sdk-forecastservice-doc
AWS SDK for Ruby - Amazon Forecast Service documentation files.

Official AWS Ruby gem for Amazon Forecast Service. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-forecastservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-forecastservice.


%package       -n gem-aws-sdk-forecastservice-devel
Version:       1.21.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Forecast Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-forecastservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-forecastservice) = 1.21.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-forecastservice-devel
AWS SDK for Ruby - Amazon Forecast Service development package.

Official AWS Ruby gem for Amazon Forecast Service. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-forecastservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-forecastservice.
0G1G

%package       -n gem-aws-sdk-codeartifact
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeArtifact
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-codeartifact) = 1.10.0

%description   -n gem-aws-sdk-codeartifact
Official AWS Ruby gem for CodeArtifact. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-codeartifact-doc
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeArtifact documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codeartifact
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codeartifact) = 1.10.0

%description   -n gem-aws-sdk-codeartifact-doc
AWS SDK for Ruby - CodeArtifact documentation files.

Official AWS Ruby gem for CodeArtifact. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-codeartifact-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codeartifact.


%package       -n gem-aws-sdk-codeartifact-devel
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodeArtifact development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codeartifact
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codeartifact) = 1.10.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-codeartifact-devel
AWS SDK for Ruby - CodeArtifact development package.

Official AWS Ruby gem for CodeArtifact. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-codeartifact-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codeartifact.


%package       -n gem-aws-sdk-sagemakeredgemanager
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Sagemaker Edge Manager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-sagemakeredgemanager) = 1.2.0

%description   -n gem-aws-sdk-sagemakeredgemanager
Official AWS Ruby gem for Amazon Sagemaker Edge Manager. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-sagemakeredgemanager-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Sagemaker Edge Manager documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sagemakeredgemanager
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakeredgemanager) = 1.2.0

%description   -n gem-aws-sdk-sagemakeredgemanager-doc
AWS SDK for Ruby - Amazon Sagemaker Edge Manager documentation files.

Official AWS Ruby gem for Amazon Sagemaker Edge Manager. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-sagemakeredgemanager-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sagemakeredgemanager.


%package       -n gem-aws-sdk-sagemakeredgemanager-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Sagemaker Edge Manager development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sagemakeredgemanager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemakeredgemanager) = 1.2.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-sagemakeredgemanager-devel
AWS SDK for Ruby - Amazon Sagemaker Edge Manager development package.

Official AWS Ruby gem for Amazon Sagemaker Edge Manager. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-sagemakeredgemanager-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sagemakeredgemanager.


%package       -n gem-aws-sdk-resourcegroups
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - Resource Groups
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-resourcegroups) = 1.36.0

%description   -n gem-aws-sdk-resourcegroups
Official AWS Ruby gem for AWS Resource Groups (Resource Groups). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-resourcegroups-doc
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - Resource Groups documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-resourcegroups
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-resourcegroups) = 1.36.0

%description   -n gem-aws-sdk-resourcegroups-doc
AWS SDK for Ruby - Resource Groups documentation files.

Official AWS Ruby gem for AWS Resource Groups (Resource Groups). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-resourcegroups-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-resourcegroups.


%package       -n gem-aws-sdk-resourcegroups-devel
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - Resource Groups development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-resourcegroups
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-resourcegroups) = 1.36.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-resourcegroups-devel
AWS SDK for Ruby - Resource Groups development package.

Official AWS Ruby gem for AWS Resource Groups (Resource Groups). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-resourcegroups-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-resourcegroups.


%package       -n gem-aws-sdk-applicationinsights
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - Application Insights
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-applicationinsights) = 1.18.0

%description   -n gem-aws-sdk-applicationinsights
Official AWS Ruby gem for Amazon CloudWatch Application Insights (Application
Insights). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-applicationinsights-doc
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - Application Insights documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-applicationinsights
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationinsights) = 1.18.0

%description   -n gem-aws-sdk-applicationinsights-doc
AWS SDK for Ruby - Application Insights documentation files.

Official AWS Ruby gem for Amazon CloudWatch Application Insights (Application
Insights). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-applicationinsights-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-applicationinsights.


%package       -n gem-aws-sdk-applicationinsights-devel
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - Application Insights development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-applicationinsights
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationinsights) = 1.18.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-applicationinsights-devel
AWS SDK for Ruby - Application Insights development package.

Official AWS Ruby gem for Amazon CloudWatch Application Insights (Application
Insights). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-applicationinsights-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-applicationinsights.


%package       -n gem-aws-sdk-directconnect
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Direct Connect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-directconnect) = 1.41.0

%description   -n gem-aws-sdk-directconnect
Official AWS Ruby gem for AWS Direct Connect. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-directconnect-doc
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Direct Connect documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-directconnect
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-directconnect) = 1.41.0

%description   -n gem-aws-sdk-directconnect-doc
AWS SDK for Ruby - AWS Direct Connect documentation files.

Official AWS Ruby gem for AWS Direct Connect. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-directconnect-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-directconnect.


%package       -n gem-aws-sdk-directconnect-devel
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Direct Connect development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-directconnect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-directconnect) = 1.41.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-directconnect-devel
AWS SDK for Ruby - AWS Direct Connect development package.

Official AWS Ruby gem for AWS Direct Connect. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-directconnect-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-directconnect.


%package       -n gem-aws-sdk-pricing
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Pricing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-pricing) = 1.27.0

%description   -n gem-aws-sdk-pricing
Official AWS Ruby gem for AWS Price List Service (AWS Pricing). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-pricing-doc
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Pricing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-pricing
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-pricing) = 1.27.0

%description   -n gem-aws-sdk-pricing-doc
AWS SDK for Ruby - AWS Pricing documentation files.

Official AWS Ruby gem for AWS Price List Service (AWS Pricing). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pricing-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-pricing.


%package       -n gem-aws-sdk-pricing-devel
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Pricing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-pricing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-pricing) = 1.27.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-pricing-devel
AWS SDK for Ruby - AWS Pricing development package.

Official AWS Ruby gem for AWS Price List Service (AWS Pricing). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pricing-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-pricing.


%package       -n gem-aws-sigv2
Version:       1.0.2
Release:       alt1
Summary:       AWS Signature Version 2 library
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(aws-sigv2) = 1.0.2

%description   -n gem-aws-sigv2
Amazon Web Services Signature Version 2 signing library. Generates sigv2
signature for HTTP requests.


%package       -n gem-aws-sigv2-doc
Version:       1.0.2
Release:       alt1
Summary:       AWS Signature Version 2 library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sigv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sigv2) = 1.0.2

%description   -n gem-aws-sigv2-doc
AWS Signature Version 2 library documentation files.

Amazon Web Services Signature Version 2 signing library. Generates sigv2
signature for HTTP requests.

%description   -n gem-aws-sigv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sigv2.


%package       -n gem-aws-sdk-dynamodb
Version:       1.60.0
Release:       alt1
Summary:       AWS SDK for Ruby - DynamoDB
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-dynamodb) = 1.60.0

%description   -n gem-aws-sdk-dynamodb
Official AWS Ruby gem for Amazon DynamoDB (DynamoDB). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-dynamodb-doc
Version:       1.60.0
Release:       alt1
Summary:       AWS SDK for Ruby - DynamoDB documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-dynamodb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-dynamodb) = 1.60.0

%description   -n gem-aws-sdk-dynamodb-doc
AWS SDK for Ruby - DynamoDB documentation files.

Official AWS Ruby gem for Amazon DynamoDB (DynamoDB). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-dynamodb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-dynamodb.


%package       -n gem-aws-sdk-dynamodb-devel
Version:       1.60.0
Release:       alt1
Summary:       AWS SDK for Ruby - DynamoDB development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-dynamodb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-dynamodb) = 1.60.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-dynamodb-devel
AWS SDK for Ruby - DynamoDB development package.

Official AWS Ruby gem for Amazon DynamoDB (DynamoDB). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-dynamodb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-dynamodb.


%package       -n gem-aws-sdk-dax
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DAX
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-dax) = 1.29.0

%description   -n gem-aws-sdk-dax
Official AWS Ruby gem for Amazon DynamoDB Accelerator (DAX) (Amazon DAX). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-dax-doc
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DAX documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-dax
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-dax) = 1.29.0

%description   -n gem-aws-sdk-dax-doc
AWS SDK for Ruby - Amazon DAX documentation files.

Official AWS Ruby gem for Amazon DynamoDB Accelerator (DAX) (Amazon DAX). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-dax-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-dax.


%package       -n gem-aws-sdk-dax-devel
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DAX development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-dax
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-dax) = 1.29.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-dax-devel
AWS SDK for Ruby - Amazon DAX development package.

Official AWS Ruby gem for Amazon DynamoDB Accelerator (DAX) (Amazon DAX). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-dax-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-dax.


%package       -n gem-aws-sdk-iotsecuretunneling
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Secure Tunneling
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-iotsecuretunneling) = 1.11.0

%description   -n gem-aws-sdk-iotsecuretunneling
Official AWS Ruby gem for AWS IoT Secure Tunneling. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-iotsecuretunneling-doc
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Secure Tunneling documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotsecuretunneling
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotsecuretunneling) = 1.11.0

%description   -n gem-aws-sdk-iotsecuretunneling-doc
AWS SDK for Ruby - AWS IoT Secure Tunneling documentation files.

Official AWS Ruby gem for AWS IoT Secure Tunneling. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-iotsecuretunneling-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotsecuretunneling.


%package       -n gem-aws-sdk-iotsecuretunneling-devel
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Secure Tunneling development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotsecuretunneling
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotsecuretunneling) = 1.11.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-iotsecuretunneling-devel
AWS SDK for Ruby - AWS IoT Secure Tunneling development package.

Official AWS Ruby gem for AWS IoT Secure Tunneling. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-iotsecuretunneling-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotsecuretunneling.


%package       -n gem-aws-sdk-cognitoidentity
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Cognito Identity
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-cognitoidentity) = 1.31.0

%description   -n gem-aws-sdk-cognitoidentity
Official AWS Ruby gem for Amazon Cognito Identity. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-cognitoidentity-doc
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Cognito Identity documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cognitoidentity
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cognitoidentity) = 1.31.0

%description   -n gem-aws-sdk-cognitoidentity-doc
AWS SDK for Ruby - Amazon Cognito Identity documentation files.

Official AWS Ruby gem for Amazon Cognito Identity. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-cognitoidentity-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cognitoidentity.


%package       -n gem-aws-sdk-cognitoidentity-devel
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Cognito Identity development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cognitoidentity
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cognitoidentity) = 1.31.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-cognitoidentity-devel
AWS SDK for Ruby - Amazon Cognito Identity development package.

Official AWS Ruby gem for Amazon Cognito Identity. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-cognitoidentity-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cognitoidentity.


%package       -n gem-aws-sdk-gamelift
Version:       1.44.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon GameLift
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-gamelift) = 1.44.0

%description   -n gem-aws-sdk-gamelift
Official AWS Ruby gem for Amazon GameLift. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-gamelift-doc
Version:       1.44.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon GameLift documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-gamelift
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-gamelift) = 1.44.0

%description   -n gem-aws-sdk-gamelift-doc
AWS SDK for Ruby - Amazon GameLift documentation files.

Official AWS Ruby gem for Amazon GameLift. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-gamelift-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-gamelift.


%package       -n gem-aws-sdk-gamelift-devel
Version:       1.44.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon GameLift development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-gamelift
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-gamelift) = 1.44.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-gamelift-devel
AWS SDK for Ruby - Amazon GameLift development package.

Official AWS Ruby gem for Amazon GameLift. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-gamelift-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-gamelift.


%package       -n gem-aws-sdk-cloudwatchevents
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudWatch Events
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-cloudwatchevents) = 1.46.0

%description   -n gem-aws-sdk-cloudwatchevents
Official AWS Ruby gem for Amazon CloudWatch Events. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-cloudwatchevents-doc
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudWatch Events documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudwatchevents
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatchevents) = 1.46.0

%description   -n gem-aws-sdk-cloudwatchevents-doc
AWS SDK for Ruby - Amazon CloudWatch Events documentation files.

Official AWS Ruby gem for Amazon CloudWatch Events. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-cloudwatchevents-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudwatchevents.


%package       -n gem-aws-sdk-cloudwatchevents-devel
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudWatch Events development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudwatchevents
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatchevents) = 1.46.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-cloudwatchevents-devel
AWS SDK for Ruby - Amazon CloudWatch Events development package.

Official AWS Ruby gem for Amazon CloudWatch Events. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-cloudwatchevents-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudwatchevents.


%package       -n gem-aws-sdk-s3
Version:       1.96.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon S3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kms) >= 1 gem(aws-sdk-kms) < 2
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Provides:      gem(aws-sdk-s3) = 1.96.0

%description   -n gem-aws-sdk-s3
Official AWS Ruby gem for Amazon Simple Storage Service (Amazon S3). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-s3-doc
Version:       1.96.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon S3 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-s3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-s3) = 1.96.0

%description   -n gem-aws-sdk-s3-doc
AWS SDK for Ruby - Amazon S3 documentation files.

Official AWS Ruby gem for Amazon Simple Storage Service (Amazon S3). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-s3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-s3.


%package       -n gem-aws-sdk-s3-devel
Version:       1.96.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon S3 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-s3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-s3) = 1.96.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-s3-devel
AWS SDK for Ruby - Amazon S3 development package.

Official AWS Ruby gem for Amazon Simple Storage Service (Amazon S3). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-s3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-s3.


%package       -n gem-aws-sdk-connectparticipant
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Connect Participant
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-connectparticipant) = 1.11.0

%description   -n gem-aws-sdk-connectparticipant
Official AWS Ruby gem for Amazon Connect Participant Service (Amazon Connect
Participant). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-connectparticipant-doc
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Connect Participant documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-connectparticipant
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-connectparticipant) = 1.11.0

%description   -n gem-aws-sdk-connectparticipant-doc
AWS SDK for Ruby - Amazon Connect Participant documentation files.

Official AWS Ruby gem for Amazon Connect Participant Service (Amazon Connect
Participant). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-connectparticipant-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-connectparticipant.


%package       -n gem-aws-sdk-connectparticipant-devel
Version:       1.11.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Connect Participant development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-connectparticipant
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-connectparticipant) = 1.11.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-connectparticipant-devel
AWS SDK for Ruby - Amazon Connect Participant development package.

Official AWS Ruby gem for Amazon Connect Participant Service (Amazon Connect
Participant). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-connectparticipant-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-connectparticipant.


%package       -n gem-aws-sdk-codepipeline
Version:       1.44.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodePipeline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-codepipeline) = 1.44.0

%description   -n gem-aws-sdk-codepipeline
Official AWS Ruby gem for AWS CodePipeline (CodePipeline). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-codepipeline-doc
Version:       1.44.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodePipeline documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-codepipeline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-codepipeline) = 1.44.0

%description   -n gem-aws-sdk-codepipeline-doc
AWS SDK for Ruby - CodePipeline documentation files.

Official AWS Ruby gem for AWS CodePipeline (CodePipeline). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-codepipeline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-codepipeline.


%package       -n gem-aws-sdk-codepipeline-devel
Version:       1.44.0
Release:       alt1
Summary:       AWS SDK for Ruby - CodePipeline development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-codepipeline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-codepipeline) = 1.44.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-codepipeline-devel
AWS SDK for Ruby - CodePipeline development package.

Official AWS Ruby gem for AWS CodePipeline (CodePipeline). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-codepipeline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-codepipeline.


%package       -n gem-aws-sdk-costandusagereportservice
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Cost and Usage Report Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-costandusagereportservice) = 1.31.0

%description   -n gem-aws-sdk-costandusagereportservice
Official AWS Ruby gem for AWS Cost and Usage Report Service. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-costandusagereportservice-doc
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Cost and Usage Report Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-costandusagereportservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-costandusagereportservice) = 1.31.0

%description   -n gem-aws-sdk-costandusagereportservice-doc
AWS SDK for Ruby - AWS Cost and Usage Report Service documentation
files.

Official AWS Ruby gem for AWS Cost and Usage Report Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-costandusagereportservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-costandusagereportservice.


%package       -n gem-aws-sdk-costandusagereportservice-devel
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Cost and Usage Report Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-costandusagereportservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-costandusagereportservice) = 1.31.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-costandusagereportservice-devel
AWS SDK for Ruby - AWS Cost and Usage Report Service development
package.

Official AWS Ruby gem for AWS Cost and Usage Report Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-costandusagereportservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-costandusagereportservice.


%package       -n gem-aws-sdk-s3control
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS S3 Control
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Provides:      gem(aws-sdk-s3control) = 1.34.0

%description   -n gem-aws-sdk-s3control
Official AWS Ruby gem for AWS S3 Control. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-s3control-doc
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS S3 Control documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-s3control
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-s3control) = 1.34.0

%description   -n gem-aws-sdk-s3control-doc
AWS SDK for Ruby - AWS S3 Control documentation files.

Official AWS Ruby gem for AWS S3 Control. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-s3control-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-s3control.


%package       -n gem-aws-sdk-s3control-devel
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS S3 Control development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-s3control
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-s3control) = 1.34.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-s3control-devel
AWS SDK for Ruby - AWS S3 Control development package.

Official AWS Ruby gem for AWS S3 Control. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-s3control-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-s3control.


%package       -n gem-aws-sdk-marketplacemetering
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSMarketplace Metering
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-marketplacemetering) = 1.34.0

%description   -n gem-aws-sdk-marketplacemetering
Official AWS Ruby gem for AWSMarketplace Metering. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-marketplacemetering-doc
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSMarketplace Metering documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-marketplacemetering
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplacemetering) = 1.34.0

%description   -n gem-aws-sdk-marketplacemetering-doc
AWS SDK for Ruby - AWSMarketplace Metering documentation files.

Official AWS Ruby gem for AWSMarketplace Metering. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-marketplacemetering-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-marketplacemetering.


%package       -n gem-aws-sdk-marketplacemetering-devel
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSMarketplace Metering development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-marketplacemetering
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplacemetering) = 1.34.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-marketplacemetering-devel
AWS SDK for Ruby - AWSMarketplace Metering development package.

Official AWS Ruby gem for AWSMarketplace Metering. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-marketplacemetering-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-marketplacemetering.


%package       -n gem-aws-sdk-forecastqueryservice
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Forecast Query Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-forecastqueryservice) = 1.12.0

%description   -n gem-aws-sdk-forecastqueryservice
Official AWS Ruby gem for Amazon Forecast Query Service. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-forecastqueryservice-doc
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Forecast Query Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-forecastqueryservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-forecastqueryservice) = 1.12.0

%description   -n gem-aws-sdk-forecastqueryservice-doc
AWS SDK for Ruby - Amazon Forecast Query Service documentation files.

Official AWS Ruby gem for Amazon Forecast Query Service. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-forecastqueryservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-forecastqueryservice.


%package       -n gem-aws-sdk-forecastqueryservice-devel
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Forecast Query Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-forecastqueryservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-forecastqueryservice) = 1.12.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-forecastqueryservice-devel
AWS SDK for Ruby - Amazon Forecast Query Service development package.

Official AWS Ruby gem for Amazon Forecast Query Service. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-forecastqueryservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-forecastqueryservice.


%package       -n gem-aws-sdk-pi
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS PI
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-pi) = 1.28.0

%description   -n gem-aws-sdk-pi
Official AWS Ruby gem for AWS Performance Insights (AWS PI). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-pi-doc
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS PI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-pi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-pi) = 1.28.0

%description   -n gem-aws-sdk-pi-doc
AWS SDK for Ruby - AWS PI documentation files.

Official AWS Ruby gem for AWS Performance Insights (AWS PI). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-pi.


%package       -n gem-aws-sdk-pi-devel
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS PI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-pi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-pi) = 1.28.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-pi-devel
AWS SDK for Ruby - AWS PI development package.

Official AWS Ruby gem for AWS Performance Insights (AWS PI). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-pi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-pi.


%package       -n gem-aws-sdk-waf
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - WAF
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-waf) = 1.38.0

%description   -n gem-aws-sdk-waf
Official AWS Ruby gem for AWS WAF (WAF). This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-waf-doc
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - WAF documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-waf
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-waf) = 1.38.0

%description   -n gem-aws-sdk-waf-doc
AWS SDK for Ruby - WAF documentation files.

Official AWS Ruby gem for AWS WAF (WAF). This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-waf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-waf.


%package       -n gem-aws-sdk-waf-devel
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - WAF development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-waf
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-waf) = 1.38.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-waf-devel
AWS SDK for Ruby - WAF development package.

Official AWS Ruby gem for AWS WAF (WAF). This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-waf-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-waf.


%package       -n gem-aws-sdk-mediastore
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaStore
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-mediastore) = 1.32.0

%description   -n gem-aws-sdk-mediastore
Official AWS Ruby gem for AWS Elemental MediaStore (MediaStore). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mediastore-doc
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaStore documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mediastore
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mediastore) = 1.32.0

%description   -n gem-aws-sdk-mediastore-doc
AWS SDK for Ruby - MediaStore documentation files.

Official AWS Ruby gem for AWS Elemental MediaStore (MediaStore). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediastore-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mediastore.


%package       -n gem-aws-sdk-mediastore-devel
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaStore development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mediastore
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mediastore) = 1.32.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-mediastore-devel
AWS SDK for Ruby - MediaStore development package.

Official AWS Ruby gem for AWS Elemental MediaStore (MediaStore). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediastore-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mediastore.


%package       -n gem-aws-sdk-elasticloadbalancingv2
Version:       1.61.0
Release:       alt1
Summary:       AWS SDK for Ruby - Elastic Load Balancing v2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-elasticloadbalancingv2) = 1.61.0

%description   -n gem-aws-sdk-elasticloadbalancingv2
Official AWS Ruby gem for Elastic Load Balancing (Elastic Load Balancing v2).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-elasticloadbalancingv2-doc
Version:       1.61.0
Release:       alt1
Summary:       AWS SDK for Ruby - Elastic Load Balancing v2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-elasticloadbalancingv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticloadbalancingv2) = 1.61.0

%description   -n gem-aws-sdk-elasticloadbalancingv2-doc
AWS SDK for Ruby - Elastic Load Balancing v2 documentation files.

Official AWS Ruby gem for Elastic Load Balancing (Elastic Load Balancing v2).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-elasticloadbalancingv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-elasticloadbalancingv2.


%package       -n gem-aws-sdk-elasticloadbalancingv2-devel
Version:       1.61.0
Release:       alt1
Summary:       AWS SDK for Ruby - Elastic Load Balancing v2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-elasticloadbalancingv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticloadbalancingv2) = 1.61.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-elasticloadbalancingv2-devel
AWS SDK for Ruby - Elastic Load Balancing v2 development package.

Official AWS Ruby gem for Elastic Load Balancing (Elastic Load Balancing v2).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-elasticloadbalancingv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-elasticloadbalancingv2.


%package       -n gem-aws-sdk-serverlessapplicationrepository
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSServerlessApplicationRepository
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-serverlessapplicationrepository) = 1.34.0

%description   -n gem-aws-sdk-serverlessapplicationrepository
Official AWS Ruby gem for AWSServerlessApplicationRepository. This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-serverlessapplicationrepository-doc
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSServerlessApplicationRepository documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-serverlessapplicationrepository
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-serverlessapplicationrepository) = 1.34.0

%description   -n gem-aws-sdk-serverlessapplicationrepository-doc
AWS SDK for Ruby - AWSServerlessApplicationRepository documentation
files.

Official AWS Ruby gem for AWSServerlessApplicationRepository. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-serverlessapplicationrepository-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-serverlessapplicationrepository.


%package       -n gem-aws-sdk-serverlessapplicationrepository-devel
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSServerlessApplicationRepository development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-serverlessapplicationrepository
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-serverlessapplicationrepository) = 1.34.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-serverlessapplicationrepository-devel
AWS SDK for Ruby - AWSServerlessApplicationRepository development
package.

Official AWS Ruby gem for AWSServerlessApplicationRepository. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-serverlessapplicationrepository-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-serverlessapplicationrepository.


%package       -n gem-aws-sdk-lexmodelbuildingservice
Version:       1.45.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Lex Model Building Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-lexmodelbuildingservice) = 1.45.0

%description   -n gem-aws-sdk-lexmodelbuildingservice
Official AWS Ruby gem for Amazon Lex Model Building Service. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-lexmodelbuildingservice-doc
Version:       1.45.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Lex Model Building Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lexmodelbuildingservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lexmodelbuildingservice) = 1.45.0

%description   -n gem-aws-sdk-lexmodelbuildingservice-doc
AWS SDK for Ruby - Amazon Lex Model Building Service documentation
files.

Official AWS Ruby gem for Amazon Lex Model Building Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lexmodelbuildingservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lexmodelbuildingservice.


%package       -n gem-aws-sdk-lexmodelbuildingservice-devel
Version:       1.45.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Lex Model Building Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lexmodelbuildingservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lexmodelbuildingservice) = 1.45.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-lexmodelbuildingservice-devel
AWS SDK for Ruby - Amazon Lex Model Building Service development
package.

Official AWS Ruby gem for Amazon Lex Model Building Service. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lexmodelbuildingservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lexmodelbuildingservice.


%package       -n gem-aws-sdk-medialive
Version:       1.71.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaLive
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-medialive) = 1.71.0

%description   -n gem-aws-sdk-medialive
Official AWS Ruby gem for AWS Elemental MediaLive (MediaLive). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-medialive-doc
Version:       1.71.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaLive documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-medialive
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-medialive) = 1.71.0

%description   -n gem-aws-sdk-medialive-doc
AWS SDK for Ruby - MediaLive documentation files.

Official AWS Ruby gem for AWS Elemental MediaLive (MediaLive). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-medialive-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-medialive.


%package       -n gem-aws-sdk-medialive-devel
Version:       1.71.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaLive development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-medialive
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-medialive) = 1.71.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-medialive-devel
AWS SDK for Ruby - MediaLive development package.

Official AWS Ruby gem for AWS Elemental MediaLive (MediaLive). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-medialive-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-medialive.


%package       -n gem-aws-sdk-connectcontactlens
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Connect Contact Lens
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-connectcontactlens) = 1.2.0

%description   -n gem-aws-sdk-connectcontactlens
Official AWS Ruby gem for Amazon Connect Contact Lens. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-connectcontactlens-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Connect Contact Lens documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-connectcontactlens
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-connectcontactlens) = 1.2.0

%description   -n gem-aws-sdk-connectcontactlens-doc
AWS SDK for Ruby - Amazon Connect Contact Lens documentation files.

Official AWS Ruby gem for Amazon Connect Contact Lens. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-connectcontactlens-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-connectcontactlens.


%package       -n gem-aws-sdk-connectcontactlens-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Connect Contact Lens development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-connectcontactlens
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-connectcontactlens) = 1.2.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-connectcontactlens-devel
AWS SDK for Ruby - Amazon Connect Contact Lens development package.

Official AWS Ruby gem for Amazon Connect Contact Lens. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-connectcontactlens-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-connectcontactlens.


%package       -n gem-aws-sdk-comprehendmedical
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - ComprehendMedical
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-comprehendmedical) = 1.26.0

%description   -n gem-aws-sdk-comprehendmedical
Official AWS Ruby gem for AWS Comprehend Medical (ComprehendMedical). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-comprehendmedical-doc
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - ComprehendMedical documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-comprehendmedical
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-comprehendmedical) = 1.26.0

%description   -n gem-aws-sdk-comprehendmedical-doc
AWS SDK for Ruby - ComprehendMedical documentation files.

Official AWS Ruby gem for AWS Comprehend Medical (ComprehendMedical). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-comprehendmedical-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-comprehendmedical.


%package       -n gem-aws-sdk-comprehendmedical-devel
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - ComprehendMedical development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-comprehendmedical
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-comprehendmedical) = 1.26.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-comprehendmedical-devel
AWS SDK for Ruby - ComprehendMedical development package.

Official AWS Ruby gem for AWS Comprehend Medical (ComprehendMedical). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-comprehendmedical-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-comprehendmedical.


%package       -n gem-aws-sdk-outposts
Version:       1.16.0
Release:       alt1
Summary:       AWS SDK for Ruby - Outposts
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-outposts) = 1.16.0

%description   -n gem-aws-sdk-outposts
Official AWS Ruby gem for AWS Outposts (Outposts). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-outposts-doc
Version:       1.16.0
Release:       alt1
Summary:       AWS SDK for Ruby - Outposts documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-outposts
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-outposts) = 1.16.0

%description   -n gem-aws-sdk-outposts-doc
AWS SDK for Ruby - Outposts documentation files.

Official AWS Ruby gem for AWS Outposts (Outposts). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-outposts-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-outposts.


%package       -n gem-aws-sdk-outposts-devel
Version:       1.16.0
Release:       alt1
Summary:       AWS SDK for Ruby - Outposts development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-outposts
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-outposts) = 1.16.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-outposts-devel
AWS SDK for Ruby - Outposts development package.

Official AWS Ruby gem for AWS Outposts (Outposts). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-outposts-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-outposts.


%package       -n gem-aws-sdk-workdocs
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkDocs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-workdocs) = 1.30.0

%description   -n gem-aws-sdk-workdocs
Official AWS Ruby gem for Amazon WorkDocs. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-workdocs-doc
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkDocs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-workdocs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-workdocs) = 1.30.0

%description   -n gem-aws-sdk-workdocs-doc
AWS SDK for Ruby - Amazon WorkDocs documentation files.

Official AWS Ruby gem for Amazon WorkDocs. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-workdocs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-workdocs.


%package       -n gem-aws-sdk-workdocs-devel
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkDocs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-workdocs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-workdocs) = 1.30.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-workdocs-devel
AWS SDK for Ruby - Amazon WorkDocs development package.

Official AWS Ruby gem for Amazon WorkDocs. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-workdocs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-workdocs.


%package       -n gem-aws-sdk-kinesisvideo
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Video
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-kinesisvideo) = 1.32.0

%description   -n gem-aws-sdk-kinesisvideo
Official AWS Ruby gem for Amazon Kinesis Video Streams (Kinesis Video). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kinesisvideo-doc
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Video documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesisvideo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideo) = 1.32.0

%description   -n gem-aws-sdk-kinesisvideo-doc
AWS SDK for Ruby - Kinesis Video documentation files.

Official AWS Ruby gem for Amazon Kinesis Video Streams (Kinesis Video). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesisvideo.


%package       -n gem-aws-sdk-kinesisvideo-devel
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Video development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesisvideo
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideo) = 1.32.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-kinesisvideo-devel
AWS SDK for Ruby - Kinesis Video development package.

Official AWS Ruby gem for Amazon Kinesis Video Streams (Kinesis Video). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideo-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesisvideo.


%package       -n gem-aws-sdk-cloudwatchlogs
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudWatch Logs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-cloudwatchlogs) = 1.41.0

%description   -n gem-aws-sdk-cloudwatchlogs
Official AWS Ruby gem for Amazon CloudWatch Logs. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-cloudwatchlogs-doc
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudWatch Logs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudwatchlogs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatchlogs) = 1.41.0

%description   -n gem-aws-sdk-cloudwatchlogs-doc
AWS SDK for Ruby - Amazon CloudWatch Logs documentation files.

Official AWS Ruby gem for Amazon CloudWatch Logs. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-cloudwatchlogs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudwatchlogs.


%package       -n gem-aws-sdk-cloudwatchlogs-devel
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon CloudWatch Logs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudwatchlogs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudwatchlogs) = 1.41.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-cloudwatchlogs-devel
AWS SDK for Ruby - Amazon CloudWatch Logs development package.

Official AWS Ruby gem for Amazon CloudWatch Logs. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-cloudwatchlogs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudwatchlogs.


%package       -n gem-aws-sdk
Version:       3.0.2
Release:       alt1
Summary:       AWS SDK for Ruby - Core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-resources) >= 3 gem(aws-sdk-resources) < 4
Provides:      gem(aws-sdk) = 3.0.2

%description   -n gem-aws-sdk
The official AWS SDK for Ruby. Provides both resource oriented interfaces and
API clients for AWS services.


%package       -n gem-aws-sdk-doc
Version:       3.0.2
Release:       alt1
Summary:       AWS SDK for Ruby - Core documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk) = 3.0.2

%description   -n gem-aws-sdk-doc
AWS SDK for Ruby - Core documentation files.

The official AWS SDK for Ruby. Provides both resource oriented interfaces and
API clients for AWS services.

%description   -n gem-aws-sdk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk.


%package       -n gem-aws-sdk-devel
Version:       3.0.2
Release:       alt1
Summary:       AWS SDK for Ruby - Core development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk) = 3.0.2
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-devel
AWS SDK for Ruby - Core development package.

The official AWS SDK for Ruby. Provides both resource oriented interfaces and
API clients for AWS services.

%description   -n gem-aws-sdk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk.


%package       -n gem-aws-sdk-mediapackagevod
Version:       1.23.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaPackage Vod
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-mediapackagevod) = 1.23.0

%description   -n gem-aws-sdk-mediapackagevod
Official AWS Ruby gem for AWS Elemental MediaPackage VOD (MediaPackage Vod).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mediapackagevod-doc
Version:       1.23.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaPackage Vod documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mediapackagevod
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mediapackagevod) = 1.23.0

%description   -n gem-aws-sdk-mediapackagevod-doc
AWS SDK for Ruby - MediaPackage Vod documentation files.

Official AWS Ruby gem for AWS Elemental MediaPackage VOD (MediaPackage Vod).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediapackagevod-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mediapackagevod.


%package       -n gem-aws-sdk-mediapackagevod-devel
Version:       1.23.0
Release:       alt1
Summary:       AWS SDK for Ruby - MediaPackage Vod development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mediapackagevod
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mediapackagevod) = 1.23.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-mediapackagevod-devel
AWS SDK for Ruby - MediaPackage Vod development package.

Official AWS Ruby gem for AWS Elemental MediaPackage VOD (MediaPackage Vod).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mediapackagevod-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mediapackagevod.


%package       -n gem-aws-sdk-glacier
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Glacier
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-glacier) = 1.37.0

%description   -n gem-aws-sdk-glacier
Official AWS Ruby gem for Amazon Glacier. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-glacier-doc
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Glacier documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-glacier
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-glacier) = 1.37.0

%description   -n gem-aws-sdk-glacier-doc
AWS SDK for Ruby - Amazon Glacier documentation files.

Official AWS Ruby gem for Amazon Glacier. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-glacier-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-glacier.


%package       -n gem-aws-sdk-glacier-devel
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Glacier development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-glacier
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-glacier) = 1.37.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-glacier-devel
AWS SDK for Ruby - Amazon Glacier development package.

Official AWS Ruby gem for Amazon Glacier. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-glacier-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-glacier.


%package       -n gem-aws-sdk-simpledb
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SimpleDB
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv2) >= 1.0 gem(aws-sigv2) < 2
Provides:      gem(aws-sdk-simpledb) = 1.26.0

%description   -n gem-aws-sdk-simpledb
Official AWS Ruby gem for Amazon SimpleDB. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-simpledb-doc
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SimpleDB documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-simpledb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-simpledb) = 1.26.0

%description   -n gem-aws-sdk-simpledb-doc
AWS SDK for Ruby - Amazon SimpleDB documentation files.

Official AWS Ruby gem for Amazon SimpleDB. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-simpledb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-simpledb.


%package       -n gem-aws-sdk-simpledb-devel
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SimpleDB development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-simpledb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-simpledb) = 1.26.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-simpledb-devel
AWS SDK for Ruby - Amazon SimpleDB development package.

Official AWS Ruby gem for Amazon SimpleDB. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-simpledb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-simpledb.


%package       -n gem-aws-sdk-emr
Version:       1.45.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EMR
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-emr) = 1.45.0

%description   -n gem-aws-sdk-emr
Official AWS Ruby gem for Amazon Elastic MapReduce (Amazon EMR). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-emr-doc
Version:       1.45.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EMR documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-emr
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-emr) = 1.45.0

%description   -n gem-aws-sdk-emr-doc
AWS SDK for Ruby - Amazon EMR documentation files.

Official AWS Ruby gem for Amazon Elastic MapReduce (Amazon EMR). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-emr-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-emr.


%package       -n gem-aws-sdk-emr-devel
Version:       1.45.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EMR development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-emr
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-emr) = 1.45.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-emr-devel
AWS SDK for Ruby - Amazon EMR development package.

Official AWS Ruby gem for Amazon Elastic MapReduce (Amazon EMR). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-emr-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-emr.


%package       -n gem-aws-sdk-ecr
Version:       1.42.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon ECR
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-ecr) = 1.42.0

%description   -n gem-aws-sdk-ecr
Official AWS Ruby gem for Amazon EC2 Container Registry (Amazon ECR). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ecr-doc
Version:       1.42.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon ECR documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ecr
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ecr) = 1.42.0

%description   -n gem-aws-sdk-ecr-doc
AWS SDK for Ruby - Amazon ECR documentation files.

Official AWS Ruby gem for Amazon EC2 Container Registry (Amazon ECR). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ecr-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ecr.


%package       -n gem-aws-sdk-ecr-devel
Version:       1.42.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon ECR development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ecr
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ecr) = 1.42.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ecr-devel
AWS SDK for Ruby - Amazon ECR development package.

Official AWS Ruby gem for Amazon EC2 Container Registry (Amazon ECR). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ecr-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ecr.


%package       -n gem-aws-sdk-rekognition
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Rekognition
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-rekognition) = 1.51.0

%description   -n gem-aws-sdk-rekognition
Official AWS Ruby gem for Amazon Rekognition. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-rekognition-doc
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Rekognition documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-rekognition
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-rekognition) = 1.51.0

%description   -n gem-aws-sdk-rekognition-doc
AWS SDK for Ruby - Amazon Rekognition documentation files.

Official AWS Ruby gem for Amazon Rekognition. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-rekognition-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-rekognition.


%package       -n gem-aws-sdk-rekognition-devel
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Rekognition development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-rekognition
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-rekognition) = 1.51.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-rekognition-devel
AWS SDK for Ruby - Amazon Rekognition development package.

Official AWS Ruby gem for Amazon Rekognition. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-rekognition-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-rekognition.


%package       -n gem-aws-sdk-directoryservice
Version:       1.39.0
Release:       alt1
Summary:       AWS SDK for Ruby - Directory Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-directoryservice) = 1.39.0

%description   -n gem-aws-sdk-directoryservice
Official AWS Ruby gem for AWS Directory Service (Directory Service). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-directoryservice-doc
Version:       1.39.0
Release:       alt1
Summary:       AWS SDK for Ruby - Directory Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-directoryservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-directoryservice) = 1.39.0

%description   -n gem-aws-sdk-directoryservice-doc
AWS SDK for Ruby - Directory Service documentation files.

Official AWS Ruby gem for AWS Directory Service (Directory Service). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-directoryservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-directoryservice.


%package       -n gem-aws-sdk-directoryservice-devel
Version:       1.39.0
Release:       alt1
Summary:       AWS SDK for Ruby - Directory Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-directoryservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-directoryservice) = 1.39.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-directoryservice-devel
AWS SDK for Ruby - Directory Service development package.

Official AWS Ruby gem for AWS Directory Service (Directory Service). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-directoryservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-directoryservice.


%package       -n gem-aws-sdk-organizations
Version:       1.59.0
Release:       alt1
Summary:       AWS SDK for Ruby - Organizations
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-organizations) = 1.59.0

%description   -n gem-aws-sdk-organizations
Official AWS Ruby gem for AWS Organizations (Organizations). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-organizations-doc
Version:       1.59.0
Release:       alt1
Summary:       AWS SDK for Ruby - Organizations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-organizations
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-organizations) = 1.59.0

%description   -n gem-aws-sdk-organizations-doc
AWS SDK for Ruby - Organizations documentation files.

Official AWS Ruby gem for AWS Organizations (Organizations). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-organizations-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-organizations.


%package       -n gem-aws-sdk-organizations-devel
Version:       1.59.0
Release:       alt1
Summary:       AWS SDK for Ruby - Organizations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-organizations
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-organizations) = 1.59.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-organizations-devel
AWS SDK for Ruby - Organizations development package.

Official AWS Ruby gem for AWS Organizations (Organizations). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-organizations-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-organizations.


%package       -n gem-aws-sdk-servicediscovery
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - ServiceDiscovery
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-servicediscovery) = 1.36.0

%description   -n gem-aws-sdk-servicediscovery
Official AWS Ruby gem for AWS Cloud Map (ServiceDiscovery). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-servicediscovery-doc
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - ServiceDiscovery documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-servicediscovery
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-servicediscovery) = 1.36.0

%description   -n gem-aws-sdk-servicediscovery-doc
AWS SDK for Ruby - ServiceDiscovery documentation files.

Official AWS Ruby gem for AWS Cloud Map (ServiceDiscovery). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-servicediscovery-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-servicediscovery.


%package       -n gem-aws-sdk-servicediscovery-devel
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - ServiceDiscovery development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-servicediscovery
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-servicediscovery) = 1.36.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-servicediscovery-devel
AWS SDK for Ruby - ServiceDiscovery development package.

Official AWS Ruby gem for AWS Cloud Map (ServiceDiscovery). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-servicediscovery-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-servicediscovery.


%package       -n gem-aws-sdk-batch
Version:       1.47.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Batch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-batch) = 1.47.0

%description   -n gem-aws-sdk-batch
Official AWS Ruby gem for AWS Batch. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-batch-doc
Version:       1.47.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Batch documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-batch
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-batch) = 1.47.0

%description   -n gem-aws-sdk-batch-doc
AWS SDK for Ruby - AWS Batch documentation files.

Official AWS Ruby gem for AWS Batch. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-batch-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-batch.


%package       -n gem-aws-sdk-batch-devel
Version:       1.47.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Batch development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-batch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-batch) = 1.47.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-batch-devel
AWS SDK for Ruby - AWS Batch development package.

Official AWS Ruby gem for AWS Batch. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-batch-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-batch.


%package       -n gem-aws-sdk-acmpca
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - ACM-PCA
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-acmpca) = 1.36.0

%description   -n gem-aws-sdk-acmpca
Official AWS Ruby gem for AWS Certificate Manager Private Certificate Authority
(ACM-PCA). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-acmpca-doc
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - ACM-PCA documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-acmpca
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-acmpca) = 1.36.0

%description   -n gem-aws-sdk-acmpca-doc
AWS SDK for Ruby - ACM-PCA documentation files.

Official AWS Ruby gem for AWS Certificate Manager Private Certificate Authority
(ACM-PCA). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-acmpca-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-acmpca.


%package       -n gem-aws-sdk-acmpca-devel
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - ACM-PCA development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-acmpca
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-acmpca) = 1.36.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-acmpca-devel
AWS SDK for Ruby - ACM-PCA development package.

Official AWS Ruby gem for AWS Certificate Manager Private Certificate Authority
(ACM-PCA). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-acmpca-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-acmpca.


%package       -n gem-aws-sdk-qldb
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - QLDB
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-qldb) = 1.15.0

%description   -n gem-aws-sdk-qldb
Official AWS Ruby gem for Amazon QLDB (QLDB). This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-qldb-doc
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - QLDB documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-qldb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-qldb) = 1.15.0

%description   -n gem-aws-sdk-qldb-doc
AWS SDK for Ruby - QLDB documentation files.

Official AWS Ruby gem for Amazon QLDB (QLDB). This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-qldb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-qldb.


%package       -n gem-aws-sdk-qldb-devel
Version:       1.15.0
Release:       alt1
Summary:       AWS SDK for Ruby - QLDB development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-qldb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-qldb) = 1.15.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-qldb-devel
AWS SDK for Ruby - QLDB development package.

Official AWS Ruby gem for Amazon QLDB (QLDB). This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-qldb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-qldb.


%package       -n gem-aws-sdk-mediaconnect
Version:       1.33.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS MediaConnect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-mediaconnect) = 1.33.0

%description   -n gem-aws-sdk-mediaconnect
Official AWS Ruby gem for AWS MediaConnect. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-mediaconnect-doc
Version:       1.33.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS MediaConnect documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mediaconnect
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mediaconnect) = 1.33.0

%description   -n gem-aws-sdk-mediaconnect-doc
AWS SDK for Ruby - AWS MediaConnect documentation files.

Official AWS Ruby gem for AWS MediaConnect. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-mediaconnect-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mediaconnect.


%package       -n gem-aws-sdk-mediaconnect-devel
Version:       1.33.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS MediaConnect development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mediaconnect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mediaconnect) = 1.33.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-mediaconnect-devel
AWS SDK for Ruby - AWS MediaConnect development package.

Official AWS Ruby gem for AWS MediaConnect. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-mediaconnect-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mediaconnect.


%package       -n gem-aws-sdk-cloudtrail
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudTrail
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-cloudtrail) = 1.35.0

%description   -n gem-aws-sdk-cloudtrail
Official AWS Ruby gem for AWS CloudTrail (CloudTrail). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-cloudtrail-doc
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudTrail documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudtrail
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudtrail) = 1.35.0

%description   -n gem-aws-sdk-cloudtrail-doc
AWS SDK for Ruby - CloudTrail documentation files.

Official AWS Ruby gem for AWS CloudTrail (CloudTrail). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudtrail-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudtrail.


%package       -n gem-aws-sdk-cloudtrail-devel
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - CloudTrail development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudtrail
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudtrail) = 1.35.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-cloudtrail-devel
AWS SDK for Ruby - CloudTrail development package.

Official AWS Ruby gem for AWS CloudTrail (CloudTrail). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-cloudtrail-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudtrail.


%package       -n gem-aws-sdk-dynamodbstreams
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DynamoDB Streams
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-dynamodbstreams) = 1.29.0

%description   -n gem-aws-sdk-dynamodbstreams
Official AWS Ruby gem for Amazon DynamoDB Streams. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-dynamodbstreams-doc
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DynamoDB Streams documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-dynamodbstreams
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-dynamodbstreams) = 1.29.0

%description   -n gem-aws-sdk-dynamodbstreams-doc
AWS SDK for Ruby - Amazon DynamoDB Streams documentation files.

Official AWS Ruby gem for Amazon DynamoDB Streams. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-dynamodbstreams-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-dynamodbstreams.


%package       -n gem-aws-sdk-dynamodbstreams-devel
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DynamoDB Streams development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-dynamodbstreams
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-dynamodbstreams) = 1.29.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-dynamodbstreams-devel
AWS SDK for Ruby - Amazon DynamoDB Streams development package.

Official AWS Ruby gem for Amazon DynamoDB Streams. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-dynamodbstreams-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-dynamodbstreams.


%package       -n gem-aws-sdk-guardduty
Version:       1.45.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon GuardDuty
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-guardduty) = 1.45.0

%description   -n gem-aws-sdk-guardduty
Official AWS Ruby gem for Amazon GuardDuty. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-guardduty-doc
Version:       1.45.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon GuardDuty documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-guardduty
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-guardduty) = 1.45.0

%description   -n gem-aws-sdk-guardduty-doc
AWS SDK for Ruby - Amazon GuardDuty documentation files.

Official AWS Ruby gem for Amazon GuardDuty. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-guardduty-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-guardduty.


%package       -n gem-aws-sdk-guardduty-devel
Version:       1.45.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon GuardDuty development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-guardduty
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-guardduty) = 1.45.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-guardduty-devel
AWS SDK for Ruby - Amazon GuardDuty development package.

Official AWS Ruby gem for Amazon GuardDuty. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-guardduty-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-guardduty.


%package       -n gem-aws-sdk-iotjobsdataplane
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Jobs Data Plane
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-iotjobsdataplane) = 1.27.0

%description   -n gem-aws-sdk-iotjobsdataplane
Official AWS Ruby gem for AWS IoT Jobs Data Plane. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-iotjobsdataplane-doc
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Jobs Data Plane documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotjobsdataplane
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotjobsdataplane) = 1.27.0

%description   -n gem-aws-sdk-iotjobsdataplane-doc
AWS SDK for Ruby - AWS IoT Jobs Data Plane documentation files.

Official AWS Ruby gem for AWS IoT Jobs Data Plane. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-iotjobsdataplane-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotjobsdataplane.


%package       -n gem-aws-sdk-iotjobsdataplane-devel
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Jobs Data Plane development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotjobsdataplane
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotjobsdataplane) = 1.27.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-iotjobsdataplane-devel
AWS SDK for Ruby - AWS IoT Jobs Data Plane development package.

Official AWS Ruby gem for AWS IoT Jobs Data Plane. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-iotjobsdataplane-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotjobsdataplane.


%package       -n gem-aws-sdk-dlm
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DLM
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-dlm) = 1.40.0

%description   -n gem-aws-sdk-dlm
Official AWS Ruby gem for Amazon Data Lifecycle Manager (Amazon DLM). This gem
is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-dlm-doc
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DLM documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-dlm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-dlm) = 1.40.0

%description   -n gem-aws-sdk-dlm-doc
AWS SDK for Ruby - Amazon DLM documentation files.

Official AWS Ruby gem for Amazon Data Lifecycle Manager (Amazon DLM). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-dlm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-dlm.


%package       -n gem-aws-sdk-dlm-devel
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon DLM development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-dlm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-dlm) = 1.40.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-dlm-devel
AWS SDK for Ruby - Amazon DLM development package.

Official AWS Ruby gem for Amazon Data Lifecycle Manager (Amazon DLM). This gem
is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-dlm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-dlm.


%package       -n gem-aws-sdk-devicefarm
Version:       1.42.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Device Farm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-devicefarm) = 1.42.0

%description   -n gem-aws-sdk-devicefarm
Official AWS Ruby gem for AWS Device Farm. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-devicefarm-doc
Version:       1.42.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Device Farm documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-devicefarm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-devicefarm) = 1.42.0

%description   -n gem-aws-sdk-devicefarm-doc
AWS SDK for Ruby - AWS Device Farm documentation files.

Official AWS Ruby gem for AWS Device Farm. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-devicefarm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-devicefarm.


%package       -n gem-aws-sdk-devicefarm-devel
Version:       1.42.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Device Farm development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-devicefarm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-devicefarm) = 1.42.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-devicefarm-devel
AWS SDK for Ruby - AWS Device Farm development package.

Official AWS Ruby gem for AWS Device Farm. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-devicefarm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-devicefarm.


%package       -n gem-aws-sdk-textract
Version:       1.24.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Textract
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-textract) = 1.24.0

%description   -n gem-aws-sdk-textract
Official AWS Ruby gem for Amazon Textract. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-textract-doc
Version:       1.24.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Textract documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-textract
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-textract) = 1.24.0

%description   -n gem-aws-sdk-textract-doc
AWS SDK for Ruby - Amazon Textract documentation files.

Official AWS Ruby gem for Amazon Textract. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-textract-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-textract.


%package       -n gem-aws-sdk-textract-devel
Version:       1.24.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Textract development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-textract
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-textract) = 1.24.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-textract-devel
AWS SDK for Ruby - Amazon Textract development package.

Official AWS Ruby gem for Amazon Textract. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-textract-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-textract.


%package       -n gem-aws-sdk-lex
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Lex Runtime Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-lex) = 1.36.0

%description   -n gem-aws-sdk-lex
Official AWS Ruby gem for Amazon Lex Runtime Service. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-lex-doc
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Lex Runtime Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lex
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lex) = 1.36.0

%description   -n gem-aws-sdk-lex-doc
AWS SDK for Ruby - Amazon Lex Runtime Service documentation files.

Official AWS Ruby gem for Amazon Lex Runtime Service. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-lex-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lex.


%package       -n gem-aws-sdk-lex-devel
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Lex Runtime Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lex
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lex) = 1.36.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-lex-devel
AWS SDK for Ruby - Amazon Lex Runtime Service development package.

Official AWS Ruby gem for Amazon Lex Runtime Service. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-lex-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lex.


%package       -n gem-aws-sdk-personalizeruntime
Version:       1.22.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Personalize Runtime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-personalizeruntime) = 1.22.0

%description   -n gem-aws-sdk-personalizeruntime
Official AWS Ruby gem for Amazon Personalize Runtime. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-personalizeruntime-doc
Version:       1.22.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Personalize Runtime documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-personalizeruntime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-personalizeruntime) = 1.22.0

%description   -n gem-aws-sdk-personalizeruntime-doc
AWS SDK for Ruby - Amazon Personalize Runtime documentation files.

Official AWS Ruby gem for Amazon Personalize Runtime. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-personalizeruntime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-personalizeruntime.


%package       -n gem-aws-sdk-personalizeruntime-devel
Version:       1.22.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Personalize Runtime development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-personalizeruntime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-personalizeruntime) = 1.22.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-personalizeruntime-devel
AWS SDK for Ruby - Amazon Personalize Runtime development package.

Official AWS Ruby gem for Amazon Personalize Runtime. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-personalizeruntime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-personalizeruntime.


%package       -n gem-aws-sdk-servicecatalog
Version:       1.59.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Service Catalog
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-servicecatalog) = 1.59.0

%description   -n gem-aws-sdk-servicecatalog
Official AWS Ruby gem for AWS Service Catalog. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-servicecatalog-doc
Version:       1.59.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Service Catalog documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-servicecatalog
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-servicecatalog) = 1.59.0

%description   -n gem-aws-sdk-servicecatalog-doc
AWS SDK for Ruby - AWS Service Catalog documentation files.

Official AWS Ruby gem for AWS Service Catalog. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-servicecatalog-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-servicecatalog.


%package       -n gem-aws-sdk-servicecatalog-devel
Version:       1.59.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Service Catalog development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-servicecatalog
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-servicecatalog) = 1.59.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-servicecatalog-devel
AWS SDK for Ruby - AWS Service Catalog development package.

Official AWS Ruby gem for AWS Service Catalog. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-servicecatalog-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-servicecatalog.


%package       -n gem-aws-sdk-route53
Version:       1.49.0
Release:       alt1
Summary:       AWS SDK for Ruby - Route 53
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-route53) = 1.49.0

%description   -n gem-aws-sdk-route53
Official AWS Ruby gem for Amazon Route 53 (Route 53). This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-route53-doc
Version:       1.49.0
Release:       alt1
Summary:       AWS SDK for Ruby - Route 53 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-route53
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-route53) = 1.49.0

%description   -n gem-aws-sdk-route53-doc
AWS SDK for Ruby - Route 53 documentation files.

Official AWS Ruby gem for Amazon Route 53 (Route 53). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-route53-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-route53.


%package       -n gem-aws-sdk-route53-devel
Version:       1.49.0
Release:       alt1
Summary:       AWS SDK for Ruby - Route 53 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-route53
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-route53) = 1.49.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-route53-devel
AWS SDK for Ruby - Route 53 development package.

Official AWS Ruby gem for Amazon Route 53 (Route 53). This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-route53-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-route53.


%package       -n gem-aws-sdk-workmailmessageflow
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkMail Message Flow
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-workmailmessageflow) = 1.12.0

%description   -n gem-aws-sdk-workmailmessageflow
Official AWS Ruby gem for Amazon WorkMail Message Flow. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-workmailmessageflow-doc
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkMail Message Flow documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-workmailmessageflow
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-workmailmessageflow) = 1.12.0

%description   -n gem-aws-sdk-workmailmessageflow-doc
AWS SDK for Ruby - Amazon WorkMail Message Flow documentation files.

Official AWS Ruby gem for Amazon WorkMail Message Flow. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-workmailmessageflow-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-workmailmessageflow.


%package       -n gem-aws-sdk-workmailmessageflow-devel
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkMail Message Flow development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-workmailmessageflow
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-workmailmessageflow) = 1.12.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-workmailmessageflow-devel
AWS SDK for Ruby - Amazon WorkMail Message Flow development package.

Official AWS Ruby gem for Amazon WorkMail Message Flow. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-workmailmessageflow-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-workmailmessageflow.


%package       -n gem-aws-sdk-detective
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Detective
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-detective) = 1.18.0

%description   -n gem-aws-sdk-detective
Official AWS Ruby gem for Amazon Detective. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-detective-doc
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Detective documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-detective
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-detective) = 1.18.0

%description   -n gem-aws-sdk-detective-doc
AWS SDK for Ruby - Amazon Detective documentation files.

Official AWS Ruby gem for Amazon Detective. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-detective-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-detective.


%package       -n gem-aws-sdk-detective-devel
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Detective development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-detective
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-detective) = 1.18.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-detective-devel
AWS SDK for Ruby - Amazon Detective development package.

Official AWS Ruby gem for Amazon Detective. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-detective-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-detective.


%package       -n gem-aws-sdk-resourcegroupstaggingapi
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Resource Groups Tagging API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-resourcegroupstaggingapi) = 1.37.0

%description   -n gem-aws-sdk-resourcegroupstaggingapi
Official AWS Ruby gem for AWS Resource Groups Tagging API. This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-resourcegroupstaggingapi-doc
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Resource Groups Tagging API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-resourcegroupstaggingapi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-resourcegroupstaggingapi) = 1.37.0

%description   -n gem-aws-sdk-resourcegroupstaggingapi-doc
AWS SDK for Ruby - AWS Resource Groups Tagging API documentation
files.

Official AWS Ruby gem for AWS Resource Groups Tagging API. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-resourcegroupstaggingapi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-resourcegroupstaggingapi.


%package       -n gem-aws-sdk-resourcegroupstaggingapi-devel
Version:       1.37.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Resource Groups Tagging API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-resourcegroupstaggingapi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-resourcegroupstaggingapi) = 1.37.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-resourcegroupstaggingapi-devel
AWS SDK for Ruby - AWS Resource Groups Tagging API development
package.

Official AWS Ruby gem for AWS Resource Groups Tagging API. This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-resourcegroupstaggingapi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-resourcegroupstaggingapi.


%package       -n gem-aws-sdk-datapipeline
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Data Pipeline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-datapipeline) = 1.27.0

%description   -n gem-aws-sdk-datapipeline
Official AWS Ruby gem for AWS Data Pipeline. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-datapipeline-doc
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Data Pipeline documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-datapipeline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-datapipeline) = 1.27.0

%description   -n gem-aws-sdk-datapipeline-doc
AWS SDK for Ruby - AWS Data Pipeline documentation files.

Official AWS Ruby gem for AWS Data Pipeline. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-datapipeline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-datapipeline.


%package       -n gem-aws-sdk-datapipeline-devel
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Data Pipeline development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-datapipeline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-datapipeline) = 1.27.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-datapipeline-devel
AWS SDK for Ruby - AWS Data Pipeline development package.

Official AWS Ruby gem for AWS Data Pipeline. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-datapipeline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-datapipeline.


%package       -n gem-aws-sdk-iotthingsgraph
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Things Graph
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-iotthingsgraph) = 1.14.0

%description   -n gem-aws-sdk-iotthingsgraph
Official AWS Ruby gem for AWS IoT Things Graph. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-iotthingsgraph-doc
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Things Graph documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotthingsgraph
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotthingsgraph) = 1.14.0

%description   -n gem-aws-sdk-iotthingsgraph-doc
AWS SDK for Ruby - AWS IoT Things Graph documentation files.

Official AWS Ruby gem for AWS IoT Things Graph. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-iotthingsgraph-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotthingsgraph.


%package       -n gem-aws-sdk-iotthingsgraph-devel
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT Things Graph development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotthingsgraph
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotthingsgraph) = 1.14.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-iotthingsgraph-devel
AWS SDK for Ruby - AWS IoT Things Graph development package.

Official AWS Ruby gem for AWS IoT Things Graph. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-iotthingsgraph-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotthingsgraph.


%package       -n gem-aws-sdk-ecs
Version:       1.80.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon ECS
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-ecs) = 1.80.0

%description   -n gem-aws-sdk-ecs
Official AWS Ruby gem for Amazon EC2 Container Service (Amazon ECS). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ecs-doc
Version:       1.80.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon ECS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ecs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ecs) = 1.80.0

%description   -n gem-aws-sdk-ecs-doc
AWS SDK for Ruby - Amazon ECS documentation files.

Official AWS Ruby gem for Amazon EC2 Container Service (Amazon ECS). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ecs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ecs.


%package       -n gem-aws-sdk-ecs-devel
Version:       1.80.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon ECS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ecs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ecs) = 1.80.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ecs-devel
AWS SDK for Ruby - Amazon ECS development package.

Official AWS Ruby gem for Amazon EC2 Container Service (Amazon ECS). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ecs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ecs.


%package       -n gem-aws-sdk-mq
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonMQ
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-mq) = 1.36.0

%description   -n gem-aws-sdk-mq
Official AWS Ruby gem for AmazonMQ. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-mq-doc
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonMQ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-mq
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-mq) = 1.36.0

%description   -n gem-aws-sdk-mq-doc
AWS SDK for Ruby - AmazonMQ documentation files.

Official AWS Ruby gem for AmazonMQ. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mq-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-mq.


%package       -n gem-aws-sdk-mq-devel
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonMQ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-mq
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-mq) = 1.36.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-mq-devel
AWS SDK for Ruby - AmazonMQ development package.

Official AWS Ruby gem for AmazonMQ. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-mq-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-mq.


%package       -n gem-aws-sdk-ebs
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EBS
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-ebs) = 1.13.0

%description   -n gem-aws-sdk-ebs
Official AWS Ruby gem for Amazon Elastic Block Store (Amazon EBS). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ebs-doc
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EBS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ebs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ebs) = 1.13.0

%description   -n gem-aws-sdk-ebs-doc
AWS SDK for Ruby - Amazon EBS documentation files.

Official AWS Ruby gem for Amazon Elastic Block Store (Amazon EBS). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ebs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ebs.


%package       -n gem-aws-sdk-ebs-devel
Version:       1.13.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon EBS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ebs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ebs) = 1.13.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ebs-devel
AWS SDK for Ruby - Amazon EBS development package.

Official AWS Ruby gem for Amazon Elastic Block Store (Amazon EBS). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ebs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ebs.


%package       -n gem-aws-sdk-prometheusservice
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Prometheus Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-prometheusservice) = 1.3.0

%description   -n gem-aws-sdk-prometheusservice
Official AWS Ruby gem for Amazon Prometheus Service. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-prometheusservice-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Prometheus Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-prometheusservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-prometheusservice) = 1.3.0

%description   -n gem-aws-sdk-prometheusservice-doc
AWS SDK for Ruby - Amazon Prometheus Service documentation files.

Official AWS Ruby gem for Amazon Prometheus Service. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-prometheusservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-prometheusservice.


%package       -n gem-aws-sdk-prometheusservice-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Prometheus Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-prometheusservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-prometheusservice) = 1.3.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-prometheusservice-devel
AWS SDK for Ruby - Amazon Prometheus Service development package.

Official AWS Ruby gem for Amazon Prometheus Service. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-prometheusservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-prometheusservice.


%package       -n gem-aws-sdk-ssm
Version:       1.111.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SSM
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-ssm) = 1.111.0

%description   -n gem-aws-sdk-ssm
Official AWS Ruby gem for Amazon Simple Systems Manager (SSM) (Amazon SSM). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ssm-doc
Version:       1.111.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SSM documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ssm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ssm) = 1.111.0

%description   -n gem-aws-sdk-ssm-doc
AWS SDK for Ruby - Amazon SSM documentation files.

Official AWS Ruby gem for Amazon Simple Systems Manager (SSM) (Amazon SSM). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ssm.


%package       -n gem-aws-sdk-ssm-devel
Version:       1.111.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SSM development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ssm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ssm) = 1.111.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ssm-devel
AWS SDK for Ruby - Amazon SSM development package.

Official AWS Ruby gem for Amazon Simple Systems Manager (SSM) (Amazon SSM). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ssm.


%package       -n gem-aws-sdk-workspaces
Version:       1.53.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkSpaces
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-workspaces) = 1.53.0

%description   -n gem-aws-sdk-workspaces
Official AWS Ruby gem for Amazon WorkSpaces. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-workspaces-doc
Version:       1.53.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkSpaces documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-workspaces
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-workspaces) = 1.53.0

%description   -n gem-aws-sdk-workspaces-doc
AWS SDK for Ruby - Amazon WorkSpaces documentation files.

Official AWS Ruby gem for Amazon WorkSpaces. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-workspaces-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-workspaces.


%package       -n gem-aws-sdk-workspaces-devel
Version:       1.53.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon WorkSpaces development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-workspaces
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-workspaces) = 1.53.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-workspaces-devel
AWS SDK for Ruby - Amazon WorkSpaces development package.

Official AWS Ruby gem for Amazon WorkSpaces. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-workspaces-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-workspaces.


%package       -n gem-aws-sdk-schemas
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Schemas
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-schemas) = 1.12.0

%description   -n gem-aws-sdk-schemas
Official AWS Ruby gem for Schemas. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-schemas-doc
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Schemas documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-schemas
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-schemas) = 1.12.0

%description   -n gem-aws-sdk-schemas-doc
AWS SDK for Ruby - Schemas documentation files.

Official AWS Ruby gem for Schemas. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-schemas-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-schemas.


%package       -n gem-aws-sdk-schemas-devel
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Schemas development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-schemas
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-schemas) = 1.12.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-schemas-devel
AWS SDK for Ruby - Schemas development package.

Official AWS Ruby gem for Schemas. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-schemas-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-schemas.


%package       -n gem-aws-sdk-licensemanager
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS License Manager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-licensemanager) = 1.27.0

%description   -n gem-aws-sdk-licensemanager
Official AWS Ruby gem for AWS License Manager. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-licensemanager-doc
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS License Manager documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-licensemanager
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-licensemanager) = 1.27.0

%description   -n gem-aws-sdk-licensemanager-doc
AWS SDK for Ruby - AWS License Manager documentation files.

Official AWS Ruby gem for AWS License Manager. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-licensemanager-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-licensemanager.


%package       -n gem-aws-sdk-licensemanager-devel
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS License Manager development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-licensemanager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-licensemanager) = 1.27.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-licensemanager-devel
AWS SDK for Ruby - AWS License Manager development package.

Official AWS Ruby gem for AWS License Manager. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-licensemanager-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-licensemanager.


%package       -n gem-aws-sdk-ssooidc
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - SSO OIDC
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-ssooidc) = 1.10.0

%description   -n gem-aws-sdk-ssooidc
Official AWS Ruby gem for AWS SSO OIDC (SSO OIDC). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-ssooidc-doc
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - SSO OIDC documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ssooidc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ssooidc) = 1.10.0

%description   -n gem-aws-sdk-ssooidc-doc
AWS SDK for Ruby - SSO OIDC documentation files.

Official AWS Ruby gem for AWS SSO OIDC (SSO OIDC). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-ssooidc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ssooidc.


%package       -n gem-aws-sdk-ssooidc-devel
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - SSO OIDC development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ssooidc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ssooidc) = 1.10.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ssooidc-devel
AWS SDK for Ruby - SSO OIDC development package.

Official AWS Ruby gem for AWS SSO OIDC (SSO OIDC). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-ssooidc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ssooidc.


%package       -n gem-aws-sdk-signer
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - signer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-signer) = 1.29.0

%description   -n gem-aws-sdk-signer
Official AWS Ruby gem for AWS Signer (signer). This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-signer-doc
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - signer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-signer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-signer) = 1.29.0

%description   -n gem-aws-sdk-signer-doc
AWS SDK for Ruby - signer documentation files.

Official AWS Ruby gem for AWS Signer (signer). This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-signer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-signer.


%package       -n gem-aws-sdk-signer-devel
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - signer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-signer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-signer) = 1.29.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-signer-devel
AWS SDK for Ruby - signer development package.

Official AWS Ruby gem for AWS Signer (signer). This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-signer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-signer.


%package       -n gem-aws-sdk-ses
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SES
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-ses) = 1.38.0

%description   -n gem-aws-sdk-ses
Official AWS Ruby gem for Amazon Simple Email Service (Amazon SES). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ses-doc
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SES documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ses
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ses) = 1.38.0

%description   -n gem-aws-sdk-ses-doc
AWS SDK for Ruby - Amazon SES documentation files.

Official AWS Ruby gem for Amazon Simple Email Service (Amazon SES). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ses-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ses.


%package       -n gem-aws-sdk-ses-devel
Version:       1.38.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon SES development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ses
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ses) = 1.38.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ses-devel
AWS SDK for Ruby - Amazon SES development package.

Official AWS Ruby gem for Amazon Simple Email Service (Amazon SES). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ses-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ses.


%package       -n gem-aws-sdk-inspector
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Inspector
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-inspector) = 1.34.0

%description   -n gem-aws-sdk-inspector
Official AWS Ruby gem for Amazon Inspector. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-inspector-doc
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Inspector documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-inspector
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-inspector) = 1.34.0

%description   -n gem-aws-sdk-inspector-doc
AWS SDK for Ruby - Amazon Inspector documentation files.

Official AWS Ruby gem for Amazon Inspector. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-inspector-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-inspector.


%package       -n gem-aws-sdk-inspector-devel
Version:       1.34.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Inspector development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-inspector
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-inspector) = 1.34.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-inspector-devel
AWS SDK for Ruby - Amazon Inspector development package.

Official AWS Ruby gem for Amazon Inspector. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-inspector-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-inspector.


%package       -n gem-aws-sdk-chime
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-chime) = 1.46.0

%description   -n gem-aws-sdk-chime
Official AWS Ruby gem for Amazon Chime. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-chime-doc
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-chime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-chime) = 1.46.0

%description   -n gem-aws-sdk-chime-doc
AWS SDK for Ruby - Amazon Chime documentation files.

Official AWS Ruby gem for Amazon Chime. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-chime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-chime.


%package       -n gem-aws-sdk-chime-devel
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Chime development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-chime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-chime) = 1.46.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-chime-devel
AWS SDK for Ruby - Amazon Chime development package.

Official AWS Ruby gem for Amazon Chime. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-chime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-chime.


%package       -n gem-aws-sdk-elasticinference
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Elastic Inference
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-elasticinference) = 1.12.0

%description   -n gem-aws-sdk-elasticinference
Official AWS Ruby gem for Amazon Elastic Inference (Amazon Elastic Inference).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-elasticinference-doc
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Elastic Inference documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-elasticinference
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticinference) = 1.12.0

%description   -n gem-aws-sdk-elasticinference-doc
AWS SDK for Ruby - Amazon Elastic Inference documentation files.

Official AWS Ruby gem for Amazon Elastic Inference (Amazon Elastic Inference).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-elasticinference-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-elasticinference.


%package       -n gem-aws-sdk-elasticinference-devel
Version:       1.12.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Elastic Inference development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-elasticinference
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticinference) = 1.12.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-elasticinference-devel
AWS SDK for Ruby - Amazon Elastic Inference development package.

Official AWS Ruby gem for Amazon Elastic Inference (Amazon Elastic Inference).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-elasticinference-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-elasticinference.


%package       -n gem-aws-sdk-autoscalingplans
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Auto Scaling Plans
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-autoscalingplans) = 1.31.0

%description   -n gem-aws-sdk-autoscalingplans
Official AWS Ruby gem for AWS Auto Scaling Plans. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-autoscalingplans-doc
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Auto Scaling Plans documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-autoscalingplans
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-autoscalingplans) = 1.31.0

%description   -n gem-aws-sdk-autoscalingplans-doc
AWS SDK for Ruby - AWS Auto Scaling Plans documentation files.

Official AWS Ruby gem for AWS Auto Scaling Plans. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-autoscalingplans-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-autoscalingplans.


%package       -n gem-aws-sdk-autoscalingplans-devel
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Auto Scaling Plans development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-autoscalingplans
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-autoscalingplans) = 1.31.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-autoscalingplans-devel
AWS SDK for Ruby - AWS Auto Scaling Plans development package.

Official AWS Ruby gem for AWS Auto Scaling Plans. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-autoscalingplans-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-autoscalingplans.


%package       -n gem-aws-sdk-cognitosync
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Cognito Sync
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-cognitosync) = 1.27.0

%description   -n gem-aws-sdk-cognitosync
Official AWS Ruby gem for Amazon Cognito Sync. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-cognitosync-doc
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Cognito Sync documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cognitosync
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cognitosync) = 1.27.0

%description   -n gem-aws-sdk-cognitosync-doc
AWS SDK for Ruby - Amazon Cognito Sync documentation files.

Official AWS Ruby gem for Amazon Cognito Sync. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-cognitosync-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cognitosync.


%package       -n gem-aws-sdk-cognitosync-devel
Version:       1.27.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Cognito Sync development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cognitosync
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cognitosync) = 1.27.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-cognitosync-devel
AWS SDK for Ruby - Amazon Cognito Sync development package.

Official AWS Ruby gem for Amazon Cognito Sync. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-cognitosync-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cognitosync.


%package       -n gem-aws-sdk-backup
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Backup
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-backup) = 1.28.0

%description   -n gem-aws-sdk-backup
Official AWS Ruby gem for AWS Backup. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-backup-doc
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Backup documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-backup
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-backup) = 1.28.0

%description   -n gem-aws-sdk-backup-doc
AWS SDK for Ruby - AWS Backup documentation files.

Official AWS Ruby gem for AWS Backup. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-backup-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-backup.


%package       -n gem-aws-sdk-backup-devel
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Backup development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-backup
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-backup) = 1.28.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-backup-devel
AWS SDK for Ruby - AWS Backup development package.

Official AWS Ruby gem for AWS Backup. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-backup-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-backup.


%package       -n gem-aws-sdk-elasticsearchservice
Version:       1.52.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Elasticsearch Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-elasticsearchservice) = 1.52.0

%description   -n gem-aws-sdk-elasticsearchservice
Official AWS Ruby gem for Amazon Elasticsearch Service. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-elasticsearchservice-doc
Version:       1.52.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Elasticsearch Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-elasticsearchservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticsearchservice) = 1.52.0

%description   -n gem-aws-sdk-elasticsearchservice-doc
AWS SDK for Ruby - Amazon Elasticsearch Service documentation files.

Official AWS Ruby gem for Amazon Elasticsearch Service. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-elasticsearchservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-elasticsearchservice.


%package       -n gem-aws-sdk-elasticsearchservice-devel
Version:       1.52.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Elasticsearch Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-elasticsearchservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-elasticsearchservice) = 1.52.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-elasticsearchservice-devel
AWS SDK for Ruby - Amazon Elasticsearch Service development package.

Official AWS Ruby gem for Amazon Elasticsearch Service. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-elasticsearchservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-elasticsearchservice.


%package       -n gem-aws-sdk-imagebuilder
Version:       1.22.0
Release:       alt1
Summary:       AWS SDK for Ruby - imagebuilder
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-imagebuilder) = 1.22.0

%description   -n gem-aws-sdk-imagebuilder
Official AWS Ruby gem for EC2 Image Builder (imagebuilder). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-imagebuilder-doc
Version:       1.22.0
Release:       alt1
Summary:       AWS SDK for Ruby - imagebuilder documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-imagebuilder
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-imagebuilder) = 1.22.0

%description   -n gem-aws-sdk-imagebuilder-doc
AWS SDK for Ruby - imagebuilder documentation files.

Official AWS Ruby gem for EC2 Image Builder (imagebuilder). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-imagebuilder-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-imagebuilder.


%package       -n gem-aws-sdk-imagebuilder-devel
Version:       1.22.0
Release:       alt1
Summary:       AWS SDK for Ruby - imagebuilder development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-imagebuilder
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-imagebuilder) = 1.22.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-imagebuilder-devel
AWS SDK for Ruby - imagebuilder development package.

Official AWS Ruby gem for EC2 Image Builder (imagebuilder). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-imagebuilder-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-imagebuilder.


%package       -n gem-aws-sdk-lexruntimev2
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Lex Runtime V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-lexruntimev2) = 1.2.0

%description   -n gem-aws-sdk-lexruntimev2
Official AWS Ruby gem for Amazon Lex Runtime V2 (Lex Runtime V2). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-lexruntimev2-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Lex Runtime V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lexruntimev2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lexruntimev2) = 1.2.0

%description   -n gem-aws-sdk-lexruntimev2-doc
AWS SDK for Ruby - Lex Runtime V2 documentation files.

Official AWS Ruby gem for Amazon Lex Runtime V2 (Lex Runtime V2). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lexruntimev2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lexruntimev2.


%package       -n gem-aws-sdk-lexruntimev2-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - Lex Runtime V2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lexruntimev2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lexruntimev2) = 1.2.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-lexruntimev2-devel
AWS SDK for Ruby - Lex Runtime V2 development package.

Official AWS Ruby gem for Amazon Lex Runtime V2 (Lex Runtime V2). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lexruntimev2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lexruntimev2.


%package       -n gem-aws-sdk-finspacedata
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - FinSpace Data
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-finspacedata) = 1.1.0

%description   -n gem-aws-sdk-finspacedata
Official AWS Ruby gem for FinSpace Public API (FinSpace Data). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-finspacedata-doc
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - FinSpace Data documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-finspacedata
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-finspacedata) = 1.1.0

%description   -n gem-aws-sdk-finspacedata-doc
AWS SDK for Ruby - FinSpace Data documentation files.

Official AWS Ruby gem for FinSpace Public API (FinSpace Data). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-finspacedata-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-finspacedata.


%package       -n gem-aws-sdk-finspacedata-devel
Version:       1.1.0
Release:       alt1
Summary:       AWS SDK for Ruby - FinSpace Data development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-finspacedata
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-finspacedata) = 1.1.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-finspacedata-devel
AWS SDK for Ruby - FinSpace Data development package.

Official AWS Ruby gem for FinSpace Public API (FinSpace Data). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-finspacedata-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-finspacedata.


%package       -n gem-aws-sdk-apigatewaymanagementapi
Version:       1.21.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonApiGatewayManagementApi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-apigatewaymanagementapi) = 1.21.0

%description   -n gem-aws-sdk-apigatewaymanagementapi
Official AWS Ruby gem for AmazonApiGatewayManagementApi. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-apigatewaymanagementapi-doc
Version:       1.21.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonApiGatewayManagementApi documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-apigatewaymanagementapi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-apigatewaymanagementapi) = 1.21.0

%description   -n gem-aws-sdk-apigatewaymanagementapi-doc
AWS SDK for Ruby - AmazonApiGatewayManagementApi documentation files.

Official AWS Ruby gem for AmazonApiGatewayManagementApi. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-apigatewaymanagementapi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-apigatewaymanagementapi.


%package       -n gem-aws-sdk-apigatewaymanagementapi-devel
Version:       1.21.0
Release:       alt1
Summary:       AWS SDK for Ruby - AmazonApiGatewayManagementApi development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-apigatewaymanagementapi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-apigatewaymanagementapi) = 1.21.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-apigatewaymanagementapi-devel
AWS SDK for Ruby - AmazonApiGatewayManagementApi development package.

Official AWS Ruby gem for AmazonApiGatewayManagementApi. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-apigatewaymanagementapi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-apigatewaymanagementapi.


%package       -n gem-aws-sdk-redshift
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Redshift
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-redshift) = 1.62.0

%description   -n gem-aws-sdk-redshift
Official AWS Ruby gem for Amazon Redshift. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-redshift-doc
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Redshift documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-redshift
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-redshift) = 1.62.0

%description   -n gem-aws-sdk-redshift-doc
AWS SDK for Ruby - Amazon Redshift documentation files.

Official AWS Ruby gem for Amazon Redshift. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-redshift-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-redshift.


%package       -n gem-aws-sdk-redshift-devel
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Redshift development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-redshift
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-redshift) = 1.62.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-redshift-devel
AWS SDK for Ruby - Amazon Redshift development package.

Official AWS Ruby gem for Amazon Redshift. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-redshift-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-redshift.


%package       -n gem-aws-sdk-kinesis
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-kinesis) = 1.32.0

%description   -n gem-aws-sdk-kinesis
Official AWS Ruby gem for Amazon Kinesis (Kinesis). This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-kinesis-doc
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesis) = 1.32.0

%description   -n gem-aws-sdk-kinesis-doc
AWS SDK for Ruby - Kinesis documentation files.

Official AWS Ruby gem for Amazon Kinesis (Kinesis). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-kinesis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesis.


%package       -n gem-aws-sdk-kinesis-devel
Version:       1.32.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesis
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesis) = 1.32.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-kinesis-devel
AWS SDK for Ruby - Kinesis development package.

Official AWS Ruby gem for Amazon Kinesis (Kinesis). This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-kinesis-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesis.


%package       -n gem-aws-sdk-apprunner
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS App Runner
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-apprunner) = 1.0.0

%description   -n gem-aws-sdk-apprunner
Official AWS Ruby gem for AWS App Runner. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-apprunner-doc
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS App Runner documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-apprunner
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-apprunner) = 1.0.0

%description   -n gem-aws-sdk-apprunner-doc
AWS SDK for Ruby - AWS App Runner documentation files.

Official AWS Ruby gem for AWS App Runner. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-apprunner-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-apprunner.


%package       -n gem-aws-sdk-apprunner-devel
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS App Runner development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-apprunner
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-apprunner) = 1.0.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-apprunner-devel
AWS SDK for Ruby - AWS App Runner development package.

Official AWS Ruby gem for AWS App Runner. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-apprunner-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-apprunner.


%package       -n gem-aws-sdk-applicationautoscaling
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - Application Auto Scaling
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-applicationautoscaling) = 1.51.0

%description   -n gem-aws-sdk-applicationautoscaling
Official AWS Ruby gem for Application Auto Scaling. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-applicationautoscaling-doc
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - Application Auto Scaling documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-applicationautoscaling
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationautoscaling) = 1.51.0

%description   -n gem-aws-sdk-applicationautoscaling-doc
AWS SDK for Ruby - Application Auto Scaling documentation files.

Official AWS Ruby gem for Application Auto Scaling. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-applicationautoscaling-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-applicationautoscaling.


%package       -n gem-aws-sdk-applicationautoscaling-devel
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - Application Auto Scaling development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-applicationautoscaling
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationautoscaling) = 1.51.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-applicationautoscaling-devel
AWS SDK for Ruby - Application Auto Scaling development package.

Official AWS Ruby gem for Application Auto Scaling. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-applicationautoscaling-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-applicationautoscaling.


%package       -n gem-aws-sdk-kinesisvideomedia
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Video Media
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-kinesisvideomedia) = 1.28.0

%description   -n gem-aws-sdk-kinesisvideomedia
Official AWS Ruby gem for Amazon Kinesis Video Streams Media (Kinesis Video
Media). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kinesisvideomedia-doc
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Video Media documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesisvideomedia
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideomedia) = 1.28.0

%description   -n gem-aws-sdk-kinesisvideomedia-doc
AWS SDK for Ruby - Kinesis Video Media documentation files.

Official AWS Ruby gem for Amazon Kinesis Video Streams Media (Kinesis Video
Media). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideomedia-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesisvideomedia.


%package       -n gem-aws-sdk-kinesisvideomedia-devel
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Video Media development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesisvideomedia
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisvideomedia) = 1.28.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-kinesisvideomedia-devel
AWS SDK for Ruby - Kinesis Video Media development package.

Official AWS Ruby gem for Amazon Kinesis Video Streams Media (Kinesis Video
Media). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisvideomedia-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesisvideomedia.


%package       -n gem-aws-sdk-appflow
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Appflow
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-appflow) = 1.10.0

%description   -n gem-aws-sdk-appflow
Official AWS Ruby gem for Amazon Appflow. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-appflow-doc
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Appflow documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appflow
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appflow) = 1.10.0

%description   -n gem-aws-sdk-appflow-doc
AWS SDK for Ruby - Amazon Appflow documentation files.

Official AWS Ruby gem for Amazon Appflow. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-appflow-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appflow.


%package       -n gem-aws-sdk-appflow-devel
Version:       1.10.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Appflow development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appflow
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appflow) = 1.10.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-appflow-devel
AWS SDK for Ruby - Amazon Appflow development package.

Official AWS Ruby gem for Amazon Appflow. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-appflow-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appflow.


%package       -n gem-aws-sdk-greengrassv2
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS GreengrassV2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-greengrassv2) = 1.3.0

%description   -n gem-aws-sdk-greengrassv2
Official AWS Ruby gem for AWS IoT Greengrass V2 (AWS GreengrassV2). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-greengrassv2-doc
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS GreengrassV2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-greengrassv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-greengrassv2) = 1.3.0

%description   -n gem-aws-sdk-greengrassv2-doc
AWS SDK for Ruby - AWS GreengrassV2 documentation files.

Official AWS Ruby gem for AWS IoT Greengrass V2 (AWS GreengrassV2). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-greengrassv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-greengrassv2.


%package       -n gem-aws-sdk-greengrassv2-devel
Version:       1.3.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS GreengrassV2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-greengrassv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-greengrassv2) = 1.3.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-greengrassv2-devel
AWS SDK for Ruby - AWS GreengrassV2 development package.

Official AWS Ruby gem for AWS IoT Greengrass V2 (AWS GreengrassV2). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-greengrassv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-greengrassv2.


%package       -n gem-aws-sdk-health
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSHealth
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-health) = 1.35.0

%description   -n gem-aws-sdk-health
Official AWS Ruby gem for AWS Health APIs and Notifications (AWSHealth). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-health-doc
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSHealth documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-health
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-health) = 1.35.0

%description   -n gem-aws-sdk-health-doc
AWS SDK for Ruby - AWSHealth documentation files.

Official AWS Ruby gem for AWS Health APIs and Notifications (AWSHealth). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-health-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-health.


%package       -n gem-aws-sdk-health-devel
Version:       1.35.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWSHealth development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-health
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-health) = 1.35.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-health-devel
AWS SDK for Ruby - AWSHealth development package.

Official AWS Ruby gem for AWS Health APIs and Notifications (AWSHealth). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-health-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-health.


%package       -n gem-aws-sdk-migrationhub
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Migration Hub
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-migrationhub) = 1.31.0

%description   -n gem-aws-sdk-migrationhub
Official AWS Ruby gem for AWS Migration Hub. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-migrationhub-doc
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Migration Hub documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-migrationhub
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-migrationhub) = 1.31.0

%description   -n gem-aws-sdk-migrationhub-doc
AWS SDK for Ruby - AWS Migration Hub documentation files.

Official AWS Ruby gem for AWS Migration Hub. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-migrationhub-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-migrationhub.


%package       -n gem-aws-sdk-migrationhub-devel
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Migration Hub development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-migrationhub
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-migrationhub) = 1.31.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-migrationhub-devel
AWS SDK for Ruby - AWS Migration Hub development package.

Official AWS Ruby gem for AWS Migration Hub. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-migrationhub-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-migrationhub.


%package       -n gem-aws-sdk-costexplorer
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Cost Explorer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-costexplorer) = 1.62.0

%description   -n gem-aws-sdk-costexplorer
Official AWS Ruby gem for AWS Cost Explorer Service (AWS Cost Explorer). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-costexplorer-doc
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Cost Explorer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-costexplorer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-costexplorer) = 1.62.0

%description   -n gem-aws-sdk-costexplorer-doc
AWS SDK for Ruby - AWS Cost Explorer documentation files.

Official AWS Ruby gem for AWS Cost Explorer Service (AWS Cost Explorer). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-costexplorer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-costexplorer.


%package       -n gem-aws-sdk-costexplorer-devel
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Cost Explorer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-costexplorer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-costexplorer) = 1.62.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-costexplorer-devel
AWS SDK for Ruby - AWS Cost Explorer development package.

Official AWS Ruby gem for AWS Cost Explorer Service (AWS Cost Explorer). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-costexplorer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-costexplorer.


%package       -n gem-aws-sdk-ivs
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon IVS
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-ivs) = 1.9.0

%description   -n gem-aws-sdk-ivs
Official AWS Ruby gem for Amazon Interactive Video Service (Amazon IVS). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ivs-doc
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon IVS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ivs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ivs) = 1.9.0

%description   -n gem-aws-sdk-ivs-doc
AWS SDK for Ruby - Amazon IVS documentation files.

Official AWS Ruby gem for Amazon Interactive Video Service (Amazon IVS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ivs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ivs.


%package       -n gem-aws-sdk-ivs-devel
Version:       1.9.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon IVS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ivs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ivs) = 1.9.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ivs-devel
AWS SDK for Ruby - Amazon IVS development package.

Official AWS Ruby gem for Amazon Interactive Video Service (Amazon IVS). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ivs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ivs.


%package       -n gem-aws-sdk-globalaccelerator
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Global Accelerator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-globalaccelerator) = 1.30.0

%description   -n gem-aws-sdk-globalaccelerator
Official AWS Ruby gem for AWS Global Accelerator. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-globalaccelerator-doc
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Global Accelerator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-globalaccelerator
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-globalaccelerator) = 1.30.0

%description   -n gem-aws-sdk-globalaccelerator-doc
AWS SDK for Ruby - AWS Global Accelerator documentation files.

Official AWS Ruby gem for AWS Global Accelerator. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-globalaccelerator-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-globalaccelerator.


%package       -n gem-aws-sdk-globalaccelerator-devel
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Global Accelerator development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-globalaccelerator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-globalaccelerator) = 1.30.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-globalaccelerator-devel
AWS SDK for Ruby - AWS Global Accelerator development package.

Official AWS Ruby gem for AWS Global Accelerator. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-globalaccelerator-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-globalaccelerator.


%package       -n gem-aws-sdk-ssmincidents
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - SSM Incidents
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-ssmincidents) = 1.0.0

%description   -n gem-aws-sdk-ssmincidents
Official AWS Ruby gem for AWS Systems Manager Incident Manager (SSM Incidents).
This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-ssmincidents-doc
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - SSM Incidents documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-ssmincidents
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-ssmincidents) = 1.0.0

%description   -n gem-aws-sdk-ssmincidents-doc
AWS SDK for Ruby - SSM Incidents documentation files.

Official AWS Ruby gem for AWS Systems Manager Incident Manager (SSM Incidents).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssmincidents-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-ssmincidents.


%package       -n gem-aws-sdk-ssmincidents-devel
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - SSM Incidents development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-ssmincidents
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-ssmincidents) = 1.0.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-ssmincidents-devel
AWS SDK for Ruby - SSM Incidents development package.

Official AWS Ruby gem for AWS Systems Manager Incident Manager (SSM Incidents).
This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-ssmincidents-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-ssmincidents.


%package       -n gem-aws-sdk-iotsitewise
Version:       1.23.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT SiteWise
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-iotsitewise) = 1.23.0

%description   -n gem-aws-sdk-iotsitewise
Official AWS Ruby gem for AWS IoT SiteWise. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-iotsitewise-doc
Version:       1.23.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT SiteWise documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iotsitewise
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iotsitewise) = 1.23.0

%description   -n gem-aws-sdk-iotsitewise-doc
AWS SDK for Ruby - AWS IoT SiteWise documentation files.

Official AWS Ruby gem for AWS IoT SiteWise. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-iotsitewise-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iotsitewise.


%package       -n gem-aws-sdk-iotsitewise-devel
Version:       1.23.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT SiteWise development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iotsitewise
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iotsitewise) = 1.23.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-iotsitewise-devel
AWS SDK for Ruby - AWS IoT SiteWise development package.

Official AWS Ruby gem for AWS IoT SiteWise. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-iotsitewise-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iotsitewise.


%package       -n gem-aws-sdk-wafv2
Version:       1.20.0
Release:       alt1
Summary:       AWS SDK for Ruby - WAFV2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-wafv2) = 1.20.0

%description   -n gem-aws-sdk-wafv2
Official AWS Ruby gem for AWS WAFV2 (WAFV2). This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-wafv2-doc
Version:       1.20.0
Release:       alt1
Summary:       AWS SDK for Ruby - WAFV2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-wafv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-wafv2) = 1.20.0

%description   -n gem-aws-sdk-wafv2-doc
AWS SDK for Ruby - WAFV2 documentation files.

Official AWS Ruby gem for AWS WAFV2 (WAFV2). This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-wafv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-wafv2.


%package       -n gem-aws-sdk-wafv2-devel
Version:       1.20.0
Release:       alt1
Summary:       AWS SDK for Ruby - WAFV2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-wafv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-wafv2) = 1.20.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-wafv2-devel
AWS SDK for Ruby - WAFV2 development package.

Official AWS Ruby gem for AWS WAFV2 (WAFV2). This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-wafv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-wafv2.


%package       -n gem-aws-sdk-kinesisanalyticsv2
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Analytics V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-kinesisanalyticsv2) = 1.30.0

%description   -n gem-aws-sdk-kinesisanalyticsv2
Official AWS Ruby gem for Amazon Kinesis Analytics (Kinesis Analytics V2). This
gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-kinesisanalyticsv2-doc
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Analytics V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-kinesisanalyticsv2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisanalyticsv2) = 1.30.0

%description   -n gem-aws-sdk-kinesisanalyticsv2-doc
AWS SDK for Ruby - Kinesis Analytics V2 documentation files.

Official AWS Ruby gem for Amazon Kinesis Analytics (Kinesis Analytics V2). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisanalyticsv2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-kinesisanalyticsv2.


%package       -n gem-aws-sdk-kinesisanalyticsv2-devel
Version:       1.30.0
Release:       alt1
Summary:       AWS SDK for Ruby - Kinesis Analytics V2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-kinesisanalyticsv2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-kinesisanalyticsv2) = 1.30.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-kinesisanalyticsv2-devel
AWS SDK for Ruby - Kinesis Analytics V2 development package.

Official AWS Ruby gem for Amazon Kinesis Analytics (Kinesis Analytics V2). This
gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-kinesisanalyticsv2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-kinesisanalyticsv2.


%package       -n gem-aws-sdk-macie
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Macie
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-macie) = 1.28.0

%description   -n gem-aws-sdk-macie
Official AWS Ruby gem for Amazon Macie. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-macie-doc
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Macie documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-macie
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-macie) = 1.28.0

%description   -n gem-aws-sdk-macie-doc
AWS SDK for Ruby - Amazon Macie documentation files.

Official AWS Ruby gem for Amazon Macie. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-macie-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-macie.


%package       -n gem-aws-sdk-macie-devel
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Macie development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-macie
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-macie) = 1.28.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-macie-devel
AWS SDK for Ruby - Amazon Macie development package.

Official AWS Ruby gem for Amazon Macie. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-macie-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-macie.


%package       -n gem-aws-sdk-polly
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Polly
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-polly) = 1.41.0

%description   -n gem-aws-sdk-polly
Official AWS Ruby gem for Amazon Polly. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-polly-doc
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Polly documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-polly
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-polly) = 1.41.0

%description   -n gem-aws-sdk-polly-doc
AWS SDK for Ruby - Amazon Polly documentation files.

Official AWS Ruby gem for Amazon Polly. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-polly-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-polly.


%package       -n gem-aws-sdk-polly-devel
Version:       1.41.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Polly development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-polly
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-polly) = 1.41.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-polly-devel
AWS SDK for Ruby - Amazon Polly development package.

Official AWS Ruby gem for Amazon Polly. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-polly-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-polly.


%package       -n gem-aws-sdk-support
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Support
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-support) = 1.31.0

%description   -n gem-aws-sdk-support
Official AWS Ruby gem for AWS Support. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-support-doc
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Support documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-support
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-support) = 1.31.0

%description   -n gem-aws-sdk-support-doc
AWS SDK for Ruby - AWS Support documentation files.

Official AWS Ruby gem for AWS Support. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-support-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-support.


%package       -n gem-aws-sdk-support-devel
Version:       1.31.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Support development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-support
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-support) = 1.31.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-support-devel
AWS SDK for Ruby - AWS Support development package.

Official AWS Ruby gem for AWS Support. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-support-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-support.


%package       -n gem-aws-sdk-marketplaceentitlementservice
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Marketplace Entitlement Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-marketplaceentitlementservice) = 1.26.0

%description   -n gem-aws-sdk-marketplaceentitlementservice
Official AWS Ruby gem for AWS Marketplace Entitlement Service. This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-marketplaceentitlementservice-doc
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Marketplace Entitlement Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-marketplaceentitlementservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplaceentitlementservice) = 1.26.0

%description   -n gem-aws-sdk-marketplaceentitlementservice-doc
AWS SDK for Ruby - AWS Marketplace Entitlement Service documentation
files.

Official AWS Ruby gem for AWS Marketplace Entitlement Service. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-marketplaceentitlementservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-marketplaceentitlementservice.


%package       -n gem-aws-sdk-marketplaceentitlementservice-devel
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Marketplace Entitlement Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-marketplaceentitlementservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-marketplaceentitlementservice) = 1.26.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-marketplaceentitlementservice-devel
AWS SDK for Ruby - AWS Marketplace Entitlement Service development
package.

Official AWS Ruby gem for AWS Marketplace Entitlement Service. This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-marketplaceentitlementservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-marketplaceentitlementservice.


%package       -n gem-aws-sdk-appstream
Version:       1.52.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon AppStream
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-appstream) = 1.52.0

%description   -n gem-aws-sdk-appstream
Official AWS Ruby gem for Amazon AppStream. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-appstream-doc
Version:       1.52.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon AppStream documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-appstream
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-appstream) = 1.52.0

%description   -n gem-aws-sdk-appstream-doc
AWS SDK for Ruby - Amazon AppStream documentation files.

Official AWS Ruby gem for Amazon AppStream. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-appstream-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-appstream.


%package       -n gem-aws-sdk-appstream-devel
Version:       1.52.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon AppStream development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-appstream
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-appstream) = 1.52.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-appstream-devel
AWS SDK for Ruby - Amazon AppStream development package.

Official AWS Ruby gem for Amazon AppStream. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-appstream-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-appstream.


%package       -n gem-aws-sdk-computeoptimizer
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Compute Optimizer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-computeoptimizer) = 1.18.0

%description   -n gem-aws-sdk-computeoptimizer
Official AWS Ruby gem for AWS Compute Optimizer. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-computeoptimizer-doc
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Compute Optimizer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-computeoptimizer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-computeoptimizer) = 1.18.0

%description   -n gem-aws-sdk-computeoptimizer-doc
AWS SDK for Ruby - AWS Compute Optimizer documentation files.

Official AWS Ruby gem for AWS Compute Optimizer. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-computeoptimizer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-computeoptimizer.


%package       -n gem-aws-sdk-computeoptimizer-devel
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Compute Optimizer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-computeoptimizer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-computeoptimizer) = 1.18.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-computeoptimizer-devel
AWS SDK for Ruby - AWS Compute Optimizer development package.

Official AWS Ruby gem for AWS Compute Optimizer. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-computeoptimizer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-computeoptimizer.


%package       -n gem-aws-sdk-iot1clickprojects
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT 1-Click Projects
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-iot1clickprojects) = 1.28.0

%description   -n gem-aws-sdk-iot1clickprojects
Official AWS Ruby gem for AWS IoT 1-Click Projects Service (AWS IoT 1-Click
Projects). This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-iot1clickprojects-doc
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT 1-Click Projects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-iot1clickprojects
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-iot1clickprojects) = 1.28.0

%description   -n gem-aws-sdk-iot1clickprojects-doc
AWS SDK for Ruby - AWS IoT 1-Click Projects documentation files.

Official AWS Ruby gem for AWS IoT 1-Click Projects Service (AWS IoT 1-Click
Projects). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iot1clickprojects-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-iot1clickprojects.


%package       -n gem-aws-sdk-iot1clickprojects-devel
Version:       1.28.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS IoT 1-Click Projects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-iot1clickprojects
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-iot1clickprojects) = 1.28.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-iot1clickprojects-devel
AWS SDK for Ruby - AWS IoT 1-Click Projects development package.

Official AWS Ruby gem for AWS IoT 1-Click Projects Service (AWS IoT 1-Click
Projects). This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-iot1clickprojects-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-iot1clickprojects.


%package       -n gem-aws-sdk-lightsail
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Lightsail
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-lightsail) = 1.51.0

%description   -n gem-aws-sdk-lightsail
Official AWS Ruby gem for Amazon Lightsail. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-lightsail-doc
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Lightsail documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lightsail
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lightsail) = 1.51.0

%description   -n gem-aws-sdk-lightsail-doc
AWS SDK for Ruby - Amazon Lightsail documentation files.

Official AWS Ruby gem for Amazon Lightsail. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-lightsail-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lightsail.


%package       -n gem-aws-sdk-lightsail-devel
Version:       1.51.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Lightsail development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lightsail
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lightsail) = 1.51.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-lightsail-devel
AWS SDK for Ruby - Amazon Lightsail development package.

Official AWS Ruby gem for Amazon Lightsail. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-lightsail-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lightsail.


%package       -n gem-aws-sdk-auditmanager
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Audit Manager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-auditmanager) = 1.7.0

%description   -n gem-aws-sdk-auditmanager
Official AWS Ruby gem for AWS Audit Manager. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-auditmanager-doc
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Audit Manager documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-auditmanager
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-auditmanager) = 1.7.0

%description   -n gem-aws-sdk-auditmanager-doc
AWS SDK for Ruby - AWS Audit Manager documentation files.

Official AWS Ruby gem for AWS Audit Manager. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-auditmanager-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-auditmanager.


%package       -n gem-aws-sdk-auditmanager-devel
Version:       1.7.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Audit Manager development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-auditmanager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-auditmanager) = 1.7.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-auditmanager-devel
AWS SDK for Ruby - AWS Audit Manager development package.

Official AWS Ruby gem for AWS Audit Manager. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-auditmanager-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-auditmanager.


%package       -n gem-aws-sdk-locationservice
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Location Service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-locationservice) = 1.4.0

%description   -n gem-aws-sdk-locationservice
Official AWS Ruby gem for Amazon Location Service. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-locationservice-doc
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Location Service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-locationservice
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-locationservice) = 1.4.0

%description   -n gem-aws-sdk-locationservice-doc
AWS SDK for Ruby - Amazon Location Service documentation files.

Official AWS Ruby gem for Amazon Location Service. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-locationservice-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-locationservice.


%package       -n gem-aws-sdk-locationservice-devel
Version:       1.4.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Location Service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-locationservice
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-locationservice) = 1.4.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-locationservice-devel
AWS SDK for Ruby - Amazon Location Service development package.

Official AWS Ruby gem for Amazon Location Service. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-locationservice-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-locationservice.


%package       -n gem-aws-sdk-lakeformation
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Lake Formation
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-lakeformation) = 1.14.0

%description   -n gem-aws-sdk-lakeformation
Official AWS Ruby gem for AWS Lake Formation. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-lakeformation-doc
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Lake Formation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lakeformation
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lakeformation) = 1.14.0

%description   -n gem-aws-sdk-lakeformation-doc
AWS SDK for Ruby - AWS Lake Formation documentation files.

Official AWS Ruby gem for AWS Lake Formation. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-lakeformation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lakeformation.


%package       -n gem-aws-sdk-lakeformation-devel
Version:       1.14.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Lake Formation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lakeformation
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lakeformation) = 1.14.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-lakeformation-devel
AWS SDK for Ruby - AWS Lake Formation development package.

Official AWS Ruby gem for AWS Lake Formation. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-lakeformation-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lakeformation.


%package       -n gem-aws-sdk-fms
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - FMS
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-fms) = 1.36.0

%description   -n gem-aws-sdk-fms
Official AWS Ruby gem for Firewall Management Service (FMS). This gem is part of
the AWS SDK for Ruby.


%package       -n gem-aws-sdk-fms-doc
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - FMS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-fms
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-fms) = 1.36.0

%description   -n gem-aws-sdk-fms-doc
AWS SDK for Ruby - FMS documentation files.

Official AWS Ruby gem for Firewall Management Service (FMS). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-fms-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-fms.


%package       -n gem-aws-sdk-fms-devel
Version:       1.36.0
Release:       alt1
Summary:       AWS SDK for Ruby - FMS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-fms
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-fms) = 1.36.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-fms-devel
AWS SDK for Ruby - FMS development package.

Official AWS Ruby gem for Firewall Management Service (FMS). This gem is part of
the AWS SDK for Ruby.

%description   -n gem-aws-sdk-fms-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-fms.


%package       -n gem-aws-sdk-lambda
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Lambda
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-lambda) = 1.62.0

%description   -n gem-aws-sdk-lambda
Official AWS Ruby gem for AWS Lambda. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-lambda-doc
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Lambda documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lambda
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lambda) = 1.62.0

%description   -n gem-aws-sdk-lambda-doc
AWS SDK for Ruby - AWS Lambda documentation files.

Official AWS Ruby gem for AWS Lambda. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lambda-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lambda.


%package       -n gem-aws-sdk-lambda-devel
Version:       1.62.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Lambda development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lambda
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lambda) = 1.62.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-lambda-devel
AWS SDK for Ruby - AWS Lambda development package.

Official AWS Ruby gem for AWS Lambda. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lambda-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lambda.


%package       -n gem-aws-sdk-lambdapreview
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Lambda
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-lambdapreview) = 1.26.0

%description   -n gem-aws-sdk-lambdapreview
Official AWS Ruby gem for AWS Lambda. This gem is part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-lambdapreview-doc
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Lambda documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-lambdapreview
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-lambdapreview) = 1.26.0

%description   -n gem-aws-sdk-lambdapreview-doc
AWS SDK for Ruby - AWS Lambda documentation files.

Official AWS Ruby gem for AWS Lambda. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lambdapreview-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-lambdapreview.


%package       -n gem-aws-sdk-lambdapreview-devel
Version:       1.26.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Lambda development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-lambdapreview
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-lambdapreview) = 1.26.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-lambdapreview-devel
AWS SDK for Ruby - AWS Lambda development package.

Official AWS Ruby gem for AWS Lambda. This gem is part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-lambdapreview-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-lambdapreview.


%package       -n gem-aws-sdk-cloudformation
Version:       1.52.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS CloudFormation
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-cloudformation) = 1.52.0

%description   -n gem-aws-sdk-cloudformation
Official AWS Ruby gem for AWS CloudFormation. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-cloudformation-doc
Version:       1.52.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS CloudFormation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-cloudformation
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudformation) = 1.52.0

%description   -n gem-aws-sdk-cloudformation-doc
AWS SDK for Ruby - AWS CloudFormation documentation files.

Official AWS Ruby gem for AWS CloudFormation. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-cloudformation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-cloudformation.


%package       -n gem-aws-sdk-cloudformation-devel
Version:       1.52.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS CloudFormation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-cloudformation
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-cloudformation) = 1.52.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-cloudformation-devel
AWS SDK for Ruby - AWS CloudFormation development package.

Official AWS Ruby gem for AWS CloudFormation. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-cloudformation-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-cloudformation.


%package       -n gem-aws-sdk-securityhub
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS SecurityHub
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-securityhub) = 1.46.0

%description   -n gem-aws-sdk-securityhub
Official AWS Ruby gem for AWS SecurityHub. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-securityhub-doc
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS SecurityHub documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-securityhub
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-securityhub) = 1.46.0

%description   -n gem-aws-sdk-securityhub-doc
AWS SDK for Ruby - AWS SecurityHub documentation files.

Official AWS Ruby gem for AWS SecurityHub. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-securityhub-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-securityhub.


%package       -n gem-aws-sdk-securityhub-devel
Version:       1.46.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS SecurityHub development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-securityhub
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-securityhub) = 1.46.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-securityhub-devel
AWS SDK for Ruby - AWS SecurityHub development package.

Official AWS Ruby gem for AWS SecurityHub. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-securityhub-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-securityhub.


%package       -n gem-aws-sdk-resources
Version:       3.104.0
Release:       alt1
Summary:       AWS SDK for Ruby - Resources
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-acm) >= 1 gem(aws-sdk-acm) < 2
Requires:      gem(aws-sdk-acmpca) >= 1 gem(aws-sdk-acmpca) < 2
Requires:      gem(aws-sdk-apigateway) >= 1 gem(aws-sdk-apigateway) < 2
Requires:      gem(aws-sdk-accessanalyzer) >= 1 gem(aws-sdk-accessanalyzer) < 2
Requires:      gem(aws-sdk-alexaforbusiness) >= 1 gem(aws-sdk-alexaforbusiness) < 2
Requires:      gem(aws-sdk-amplify) >= 1 gem(aws-sdk-amplify) < 2
Requires:      gem(aws-sdk-amplifybackend) >= 1 gem(aws-sdk-amplifybackend) < 2
Requires:      gem(aws-sdk-apigatewaymanagementapi) >= 1 gem(aws-sdk-apigatewaymanagementapi) < 2
Requires:      gem(aws-sdk-apigatewayv2) >= 1 gem(aws-sdk-apigatewayv2) < 2
Requires:      gem(aws-sdk-appconfig) >= 1 gem(aws-sdk-appconfig) < 2
Requires:      gem(aws-sdk-appintegrationsservice) >= 1 gem(aws-sdk-appintegrationsservice) < 2
Requires:      gem(aws-sdk-appmesh) >= 1 gem(aws-sdk-appmesh) < 2
Requires:      gem(aws-sdk-appregistry) >= 1 gem(aws-sdk-appregistry) < 2
Requires:      gem(aws-sdk-apprunner) >= 1 gem(aws-sdk-apprunner) < 2
Requires:      gem(aws-sdk-appstream) >= 1 gem(aws-sdk-appstream) < 2
Requires:      gem(aws-sdk-appsync) >= 1 gem(aws-sdk-appsync) < 2
Requires:      gem(aws-sdk-appflow) >= 1 gem(aws-sdk-appflow) < 2
Requires:      gem(aws-sdk-applicationautoscaling) >= 1 gem(aws-sdk-applicationautoscaling) < 2
Requires:      gem(aws-sdk-applicationcostprofiler) >= 1 gem(aws-sdk-applicationcostprofiler) < 2
Requires:      gem(aws-sdk-applicationdiscoveryservice) >= 1 gem(aws-sdk-applicationdiscoveryservice) < 2
Requires:      gem(aws-sdk-applicationinsights) >= 1 gem(aws-sdk-applicationinsights) < 2
Requires:      gem(aws-sdk-athena) >= 1 gem(aws-sdk-athena) < 2
Requires:      gem(aws-sdk-auditmanager) >= 1 gem(aws-sdk-auditmanager) < 2
Requires:      gem(aws-sdk-augmentedairuntime) >= 1 gem(aws-sdk-augmentedairuntime) < 2
Requires:      gem(aws-sdk-autoscaling) >= 1 gem(aws-sdk-autoscaling) < 2
Requires:      gem(aws-sdk-autoscalingplans) >= 1 gem(aws-sdk-autoscalingplans) < 2
Requires:      gem(aws-sdk-backup) >= 1 gem(aws-sdk-backup) < 2
Requires:      gem(aws-sdk-batch) >= 1 gem(aws-sdk-batch) < 2
Requires:      gem(aws-sdk-braket) >= 1 gem(aws-sdk-braket) < 2
Requires:      gem(aws-sdk-budgets) >= 1 gem(aws-sdk-budgets) < 2
Requires:      gem(aws-sdk-chime) >= 1 gem(aws-sdk-chime) < 2
Requires:      gem(aws-sdk-cloud9) >= 1 gem(aws-sdk-cloud9) < 2
Requires:      gem(aws-sdk-clouddirectory) >= 1 gem(aws-sdk-clouddirectory) < 2
Requires:      gem(aws-sdk-cloudformation) >= 1 gem(aws-sdk-cloudformation) < 2
Requires:      gem(aws-sdk-cloudfront) >= 1 gem(aws-sdk-cloudfront) < 2
Requires:      gem(aws-sdk-cloudhsm) >= 1 gem(aws-sdk-cloudhsm) < 2
Requires:      gem(aws-sdk-cloudhsmv2) >= 1 gem(aws-sdk-cloudhsmv2) < 2
Requires:      gem(aws-sdk-cloudsearch) >= 1 gem(aws-sdk-cloudsearch) < 2
Requires:      gem(aws-sdk-cloudsearchdomain) >= 1 gem(aws-sdk-cloudsearchdomain) < 2
Requires:      gem(aws-sdk-cloudtrail) >= 1 gem(aws-sdk-cloudtrail) < 2
Requires:      gem(aws-sdk-cloudwatch) >= 1 gem(aws-sdk-cloudwatch) < 2
Requires:      gem(aws-sdk-cloudwatchevents) >= 1 gem(aws-sdk-cloudwatchevents) < 2
Requires:      gem(aws-sdk-cloudwatchlogs) >= 1 gem(aws-sdk-cloudwatchlogs) < 2
Requires:      gem(aws-sdk-codeartifact) >= 1 gem(aws-sdk-codeartifact) < 2
Requires:      gem(aws-sdk-codebuild) >= 1 gem(aws-sdk-codebuild) < 2
Requires:      gem(aws-sdk-codecommit) >= 1 gem(aws-sdk-codecommit) < 2
Requires:      gem(aws-sdk-codedeploy) >= 1 gem(aws-sdk-codedeploy) < 2
Requires:      gem(aws-sdk-codeguruprofiler) >= 1 gem(aws-sdk-codeguruprofiler) < 2
Requires:      gem(aws-sdk-codegurureviewer) >= 1 gem(aws-sdk-codegurureviewer) < 2
Requires:      gem(aws-sdk-codepipeline) >= 1 gem(aws-sdk-codepipeline) < 2
Requires:      gem(aws-sdk-codestar) >= 1 gem(aws-sdk-codestar) < 2
Requires:      gem(aws-sdk-codestarnotifications) >= 1 gem(aws-sdk-codestarnotifications) < 2
Requires:      gem(aws-sdk-codestarconnections) >= 1 gem(aws-sdk-codestarconnections) < 2
Requires:      gem(aws-sdk-cognitoidentity) >= 1 gem(aws-sdk-cognitoidentity) < 2
Requires:      gem(aws-sdk-cognitoidentityprovider) >= 1 gem(aws-sdk-cognitoidentityprovider) < 2
Requires:      gem(aws-sdk-cognitosync) >= 1 gem(aws-sdk-cognitosync) < 2
Requires:      gem(aws-sdk-comprehend) >= 1 gem(aws-sdk-comprehend) < 2
Requires:      gem(aws-sdk-comprehendmedical) >= 1 gem(aws-sdk-comprehendmedical) < 2
Requires:      gem(aws-sdk-computeoptimizer) >= 1 gem(aws-sdk-computeoptimizer) < 2
Requires:      gem(aws-sdk-configservice) >= 1 gem(aws-sdk-configservice) < 2
Requires:      gem(aws-sdk-connect) >= 1 gem(aws-sdk-connect) < 2
Requires:      gem(aws-sdk-connectcontactlens) >= 1 gem(aws-sdk-connectcontactlens) < 2
Requires:      gem(aws-sdk-connectparticipant) >= 1 gem(aws-sdk-connectparticipant) < 2
Requires:      gem(aws-sdk-costexplorer) >= 1 gem(aws-sdk-costexplorer) < 2
Requires:      gem(aws-sdk-costandusagereportservice) >= 1 gem(aws-sdk-costandusagereportservice) < 2
Requires:      gem(aws-sdk-customerprofiles) >= 1 gem(aws-sdk-customerprofiles) < 2
Requires:      gem(aws-sdk-dax) >= 1 gem(aws-sdk-dax) < 2
Requires:      gem(aws-sdk-dlm) >= 1 gem(aws-sdk-dlm) < 2
Requires:      gem(aws-sdk-dataexchange) >= 1 gem(aws-sdk-dataexchange) < 2
Requires:      gem(aws-sdk-datapipeline) >= 1 gem(aws-sdk-datapipeline) < 2
Requires:      gem(aws-sdk-datasync) >= 1 gem(aws-sdk-datasync) < 2
Requires:      gem(aws-sdk-databasemigrationservice) >= 1 gem(aws-sdk-databasemigrationservice) < 2
Requires:      gem(aws-sdk-detective) >= 1 gem(aws-sdk-detective) < 2
Requires:      gem(aws-sdk-devopsguru) >= 1 gem(aws-sdk-devopsguru) < 2
Requires:      gem(aws-sdk-devicefarm) >= 1 gem(aws-sdk-devicefarm) < 2
Requires:      gem(aws-sdk-directconnect) >= 1 gem(aws-sdk-directconnect) < 2
Requires:      gem(aws-sdk-directoryservice) >= 1 gem(aws-sdk-directoryservice) < 2
Requires:      gem(aws-sdk-docdb) >= 1 gem(aws-sdk-docdb) < 2
Requires:      gem(aws-sdk-dynamodb) >= 1 gem(aws-sdk-dynamodb) < 2
Requires:      gem(aws-sdk-dynamodbstreams) >= 1 gem(aws-sdk-dynamodbstreams) < 2
Requires:      gem(aws-sdk-ebs) >= 1 gem(aws-sdk-ebs) < 2
Requires:      gem(aws-sdk-ec2) >= 1 gem(aws-sdk-ec2) < 2
Requires:      gem(aws-sdk-ec2instanceconnect) >= 1 gem(aws-sdk-ec2instanceconnect) < 2
Requires:      gem(aws-sdk-ecr) >= 1 gem(aws-sdk-ecr) < 2
Requires:      gem(aws-sdk-ecrpublic) >= 1 gem(aws-sdk-ecrpublic) < 2
Requires:      gem(aws-sdk-ecs) >= 1 gem(aws-sdk-ecs) < 2
Requires:      gem(aws-sdk-efs) >= 1 gem(aws-sdk-efs) < 2
Requires:      gem(aws-sdk-eks) >= 1 gem(aws-sdk-eks) < 2
Requires:      gem(aws-sdk-emr) >= 1 gem(aws-sdk-emr) < 2
Requires:      gem(aws-sdk-emrcontainers) >= 1 gem(aws-sdk-emrcontainers) < 2
Requires:      gem(aws-sdk-elasticache) >= 1 gem(aws-sdk-elasticache) < 2
Requires:      gem(aws-sdk-elasticbeanstalk) >= 1 gem(aws-sdk-elasticbeanstalk) < 2
Requires:      gem(aws-sdk-elasticinference) >= 1 gem(aws-sdk-elasticinference) < 2
Requires:      gem(aws-sdk-elasticloadbalancing) >= 1 gem(aws-sdk-elasticloadbalancing) < 2
Requires:      gem(aws-sdk-elasticloadbalancingv2) >= 1 gem(aws-sdk-elasticloadbalancingv2) < 2
Requires:      gem(aws-sdk-elastictranscoder) >= 1 gem(aws-sdk-elastictranscoder) < 2
Requires:      gem(aws-sdk-elasticsearchservice) >= 1 gem(aws-sdk-elasticsearchservice) < 2
Requires:      gem(aws-sdk-eventbridge) >= 1 gem(aws-sdk-eventbridge) < 2
Requires:      gem(aws-sdk-fis) >= 1 gem(aws-sdk-fis) < 2
Requires:      gem(aws-sdk-fms) >= 1 gem(aws-sdk-fms) < 2
Requires:      gem(aws-sdk-fsx) >= 1 gem(aws-sdk-fsx) < 2
Requires:      gem(aws-sdk-finspacedata) >= 1 gem(aws-sdk-finspacedata) < 2
Requires:      gem(aws-sdk-finspace) >= 1 gem(aws-sdk-finspace) < 2
Requires:      gem(aws-sdk-firehose) >= 1 gem(aws-sdk-firehose) < 2
Requires:      gem(aws-sdk-forecastqueryservice) >= 1 gem(aws-sdk-forecastqueryservice) < 2
Requires:      gem(aws-sdk-forecastservice) >= 1 gem(aws-sdk-forecastservice) < 2
Requires:      gem(aws-sdk-frauddetector) >= 1 gem(aws-sdk-frauddetector) < 2
Requires:      gem(aws-sdk-gamelift) >= 1 gem(aws-sdk-gamelift) < 2
Requires:      gem(aws-sdk-glacier) >= 1 gem(aws-sdk-glacier) < 2
Requires:      gem(aws-sdk-globalaccelerator) >= 1 gem(aws-sdk-globalaccelerator) < 2
Requires:      gem(aws-sdk-glue) >= 1 gem(aws-sdk-glue) < 2
Requires:      gem(aws-sdk-gluedatabrew) >= 1 gem(aws-sdk-gluedatabrew) < 2
Requires:      gem(aws-sdk-greengrass) >= 1 gem(aws-sdk-greengrass) < 2
Requires:      gem(aws-sdk-greengrassv2) >= 1 gem(aws-sdk-greengrassv2) < 2
Requires:      gem(aws-sdk-groundstation) >= 1 gem(aws-sdk-groundstation) < 2
Requires:      gem(aws-sdk-guardduty) >= 1 gem(aws-sdk-guardduty) < 2
Requires:      gem(aws-sdk-health) >= 1 gem(aws-sdk-health) < 2
Requires:      gem(aws-sdk-healthlake) >= 1 gem(aws-sdk-healthlake) < 2
Requires:      gem(aws-sdk-honeycode) >= 1 gem(aws-sdk-honeycode) < 2
Requires:      gem(aws-sdk-iam) >= 1 gem(aws-sdk-iam) < 2
Requires:      gem(aws-sdk-ivs) >= 1 gem(aws-sdk-ivs) < 2
Requires:      gem(aws-sdk-identitystore) >= 1 gem(aws-sdk-identitystore) < 2
Requires:      gem(aws-sdk-imagebuilder) >= 1 gem(aws-sdk-imagebuilder) < 2
Requires:      gem(aws-sdk-importexport) >= 1 gem(aws-sdk-importexport) < 2
Requires:      gem(aws-sdk-inspector) >= 1 gem(aws-sdk-inspector) < 2
Requires:      gem(aws-sdk-iot) >= 1 gem(aws-sdk-iot) < 2
Requires:      gem(aws-sdk-iot1clickdevicesservice) >= 1 gem(aws-sdk-iot1clickdevicesservice) < 2
Requires:      gem(aws-sdk-iot1clickprojects) >= 1 gem(aws-sdk-iot1clickprojects) < 2
Requires:      gem(aws-sdk-iotanalytics) >= 1 gem(aws-sdk-iotanalytics) < 2
Requires:      gem(aws-sdk-iotdataplane) >= 1 gem(aws-sdk-iotdataplane) < 2
Requires:      gem(aws-sdk-iotdeviceadvisor) >= 1 gem(aws-sdk-iotdeviceadvisor) < 2
Requires:      gem(aws-sdk-iotevents) >= 1 gem(aws-sdk-iotevents) < 2
Requires:      gem(aws-sdk-ioteventsdata) >= 1 gem(aws-sdk-ioteventsdata) < 2
Requires:      gem(aws-sdk-iotfleethub) >= 1 gem(aws-sdk-iotfleethub) < 2
Requires:      gem(aws-sdk-iotjobsdataplane) >= 1 gem(aws-sdk-iotjobsdataplane) < 2
Requires:      gem(aws-sdk-iotsecuretunneling) >= 1 gem(aws-sdk-iotsecuretunneling) < 2
Requires:      gem(aws-sdk-iotsitewise) >= 1 gem(aws-sdk-iotsitewise) < 2
Requires:      gem(aws-sdk-iotthingsgraph) >= 1 gem(aws-sdk-iotthingsgraph) < 2
Requires:      gem(aws-sdk-iotwireless) >= 1 gem(aws-sdk-iotwireless) < 2
Requires:      gem(aws-sdk-kms) >= 1 gem(aws-sdk-kms) < 2
Requires:      gem(aws-sdk-kafka) >= 1 gem(aws-sdk-kafka) < 2
Requires:      gem(aws-sdk-kendra) >= 1 gem(aws-sdk-kendra) < 2
Requires:      gem(aws-sdk-kinesis) >= 1 gem(aws-sdk-kinesis) < 2
Requires:      gem(aws-sdk-kinesisanalytics) >= 1 gem(aws-sdk-kinesisanalytics) < 2
Requires:      gem(aws-sdk-kinesisanalyticsv2) >= 1 gem(aws-sdk-kinesisanalyticsv2) < 2
Requires:      gem(aws-sdk-kinesisvideo) >= 1 gem(aws-sdk-kinesisvideo) < 2
Requires:      gem(aws-sdk-kinesisvideoarchivedmedia) >= 1 gem(aws-sdk-kinesisvideoarchivedmedia) < 2
Requires:      gem(aws-sdk-kinesisvideomedia) >= 1 gem(aws-sdk-kinesisvideomedia) < 2
Requires:      gem(aws-sdk-kinesisvideosignalingchannels) >= 1 gem(aws-sdk-kinesisvideosignalingchannels) < 2
Requires:      gem(aws-sdk-lakeformation) >= 1 gem(aws-sdk-lakeformation) < 2
Requires:      gem(aws-sdk-lambda) >= 1 gem(aws-sdk-lambda) < 2
Requires:      gem(aws-sdk-lambdapreview) >= 1 gem(aws-sdk-lambdapreview) < 2
Requires:      gem(aws-sdk-lex) >= 1 gem(aws-sdk-lex) < 2
Requires:      gem(aws-sdk-lexmodelbuildingservice) >= 1 gem(aws-sdk-lexmodelbuildingservice) < 2
Requires:      gem(aws-sdk-lexmodelsv2) >= 1 gem(aws-sdk-lexmodelsv2) < 2
Requires:      gem(aws-sdk-lexruntimev2) >= 1 gem(aws-sdk-lexruntimev2) < 2
Requires:      gem(aws-sdk-licensemanager) >= 1 gem(aws-sdk-licensemanager) < 2
Requires:      gem(aws-sdk-lightsail) >= 1 gem(aws-sdk-lightsail) < 2
Requires:      gem(aws-sdk-locationservice) >= 1 gem(aws-sdk-locationservice) < 2
Requires:      gem(aws-sdk-lookoutequipment) >= 1 gem(aws-sdk-lookoutequipment) < 2
Requires:      gem(aws-sdk-lookoutmetrics) >= 1 gem(aws-sdk-lookoutmetrics) < 2
Requires:      gem(aws-sdk-lookoutforvision) >= 1 gem(aws-sdk-lookoutforvision) < 2
Requires:      gem(aws-sdk-mq) >= 1 gem(aws-sdk-mq) < 2
Requires:      gem(aws-sdk-mturk) >= 1 gem(aws-sdk-mturk) < 2
Requires:      gem(aws-sdk-mwaa) >= 1 gem(aws-sdk-mwaa) < 2
Requires:      gem(aws-sdk-machinelearning) >= 1 gem(aws-sdk-machinelearning) < 2
Requires:      gem(aws-sdk-macie) >= 1 gem(aws-sdk-macie) < 2
Requires:      gem(aws-sdk-macie2) >= 1 gem(aws-sdk-macie2) < 2
Requires:      gem(aws-sdk-managedblockchain) >= 1 gem(aws-sdk-managedblockchain) < 2
Requires:      gem(aws-sdk-marketplacecatalog) >= 1 gem(aws-sdk-marketplacecatalog) < 2
Requires:      gem(aws-sdk-marketplacecommerceanalytics) >= 1 gem(aws-sdk-marketplacecommerceanalytics) < 2
Requires:      gem(aws-sdk-marketplaceentitlementservice) >= 1 gem(aws-sdk-marketplaceentitlementservice) < 2
Requires:      gem(aws-sdk-marketplacemetering) >= 1 gem(aws-sdk-marketplacemetering) < 2
Requires:      gem(aws-sdk-mediaconnect) >= 1 gem(aws-sdk-mediaconnect) < 2
Requires:      gem(aws-sdk-mediaconvert) >= 1 gem(aws-sdk-mediaconvert) < 2
Requires:      gem(aws-sdk-medialive) >= 1 gem(aws-sdk-medialive) < 2
Requires:      gem(aws-sdk-mediapackage) >= 1 gem(aws-sdk-mediapackage) < 2
Requires:      gem(aws-sdk-mediapackagevod) >= 1 gem(aws-sdk-mediapackagevod) < 2
Requires:      gem(aws-sdk-mediastore) >= 1 gem(aws-sdk-mediastore) < 2
Requires:      gem(aws-sdk-mediastoredata) >= 1 gem(aws-sdk-mediastoredata) < 2
Requires:      gem(aws-sdk-mediatailor) >= 1 gem(aws-sdk-mediatailor) < 2
Requires:      gem(aws-sdk-mgn) >= 1 gem(aws-sdk-mgn) < 2
Requires:      gem(aws-sdk-migrationhub) >= 1 gem(aws-sdk-migrationhub) < 2
Requires:      gem(aws-sdk-migrationhubconfig) >= 1 gem(aws-sdk-migrationhubconfig) < 2
Requires:      gem(aws-sdk-mobile) >= 1 gem(aws-sdk-mobile) < 2
Requires:      gem(aws-sdk-neptune) >= 1 gem(aws-sdk-neptune) < 2
Requires:      gem(aws-sdk-networkfirewall) >= 1 gem(aws-sdk-networkfirewall) < 2
Requires:      gem(aws-sdk-networkmanager) >= 1 gem(aws-sdk-networkmanager) < 2
Requires:      gem(aws-sdk-nimblestudio) >= 1 gem(aws-sdk-nimblestudio) < 2
Requires:      gem(aws-sdk-opsworks) >= 1 gem(aws-sdk-opsworks) < 2
Requires:      gem(aws-sdk-opsworkscm) >= 1 gem(aws-sdk-opsworkscm) < 2
Requires:      gem(aws-sdk-organizations) >= 1 gem(aws-sdk-organizations) < 2
Requires:      gem(aws-sdk-outposts) >= 1 gem(aws-sdk-outposts) < 2
Requires:      gem(aws-sdk-pi) >= 1 gem(aws-sdk-pi) < 2
Requires:      gem(aws-sdk-personalize) >= 1 gem(aws-sdk-personalize) < 2
Requires:      gem(aws-sdk-personalizeevents) >= 1 gem(aws-sdk-personalizeevents) < 2
Requires:      gem(aws-sdk-personalizeruntime) >= 1 gem(aws-sdk-personalizeruntime) < 2
Requires:      gem(aws-sdk-pinpoint) >= 1 gem(aws-sdk-pinpoint) < 2
Requires:      gem(aws-sdk-pinpointemail) >= 1 gem(aws-sdk-pinpointemail) < 2
Requires:      gem(aws-sdk-pinpointsmsvoice) >= 1 gem(aws-sdk-pinpointsmsvoice) < 2
Requires:      gem(aws-sdk-polly) >= 1 gem(aws-sdk-polly) < 2
Requires:      gem(aws-sdk-pricing) >= 1 gem(aws-sdk-pricing) < 2
Requires:      gem(aws-sdk-prometheusservice) >= 1 gem(aws-sdk-prometheusservice) < 2
Requires:      gem(aws-sdk-qldb) >= 1 gem(aws-sdk-qldb) < 2
Requires:      gem(aws-sdk-qldbsession) >= 1 gem(aws-sdk-qldbsession) < 2
Requires:      gem(aws-sdk-quicksight) >= 1 gem(aws-sdk-quicksight) < 2
Requires:      gem(aws-sdk-ram) >= 1 gem(aws-sdk-ram) < 2
Requires:      gem(aws-sdk-rds) >= 1 gem(aws-sdk-rds) < 2
Requires:      gem(aws-sdk-rdsdataservice) >= 1 gem(aws-sdk-rdsdataservice) < 2
Requires:      gem(aws-sdk-redshift) >= 1 gem(aws-sdk-redshift) < 2
Requires:      gem(aws-sdk-redshiftdataapiservice) >= 1 gem(aws-sdk-redshiftdataapiservice) < 2
Requires:      gem(aws-sdk-rekognition) >= 1 gem(aws-sdk-rekognition) < 2
Requires:      gem(aws-sdk-resourcegroups) >= 1 gem(aws-sdk-resourcegroups) < 2
Requires:      gem(aws-sdk-resourcegroupstaggingapi) >= 1 gem(aws-sdk-resourcegroupstaggingapi) < 2
Requires:      gem(aws-sdk-robomaker) >= 1 gem(aws-sdk-robomaker) < 2
Requires:      gem(aws-sdk-route53) >= 1 gem(aws-sdk-route53) < 2
Requires:      gem(aws-sdk-route53domains) >= 1 gem(aws-sdk-route53domains) < 2
Requires:      gem(aws-sdk-route53resolver) >= 1 gem(aws-sdk-route53resolver) < 2
Requires:      gem(aws-sdk-s3) >= 1 gem(aws-sdk-s3) < 2
Requires:      gem(aws-sdk-s3control) >= 1 gem(aws-sdk-s3control) < 2
Requires:      gem(aws-sdk-s3outposts) >= 1 gem(aws-sdk-s3outposts) < 2
Requires:      gem(aws-sdk-ses) >= 1 gem(aws-sdk-ses) < 2
Requires:      gem(aws-sdk-sesv2) >= 1 gem(aws-sdk-sesv2) < 2
Requires:      gem(aws-sdk-sms) >= 1 gem(aws-sdk-sms) < 2
Requires:      gem(aws-sdk-sns) >= 1 gem(aws-sdk-sns) < 2
Requires:      gem(aws-sdk-sqs) >= 1 gem(aws-sdk-sqs) < 2
Requires:      gem(aws-sdk-ssm) >= 1 gem(aws-sdk-ssm) < 2
Requires:      gem(aws-sdk-ssmcontacts) >= 1 gem(aws-sdk-ssmcontacts) < 2
Requires:      gem(aws-sdk-ssmincidents) >= 1 gem(aws-sdk-ssmincidents) < 2
Requires:      gem(aws-sdk-ssoadmin) >= 1 gem(aws-sdk-ssoadmin) < 2
Requires:      gem(aws-sdk-ssooidc) >= 1 gem(aws-sdk-ssooidc) < 2
Requires:      gem(aws-sdk-swf) >= 1 gem(aws-sdk-swf) < 2
Requires:      gem(aws-sdk-sagemaker) >= 1 gem(aws-sdk-sagemaker) < 2
Requires:      gem(aws-sdk-sagemakerfeaturestoreruntime) >= 1 gem(aws-sdk-sagemakerfeaturestoreruntime) < 2
Requires:      gem(aws-sdk-sagemakerruntime) >= 1 gem(aws-sdk-sagemakerruntime) < 2
Requires:      gem(aws-sdk-sagemakeredgemanager) >= 1 gem(aws-sdk-sagemakeredgemanager) < 2
Requires:      gem(aws-sdk-savingsplans) >= 1 gem(aws-sdk-savingsplans) < 2
Requires:      gem(aws-sdk-schemas) >= 1 gem(aws-sdk-schemas) < 2
Requires:      gem(aws-sdk-secretsmanager) >= 1 gem(aws-sdk-secretsmanager) < 2
Requires:      gem(aws-sdk-securityhub) >= 1 gem(aws-sdk-securityhub) < 2
Requires:      gem(aws-sdk-serverlessapplicationrepository) >= 1 gem(aws-sdk-serverlessapplicationrepository) < 2
Requires:      gem(aws-sdk-servicecatalog) >= 1 gem(aws-sdk-servicecatalog) < 2
Requires:      gem(aws-sdk-servicediscovery) >= 1 gem(aws-sdk-servicediscovery) < 2
Requires:      gem(aws-sdk-servicequotas) >= 1 gem(aws-sdk-servicequotas) < 2
Requires:      gem(aws-sdk-shield) >= 1 gem(aws-sdk-shield) < 2
Requires:      gem(aws-sdk-signer) >= 1 gem(aws-sdk-signer) < 2
Requires:      gem(aws-sdk-simpledb) >= 1 gem(aws-sdk-simpledb) < 2
Requires:      gem(aws-sdk-snowball) >= 1 gem(aws-sdk-snowball) < 2
Requires:      gem(aws-sdk-states) >= 1 gem(aws-sdk-states) < 2
Requires:      gem(aws-sdk-storagegateway) >= 1 gem(aws-sdk-storagegateway) < 2
Requires:      gem(aws-sdk-support) >= 1 gem(aws-sdk-support) < 2
Requires:      gem(aws-sdk-synthetics) >= 1 gem(aws-sdk-synthetics) < 2
Requires:      gem(aws-sdk-textract) >= 1 gem(aws-sdk-textract) < 2
Requires:      gem(aws-sdk-timestreamquery) >= 1 gem(aws-sdk-timestreamquery) < 2
Requires:      gem(aws-sdk-timestreamwrite) >= 1 gem(aws-sdk-timestreamwrite) < 2
Requires:      gem(aws-sdk-transcribeservice) >= 1 gem(aws-sdk-transcribeservice) < 2
Requires:      gem(aws-sdk-transcribestreamingservice) >= 1 gem(aws-sdk-transcribestreamingservice) < 2
Requires:      gem(aws-sdk-transfer) >= 1 gem(aws-sdk-transfer) < 2
Requires:      gem(aws-sdk-translate) >= 1 gem(aws-sdk-translate) < 2
Requires:      gem(aws-sdk-waf) >= 1 gem(aws-sdk-waf) < 2
Requires:      gem(aws-sdk-wafregional) >= 1 gem(aws-sdk-wafregional) < 2
Requires:      gem(aws-sdk-wafv2) >= 1 gem(aws-sdk-wafv2) < 2
Requires:      gem(aws-sdk-wellarchitected) >= 1 gem(aws-sdk-wellarchitected) < 2
Requires:      gem(aws-sdk-workdocs) >= 1 gem(aws-sdk-workdocs) < 2
Requires:      gem(aws-sdk-worklink) >= 1 gem(aws-sdk-worklink) < 2
Requires:      gem(aws-sdk-workmail) >= 1 gem(aws-sdk-workmail) < 2
Requires:      gem(aws-sdk-workmailmessageflow) >= 1 gem(aws-sdk-workmailmessageflow) < 2
Requires:      gem(aws-sdk-workspaces) >= 1 gem(aws-sdk-workspaces) < 2
Requires:      gem(aws-sdk-xray) >= 1 gem(aws-sdk-xray) < 2
Provides:      gem(aws-sdk-resources) = 3.104.0

%description   -n gem-aws-sdk-resources
Provides resource oriented interfaces and other higher-level abstractions for
many AWS services. This gem is part of the official AWS SDK for Ruby.


%package       -n aws-v3-rb
Version:       3.104.0
Release:       alt1
Summary:       AWS SDK for Ruby - Resources executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета aws-sdk-resources
Group:         Other
BuildArch:     noarch

Requires:      gem(aws-sdk-resources) = 3.104.0

%description   -n aws-v3-rb
AWS SDK for Ruby - Resources executable(s).

Provides resource oriented interfaces and other higher-level abstractions for
many AWS services. This gem is part of the official AWS SDK for Ruby.

%description   -n aws-v3-rb -l ru_RU.UTF-8
Исполнямка для самоцвета aws-sdk-resources.


%package       -n gem-aws-sdk-resources-doc
Version:       3.104.0
Release:       alt1
Summary:       AWS SDK for Ruby - Resources documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-resources
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-resources) = 3.104.0

%description   -n gem-aws-sdk-resources-doc
AWS SDK for Ruby - Resources documentation files.

Provides resource oriented interfaces and other higher-level abstractions for
many AWS services. This gem is part of the official AWS SDK for Ruby.

%description   -n gem-aws-sdk-resources-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-resources.


%package       -n gem-aws-sdk-resources-devel
Version:       3.104.0
Release:       alt1
Summary:       AWS SDK for Ruby - Resources development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-resources
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-resources) = 3.104.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-resources-devel
AWS SDK for Ruby - Resources development package.

Provides resource oriented interfaces and other higher-level abstractions for
many AWS services. This gem is part of the official AWS SDK for Ruby.

%description   -n gem-aws-sdk-resources-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-resources.


%package       -n gem-aws-sdk-sts
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - STS
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.110.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-sts) = 1.2.0

%description   -n gem-aws-sdk-sts
Official AWS Ruby gem for AWS Security Token Service (STS). STS is included as
part of aws-sdk-core - this gem is an alias for loading aws-sdk-core.


%package       -n gem-aws-sdk-sts-doc
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - STS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sts
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sts) = 1.2.0

%description   -n gem-aws-sdk-sts-doc
AWS SDK for Ruby - STS documentation files.

Official AWS Ruby gem for AWS Security Token Service (STS). STS is included as
part of aws-sdk-core - this gem is an alias for loading aws-sdk-core.

%description   -n gem-aws-sdk-sts-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sts.


%package       -n gem-aws-sdk-sts-devel
Version:       1.2.0
Release:       alt1
Summary:       AWS SDK for Ruby - STS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sts
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sts) = 1.2.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-sts-devel
AWS SDK for Ruby - STS development package.

Official AWS Ruby gem for AWS Security Token Service (STS). STS is included as
part of aws-sdk-core - this gem is an alias for loading aws-sdk-core.

%description   -n gem-aws-sdk-sts-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sts.


%package       -n gem-aws-sdk-elastictranscoder
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Elastic Transcoder
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-elastictranscoder) = 1.29.0

%description   -n gem-aws-sdk-elastictranscoder
Official AWS Ruby gem for Amazon Elastic Transcoder. This gem is part of the AWS
SDK for Ruby.


%package       -n gem-aws-sdk-elastictranscoder-doc
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Elastic Transcoder documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-elastictranscoder
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-elastictranscoder) = 1.29.0

%description   -n gem-aws-sdk-elastictranscoder-doc
AWS SDK for Ruby - Amazon Elastic Transcoder documentation files.

Official AWS Ruby gem for Amazon Elastic Transcoder. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-elastictranscoder-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-elastictranscoder.


%package       -n gem-aws-sdk-elastictranscoder-devel
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Elastic Transcoder development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-elastictranscoder
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-elastictranscoder) = 1.29.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-elastictranscoder-devel
AWS SDK for Ruby - Amazon Elastic Transcoder development package.

Official AWS Ruby gem for Amazon Elastic Transcoder. This gem is part of the AWS
SDK for Ruby.

%description   -n gem-aws-sdk-elastictranscoder-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-elastictranscoder.


%package       -n gem-aws-sdk-applicationcostprofiler
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Application Cost Profiler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-applicationcostprofiler) = 1.0.0

%description   -n gem-aws-sdk-applicationcostprofiler
Official AWS Ruby gem for AWS Application Cost Profiler. This gem is part of the
AWS SDK for Ruby.


%package       -n gem-aws-sdk-applicationcostprofiler-doc
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Application Cost Profiler documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-applicationcostprofiler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationcostprofiler) = 1.0.0

%description   -n gem-aws-sdk-applicationcostprofiler-doc
AWS SDK for Ruby - AWS Application Cost Profiler documentation files.

Official AWS Ruby gem for AWS Application Cost Profiler. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-applicationcostprofiler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-applicationcostprofiler.


%package       -n gem-aws-sdk-applicationcostprofiler-devel
Version:       1.0.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Application Cost Profiler development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-applicationcostprofiler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-applicationcostprofiler) = 1.0.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-applicationcostprofiler-devel
AWS SDK for Ruby - AWS Application Cost Profiler development package.

Official AWS Ruby gem for AWS Application Cost Profiler. This gem is part of the
AWS SDK for Ruby.

%description   -n gem-aws-sdk-applicationcostprofiler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-applicationcostprofiler.


%package       -n gem-aws-sdk-connect
Version:       1.44.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Connect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-connect) = 1.44.0

%description   -n gem-aws-sdk-connect
Official AWS Ruby gem for Amazon Connect Service (Amazon Connect). This gem is
part of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-connect-doc
Version:       1.44.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Connect documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-connect
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-connect) = 1.44.0

%description   -n gem-aws-sdk-connect-doc
AWS SDK for Ruby - Amazon Connect documentation files.

Official AWS Ruby gem for Amazon Connect Service (Amazon Connect). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-connect-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-connect.


%package       -n gem-aws-sdk-connect-devel
Version:       1.44.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Connect development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-connect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-connect) = 1.44.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-connect-devel
AWS SDK for Ruby - Amazon Connect development package.

Official AWS Ruby gem for Amazon Connect Service (Amazon Connect). This gem is
part of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-connect-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-connect.


%package       -n gem-aws-sdk-groundstation
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Ground Station
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-groundstation) = 1.18.0

%description   -n gem-aws-sdk-groundstation
Official AWS Ruby gem for AWS Ground Station. This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-groundstation-doc
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Ground Station documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-groundstation
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-groundstation) = 1.18.0

%description   -n gem-aws-sdk-groundstation-doc
AWS SDK for Ruby - AWS Ground Station documentation files.

Official AWS Ruby gem for AWS Ground Station. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-groundstation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-groundstation.


%package       -n gem-aws-sdk-groundstation-devel
Version:       1.18.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Ground Station development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-groundstation
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-groundstation) = 1.18.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-groundstation-devel
AWS SDK for Ruby - AWS Ground Station development package.

Official AWS Ruby gem for AWS Ground Station. This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-groundstation-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-groundstation.


%package       -n gem-aws-sdk-greengrass
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Greengrass
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-greengrass) = 1.40.0

%description   -n gem-aws-sdk-greengrass
Official AWS Ruby gem for AWS Greengrass. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-greengrass-doc
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Greengrass documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-greengrass
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-greengrass) = 1.40.0

%description   -n gem-aws-sdk-greengrass-doc
AWS SDK for Ruby - AWS Greengrass documentation files.

Official AWS Ruby gem for AWS Greengrass. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-greengrass-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-greengrass.


%package       -n gem-aws-sdk-greengrass-devel
Version:       1.40.0
Release:       alt1
Summary:       AWS SDK for Ruby - AWS Greengrass development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-greengrass
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-greengrass) = 1.40.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-greengrass-devel
AWS SDK for Ruby - AWS Greengrass development package.

Official AWS Ruby gem for AWS Greengrass. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-greengrass-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-greengrass.


%package       -n gem-aws-sdk-sagemaker
Version:       1.88.0
Release:       alt1
Summary:       AWS SDK for Ruby - SageMaker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-sagemaker) = 1.88.0

%description   -n gem-aws-sdk-sagemaker
Official AWS Ruby gem for Amazon SageMaker Service (SageMaker). This gem is part
of the AWS SDK for Ruby.


%package       -n gem-aws-sdk-sagemaker-doc
Version:       1.88.0
Release:       alt1
Summary:       AWS SDK for Ruby - SageMaker documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-sagemaker
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemaker) = 1.88.0

%description   -n gem-aws-sdk-sagemaker-doc
AWS SDK for Ruby - SageMaker documentation files.

Official AWS Ruby gem for Amazon SageMaker Service (SageMaker). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sagemaker-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-sagemaker.


%package       -n gem-aws-sdk-sagemaker-devel
Version:       1.88.0
Release:       alt1
Summary:       AWS SDK for Ruby - SageMaker development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-sagemaker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-sagemaker) = 1.88.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-sagemaker-devel
AWS SDK for Ruby - SageMaker development package.

Official AWS Ruby gem for Amazon SageMaker Service (SageMaker). This gem is part
of the AWS SDK for Ruby.

%description   -n gem-aws-sdk-sagemaker-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-sagemaker.


%package       -n gem-aws-sdk-amplify
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amplify
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-amplify) = 1.29.0

%description   -n gem-aws-sdk-amplify
Official AWS Ruby gem for AWS Amplify (Amplify). This gem is part of the AWS SDK
for Ruby.


%package       -n gem-aws-sdk-amplify-doc
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amplify documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-amplify
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-amplify) = 1.29.0

%description   -n gem-aws-sdk-amplify-doc
AWS SDK for Ruby - Amplify documentation files.

Official AWS Ruby gem for AWS Amplify (Amplify). This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-amplify-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-amplify.


%package       -n gem-aws-sdk-amplify-devel
Version:       1.29.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amplify development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-amplify
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-amplify) = 1.29.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-amplify-devel
AWS SDK for Ruby - Amplify development package.

Official AWS Ruby gem for AWS Amplify (Amplify). This gem is part of the AWS SDK
for Ruby.

%description   -n gem-aws-sdk-amplify-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-amplify.


%package       -n gem-aws-sdk-pinpoint
Version:       1.53.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Pinpoint
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-core) >= 3.112.0 gem(aws-sdk-core) < 4
Requires:      gem(aws-sigv4) >= 1.1 gem(aws-sigv4) < 2
Provides:      gem(aws-sdk-pinpoint) = 1.53.0

%description   -n gem-aws-sdk-pinpoint
Official AWS Ruby gem for Amazon Pinpoint. This gem is part of the AWS SDK for
Ruby.


%package       -n gem-aws-sdk-pinpoint-doc
Version:       1.53.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Pinpoint documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-sdk-pinpoint
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-sdk-pinpoint) = 1.53.0

%description   -n gem-aws-sdk-pinpoint-doc
AWS SDK for Ruby - Amazon Pinpoint documentation files.

Official AWS Ruby gem for Amazon Pinpoint. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-pinpoint-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-sdk-pinpoint.


%package       -n gem-aws-sdk-pinpoint-devel
Version:       1.53.0
Release:       alt1
Summary:       AWS SDK for Ruby - Amazon Pinpoint development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-sdk-pinpoint
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-sdk-pinpoint) = 1.53.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(yard) >= 0.9
Requires:      gem(oga) >= 3

%description   -n gem-aws-sdk-pinpoint-devel
AWS SDK for Ruby - Amazon Pinpoint development package.

Official AWS Ruby gem for Amazon Pinpoint. This gem is part of the AWS SDK for
Ruby.

%description   -n gem-aws-sdk-pinpoint-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-sdk-pinpoint.


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

%files         -n gem-aws-sdk-code-generator
%doc README.md
%ruby_gemspecdir/aws-sdk-code-generator-0.2.3.pre.gemspec
%ruby_gemslibdir/aws-sdk-code-generator-0.2.3.pre

%files         -n gem-aws-sdk-code-generator-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-code-generator-0.2.3.pre

%files         -n gem-aws-sdk-code-generator-devel
%doc README.md

%files         -n gem-aws-sdk-s3outposts
%doc README.md
%ruby_gemspecdir/aws-sdk-s3outposts-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-s3outposts-1.2.0

%files         -n gem-aws-sdk-s3outposts-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-s3outposts-1.2.0

%files         -n gem-aws-sdk-s3outposts-devel

%files         -n gem-aws-sdk-elasticloadbalancing
%doc README.md
%ruby_gemspecdir/aws-sdk-elasticloadbalancing-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-elasticloadbalancing-1.31.0

%files         -n gem-aws-sdk-elasticloadbalancing-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-elasticloadbalancing-1.31.0

%files         -n gem-aws-sdk-elasticloadbalancing-devel

%files         -n gem-aws-sdk-swf
%doc README.md
%ruby_gemspecdir/aws-sdk-swf-1.27.0.gemspec
%ruby_gemslibdir/aws-sdk-swf-1.27.0

%files         -n gem-aws-sdk-swf-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-swf-1.27.0

%files         -n gem-aws-sdk-swf-devel

%files         -n gem-aws-sdk-alexaforbusiness
%doc README.md
%ruby_gemspecdir/aws-sdk-alexaforbusiness-1.47.0.gemspec
%ruby_gemslibdir/aws-sdk-alexaforbusiness-1.47.0

%files         -n gem-aws-sdk-alexaforbusiness-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-alexaforbusiness-1.47.0

%files         -n gem-aws-sdk-alexaforbusiness-devel

%files         -n gem-aws-sdk-ecrpublic
%doc README.md
%ruby_gemspecdir/aws-sdk-ecrpublic-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-ecrpublic-1.3.0

%files         -n gem-aws-sdk-ecrpublic-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ecrpublic-1.3.0

%files         -n gem-aws-sdk-ecrpublic-devel

%files         -n gem-aws-sdk-route53resolver
%doc README.md
%ruby_gemspecdir/aws-sdk-route53resolver-1.26.0.gemspec
%ruby_gemslibdir/aws-sdk-route53resolver-1.26.0

%files         -n gem-aws-sdk-route53resolver-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-route53resolver-1.26.0

%files         -n gem-aws-sdk-route53resolver-devel

%files         -n gem-aws-sdk-ssmcontacts
%doc README.md
%ruby_gemspecdir/aws-sdk-ssmcontacts-1.0.0.gemspec
%ruby_gemslibdir/aws-sdk-ssmcontacts-1.0.0

%files         -n gem-aws-sdk-ssmcontacts-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ssmcontacts-1.0.0

%files         -n gem-aws-sdk-ssmcontacts-devel

%files         -n gem-aws-sdk-eventbridge
%doc README.md
%ruby_gemspecdir/aws-sdk-eventbridge-1.24.0.gemspec
%ruby_gemslibdir/aws-sdk-eventbridge-1.24.0

%files         -n gem-aws-sdk-eventbridge-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-eventbridge-1.24.0

%files         -n gem-aws-sdk-eventbridge-devel

%files         -n gem-aws-sdk-wellarchitected
%doc README.md
%ruby_gemspecdir/aws-sdk-wellarchitected-1.4.0.gemspec
%ruby_gemslibdir/aws-sdk-wellarchitected-1.4.0

%files         -n gem-aws-sdk-wellarchitected-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-wellarchitected-1.4.0

%files         -n gem-aws-sdk-wellarchitected-devel

%files         -n gem-aws-sdk-appregistry
%doc README.md
%ruby_gemspecdir/aws-sdk-appregistry-1.5.0.gemspec
%ruby_gemslibdir/aws-sdk-appregistry-1.5.0

%files         -n gem-aws-sdk-appregistry-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-appregistry-1.5.0

%files         -n gem-aws-sdk-appregistry-devel

%files         -n gem-aws-sdk-networkfirewall
%doc README.md
%ruby_gemspecdir/aws-sdk-networkfirewall-1.4.0.gemspec
%ruby_gemslibdir/aws-sdk-networkfirewall-1.4.0

%files         -n gem-aws-sdk-networkfirewall-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-networkfirewall-1.4.0

%files         -n gem-aws-sdk-networkfirewall-devel

%files         -n gem-aws-sdk-codebuild
%doc README.md
%ruby_gemspecdir/aws-sdk-codebuild-1.72.0.gemspec
%ruby_gemslibdir/aws-sdk-codebuild-1.72.0

%files         -n gem-aws-sdk-codebuild-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-codebuild-1.72.0

%files         -n gem-aws-sdk-codebuild-devel

%files         -n gem-aws-sdk-marketplacecommerceanalytics
%doc README.md
%ruby_gemspecdir/aws-sdk-marketplacecommerceanalytics-1.32.0.gemspec
%ruby_gemslibdir/aws-sdk-marketplacecommerceanalytics-1.32.0

%files         -n gem-aws-sdk-marketplacecommerceanalytics-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-marketplacecommerceanalytics-1.32.0

%files         -n gem-aws-sdk-marketplacecommerceanalytics-devel

%files         -n gem-aws-sdk-personalize
%doc README.md
%ruby_gemspecdir/aws-sdk-personalize-1.27.0.gemspec
%ruby_gemslibdir/aws-sdk-personalize-1.27.0

%files         -n gem-aws-sdk-personalize-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-personalize-1.27.0

%files         -n gem-aws-sdk-personalize-devel

%files         -n gem-aws-sdk-lookoutequipment
%doc README.md
%ruby_gemspecdir/aws-sdk-lookoutequipment-1.0.0.gemspec
%ruby_gemslibdir/aws-sdk-lookoutequipment-1.0.0

%files         -n gem-aws-sdk-lookoutequipment-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-lookoutequipment-1.0.0

%files         -n gem-aws-sdk-lookoutequipment-devel

%files         -n gem-aws-sdk-rdsdataservice
%doc README.md
%ruby_gemspecdir/aws-sdk-rdsdataservice-1.25.0.gemspec
%ruby_gemslibdir/aws-sdk-rdsdataservice-1.25.0

%files         -n gem-aws-sdk-rdsdataservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-rdsdataservice-1.25.0

%files         -n gem-aws-sdk-rdsdataservice-devel

%files         -n gem-aws-sdk-accessanalyzer
%doc README.md
%ruby_gemspecdir/aws-sdk-accessanalyzer-1.19.0.gemspec
%ruby_gemslibdir/aws-sdk-accessanalyzer-1.19.0

%files         -n gem-aws-sdk-accessanalyzer-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-accessanalyzer-1.19.0

%files         -n gem-aws-sdk-accessanalyzer-devel

%files         -n gem-aws-sdk-codestarnotifications
%doc README.md
%ruby_gemspecdir/aws-sdk-codestarnotifications-1.10.0.gemspec
%ruby_gemslibdir/aws-sdk-codestarnotifications-1.10.0

%files         -n gem-aws-sdk-codestarnotifications-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-codestarnotifications-1.10.0

%files         -n gem-aws-sdk-codestarnotifications-devel

%files         -n gem-aws-sdk-fis
%doc README.md
%ruby_gemspecdir/aws-sdk-fis-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-fis-1.1.0

%files         -n gem-aws-sdk-fis-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-fis-1.1.0

%files         -n gem-aws-sdk-fis-devel

%files         -n gem-aws-sdk-firehose
%doc README.md
%ruby_gemspecdir/aws-sdk-firehose-1.37.0.gemspec
%ruby_gemslibdir/aws-sdk-firehose-1.37.0

%files         -n gem-aws-sdk-firehose-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-firehose-1.37.0

%files         -n gem-aws-sdk-firehose-devel

%files         -n gem-aws-sdk-pinpointsmsvoice
%doc README.md
%ruby_gemspecdir/aws-sdk-pinpointsmsvoice-1.23.0.gemspec
%ruby_gemslibdir/aws-sdk-pinpointsmsvoice-1.23.0

%files         -n gem-aws-sdk-pinpointsmsvoice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-pinpointsmsvoice-1.23.0

%files         -n gem-aws-sdk-pinpointsmsvoice-devel

%files         -n gem-aws-sdk-codecommit
%doc README.md
%ruby_gemspecdir/aws-sdk-codecommit-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-codecommit-1.42.0

%files         -n gem-aws-sdk-codecommit-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-codecommit-1.42.0

%files         -n gem-aws-sdk-codecommit-devel

%files         -n gem-aws-sdk-lookoutmetrics
%doc README.md
%ruby_gemspecdir/aws-sdk-lookoutmetrics-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-lookoutmetrics-1.3.0

%files         -n gem-aws-sdk-lookoutmetrics-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-lookoutmetrics-1.3.0

%files         -n gem-aws-sdk-lookoutmetrics-devel

%files         -n gem-aws-sdk-customerprofiles
%doc README.md
%ruby_gemspecdir/aws-sdk-customerprofiles-1.7.0.gemspec
%ruby_gemslibdir/aws-sdk-customerprofiles-1.7.0

%files         -n gem-aws-sdk-customerprofiles-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-customerprofiles-1.7.0

%files         -n gem-aws-sdk-customerprofiles-devel

%files         -n gem-aws-sdk-ssoadmin
%doc README.md
%ruby_gemspecdir/aws-sdk-ssoadmin-1.7.0.gemspec
%ruby_gemslibdir/aws-sdk-ssoadmin-1.7.0

%files         -n gem-aws-sdk-ssoadmin-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ssoadmin-1.7.0

%files         -n gem-aws-sdk-ssoadmin-devel

%files         -n gem-aws-sdk-wafregional
%doc README.md
%ruby_gemspecdir/aws-sdk-wafregional-1.39.0.gemspec
%ruby_gemslibdir/aws-sdk-wafregional-1.39.0

%files         -n gem-aws-sdk-wafregional-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-wafregional-1.39.0

%files         -n gem-aws-sdk-wafregional-devel

%files         -n gem-aws-sdk-mediaconvert
%doc README.md
%ruby_gemspecdir/aws-sdk-mediaconvert-1.67.0.gemspec
%ruby_gemslibdir/aws-sdk-mediaconvert-1.67.0

%files         -n gem-aws-sdk-mediaconvert-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-mediaconvert-1.67.0

%files         -n gem-aws-sdk-mediaconvert-devel

%files         -n gem-aws-sdk-finspace
%doc README.md
%ruby_gemspecdir/aws-sdk-finspace-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-finspace-1.2.0

%files         -n gem-aws-sdk-finspace-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-finspace-1.2.0

%files         -n gem-aws-sdk-finspace-devel

%files         -n gem-aws-sdk-iot
%doc README.md
%ruby_gemspecdir/aws-sdk-iot-1.69.0.gemspec
%ruby_gemslibdir/aws-sdk-iot-1.69.0

%files         -n gem-aws-sdk-iot-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-iot-1.69.0

%files         -n gem-aws-sdk-iot-devel

%files         -n gem-aws-sdk-importexport
%doc README.md
%ruby_gemspecdir/aws-sdk-importexport-1.26.0.gemspec
%ruby_gemslibdir/aws-sdk-importexport-1.26.0

%files         -n gem-aws-sdk-importexport-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-importexport-1.26.0

%files         -n gem-aws-sdk-importexport-devel

%files         -n gem-aws-sdk-codestar
%doc README.md
%ruby_gemspecdir/aws-sdk-codestar-1.29.0.gemspec
%ruby_gemslibdir/aws-sdk-codestar-1.29.0

%files         -n gem-aws-sdk-codestar-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-codestar-1.29.0

%files         -n gem-aws-sdk-codestar-devel

%files         -n gem-aws-sdk-iotfleethub
%doc README.md
%ruby_gemspecdir/aws-sdk-iotfleethub-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-iotfleethub-1.2.0

%files         -n gem-aws-sdk-iotfleethub-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-iotfleethub-1.2.0

%files         -n gem-aws-sdk-iotfleethub-devel

%files         -n gem-aws-sdk-sso
%doc README.md
%ruby_gemspecdir/aws-sdk-sso-1.7.1.gemspec
%ruby_gemslibdir/aws-sdk-sso-1.7.1

%files         -n gem-aws-sdk-sso-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-sso-1.7.1

%files         -n gem-aws-sdk-sso-devel

%files         -n gem-aws-sdk-cloudfront
%doc README.md
%ruby_gemspecdir/aws-sdk-cloudfront-1.51.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudfront-1.51.0

%files         -n gem-aws-sdk-cloudfront-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-cloudfront-1.51.0

%files         -n gem-aws-sdk-cloudfront-devel

%files         -n gem-aws-sdk-configservice
%doc README.md
%ruby_gemspecdir/aws-sdk-configservice-1.62.0.gemspec
%ruby_gemslibdir/aws-sdk-configservice-1.62.0

%files         -n gem-aws-sdk-configservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-configservice-1.62.0

%files         -n gem-aws-sdk-configservice-devel

%files         -n gem-aws-sdk-athena
%doc README.md
%ruby_gemspecdir/aws-sdk-athena-1.37.0.gemspec
%ruby_gemslibdir/aws-sdk-athena-1.37.0

%files         -n gem-aws-sdk-athena-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-athena-1.37.0

%files         -n gem-aws-sdk-athena-devel

%files         -n gem-aws-sdk-iot1clickdevicesservice
%doc README.md
%ruby_gemspecdir/aws-sdk-iot1clickdevicesservice-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-iot1clickdevicesservice-1.28.0

%files         -n gem-aws-sdk-iot1clickdevicesservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-iot1clickdevicesservice-1.28.0

%files         -n gem-aws-sdk-iot1clickdevicesservice-devel

%files         -n gem-aws-sdk-worklink
%doc README.md
%ruby_gemspecdir/aws-sdk-worklink-1.23.0.gemspec
%ruby_gemslibdir/aws-sdk-worklink-1.23.0

%files         -n gem-aws-sdk-worklink-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-worklink-1.23.0

%files         -n gem-aws-sdk-worklink-devel

%files         -n gem-aws-sdk-snowball
%doc README.md
%ruby_gemspecdir/aws-sdk-snowball-1.38.0.gemspec
%ruby_gemslibdir/aws-sdk-snowball-1.38.0

%files         -n gem-aws-sdk-snowball-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-snowball-1.38.0

%files         -n gem-aws-sdk-snowball-devel

%files         -n gem-aws-sdk-sagemakerruntime
%doc README.md
%ruby_gemspecdir/aws-sdk-sagemakerruntime-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-sagemakerruntime-1.31.0

%files         -n gem-aws-sdk-sagemakerruntime-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-sagemakerruntime-1.31.0

%files         -n gem-aws-sdk-sagemakerruntime-devel

%files         -n gem-aws-sdk-nimblestudio
%doc README.md
%ruby_gemspecdir/aws-sdk-nimblestudio-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-nimblestudio-1.1.0

%files         -n gem-aws-sdk-nimblestudio-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-nimblestudio-1.1.0

%files         -n gem-aws-sdk-nimblestudio-devel

%files         -n gem-aws-sdk-route53domains
%doc README.md
%ruby_gemspecdir/aws-sdk-route53domains-1.30.0.gemspec
%ruby_gemslibdir/aws-sdk-route53domains-1.30.0

%files         -n gem-aws-sdk-route53domains-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-route53domains-1.30.0

%files         -n gem-aws-sdk-route53domains-devel

%files         -n gem-aws-sdk-transcribeservice
%doc README.md
%ruby_gemspecdir/aws-sdk-transcribeservice-1.55.0.gemspec
%ruby_gemslibdir/aws-sdk-transcribeservice-1.55.0

%files         -n gem-aws-sdk-transcribeservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-transcribeservice-1.55.0

%files         -n gem-aws-sdk-transcribeservice-devel

%files         -n gem-aws-sdk-databasemigrationservice
%doc README.md
%ruby_gemspecdir/aws-sdk-databasemigrationservice-1.53.0.gemspec
%ruby_gemslibdir/aws-sdk-databasemigrationservice-1.53.0

%files         -n gem-aws-sdk-databasemigrationservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-databasemigrationservice-1.53.0

%files         -n gem-aws-sdk-databasemigrationservice-devel

%files         -n gem-aws-sdk-ec2instanceconnect
%doc README.md
%ruby_gemspecdir/aws-sdk-ec2instanceconnect-1.14.0.gemspec
%ruby_gemslibdir/aws-sdk-ec2instanceconnect-1.14.0

%files         -n gem-aws-sdk-ec2instanceconnect-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ec2instanceconnect-1.14.0

%files         -n gem-aws-sdk-ec2instanceconnect-devel

%files         -n gem-aws-sdk-amplifybackend
%doc README.md
%ruby_gemspecdir/aws-sdk-amplifybackend-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-amplifybackend-1.3.0

%files         -n gem-aws-sdk-amplifybackend-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-amplifybackend-1.3.0

%files         -n gem-aws-sdk-amplifybackend-devel

%files         -n gem-aws-sdk-appsync
%doc README.md
%ruby_gemspecdir/aws-sdk-appsync-1.40.0.gemspec
%ruby_gemslibdir/aws-sdk-appsync-1.40.0

%files         -n gem-aws-sdk-appsync-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-appsync-1.40.0

%files         -n gem-aws-sdk-appsync-devel

%files         -n gem-aws-sdk-appconfig
%doc README.md
%ruby_gemspecdir/aws-sdk-appconfig-1.14.0.gemspec
%ruby_gemslibdir/aws-sdk-appconfig-1.14.0

%files         -n gem-aws-sdk-appconfig-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-appconfig-1.14.0

%files         -n gem-aws-sdk-appconfig-devel

%files         -n gem-aws-sdk-quicksight
%doc README.md
%ruby_gemspecdir/aws-sdk-quicksight-1.46.0.gemspec
%ruby_gemslibdir/aws-sdk-quicksight-1.46.0

%files         -n gem-aws-sdk-quicksight-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-quicksight-1.46.0

%files         -n gem-aws-sdk-quicksight-devel

%files         -n gem-aws-sdk-kinesisvideoarchivedmedia
%doc README.md
%ruby_gemspecdir/aws-sdk-kinesisvideoarchivedmedia-1.34.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesisvideoarchivedmedia-1.34.0

%files         -n gem-aws-sdk-kinesisvideoarchivedmedia-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-kinesisvideoarchivedmedia-1.34.0

%files         -n gem-aws-sdk-kinesisvideoarchivedmedia-devel

%files         -n gem-aws-sdk-kendra
%doc README.md
%ruby_gemspecdir/aws-sdk-kendra-1.25.0.gemspec
%ruby_gemslibdir/aws-sdk-kendra-1.25.0

%files         -n gem-aws-sdk-kendra-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-kendra-1.25.0

%files         -n gem-aws-sdk-kendra-devel

%files         -n gem-aws-sdk-sesv2
%doc README.md
%ruby_gemspecdir/aws-sdk-sesv2-1.17.0.gemspec
%ruby_gemslibdir/aws-sdk-sesv2-1.17.0

%files         -n gem-aws-sdk-sesv2-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-sesv2-1.17.0

%files         -n gem-aws-sdk-sesv2-devel

%files         -n gem-aws-sdk-xray
%doc README.md
%ruby_gemspecdir/aws-sdk-xray-1.37.0.gemspec
%ruby_gemslibdir/aws-sdk-xray-1.37.0

%files         -n gem-aws-sdk-xray-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-xray-1.37.0

%files         -n gem-aws-sdk-xray-devel

%files         -n gem-aws-sdk-docdb
%doc README.md
%ruby_gemspecdir/aws-sdk-docdb-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-docdb-1.31.0

%files         -n gem-aws-sdk-docdb-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-docdb-1.31.0

%files         -n gem-aws-sdk-docdb-devel

%files         -n gem-aws-sdk-machinelearning
%doc README.md
%ruby_gemspecdir/aws-sdk-machinelearning-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-machinelearning-1.28.0

%files         -n gem-aws-sdk-machinelearning-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-machinelearning-1.28.0

%files         -n gem-aws-sdk-machinelearning-devel

%files         -n gem-aws-sdk-synthetics
%doc README.md
%ruby_gemspecdir/aws-sdk-synthetics-1.12.0.gemspec
%ruby_gemslibdir/aws-sdk-synthetics-1.12.0

%files         -n gem-aws-sdk-synthetics-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-synthetics-1.12.0

%files         -n gem-aws-sdk-synthetics-devel

%files         -n gem-aws-sdk-sns
%doc README.md
%ruby_gemspecdir/aws-sdk-sns-1.41.0.gemspec
%ruby_gemslibdir/aws-sdk-sns-1.41.0

%files         -n gem-aws-sdk-sns-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-sns-1.41.0

%files         -n gem-aws-sdk-sns-devel

%files         -n gem-aws-sdk-servicequotas
%doc README.md
%ruby_gemspecdir/aws-sdk-servicequotas-1.14.0.gemspec
%ruby_gemslibdir/aws-sdk-servicequotas-1.14.0

%files         -n gem-aws-sdk-servicequotas-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-servicequotas-1.14.0

%files         -n gem-aws-sdk-servicequotas-devel

%files         -n gem-aws-sdk-pinpointemail
%doc README.md
%ruby_gemspecdir/aws-sdk-pinpointemail-1.26.0.gemspec
%ruby_gemslibdir/aws-sdk-pinpointemail-1.26.0

%files         -n gem-aws-sdk-pinpointemail-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-pinpointemail-1.26.0

%files         -n gem-aws-sdk-pinpointemail-devel

%files         -n gem-aws-sdk-mwaa
%doc README.md
%ruby_gemspecdir/aws-sdk-mwaa-1.5.0.gemspec
%ruby_gemslibdir/aws-sdk-mwaa-1.5.0

%files         -n gem-aws-sdk-mwaa-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-mwaa-1.5.0

%files         -n gem-aws-sdk-mwaa-devel

%files         -n gem-aws-sdk-opsworkscm
%doc README.md
%ruby_gemspecdir/aws-sdk-opsworkscm-1.43.0.gemspec
%ruby_gemslibdir/aws-sdk-opsworkscm-1.43.0

%files         -n gem-aws-sdk-opsworkscm-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-opsworkscm-1.43.0

%files         -n gem-aws-sdk-opsworkscm-devel

%files         -n gem-aws-sdk-codedeploy
%doc README.md
%ruby_gemspecdir/aws-sdk-codedeploy-1.40.0.gemspec
%ruby_gemslibdir/aws-sdk-codedeploy-1.40.0

%files         -n gem-aws-sdk-codedeploy-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-codedeploy-1.40.0

%files         -n gem-aws-sdk-codedeploy-devel

%files         -n gem-aws-sdk-managedblockchain
%doc README.md
%ruby_gemspecdir/aws-sdk-managedblockchain-1.22.0.gemspec
%ruby_gemslibdir/aws-sdk-managedblockchain-1.22.0

%files         -n gem-aws-sdk-managedblockchain-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-managedblockchain-1.22.0

%files         -n gem-aws-sdk-managedblockchain-devel

%files         -n gem-aws-sdk-ec2
%doc README.md
%ruby_gemspecdir/aws-sdk-ec2-1.240.0.gemspec
%ruby_gemslibdir/aws-sdk-ec2-1.240.0

%files         -n gem-aws-sdk-ec2-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ec2-1.240.0

%files         -n gem-aws-sdk-ec2-devel

%files         -n gem-aws-sdk-iotevents
%doc README.md
%ruby_gemspecdir/aws-sdk-iotevents-1.24.0.gemspec
%ruby_gemslibdir/aws-sdk-iotevents-1.24.0

%files         -n gem-aws-sdk-iotevents-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-iotevents-1.24.0

%files         -n gem-aws-sdk-iotevents-devel

%files         -n gem-aws-sdk-budgets
%doc README.md
%ruby_gemspecdir/aws-sdk-budgets-1.38.0.gemspec
%ruby_gemslibdir/aws-sdk-budgets-1.38.0

%files         -n gem-aws-sdk-budgets-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-budgets-1.38.0

%files         -n gem-aws-sdk-budgets-devel

%files         -n gem-aws-sdk-apigateway
%doc README.md
%ruby_gemspecdir/aws-sdk-apigateway-1.62.0.gemspec
%ruby_gemslibdir/aws-sdk-apigateway-1.62.0

%files         -n gem-aws-sdk-apigateway-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-apigateway-1.62.0

%files         -n gem-aws-sdk-apigateway-devel

%files         -n gem-aws-sdk-timestreamwrite
%doc README.md
%ruby_gemspecdir/aws-sdk-timestreamwrite-1.4.0.gemspec
%ruby_gemslibdir/aws-sdk-timestreamwrite-1.4.0

%files         -n gem-aws-sdk-timestreamwrite-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-timestreamwrite-1.4.0

%files         -n gem-aws-sdk-timestreamwrite-devel

%files         -n gem-aws-sdk-braket
%doc README.md
%ruby_gemspecdir/aws-sdk-braket-1.8.0.gemspec
%ruby_gemslibdir/aws-sdk-braket-1.8.0

%files         -n gem-aws-sdk-braket-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-braket-1.8.0

%files         -n gem-aws-sdk-braket-devel

%files         -n gem-aws-eventstream
%doc README.md
%ruby_gemspecdir/aws-eventstream-1.1.1.gemspec
%ruby_gemslibdir/aws-eventstream-1.1.1

%files         -n gem-aws-eventstream-doc
%doc README.md
%ruby_gemsdocdir/aws-eventstream-1.1.1

%files         -n gem-aws-sdk-acm
%doc README.md
%ruby_gemspecdir/aws-sdk-acm-1.41.0.gemspec
%ruby_gemslibdir/aws-sdk-acm-1.41.0

%files         -n gem-aws-sdk-acm-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-acm-1.41.0

%files         -n gem-aws-sdk-acm-devel

%files         -n gem-aws-sdk-macie2
%doc README.md
%ruby_gemspecdir/aws-sdk-macie2-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-macie2-1.28.0

%files         -n gem-aws-sdk-macie2-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-macie2-1.28.0

%files         -n gem-aws-sdk-macie2-devel

%files         -n gem-aws-sdk-apigatewayv2
%doc README.md
%ruby_gemspecdir/aws-sdk-apigatewayv2-1.32.0.gemspec
%ruby_gemslibdir/aws-sdk-apigatewayv2-1.32.0

%files         -n gem-aws-sdk-apigatewayv2-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-apigatewayv2-1.32.0

%files         -n gem-aws-sdk-apigatewayv2-devel

%files         -n gem-aws-sdk-autoscaling
%doc README.md
%ruby_gemspecdir/aws-sdk-autoscaling-1.63.0.gemspec
%ruby_gemslibdir/aws-sdk-autoscaling-1.63.0

%files         -n gem-aws-sdk-autoscaling-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-autoscaling-1.63.0

%files         -n gem-aws-sdk-autoscaling-devel

%files         -n gem-aws-sdk-secretsmanager
%doc README.md
%ruby_gemspecdir/aws-sdk-secretsmanager-1.46.0.gemspec
%ruby_gemslibdir/aws-sdk-secretsmanager-1.46.0

%files         -n gem-aws-sdk-secretsmanager-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-secretsmanager-1.46.0

%files         -n gem-aws-sdk-secretsmanager-devel

%files         -n gem-aws-sdk-cloudhsm
%doc README.md
%ruby_gemspecdir/aws-sdk-cloudhsm-1.30.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudhsm-1.30.0

%files         -n gem-aws-sdk-cloudhsm-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-cloudhsm-1.30.0

%files         -n gem-aws-sdk-cloudhsm-devel

%files         -n gem-aws-sdk-mediastoredata
%doc README.md
%ruby_gemspecdir/aws-sdk-mediastoredata-1.29.0.gemspec
%ruby_gemslibdir/aws-sdk-mediastoredata-1.29.0

%files         -n gem-aws-sdk-mediastoredata-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-mediastoredata-1.29.0

%files         -n gem-aws-sdk-mediastoredata-devel

%files         -n gem-aws-sdk-augmentedairuntime
%doc README.md
%ruby_gemspecdir/aws-sdk-augmentedairuntime-1.13.0.gemspec
%ruby_gemslibdir/aws-sdk-augmentedairuntime-1.13.0

%files         -n gem-aws-sdk-augmentedairuntime-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-augmentedairuntime-1.13.0

%files         -n gem-aws-sdk-augmentedairuntime-devel

%files         -n gem-aws-sdk-transcribestreamingservice
%doc README.md
%ruby_gemspecdir/aws-sdk-transcribestreamingservice-1.29.0.gemspec
%ruby_gemslibdir/aws-sdk-transcribestreamingservice-1.29.0

%files         -n gem-aws-sdk-transcribestreamingservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-transcribestreamingservice-1.29.0

%files         -n gem-aws-sdk-transcribestreamingservice-devel

%files         -n gem-aws-sdk-cloudsearchdomain
%doc README.md
%ruby_gemspecdir/aws-sdk-cloudsearchdomain-1.24.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudsearchdomain-1.24.0

%files         -n gem-aws-sdk-cloudsearchdomain-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-cloudsearchdomain-1.24.0

%files         -n gem-aws-sdk-cloudsearchdomain-devel

%files         -n gem-aws-sdk-sms
%doc README.md
%ruby_gemspecdir/aws-sdk-sms-1.29.0.gemspec
%ruby_gemslibdir/aws-sdk-sms-1.29.0

%files         -n gem-aws-sdk-sms-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-sms-1.29.0

%files         -n gem-aws-sdk-sms-devel

%files         -n gem-aws-sdk-sqs
%doc README.md
%ruby_gemspecdir/aws-sdk-sqs-1.39.0.gemspec
%ruby_gemslibdir/aws-sdk-sqs-1.39.0

%files         -n gem-aws-sdk-sqs-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-sqs-1.39.0

%files         -n gem-aws-sdk-sqs-devel

%files         -n gem-aws-sdk-devopsguru
%doc README.md
%ruby_gemspecdir/aws-sdk-devopsguru-1.6.0.gemspec
%ruby_gemslibdir/aws-sdk-devopsguru-1.6.0

%files         -n gem-aws-sdk-devopsguru-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-devopsguru-1.6.0

%files         -n gem-aws-sdk-devopsguru-devel

%files         -n gem-aws-sdk-ram
%doc README.md
%ruby_gemspecdir/aws-sdk-ram-1.25.0.gemspec
%ruby_gemslibdir/aws-sdk-ram-1.25.0

%files         -n gem-aws-sdk-ram-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ram-1.25.0

%files         -n gem-aws-sdk-ram-devel

%files         -n gem-aws-sdk-kafka
%doc README.md
%ruby_gemspecdir/aws-sdk-kafka-1.36.0.gemspec
%ruby_gemslibdir/aws-sdk-kafka-1.36.0

%files         -n gem-aws-sdk-kafka-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-kafka-1.36.0

%files         -n gem-aws-sdk-kafka-devel

%files         -n gem-aws-sdk-datasync
%doc README.md
%ruby_gemspecdir/aws-sdk-datasync-1.32.0.gemspec
%ruby_gemslibdir/aws-sdk-datasync-1.32.0

%files         -n gem-aws-sdk-datasync-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-datasync-1.32.0

%files         -n gem-aws-sdk-datasync-devel

%files         -n gem-aws-sdk-kinesisvideosignalingchannels
%doc README.md
%ruby_gemspecdir/aws-sdk-kinesisvideosignalingchannels-1.10.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesisvideosignalingchannels-1.10.0

%files         -n gem-aws-sdk-kinesisvideosignalingchannels-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-kinesisvideosignalingchannels-1.10.0

%files         -n gem-aws-sdk-kinesisvideosignalingchannels-devel

%files         -n gem-aws-sdk-applicationdiscoveryservice
%doc README.md
%ruby_gemspecdir/aws-sdk-applicationdiscoveryservice-1.35.0.gemspec
%ruby_gemslibdir/aws-sdk-applicationdiscoveryservice-1.35.0

%files         -n gem-aws-sdk-applicationdiscoveryservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-applicationdiscoveryservice-1.35.0

%files         -n gem-aws-sdk-applicationdiscoveryservice-devel

%files         -n gem-aws-sdk-glue
%doc README.md
%ruby_gemspecdir/aws-sdk-glue-1.88.0.gemspec
%ruby_gemslibdir/aws-sdk-glue-1.88.0

%files         -n gem-aws-sdk-glue-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-glue-1.88.0

%files         -n gem-aws-sdk-glue-devel

%files         -n gem-aws-sdk-mediapackage
%doc README.md
%ruby_gemspecdir/aws-sdk-mediapackage-1.40.0.gemspec
%ruby_gemslibdir/aws-sdk-mediapackage-1.40.0

%files         -n gem-aws-sdk-mediapackage-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-mediapackage-1.40.0

%files         -n gem-aws-sdk-mediapackage-devel

%files         -n gem-aws-sdk-identitystore
%doc README.md
%ruby_gemspecdir/aws-sdk-identitystore-1.5.0.gemspec
%ruby_gemslibdir/aws-sdk-identitystore-1.5.0

%files         -n gem-aws-sdk-identitystore-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-identitystore-1.5.0

%files         -n gem-aws-sdk-identitystore-devel

%files         -n gem-aws-sdk-elasticache
%doc README.md
%ruby_gemspecdir/aws-sdk-elasticache-1.57.0.gemspec
%ruby_gemslibdir/aws-sdk-elasticache-1.57.0

%files         -n gem-aws-sdk-elasticache-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-elasticache-1.57.0

%files         -n gem-aws-sdk-elasticache-devel

%files         -n gem-aws-sdk-emrcontainers
%doc README.md
%ruby_gemspecdir/aws-sdk-emrcontainers-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-emrcontainers-1.3.0

%files         -n gem-aws-sdk-emrcontainers-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-emrcontainers-1.3.0

%files         -n gem-aws-sdk-emrcontainers-devel

%files         -n gem-aws-sdk-shield
%doc README.md
%ruby_gemspecdir/aws-sdk-shield-1.37.0.gemspec
%ruby_gemslibdir/aws-sdk-shield-1.37.0

%files         -n gem-aws-sdk-shield-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-shield-1.37.0

%files         -n gem-aws-sdk-shield-devel

%files         -n gem-aws-sdk-neptune
%doc README.md
%ruby_gemspecdir/aws-sdk-neptune-1.35.0.gemspec
%ruby_gemslibdir/aws-sdk-neptune-1.35.0

%files         -n gem-aws-sdk-neptune-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-neptune-1.35.0

%files         -n gem-aws-sdk-neptune-devel

%files         -n gem-aws-sdk-robomaker
%doc README.md
%ruby_gemspecdir/aws-sdk-robomaker-1.36.0.gemspec
%ruby_gemslibdir/aws-sdk-robomaker-1.36.0

%files         -n gem-aws-sdk-robomaker-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-robomaker-1.36.0

%files         -n gem-aws-sdk-robomaker-devel

%files         -n gem-aws-sdk-comprehend
%doc README.md
%ruby_gemspecdir/aws-sdk-comprehend-1.46.0.gemspec
%ruby_gemslibdir/aws-sdk-comprehend-1.46.0

%files         -n gem-aws-sdk-comprehend-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-comprehend-1.46.0

%files         -n gem-aws-sdk-comprehend-devel

%files         -n gem-aws-sdk-rds
%doc README.md
%ruby_gemspecdir/aws-sdk-rds-1.119.0.gemspec
%ruby_gemslibdir/aws-sdk-rds-1.119.0

%files         -n gem-aws-sdk-rds-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-rds-1.119.0

%files         -n gem-aws-sdk-rds-devel

%files         -n gem-aws-sdk-iam
%doc README.md
%ruby_gemspecdir/aws-sdk-iam-1.55.0.gemspec
%ruby_gemslibdir/aws-sdk-iam-1.55.0

%files         -n gem-aws-sdk-iam-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-iam-1.55.0

%files         -n gem-aws-sdk-iam-devel

%files         -n gem-aws-sdk-storagegateway
%doc README.md
%ruby_gemspecdir/aws-sdk-storagegateway-1.55.0.gemspec
%ruby_gemslibdir/aws-sdk-storagegateway-1.55.0

%files         -n gem-aws-sdk-storagegateway-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-storagegateway-1.55.0

%files         -n gem-aws-sdk-storagegateway-devel

%files         -n gem-aws-sdk-cloudwatch
%doc README.md
%ruby_gemspecdir/aws-sdk-cloudwatch-1.51.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudwatch-1.51.0

%files         -n gem-aws-sdk-cloudwatch-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-cloudwatch-1.51.0

%files         -n gem-aws-sdk-cloudwatch-devel

%files         -n gem-aws-sdk-iotwireless
%doc README.md
%ruby_gemspecdir/aws-sdk-iotwireless-1.10.0.gemspec
%ruby_gemslibdir/aws-sdk-iotwireless-1.10.0

%files         -n gem-aws-sdk-iotwireless-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-iotwireless-1.10.0

%files         -n gem-aws-sdk-iotwireless-devel

%files         -n gem-aws-partitions
%doc README.md
%ruby_gemspecdir/aws-partitions-1.465.0.gemspec
%ruby_gemslibdir/aws-partitions-1.465.0

%files         -n gem-aws-partitions-doc
%doc README.md
%ruby_gemsdocdir/aws-partitions-1.465.0

%files         -n gem-aws-sdk-eks
%doc README.md
%ruby_gemspecdir/aws-sdk-eks-1.55.0.gemspec
%ruby_gemslibdir/aws-sdk-eks-1.55.0

%files         -n gem-aws-sdk-eks-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-eks-1.55.0

%files         -n gem-aws-sdk-eks-devel

%files         -n gem-aws-sdk-iotanalytics
%doc README.md
%ruby_gemspecdir/aws-sdk-iotanalytics-1.38.0.gemspec
%ruby_gemslibdir/aws-sdk-iotanalytics-1.38.0

%files         -n gem-aws-sdk-iotanalytics-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-iotanalytics-1.38.0

%files         -n gem-aws-sdk-iotanalytics-devel

%files         -n gem-aws-sdk-mturk
%doc README.md
%ruby_gemspecdir/aws-sdk-mturk-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-mturk-1.31.0

%files         -n gem-aws-sdk-mturk-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-mturk-1.31.0

%files         -n gem-aws-sdk-mturk-devel

%files         -n gem-aws-sdk-cognitoidentityprovider
%doc README.md
%ruby_gemspecdir/aws-sdk-cognitoidentityprovider-1.51.0.gemspec
%ruby_gemslibdir/aws-sdk-cognitoidentityprovider-1.51.0

%files         -n gem-aws-sdk-cognitoidentityprovider-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-cognitoidentityprovider-1.51.0

%files         -n gem-aws-sdk-cognitoidentityprovider-devel

%files         -n gem-aws-sdk-elasticbeanstalk
%doc README.md
%ruby_gemspecdir/aws-sdk-elasticbeanstalk-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-elasticbeanstalk-1.42.0

%files         -n gem-aws-sdk-elasticbeanstalk-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-elasticbeanstalk-1.42.0

%files         -n gem-aws-sdk-elasticbeanstalk-devel

%files         -n gem-aws-sdk-fsx
%doc README.md
%ruby_gemspecdir/aws-sdk-fsx-1.37.0.gemspec
%ruby_gemslibdir/aws-sdk-fsx-1.37.0

%files         -n gem-aws-sdk-fsx-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-fsx-1.37.0

%files         -n gem-aws-sdk-fsx-devel

%files         -n gem-aws-sdk-clouddirectory
%doc README.md
%ruby_gemspecdir/aws-sdk-clouddirectory-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-clouddirectory-1.31.0

%files         -n gem-aws-sdk-clouddirectory-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-clouddirectory-1.31.0

%files         -n gem-aws-sdk-clouddirectory-devel

%files         -n gem-aws-sdk-efs
%doc README.md
%ruby_gemspecdir/aws-sdk-efs-1.40.0.gemspec
%ruby_gemslibdir/aws-sdk-efs-1.40.0

%files         -n gem-aws-sdk-efs-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-efs-1.40.0

%files         -n gem-aws-sdk-efs-devel

%files         -n gem-aws-sdk-sagemakerfeaturestoreruntime
%doc README.md
%ruby_gemspecdir/aws-sdk-sagemakerfeaturestoreruntime-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-sagemakerfeaturestoreruntime-1.2.0

%files         -n gem-aws-sdk-sagemakerfeaturestoreruntime-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-sagemakerfeaturestoreruntime-1.2.0

%files         -n gem-aws-sdk-sagemakerfeaturestoreruntime-devel

%files         -n gem-aws-sdk-lookoutforvision
%doc README.md
%ruby_gemspecdir/aws-sdk-lookoutforvision-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-lookoutforvision-1.3.0

%files         -n gem-aws-sdk-lookoutforvision-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-lookoutforvision-1.3.0

%files         -n gem-aws-sdk-lookoutforvision-devel

%files         -n gem-aws-sdk-mgn
%doc README.md
%ruby_gemspecdir/aws-sdk-mgn-1.0.0.gemspec
%ruby_gemslibdir/aws-sdk-mgn-1.0.0

%files         -n gem-aws-sdk-mgn-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-mgn-1.0.0

%files         -n gem-aws-sdk-mgn-devel

%files         -n gem-aws-sdk-honeycode
%doc README.md
%ruby_gemspecdir/aws-sdk-honeycode-1.6.0.gemspec
%ruby_gemslibdir/aws-sdk-honeycode-1.6.0

%files         -n gem-aws-sdk-honeycode-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-honeycode-1.6.0

%files         -n gem-aws-sdk-honeycode-devel

%files         -n gem-aws-sdk-marketplacecatalog
%doc README.md
%ruby_gemspecdir/aws-sdk-marketplacecatalog-1.12.0.gemspec
%ruby_gemslibdir/aws-sdk-marketplacecatalog-1.12.0

%files         -n gem-aws-sdk-marketplacecatalog-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-marketplacecatalog-1.12.0

%files         -n gem-aws-sdk-marketplacecatalog-devel

%files         -n gem-aws-sdk-appintegrationsservice
%doc README.md
%ruby_gemspecdir/aws-sdk-appintegrationsservice-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-appintegrationsservice-1.2.0

%files         -n gem-aws-sdk-appintegrationsservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-appintegrationsservice-1.2.0

%files         -n gem-aws-sdk-appintegrationsservice-devel

%files         -n gem-aws-sdk-cloudsearch
%doc README.md
%ruby_gemspecdir/aws-sdk-cloudsearch-1.29.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudsearch-1.29.0

%files         -n gem-aws-sdk-cloudsearch-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-cloudsearch-1.29.0

%files         -n gem-aws-sdk-cloudsearch-devel

%files         -n gem-aws-sigv4
%doc README.md
%ruby_gemspecdir/aws-sigv4-1.2.3.gemspec
%ruby_gemslibdir/aws-sigv4-1.2.3

%files         -n gem-aws-sigv4-doc
%doc README.md
%ruby_gemsdocdir/aws-sigv4-1.2.3

%files         -n gem-aws-sigv4-devel

%files         -n gem-aws-sdk-codeguruprofiler
%doc README.md
%ruby_gemspecdir/aws-sdk-codeguruprofiler-1.15.0.gemspec
%ruby_gemslibdir/aws-sdk-codeguruprofiler-1.15.0

%files         -n gem-aws-sdk-codeguruprofiler-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-codeguruprofiler-1.15.0

%files         -n gem-aws-sdk-codeguruprofiler-devel

%files         -n gem-aws-sdk-states
%doc README.md
%ruby_gemspecdir/aws-sdk-states-1.39.0.gemspec
%ruby_gemslibdir/aws-sdk-states-1.39.0

%files         -n gem-aws-sdk-states-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-states-1.39.0

%files         -n gem-aws-sdk-states-devel

%files         -n gem-aws-sdk-cloud9
%doc README.md
%ruby_gemspecdir/aws-sdk-cloud9-1.33.0.gemspec
%ruby_gemslibdir/aws-sdk-cloud9-1.33.0

%files         -n gem-aws-sdk-cloud9-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-cloud9-1.33.0

%files         -n gem-aws-sdk-cloud9-devel

%files         -n gem-aws-sdk-codestarconnections
%doc README.md
%ruby_gemspecdir/aws-sdk-codestarconnections-1.15.0.gemspec
%ruby_gemslibdir/aws-sdk-codestarconnections-1.15.0

%files         -n gem-aws-sdk-codestarconnections-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-codestarconnections-1.15.0

%files         -n gem-aws-sdk-codestarconnections-devel

%files         -n gem-aws-sdk-codegurureviewer
%doc README.md
%ruby_gemspecdir/aws-sdk-codegurureviewer-1.17.0.gemspec
%ruby_gemslibdir/aws-sdk-codegurureviewer-1.17.0

%files         -n gem-aws-sdk-codegurureviewer-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-codegurureviewer-1.17.0

%files         -n gem-aws-sdk-codegurureviewer-devel

%files         -n gem-aws-sdk-iotdeviceadvisor
%doc README.md
%ruby_gemspecdir/aws-sdk-iotdeviceadvisor-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-iotdeviceadvisor-1.3.0

%files         -n gem-aws-sdk-iotdeviceadvisor-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-iotdeviceadvisor-1.3.0

%files         -n gem-aws-sdk-iotdeviceadvisor-devel

%files         -n gem-aws-sdk-cloudhsmv2
%doc README.md
%ruby_gemspecdir/aws-sdk-cloudhsmv2-1.33.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudhsmv2-1.33.0

%files         -n gem-aws-sdk-cloudhsmv2-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-cloudhsmv2-1.33.0

%files         -n gem-aws-sdk-cloudhsmv2-devel

%files         -n gem-aws-sdk-opsworks
%doc README.md
%ruby_gemspecdir/aws-sdk-opsworks-1.32.0.gemspec
%ruby_gemslibdir/aws-sdk-opsworks-1.32.0

%files         -n gem-aws-sdk-opsworks-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-opsworks-1.32.0

%files         -n gem-aws-sdk-opsworks-devel

%files         -n gem-aws-sdk-iotdataplane
%doc README.md
%ruby_gemspecdir/aws-sdk-iotdataplane-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-iotdataplane-1.28.0

%files         -n gem-aws-sdk-iotdataplane-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-iotdataplane-1.28.0

%files         -n gem-aws-sdk-iotdataplane-devel

%files         -n gem-aws-sdk-dataexchange
%doc README.md
%ruby_gemspecdir/aws-sdk-dataexchange-1.13.0.gemspec
%ruby_gemslibdir/aws-sdk-dataexchange-1.13.0

%files         -n gem-aws-sdk-dataexchange-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-dataexchange-1.13.0

%files         -n gem-aws-sdk-dataexchange-devel

%files         -n gem-aws-sdk-qldbsession
%doc README.md
%ruby_gemspecdir/aws-sdk-qldbsession-1.13.0.gemspec
%ruby_gemslibdir/aws-sdk-qldbsession-1.13.0

%files         -n gem-aws-sdk-qldbsession-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-qldbsession-1.13.0

%files         -n gem-aws-sdk-qldbsession-devel

%files         -n gem-aws-sdk-mediatailor
%doc README.md
%ruby_gemspecdir/aws-sdk-mediatailor-1.38.0.gemspec
%ruby_gemslibdir/aws-sdk-mediatailor-1.38.0

%files         -n gem-aws-sdk-mediatailor-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-mediatailor-1.38.0

%files         -n gem-aws-sdk-mediatailor-devel

%files         -n gem-aws-sdk-timestreamquery
%doc README.md
%ruby_gemspecdir/aws-sdk-timestreamquery-1.4.0.gemspec
%ruby_gemslibdir/aws-sdk-timestreamquery-1.4.0

%files         -n gem-aws-sdk-timestreamquery-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-timestreamquery-1.4.0

%files         -n gem-aws-sdk-timestreamquery-devel

%files         -n gem-aws-sdk-translate
%doc README.md
%ruby_gemspecdir/aws-sdk-translate-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-translate-1.31.0

%files         -n gem-aws-sdk-translate-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-translate-1.31.0

%files         -n gem-aws-sdk-translate-devel

%files         -n gem-aws-sdk-workmail
%doc README.md
%ruby_gemspecdir/aws-sdk-workmail-1.37.0.gemspec
%ruby_gemslibdir/aws-sdk-workmail-1.37.0

%files         -n gem-aws-sdk-workmail-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-workmail-1.37.0

%files         -n gem-aws-sdk-workmail-devel

%files         -n gem-aws-sdk-transfer
%doc README.md
%ruby_gemspecdir/aws-sdk-transfer-1.33.0.gemspec
%ruby_gemslibdir/aws-sdk-transfer-1.33.0

%files         -n gem-aws-sdk-transfer-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-transfer-1.33.0

%files         -n gem-aws-sdk-transfer-devel

%files         -n gem-aws-sdk-ioteventsdata
%doc README.md
%ruby_gemspecdir/aws-sdk-ioteventsdata-1.16.0.gemspec
%ruby_gemslibdir/aws-sdk-ioteventsdata-1.16.0

%files         -n gem-aws-sdk-ioteventsdata-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ioteventsdata-1.16.0

%files         -n gem-aws-sdk-ioteventsdata-devel

%files         -n gem-aws-sdk-kms
%doc README.md
%ruby_gemspecdir/aws-sdk-kms-1.43.0.gemspec
%ruby_gemslibdir/aws-sdk-kms-1.43.0

%files         -n gem-aws-sdk-kms-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-kms-1.43.0

%files         -n gem-aws-sdk-kms-devel

%files         -n gem-aws-sdk-frauddetector
%doc README.md
%ruby_gemspecdir/aws-sdk-frauddetector-1.18.0.gemspec
%ruby_gemslibdir/aws-sdk-frauddetector-1.18.0

%files         -n gem-aws-sdk-frauddetector-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-frauddetector-1.18.0

%files         -n gem-aws-sdk-frauddetector-devel

%files         -n gem-aws-sdk-lexmodelsv2
%doc README.md
%ruby_gemspecdir/aws-sdk-lexmodelsv2-1.4.0.gemspec
%ruby_gemslibdir/aws-sdk-lexmodelsv2-1.4.0

%files         -n gem-aws-sdk-lexmodelsv2-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-lexmodelsv2-1.4.0

%files         -n gem-aws-sdk-lexmodelsv2-devel

%files         -n gem-aws-sdk-healthlake
%doc README.md
%ruby_gemspecdir/aws-sdk-healthlake-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-healthlake-1.3.0

%files         -n gem-aws-sdk-healthlake-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-healthlake-1.3.0

%files         -n gem-aws-sdk-healthlake-devel

%files         -n gem-aws-sdk-gluedatabrew
%doc README.md
%ruby_gemspecdir/aws-sdk-gluedatabrew-1.7.0.gemspec
%ruby_gemslibdir/aws-sdk-gluedatabrew-1.7.0

%files         -n gem-aws-sdk-gluedatabrew-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-gluedatabrew-1.7.0

%files         -n gem-aws-sdk-gluedatabrew-devel

%files         -n gem-aws-sdk-migrationhubconfig
%doc README.md
%ruby_gemspecdir/aws-sdk-migrationhubconfig-1.11.0.gemspec
%ruby_gemslibdir/aws-sdk-migrationhubconfig-1.11.0

%files         -n gem-aws-sdk-migrationhubconfig-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-migrationhubconfig-1.11.0

%files         -n gem-aws-sdk-migrationhubconfig-devel

%files         -n gem-aws-sdk-networkmanager
%doc README.md
%ruby_gemspecdir/aws-sdk-networkmanager-1.11.0.gemspec
%ruby_gemslibdir/aws-sdk-networkmanager-1.11.0

%files         -n gem-aws-sdk-networkmanager-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-networkmanager-1.11.0

%files         -n gem-aws-sdk-networkmanager-devel

%files         -n gem-aws-sdk-kinesisanalytics
%doc README.md
%ruby_gemspecdir/aws-sdk-kinesisanalytics-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesisanalytics-1.31.0

%files         -n gem-aws-sdk-kinesisanalytics-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-kinesisanalytics-1.31.0

%files         -n gem-aws-sdk-kinesisanalytics-devel

%files         -n gem-aws-sdk-redshiftdataapiservice
%doc README.md
%ruby_gemspecdir/aws-sdk-redshiftdataapiservice-1.6.0.gemspec
%ruby_gemslibdir/aws-sdk-redshiftdataapiservice-1.6.0

%files         -n gem-aws-sdk-redshiftdataapiservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-redshiftdataapiservice-1.6.0

%files         -n gem-aws-sdk-redshiftdataapiservice-devel

%files         -n gem-aws-sdk-personalizeevents
%doc README.md
%ruby_gemspecdir/aws-sdk-personalizeevents-1.17.0.gemspec
%ruby_gemslibdir/aws-sdk-personalizeevents-1.17.0

%files         -n gem-aws-sdk-personalizeevents-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-personalizeevents-1.17.0

%files         -n gem-aws-sdk-personalizeevents-devel

%files         -n gem-aws-sdk-appmesh
%doc README.md
%ruby_gemspecdir/aws-sdk-appmesh-1.35.0.gemspec
%ruby_gemslibdir/aws-sdk-appmesh-1.35.0

%files         -n gem-aws-sdk-appmesh-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-appmesh-1.35.0

%files         -n gem-aws-sdk-appmesh-devel

%files         -n gem-aws-sdk-savingsplans
%doc README.md
%ruby_gemspecdir/aws-sdk-savingsplans-1.15.0.gemspec
%ruby_gemslibdir/aws-sdk-savingsplans-1.15.0

%files         -n gem-aws-sdk-savingsplans-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-savingsplans-1.15.0

%files         -n gem-aws-sdk-savingsplans-devel

%files         -n gem-aws-sdk-mobile
%doc README.md
%ruby_gemspecdir/aws-sdk-mobile-1.26.0.gemspec
%ruby_gemslibdir/aws-sdk-mobile-1.26.0

%files         -n gem-aws-sdk-mobile-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-mobile-1.26.0

%files         -n gem-aws-sdk-mobile-devel

%files         -n gem-aws-sdk-core
%doc README.md
%ruby_gemspecdir/aws-sdk-core-3.114.1.gemspec
%ruby_gemslibdir/aws-sdk-core-3.114.1

%files         -n gem-aws-sdk-core-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-core-3.114.1

%files         -n gem-aws-sdk-core-devel

%files         -n gem-aws-sdk-forecastservice
%doc README.md
%ruby_gemspecdir/aws-sdk-forecastservice-1.21.0.gemspec
%ruby_gemslibdir/aws-sdk-forecastservice-1.21.0

%files         -n gem-aws-sdk-forecastservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-forecastservice-1.21.0

%files         -n gem-aws-sdk-forecastservice-devel

%files         -n gem-aws-sdk-codeartifact
%doc README.md
%ruby_gemspecdir/aws-sdk-codeartifact-1.10.0.gemspec
%ruby_gemslibdir/aws-sdk-codeartifact-1.10.0

%files         -n gem-aws-sdk-codeartifact-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-codeartifact-1.10.0

%files         -n gem-aws-sdk-codeartifact-devel

%files         -n gem-aws-sdk-sagemakeredgemanager
%doc README.md
%ruby_gemspecdir/aws-sdk-sagemakeredgemanager-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-sagemakeredgemanager-1.2.0

%files         -n gem-aws-sdk-sagemakeredgemanager-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-sagemakeredgemanager-1.2.0

%files         -n gem-aws-sdk-sagemakeredgemanager-devel

%files         -n gem-aws-sdk-resourcegroups
%doc README.md
%ruby_gemspecdir/aws-sdk-resourcegroups-1.36.0.gemspec
%ruby_gemslibdir/aws-sdk-resourcegroups-1.36.0

%files         -n gem-aws-sdk-resourcegroups-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-resourcegroups-1.36.0

%files         -n gem-aws-sdk-resourcegroups-devel

%files         -n gem-aws-sdk-applicationinsights
%doc README.md
%ruby_gemspecdir/aws-sdk-applicationinsights-1.18.0.gemspec
%ruby_gemslibdir/aws-sdk-applicationinsights-1.18.0

%files         -n gem-aws-sdk-applicationinsights-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-applicationinsights-1.18.0

%files         -n gem-aws-sdk-applicationinsights-devel

%files         -n gem-aws-sdk-directconnect
%doc README.md
%ruby_gemspecdir/aws-sdk-directconnect-1.41.0.gemspec
%ruby_gemslibdir/aws-sdk-directconnect-1.41.0

%files         -n gem-aws-sdk-directconnect-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-directconnect-1.41.0

%files         -n gem-aws-sdk-directconnect-devel

%files         -n gem-aws-sdk-pricing
%doc README.md
%ruby_gemspecdir/aws-sdk-pricing-1.27.0.gemspec
%ruby_gemslibdir/aws-sdk-pricing-1.27.0

%files         -n gem-aws-sdk-pricing-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-pricing-1.27.0

%files         -n gem-aws-sdk-pricing-devel

%files         -n gem-aws-sigv2
%doc README.md
%ruby_gemspecdir/aws-sigv2-1.0.2.gemspec
%ruby_gemslibdir/aws-sigv2-1.0.2

%files         -n gem-aws-sigv2-doc
%doc README.md
%ruby_gemsdocdir/aws-sigv2-1.0.2

%files         -n gem-aws-sdk-dynamodb
%doc README.md
%ruby_gemspecdir/aws-sdk-dynamodb-1.60.0.gemspec
%ruby_gemslibdir/aws-sdk-dynamodb-1.60.0

%files         -n gem-aws-sdk-dynamodb-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-dynamodb-1.60.0

%files         -n gem-aws-sdk-dynamodb-devel

%files         -n gem-aws-sdk-dax
%doc README.md
%ruby_gemspecdir/aws-sdk-dax-1.29.0.gemspec
%ruby_gemslibdir/aws-sdk-dax-1.29.0

%files         -n gem-aws-sdk-dax-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-dax-1.29.0

%files         -n gem-aws-sdk-dax-devel

%files         -n gem-aws-sdk-iotsecuretunneling
%doc README.md
%ruby_gemspecdir/aws-sdk-iotsecuretunneling-1.11.0.gemspec
%ruby_gemslibdir/aws-sdk-iotsecuretunneling-1.11.0

%files         -n gem-aws-sdk-iotsecuretunneling-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-iotsecuretunneling-1.11.0

%files         -n gem-aws-sdk-iotsecuretunneling-devel

%files         -n gem-aws-sdk-cognitoidentity
%doc README.md
%ruby_gemspecdir/aws-sdk-cognitoidentity-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-cognitoidentity-1.31.0

%files         -n gem-aws-sdk-cognitoidentity-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-cognitoidentity-1.31.0

%files         -n gem-aws-sdk-cognitoidentity-devel

%files         -n gem-aws-sdk-gamelift
%doc README.md
%ruby_gemspecdir/aws-sdk-gamelift-1.44.0.gemspec
%ruby_gemslibdir/aws-sdk-gamelift-1.44.0

%files         -n gem-aws-sdk-gamelift-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-gamelift-1.44.0

%files         -n gem-aws-sdk-gamelift-devel

%files         -n gem-aws-sdk-cloudwatchevents
%doc README.md
%ruby_gemspecdir/aws-sdk-cloudwatchevents-1.46.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudwatchevents-1.46.0

%files         -n gem-aws-sdk-cloudwatchevents-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-cloudwatchevents-1.46.0

%files         -n gem-aws-sdk-cloudwatchevents-devel

%files         -n gem-aws-sdk-s3
%doc README.md
%ruby_gemspecdir/aws-sdk-s3-1.96.0.gemspec
%ruby_gemslibdir/aws-sdk-s3-1.96.0

%files         -n gem-aws-sdk-s3-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-s3-1.96.0

%files         -n gem-aws-sdk-s3-devel

%files         -n gem-aws-sdk-connectparticipant
%doc README.md
%ruby_gemspecdir/aws-sdk-connectparticipant-1.11.0.gemspec
%ruby_gemslibdir/aws-sdk-connectparticipant-1.11.0

%files         -n gem-aws-sdk-connectparticipant-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-connectparticipant-1.11.0

%files         -n gem-aws-sdk-connectparticipant-devel

%files         -n gem-aws-sdk-codepipeline
%doc README.md
%ruby_gemspecdir/aws-sdk-codepipeline-1.44.0.gemspec
%ruby_gemslibdir/aws-sdk-codepipeline-1.44.0

%files         -n gem-aws-sdk-codepipeline-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-codepipeline-1.44.0

%files         -n gem-aws-sdk-codepipeline-devel

%files         -n gem-aws-sdk-costandusagereportservice
%doc README.md
%ruby_gemspecdir/aws-sdk-costandusagereportservice-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-costandusagereportservice-1.31.0

%files         -n gem-aws-sdk-costandusagereportservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-costandusagereportservice-1.31.0

%files         -n gem-aws-sdk-costandusagereportservice-devel

%files         -n gem-aws-sdk-s3control
%doc README.md
%ruby_gemspecdir/aws-sdk-s3control-1.34.0.gemspec
%ruby_gemslibdir/aws-sdk-s3control-1.34.0

%files         -n gem-aws-sdk-s3control-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-s3control-1.34.0

%files         -n gem-aws-sdk-s3control-devel

%files         -n gem-aws-sdk-marketplacemetering
%doc README.md
%ruby_gemspecdir/aws-sdk-marketplacemetering-1.34.0.gemspec
%ruby_gemslibdir/aws-sdk-marketplacemetering-1.34.0

%files         -n gem-aws-sdk-marketplacemetering-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-marketplacemetering-1.34.0

%files         -n gem-aws-sdk-marketplacemetering-devel

%files         -n gem-aws-sdk-forecastqueryservice
%doc README.md
%ruby_gemspecdir/aws-sdk-forecastqueryservice-1.12.0.gemspec
%ruby_gemslibdir/aws-sdk-forecastqueryservice-1.12.0

%files         -n gem-aws-sdk-forecastqueryservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-forecastqueryservice-1.12.0

%files         -n gem-aws-sdk-forecastqueryservice-devel

%files         -n gem-aws-sdk-pi
%doc README.md
%ruby_gemspecdir/aws-sdk-pi-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-pi-1.28.0

%files         -n gem-aws-sdk-pi-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-pi-1.28.0

%files         -n gem-aws-sdk-pi-devel

%files         -n gem-aws-sdk-waf
%doc README.md
%ruby_gemspecdir/aws-sdk-waf-1.38.0.gemspec
%ruby_gemslibdir/aws-sdk-waf-1.38.0

%files         -n gem-aws-sdk-waf-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-waf-1.38.0

%files         -n gem-aws-sdk-waf-devel

%files         -n gem-aws-sdk-mediastore
%doc README.md
%ruby_gemspecdir/aws-sdk-mediastore-1.32.0.gemspec
%ruby_gemslibdir/aws-sdk-mediastore-1.32.0

%files         -n gem-aws-sdk-mediastore-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-mediastore-1.32.0

%files         -n gem-aws-sdk-mediastore-devel

%files         -n gem-aws-sdk-elasticloadbalancingv2
%doc README.md
%ruby_gemspecdir/aws-sdk-elasticloadbalancingv2-1.61.0.gemspec
%ruby_gemslibdir/aws-sdk-elasticloadbalancingv2-1.61.0

%files         -n gem-aws-sdk-elasticloadbalancingv2-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-elasticloadbalancingv2-1.61.0

%files         -n gem-aws-sdk-elasticloadbalancingv2-devel

%files         -n gem-aws-sdk-serverlessapplicationrepository
%doc README.md
%ruby_gemspecdir/aws-sdk-serverlessapplicationrepository-1.34.0.gemspec
%ruby_gemslibdir/aws-sdk-serverlessapplicationrepository-1.34.0

%files         -n gem-aws-sdk-serverlessapplicationrepository-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-serverlessapplicationrepository-1.34.0

%files         -n gem-aws-sdk-serverlessapplicationrepository-devel

%files         -n gem-aws-sdk-lexmodelbuildingservice
%doc README.md
%ruby_gemspecdir/aws-sdk-lexmodelbuildingservice-1.45.0.gemspec
%ruby_gemslibdir/aws-sdk-lexmodelbuildingservice-1.45.0

%files         -n gem-aws-sdk-lexmodelbuildingservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-lexmodelbuildingservice-1.45.0

%files         -n gem-aws-sdk-lexmodelbuildingservice-devel

%files         -n gem-aws-sdk-medialive
%doc README.md
%ruby_gemspecdir/aws-sdk-medialive-1.71.0.gemspec
%ruby_gemslibdir/aws-sdk-medialive-1.71.0

%files         -n gem-aws-sdk-medialive-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-medialive-1.71.0

%files         -n gem-aws-sdk-medialive-devel

%files         -n gem-aws-sdk-connectcontactlens
%doc README.md
%ruby_gemspecdir/aws-sdk-connectcontactlens-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-connectcontactlens-1.2.0

%files         -n gem-aws-sdk-connectcontactlens-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-connectcontactlens-1.2.0

%files         -n gem-aws-sdk-connectcontactlens-devel

%files         -n gem-aws-sdk-comprehendmedical
%doc README.md
%ruby_gemspecdir/aws-sdk-comprehendmedical-1.26.0.gemspec
%ruby_gemslibdir/aws-sdk-comprehendmedical-1.26.0

%files         -n gem-aws-sdk-comprehendmedical-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-comprehendmedical-1.26.0

%files         -n gem-aws-sdk-comprehendmedical-devel

%files         -n gem-aws-sdk-outposts
%doc README.md
%ruby_gemspecdir/aws-sdk-outposts-1.16.0.gemspec
%ruby_gemslibdir/aws-sdk-outposts-1.16.0

%files         -n gem-aws-sdk-outposts-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-outposts-1.16.0

%files         -n gem-aws-sdk-outposts-devel

%files         -n gem-aws-sdk-workdocs
%doc README.md
%ruby_gemspecdir/aws-sdk-workdocs-1.30.0.gemspec
%ruby_gemslibdir/aws-sdk-workdocs-1.30.0

%files         -n gem-aws-sdk-workdocs-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-workdocs-1.30.0

%files         -n gem-aws-sdk-workdocs-devel

%files         -n gem-aws-sdk-kinesisvideo
%doc README.md
%ruby_gemspecdir/aws-sdk-kinesisvideo-1.32.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesisvideo-1.32.0

%files         -n gem-aws-sdk-kinesisvideo-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-kinesisvideo-1.32.0

%files         -n gem-aws-sdk-kinesisvideo-devel

%files         -n gem-aws-sdk-cloudwatchlogs
%doc README.md
%ruby_gemspecdir/aws-sdk-cloudwatchlogs-1.41.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudwatchlogs-1.41.0

%files         -n gem-aws-sdk-cloudwatchlogs-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-cloudwatchlogs-1.41.0

%files         -n gem-aws-sdk-cloudwatchlogs-devel

%files         -n gem-aws-sdk
%doc README.md
%ruby_gemspecdir/aws-sdk-3.0.2.gemspec
%ruby_gemslibdir/aws-sdk-3.0.2

%files         -n gem-aws-sdk-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-3.0.2

%files         -n gem-aws-sdk-devel

%files         -n gem-aws-sdk-mediapackagevod
%doc README.md
%ruby_gemspecdir/aws-sdk-mediapackagevod-1.23.0.gemspec
%ruby_gemslibdir/aws-sdk-mediapackagevod-1.23.0

%files         -n gem-aws-sdk-mediapackagevod-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-mediapackagevod-1.23.0

%files         -n gem-aws-sdk-mediapackagevod-devel

%files         -n gem-aws-sdk-glacier
%doc README.md
%ruby_gemspecdir/aws-sdk-glacier-1.37.0.gemspec
%ruby_gemslibdir/aws-sdk-glacier-1.37.0

%files         -n gem-aws-sdk-glacier-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-glacier-1.37.0

%files         -n gem-aws-sdk-glacier-devel

%files         -n gem-aws-sdk-simpledb
%doc README.md
%ruby_gemspecdir/aws-sdk-simpledb-1.26.0.gemspec
%ruby_gemslibdir/aws-sdk-simpledb-1.26.0

%files         -n gem-aws-sdk-simpledb-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-simpledb-1.26.0

%files         -n gem-aws-sdk-simpledb-devel

%files         -n gem-aws-sdk-emr
%doc README.md
%ruby_gemspecdir/aws-sdk-emr-1.45.0.gemspec
%ruby_gemslibdir/aws-sdk-emr-1.45.0

%files         -n gem-aws-sdk-emr-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-emr-1.45.0

%files         -n gem-aws-sdk-emr-devel

%files         -n gem-aws-sdk-ecr
%doc README.md
%ruby_gemspecdir/aws-sdk-ecr-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-ecr-1.42.0

%files         -n gem-aws-sdk-ecr-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ecr-1.42.0

%files         -n gem-aws-sdk-ecr-devel

%files         -n gem-aws-sdk-rekognition
%doc README.md
%ruby_gemspecdir/aws-sdk-rekognition-1.51.0.gemspec
%ruby_gemslibdir/aws-sdk-rekognition-1.51.0

%files         -n gem-aws-sdk-rekognition-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-rekognition-1.51.0

%files         -n gem-aws-sdk-rekognition-devel

%files         -n gem-aws-sdk-directoryservice
%doc README.md
%ruby_gemspecdir/aws-sdk-directoryservice-1.39.0.gemspec
%ruby_gemslibdir/aws-sdk-directoryservice-1.39.0

%files         -n gem-aws-sdk-directoryservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-directoryservice-1.39.0

%files         -n gem-aws-sdk-directoryservice-devel

%files         -n gem-aws-sdk-organizations
%doc README.md
%ruby_gemspecdir/aws-sdk-organizations-1.59.0.gemspec
%ruby_gemslibdir/aws-sdk-organizations-1.59.0

%files         -n gem-aws-sdk-organizations-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-organizations-1.59.0

%files         -n gem-aws-sdk-organizations-devel

%files         -n gem-aws-sdk-servicediscovery
%doc README.md
%ruby_gemspecdir/aws-sdk-servicediscovery-1.36.0.gemspec
%ruby_gemslibdir/aws-sdk-servicediscovery-1.36.0

%files         -n gem-aws-sdk-servicediscovery-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-servicediscovery-1.36.0

%files         -n gem-aws-sdk-servicediscovery-devel

%files         -n gem-aws-sdk-batch
%doc README.md
%ruby_gemspecdir/aws-sdk-batch-1.47.0.gemspec
%ruby_gemslibdir/aws-sdk-batch-1.47.0

%files         -n gem-aws-sdk-batch-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-batch-1.47.0

%files         -n gem-aws-sdk-batch-devel

%files         -n gem-aws-sdk-acmpca
%doc README.md
%ruby_gemspecdir/aws-sdk-acmpca-1.36.0.gemspec
%ruby_gemslibdir/aws-sdk-acmpca-1.36.0

%files         -n gem-aws-sdk-acmpca-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-acmpca-1.36.0

%files         -n gem-aws-sdk-acmpca-devel

%files         -n gem-aws-sdk-qldb
%doc README.md
%ruby_gemspecdir/aws-sdk-qldb-1.15.0.gemspec
%ruby_gemslibdir/aws-sdk-qldb-1.15.0

%files         -n gem-aws-sdk-qldb-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-qldb-1.15.0

%files         -n gem-aws-sdk-qldb-devel

%files         -n gem-aws-sdk-mediaconnect
%doc README.md
%ruby_gemspecdir/aws-sdk-mediaconnect-1.33.0.gemspec
%ruby_gemslibdir/aws-sdk-mediaconnect-1.33.0

%files         -n gem-aws-sdk-mediaconnect-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-mediaconnect-1.33.0

%files         -n gem-aws-sdk-mediaconnect-devel

%files         -n gem-aws-sdk-cloudtrail
%doc README.md
%ruby_gemspecdir/aws-sdk-cloudtrail-1.35.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudtrail-1.35.0

%files         -n gem-aws-sdk-cloudtrail-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-cloudtrail-1.35.0

%files         -n gem-aws-sdk-cloudtrail-devel

%files         -n gem-aws-sdk-dynamodbstreams
%doc README.md
%ruby_gemspecdir/aws-sdk-dynamodbstreams-1.29.0.gemspec
%ruby_gemslibdir/aws-sdk-dynamodbstreams-1.29.0

%files         -n gem-aws-sdk-dynamodbstreams-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-dynamodbstreams-1.29.0

%files         -n gem-aws-sdk-dynamodbstreams-devel

%files         -n gem-aws-sdk-guardduty
%doc README.md
%ruby_gemspecdir/aws-sdk-guardduty-1.45.0.gemspec
%ruby_gemslibdir/aws-sdk-guardduty-1.45.0

%files         -n gem-aws-sdk-guardduty-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-guardduty-1.45.0

%files         -n gem-aws-sdk-guardduty-devel

%files         -n gem-aws-sdk-iotjobsdataplane
%doc README.md
%ruby_gemspecdir/aws-sdk-iotjobsdataplane-1.27.0.gemspec
%ruby_gemslibdir/aws-sdk-iotjobsdataplane-1.27.0

%files         -n gem-aws-sdk-iotjobsdataplane-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-iotjobsdataplane-1.27.0

%files         -n gem-aws-sdk-iotjobsdataplane-devel

%files         -n gem-aws-sdk-dlm
%doc README.md
%ruby_gemspecdir/aws-sdk-dlm-1.40.0.gemspec
%ruby_gemslibdir/aws-sdk-dlm-1.40.0

%files         -n gem-aws-sdk-dlm-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-dlm-1.40.0

%files         -n gem-aws-sdk-dlm-devel

%files         -n gem-aws-sdk-devicefarm
%doc README.md
%ruby_gemspecdir/aws-sdk-devicefarm-1.42.0.gemspec
%ruby_gemslibdir/aws-sdk-devicefarm-1.42.0

%files         -n gem-aws-sdk-devicefarm-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-devicefarm-1.42.0

%files         -n gem-aws-sdk-devicefarm-devel

%files         -n gem-aws-sdk-textract
%doc README.md
%ruby_gemspecdir/aws-sdk-textract-1.24.0.gemspec
%ruby_gemslibdir/aws-sdk-textract-1.24.0

%files         -n gem-aws-sdk-textract-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-textract-1.24.0

%files         -n gem-aws-sdk-textract-devel

%files         -n gem-aws-sdk-lex
%doc README.md
%ruby_gemspecdir/aws-sdk-lex-1.36.0.gemspec
%ruby_gemslibdir/aws-sdk-lex-1.36.0

%files         -n gem-aws-sdk-lex-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-lex-1.36.0

%files         -n gem-aws-sdk-lex-devel

%files         -n gem-aws-sdk-personalizeruntime
%doc README.md
%ruby_gemspecdir/aws-sdk-personalizeruntime-1.22.0.gemspec
%ruby_gemslibdir/aws-sdk-personalizeruntime-1.22.0

%files         -n gem-aws-sdk-personalizeruntime-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-personalizeruntime-1.22.0

%files         -n gem-aws-sdk-personalizeruntime-devel

%files         -n gem-aws-sdk-servicecatalog
%doc README.md
%ruby_gemspecdir/aws-sdk-servicecatalog-1.59.0.gemspec
%ruby_gemslibdir/aws-sdk-servicecatalog-1.59.0

%files         -n gem-aws-sdk-servicecatalog-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-servicecatalog-1.59.0

%files         -n gem-aws-sdk-servicecatalog-devel

%files         -n gem-aws-sdk-route53
%doc README.md
%ruby_gemspecdir/aws-sdk-route53-1.49.0.gemspec
%ruby_gemslibdir/aws-sdk-route53-1.49.0

%files         -n gem-aws-sdk-route53-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-route53-1.49.0

%files         -n gem-aws-sdk-route53-devel

%files         -n gem-aws-sdk-workmailmessageflow
%doc README.md
%ruby_gemspecdir/aws-sdk-workmailmessageflow-1.12.0.gemspec
%ruby_gemslibdir/aws-sdk-workmailmessageflow-1.12.0

%files         -n gem-aws-sdk-workmailmessageflow-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-workmailmessageflow-1.12.0

%files         -n gem-aws-sdk-workmailmessageflow-devel

%files         -n gem-aws-sdk-detective
%doc README.md
%ruby_gemspecdir/aws-sdk-detective-1.18.0.gemspec
%ruby_gemslibdir/aws-sdk-detective-1.18.0

%files         -n gem-aws-sdk-detective-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-detective-1.18.0

%files         -n gem-aws-sdk-detective-devel

%files         -n gem-aws-sdk-resourcegroupstaggingapi
%doc README.md
%ruby_gemspecdir/aws-sdk-resourcegroupstaggingapi-1.37.0.gemspec
%ruby_gemslibdir/aws-sdk-resourcegroupstaggingapi-1.37.0

%files         -n gem-aws-sdk-resourcegroupstaggingapi-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-resourcegroupstaggingapi-1.37.0

%files         -n gem-aws-sdk-resourcegroupstaggingapi-devel

%files         -n gem-aws-sdk-datapipeline
%doc README.md
%ruby_gemspecdir/aws-sdk-datapipeline-1.27.0.gemspec
%ruby_gemslibdir/aws-sdk-datapipeline-1.27.0

%files         -n gem-aws-sdk-datapipeline-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-datapipeline-1.27.0

%files         -n gem-aws-sdk-datapipeline-devel

%files         -n gem-aws-sdk-iotthingsgraph
%doc README.md
%ruby_gemspecdir/aws-sdk-iotthingsgraph-1.14.0.gemspec
%ruby_gemslibdir/aws-sdk-iotthingsgraph-1.14.0

%files         -n gem-aws-sdk-iotthingsgraph-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-iotthingsgraph-1.14.0

%files         -n gem-aws-sdk-iotthingsgraph-devel

%files         -n gem-aws-sdk-ecs
%doc README.md
%ruby_gemspecdir/aws-sdk-ecs-1.80.0.gemspec
%ruby_gemslibdir/aws-sdk-ecs-1.80.0

%files         -n gem-aws-sdk-ecs-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ecs-1.80.0

%files         -n gem-aws-sdk-ecs-devel

%files         -n gem-aws-sdk-mq
%doc README.md
%ruby_gemspecdir/aws-sdk-mq-1.36.0.gemspec
%ruby_gemslibdir/aws-sdk-mq-1.36.0

%files         -n gem-aws-sdk-mq-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-mq-1.36.0

%files         -n gem-aws-sdk-mq-devel

%files         -n gem-aws-sdk-ebs
%doc README.md
%ruby_gemspecdir/aws-sdk-ebs-1.13.0.gemspec
%ruby_gemslibdir/aws-sdk-ebs-1.13.0

%files         -n gem-aws-sdk-ebs-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ebs-1.13.0

%files         -n gem-aws-sdk-ebs-devel

%files         -n gem-aws-sdk-prometheusservice
%doc README.md
%ruby_gemspecdir/aws-sdk-prometheusservice-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-prometheusservice-1.3.0

%files         -n gem-aws-sdk-prometheusservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-prometheusservice-1.3.0

%files         -n gem-aws-sdk-prometheusservice-devel

%files         -n gem-aws-sdk-ssm
%doc README.md
%ruby_gemspecdir/aws-sdk-ssm-1.111.0.gemspec
%ruby_gemslibdir/aws-sdk-ssm-1.111.0

%files         -n gem-aws-sdk-ssm-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ssm-1.111.0

%files         -n gem-aws-sdk-ssm-devel

%files         -n gem-aws-sdk-workspaces
%doc README.md
%ruby_gemspecdir/aws-sdk-workspaces-1.53.0.gemspec
%ruby_gemslibdir/aws-sdk-workspaces-1.53.0

%files         -n gem-aws-sdk-workspaces-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-workspaces-1.53.0

%files         -n gem-aws-sdk-workspaces-devel

%files         -n gem-aws-sdk-schemas
%doc README.md
%ruby_gemspecdir/aws-sdk-schemas-1.12.0.gemspec
%ruby_gemslibdir/aws-sdk-schemas-1.12.0

%files         -n gem-aws-sdk-schemas-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-schemas-1.12.0

%files         -n gem-aws-sdk-schemas-devel

%files         -n gem-aws-sdk-licensemanager
%doc README.md
%ruby_gemspecdir/aws-sdk-licensemanager-1.27.0.gemspec
%ruby_gemslibdir/aws-sdk-licensemanager-1.27.0

%files         -n gem-aws-sdk-licensemanager-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-licensemanager-1.27.0

%files         -n gem-aws-sdk-licensemanager-devel

%files         -n gem-aws-sdk-ssooidc
%doc README.md
%ruby_gemspecdir/aws-sdk-ssooidc-1.10.0.gemspec
%ruby_gemslibdir/aws-sdk-ssooidc-1.10.0

%files         -n gem-aws-sdk-ssooidc-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ssooidc-1.10.0

%files         -n gem-aws-sdk-ssooidc-devel

%files         -n gem-aws-sdk-signer
%doc README.md
%ruby_gemspecdir/aws-sdk-signer-1.29.0.gemspec
%ruby_gemslibdir/aws-sdk-signer-1.29.0

%files         -n gem-aws-sdk-signer-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-signer-1.29.0

%files         -n gem-aws-sdk-signer-devel

%files         -n gem-aws-sdk-ses
%doc README.md
%ruby_gemspecdir/aws-sdk-ses-1.38.0.gemspec
%ruby_gemslibdir/aws-sdk-ses-1.38.0

%files         -n gem-aws-sdk-ses-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ses-1.38.0

%files         -n gem-aws-sdk-ses-devel

%files         -n gem-aws-sdk-inspector
%doc README.md
%ruby_gemspecdir/aws-sdk-inspector-1.34.0.gemspec
%ruby_gemslibdir/aws-sdk-inspector-1.34.0

%files         -n gem-aws-sdk-inspector-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-inspector-1.34.0

%files         -n gem-aws-sdk-inspector-devel

%files         -n gem-aws-sdk-chime
%doc README.md
%ruby_gemspecdir/aws-sdk-chime-1.46.0.gemspec
%ruby_gemslibdir/aws-sdk-chime-1.46.0

%files         -n gem-aws-sdk-chime-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-chime-1.46.0

%files         -n gem-aws-sdk-chime-devel

%files         -n gem-aws-sdk-elasticinference
%doc README.md
%ruby_gemspecdir/aws-sdk-elasticinference-1.12.0.gemspec
%ruby_gemslibdir/aws-sdk-elasticinference-1.12.0

%files         -n gem-aws-sdk-elasticinference-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-elasticinference-1.12.0

%files         -n gem-aws-sdk-elasticinference-devel

%files         -n gem-aws-sdk-autoscalingplans
%doc README.md
%ruby_gemspecdir/aws-sdk-autoscalingplans-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-autoscalingplans-1.31.0

%files         -n gem-aws-sdk-autoscalingplans-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-autoscalingplans-1.31.0

%files         -n gem-aws-sdk-autoscalingplans-devel

%files         -n gem-aws-sdk-cognitosync
%doc README.md
%ruby_gemspecdir/aws-sdk-cognitosync-1.27.0.gemspec
%ruby_gemslibdir/aws-sdk-cognitosync-1.27.0

%files         -n gem-aws-sdk-cognitosync-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-cognitosync-1.27.0

%files         -n gem-aws-sdk-cognitosync-devel

%files         -n gem-aws-sdk-backup
%doc README.md
%ruby_gemspecdir/aws-sdk-backup-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-backup-1.28.0

%files         -n gem-aws-sdk-backup-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-backup-1.28.0

%files         -n gem-aws-sdk-backup-devel

%files         -n gem-aws-sdk-elasticsearchservice
%doc README.md
%ruby_gemspecdir/aws-sdk-elasticsearchservice-1.52.0.gemspec
%ruby_gemslibdir/aws-sdk-elasticsearchservice-1.52.0

%files         -n gem-aws-sdk-elasticsearchservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-elasticsearchservice-1.52.0

%files         -n gem-aws-sdk-elasticsearchservice-devel

%files         -n gem-aws-sdk-imagebuilder
%doc README.md
%ruby_gemspecdir/aws-sdk-imagebuilder-1.22.0.gemspec
%ruby_gemslibdir/aws-sdk-imagebuilder-1.22.0

%files         -n gem-aws-sdk-imagebuilder-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-imagebuilder-1.22.0

%files         -n gem-aws-sdk-imagebuilder-devel

%files         -n gem-aws-sdk-lexruntimev2
%doc README.md
%ruby_gemspecdir/aws-sdk-lexruntimev2-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-lexruntimev2-1.2.0

%files         -n gem-aws-sdk-lexruntimev2-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-lexruntimev2-1.2.0

%files         -n gem-aws-sdk-lexruntimev2-devel

%files         -n gem-aws-sdk-finspacedata
%doc README.md
%ruby_gemspecdir/aws-sdk-finspacedata-1.1.0.gemspec
%ruby_gemslibdir/aws-sdk-finspacedata-1.1.0

%files         -n gem-aws-sdk-finspacedata-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-finspacedata-1.1.0

%files         -n gem-aws-sdk-finspacedata-devel

%files         -n gem-aws-sdk-apigatewaymanagementapi
%doc README.md
%ruby_gemspecdir/aws-sdk-apigatewaymanagementapi-1.21.0.gemspec
%ruby_gemslibdir/aws-sdk-apigatewaymanagementapi-1.21.0

%files         -n gem-aws-sdk-apigatewaymanagementapi-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-apigatewaymanagementapi-1.21.0

%files         -n gem-aws-sdk-apigatewaymanagementapi-devel

%files         -n gem-aws-sdk-redshift
%doc README.md
%ruby_gemspecdir/aws-sdk-redshift-1.62.0.gemspec
%ruby_gemslibdir/aws-sdk-redshift-1.62.0

%files         -n gem-aws-sdk-redshift-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-redshift-1.62.0

%files         -n gem-aws-sdk-redshift-devel

%files         -n gem-aws-sdk-kinesis
%doc README.md
%ruby_gemspecdir/aws-sdk-kinesis-1.32.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesis-1.32.0

%files         -n gem-aws-sdk-kinesis-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-kinesis-1.32.0

%files         -n gem-aws-sdk-kinesis-devel

%files         -n gem-aws-sdk-apprunner
%doc README.md
%ruby_gemspecdir/aws-sdk-apprunner-1.0.0.gemspec
%ruby_gemslibdir/aws-sdk-apprunner-1.0.0

%files         -n gem-aws-sdk-apprunner-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-apprunner-1.0.0

%files         -n gem-aws-sdk-apprunner-devel

%files         -n gem-aws-sdk-applicationautoscaling
%doc README.md
%ruby_gemspecdir/aws-sdk-applicationautoscaling-1.51.0.gemspec
%ruby_gemslibdir/aws-sdk-applicationautoscaling-1.51.0

%files         -n gem-aws-sdk-applicationautoscaling-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-applicationautoscaling-1.51.0

%files         -n gem-aws-sdk-applicationautoscaling-devel

%files         -n gem-aws-sdk-kinesisvideomedia
%doc README.md
%ruby_gemspecdir/aws-sdk-kinesisvideomedia-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesisvideomedia-1.28.0

%files         -n gem-aws-sdk-kinesisvideomedia-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-kinesisvideomedia-1.28.0

%files         -n gem-aws-sdk-kinesisvideomedia-devel

%files         -n gem-aws-sdk-appflow
%doc README.md
%ruby_gemspecdir/aws-sdk-appflow-1.10.0.gemspec
%ruby_gemslibdir/aws-sdk-appflow-1.10.0

%files         -n gem-aws-sdk-appflow-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-appflow-1.10.0

%files         -n gem-aws-sdk-appflow-devel

%files         -n gem-aws-sdk-greengrassv2
%doc README.md
%ruby_gemspecdir/aws-sdk-greengrassv2-1.3.0.gemspec
%ruby_gemslibdir/aws-sdk-greengrassv2-1.3.0

%files         -n gem-aws-sdk-greengrassv2-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-greengrassv2-1.3.0

%files         -n gem-aws-sdk-greengrassv2-devel

%files         -n gem-aws-sdk-health
%doc README.md
%ruby_gemspecdir/aws-sdk-health-1.35.0.gemspec
%ruby_gemslibdir/aws-sdk-health-1.35.0

%files         -n gem-aws-sdk-health-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-health-1.35.0

%files         -n gem-aws-sdk-health-devel

%files         -n gem-aws-sdk-migrationhub
%doc README.md
%ruby_gemspecdir/aws-sdk-migrationhub-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-migrationhub-1.31.0

%files         -n gem-aws-sdk-migrationhub-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-migrationhub-1.31.0

%files         -n gem-aws-sdk-migrationhub-devel

%files         -n gem-aws-sdk-costexplorer
%doc README.md
%ruby_gemspecdir/aws-sdk-costexplorer-1.62.0.gemspec
%ruby_gemslibdir/aws-sdk-costexplorer-1.62.0

%files         -n gem-aws-sdk-costexplorer-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-costexplorer-1.62.0

%files         -n gem-aws-sdk-costexplorer-devel

%files         -n gem-aws-sdk-ivs
%doc README.md
%ruby_gemspecdir/aws-sdk-ivs-1.9.0.gemspec
%ruby_gemslibdir/aws-sdk-ivs-1.9.0

%files         -n gem-aws-sdk-ivs-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ivs-1.9.0

%files         -n gem-aws-sdk-ivs-devel

%files         -n gem-aws-sdk-globalaccelerator
%doc README.md
%ruby_gemspecdir/aws-sdk-globalaccelerator-1.30.0.gemspec
%ruby_gemslibdir/aws-sdk-globalaccelerator-1.30.0

%files         -n gem-aws-sdk-globalaccelerator-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-globalaccelerator-1.30.0

%files         -n gem-aws-sdk-globalaccelerator-devel

%files         -n gem-aws-sdk-ssmincidents
%doc README.md
%ruby_gemspecdir/aws-sdk-ssmincidents-1.0.0.gemspec
%ruby_gemslibdir/aws-sdk-ssmincidents-1.0.0

%files         -n gem-aws-sdk-ssmincidents-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-ssmincidents-1.0.0

%files         -n gem-aws-sdk-ssmincidents-devel

%files         -n gem-aws-sdk-iotsitewise
%doc README.md
%ruby_gemspecdir/aws-sdk-iotsitewise-1.23.0.gemspec
%ruby_gemslibdir/aws-sdk-iotsitewise-1.23.0

%files         -n gem-aws-sdk-iotsitewise-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-iotsitewise-1.23.0

%files         -n gem-aws-sdk-iotsitewise-devel

%files         -n gem-aws-sdk-wafv2
%doc README.md
%ruby_gemspecdir/aws-sdk-wafv2-1.20.0.gemspec
%ruby_gemslibdir/aws-sdk-wafv2-1.20.0

%files         -n gem-aws-sdk-wafv2-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-wafv2-1.20.0

%files         -n gem-aws-sdk-wafv2-devel

%files         -n gem-aws-sdk-kinesisanalyticsv2
%doc README.md
%ruby_gemspecdir/aws-sdk-kinesisanalyticsv2-1.30.0.gemspec
%ruby_gemslibdir/aws-sdk-kinesisanalyticsv2-1.30.0

%files         -n gem-aws-sdk-kinesisanalyticsv2-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-kinesisanalyticsv2-1.30.0

%files         -n gem-aws-sdk-kinesisanalyticsv2-devel

%files         -n gem-aws-sdk-macie
%doc README.md
%ruby_gemspecdir/aws-sdk-macie-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-macie-1.28.0

%files         -n gem-aws-sdk-macie-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-macie-1.28.0

%files         -n gem-aws-sdk-macie-devel

%files         -n gem-aws-sdk-polly
%doc README.md
%ruby_gemspecdir/aws-sdk-polly-1.41.0.gemspec
%ruby_gemslibdir/aws-sdk-polly-1.41.0

%files         -n gem-aws-sdk-polly-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-polly-1.41.0

%files         -n gem-aws-sdk-polly-devel

%files         -n gem-aws-sdk-support
%doc README.md
%ruby_gemspecdir/aws-sdk-support-1.31.0.gemspec
%ruby_gemslibdir/aws-sdk-support-1.31.0

%files         -n gem-aws-sdk-support-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-support-1.31.0

%files         -n gem-aws-sdk-support-devel

%files         -n gem-aws-sdk-marketplaceentitlementservice
%doc README.md
%ruby_gemspecdir/aws-sdk-marketplaceentitlementservice-1.26.0.gemspec
%ruby_gemslibdir/aws-sdk-marketplaceentitlementservice-1.26.0

%files         -n gem-aws-sdk-marketplaceentitlementservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-marketplaceentitlementservice-1.26.0

%files         -n gem-aws-sdk-marketplaceentitlementservice-devel

%files         -n gem-aws-sdk-appstream
%doc README.md
%ruby_gemspecdir/aws-sdk-appstream-1.52.0.gemspec
%ruby_gemslibdir/aws-sdk-appstream-1.52.0

%files         -n gem-aws-sdk-appstream-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-appstream-1.52.0

%files         -n gem-aws-sdk-appstream-devel

%files         -n gem-aws-sdk-computeoptimizer
%doc README.md
%ruby_gemspecdir/aws-sdk-computeoptimizer-1.18.0.gemspec
%ruby_gemslibdir/aws-sdk-computeoptimizer-1.18.0

%files         -n gem-aws-sdk-computeoptimizer-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-computeoptimizer-1.18.0

%files         -n gem-aws-sdk-computeoptimizer-devel

%files         -n gem-aws-sdk-iot1clickprojects
%doc README.md
%ruby_gemspecdir/aws-sdk-iot1clickprojects-1.28.0.gemspec
%ruby_gemslibdir/aws-sdk-iot1clickprojects-1.28.0

%files         -n gem-aws-sdk-iot1clickprojects-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-iot1clickprojects-1.28.0

%files         -n gem-aws-sdk-iot1clickprojects-devel

%files         -n gem-aws-sdk-lightsail
%doc README.md
%ruby_gemspecdir/aws-sdk-lightsail-1.51.0.gemspec
%ruby_gemslibdir/aws-sdk-lightsail-1.51.0

%files         -n gem-aws-sdk-lightsail-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-lightsail-1.51.0

%files         -n gem-aws-sdk-lightsail-devel

%files         -n gem-aws-sdk-auditmanager
%doc README.md
%ruby_gemspecdir/aws-sdk-auditmanager-1.7.0.gemspec
%ruby_gemslibdir/aws-sdk-auditmanager-1.7.0

%files         -n gem-aws-sdk-auditmanager-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-auditmanager-1.7.0

%files         -n gem-aws-sdk-auditmanager-devel

%files         -n gem-aws-sdk-locationservice
%doc README.md
%ruby_gemspecdir/aws-sdk-locationservice-1.4.0.gemspec
%ruby_gemslibdir/aws-sdk-locationservice-1.4.0

%files         -n gem-aws-sdk-locationservice-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-locationservice-1.4.0

%files         -n gem-aws-sdk-locationservice-devel

%files         -n gem-aws-sdk-lakeformation
%doc README.md
%ruby_gemspecdir/aws-sdk-lakeformation-1.14.0.gemspec
%ruby_gemslibdir/aws-sdk-lakeformation-1.14.0

%files         -n gem-aws-sdk-lakeformation-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-lakeformation-1.14.0

%files         -n gem-aws-sdk-lakeformation-devel

%files         -n gem-aws-sdk-fms
%doc README.md
%ruby_gemspecdir/aws-sdk-fms-1.36.0.gemspec
%ruby_gemslibdir/aws-sdk-fms-1.36.0

%files         -n gem-aws-sdk-fms-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-fms-1.36.0

%files         -n gem-aws-sdk-fms-devel

%files         -n gem-aws-sdk-lambda
%doc README.md
%ruby_gemspecdir/aws-sdk-lambda-1.62.0.gemspec
%ruby_gemslibdir/aws-sdk-lambda-1.62.0

%files         -n gem-aws-sdk-lambda-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-lambda-1.62.0

%files         -n gem-aws-sdk-lambda-devel

%files         -n gem-aws-sdk-lambdapreview
%doc README.md
%ruby_gemspecdir/aws-sdk-lambdapreview-1.26.0.gemspec
%ruby_gemslibdir/aws-sdk-lambdapreview-1.26.0

%files         -n gem-aws-sdk-lambdapreview-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-lambdapreview-1.26.0

%files         -n gem-aws-sdk-lambdapreview-devel

%files         -n gem-aws-sdk-cloudformation
%doc README.md
%ruby_gemspecdir/aws-sdk-cloudformation-1.52.0.gemspec
%ruby_gemslibdir/aws-sdk-cloudformation-1.52.0

%files         -n gem-aws-sdk-cloudformation-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-cloudformation-1.52.0

%files         -n gem-aws-sdk-cloudformation-devel

%files         -n gem-aws-sdk-securityhub
%doc README.md
%ruby_gemspecdir/aws-sdk-securityhub-1.46.0.gemspec
%ruby_gemslibdir/aws-sdk-securityhub-1.46.0

%files         -n gem-aws-sdk-securityhub-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-securityhub-1.46.0

%files         -n gem-aws-sdk-securityhub-devel

%files         -n gem-aws-sdk-resources
%doc README.md
%ruby_gemspecdir/aws-sdk-resources-3.104.0.gemspec
%ruby_gemslibdir/aws-sdk-resources-3.104.0

%files         -n aws-v3-rb
%_bindir/aws-v3.rb

%files         -n gem-aws-sdk-resources-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-resources-3.104.0

%files         -n gem-aws-sdk-resources-devel

%files         -n gem-aws-sdk-sts
%doc README.md
%ruby_gemspecdir/aws-sdk-sts-1.2.0.gemspec
%ruby_gemslibdir/aws-sdk-sts-1.2.0

%files         -n gem-aws-sdk-sts-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-sts-1.2.0

%files         -n gem-aws-sdk-sts-devel

%files         -n gem-aws-sdk-elastictranscoder
%doc README.md
%ruby_gemspecdir/aws-sdk-elastictranscoder-1.29.0.gemspec
%ruby_gemslibdir/aws-sdk-elastictranscoder-1.29.0

%files         -n gem-aws-sdk-elastictranscoder-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-elastictranscoder-1.29.0

%files         -n gem-aws-sdk-elastictranscoder-devel

%files         -n gem-aws-sdk-applicationcostprofiler
%doc README.md
%ruby_gemspecdir/aws-sdk-applicationcostprofiler-1.0.0.gemspec
%ruby_gemslibdir/aws-sdk-applicationcostprofiler-1.0.0

%files         -n gem-aws-sdk-applicationcostprofiler-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-applicationcostprofiler-1.0.0

%files         -n gem-aws-sdk-applicationcostprofiler-devel

%files         -n gem-aws-sdk-connect
%doc README.md
%ruby_gemspecdir/aws-sdk-connect-1.44.0.gemspec
%ruby_gemslibdir/aws-sdk-connect-1.44.0

%files         -n gem-aws-sdk-connect-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-connect-1.44.0

%files         -n gem-aws-sdk-connect-devel

%files         -n gem-aws-sdk-groundstation
%doc README.md
%ruby_gemspecdir/aws-sdk-groundstation-1.18.0.gemspec
%ruby_gemslibdir/aws-sdk-groundstation-1.18.0

%files         -n gem-aws-sdk-groundstation-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-groundstation-1.18.0

%files         -n gem-aws-sdk-groundstation-devel

%files         -n gem-aws-sdk-greengrass
%doc README.md
%ruby_gemspecdir/aws-sdk-greengrass-1.40.0.gemspec
%ruby_gemslibdir/aws-sdk-greengrass-1.40.0

%files         -n gem-aws-sdk-greengrass-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-greengrass-1.40.0

%files         -n gem-aws-sdk-greengrass-devel

%files         -n gem-aws-sdk-sagemaker
%doc README.md
%ruby_gemspecdir/aws-sdk-sagemaker-1.88.0.gemspec
%ruby_gemslibdir/aws-sdk-sagemaker-1.88.0

%files         -n gem-aws-sdk-sagemaker-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-sagemaker-1.88.0

%files         -n gem-aws-sdk-sagemaker-devel

%files         -n gem-aws-sdk-amplify
%doc README.md
%ruby_gemspecdir/aws-sdk-amplify-1.29.0.gemspec
%ruby_gemslibdir/aws-sdk-amplify-1.29.0

%files         -n gem-aws-sdk-amplify-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-amplify-1.29.0

%files         -n gem-aws-sdk-amplify-devel

%files         -n gem-aws-sdk-pinpoint
%doc README.md
%ruby_gemspecdir/aws-sdk-pinpoint-1.53.0.gemspec
%ruby_gemslibdir/aws-sdk-pinpoint-1.53.0

%files         -n gem-aws-sdk-pinpoint-doc
%doc README.md
%ruby_gemsdocdir/aws-sdk-pinpoint-1.53.0

%files         -n gem-aws-sdk-pinpoint-devel


%changelog
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
