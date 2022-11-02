%define        gemname mongo

Name:          gem-mongo
Version:       2.18.1
Release:       alt1
Summary:       Ruby driver for MongoDB
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://mongodb.com/docs/ruby-driver/
Vcs:           https://github.com/mongodb/mongo-ruby-driver.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(yard) >= 0
BuildRequires: gem(ffi) >= 0
BuildRequires: gem(rspec-core) >= 3.9 gem(rspec-core) < 4
BuildRequires: gem(activesupport) < 7.1
BuildRequires: gem(rake) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(aws-sdk-core) >= 3 gem(aws-sdk-core) < 4
BuildRequires: gem(aws-sdk-cloudwatchlogs) >= 0
BuildRequires: gem(aws-sdk-ec2) >= 0
BuildRequires: gem(aws-sdk-ecs) >= 0
BuildRequires: gem(aws-sdk-iam) >= 0
BuildRequires: gem(paint) >= 0
BuildRequires: gem(yajl-ruby) >= 0
BuildRequires: gem(celluloid) >= 0
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(ice_nine) >= 0
BuildRequires: gem(rubydns) >= 0
BuildRequires: gem(rspec-retry) >= 0
BuildRequires: gem(rspec-expectations) >= 3.9 gem(rspec-expectations) < 4
BuildRequires: gem(rspec-mocks-diag) >= 3.9 gem(rspec-mocks-diag) < 4
BuildRequires: gem(rfc) >= 0.2.0 gem(rfc) < 0.3
BuildRequires: gem(fuubar) >= 0
BuildRequires: gem(timeout-interrupt) >= 0
BuildRequires: gem(dotenv) >= 0
BuildRequires: gem(childprocess) >= 0
BuildRequires: gem(ruby-prof) >= 0
BuildRequires: gem(erubi) >= 0
BuildRequires: gem(tilt) >= 0
BuildRequires: gem(bson) >= 4.14.1 gem(bson) < 5.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(bson) >= 4.14.1 gem(bson) < 5.0.0
Provides:      gem(mongo) = 2.18.1


%description
A Ruby driver for MongoDB


%package       -n mongo-console
Version:       2.18.1
Release:       alt1
Summary:       Ruby driver for MongoDB executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета mongo
Group:         Other
BuildArch:     noarch

Requires:      gem(mongo) = 2.18.1

%description   -n mongo-console
Ruby driver for MongoDB executable(s).

A Ruby driver for MongoDB

%description   -n mongo-console -l ru_RU.UTF-8
Исполнямка для самоцвета mongo.


%package       -n gem-mongo-doc
Version:       2.18.1
Release:       alt1
Summary:       Ruby driver for MongoDB documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mongo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mongo) = 2.18.1

%description   -n gem-mongo-doc
Ruby driver for MongoDB documentation files.

A Ruby driver for MongoDB

%description   -n gem-mongo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mongo.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md spec/README.aws-auth.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n mongo-console
%doc README.md spec/README.aws-auth.md
%_bindir/mongo_console

%files         -n gem-mongo-doc
%doc README.md spec/README.aws-auth.md
%ruby_gemdocdir


%changelog
* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 2.18.1-alt1
- + packaged gem with Ruby Policy 2.0
