%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname connection_pool

Name:          gem-connection-pool
Version:       2.5.0
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
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(minitest) >= 5.0.0
BuildRequires: gem(standard) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names connection_pool,connection-pool
Requires:      ruby >= 2.5.0
Obsoletes:     ruby-connection_pool < %EVR
Provides:      ruby-connection_pool = %EVR
Provides:      gem(connection_pool) = 2.5.0

%description
Generic connection pooling for Ruby.

MongoDB has its own connection pool. ActiveRecord has its own connection pool.
This is a generic connection pool that can be used with anything, e.g. Redis,
Dalli and other Ruby network clients.


%if_enabled    doc
%package       -n gem-connection-pool-doc
Version:       2.5.0
Release:       alt1
Summary:       Generic connection pooling for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета connection_pool
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(connection_pool) = 2.5.0

%description   -n gem-connection-pool-doc
Generic connection pooling for Ruby documentation files.

%description   -n gem-connection-pool-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета connection_pool.
%endif


%if_enabled    devel
%package       -n gem-connection-pool-devel
Version:       2.5.0
Release:       alt1
Summary:       Generic connection pooling for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета connection_pool
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(connection_pool) = 2.5.0
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 5.0.0
Requires:      gem(rake) >= 0
Requires:      gem(standard) >= 0

%description   -n gem-connection-pool-devel
Generic connection pooling for Ruby development package.

%description   -n gem-connection-pool-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета connection_pool.
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
%files         -n gem-connection-pool-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-connection-pool-devel
%doc LICENSE README.md
%endif


%changelog
* Tue Jan 21 2025 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- ^ 2.2.5 -> 2.5.0

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.5-alt1
- ^ 2.2.2 -> 2.2.5

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- Initial build for Sisyphus
