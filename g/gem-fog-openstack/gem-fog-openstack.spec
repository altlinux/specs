%define        gemname fog-openstack

Name:          gem-fog-openstack
Version:       1.1.0
Release:       alt1
Summary:       Fog for OpenStack Platform
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-openstack
Vcs:           https://github.com/fog/fog-openstack.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(mime-types) >= 0
BuildRequires: gem(mime-types-data) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(shindo) >= 0.3
BuildRequires: gem(vcr) >= 0
BuildRequires: gem(webmock) >= 1.24.6
BuildRequires: gem(fog-core) >= 2.1
BuildRequires: gem(fog-json) >= 1.0
BuildConflicts: gem(shindo) >= 1
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(fog-core) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
Requires:      gem(fog-core) >= 2.1
Requires:      gem(fog-json) >= 1.0
Conflicts:     gem(fog-core) >= 3
Obsoletes:     ruby-fog-openstack < %EVR
Provides:      ruby-fog-openstack = %EVR
Provides:      gem(fog-openstack) = 1.1.0


%description
This is the plugin Gem to talk to OpenStack clouds via fog.


%package       -n gem-fog-openstack-doc
Version:       1.1.0
Release:       alt1
Summary:       Fog for OpenStack Platform documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-openstack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-openstack) = 1.1.0

%description   -n gem-fog-openstack-doc
Fog for OpenStack Platform documentation files.

This is the plugin Gem to talk to OpenStack clouds via fog.

%description   -n gem-fog-openstack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-openstack.


%package       -n gem-fog-openstack-devel
Version:       1.1.0
Release:       alt1
Summary:       Fog for OpenStack Platform development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-openstack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-openstack) = 1.1.0
Requires:      gem(bundler) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(mime-types) >= 0
Requires:      gem(mime-types-data) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rubocop) >= 0
Requires:      gem(shindo) >= 0.3
Requires:      gem(vcr) >= 0
Requires:      gem(webmock) >= 1.24.6
Conflicts:     gem(shindo) >= 1
Conflicts:     gem(webmock) >= 4

%description   -n gem-fog-openstack-devel
Fog for OpenStack Platform development package.

This is the plugin Gem to talk to OpenStack clouds via fog.

%description   -n gem-fog-openstack-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-openstack.


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

%files         -n gem-fog-openstack-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-openstack-devel
%doc README.md


%changelog
* Wed Jan 25 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- ^ 1.0.11 -> 1.1.0

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.11-alt1
- ^ 1.0.10 -> 1.0.11

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.10-alt1
- update (^) 1.0.8 -> 1.0.10
- fix (!) spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.8-alt1
- Bump to 1.0.8
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.24-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.24-alt1
- Initial build for Sisyphus
