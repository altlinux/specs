%define        gemname redis

Name:          gem-redis
Version:       5.0.6
Release:       alt1
Summary:       A Ruby client library for Redis
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/redis/redis-rb
Vcs:           https://github.com/redis/redis-rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(hiredis-client) >= 0
BuildRequires: gem(redis-client) >= 0.9.0
BuildRequires: gem(redis-cluster-client) >= 0.3.7
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(redis-client) >= 0.9.0
Obsoletes:     ruby-redis < %EVR
Provides:      ruby-redis = %EVR
Provides:      gem(redis) = 5.0.6


%description
A Ruby client that tries to match Redis' API one-to-one, while still providing
an idiomatic interface.


%package       -n gem-redis-clustering
Version:       5.0.6
Release:       alt1
Summary:       A Ruby client library for Redis Cluster
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redis) = 5.0.6
Requires:      gem(redis-cluster-client) >= 0.3.7
Provides:      gem(redis-clustering) = 5.0.6

%description   -n gem-redis-clustering
A Ruby client that tries to match Redis' Cluster API one-to-one, while still
providing an idiomatic interface.


%package       -n gem-redis-clustering-doc
Version:       5.0.6
Release:       alt1
Summary:       A Ruby client library for Redis Cluster documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redis-clustering
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redis-clustering) = 5.0.6

%description   -n gem-redis-clustering-doc
A Ruby client library for Redis Cluster documentation files.

A Ruby client that tries to match Redis' Cluster API one-to-one, while still
providing an idiomatic interface.

%description   -n gem-redis-clustering-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redis-clustering.


%package       -n gem-redis-clustering-devel
Version:       5.0.6
Release:       alt1
Summary:       A Ruby client library for Redis Cluster development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redis-clustering
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redis-clustering) = 5.0.6
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(mocha) >= 0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-redis-clustering-devel
A Ruby client library for Redis Cluster development package.

A Ruby client that tries to match Redis' Cluster API one-to-one, while still
providing an idiomatic interface.

%description   -n gem-redis-clustering-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета redis-clustering.


%package       -n gem-redis-doc
Version:       5.0.6
Release:       alt1
Summary:       A Ruby client library for Redis documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redis) = 5.0.6

%description   -n gem-redis-doc
A Ruby client library for Redis documentation files.

A Ruby client that tries to match Redis' API one-to-one, while still providing
an idiomatic interface.

%description   -n gem-redis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redis.


%package       -n gem-redis-devel
Version:       5.0.6
Release:       alt1
Summary:       A Ruby client library for Redis development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redis
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redis) = 5.0.6
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(mocha) >= 0
Requires:      gem(hiredis-client) >= 0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-redis-devel
A Ruby client library for Redis development package.

A Ruby client that tries to match Redis' API one-to-one, while still providing
an idiomatic interface.

%description   -n gem-redis-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета redis.


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

%files         -n gem-redis-clustering
%doc README.md
%ruby_gemspecdir/redis-clustering-5.0.6.gemspec
%ruby_gemslibdir/redis-clustering-5.0.6

%files         -n gem-redis-clustering-doc
%doc README.md
%ruby_gemsdocdir/redis-clustering-5.0.6

%files         -n gem-redis-clustering-devel
%doc README.md

%files         -n gem-redis-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-redis-devel
%doc README.md


%changelog
* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 5.0.6-alt1
- ^ 4.3.1 -> 5.0.6

* Tue Jun 29 2021 Pavel Skrylev <majioa@altlinux.org> 4.3.1-alt1
- ^ 4.2.5 -> 4.3.1

* Tue Dec 15 2020 Pavel Skrylev <majioa@altlinux.org> 4.2.5-alt1
- ^ 4.1.0 -> 4.2.5
- * policied name

* Fri Apr 12 2019 Pavel Skrylev <majioa@altlinux.org> 4.1.0-alt1
- > Ruby Policy 2.0
- ^ 4.0.2 -> 4.1.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.1-alt1
- Initial build for Sisyphus
