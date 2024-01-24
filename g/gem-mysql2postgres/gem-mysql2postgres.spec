%define        _unpackaged_files_terminate_build 1
%define        gemname mysql2postgres

Name:          gem-mysql2postgres
Version:       0.4.1
Release:       alt1
Summary:       MySQL to PostgreSQL Data Translation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/AlphaNodes/mysql2postgres
Vcs:           https://github.com/alphanodes/mysql2postgres.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(pg) >= 1.2.2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(ruby-mysql) >= 3.0
BuildConflicts: gem(pg) >= 2
BuildConflicts: gem(ruby-mysql) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency pg >= 1.3.5,pg < 2
%ruby_use_gem_dependency ruby-mysql >= 4.1.0,ruby-mysql < 5
Requires:      gem(pg) >= 1.2.2
Requires:      gem(rake) >= 0
Requires:      gem(ruby-mysql) >= 3.0
Conflicts:     gem(pg) >= 2
Conflicts:     gem(ruby-mysql) >= 5
Provides:      gem(mysql2postgres) = 0.4.1


%description
Translates MySQL -> PostgreSQL. Convert MySQL database to PostgreSQL database.


%package       -n mysql2postgres
Version:       0.4.1
Release:       alt1
Summary:       MySQL to PostgreSQL Data Translation executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета mysql2postgres
Group:         Other
BuildArch:     noarch

Requires:      gem(mysql2postgres) = 0.4.1

%description   -n mysql2postgres
MySQL to PostgreSQL Data Translation executable(s).

Translates MySQL -> PostgreSQL. Convert MySQL database to PostgreSQL database.

%description   -n mysql2postgres -l ru_RU.UTF-8
Исполнямка для самоцвета mysql2postgres.


%package       -n gem-mysql2postgres-doc
Version:       0.4.1
Release:       alt1
Summary:       MySQL to PostgreSQL Data Translation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mysql2postgres
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mysql2postgres) = 0.4.1

%description   -n gem-mysql2postgres-doc
MySQL to PostgreSQL Data Translation documentation files.

Translates MySQL -> PostgreSQL. Convert MySQL database to PostgreSQL database.

%description   -n gem-mysql2postgres-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mysql2postgres.


%package       -n gem-mysql2postgres-devel
Version:       0.4.1
Release:       alt1
Summary:       MySQL to PostgreSQL Data Translation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mysql2postgres
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mysql2postgres) = 0.4.1

%description   -n gem-mysql2postgres-devel
MySQL to PostgreSQL Data Translation development package.

Translates MySQL -> PostgreSQL. Convert MySQL database to PostgreSQL database.

%description   -n gem-mysql2postgres-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mysql2postgres.


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
%ruby_gemspec
%ruby_gemlibdir

%files         -n mysql2postgres
%doc README.md
%_bindir/mysql2postgres

%files         -n gem-mysql2postgres-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mysql2postgres-devel
%doc README.md


%changelog
* Wed Jan 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.4.1-alt1
- + packaged gem with Ruby Policy 2.0
