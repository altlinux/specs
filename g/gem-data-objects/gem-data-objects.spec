%define        _unpackaged_files_terminate_build 0
%def_enable    check
%def_enable    doc
%def_enable   devel
%define        gemname data_objects

Name:          gem-data-objects
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/datamapper/do
Vcs:           https://github.com/datamapper/do.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libmysqlclient21-devel
BuildRequires: libsqlite3-devel
BuildRequires: libpq5-devel
BuildRequires: postgresql17-server-devel
%if_enabled check
BuildRequires: gem(addressable) >= 2.1
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 2.5
BuildRequires: gem(rake-compiler) >= 0.7
BuildRequires: gem(yard) >= 0.5
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_ignore_names gem-data-objects,do_h2,do_jdbc,do_derby,do_hsqldb,do_openedge,do_sqlserver
Requires:      gem(addressable) >= 2.1
Conflicts:     gem(addressable) >= 3
Provides:      gem(data_objects) = 0.10.17


%description
Provide a standard and simplified API for communicating with RDBMS from Ruby.


%package       -n gem-do-mysql
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications
Group:         Development/Ruby

Requires:      gem(data_objects) = 0.10.17
Provides:      gem(do_mysql) = 0.10.17

%description   -n gem-do-mysql
Implements the DataObjects API for MySQL


%if_enabled    doc
%package       -n gem-do-mysql-doc
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета do_mysql
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(do_mysql) = 0.10.17

%description   -n gem-do-mysql-doc
DataObjects basic API and shared driver specifications documentation
files.

Implements the DataObjects API for MySQL

%description   -n gem-do-mysql-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета do_mysql.
%endif


%if_enabled    devel
%package       -n gem-do-mysql-devel
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета do_mysql
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(do_mysql) = 0.10.17
Requires:      gem(rspec) >= 2.5
Requires:      gem(rake-compiler) >= 0.7
Requires:      gem(rake) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rake-compiler) >= 2

%description   -n gem-do-mysql-devel
DataObjects basic API and shared driver specifications development
package.

Implements the DataObjects API for MySQL

%description   -n gem-do-mysql-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета do_mysql.
%endif


%package       -n gem-do-oracle
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications
Group:         Development/Ruby

Requires:      gem(data_objects) = 0.10.17
Provides:      gem(do_oracle) = 0.10.17

%description   -n gem-do-oracle
Implements the DataObjects API for Oracle


%if_enabled    doc
%package       -n gem-do-oracle-doc
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета do_oracle
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(do_oracle) = 0.10.17

%description   -n gem-do-oracle-doc
DataObjects basic API and shared driver specifications documentation
files.

Implements the DataObjects API for Oracle

%description   -n gem-do-oracle-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета do_oracle.
%endif


%if_enabled    devel
%package       -n gem-do-oracle-devel
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета do_oracle
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(do_oracle) = 0.10.17
Requires:      gem(rspec) >= 2.5
Requires:      gem(rake-compiler) >= 0.7
Requires:      gem(rake) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rake-compiler) >= 2

%description   -n gem-do-oracle-devel
DataObjects basic API and shared driver specifications development
package.

Implements the DataObjects API for Oracle

%description   -n gem-do-oracle-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета do_oracle.
%endif


%package       -n gem-do-sqlite3
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications
Group:         Development/Ruby

Requires:      gem(data_objects) = 0.10.17
Provides:      gem(do_sqlite3) = 0.10.17

%description   -n gem-do-sqlite3
Implements the DataObjects API for Sqlite3


%if_enabled    doc
%package       -n gem-do-sqlite3-doc
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета do_sqlite3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(do_sqlite3) = 0.10.17

%description   -n gem-do-sqlite3-doc
DataObjects basic API and shared driver specifications documentation
files.

Implements the DataObjects API for Sqlite3

%description   -n gem-do-sqlite3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета do_sqlite3.
%endif


%if_enabled    devel
%package       -n gem-do-sqlite3-devel
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета do_sqlite3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(do_sqlite3) = 0.10.17
Requires:      gem(rspec) >= 2.5
Requires:      gem(rake-compiler) >= 0.7
Requires:      gem(rake) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rake-compiler) >= 2

%description   -n gem-do-sqlite3-devel
DataObjects basic API and shared driver specifications development
package.

Implements the DataObjects API for Sqlite3

%description   -n gem-do-sqlite3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета do_sqlite3.
%endif


%package       -n gem-do-postgres
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications
Group:         Development/Ruby

Requires:      gem(data_objects) = 0.10.17
Provides:      gem(do_postgres) = 0.10.17

%description   -n gem-do-postgres
Implements the DataObjects API for PostgreSQL


%if_enabled    doc
%package       -n gem-do-postgres-doc
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета do_postgres
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(do_postgres) = 0.10.17

%description   -n gem-do-postgres-doc
DataObjects basic API and shared driver specifications documentation
files.

Implements the DataObjects API for PostgreSQL

%description   -n gem-do-postgres-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета do_postgres.
%endif


%if_enabled    devel
%package       -n gem-do-postgres-devel
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета do_postgres
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(do_postgres) = 0.10.17
Requires:      gem(rspec) >= 2.5
Requires:      gem(rake-compiler) >= 0.7
Requires:      gem(rake) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rake-compiler) >= 2

%description   -n gem-do-postgres-devel
DataObjects basic API and shared driver specifications development
package.

Implements the DataObjects API for PostgreSQL

%description   -n gem-do-postgres-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета do_postgres.
%endif


%if_enabled    doc
%package       -n gem-data-objects-doc
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета data_objects
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(data_objects) = 0.10.17

%description   -n gem-data-objects-doc
DataObjects basic API and shared driver specifications documentation
files.

Provide a standard and simplified API for communicating with RDBMS from Ruby

%description   -n gem-data-objects-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета data_objects.
%endif


%if_enabled    devel
%package       -n gem-data-objects-devel
Version:       0.10.17
Release:       alt2
Summary:       DataObjects basic API and shared driver specifications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета data_objects
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(data_objects) = 0.10.17
Requires:      gem(rspec) >= 2.5
Requires:      gem(yard) >= 0.5
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-data-objects-devel
DataObjects basic API and shared driver specifications development
package.

Provide a standard and simplified API for communicating with RDBMS from Ruby

%description   -n gem-data-objects-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета data_objects.
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
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-do-mysql
%doc README.markdown
%ruby_gemspecdir/do_mysql-0.10.17.gemspec
%ruby_gemslibdir/do_mysql-0.10.17
%ruby_gemsextdir/do_mysql-0.10.17

%if_enabled    doc
%files         -n gem-do-mysql-doc
%doc README.markdown
%ruby_gemsdocdir/do_mysql-0.10.17
%endif

%if_enabled    devel
%files         -n gem-do-mysql-devel
%doc README.markdown
%ruby_includedir/do_mysql/
%endif

%files         -n gem-do-oracle
%doc README.markdown
%ruby_gemspecdir/do_oracle-0.10.17.gemspec
%ruby_gemslibdir/do_oracle-0.10.17
%ruby_gemsextdir/do_oracle-0.10.17

%if_enabled    doc
%files         -n gem-do-oracle-doc
%doc README.markdown
%ruby_gemsdocdir/do_oracle-0.10.17
%endif

%if_enabled    devel
%files         -n gem-do-oracle-devel
%doc README.markdown
%endif

%files         -n gem-do-sqlite3
%doc README.markdown
%ruby_gemspecdir/do_sqlite3-0.10.17.gemspec
%ruby_gemslibdir/do_sqlite3-0.10.17
%ruby_gemsextdir/do_sqlite3-0.10.17

%if_enabled    doc
%files         -n gem-do-sqlite3-doc
%doc README.markdown
%ruby_gemsdocdir/do_sqlite3-0.10.17
%endif

%if_enabled    devel
%files         -n gem-do-sqlite3-devel
%doc README.markdown
%ruby_includedir/do_sqlite3/
%endif

%files         -n gem-do-postgres
%doc README.markdown
%ruby_gemspecdir/do_postgres-0.10.17.gemspec
%ruby_gemslibdir/do_postgres-0.10.17
%ruby_gemsextdir/do_postgres-0.10.17

%if_enabled    doc
%files         -n gem-do-postgres-doc
%doc README.markdown
%ruby_gemsdocdir/do_postgres-0.10.17
%endif

%if_enabled    devel
%files         -n gem-do-postgres-devel
%doc README.markdown
%ruby_includedir/do_postgres/
%endif

%if_enabled    doc
%files         -n gem-data-objects-doc
%doc README.markdown
%ruby_gemsdocdir/data_objects-0.10.17
%endif

%if_enabled    devel
%files         -n gem-data-objects-devel
%doc README.markdown
%endif


%changelog
* Wed Nov 06 2024 Pavel Skrylev <majioa@altlinux.org> 0.10.17-alt2
- ! fixed builddeps and spec structure
- ! rebased

* Wed May 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.10.17-alt1
- + packaged gem with Ruby Policy 2.0
