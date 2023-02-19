# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname smart_proxy_discovery

Name:          gem-smart-proxy-discovery
Version:       1.0.5.15
Release:       alt0.1
Summary:       Add the capability to discover unknown bare-metal
License:       GPLv3
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_discovery
Vcs:           https://github.com/theforeman/smart_proxy_discovery.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(ci_reporter_test_unit) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(rest-client) >= 0
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_alias_names smart_proxy_discovery,smart-proxy-discovery
Requires:      gem(rest-client) >= 0
Provides:      gem(smart_proxy_discovery) = 1.0.5.15

%ruby_use_gem_version smart_proxy_discovery:1.0.5.15

%description
This smart proxy plugin, together with a Foreman plugin, add the capability to
discover unknown bare-metal. This plugin provides proxy API for nodes to
communicate with Foreman instance and vice versa. This plugin works only if the
Discovery plugin is running on Foreman.


%package       -n gem-smart-proxy-discovery-doc
Version:       1.0.5.15
Release:       alt0.1
Summary:       Add the capability to discover unknown bare-metal documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета smart_proxy_discovery
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(smart_proxy_discovery) = 1.0.5.15

%description   -n gem-smart-proxy-discovery-doc
Add the capability to discover unknown bare-metal documentation files.

This smart proxy plugin, together with a Foreman plugin, add the capability to
discover unknown bare-metal. This plugin provides proxy API for nodes to
communicate with Foreman instance and vice versa. This plugin works only if the
Discovery plugin is running on Foreman.

%description   -n gem-smart-proxy-discovery-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета smart_proxy_discovery.


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

%files         -n gem-smart-proxy-discovery-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.5.15-alt0.1
- ^ 1.0.5 -> 1.0.5p15 (no devel)

* Thu Feb 11 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- + packaged gem with usage Ruby Policy 2.0
