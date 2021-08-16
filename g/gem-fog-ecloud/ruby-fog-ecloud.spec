%define        gemname fog-ecloud

Name:          gem-fog-ecloud
Version:       0.3.0
Release:       alt2
Summary:       Module for the 'fog' gem to support Terremark Enterprise Cloud
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-ecloud
Vcs:           https://github.com/fog/fog-ecloud.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-xml) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(shindo) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(turn) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rubocop) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fog-core) >= 0
Requires:      gem(fog-xml) >= 0
Obsoletes:     ruby-fog-ecloud < %EVR
Provides:      ruby-fog-ecloud = %EVR
Provides:      gem(fog-ecloud) = 0.3.0


%description
This library can be used as a module for `fog` or as standalone provider to use
the Terremark EnterpriseCloud in applications.


%package       -n gem-fog-ecloud-doc
Version:       0.3.0
Release:       alt2
Summary:       Module for the 'fog' gem to support Terremark Enterprise Cloud documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-ecloud
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-ecloud) = 0.3.0

%description   -n gem-fog-ecloud-doc
Module for the 'fog' gem to support Terremark Enterprise Cloud documentation
files.

This library can be used as a module for `fog` or as standalone provider to use
the Terremark EnterpriseCloud in applications.

%description   -n gem-fog-ecloud-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-ecloud.


%package       -n gem-fog-ecloud-devel
Version:       0.3.0
Release:       alt2
Summary:       Module for the 'fog' gem to support Terremark Enterprise Cloud development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-ecloud
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-ecloud) = 0.3.0
Requires:      gem(rake) >= 0
Requires:      gem(shindo) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(turn) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-fog-ecloud-devel
Module for the 'fog' gem to support Terremark Enterprise Cloud development
package.

This library can be used as a module for `fog` or as standalone provider to use
the Terremark EnterpriseCloud in applications.

%description   -n gem-fog-ecloud-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-ecloud.


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

%files         -n gem-fog-ecloud-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-ecloud-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt2
- ! spec

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
