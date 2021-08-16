%define        gemname fog-json

Name:          gem-fog-json
Version:       1.2.0.1
Release:       alt0.1
Summary:       Shared JSON related functionality for fog
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-json
Vcs:           https://github.com/fog/fog-json.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(multi_json) >= 1.10 gem(multi_json) < 2
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(minitest) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fog-core) >= 0
Requires:      gem(multi_json) >= 1.10 gem(multi_json) < 2
Obsoletes:     ruby-fog-json < %EVR
Provides:      ruby-fog-json = %EVR
Provides:      gem(fog-json) = 1.2.0.1

%ruby_use_gem_version fog-json:1.2.0.1

%description
Extraction of the JSON parsing tools shared between a number of providers in
the 'fog' gem.


%package       -n gem-fog-json-doc
Version:       1.2.0.1
Release:       alt0.1
Summary:       Shared JSON related functionality for fog documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-json
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-json) = 1.2.0.1

%description   -n gem-fog-json-doc
Shared JSON related functionality for fog documentation files.

Extraction of the JSON parsing tools shared between a number of providers in
the 'fog' gem.

%description   -n gem-fog-json-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-json.


%package       -n gem-fog-json-devel
Version:       1.2.0.1
Release:       alt0.1
Summary:       Shared JSON related functionality for fog development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-json
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-json) = 1.2.0.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(minitest) >= 0

%description   -n gem-fog-json-devel
Shared JSON related functionality for fog development package.

Extraction of the JSON parsing tools shared between a number of providers in
the 'fog' gem.

%description   -n gem-fog-json-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-json.


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

%files         -n gem-fog-json-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-json-devel
%doc README.md


%changelog
* Mon May 31 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.0.1-alt0.1
- ^ 1.2.0 -> 1.2.0[1]
- ! spec

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun Jun 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
