%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname redis

Name:          gem-redis
Version:       6.0.0
Release:       alt1
Summary:       A Ruby client library for Redis
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/redis/redis-rb
Vcs:           https://github.com/redis/redis-rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(hiredis-client) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(redis-client) = 0.30.1
BuildRequires: gem(redis-cluster-client) >= 0.17.0
BuildRequires: gem(rubocop) >= 1.15.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0
%ruby_use_gem_dependency redis-cluster-client >= 0.17.0
Requires:      ruby >= 3.2.0
Requires:      gem(redis-client) = 0.30.1
Obsoletes:     ruby-redis < %EVR
Provides:      ruby-redis = %EVR
Provides:      gem(redis) = 6.0.0

%description
A Ruby client that tries to match Redis' API one-to-one, while still providing
an idiomatic interface.


%package       -n gem-redis-clustering
Version:       6.0.0
Release:       alt1
Summary:       A Ruby client library for Redis Cluster
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 3.2.0
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(redis) = 6.0.0
Requires:      gem(redis-cluster-client) >= 0.17.0
Requires:      gem(redis-clustering) >= 0
Requires:      gem(rubocop) >= 1.88.0
Provides:      gem(redis-clustering) = 6.0.0

%description   -n gem-redis-clustering
A Ruby client that tries to match Redis' Cluster API one-to-one, while still
providing an idiomatic interface.


%if_enabled    doc
%package       -n gem-redis-clustering-doc
Version:       6.0.0
Release:       alt1
Summary:       A Ruby client library for Redis Cluster documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redis-clustering
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redis-clustering) = 6.0.0

%description   -n gem-redis-clustering-doc
A Ruby client library for Redis Cluster documentation files.

A Ruby client that tries to match Redis' Cluster API one-to-one, while still
providing an idiomatic interface.

%description   -n gem-redis-clustering-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redis-clustering.
%endif


%if_enabled    devel
%package       -n gem-redis-clustering-devel
Version:       6.0.0
Release:       alt1
Summary:       A Ruby client library for Redis Cluster development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redis-clustering
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redis-clustering) = 6.0.0
Requires:      gem(hiredis-client) >= 0

%description   -n gem-redis-clustering-devel
A Ruby client library for Redis Cluster development package.

A Ruby client that tries to match Redis' Cluster API one-to-one, while still
providing an idiomatic interface.

%description   -n gem-redis-clustering-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета redis-clustering.
%endif


%if_enabled    doc
%package       -n gem-redis-doc
Version:       6.0.0
Release:       alt1
Summary:       A Ruby client library for Redis documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redis) = 6.0.0

%description   -n gem-redis-doc
A Ruby client library for Redis documentation files.

A Ruby client that tries to match Redis' API one-to-one, while still providing
an idiomatic interface.

%description   -n gem-redis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redis.
%endif


%if_enabled    devel
%package       -n gem-redis-devel
Version:       6.0.0
Release:       alt1
Summary:       A Ruby client library for Redis development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redis
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redis) = 6.0.0
Requires:      gem(hiredis-client) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(redis-client) = 0.30.1
Requires:      gem(rubocop) >= 1.15.0

%description   -n gem-redis-devel
A Ruby client library for Redis development package.

A Ruby client that tries to match Redis' API one-to-one, while still providing
an idiomatic interface.

%description   -n gem-redis-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета redis.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-redis-clustering
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspecdir/redis-clustering-6.0.0.gemspec
%ruby_gemslibdir/redis-clustering-6.0.0

%if_enabled    doc
%files         -n gem-redis-clustering-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemsdocdir/redis-clustering-6.0.0
%endif

%if_enabled    devel
%files         -n gem-redis-clustering-devel
%doc CHANGELOG.md LICENSE README.md
%endif

%if_enabled    doc
%files         -n gem-redis-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-redis-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Mon Sep 28 2026 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt1
- ^ 5.0.6 -> 6.0.0

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
