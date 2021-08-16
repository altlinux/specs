%define        gemname fog-riakcs

Name:          gem-fog-riakcs
Version:       0.1.0
Release:       alt2
Summary:       Module for the 'fog' gem to support RiakCS
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-riakcs
Vcs:           https://github.com/fog/fog-riakcs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-json) >= 0
BuildRequires: gem(fog-xml) >= 0
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
Requires:      gem(fog-xml) >= 0
Obsoletes:     ruby-fog-riakcs < %EVR
Provides:      ruby-fog-riakcs = %EVR
Provides:      gem(fog-riakcs) = 0.1.0


%description
This library can be used as a module for `fog` or as standalone provider to use
the Riakcs in applications.


%package       -n gem-fog-riakcs-doc
Version:       0.1.0
Release:       alt2
Summary:       Module for the 'fog' gem to support RiakCS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-riakcs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-riakcs) = 0.1.0

%description   -n gem-fog-riakcs-doc
Module for the 'fog' gem to support RiakCS documentation files.

This library can be used as a module for `fog` or as standalone provider to use
the Riakcs in applications.

%description   -n gem-fog-riakcs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-riakcs.


%package       -n gem-fog-riakcs-devel
Version:       0.1.0
Release:       alt2
Summary:       Module for the 'fog' gem to support RiakCS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-riakcs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-riakcs) = 0.1.0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(minitest) >= 0 gem(minitest) < 6
Requires:      gem(shindo) >= 0
Requires:      gem(turn) >= 0
Requires:      gem(pry) >= 0 gem(pry) < 1
Requires:      gem(coveralls) >= 0
Requires:      gem(rubocop) >= 0 gem(rubocop) < 2

%description   -n gem-fog-riakcs-devel
Module for the 'fog' gem to support RiakCS development package.

This library can be used as a module for `fog` or as standalone provider to use
the Riakcs in applications.

%description   -n gem-fog-riakcs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-riakcs.


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

%files         -n gem-fog-riakcs-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-riakcs-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt2
- ! spec
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
