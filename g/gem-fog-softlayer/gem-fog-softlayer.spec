%define        gemname fog-softlayer

Name:          gem-fog-softlayer
Version:       1.1.4.8
Release:       alt0.1
Summary:       SoftLayer module for fog
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-softlayer
Vcs:           https://github.com/fog/fog-softlayer.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(netrc) >= 0
BuildRequires: gem(octokit) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rbvmomi) >= 3.0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(thor) >= 0
BuildRequires: gem(rbovirt) >= 0.0.24
BuildRequires: gem(shindo) >= 0.3.4
BuildRequires: gem(fission) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(osrcry) >= 0
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-json) >= 0
BuildConflicts: gem(rbovirt) >= 1
BuildConflicts: gem(rbvmomi) >= 4
BuildConflicts: gem(shindo) >= 0.4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rbovirt >= 0.0.24,rbovirt < 1
Requires:      gem(fog-core) >= 0
Requires:      gem(fog-json) >= 0
Obsoletes:     ruby-fog-softlayer < %EVR
Provides:      ruby-fog-softlayer = %EVR
Provides:      gem(fog-softlayer) = 1.1.4.8

%ruby_use_gem_version fog-softlayer:1.1.4.8

%description
Module for the 'fog' gem to support SoftLayer Cloud.


%package       -n gem-fog-softlayer-doc
Version:       1.1.4.8
Release:       alt0.1
Summary:       SoftLayer module for fog documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-softlayer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-softlayer) = 1.1.4.8

%description   -n gem-fog-softlayer-doc
SoftLayer module for fog documentation files.

Module for the 'fog' gem to support SoftLayer Cloud.

%description   -n gem-fog-softlayer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-softlayer.


%package       -n gem-fog-softlayer-devel
Version:       1.1.4.8
Release:       alt0.1
Summary:       SoftLayer module for fog development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-softlayer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-softlayer) = 1.1.4.8
Requires:      gem(coveralls) >= 0
Requires:      gem(netrc) >= 0
Requires:      gem(octokit) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rbvmomi) >= 3.0
Requires:      gem(yard) >= 0
Requires:      gem(thor) >= 0
Requires:      gem(rbovirt) >= 0.0.24
Requires:      gem(shindo) >= 0.3.4
Requires:      gem(fission) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(osrcry) >= 0
Conflicts:     gem(rbovirt) >= 1
Conflicts:     gem(rbvmomi) >= 4
Conflicts:     gem(shindo) >= 0.4

%description   -n gem-fog-softlayer-devel
SoftLayer module for fog development package.

Module for the 'fog' gem to support SoftLayer Cloud.

%description   -n gem-fog-softlayer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-softlayer.


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

%files         -n gem-fog-softlayer-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-softlayer-devel
%doc README.md


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.4.8-alt0.1
- ^ 1.1.4 -> 1.1.4p8

* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.4-alt2
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1
- Initial build for Sisyphus
