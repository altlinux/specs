# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname foreman-default-hostgroup
%define        gemname foreman_default_hostgroup

Name:          gem-%pkgname
Version:       5.0.0
Release:       alt1
Summary:       A plugin to set the default hostgroup when hosts are created
License:       GPLv3
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_default_hostgroup/
Vcs:           https://github.com/theforeman/foreman_default_hostgroup.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 5.0.0-alt1
- + packaged gem with usage Ruby Policy 2.0
