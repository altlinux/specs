%define        gemname fog-libvirt

Name:          gem-fog-libvirt
Version:       0.9.0
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
BuildRequires: gem(fog-xml) >= 0.1.1 gem(fog-xml) < 0.2
BuildRequires: gem(ruby-libvirt) >= 0.7.0
BuildRequires: gem(json) >= 0
BuildRequires: gem(net-ssh) >= 0
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(minitest-stub-const) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(shindo) >= 0.3.4 gem(shindo) < 0.4
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(mocha) >= 1.11.2 gem(mocha) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fog-core) >= 1.27.4
Requires:      gem(fog-json) >= 0
Requires:      gem(fog-xml) >= 0.1.1 gem(fog-xml) < 0.2
Requires:      gem(ruby-libvirt) >= 0.7.0
Requires:      gem(json) >= 0
Obsoletes:     ruby-fog-libvirt < %EVR
Provides:      ruby-fog-libvirt = %EVR
Provides:      gem(fog-libvirt) = 0.9.0


%description
fog-libvirt is a libvirt provider for fog.


%package       -n gem-fog-libvirt-doc
Version:       0.9.0
Release:       alt1
Summary:       libvirt provider for fog documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-libvirt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-libvirt) = 0.9.0

%description   -n gem-fog-libvirt-doc
libvirt provider for fog documentation files.

fog-libvirt is a libvirt provider for fog.

%description   -n gem-fog-libvirt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-libvirt.


%package       -n gem-fog-libvirt-devel
Version:       0.9.0
Release:       alt1
Summary:       libvirt provider for fog development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-libvirt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-libvirt) = 0.9.0
Requires:      gem(net-ssh) >= 0
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(minitest-stub-const) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(shindo) >= 0.3.4 gem(shindo) < 0.4
Requires:      gem(simplecov) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(mocha) >= 1.11.2 gem(mocha) < 2

%description   -n gem-fog-libvirt-devel
libvirt provider for fog development package.

fog-libvirt is a libvirt provider for fog.

%description   -n gem-fog-libvirt-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-libvirt.


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

%files         -n gem-fog-libvirt-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-libvirt-devel
%doc README.md


%changelog
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
