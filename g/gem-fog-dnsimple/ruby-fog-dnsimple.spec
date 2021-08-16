%define        gemname fog-dnsimple

Name:          gem-fog-dnsimple
Epoch:         1
Version:       2.1.0
Release:       alt2.1
Summary:       Module for the 'fog' gem to support DNSimple
License:       MIT
Group:         Development/Ruby
Url:           https://developer.dnsimple.com/
Vcs:           https://github.com/fog/fog-dnsimple.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.12 gem(bundler) < 3
BuildRequires: gem(rake) >= 12.0 gem(rake) < 14
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-reporters) >= 0
BuildRequires: gem(fog-core) >= 1.38 gem(fog-core) < 3
BuildRequires: gem(fog-json) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency fog-core >= 2.2.4,fog-core < 3
Requires:      gem(fog-core) >= 1.38 gem(fog-core) < 3
Requires:      gem(fog-json) >= 0
Obsoletes:     ruby-fog-dnsimple < %EVR
Provides:      ruby-fog-dnsimple = %EVR
Provides:      gem(fog-dnsimple) = 2.1.0


%description
This library currently uses the DNSimple API v2 and it is compatible with the
legacy implementation bundled with the fog gem.


%package       -n gem-fog-dnsimple-doc
Version:       2.1.0
Release:       alt2.1
Summary:       Module for the 'fog' gem to support DNSimple documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-dnsimple
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-dnsimple) = 2.1.0

%description   -n gem-fog-dnsimple-doc
Module for the 'fog' gem to support DNSimple documentation files.

This library currently uses the DNSimple API v2 and it is compatible with the
legacy implementation bundled with the fog gem.

%description   -n gem-fog-dnsimple-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-dnsimple.


%package       -n gem-fog-dnsimple-devel
Version:       2.1.0
Release:       alt2.1
Summary:       Module for the 'fog' gem to support DNSimple development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-dnsimple
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-dnsimple) = 2.1.0
Requires:      gem(bundler) >= 1.12 gem(bundler) < 3
Requires:      gem(rake) >= 12.0 gem(rake) < 14
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-reporters) >= 0

%description   -n gem-fog-dnsimple-devel
Module for the 'fog' gem to support DNSimple development package.

This library currently uses the DNSimple API v2 and it is compatible with the
legacy implementation bundled with the fog gem.

%description   -n gem-fog-dnsimple-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-dnsimple.


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

%files         -n gem-fog-dnsimple-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-dnsimple-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1:2.1.0-alt2.1
- ! spec

* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1:2.1.0-alt2
- Bump to 2.1.0
- Use Ruby Policy 2.0

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.0.0-alt1
- Reset to old version for fog.

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
