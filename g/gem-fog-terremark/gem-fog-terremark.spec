%define        gemname fog-terremark

Name:          gem-fog-terremark
Version:       0.1.0
Release:       alt2.1
Summary:       Module for the 'fog' gem to support Terremark vCloud
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-terremark
Vcs:           https://github.com/fog/fog-terremark.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(turn) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(vcr) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-xml) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fog-core) >= 0
Requires:      gem(fog-xml) >= 0
Obsoletes:     ruby-fog-terremark < %EVR
Provides:      ruby-fog-terremark = %EVR
Provides:      gem(fog-terremark) = 0.1.0


%description
This library can be used as a module for `fog` or as standalone provider to use
the Terremark vCloud in applications.


%package       -n gem-fog-terremark-doc
Version:       0.1.0
Release:       alt2.1
Summary:       Module for the 'fog' gem to support Terremark vCloud documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-terremark
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-terremark) = 0.1.0

%description   -n gem-fog-terremark-doc
Module for the 'fog' gem to support Terremark vCloud documentation files.

This library can be used as a module for `fog` or as standalone provider to use
the Terremark vCloud in applications.

%description   -n gem-fog-terremark-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-terremark.


%package       -n gem-fog-terremark-devel
Version:       0.1.0
Release:       alt2.1
Summary:       Module for the 'fog' gem to support Terremark vCloud development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-terremark
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-terremark) = 0.1.0
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(turn) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(vcr) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-fog-terremark-devel
Module for the 'fog' gem to support Terremark vCloud development package.

This library can be used as a module for `fog` or as standalone provider to use
the Terremark vCloud in applications.

%description   -n gem-fog-terremark-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-terremark.


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

%files         -n gem-fog-terremark-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-terremark-devel
%doc README.md


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt2.1
- ! by closing build deps under check condition

* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt2
- ! spec

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
