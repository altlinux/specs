%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname redis-client

Name:          gem-redis-client
Version:       0.23.0
Release:       alt1
Summary:       Simple low-level client for Redis 6+
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/redis-rb/redis-client
Vcs:           https://github.com/redis-rb/redis-client.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(connection_pool) >= 0
BuildRequires: libssl-devel
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(rake-compiler) >= 0
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(benchmark) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(hiredis) >= 0
BuildRequires: gem(megatest) >= 0
BuildRequires: gem(redis) >= 4.6
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-minitest) >= 0
BuildRequires: gem(toxiproxy) >= 0
BuildConflicts: gem(redis) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency redis >= 6.0.0,redis < 7
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Requires:      ruby >= 2.6.0
Requires:      gem(connection_pool) >= 0
Provides:      gem(redis-client) = 0.23.0

%description
Simple low-level client for Redis 6+

redis-client is a simple, low-level, client for Redis 6+, Valkey 7+, KeyDB, and
several other databases that implement the same RESP3 protocol.

Contrary to the redis gem, redis-client doesn't try to map all Redis commands to
Ruby constructs, it merely is a thin wrapper on top of the RESP3 protocol.


%package       -n gem-hiredis-client
Version:       0.23.0
Release:       alt1
Summary:       Simple low-level client for Redis 6+
Group:         Development/Ruby

Requires:      ruby >= 2.6.0
Requires:      gem(redis-client) = 0.23.0
Provides:      gem(hiredis-client) = 0.23.0

%description   -n gem-hiredis-client
Hiredis binding for redis-client

redis-client is a simple, low-level, client for Redis 6+, Valkey 7+, KeyDB, and
several other databases that implement the same RESP3 protocol.

Contrary to the redis gem, redis-client doesn't try to map all Redis commands to
Ruby constructs, it merely is a thin wrapper on top of the RESP3 protocol.


%if_enabled    doc
%package       -n gem-hiredis-client-doc
Version:       0.23.0
Release:       alt1
Summary:       Simple low-level client for Redis 6+ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hiredis-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hiredis-client) = 0.23.0

%description   -n gem-hiredis-client-doc
Simple low-level client for Redis 6+ documentation files.

redis-client is a simple, low-level, client for Redis 6+, Valkey 7+, KeyDB, and
several other databases that implement the same RESP3 protocol.

Contrary to the redis gem, redis-client doesn't try to map all Redis commands to
Ruby constructs, it merely is a thin wrapper on top of the RESP3 protocol.

%description   -n gem-hiredis-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hiredis-client.
%endif


%if_enabled    devel
%package       -n gem-hiredis-client-devel
Version:       0.23.0
Release:       alt1
Summary:       Simple low-level client for Redis 6+ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hiredis-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hiredis-client) = 0.23.0
Requires:      gem(redis-client) = 0.23.0
Requires:      libssl-devel

%description   -n gem-hiredis-client-devel
Simple low-level client for Redis 6+ development package.

Hiredis binding for redis-client
redis-client is a simple, low-level, client for Redis 6+, Valkey 7+, KeyDB, and
several other databases that implement the same RESP3 protocol.

Contrary to the redis gem, redis-client doesn't try to map all Redis commands to
Ruby constructs, it merely is a thin wrapper on top of the RESP3 protocol.

%description   -n gem-hiredis-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hiredis-client.
%endif


%if_enabled    doc
%package       -n gem-redis-client-doc
Version:       0.23.0
Release:       alt1
Summary:       Simple low-level client for Redis 6+ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redis-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redis-client) = 0.23.0

%description   -n gem-redis-client-doc
Simple low-level client for Redis 6+ documentation files.

redis-client is a simple, low-level, client for Redis 6+, Valkey 7+, KeyDB, and
several other databases that implement the same RESP3 protocol.

Contrary to the redis gem, redis-client doesn't try to map all Redis commands to
Ruby constructs, it merely is a thin wrapper on top of the RESP3 protocol.

%description   -n gem-redis-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redis-client.
%endif


%if_enabled    devel
%package       -n gem-redis-client-devel
Version:       0.23.0
Release:       alt1
Summary:       Simple low-level client for Redis 6+ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redis-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      libssl-devel
Requires:      gem(redis-client) = 0.23.0
Requires:      gem(benchmark) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(connection_pool) >= 0
Requires:      gem(hiredis) >= 0
Requires:      gem(megatest) >= 0
Requires:      gem(rake) >= 13.1.0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(redis) >= 4.6
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-minitest) >= 0
Requires:      gem(toxiproxy) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(redis) >= 7

%description   -n gem-redis-client-devel
Simple low-level client for Redis 6+ development package.

redis-client is a simple, low-level, client for Redis 6+, Valkey 7+, KeyDB, and
several other databases that implement the same RESP3 protocol.

Contrary to the redis gem, redis-client doesn't try to map all Redis commands to
Ruby constructs, it merely is a thin wrapper on top of the RESP3 protocol.

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
%doc CHANGELOG.md LICENSE.md README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-hiredis-client
%doc README.md
%ruby_gemspecdir/hiredis-client-0.23.0.gemspec
%ruby_gemslibdir/hiredis-client-0.23.0
%ruby_gemsextdir/hiredis-client-0.23.0

%if_enabled    doc
%files         -n gem-hiredis-client-doc
%doc README.md
%ruby_gemsdocdir/hiredis-client-0.23.0
%endif

%if_enabled    devel
%files         -n gem-hiredis-client-devel
%doc README.md
%ruby_includedir/*
%endif

%if_enabled    doc
%files         -n gem-redis-client-doc
%doc CHANGELOG.md LICENSE.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-redis-client-devel
%doc CHANGELOG.md LICENSE.md README.md
%endif


%changelog
* Thu Dec 12 2024 Pavel Skrylev <majioa@altlinux.org> 0.23.0-alt1
- ^ 0.22.2 -> 0.23.0

* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 0.22.2-alt1
- ^ 0.12.1 -> 0.22.2

* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 0.12.1-alt1
- + packaged gem with Ruby Policy 2.0
