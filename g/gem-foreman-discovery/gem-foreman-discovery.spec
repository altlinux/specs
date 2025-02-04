%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname foreman_discovery

Name:          gem-foreman-discovery
Version:       24.0.2
Release:       alt1
Summary:       MaaS Discovery Plugin for Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_discovery
Vcs:           https://github.com/theforeman/foreman_discovery.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source1:       .public.tar
Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(theforeman-rubocop) >= 0.1.0
BuildConflicts: gem(theforeman-rubocop) >= 0.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names foreman_discovery,foreman-discovery
Provides:      gem(foreman_discovery) = 24.0.2


%description
A plugin to enable Metal-as-a-Service discovery functionality in foreman.


%if_enabled    doc
%package       -n gem-foreman-discovery-doc
Version:       24.0.2
Release:       alt1
Summary:       MaaS Discovery Plugin for Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_discovery
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_discovery) = 24.0.2

%description   -n gem-foreman-discovery-doc
MaaS Discovery Plugin for Foreman documentation files.

A plugin to enable Metal-as-a-Service discovery functionality in foreman.

%description   -n gem-foreman-discovery-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_discovery.
%endif


%if_enabled    devel
%package       -n gem-foreman-discovery-devel
Version:       24.0.2
Release:       alt1
Summary:       MaaS Discovery Plugin for Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_discovery
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_discovery) = 24.0.2
Requires:      gem(theforeman-rubocop) >= 0.1.0
Conflicts:     gem(theforeman-rubocop) >= 0.2

%description   -n gem-foreman-discovery-devel
MaaS Discovery Plugin for Foreman development package.

A plugin to enable Metal-as-a-Service discovery functionality in foreman.

%description   -n gem-foreman-discovery-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_discovery.
%endif


%prep
%setup -a 1

%build
%ruby_build

%install
%ruby_install
install -d %buildroot%_datadir/foreman/
cp -rp .public %buildroot%_datadir/foreman/public

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%_datadir/foreman/public

%if_enabled    doc
%files         -n gem-foreman-discovery-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-foreman-discovery-devel
%doc README.md
%endif


%changelog
* Tue Oct 01 2024 Pavel Skrylev <majioa@altlinux.org> 24.0.2-alt1
- ^ 21.0.3 -> 24.0.2

* Thu Apr 06 2023 Pavel Skrylev <majioa@altlinux.org> 21.0.3-alt1.1
- ! public webpack

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 21.0.3-alt1
- ^ 18.0.4 -> 21.0.3

* Wed Oct 27 2021 Pavel Skrylev <majioa@altlinux.org> 18.0.4-alt1
- ^ 17.1.0 -> 18.0.4

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 17.1.0-alt1
- + packaged gem with Ruby Policy 2.0
