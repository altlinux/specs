%define        gemname fog-profitbricks

Name:          gem-fog-profitbricks
Version:       4.1.1.1
Release:       alt0.1
Summary:       Module for the 'fog' gem to support ProfitBricks
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-profitbricks
Vcs:           https://github.com/fog/fog-profitbricks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         version.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(fog-core) >= 1.42 gem(fog-core) <= 3
BuildRequires: gem(fog-json) >= 1.0 gem(fog-json) < 2
BuildRequires: gem(rake) >= 12.3.3 gem(rake) < 14
BuildRequires: gem(minitest) >= 4 gem(minitest) < 6
BuildRequires: gem(shindo) >= 0.3 gem(shindo) < 1
BuildRequires: gem(turn) >= 0.9 gem(turn) < 1
BuildRequires: gem(pry) >= 0.10 gem(pry) < 1
BuildRequires: gem(rubocop) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency fog-core >= 2.0,fog-core < 3
Requires:      gem(fog-core) >= 1.42 gem(fog-core) <= 3
Requires:      gem(fog-json) >= 1.0 gem(fog-json) < 2
Obsoletes:     ruby-fog-profitbricks < %EVR
Provides:      ruby-fog-profitbricks = %EVR
Provides:      gem(fog-profitbricks) = 4.1.1


%description
This library can be used as a module for 'fog' or as standalone ProfitBricks
provider.


%package       -n gem-fog-profitbricks-doc
Version:       4.1.1.1
Release:       alt0.1
Summary:       Module for the 'fog' gem to support ProfitBricks documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-profitbricks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-profitbricks) = 4.1.1

%description   -n gem-fog-profitbricks-doc
Module for the 'fog' gem to support ProfitBricks documentation files.

This library can be used as a module for 'fog' or as standalone ProfitBricks
provider.

%description   -n gem-fog-profitbricks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-profitbricks.


%package       -n gem-fog-profitbricks-devel
Version:       4.1.1.1
Release:       alt0.1
Summary:       Module for the 'fog' gem to support ProfitBricks development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-profitbricks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-profitbricks) = 4.1.1
Requires:      gem(rake) >= 12.3.3 gem(rake) < 14
Requires:      gem(minitest) >= 4 gem(minitest) < 6
Requires:      gem(shindo) >= 0.3 gem(shindo) < 1
Requires:      gem(turn) >= 0.9 gem(turn) < 1
Requires:      gem(pry) >= 0.10 gem(pry) < 1
Requires:      gem(rubocop) >= 0
Requires:      gem(fog-core) >= 2.0 gem(fog-core) < 3

%description   -n gem-fog-profitbricks-devel
Module for the 'fog' gem to support ProfitBricks development package.

This library can be used as a module for 'fog' or as standalone ProfitBricks
provider.

%description   -n gem-fog-profitbricks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-profitbricks.


%prep
%setup
%patch -p1

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

%files         -n gem-fog-profitbricks-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-profitbricks-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 4.1.1.1-alt0.1
- ! spec
- ^ 4.1.1 -> 4.1.1[1]

* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 4.1.1-alt1
- Bump to 4.1.1
- Use Ruby Policy 2.0

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1
- Initial build for Sisyphus
