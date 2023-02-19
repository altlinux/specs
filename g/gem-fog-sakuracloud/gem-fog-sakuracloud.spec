%define        gemname fog-sakuracloud

Name:          gem-fog-sakuracloud
Version:       1.7.5.4
Release:       alt0.1
Summary:       Module for the 'fog' gem to support Sakura no Cloud
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-sakuracloud
Vcs:           https://github.com/fog/fog-sakuracloud.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rbvmomi2) >= 3.0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(thor) >= 0
BuildRequires: gem(rbovirt) >= 0.0.24
BuildRequires: gem(shindo) >= 0.3.4
BuildRequires: gem(fission) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-json) >= 0
BuildConflicts: gem(rbovirt) >= 1
BuildConflicts: gem(rbvmomi2) >= 4
BuildConflicts: gem(shindo) >= 0.4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rbovirt >= 0.0.24,rbovirt < 1
Requires:      gem(fog-core) >= 0
Requires:      gem(fog-json) >= 0
Obsoletes:     ruby-fog-sakuracloud < %EVR
Provides:      ruby-fog-sakuracloud = %EVR
Provides:      gem(fog-sakuracloud) = 1.7.5.4

%ruby_use_gem_version fog-sakuracloud:1.7.5.4

%description
Module for the 'fog' gem to support Sakura no Cloud.


%package       -n gem-fog-sakuracloud-doc
Version:       1.7.5.4
Release:       alt0.1
Summary:       Module for the 'fog' gem to support Sakura no Cloud documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-sakuracloud
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-sakuracloud) = 1.7.5.4

%description   -n gem-fog-sakuracloud-doc
Module for the 'fog' gem to support Sakura no Cloud documentation files.

%description   -n gem-fog-sakuracloud-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-sakuracloud.


%package       -n gem-fog-sakuracloud-devel
Version:       1.7.5.4
Release:       alt0.1
Summary:       Module for the 'fog' gem to support Sakura no Cloud development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-sakuracloud
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-sakuracloud) = 1.7.5.4
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rbvmomi2) >= 3.0
Requires:      gem(yard) >= 0
Requires:      gem(thor) >= 0
Requires:      gem(rbovirt) >= 0.0.24
Requires:      gem(shindo) >= 0.3.4
Requires:      gem(fission) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rubocop) >= 0
Conflicts:     gem(rbvmomi2) >= 4
Conflicts:     gem(shindo) >= 0.4

%description   -n gem-fog-sakuracloud-devel
Module for the 'fog' gem to support Sakura no Cloud development package.

%description   -n gem-fog-sakuracloud-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-sakuracloud.


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

%files         -n gem-fog-sakuracloud-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-sakuracloud-devel
%doc README.md


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 1.7.5.4-alt0.1
- ^ 1.7.5 -> 1.7.5p4

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.5-alt2
- ! spec

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.5-alt1
- Initial build for Sisyphus
