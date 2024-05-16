%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname sidekiq

Name:          gem-sidekiq
Version:       6.5.12
Release:       alt1
Summary:       Simple, efficient background processing for Ruby
License:       LGPL-3.0
Group:         Development/Ruby
Url:           http://sidekiq.org
Vcs:           https://github.com/mperham/sidekiq.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(redis) >= 4.5.0
BuildRequires: gem(redis-namespace) >= 0
BuildRequires: gem(redis-client) >= 0
BuildRequires: gem(rails) >= 6.0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(after_commit_everywhere) >= 0
BuildRequires: gem(net-smtp) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(codecov) >= 0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(hiredis) >= 0
BuildRequires: gem(toxiproxy) >= 0
BuildRequires: gem(connection_pool) >= 2.2.5
BuildRequires: gem(rack) >= 2.0
BuildConflicts: gem(redis) >= 6
BuildConflicts: gem(rails) >= 7
BuildConflicts: gem(connection_pool) >= 3
BuildConflicts: gem(rack) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 3.0,rack < 4
%ruby_use_gem_dependency redis >= 5.0.6,redis < 6
Requires:      gem(redis) >= 4.5.0
Requires:      gem(connection_pool) >= 2.2.5
Requires:      gem(rack) >= 2.0
Conflicts:     gem(redis) >= 6
Conflicts:     gem(connection_pool) >= 3
Conflicts:     gem(rack) >= 4
Provides:      gem(sidekiq) = 6.5.12


%description
Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.


%package       -n sidekiq
Version:       6.5.12
Release:       alt1
Summary:       Simple, efficient background processing for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sidekiq
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sidekiq) = 6.5.12

%description   -n sidekiq
Simple, efficient background processing for Ruby executable(s).

Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.

%description   -n sidekiq -l ru_RU.UTF-8
Исполнямка для самоцвета sidekiq.


%if_enabled    doc
%package       -n gem-sidekiq-doc
Version:       6.5.12
Release:       alt1
Summary:       Simple, efficient background processing for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sidekiq
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sidekiq) = 6.5.12

%description   -n gem-sidekiq-doc
Simple, efficient background processing for Ruby documentation files.

Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.

%description   -n gem-sidekiq-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sidekiq.
%endif


%if_enabled    devel
%package       -n gem-sidekiq-devel
Version:       6.5.12
Release:       alt1
Summary:       Simple, efficient background processing for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sidekiq
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sidekiq) = 6.5.12
Requires:      gem(rake) >= 0
Requires:      gem(redis-namespace) >= 0
Requires:      gem(redis-client) >= 0
Requires:      gem(rails) >= 6.0
Requires:      gem(sqlite3) >= 0
Requires:      gem(after_commit_everywhere) >= 0
Requires:      gem(net-smtp) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(codecov) >= 0
Requires:      gem(standard) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(hiredis) >= 0
Requires:      gem(toxiproxy) >= 0
Conflicts:     gem(rails) >= 7

%description   -n gem-sidekiq-devel
Simple, efficient background processing for Ruby development package.

Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.

%description   -n gem-sidekiq-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sidekiq.
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

%files         -n sidekiq
%doc README.md
%_bindir/sidekiq
%_bindir/sidekiqmon

%if_enabled    doc
%files         -n gem-sidekiq-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-sidekiq-devel
%doc README.md
%endif


%changelog
* Tue Apr 16 2024 Pavel Skrylev <majioa@altlinux.org> 6.5.12-alt1
- ^ 6.4.1 -> 6.5.12

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 6.4.1-alt1
- ^ 5.2.8 -> 6.4.1

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.8-alt1.1
- * gem deps for rack to ~> 2.0

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.8-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
