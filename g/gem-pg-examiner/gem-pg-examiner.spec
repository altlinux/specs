%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname pg_examiner

Name:          gem-pg-examiner
Version:       0.5.2
Release:       alt1
Summary:       Parse the schemas of Postgres databases in detail
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/chanks/pg_examiner
Vcs:           https://github.com/chanks/pg_examiner.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(pg) >= 0
BuildRequires: gem(bundler) >= 1.6
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(pry) >= 0
BuildConflicts: gem(bundler) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Provides:      gem(pg_examiner) = 0.5.2


%description
Examine and compare the tables, columns, constraints and other information that
makes up the schema of a PG database.


%if_enabled    doc
%package       -n gem-pg-examiner-doc
Version:       0.5.2
Release:       alt1
Summary:       Parse the schemas of Postgres databases in detail documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pg_examiner
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pg_examiner) = 0.5.2

%description   -n gem-pg-examiner-doc
Parse the schemas of Postgres databases in detail documentation files.

Examine and compare the tables, columns, constraints and other information that
makes up the schema of a PG database

%description   -n gem-pg-examiner-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pg_examiner.
%endif


%if_enabled    devel
%package       -n gem-pg-examiner-devel
Version:       0.5.2
Release:       alt1
Summary:       Parse the schemas of Postgres databases in detail development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pg_examiner
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pg_examiner) = 0.5.2
Requires:      gem(pg) >= 0
Requires:      gem(bundler) >= 1.6
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(pry) >= 0
Conflicts:     gem(bundler) >= 3

%description   -n gem-pg-examiner-devel
Parse the schemas of Postgres databases in detail development package.

Examine and compare the tables, columns, constraints and other information that
makes up the schema of a PG database

%description   -n gem-pg-examiner-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pg_examiner.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-pg-examiner-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-pg-examiner-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 0.5.2-alt1
- + packaged gem with Ruby Policy 2.0
