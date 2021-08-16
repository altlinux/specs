%define        gemname fog-serverlove

Name:          gem-fog-serverlove
Version:       0.1.2
Release:       alt2
Summary:       Module for the 'fog' gem to support ServerLove
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-serverlove
Vcs:           https://github.com/fog/fog-serverlove.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-json) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(shindo) >= 0
BuildRequires: gem(turn) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rubocop) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fog-core) >= 0
Requires:      gem(fog-json) >= 0
Obsoletes:     ruby-fog-serverlove < %EVR
Provides:      ruby-fog-serverlove = %EVR
Provides:      gem(fog-serverlove) = 0.1.2


%description
This library can be used as a module for `fog` or as standalone provider to use
the ServerLove in applications.


%package       -n gem-fog-serverlove-doc
Version:       0.1.2
Release:       alt2
Summary:       Module for the 'fog' gem to support ServerLove documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-serverlove
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-serverlove) = 0.1.2

%description   -n gem-fog-serverlove-doc
Module for the 'fog' gem to support ServerLove documentation files.

This library can be used as a module for `fog` or as standalone provider to use
the ServerLove in applications.

%description   -n gem-fog-serverlove-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-serverlove.


%package       -n gem-fog-serverlove-devel
Version:       0.1.2
Release:       alt2
Summary:       Module for the 'fog' gem to support ServerLove development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-serverlove
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-serverlove) = 0.1.2
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(shindo) >= 0
Requires:      gem(turn) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-fog-serverlove-devel
Module for the 'fog' gem to support ServerLove development package.

This library can be used as a module for `fog` or as standalone provider to use
the ServerLove in applications.

%description   -n gem-fog-serverlove-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-serverlove.


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

%files         -n gem-fog-serverlove-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-serverlove-devel
%doc README.md


%changelog
* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt2
- ! spec

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus
