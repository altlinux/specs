%define        _unpackaged_files_terminate_build 1
%define        gemname sequel

Name:          gem-sequel
Version:       5.66.0
Release:       alt1
Summary:       Sequel is a simple, flexible, and powerful SQL database access toolkit for Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://sequel.jeremyevans.net
Vcs:           https://github.com/jeremyevans/sequel.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 5.7.0
BuildRequires: gem(minitest-hooks) >= 0
BuildRequires: gem(minitest-global_expectations) >= 0
BuildRequires: gem(tzinfo) >= 0
BuildRequires: gem(activemodel) >= 0
BuildRequires: gem(nokogiri) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-sequel < %EVR
Provides:      ruby-sequel = %EVR
Provides:      gem(sequel) = 5.66.0


%description
Sequel is a simple, flexible, and powerful SQL database access toolkit for
Ruby.

- Sequel provides thread safety, connection pooling and a concise DSL for
  constructing SQL queries and table schemas.
- Sequel includes a comprehensive ORM layer for mapping records to Ruby objects
  and handling associated records.
- Sequel supports advanced database features such as prepared statements, bound
  variables, savepoints, two-phase commit, transaction isolation, master/slave
  configurations, and database sharding.
- Sequel currently has adapters for ADO, Amalgalite, IBM_DB, JDBC, MySQL,
  Mysql2, ODBC, Oracle, PostgreSQL, SQLAnywhere, SQLite3, and TinyTDS.


%package       -n sequel
Version:       5.66.0
Release:       alt1
Summary:       Sequel is a simple, flexible, and powerful SQL database access toolkit for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sequel
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sequel) = 5.66.0

%description   -n sequel
Sequel is a simple, flexible, and powerful SQL database access toolkit for Ruby
executable(s).

%description   -n sequel -l ru_RU.UTF-8
Исполнямка для самоцвета sequel.


%package       -n gem-sequel-doc
Version:       5.66.0
Release:       alt1
Summary:       Sequel is a simple, flexible, and powerful SQL database access toolkit for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sequel
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sequel) = 5.66.0

%description   -n gem-sequel-doc
Sequel is a simple, flexible, and powerful SQL database access toolkit for Ruby
documentation files.

%description   -n gem-sequel-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sequel.


%package       -n gem-sequel-devel
Version:       5.66.0
Release:       alt1
Summary:       Sequel is a simple, flexible, and powerful SQL database access toolkit for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sequel
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sequel) = 5.66.0
Requires:      gem(minitest) >= 5.7.0
Requires:      gem(minitest-hooks) >= 0
Requires:      gem(minitest-global_expectations) >= 0
Requires:      gem(tzinfo) >= 0
Requires:      gem(activemodel) >= 0
Requires:      gem(nokogiri) >= 0

%description   -n gem-sequel-devel
Sequel is a simple, flexible, and powerful SQL database access toolkit for Ruby
development package.

%description   -n gem-sequel-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sequel.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n sequel
%doc README.rdoc
%_bindir/sequel

%files         -n gem-sequel-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-sequel-devel
%doc README.rdoc


%changelog
* Sun Mar 26 2023 Pavel Skrylev <majioa@altlinux.org> 5.66.0-alt1
- ^ 5.30.0 -> 5.66.0

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 5.30.0-alt1
- updated (^) 5.24.0 -> 5.30.0

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 5.24.0-alt1
- updated (^) 5.19.0 -> 5.24.0
- fixed (!) spec

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 5.19.0-alt1
- used (>) Ruby Policy 2.0
- updated (^) 5.5.0 -> 5.19.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Feb 14 2018 Alexey Shabalin <shaba@altlinux.ru> 5.5.0-alt1
- + 5.5.0

* Sun Sep 10 2017 Andrey Cherepanov <cas@altlinux.org> 4.49.0-alt2.1
- Rebuild with Ruby 2.4.1

* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 4.49.0-alt2
-  Revert "do not require rubygems"

* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 4.49.0-alt1
- Initial build in Sisyphus
