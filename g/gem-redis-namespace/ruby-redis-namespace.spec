%define        gemname redis-namespace

Name:          gem-redis-namespace
Version:       1.8.2
Release:       alt1
Summary:       This gem adds a Redis::Namespace class which can be used to namespace Redis keys
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/resque/redis-namespace
Vcs:           https://github.com/resque/redis-namespace.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(redis) >= 3.0.4
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.7 gem(rspec) < 4
BuildRequires: gem(rspec-its) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(redis) >= 3.0.4
Obsoletes:     ruby-redis-namespace < %EVR
Provides:      ruby-redis-namespace = %EVR
Provides:      gem(redis-namespace) = 1.8.2


%description
Redis::Namespace provides an interface to a namespaced subset of your redis
keyspace (e.g., keys with a common beginning), and requires the redis-rb gem.

Redis::Namespace provides a namespaced interface to Redis by keeping an
internal registry of the method signatures in Redis provided by the redis-rb
gem; we keep track of which arguments need the namespace added, and which return
values need the namespace removed.


%package       -n gem-redis-namespace-doc
Version:       1.8.2
Release:       alt1
Summary:       This gem adds a Redis::Namespace class which can be used to namespace Redis keys documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redis-namespace
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redis-namespace) = 1.8.2

%description   -n gem-redis-namespace-doc
This gem adds a Redis::Namespace class which can be used to namespace Redis keys
documentation files.

Redis::Namespace provides an interface to a namespaced subset of your redis
keyspace (e.g., keys with a common beginning), and requires the redis-rb gem.

Redis::Namespace provides a namespaced interface to Redis by keeping an
internal registry of the method signatures in Redis provided by the redis-rb
gem; we keep track of which arguments need the namespace added, and which return
values need the namespace removed.

%description   -n gem-redis-namespace-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redis-namespace.


%package       -n gem-redis-namespace-devel
Version:       1.8.2
Release:       alt1
Summary:       This gem adds a Redis::Namespace class which can be used to namespace Redis keys development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redis-namespace
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redis-namespace) = 1.8.2
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.7 gem(rspec) < 4
Requires:      gem(rspec-its) >= 0

%description   -n gem-redis-namespace-devel
This gem adds a Redis::Namespace class which can be used to namespace Redis keys
development package.

Redis::Namespace provides an interface to a namespaced subset of your redis
keyspace (e.g., keys with a common beginning), and requires the redis-rb gem.

Redis::Namespace provides a namespaced interface to Redis by keeping an
internal registry of the method signatures in Redis provided by the redis-rb
gem; we keep track of which arguments need the namespace added, and which return
values need the namespace removed.

%description   -n gem-redis-namespace-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета redis-namespace.


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

%files         -n gem-redis-namespace-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-redis-namespace-devel
%doc README.md


%changelog
* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 1.8.2-alt1
- ^ 1.7.0 -> 1.8.2

* Sat Mar 07 2020 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- > Ruby Policy 2.0
- ^ 1.6.0 -> 1.7.0
- ! spec

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- Initial build for Sisyphus
