%define        gemname fog-vmfusion

Name:          gem-fog-vmfusion
Version:       0.1.0
Release:       alt2
Summary:       Module for the 'fog' gem to support VMWARE Fusion
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-vmfusion
Vcs:           https://github.com/fog/fog-vmfusion.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fission) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(turn) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rubocop) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fog-core) >= 0
Requires:      gem(fission) >= 0
Obsoletes:     ruby-fog-vmfusion < %EVR
Provides:      ruby-fog-vmfusion = %EVR
Provides:      gem(fog-vmfusion) = 0.1.0


%description
This library can be used as a module for `fog` or as standalone provider to use
the VMWARE FUSION in applications.


%package       -n gem-fog-vmfusion-doc
Version:       0.1.0
Release:       alt2
Summary:       Module for the 'fog' gem to support VMWARE Fusion documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-vmfusion
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-vmfusion) = 0.1.0

%description   -n gem-fog-vmfusion-doc
Module for the 'fog' gem to support VMWARE Fusion documentation files.

This library can be used as a module for `fog` or as standalone provider to use
the VMWARE FUSION in applications.

%description   -n gem-fog-vmfusion-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-vmfusion.


%package       -n gem-fog-vmfusion-devel
Version:       0.1.0
Release:       alt2
Summary:       Module for the 'fog' gem to support VMWARE Fusion development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-vmfusion
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-vmfusion) = 0.1.0
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(turn) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-fog-vmfusion-devel
Module for the 'fog' gem to support VMWARE Fusion development package.

This library can be used as a module for `fog` or as standalone provider to use
the VMWARE FUSION in applications.

%description   -n gem-fog-vmfusion-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-vmfusion.


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

%files         -n gem-fog-vmfusion-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-vmfusion-devel
%doc README.md


%changelog
* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt2
- ! spec

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
