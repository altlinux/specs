%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname redis-cluster-client

Name:          gem-redis-cluster-client
Version:       0.17.1
Release:       alt1
Summary:       A Redis cluster client for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/redis-rb/redis-cluster-client
Vcs:           https://github.com/redis-rb/redis-cluster-client.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(benchmark) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(hiredis-client) >= 0.6
BuildRequires: gem(irb) >= 0
BuildRequires: gem(logger) >= 0
BuildRequires: gem(memory_profiler) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(redis-client) >= 0.28
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-minitest) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(valkey-glide-rb) >= 0
BuildConflicts: gem(hiredis-client) >= 1
BuildConflicts: gem(redis-client) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7.0
Requires:      gem(redis-client) >= 0.28
Conflicts:     gem(redis-client) >= 1
Provides:      gem(redis-cluster-client) = 0.17.1

%description
A Redis cluster client for Ruby


%if_enabled    doc
%package       -n gem-redis-cluster-client-doc
Version:       0.17.1
Release:       alt1
Summary:       A Redis cluster client for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redis-cluster-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redis-cluster-client) = 0.17.1

%description   -n gem-redis-cluster-client-doc
A Redis cluster client for Ruby documentation files.

%description   -n gem-redis-cluster-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redis-cluster-client.
%endif


%if_enabled    devel
%package       -n gem-redis-cluster-client-devel
Version:       0.17.1
Release:       alt1
Summary:       A Redis cluster client for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redis-cluster-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redis-cluster-client) = 0.17.1
Requires:      gem(benchmark) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(hiredis-client) >= 0.6
Requires:      gem(irb) >= 0
Requires:      gem(logger) >= 0
Requires:      gem(memory_profiler) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(redis-client) >= 0.28
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-minitest) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(valkey-glide-rb) >= 0
Conflicts:     gem(hiredis-client) >= 1
Conflicts:     gem(redis-client) >= 1

%description   -n gem-redis-cluster-client-devel
A Redis cluster client for Ruby development package.

%description   -n gem-redis-cluster-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета redis-cluster-client.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-redis-cluster-client-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-redis-cluster-client-devel
%doc LICENSE README.md
%endif


%changelog
* Mon Sep 28 2026 Pavel Skrylev <majioa@altlinux.org> 0.17.1-alt1
- ^ 0.4.2 -> 0.17.1

* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 0.4.2-alt1
- + packaged gem with Ruby Policy 2.0
