%define        gemname fog-powerdns

Name:          gem-fog-powerdns
Version:       0.2.0
Release:       alt2
Summary:       Module for the 'fog' gem to support PowerDNS
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-powerdns
Vcs:           https://github.com/fog/fog-powerdns.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0 gem(bundler) < 3
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(rubocop) >= 0 gem(rubocop) < 2
BuildRequires: gem(fog-core) >= 0 gem(fog-core) < 3
BuildRequires: gem(fog-json) >= 0
BuildRequires: gem(fog-xml) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency fog-core >= 2.2.4,fog-core < 3
Requires:      gem(fog-core) >= 0 gem(fog-core) < 3
Requires:      gem(fog-json) >= 0
Requires:      gem(fog-xml) >= 0
Obsoletes:     ruby-fog-powerdns < %EVR
Provides:      ruby-fog-powerdns = %EVR
Provides:      gem(fog-powerdns) = 0.2.0


%description
This library can be used as a module for 'fog' or as a standalone provider to
use PowerDNS DNS services in applications.


%package       -n gem-fog-powerdns-doc
Version:       0.2.0
Release:       alt2
Summary:       Module for the 'fog' gem to support PowerDNS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-powerdns
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-powerdns) = 0.2.0

%description   -n gem-fog-powerdns-doc
Module for the 'fog' gem to support PowerDNS documentation files.

This library can be used as a module for 'fog' or as a standalone provider to
use PowerDNS DNS services in applications.

%description   -n gem-fog-powerdns-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-powerdns.


%package       -n gem-fog-powerdns-devel
Version:       0.2.0
Release:       alt2
Summary:       Module for the 'fog' gem to support PowerDNS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-powerdns
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-powerdns) = 0.2.0
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rubocop) >= 0 gem(rubocop) < 2

%description   -n gem-fog-powerdns-devel
Module for the 'fog' gem to support PowerDNS development package.

This library can be used as a module for 'fog' or as a standalone provider to
use PowerDNS DNS services in applications.

%description   -n gem-fog-powerdns-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-powerdns.


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

%files         -n gem-fog-powerdns-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-powerdns-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt2
- ! spec

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.0-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.2-alt1
- New version.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
