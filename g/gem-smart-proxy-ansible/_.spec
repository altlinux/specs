# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname smart-proxy-ansible
%define        gemname smart_proxy_ansible

Name:          gem-%pkgname
Version:       3.0.1
Release:       alt1
Summary:       Smart-Proxy ansible plugin
License:       GPLv3
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_ansible
Vcs:           https://github.com/theforeman/smart_proxy_ansible.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Proxy plugin to make foreman_ansible actions run in the proxy.

This plugin requires at least Foreman Proxy 2.3.


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
* Thu Feb 11 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- + packaged gem with usage Ruby Policy 2.0
