%define        gemname fog-vsphere

Name:          gem-fog-vsphere
Version:       3.5.2
Release:       alt1.1
Summary:       Fog for vSphere
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-vsphere
Vcs:           https://github.com/fog/fog-vsphere.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(rbvmomi) >= 1.9 gem(rbvmomi) < 4
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(pry) >= 0.10 gem(pry) < 1
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(minitest) >= 5.8 gem(minitest) < 6
BuildRequires: gem(rubocop) >= 0.50.0 gem(rubocop) < 2
BuildRequires: gem(mocha) >= 1.8 gem(mocha) < 2
BuildRequires: gem(shindo) >= 0.3 gem(shindo) < 1
BuildRequires: gem(webmock) >= 3.5 gem(webmock) < 4
BuildRequires: gem(vcr) >= 4.0 gem(vcr) < 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rbvmomi >= 3.0,rbvmomi < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency vcr >= 6.0.0,vcr < 7
Requires:      gem(fog-core) >= 0
Requires:      gem(rbvmomi) >= 1.9 gem(rbvmomi) < 4
Obsoletes:     ruby-fog-vsphere < %EVR
Provides:      ruby-fog-vsphere = %EVR
Provides:      gem(fog-vsphere) = 3.5.2


%description
The VMware vSphere provider allows you to use the abstractions of the Fog cloud
services library to communicate with vSphere.


%package       -n gem-fog-vsphere-doc
Version:       3.5.2
Release:       alt1.1
Summary:       Fog for vSphere documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-vsphere
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-vsphere) = 3.5.2

%description   -n gem-fog-vsphere-doc
Fog for vSphere documentation files.

The VMware vSphere provider allows you to use the abstractions of the Fog cloud
services library to communicate with vSphere.

%description   -n gem-fog-vsphere-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-vsphere.


%package       -n gem-fog-vsphere-devel
Version:       3.5.2
Release:       alt1.1
Summary:       Fog for vSphere development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-vsphere
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-vsphere) = 3.5.2
Requires:      gem(bundler) >= 0
Requires:      gem(pry) >= 0.10 gem(pry) < 1
Requires:      gem(rake) >= 12.3.3
Requires:      gem(minitest) >= 5.8 gem(minitest) < 6
Requires:      gem(rubocop) >= 0.50.0 gem(rubocop) < 2
Requires:      gem(mocha) >= 1.8 gem(mocha) < 2
Requires:      gem(shindo) >= 0.3 gem(shindo) < 1
Requires:      gem(webmock) >= 3.5 gem(webmock) < 4
Requires:      gem(vcr) >= 4.0 gem(vcr) < 7

%description   -n gem-fog-vsphere-devel
Fog for vSphere development package.

The VMware vSphere provider allows you to use the abstractions of the Fog cloud
services library to communicate with vSphere.

%description   -n gem-fog-vsphere-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-vsphere.


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

%files         -n gem-fog-vsphere-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-vsphere-devel
%doc README.md


%changelog
* Tue Dec 06 2022 Pavel Skrylev <majioa@altlinux.org> 3.5.2-alt1.1
- !fix dep to rbvmomi gem

* Fri Oct 07 2022 Pavel Skrylev <majioa@altlinux.org> 3.5.2-alt1
- ^ 3.5.0 -> 3.5.2

* Wed Dec 16 2020 Pavel Skrylev <majioa@altlinux.org> 3.5.0-alt1
- ^ 3.2.3 -> 3.5.0
- ! spec

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.2.3-alt1
- ^ 3.2.1 -> 3.2.3
- ! spec
- * policify name

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.2.1-alt1
- updated (^) 3.1.0 -> 3.2.1

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- updated (^) 2.5.0 -> 3.1.0
- moved to (>) Ruby Policy 2.0

* Mon Jan 21 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- updated (^) 2.2.0 -> 2.5.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus
