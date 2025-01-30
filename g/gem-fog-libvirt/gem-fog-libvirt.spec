%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fog-libvirt

Name:          gem-fog-libvirt
Version:       0.13.2
Release:       alt1
Summary:       libvirt provider for fog
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-libvirt
Vcs:           https://github.com/fog/fog-libvirt.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(fog-core) >= 1.27.4
BuildRequires: gem(fog-json) >= 0
BuildRequires: gem(fog-xml) >= 0.1.1
BuildRequires: gem(json) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(mocha) >= 1.11.2
BuildRequires: gem(net-ssh) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(ruby-libvirt) >= 0.7.0
BuildRequires: gem(shindo) >= 0.3.4
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(fog-xml) >= 0.2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(shindo) >= 0.4
%if_enabled check
BuildRequires: gem(netrc) >= 0
BuildRequires: gem(octokit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
Requires:      ruby >= 2.7
Requires:      gem(fog-core) >= 1.27.4
Requires:      gem(fog-json) >= 0
Requires:      gem(fog-xml) >= 0.1.1
Requires:      gem(json) >= 0
Requires:      gem(ruby-libvirt) >= 0.7.0
Conflicts:     gem(fog-xml) >= 0.2
Obsoletes:     ruby-fog-libvirt < %EVR
Provides:      ruby-fog-libvirt = %EVR
Provides:      fog-libvirt = %EVR
Provides:      gem(fog-libvirt) = 0.13.2

%description
fog-libvirt is a libvirt provider for fog.


%if_enabled    doc
%package       -n gem-fog-libvirt-doc
Version:       0.13.2
Release:       alt1
Summary:       libvirt provider for fog documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-libvirt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-libvirt) = 0.13.2

%description   -n gem-fog-libvirt-doc
libvirt provider for fog documentation files.

fog-libvirt is a libvirt provider for fog.

%description   -n gem-fog-libvirt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-libvirt.
%endif


%if_enabled    devel
%package       -n gem-fog-libvirt-devel
Version:       0.13.2
Release:       alt1
Summary:       libvirt provider for fog development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-libvirt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-libvirt) = 0.13.2
Requires:      gem(minitest) >= 5.0
Requires:      gem(mocha) >= 1.11.2
Requires:      gem(net-ssh) >= 0
Requires:      gem(netrc) >= 0
Requires:      gem(octokit) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(shindo) >= 0.3.4
Requires:      gem(simplecov) >= 0
Requires:      gem(yard) >= 0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(shindo) >= 0.4

%description   -n gem-fog-libvirt-devel
libvirt provider for fog development package.

fog-libvirt is a libvirt provider for fog.

%description   -n gem-fog-libvirt-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-libvirt.
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
%doc CONTRIBUTORS.md LICENSE.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-fog-libvirt-doc
%doc CONTRIBUTORS.md LICENSE.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fog-libvirt-devel
%doc CONTRIBUTORS.md LICENSE.md README.md
%endif


%changelog
* Mon Jan 13 2025 Pavel Skrylev <majioa@altlinux.org> 0.13.2-alt1
- ^ 0.9.0.1 -> 0.13.2

* Fri Oct 07 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.0.1-alt0.1
- ^ 0.9.0 -> 0.9.0.1

* Thu Oct 21 2021 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- ^ 0.8.0 -> 0.9.0

* Wed Jun 16 2021 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- ^ 0.7.0 -> 0.8.0

* Wed Dec 16 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- ^ 0.6.0 -> 0.7.0
- * policify name

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- > Ruby Policy 2.0
- ^ 0.5.0 -> 0.6.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 23 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
