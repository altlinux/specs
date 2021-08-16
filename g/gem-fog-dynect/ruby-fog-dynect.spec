%define        gemname fog-dynect

Name:          gem-fog-dynect
Epoch:         1
Version:       0.5.0
Release:       alt1
Summary:       Module for the 'fog' gem to support Dyn Managed DNS
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-dynect
Vcs:           https://github.com/fog/fog-dynect.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0 gem(bundler) < 3
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(shindo) >= 0.3 gem(shindo) < 1
BuildRequires: gem(fog-core) >= 0 gem(fog-core) < 3
BuildRequires: gem(fog-json) >= 0
BuildRequires: gem(fog-xml) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency fog-core >= 2.2.4,fog-core < 3
Requires:      gem(fog-core) >= 0 gem(fog-core) < 3
Requires:      gem(fog-json) >= 0
Requires:      gem(fog-xml) >= 0
Obsoletes:     ruby-fog-dynect < %EVR
Provides:      ruby-fog-dynect = %EVR
Provides:      gem(fog-dynect) = 0.5.0


%description
Module for the 'fog' gem to support Dyn Managed DNS http://dyn.com/.


%package       -n gem-fog-dynect-doc
Version:       0.5.0
Release:       alt1
Summary:       Module for the 'fog' gem to support Dyn Managed DNS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-dynect
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-dynect) = 0.5.0

%description   -n gem-fog-dynect-doc
Module for the 'fog' gem to support Dyn Managed DNS documentation files.

Module for the 'fog' gem to support Dyn Managed DNS http://dyn.com/.

%description   -n gem-fog-dynect-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-dynect.


%package       -n gem-fog-dynect-devel
Version:       0.5.0
Release:       alt1
Summary:       Module for the 'fog' gem to support Dyn Managed DNS http://dyn.com/ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-dynect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-dynect) = 0.5.0
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(shindo) >= 0.3 gem(shindo) < 1

%description   -n gem-fog-dynect-devel
Module for the 'fog' gem to support Dyn Managed DNS development package.

Module for the 'fog' gem to support Dyn Managed DNS http://dyn.com/.

%description   -n gem-fog-dynect-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-dynect.


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

%files         -n gem-fog-dynect-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-dynect-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1:0.5.0-alt1
- ^ 0.0.3 -> 0.5.0

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.0.3-alt1
- Reset to old version for fog.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1.2
- Rebuild for new Ruby autorequirements.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
