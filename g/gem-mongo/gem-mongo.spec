%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname mongo

Name:          gem-mongo
Version:       2.21.0
Release:       alt1
Summary:       Ruby driver for MongoDB
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://mongodb.com/docs/ruby-driver/
Vcs:           https://github.com/mongodb/mongo-ruby-driver.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(aws-sdk-cloudwatchlogs) >= 0
BuildRequires: gem(aws-sdk-core) >= 3
BuildRequires: gem(aws-sdk-ec2) >= 0
BuildRequires: gem(aws-sdk-ecs) >= 0
BuildRequires: gem(aws-sdk-iam) >= 0
BuildRequires: gem(aws-sdk-sts) >= 0
BuildRequires: gem(base64) >= 0
BuildRequires: gem(bson) >= 4.14.1
BuildRequires: gem(erubi) >= 0
BuildRequires: gem(ffi) >= 0
BuildRequires: gem(httparty) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(paint) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(tilt) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(yard) >= 0.9.34
BuildConflicts: gem(activesupport) >= 7.1
BuildConflicts: gem(aws-sdk-core) >= 4
BuildConflicts: gem(bson) >= 6
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-rake >= 0.6.0,rubocop-rake < 1
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      ruby >= 2.7
Requires:      gem(base64) >= 0
Requires:      gem(bson) >= 4.14.1
Conflicts:     gem(bson) >= 6
Provides:      mongo = %EVR
Provides:      gem(mongo) = 2.21.0

%description
A Ruby driver for MongoDB


%package       -n mongo-console
Version:       2.21.0
Release:       alt1
Summary:       Ruby driver for MongoDB executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета mongo
Group:         Other
BuildArch:     noarch

Requires:      gem(mongo) = 2.21.0

%description   -n mongo-console
Ruby driver for MongoDB executable(s).

A Ruby driver for MongoDB

%description   -n mongo-console -l ru_RU.UTF-8
Исполнямка для самоцвета mongo.


%if_enabled    doc
%package       -n gem-mongo-doc
Version:       2.21.0
Release:       alt1
Summary:       Ruby driver for MongoDB documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mongo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mongo) = 2.21.0

%description   -n gem-mongo-doc
Ruby driver for MongoDB documentation files.

A Ruby driver for MongoDB

%description   -n gem-mongo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mongo.
%endif


%if_enabled    devel
%package       -n gem-mongo-devel
Version:       2.21.0
Release:       alt1
Summary:       Ruby driver for MongoDB development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mongo
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mongo) = 2.21.0
Requires:      gem(aws-sdk-cloudwatchlogs) >= 0
Requires:      gem(aws-sdk-core) >= 3
Requires:      gem(aws-sdk-ec2) >= 0
Requires:      gem(aws-sdk-ecs) >= 0
Requires:      gem(aws-sdk-iam) >= 0
Requires:      gem(aws-sdk-sts) >= 0
Requires:      gem(erubi) >= 0
Requires:      gem(paint) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(tilt) >= 0
Requires:      gem(webrick) >= 0
Conflicts:     gem(activesupport) >= 7.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 3

%description   -n gem-mongo-devel
Ruby driver for MongoDB development package.

A Ruby driver for MongoDB

%description   -n gem-mongo-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mongo.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CONTRIBUTING.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n mongo-console
%doc CONTRIBUTING.md LICENSE README.md
%_bindir/mongo_console

%if_enabled    doc
%files         -n gem-mongo-doc
%doc CONTRIBUTING.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-mongo-devel
%doc CONTRIBUTING.md LICENSE README.md
%endif


%changelog
* Tue Jan 21 2025 Pavel Skrylev <majioa@altlinux.org> 2.21.0-alt1
- ^ 2.20.1 -> 2.21.0

* Tue Jul 30 2024 Pavel Skrylev <majioa@altlinux.org> 2.20.1-alt1
- ^ 2.18.1 -> 2.20.1

* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 2.18.1-alt1
- + packaged gem with Ruby Policy 2.0
