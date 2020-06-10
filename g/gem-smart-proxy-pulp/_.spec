# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname smart-proxy-pulp
%define        gemname smart_proxy_pulp

Name:          gem-%pkgname
Version:       2.1.0
Release:       alt1
Summary:       Basic Pulp support for Foreman Smart-Proxy
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_pulp
Vcs:           https://github.com/theforeman/smart_proxy_pulp.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

Foreman project plugin for Pulp allowing Katello hosts to interact with Pulp application services for content management While this plugin is part of the Foreman project it can only be used with Katello as Foreman is not content aware without the Katello plugin.
Getting Started

The Foreman project provides documentation on this specific plugin installation
from multiple methods, distribution specific RPM, distribution specific DEB and
direct manual build from source. The plugin can also be installed as part of the
foreman-installer puppet class with the --[no-]enable-foreman-proxy-plugin-pulp
option.

* working Katello instance (note not Foreman - must be Katello)
* smart proxy or capsule with the Pulp plugin installed and enabled
* Pulp installation as part of the Katello install, or a remote Pulp service to
  connect to


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
* Wed Jun 10 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- + packaged gem with usage Ruby Policy 2.0
