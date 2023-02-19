%define        gemname fog-atmos

Name:          gem-fog-atmos
Version:       0.1.0.1
Release:       alt0.1
Summary:       Module for the 'fog' gem to support Atmos Cloud Storage
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-atmos
Vcs:           https://github.com/fog/fog-atmos.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(shindo) >= 0
BuildRequires: gem(turn) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-xml) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fog-core) >= 0
Requires:      gem(fog-xml) >= 0
Obsoletes:     ruby-fog-atmos
Provides:      ruby-fog-atmos
Provides:      gem(fog-atmos) = 0.1.0.1

%ruby_use_gem_version fog-atmos:0.1.0.1

%description
Module for the 'fog' gem to support Atmos Cloud Storage.


%package       -n gem-fog-atmos-doc
Version:       0.1.0.1
Release:       alt0.1
Summary:       Module for the 'fog' gem to support Atmos Cloud Storage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-atmos
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-atmos) = 0.1.0.1

%description   -n gem-fog-atmos-doc
Module for the 'fog' gem to support Atmos Cloud Storage documentation files.

%description   -n gem-fog-atmos-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-atmos.


%package       -n gem-fog-atmos-devel
Version:       0.1.0.1
Release:       alt0.1
Summary:       Module for the 'fog' gem to support Atmos Cloud Storage development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-atmos
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-atmos) = 0.1.0.1
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(shindo) >= 0
Requires:      gem(turn) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-fog-atmos-devel
Module for the 'fog' gem to support Atmos Cloud Storage development package.

%description   -n gem-fog-atmos-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-atmos.


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

%files         -n gem-fog-atmos-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-atmos-devel
%doc README.md


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.0.1-alt0.1
- ^ 0.1.0 -> 0.1.0p1

* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt2
- > Ruby Policy 2.0
- ! spec

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
