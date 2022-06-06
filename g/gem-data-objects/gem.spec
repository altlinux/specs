%define        gemname data_objects

Name:          gem-data-objects
Version:       0.10.17
Release:       alt1
Summary:       DataObjects basic API and shared driver specifications
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/datamapper/do
Vcs:           https://github.com/datamapper/do.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(addressable) >= 2.1 gem(addressable) < 3
BuildRequires: gem(rspec) >= 2.5 gem(rspec) < 4
BuildRequires: gem(yard) >= 0.5 gem(yard) < 1
BuildRequires: gem(rake-compiler) >= 0.7 gem(rake-compiler) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Requires:      gem(addressable) >= 2.1 gem(addressable) < 3
Provides:      gem(data_objects) = 0.10.17

%description
Provide a standard and simplified API for communicating with RDBMS from Ruby.


%package       -n data-objects-doc
Version:       0.10.17
Release:       alt1
Summary:       DataObjects basic API and shared driver specifications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета data_objects
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(data_objects) = 0.10.17

%description   -n data-objects-doc
DataObjects basic API and shared driver specifications documentation
files.

Provide a standard and simplified API for communicating with RDBMS from Ruby.

%description   -n data-objects-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета data_objects.


%package       -n data-objects-devel
Version:       0.10.17
Release:       alt1
Summary:       DataObjects basic API and shared driver specifications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета data_objects
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(data_objects) = 0.10.17
Requires:      gem(rspec) >= 2.5 gem(rspec) < 4
Requires:      gem(yard) >= 0.5 gem(yard) < 1

%description   -n data-objects-devel
DataObjects basic API and shared driver specifications development
package.

Provide a standard and simplified API for communicating with RDBMS from Ruby.

%description   -n data-objects-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета data_objects.


%package       -n gem-do-mysql
Version:       0.10.17
Release:       alt1
Summary:       DataObjects MySQL Driver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(data_objects) = 0.10.17
Provides:      gem(do_mysql) = 0.10.17

%description   -n gem-do-mysql
Implements the DataObjects API for MySQL


%package       -n do-mysql-doc
Version:       0.10.17
Release:       alt1
Summary:       DataObjects MySQL Driver documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета do_mysql
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(do_mysql) = 0.10.17

%description   -n do-mysql-doc
DataObjects MySQL Driver documentation files.

Implements the DataObjects API for MySQL

%description   -n do-mysql-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета do_mysql.


%package       -n do-mysql-devel
Version:       0.10.17
Release:       alt1
Summary:       DataObjects MySQL Driver development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета do_mysql
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(do_mysql) = 0.10.17
Requires:      gem(rspec) >= 2.5 gem(rspec) < 4
Requires:      gem(rake-compiler) >= 0.7 gem(rake-compiler) < 2

%description   -n do-mysql-devel
DataObjects MySQL Driver development package.

Implements the DataObjects API for MySQL

%description   -n do-mysql-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета do_mysql.


%package       -n gem-do-oracle
Version:       0.10.17
Release:       alt1
Summary:       DataObjects Oracle Driver
Group:         Development/Ruby

Requires:      gem(data_objects) = 0.10.17
Provides:      gem(do_oracle) = 0.10.17

%description   -n gem-do-oracle
Implements the DataObjects API for Oracle


%package       -n do-oracle-doc
Version:       0.10.17
Release:       alt1
Summary:       DataObjects Oracle Driver documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета do_oracle
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(do_oracle) = 0.10.17

%description   -n do-oracle-doc
DataObjects Oracle Driver documentation files.

Implements the DataObjects API for Oracle

%description   -n do-oracle-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета do_oracle.


%package       -n do-oracle-devel
Version:       0.10.17
Release:       alt1
Summary:       DataObjects Oracle Driver development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета do_oracle
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(do_oracle) = 0.10.17
Requires:      gem(rspec) >= 2.5 gem(rspec) < 4
Requires:      gem(rake-compiler) >= 0.7 gem(rake-compiler) < 2

%description   -n do-oracle-devel
DataObjects Oracle Driver development package.

Implements the DataObjects API for Oracle

%description   -n do-oracle-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета do_oracle.


%package       -n gem-do-postgres
Version:       0.10.17
Release:       alt1
Summary:       DataObjects PostgreSQL Driver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(data_objects) = 0.10.17
Provides:      gem(do_postgres) = 0.10.17

%description   -n gem-do-postgres
Implements the DataObjects API for PostgreSQL


%package       -n do-postgres-doc
Version:       0.10.17
Release:       alt1
Summary:       DataObjects PostgreSQL Driver documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета do_postgres
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(do_postgres) = 0.10.17

%description   -n do-postgres-doc
DataObjects PostgreSQL Driver documentation files.

Implements the DataObjects API for PostgreSQL

%description   -n do-postgres-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета do_postgres.


%package       -n do-postgres-devel
Version:       0.10.17
Release:       alt1
Summary:       DataObjects PostgreSQL Driver development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета do_postgres
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(do_postgres) = 0.10.17
Requires:      gem(rspec) >= 2.5 gem(rspec) < 4
Requires:      gem(rake-compiler) >= 0.7 gem(rake-compiler) < 2

%description   -n do-postgres-devel
DataObjects PostgreSQL Driver development package.

Implements the DataObjects API for PostgreSQL

%description   -n do-postgres-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета do_postgres.


%package       -n gem-do-sqlite3
Version:       0.10.17
Release:       alt1
Summary:       DataObjects Sqlite3 Driver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(data_objects) = 0.10.17
Provides:      gem(do_sqlite3) = 0.10.17

%description   -n gem-do-sqlite3
Implements the DataObjects API for Sqlite3


%package       -n do-sqlite3-doc
Version:       0.10.17
Release:       alt1
Summary:       DataObjects Sqlite3 Driver documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета do_sqlite3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(do_sqlite3) = 0.10.17

%description   -n do-sqlite3-doc
DataObjects Sqlite3 Driver documentation files.

Implements the DataObjects API for Sqlite3

%description   -n do-sqlite3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета do_sqlite3.


%package       -n do-sqlite3-devel
Version:       0.10.17
Release:       alt1
Summary:       DataObjects Sqlite3 Driver development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета do_sqlite3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(do_sqlite3) = 0.10.17
Requires:      gem(rspec) >= 2.5 gem(rspec) < 4
Requires:      gem(rake-compiler) >= 0.7 gem(rake-compiler) < 2

%description   -n do-sqlite3-devel
DataObjects Sqlite3 Driver development package.

Implements the DataObjects API for Sqlite3

%description   -n do-sqlite3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета do_sqlite3.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n data-objects-doc
%doc README.markdown
%ruby_gemsdocdir/data_objects-0.10.17

%files         -n data-objects-devel
%doc README.markdown

%files         -n gem-do-mysql
%doc README.markdown
%ruby_gemspecdir/do_mysql-0.10.17.gemspec
%ruby_gemslibdir/do_mysql-0.10.17

%files         -n do-mysql-doc
%doc README.markdown
%ruby_gemsdocdir/do_mysql-0.10.17

%files         -n do-mysql-devel
%doc README.markdown
%ruby_includedir/*

%files         -n gem-do-oracle
%doc README.markdown
%ruby_gemspecdir/do_oracle-0.10.17.gemspec
%ruby_gemslibdir/do_oracle-0.10.17
%ruby_gemsextdir/do_oracle-0.10.17

%files         -n do-oracle-doc
%doc README.markdown
%ruby_gemsdocdir/do_oracle-0.10.17

%files         -n do-oracle-devel
%doc README.markdown

%files         -n gem-do-postgres
%doc README.markdown
%ruby_gemspecdir/do_postgres-0.10.17.gemspec
%ruby_gemslibdir/do_postgres-0.10.17

%files         -n do-postgres-doc
%doc README.markdown
%ruby_gemsdocdir/do_postgres-0.10.17

%files         -n do-postgres-devel
%doc README.markdown
%ruby_includedir/*

%files         -n gem-do-sqlite3
%doc README.markdown
%ruby_gemspecdir/do_sqlite3-0.10.17.gemspec
%ruby_gemslibdir/do_sqlite3-0.10.17

%files         -n do-sqlite3-doc
%doc README.markdown
%ruby_gemsdocdir/do_sqlite3-0.10.17

%files         -n do-sqlite3-devel
%doc README.markdown
%ruby_includedir/*


%changelog
* Wed May 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.10.17-alt1
- + packaged gem with Ruby Policy 2.0
