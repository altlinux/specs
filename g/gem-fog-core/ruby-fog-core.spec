%define        gemname fog-core

Name:          gem-fog-core
Epoch:         1
Version:       2.2.4
Release:       alt1
Summary:       fog's core, shared behaviors without API and provider specifics
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-core
Vcs:           https://github.com/fog/fog-core.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(builder) >= 0
BuildRequires: gem(mime-types) >= 0
BuildRequires: gem(excon) >= 0.71 gem(excon) < 1
BuildRequires: gem(formatador) >= 0.2 gem(formatador) < 1
BuildRequires: gem(tins) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-stub-const) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(thor) >= 0
BuildRequires: gem(yard) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
Requires:      gem(builder) >= 0
Requires:      gem(mime-types) >= 0
Requires:      gem(excon) >= 0.71 gem(excon) < 1
Requires:      gem(formatador) >= 0.2 gem(formatador) < 1
Obsoletes:     ruby-fog-core < %EVR
Provides:      ruby-fog-core = %EVR
Provides:      gem(fog-core) = 2.2.4


%description
Shared classes and tests for fog providers and services.


%package       -n gem-fog-core-doc
Version:       2.2.4
Release:       alt1
Summary:       fog's core, shared behaviors without API and provider specifics documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-core) = 2.2.4

%description   -n gem-fog-core-doc
fog's core, shared behaviors without API and provider specifics documentation
files.

Shared classes and tests for fog providers and services.

%description   -n gem-fog-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-core.


%package       -n gem-fog-core-devel
Version:       2.2.4
Release:       alt1
Summary:       fog's core, shared behaviors without API and provider specifics development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-core) = 2.2.4
Requires:      gem(tins) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-stub-const) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(thor) >= 0
Requires:      gem(yard) >= 0

%description   -n gem-fog-core-devel
fog's core, shared behaviors without API and provider specifics development
package.

Shared classes and tests for fog providers and services.

%description   -n gem-fog-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-core.


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

%files         -n gem-fog-core-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-core-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 1:2.2.4-alt1
- ^ 2.1.2 -> 2.2.4

* Wed Jun 05 2019 Pavel Skrylev <majioa@altlinux.org> 1:2.1.2-alt1
- Bump to 2.1.2
- Use Ruby Policy 2.0

* Wed Aug 29 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.45.0-alt1
- Decrease version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 23 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
