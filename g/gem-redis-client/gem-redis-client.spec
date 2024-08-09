%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname redis-client

Name:          gem-redis-client
Version:       0.22.2
Release:       alt1
Summary:       Simple low-level client for Redis 6+
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/redis-rb/redis-client
Vcs:           https://github.com/redis-rb/redis-client.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-minitest) >= 0
BuildRequires: gem(toxiproxy) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(hiredis) >= 0
BuildRequires: gem(redis) >= 4.6
BuildRequires: gem(stackprof) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(connection_pool) >= 0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(redis) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency redis > 5.0.0,redis < 6
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Requires:      gem(connection_pool) >= 0
Provides:      gem(redis-client) = 0.22.2


%description
Simple low-level client for Redis 6+


%package       -n gem-hiredis-client
Version:       0.22.2
Release:       alt1
Summary:       Simple low-level client for Redis 6+
Group:         Development/Ruby

Requires:      gem(redis-client) = 0.22.2
Provides:      gem(hiredis-client) = 0.22.2

%description   -n gem-hiredis-client
Hiredis binding for redis-client


%if_enabled    doc
%package       -n gem-hiredis-client-doc
Version:       0.22.2
Release:       alt1
Summary:       Simple low-level client for Redis 6+ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hiredis-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hiredis-client) = 0.22.2

%description   -n gem-hiredis-client-doc
Simple low-level client for Redis 6+ documentation files.

Hiredis binding for redis-client

%description   -n gem-hiredis-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hiredis-client.
%endif


%if_enabled    devel
%package       -n gem-hiredis-client-devel
Version:       0.22.2
Release:       alt1
Summary:       Simple low-level client for Redis 6+ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hiredis-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hiredis-client) = 0.22.2

%description   -n gem-hiredis-client-devel
Simple low-level client for Redis 6+ development package.

Hiredis binding for redis-client

%description   -n gem-hiredis-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hiredis-client.
%endif


%if_enabled    doc
%package       -n gem-redis-client-doc
Version:       0.22.2
Release:       alt1
Summary:       Simple low-level client for Redis 6+ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redis-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redis-client) = 0.22.2

%description   -n gem-redis-client-doc
Simple low-level client for Redis 6+ documentation files.

%description   -n gem-redis-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redis-client.
%endif


%if_enabled    devel
%package       -n gem-redis-client-devel
Version:       0.22.2
Release:       alt1
Summary:       Simple low-level client for Redis 6+ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redis-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redis-client) = 0.22.2
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 13.1.0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-minitest) >= 0
Requires:      gem(toxiproxy) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(hiredis) >= 0
Requires:      gem(redis) >= 4.6
Requires:      gem(stackprof) >= 0
Requires:      gem(byebug) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(redis) >= 6

%description   -n gem-redis-client-devel
Simple low-level client for Redis 6+ development package.

%description   -n gem-redis-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета redis-client.
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

%files         -n gem-hiredis-client
%doc README.md
%ruby_gemspecdir/hiredis-client-0.22.2.gemspec
%ruby_gemslibdir/hiredis-client-0.22.2
%ruby_gemsextdir/hiredis-client-0.22.2

%if_enabled    doc
%files         -n gem-hiredis-client-doc
%doc README.md
%ruby_gemsdocdir/hiredis-client-0.22.2
%endif

%if_enabled    devel
%files         -n gem-hiredis-client-devel
%doc README.md
%ruby_includedir/*
%endif

%if_enabled    doc
%files         -n gem-redis-client-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-redis-client-devel
%doc README.md
%endif


%changelog
* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 0.22.2-alt1
- ^ 0.12.1 -> 0.22.2

* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 0.12.1-alt1
- + packaged gem with Ruby Policy 2.0
