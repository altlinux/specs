%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fog-vsphere

Name:          gem-fog-vsphere
Version:       3.7.3
Release:       alt1
Summary:       Fog for vSphere
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-vsphere
Vcs:           https://github.com/fog/fog-vsphere.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby
BuildRequires(pre): setup-rb
BuildRequires(pre): rake
%if_enabled check
BuildRequires: gem(base64) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(codeclimate-test-reporter) >= 0
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(mocha) >= 2.2
BuildRequires: gem(ostruct) >= 0
BuildRequires: gem(pry) >= 0.10
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rbvmomi2) >= 3.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-minitest) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(shindo) >= 0.3
BuildRequires: gem(vcr) >= 6.0
BuildRequires: gem(webmock) >= 3.5
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rbvmomi2) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(shindo) >= 1
BuildConflicts: gem(vcr) >= 7
BuildConflicts: gem(webmock) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      ruby >= 2.7
Requires:      gem(base64) >= 0
Requires:      gem(fog-core) >= 0
Requires:      gem(ostruct) >= 0
Requires:      gem(rbvmomi2) >= 3.0
Conflicts:     gem(rbvmomi2) >= 4
Obsoletes:     ruby-fog-vsphere < %EVR
Provides:      ruby-fog-vsphere = %EVR
Provides:      gem(fog-vsphere) = 3.7.3

%description
The VMware vSphere provider allows you to use the abstractions of the Fog cloud
services library to communicate with vSphere.


%if_enabled    doc
%package       -n gem-fog-vsphere-doc
Version:       3.7.3
Release:       alt1
Summary:       Fog for vSphere documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-vsphere
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-vsphere) = 3.7.3

%description   -n gem-fog-vsphere-doc
Fog for vSphere documentation files.

The VMware vSphere provider allows you to use the abstractions of the Fog cloud
services library to communicate with vSphere.

%description   -n gem-fog-vsphere-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-vsphere.
%endif


%if_enabled    devel
%package       -n gem-fog-vsphere-devel
Version:       3.7.3
Release:       alt1
Summary:       Fog for vSphere development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-vsphere
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-vsphere) = 3.7.3
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(mocha) >= 2.2
Requires:      gem(pry) >= 0.10
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-minitest) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(shindo) >= 0.3
Requires:      gem(vcr) >= 6.0
Requires:      gem(webmock) >= 3.5
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(shindo) >= 1
Conflicts:     gem(vcr) >= 7
Conflicts:     gem(webmock) >= 4

%description   -n gem-fog-vsphere-devel
Fog for vSphere development package.

The VMware vSphere provider allows you to use the abstractions of the Fog cloud
services library to communicate with vSphere.

%description   -n gem-fog-vsphere-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-vsphere.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md CONTRIBUTORS.md LICENSE.md README.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-fog-vsphere-doc
%doc CHANGELOG.md CONTRIBUTORS.md LICENSE.md README.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fog-vsphere-devel
%doc CHANGELOG.md CONTRIBUTORS.md LICENSE.md README.md CONTRIBUTING.md
%endif


%changelog
* Wed Apr 29 2026 Pavel Skrylev <majioa@altlinux.org> 3.7.3-alt1
- ^ 3.7.0 -> 3.7.3

* Mon Jan 13 2025 Pavel Skrylev <majioa@altlinux.org> 3.7.0-alt1
- ^ 3.5.2 -> 3.7.0

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
