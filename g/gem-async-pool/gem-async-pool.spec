%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname async-pool

Name:          gem-async-pool
Version:       0.11.2
Release:       alt1
Summary:       A singleplex and multiplex resource pool for implementing robust clients
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-pool
Vcs:           https://github.com/socketry/async-pool.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(async) >= 2.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.2
Requires:      gem(async) >= 2.0
Provides:      async-pool = %EVR
Provides:      gem(async-pool) = 0.11.2

%description
A singleplex and multiplex resource pool for implementing robust clients.


%if_enabled    doc
%package       -n gem-async-pool-doc
Version:       0.11.2
Release:       alt1
Summary:       A singleplex and multiplex resource pool for implementing robust clients documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-pool
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(async-pool) = 0.11.2

%description   -n gem-async-pool-doc
A singleplex and multiplex resource pool for implementing robust clients
documentation files.

%description   -n gem-async-pool-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async-pool.
%endif


%if_enabled    devel
%package       -n gem-async-pool-devel
Version:       0.11.2
Release:       alt1
Summary:       A singleplex and multiplex resource pool for implementing robust clients development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-pool
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(async-pool) = 0.11.2

%description   -n gem-async-pool-devel
A singleplex and multiplex resource pool for implementing robust clients
development package.

%description   -n gem-async-pool-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async-pool.
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
%doc license.md readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-async-pool-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-async-pool-devel
%doc license.md readme.md
%endif


%changelog
* Fri Mar 20 2026 Pavel Skrylev <majioa@altlinux.org> 0.11.2-alt1
- ^ 0.3.8 -> 0.11.2

* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.8-alt1
- + packaged gem with Ruby Policy 2.0
