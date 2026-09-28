%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fakeredis

Name:          gem-fakeredis
Version:       0.9.2
Release:       alt1
Summary:       Fake (In-memory) driver for redis-rb
License:       MIT
Group:         Development/Ruby
Url:           https://guilleiguaran.github.com/fakeredis
Vcs:           https://github.com/guilleiguaran/fakeredis.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(redis) >= 4.8
BuildRequires: gem(rspec) >= 3
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency redis >= 6.0.0
Requires:      gem(redis) >= 4.8
Conflicts:     gem(redis) >= 7
Provides:      gem(fakeredis) = 0.9.2

%description
Fake (In-memory) driver for redis-rb. Useful for testing environment and
machines without Redis.


%if_enabled    doc
%package       -n gem-fakeredis-doc
Version:       0.9.2
Release:       alt1
Summary:       Fake (In-memory) driver for redis-rb documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fakeredis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fakeredis) = 0.9.2

%description   -n gem-fakeredis-doc
Fake (In-memory) driver for redis-rb documentation files.

Fake (In-memory) driver for redis-rb. Useful for testing environment and
machines without Redis.

%description   -n gem-fakeredis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fakeredis.
%endif


%if_enabled    devel
%package       -n gem-fakeredis-devel
Version:       0.9.2
Release:       alt1
Summary:       Fake (In-memory) driver for redis-rb development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fakeredis
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fakeredis) = 0.9.2
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(redis) >= 4.8
Requires:      gem(rspec) >= 3
Conflicts:     gem(rspec) >= 4

%description   -n gem-fakeredis-devel
Fake (In-memory) driver for redis-rb development package.

Fake (In-memory) driver for redis-rb. Useful for testing environment and
machines without Redis.

%description   -n gem-fakeredis-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fakeredis.
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
%files         -n gem-fakeredis-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fakeredis-devel
%doc LICENSE README.md
%endif


%changelog
* Tue Sep 29 2026 Pavel Skrylev <majioa@altlinux.org> 0.9.2-alt1
- ^ 0.8.0 -> 0.9.2

* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1.1
- ! fixed dep to redis

* Sun Oct 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- + packaged gem with Ruby Policy 2.0
