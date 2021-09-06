%define        gemname async-pool

Name:          gem-async-pool
Version:       0.3.8
Release:       alt1
Summary:       A singleplex and multiplex resource pool for implementing robust clients
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-pool
Vcs:           https://github.com/socketry/async-pool.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(async) >= 1.25
BuildRequires: gem(async-rspec) >= 1.1 gem(async-rspec) < 2
BuildRequires: gem(bake-bundler) >= 0
# BuildRequires: gem(bake-modernize) >= 0
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 3.6 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(async) >= 1.25
Provides:      gem(async-pool) = 0.3.8


%description
A singleplex and multiplex resource pool for implementing robust clients.


%package       -n gem-async-pool-doc
Version:       0.3.8
Release:       alt1
Summary:       A singleplex and multiplex resource pool for implementing robust clients documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-pool
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async-pool) = 0.3.8

%description   -n gem-async-pool-doc
A singleplex and multiplex resource pool for implementing robust clients
documentation files.

%description   -n gem-async-pool-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async-pool.


%package       -n gem-async-pool-devel
Version:       0.3.8
Release:       alt1
Summary:       A singleplex and multiplex resource pool for implementing robust clients development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-pool
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async-pool) = 0.3.8
Requires:      gem(async-rspec) >= 1.1 gem(async-rspec) < 2
Requires:      gem(bake-bundler) >= 0
Requires:      gem(bake-modernize) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 3.6 gem(rspec) < 4

%description   -n gem-async-pool-devel
A singleplex and multiplex resource pool for implementing robust clients
development package.

%description   -n gem-async-pool-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async-pool.


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

%files         -n gem-async-pool-doc
%ruby_gemdocdir

%files         -n gem-async-pool-devel


%changelog
* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.8-alt1
- + packaged gem with Ruby Policy 2.0
