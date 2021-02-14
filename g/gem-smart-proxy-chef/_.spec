# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname smart-proxy-chef
%define        gemname smart_proxy_chef

Name:          gem-%pkgname
Version:       0.2.0
Release:       alt1
Summary:       Chef support for Foreman Smart-Proxy
License:       GPLv3
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_chef
Vcs:           https://github.com/theforeman/smart_proxy_chef.git
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
* Thu Feb 11 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with usage Ruby Policy 2.0
