%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname foreman_default_hostgroup

Name:          gem-foreman-default-hostgroup
Version:       7.0.0.18
Release:       alt0.1
Summary:       A plugin to set the default hostgroup when hosts are created
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_default_hostgroup/
Vcs:           https://github.com/theforeman/foreman_default_hostgroup.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(theforeman-rubocop) >= 0.1.1
BuildConflicts: gem(theforeman-rubocop) >= 0.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names foreman_default_hostgroup,foreman-default-hostgroup
Provides:      gem(foreman_default_hostgroup) = 7.0.0.18

%ruby_use_gem_version foreman_default_hostgroup:7.0.0.18

%description
A quick plugin to set a default hostgroup on hosts which check-in via Puppet
without a Hostgroup set.


%if_enabled    doc
%package       -n gem-foreman-default-hostgroup-doc
Version:       7.0.0.18
Release:       alt0.1
Summary:       A plugin to set the default hostgroup when hosts are created documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_default_hostgroup
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_default_hostgroup) = 7.0.0.18

%description   -n gem-foreman-default-hostgroup-doc
A plugin to set the default hostgroup when hosts are created documentation
files.

A quick plugin to set a default hostgroup on hosts which check-in via Puppet
without a Hostgroup set.

%description   -n gem-foreman-default-hostgroup-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_default_hostgroup.
%endif


%if_enabled    devel
%package       -n gem-foreman-default-hostgroup-devel
Version:       7.0.0.18
Release:       alt0.1
Summary:       A plugin to set the default hostgroup when hosts are created development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_default_hostgroup
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_default_hostgroup) = 7.0.0.18
Requires:      gem(theforeman-rubocop) >= 0.1.1
Conflicts:     gem(theforeman-rubocop) >= 0.2

%description   -n gem-foreman-default-hostgroup-devel
A plugin to set the default hostgroup when hosts are created development
package.

A quick plugin to set a default hostgroup on hosts which check-in via Puppet
without a Hostgroup set.

%description   -n gem-foreman-default-hostgroup-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_default_hostgroup.
%endif


%prep
%setup
%autopatch -p1

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

%if_enabled    doc
%files         -n gem-foreman-default-hostgroup-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-foreman-default-hostgroup-devel
%doc README.md
%endif


%changelog
* Fri Oct 04 2024 Pavel Skrylev <majioa@altlinux.org> 7.0.0.18-alt0.1
- ^ 6.0.0.2 -> 7.0.0p18

* Wed Jul 05 2023 Pavel Skrylev <majioa@altlinux.org> 6.0.0.2-alt0.3
- ! fixed patch

* Tue Apr 04 2023 Pavel Skrylev <majioa@altlinux.org> 6.0.0.2-alt0.2
- ^ 6.0.0[1] -> 6.0.0[2] with patch

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 6.0.0.1-alt0.1
- ^ 6.0.0 -> 6.0.0[1]

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt1
- ^ 5.0.0 -> 6.0.0

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 5.0.0-alt1
- + packaged gem with usage Ruby Policy 2.0
