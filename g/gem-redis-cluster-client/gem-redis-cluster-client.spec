%define        gemname redis-cluster-client

Name:          gem-redis-cluster-client
Version:       0.4.2
Release:       alt1
Summary:       A Redis cluster client for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/redis-rb/redis-cluster-client
Vcs:           https://github.com/redis-rb/redis-cluster-client.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(hiredis-client) >= 0.6
BuildRequires: gem(memory_profiler) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-minitest) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(redis-client) >= 0.12
BuildConflicts: gem(hiredis-client) >= 1
BuildConflicts: gem(redis-client) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(redis-client) >= 0.12
Conflicts:     gem(redis-client) >= 1
Provides:      gem(redis-cluster-client) = 0.4.2


%description
A Redis cluster client for Ruby


%package       -n gem-redis-cluster-client-doc
Version:       0.4.2
Release:       alt1
Summary:       A Redis cluster client for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redis-cluster-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redis-cluster-client) = 0.4.2

%description   -n gem-redis-cluster-client-doc
A Redis cluster client for Ruby documentation files.

%description   -n gem-redis-cluster-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redis-cluster-client.


%package       -n gem-redis-cluster-client-devel
Version:       0.4.2
Release:       alt1
Summary:       A Redis cluster client for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redis-cluster-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redis-cluster-client) = 0.4.2
Requires:      gem(hiredis-client) >= 0.6
Requires:      gem(memory_profiler) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-minitest) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rake) >= 0
Conflicts:     gem(hiredis-client) >= 1

%description   -n gem-redis-cluster-client-devel
A Redis cluster client for Ruby development package.

%description   -n gem-redis-cluster-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета redis-cluster-client.


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

%files         -n gem-redis-cluster-client-doc
%ruby_gemdocdir

%files         -n gem-redis-cluster-client-devel


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 0.4.2-alt1
- + packaged gem with Ruby Policy 2.0
