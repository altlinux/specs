%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname que

Name:          gem-que
Version:       2.2.1
Release:       alt1
Summary:       A PostgreSQL-based Job Queue
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/que-rb/que
Vcs:           https://github.com/que-rb/que.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(activerecord) >= 6.0
BuildRequires: gem(activejob) >= 6.0
BuildRequires: gem(sequel) >= 0
BuildRequires: gem(connection_pool) >= 0
BuildRequires: gem(pond) >= 0
BuildRequires: gem(pg) >= 0
BuildRequires: gem(minitest) >= 5.10.1
BuildRequires: gem(minitest-profile) >= 0.0.2
BuildRequires: gem(minitest-hooks) >= 1.4.0
BuildRequires: gem(minitest-fail-fast) >= 0.1.0
BuildRequires: gem(m) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pg_examiner) >= 0.5.2
BuildRequires: gem(bundler) >= 0
BuildConflicts: gem(activerecord) >= 7
BuildConflicts: gem(activejob) >= 7
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(pg_examiner) >= 0.6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency minitest-profile >= 0.0.2,minitest-profile < 1
%ruby_use_gem_dependency minitest-hooks >= 1.5.0,minitest-hooks < 2
%ruby_use_gem_dependency minitest-fail-fast >= 0.1.0,minitest-fail-fast < 1
Provides:      gem(que) = 2.2.1

%description
A job queue that uses PostgreSQL's advisory locks for speed and reliability.


%package       -n que
Version:       2.2.1
Release:       alt1
Summary:       A PostgreSQL-based Job Queue executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета que
Group:         Other
BuildArch:     noarch

Requires:      gem(que) = 2.2.1

%description   -n que
A PostgreSQL-based Job Queue executable(s).

A job queue that uses PostgreSQL's advisory locks for speed and reliability.

%description   -n que -l ru_RU.UTF-8
Исполнямка для самоцвета que.


%if_enabled    doc
%package       -n gem-que-doc
Version:       2.2.1
Release:       alt1
Summary:       A PostgreSQL-based Job Queue documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета que
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(que) = 2.2.1

%description   -n gem-que-doc
A PostgreSQL-based Job Queue documentation files.

A job queue that uses PostgreSQL's advisory locks for speed and reliability.

%description   -n gem-que-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета que.
%endif


%if_enabled    devel
%package       -n gem-que-devel
Version:       2.2.1
Release:       alt1
Summary:       A PostgreSQL-based Job Queue development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета que
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(que) = 2.2.1
Requires:      gem(rake) >= 0
Requires:      gem(activerecord) >= 6.0
Requires:      gem(activejob) >= 6.0
Requires:      gem(sequel) >= 0
Requires:      gem(connection_pool) >= 0
Requires:      gem(pond) >= 0
Requires:      gem(pg) >= 0
Requires:      gem(minitest) >= 5.10.1
Requires:      gem(minitest-profile) >= 0.0.2
Requires:      gem(minitest-hooks) >= 1.4.0
Requires:      gem(minitest-fail-fast) >= 0.1.0
Requires:      gem(m) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pg_examiner) >= 0.5.2
Requires:      gem(bundler) >= 0
Conflicts:     gem(activerecord) >= 7
Conflicts:     gem(activejob) >= 7
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(pg_examiner) >= 0.6

%description   -n gem-que-devel
A PostgreSQL-based Job Queue development package.

A job queue that uses PostgreSQL's advisory locks for speed and reliability.

%description   -n gem-que-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета que.
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

%files         -n que
%doc README.md
%_bindir/que

%if_enabled    doc
%files         -n gem-que-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-que-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1
- + packaged gem with Ruby Policy 2.0
