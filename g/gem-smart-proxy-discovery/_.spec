# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname smart-proxy-discovery
%define        gemname smart_proxy_discovery

Name:          gem-%pkgname
Version:       1.0.5
Release:       alt1
Summary:       Add the capability to discover unknown bare-metal
License:       GPLv3
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_discovery
Vcs:           https://github.com/theforeman/smart_proxy_discovery.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
This smart proxy plugin, together with a Foreman plugin, add the capability to
discover unknown bare-metal. This plugin provides proxy API for nodes to
communicate with Foreman instance and vice versa.
This plugin works only if the Discovery plugin is running on Foreman.


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
* Thu Feb 11 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- + packaged gem with usage Ruby Policy 2.0
