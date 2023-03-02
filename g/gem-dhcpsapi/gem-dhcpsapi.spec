# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname dhcpsapi

Name:          gem-dhcpsapi
Version:       0.0.11
Release:       alt1.1
Summary:       Ruby wrappers for MS DHCP api
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/dmitri-d/ruby-dhcpsapi
Vcs:           https://github.com/dmitri-d/ruby-dhcpsapi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 4.3
BuildRequires: gem(yard) >= 0
BuildRequires: gem(ffi) >= 0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(ffi) >= 0
Provides:      gem(dhcpsapi) = 0.0.11


%description
This contains ffi-based ruby bindings for MS DHCP server management API.


%package       -n gem-dhcpsapi-doc
Version:       0.0.11
Release:       alt1.1
Summary:       Ruby wrappers for MS DHCP api documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dhcpsapi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dhcpsapi) = 0.0.11

%description   -n gem-dhcpsapi-doc
Ruby wrappers for MS DHCP api documentation files.

This contains ffi-based ruby bindings for MS DHCP server management API.

%description   -n gem-dhcpsapi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dhcpsapi.


%package       -n gem-dhcpsapi-devel
Version:       0.0.11
Release:       alt1.1
Summary:       Ruby wrappers for MS DHCP api development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dhcpsapi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dhcpsapi) = 0.0.11
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 4.3
Requires:      gem(yard) >= 0
Conflicts:     gem(minitest) >= 6

%description   -n gem-dhcpsapi-devel
Ruby wrappers for MS DHCP api development package.

This contains ffi-based ruby bindings for MS DHCP server management API.

%description   -n gem-dhcpsapi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dhcpsapi.


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

%files         -n gem-dhcpsapi-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-dhcpsapi-devel
%doc README.md


%changelog
* Thu Mar 02 2023 Pavel Skrylev <majioa@altlinux.org> 0.0.11-alt1.1
- ! spec

* Thu Jun 11 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.11-alt1
- + packaged gem with usage Ruby Policy 2.0
