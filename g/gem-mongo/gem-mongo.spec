%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%def_disable   java
%define        gemname mongo

Name:          gem-mongo
Version:       2.20.1
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
BuildRequires: gem(yard) >= 0.9.34
BuildRequires: gem(ffi) >= 0
%if_enabled java
BuildRequires: gem(jruby-openssl) >= 0
%endif
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(aws-sdk-core) >= 3
BuildRequires: gem(aws-sdk-cloudwatchlogs) >= 0
BuildRequires: gem(aws-sdk-ec2) >= 0
BuildRequires: gem(aws-sdk-ecs) >= 0
BuildRequires: gem(aws-sdk-iam) >= 0
BuildRequires: gem(aws-sdk-sts) >= 0
BuildRequires: gem(paint) >= 0
BuildRequires: gem(yajl-ruby) >= 0
BuildRequires: gem(celluloid) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(ice_nine) >= 0
BuildRequires: gem(rubydns) >= 0
BuildRequires: gem(rspec-retry) >= 0
BuildRequires: gem(rfc) >= 0.2.0
BuildRequires: gem(fuubar) >= 0
BuildRequires: gem(timeout-interrupt) >= 0
BuildRequires: gem(dotenv) >= 0
BuildRequires: gem(childprocess) >= 0
BuildRequires: gem(ruby-prof) >= 0
BuildRequires: gem(erubi) >= 0
BuildRequires: gem(tilt) >= 0
BuildRequires: gem(solargraph) >= 0
BuildRequires: gem(bson) >= 4.14.1
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(activesupport) >= 7.1
BuildConflicts: gem(aws-sdk-core) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(rfc) >= 0.3
BuildConflicts: gem(bson) >= 6.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(bson) >= 4.14.1
Conflicts:     gem(bson) >= 6.0.0
Provides:      gem(mongo) = 2.20.1


%description
A Ruby driver for MongoDB


%package       -n mongo-console
Version:       2.20.1
Release:       alt1
Summary:       Ruby driver for MongoDB executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета mongo
Group:         Other
BuildArch:     noarch

Requires:      gem(mongo) = 2.20.1

%description   -n mongo-console
Ruby driver for MongoDB executable(s).

A Ruby driver for MongoDB

%description   -n mongo-console -l ru_RU.UTF-8
Исполнямка для самоцвета mongo.


%if_enabled    doc
%package       -n gem-mongo-doc
Version:       2.20.1
Release:       alt1
Summary:       Ruby driver for MongoDB documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mongo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mongo) = 2.20.1

%description   -n gem-mongo-doc
Ruby driver for MongoDB documentation files.

A Ruby driver for MongoDB

%description   -n gem-mongo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mongo.
%endif


%if_enabled    devel
%package       -n gem-mongo-devel
Version:       2.20.1
Release:       alt1
Summary:       Ruby driver for MongoDB development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mongo
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mongo) = 2.20.1
Requires:      gem(yard) >= 0.9.34
Requires:      gem(ffi) >= 0
%if_enabled java
Requires:      gem(jruby-openssl) >= 0
%endif
Requires:      gem(json) >= 0
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rake) >= 0
Requires:      gem(webrick) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(ruby-debug) >= 0
Requires:      gem(aws-sdk-core) >= 3
Requires:      gem(aws-sdk-cloudwatchlogs) >= 0
Requires:      gem(aws-sdk-ec2) >= 0
Requires:      gem(aws-sdk-ecs) >= 0
Requires:      gem(aws-sdk-iam) >= 0
Requires:      gem(aws-sdk-sts) >= 0
Requires:      gem(paint) >= 0
Requires:      gem(yajl-ruby) >= 0
Requires:      gem(celluloid) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(timecop) >= 0
Requires:      gem(ice_nine) >= 0
Requires:      gem(rubydns) >= 0
Requires:      gem(rspec-retry) >= 0
Requires:      gem(rfc) >= 0.2.0
Requires:      gem(fuubar) >= 0
Requires:      gem(timeout-interrupt) >= 0
Requires:      gem(concurrent-ruby) >= 0
Requires:      gem(dotenv) >= 0
Requires:      gem(childprocess) >= 0
Requires:      gem(ruby-prof) >= 0
Requires:      gem(erubi) >= 0
Requires:      gem(tilt) >= 0
Requires:      gem(solargraph) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(activesupport) >= 7.1
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(rfc) >= 0.3

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
%doc README.md spec/README.aws-auth.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n mongo-console
%doc README.md spec/README.aws-auth.md
%_bindir/mongo_console

%if_enabled    doc
%files         -n gem-mongo-doc
%doc README.md spec/README.aws-auth.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-mongo-devel
%doc README.md spec/README.aws-auth.md
%endif


%changelog
* Tue Jul 30 2024 Pavel Skrylev <majioa@altlinux.org> 2.20.1-alt1
- ^ 2.18.1 -> 2.20.1

* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 2.18.1-alt1
- + packaged gem with Ruby Policy 2.0
