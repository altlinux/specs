%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fog-xenserver

Name:          gem-fog-xenserver
Version:       1.0.0.5
Release:       alt0.1
Summary:       Module for the 'fog' gem to support XENSERVER
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-xenserver
Vcs:           https://github.com/fog/fog-xenserver.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-xml) >= 0
BuildRequires: gem(jazz_fingers) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(turn) >= 0
BuildRequires: gem(vcr) >= 0
BuildRequires: gem(webmock) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.0
Requires:      gem(fog-core) >= 0
Requires:      gem(fog-xml) >= 0
Obsoletes:     ruby-fog-xenserver < %EVR
Provides:      ruby-fog-xenserver = %EVR
Provides:      gem(fog-xenserver) = 1.0.0.5

%ruby_use_gem_version fog-xenserver:1.0.0.5

%description
Module for the 'fog' gem to support XENSERVER.


%if_enabled    doc
%package       -n gem-fog-xenserver-doc
Version:       1.0.0.5
Release:       alt0.1
Summary:       Module for the 'fog' gem to support XENSERVER documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-xenserver
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-xenserver) = 1.0.0.5

%description   -n gem-fog-xenserver-doc
Module for the 'fog' gem to support XENSERVER documentation files.

%description   -n gem-fog-xenserver-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-xenserver.
%endif


%if_enabled    devel
%package       -n gem-fog-xenserver-devel
Version:       1.0.0.5
Release:       alt0.1
Summary:       Module for the 'fog' gem to support XENSERVER development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-xenserver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-xenserver) = 1.0.0.5
Requires:      gem(coveralls) >= 0
Requires:      gem(jazz_fingers) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(turn) >= 0
Requires:      gem(vcr) >= 0
Requires:      gem(webmock) >= 0

%description   -n gem-fog-xenserver-devel
Module for the 'fog' gem to support XENSERVER development package.

%description   -n gem-fog-xenserver-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-xenserver.
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
%files         -n gem-fog-xenserver-doc
%doc CONTRIBUTING.md CONTRIBUTORS.md LICENSE.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fog-xenserver-devel
%doc CONTRIBUTING.md CONTRIBUTORS.md LICENSE.md README.md
%endif


%changelog
* Wed Oct 22 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.0.5-alt0.1
- ^ 1.0.0 -> 1.0.0p5

* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.3.0 -> 1.0.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
