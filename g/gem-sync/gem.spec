%define        gemname sync

Name:          gem-sync
Version:       0.5.0
Release:       alt1
Summary:       A module that provides a two-phase lock with a counter
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/sync
Vcs:           https://github.com/ruby/sync.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(sync) = 0.5.0


%description
A module that provides a two-phase lock with a counter.


%package       -n gem-sync-doc
Version:       0.5.0
Release:       alt1
Summary:       A module that provides a two-phase lock with a counter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sync
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sync) = 0.5.0

%description   -n gem-sync-doc
A module that provides a two-phase lock with a counter documentation files.

%description   -n gem-sync-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sync.


%package       -n gem-sync-devel
Version:       0.5.0
Release:       alt1
Summary:       A module that provides a two-phase lock with a counter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sync
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sync) = 0.5.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-sync-devel
A module that provides a two-phase lock with a counter development package.

%description   -n gem-sync-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sync.


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

%files         -n gem-sync-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sync-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with Ruby Policy 2.0
