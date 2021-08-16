%define        gemname fog-cloudatcost

Name:          gem-fog-cloudatcost
Epoch:         1
Version:       0.4.0
Release:       alt2.1
Summary:       Module for the 'fog' gem to support CloudAtCost Services
License:       MIT
Group:         Development/Ruby
Url:           http://panel.cloudatcost.com/
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubyzip) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-json) >= 0
BuildRequires: gem(ipaddress) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fog-core) >= 0
Requires:      gem(fog-json) >= 0
Requires:      gem(ipaddress) >= 0
Obsoletes:     ruby-fog-cloudatcost < %EVR
Provides:      ruby-fog-cloudatcost = %EVR
Provides:      gem(fog-cloudatcost) = 0.4.0

%description
This library can be used as a module for `fog` or as standalone provider to use
the CloudAtCost in applications.


%package       -n gem-fog-cloudatcost-doc
Version:       0.4.0
Release:       alt2.1
Summary:       Module for the 'fog' gem to support CloudAtCost Services documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-cloudatcost
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-cloudatcost) = 0.4.0

%description   -n gem-fog-cloudatcost-doc
Module for the 'fog' gem to support CloudAtCost Services documentation files.

This library can be used as a module for `fog` or as standalone provider to use
the CloudAtCost in applications.

%description   -n gem-fog-cloudatcost-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-cloudatcost.


%package       -n gem-fog-cloudatcost-devel
Version:       0.4.0
Release:       alt2.1
Summary:       Module for the 'fog' gem to support CloudAtCost Services development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-cloudatcost
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-cloudatcost) = 0.4.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubyzip) >= 0
Requires:      gem(simplecov) >= 0

%description   -n gem-fog-cloudatcost-devel
Module for the 'fog' gem to support CloudAtCost Services development package.

This library can be used as a module for `fog` or as standalone provider to use
the CloudAtCost in applications.

%description   -n gem-fog-cloudatcost-devel -l ru_RU.UTF-8

Файлы для разработки самоцвета fog-cloudatcost.


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

%files         -n gem-fog-cloudatcost-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-cloudatcost-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1:0.4.0-alt2.1
- ! spec

* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.4.0-alt2
- Use Ruby Policy 2.0

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.1.2-alt1
- Reset to old version for fog.

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt1
- New version.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus
