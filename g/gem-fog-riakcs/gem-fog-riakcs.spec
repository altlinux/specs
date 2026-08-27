%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fog-riakcs

Name:          gem-fog-riakcs
Version:       0.1.0
Release:       alt3
Summary:       Module for the 'fog' gem to support RiakCS
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-riakcs
Vcs:           https://github.com/fog/fog-riakcs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-json) >= 0
BuildRequires: gem(fog-xml) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(shindo) >= 0
BuildRequires: gem(turn) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fog-core) >= 0
Requires:      gem(fog-json) >= 0
Requires:      gem(fog-xml) >= 0
Obsoletes:     ruby-fog-riakcs < %EVR
Provides:      ruby-fog-riakcs = %EVR
Provides:      gem(fog-riakcs) = 0.1.0

%description
Module for the 'fog' gem to support RiakCS


%if_enabled    doc
%package       -n gem-fog-riakcs-doc
Version:       0.1.0
Release:       alt3
Summary:       Module for the 'fog' gem to support RiakCS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-riakcs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-riakcs) = 0.1.0

%description   -n gem-fog-riakcs-doc
Module for the 'fog' gem to support RiakCS documentation files.

%description   -n gem-fog-riakcs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-riakcs.
%endif


%if_enabled    devel
%package       -n gem-fog-riakcs-devel
Version:       0.1.0
Release:       alt3
Summary:       Module for the 'fog' gem to support RiakCS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-riakcs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-riakcs) = 0.1.0
Requires:      gem(coveralls) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(shindo) >= 0
Requires:      gem(turn) >= 0

%description   -n gem-fog-riakcs-devel
Module for the 'fog' gem to support RiakCS development package.

%description   -n gem-fog-riakcs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-riakcs.
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
%files         -n gem-fog-riakcs-doc
%doc CONTRIBUTING.md CONTRIBUTORS.md LICENSE.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fog-riakcs-devel
%doc CONTRIBUTING.md CONTRIBUTORS.md LICENSE.md README.md
%endif


%changelog
* Wed Aug 19 2026 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt3
- * rebased to upstream

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt2
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
