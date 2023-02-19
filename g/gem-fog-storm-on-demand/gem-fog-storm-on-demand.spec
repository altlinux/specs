%define        gemname fog-storm_on_demand

Name:          gem-fog-storm-on-demand
Version:       0.1.1
Release:       alt2.1
Summary:       Module for the 'fog' gem to support StormOnDemand
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-storm_on_demand
Vcs:           https://github.com/fog/fog-storm_on_demand.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(turn) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-json) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names fog-storm_on_demand,fog-storm-on-demand
Requires:      gem(fog-core) >= 0
Requires:      gem(fog-json) >= 0
Obsoletes:     ruby-fog-storm_on_demand < %EVR
Provides:      ruby-fog-storm_on_demand = %EVR
Provides:      gem(fog-storm_on_demand) = 0.1.1


%description
This library can be used as a module for `fog` or as standalone provider to use
the StormOnDemand in applications.


%package       -n gem-fog-storm-on-demand-doc
Version:       0.1.1
Release:       alt2.1
Summary:       Module for the 'fog' gem to support StormOnDemand documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-storm_on_demand
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-storm_on_demand) = 0.1.1

%description   -n gem-fog-storm-on-demand-doc
Module for the 'fog' gem to support StormOnDemand documentation files.

This library can be used as a module for `fog` or as standalone provider to use
the StormOnDemand in applications.

%description   -n gem-fog-storm-on-demand-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-storm_on_demand.


%package       -n gem-fog-storm-on-demand-devel
Version:       0.1.1
Release:       alt2.1
Summary:       Module for the 'fog' gem to support StormOnDemand development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-storm_on_demand
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-storm_on_demand) = 0.1.1
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(turn) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-fog-storm-on-demand-devel
Module for the 'fog' gem to support StormOnDemand development package.

This library can be used as a module for `fog` or as standalone provider to use
the StormOnDemand in applications.

%description   -n gem-fog-storm-on-demand-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-storm_on_demand.


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

%files         -n gem-fog-storm-on-demand-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-storm-on-demand-devel
%doc README.md


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt2.1
- ! by closing build deps under check condition

* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt2
- ! spec

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus
