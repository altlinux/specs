%define        gemname connection_pool

Name:          gem-connection-pool
Version:       2.2.5
Release:       alt1
Summary:       Generic connection pooling for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mperham/connection_pool
Vcs:           https://github.com/mperham/connection_pool.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(minitest) >= 5.0.0
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names connection_pool,connection-pool
Obsoletes:     ruby-connection-pool < %EVR
Provides:      ruby-connection-pool = %EVR
Provides:      ruby-connection_pool = %EVR
Provides:      gem(connection_pool) = 2.2.5


%description
Generic connection pooling for Ruby.

MongoDB has its own connection pool. ActiveRecord has its own connection pool.
This is a generic connection pool that can be used with anything, e.g. Redis,
Dalli and other Ruby network clients.


%package       -n gem-connection-pool-doc
Version:       2.2.5
Release:       alt1
Summary:       Generic connection pooling for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета connection_pool
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(connection_pool) = 2.2.5

%description   -n gem-connection-pool-doc
Generic connection pooling for Ruby documentation files.

MongoDB has its own connection pool. ActiveRecord has its own connection pool.
This is a generic connection pool that can be used with anything, e.g. Redis,
Dalli and other Ruby network clients.

%description   -n gem-connection-pool-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета connection_pool.


%package       -n gem-connection-pool-devel
Version:       2.2.5
Release:       alt1
Summary:       Generic connection pooling for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета connection_pool
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(connection_pool) = 2.2.5
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(minitest) >= 5.0.0 gem(minitest) < 6
Requires:      gem(rake) >= 0 gem(rake) < 14

%description   -n gem-connection-pool-devel
Generic connection pooling for Ruby development package.

MongoDB has its own connection pool. ActiveRecord has its own connection pool.
This is a generic connection pool that can be used with anything, e.g. Redis,
Dalli and other Ruby network clients.

%description   -n gem-connection-pool-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета connection_pool.


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

%files         -n gem-connection-pool-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-connection-pool-devel
%doc README.md


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.5-alt1
- ^ 2.2.2 -> 2.2.5

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- Initial build for Sisyphus
