%define        gemname fog-ovirt

Name:          gem-fog-ovirt
Version:       2.0.1
Release:       alt1
Summary:       fog-ovirt is an ovirt provider for fog
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-ovirt
Vcs:           https://github.com/fog/fog-ovirt.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-json) >= 0
BuildRequires: gem(fog-xml) >= 0
BuildRequires: gem(ovirt-engine-sdk) >= 4.3.1
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0.52 gem(rubocop) < 2
BuildRequires: gem(shindo) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(activesupport) >= 0
Requires:      gem(fog-core) >= 0
Requires:      gem(fog-json) >= 0
Requires:      gem(fog-xml) >= 0
Requires:      gem(ovirt-engine-sdk) >= 4.3.1
Obsoletes:     ruby-fog-ovirt < %EVR
Provides:      ruby-fog-ovirt = %EVR
Provides:      gem(fog-ovirt) = 2.0.1


%description
This library can be used as a module for `fog`.


%package       -n gem-fog-ovirt-doc
Version:       2.0.1
Release:       alt1
Summary:       fog-ovirt is an ovirt provider for fog documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-ovirt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-ovirt) = 2.0.1

%description   -n gem-fog-ovirt-doc
fog-ovirt is an ovirt provider for fog documentation files.

This library can be used as a module for `fog`.

%description   -n gem-fog-ovirt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-ovirt.


%package       -n gem-fog-ovirt-devel
Version:       2.0.1
Release:       alt1
Summary:       fog-ovirt is an ovirt provider for fog development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-ovirt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-ovirt) = 2.0.1
Requires:      gem(bundler) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0.52 gem(rubocop) < 2
Requires:      gem(shindo) >= 0

%description   -n gem-fog-ovirt-devel
fog-ovirt is an ovirt provider for fog development package.

This library can be used as a module for `fog`.

%description   -n gem-fog-ovirt-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-ovirt.


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

%files         -n gem-fog-ovirt-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-ovirt-devel
%doc README.md


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- ^ 1.2.1 -> 2.0.1

* Thu Sep 26 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt1
- update (^) 1.2.0 -> 1.2.1
- fix (!) spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- Bump to 1.2.0
- Use Ruby Policy 2.0

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus
