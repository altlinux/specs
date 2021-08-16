%define        gemname fog-local

Name:          gem-fog-local
Version:       0.6.0
Release:       alt1
Summary:       Module for the 'fog' gem to support local filesystem storage
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-local
Vcs:           https://github.com/fog/fog-local.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.7 gem(bundler) < 3
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(shindo) >= 0.3 gem(shindo) < 1
BuildRequires: gem(fog-core) >= 1.27 gem(fog-core) < 3.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency fog-core >= 2.2.4,fog-core < 3
Requires:      gem(fog-core) >= 1.27 gem(fog-core) < 3.0
Obsoletes:     ruby-fog-local < %EVR
Provides:      ruby-fog-local = %EVR
Provides:      gem(fog-local) = 0.6.0


%description
This library can be used as a module for `fog` or as standalone provider to use
local filesystem storage.


%package       -n gem-fog-local-doc
Version:       0.6.0
Release:       alt1
Summary:       Module for the 'fog' gem to support local filesystem storage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-local
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-local) = 0.6.0

%description   -n gem-fog-local-doc
Module for the 'fog' gem to support local filesystem storage documentation
files.

This library can be used as a module for `fog` or as standalone provider to use
local filesystem storage.

%description   -n gem-fog-local-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-local.


%package       -n gem-fog-local-devel
Version:       0.6.0
Release:       alt1
Summary:       Module for the 'fog' gem to support local filesystem storage development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-local
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-local) = 0.6.0
Requires:      gem(bundler) >= 1.7 gem(bundler) < 3
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(shindo) >= 0.3 gem(shindo) < 1

%description   -n gem-fog-local-devel
Module for the 'fog' gem to support local filesystem storage development
package.

This library can be used as a module for `fog` or as standalone provider to use
local filesystem storage.

%description   -n gem-fog-local-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-local.


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

%files         -n gem-fog-local-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-local-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- ^ 0.5.0 -> 0.6.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
