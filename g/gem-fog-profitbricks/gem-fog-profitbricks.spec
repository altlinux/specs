%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fog-profitbricks

Name:          gem-fog-profitbricks
Version:       4.1.0.6
Epoch:         1
Release:       alt1
Summary:       Module for the 'fog' gem to support ProfitBricks
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-profitbricks
Vcs:           https://github.com/fog/fog-profitbricks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(fog-core) >= 1.42
BuildRequires: gem(fog-json) >= 1.0
BuildRequires: gem(minitest) >= 4
BuildRequires: gem(pry) >= 0.10
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(shindo) >= 0.3
BuildRequires: gem(turn) >= 0.9
BuildConflicts: gem(fog-core) >= 3
BuildConflicts: gem(fog-json) >= 2
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(shindo) >= 1
BuildConflicts: gem(turn) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0
%ruby_use_gem_dependency fog-core >= 2.2.4,fog-core < 3
Requires:      gem(fog-core) >= 1.42
Requires:      gem(fog-json) >= 1.0
Conflicts:     gem(fog-core) >= 3
Conflicts:     gem(fog-json) >= 2
Obsoletes:     ruby-fog-profitbricks < %EVR
Provides:      ruby-fog-profitbricks = %EVR
Provides:      gem(fog-profitbricks) = 4.1.0.6

%ruby_use_gem_version fog-profitbricks:4.1.0.6

%description
This library can be used as a module for 'fog' or as standalone ProfitBricks
provider.


%if_enabled    doc
%package       -n gem-fog-profitbricks-doc
Version:       4.1.0.6
Release:       alt1
Summary:       Module for the 'fog' gem to support ProfitBricks documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-profitbricks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-profitbricks) = 4.1.0.6

%description   -n gem-fog-profitbricks-doc
Module for the 'fog' gem to support ProfitBricks documentation files.

This library can be used as a module for 'fog' or as standalone ProfitBricks
provider.

%description   -n gem-fog-profitbricks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-profitbricks.
%endif


%if_enabled    devel
%package       -n gem-fog-profitbricks-devel
Version:       4.1.0.6
Release:       alt1
Summary:       Module for the 'fog' gem to support ProfitBricks development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-profitbricks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-profitbricks) = 4.1.0.6
Requires:      gem(minitest) >= 4
Requires:      gem(pry) >= 0.10
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rubocop) >= 0
Requires:      gem(shindo) >= 0.3
Requires:      gem(turn) >= 0.9
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(pry) >= 1
Conflicts:     gem(shindo) >= 1
Conflicts:     gem(turn) >= 1

%description   -n gem-fog-profitbricks-devel
Module for the 'fog' gem to support ProfitBricks development package.

This library can be used as a module for 'fog' or as standalone ProfitBricks
provider.

%description   -n gem-fog-profitbricks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-profitbricks.
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
%doc CONTRIBUTING.md CONTRIBUTORS.md LICENSE.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-fog-profitbricks-doc
%doc CONTRIBUTING.md CONTRIBUTORS.md LICENSE.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fog-profitbricks-devel
%doc CONTRIBUTING.md CONTRIBUTORS.md LICENSE.md README.md
%endif


%changelog
* Wed Aug 19 2026 Pavel Skrylev <majioa@altlinux.org> 1:4.1.0.6-alt1
- v 4.1.1.1 -> 4.1.0p6
- * rebased to upstream

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
