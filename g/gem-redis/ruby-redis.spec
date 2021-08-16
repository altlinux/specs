%define        gemname redis

Name:          gem-redis
Version:       4.3.1
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
BuildRequires: gem(em-synchrony) >= 0
BuildRequires: gem(hiredis) >= 0
BuildRequires: gem(mocha) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-redis < %EVR
Provides:      ruby-redis = %EVR
Provides:      gem(redis) = 4.3.1


%description
A Ruby client that tries to match Redis' API one-to-one, while still providing
an idiomatic interface.


%package       -n gem-redis-doc
Version:       4.3.1
Release:       alt1
Summary:       A Ruby client library for Redis documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redis) = 4.3.1

%description   -n gem-redis-doc
A Ruby client library for Redis documentation files.

A Ruby client that tries to match Redis' API one-to-one, while still providing
an idiomatic interface.

%description   -n gem-redis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redis.


%package       -n gem-redis-devel
Version:       4.3.1
Release:       alt1
Summary:       A Ruby client library for Redis development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redis
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redis) = 4.3.1
Requires:      gem(em-synchrony) >= 0
Requires:      gem(hiredis) >= 0
Requires:      gem(mocha) >= 0

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

%files         -n gem-redis-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-redis-devel
%doc README.md


%changelog
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
