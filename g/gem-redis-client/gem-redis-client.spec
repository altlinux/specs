%define        gemname redis-client

Name:          gem-redis-client
Version:       0.12.1
Release:       alt1
Summary:       Simple low-level client for Redis 6+
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/redis-rb/redis-client
Vcs:           https://github.com/redis-rb/redis-client.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 13.0
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
Requires:      gem(connection_pool) >= 0
Provides:      gem(redis-client) = 0.12.1


%description
Simple low-level client for Redis 6+


%package       -n gem-hiredis-client
Version:       0.12.1
Release:       alt1
Summary:       Hiredis binding for redis-client
Group:         Development/Ruby

Requires:      gem(redis-client) = 0.12.1
Provides:      gem(hiredis-client) = 0.12.1

%description   -n gem-hiredis-client
Hiredis binding for redis-client


%package       -n gem-hiredis-client-doc
Version:       0.12.1
Release:       alt1
Summary:       Hiredis binding for redis-client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hiredis-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hiredis-client) = 0.12.1

%description   -n gem-hiredis-client-doc
Hiredis binding for redis-client documentation files.

%description   -n gem-hiredis-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hiredis-client.


%package       -n gem-hiredis-client-devel
Version:       0.12.1
Release:       alt1
Summary:       Hiredis binding for redis-client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hiredis-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hiredis-client) = 0.12.1

%description   -n gem-hiredis-client-devel
Hiredis binding for redis-client development package.

%description   -n gem-hiredis-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hiredis-client.


%package       -n gem-redis-client-doc
Version:       0.12.1
Release:       alt1
Summary:       Simple low-level client for Redis 6+ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redis-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redis-client) = 0.12.1

%description   -n gem-redis-client-doc
Simple low-level client for Redis 6+ documentation files.

%description   -n gem-redis-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redis-client.


%package       -n gem-redis-client-devel
Version:       0.12.1
Release:       alt1
Summary:       Simple low-level client for Redis 6+ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redis-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redis-client) = 0.12.1
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 13.0
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
%ruby_gemspecdir/hiredis-client-0.12.1.gemspec
%ruby_gemslibdir/hiredis-client-0.12.1
%ruby_gemsextdir/hiredis-client-0.12.1

%files         -n gem-hiredis-client-doc
%doc README.md
%ruby_gemsdocdir/hiredis-client-0.12.1

%files         -n gem-hiredis-client-devel
%doc README.md
%ruby_includedir/*

%files         -n gem-redis-client-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-redis-client-devel
%doc README.md


%changelog
* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 0.12.1-alt1
- + packaged gem with Ruby Policy 2.0
