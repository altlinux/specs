%define        gemname foreman_default_hostgroup

Name:          gem-foreman-default-hostgroup
Version:       6.0.0
Release:       alt1
Summary:       A plugin to set the default hostgroup when hosts are created
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_default_hostgroup/
Vcs:           https://github.com/theforeman/foreman_default_hostgroup.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names foreman_default_hostgroup,foreman-default-hostgroup
Provides:      gem(foreman_default_hostgroup) = 6.0.0


%description
A quick plugin to set a default hostgroup on hosts which check-in via Puppet
without a Hostgroup set.


%package       -n gem-foreman-default-hostgroup-doc
Version:       6.0.0
Release:       alt1
Summary:       A plugin to set the default hostgroup when hosts are created documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_default_hostgroup
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_default_hostgroup) = 6.0.0

%description   -n gem-foreman-default-hostgroup-doc
A plugin to set the default hostgroup when hosts are created documentation
files.

A quick plugin to set a default hostgroup on hosts which check-in via Puppet
without a Hostgroup set.

%description   -n gem-foreman-default-hostgroup-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_default_hostgroup.


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

%files         -n gem-foreman-default-hostgroup-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt1
- ^ 5.0.0 -> 6.0.0

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 5.0.0-alt1
- + packaged gem with usage Ruby Policy 2.0
