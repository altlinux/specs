%define        gemname fog-internet-archive

Name:          gem-fog-internet-archive
Version:       0.0.2
Release:       alt1
Summary:       Internet Archive Storage support for Fog
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-internet-archive
Vcs:           https://github.com/fog/fog-internet-archive.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-json) >= 0
BuildRequires: gem(fog-xml) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(shindo) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(vcr) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(mime-types) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fog-core) >= 0 gem(fog-core) < 3
Requires:      gem(fog-json) >= 0
Requires:      gem(fog-xml) >= 0
Obsoletes:     ruby-fog-internet-archive < %EVR
Provides:      ruby-fog-internet-archive = %EVR
Provides:      gem(fog-internet-archive) = 0.0.2


%description
Internet Archive Storage support for Fog.


%package       -n gem-fog-internet-archive-doc
Version:       0.0.2
Release:       alt1
Summary:       Internet Archive Storage support for Fog documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-internet-archive
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-internet-archive) = 0.0.2

%description   -n gem-fog-internet-archive-doc
Internet Archive Storage support for Fog documentation files.

%description   -n gem-fog-internet-archive-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-internet-archive.


%package       -n gem-fog-internet-archive-devel
Version:       0.0.2
Release:       alt1
Summary:       Internet Archive Storage support for Fog development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-internet-archive
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-internet-archive) = 0.0.2
Requires:      gem(rake) >= 0
Requires:      gem(shindo) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(vcr) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(mime-types) >= 0

%description   -n gem-fog-internet-archive-devel
Internet Archive Storage support for Fog development package.

%description   -n gem-fog-internet-archive-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-internet-archive.


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

%files         -n gem-fog-internet-archive-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-internet-archive-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.2-alt1
- ^ 0.0.1 -> 0.0.2

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus
