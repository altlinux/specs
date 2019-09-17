%define        pkgname sequel

Name:          ruby-%pkgname
Version:       5.24.0
Release:       alt1
Summary:       Sequel is a simple, flexible, and powerful SQL database access toolkit for Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://sequel.jeremyevans.net
%vcs           https://github.com/jeremyevans/sequel.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Sequel is a simple, flexible, and powerful SQL database access toolkit for Ruby.

- Sequel provides thread safety, connection pooling
  and a concise DSL for constructing SQL queries and table schemas.
- Sequel includes a comprehensive ORM layer for mapping records
  to Ruby objects and handling associated records.
- Sequel supports advanced database features such as prepared statements,
  bound variables, savepoints, two-phase commit, transaction isolation,
  master/slave configurations, and database sharding.
- Sequel currently has adapters for ADO, Amalgalite, IBM_DB, JDBC, MySQL,
  Mysql2, ODBC, Oracle, PostgreSQL, SQLAnywhere, SQLite3, and TinyTDS.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname
%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir


%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 5.24.0-alt1
- ^ v5.24.0
- ! spec

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 5.19.0-alt1
- ^ Ruby Policy 2.0
- ^ v5.19.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Feb 14 2018 Alexey Shabalin <shaba@altlinux.ru> 5.5.0-alt1
- 5.5.0

* Sun Sep 10 2017 Andrey Cherepanov <cas@altlinux.org> 4.49.0-alt2.1
- Rebuild with Ruby 2.4.1

* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 4.49.0-alt2
-  Revert "do not require rubygems"

* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 4.49.0-alt1
- Initial build in Sisyphus
