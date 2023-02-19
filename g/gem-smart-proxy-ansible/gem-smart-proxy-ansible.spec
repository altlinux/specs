# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname smart_proxy_ansible

Name:          gem-smart-proxy-ansible
Version:       3.5.0
Release:       alt1
Summary:       Smart-Proxy ansible plugin
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_ansible
Vcs:           https://github.com/theforeman/smart_proxy_ansible.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(webmock) >= 3
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(logger) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(smart_proxy) >= 0
BuildRequires: gem(net-ssh) >= 0
BuildRequires: gem(smart_proxy_dynflow) >= 0.8
BuildRequires: gem(smart_proxy_remote_execution_ssh) >= 0.4
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(rack-test) >= 3
BuildConflicts: gem(smart_proxy_dynflow) >= 1
BuildConflicts: gem(smart_proxy_remote_execution_ssh) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency rack-test >= 2.0.0,rack-test < 3
%ruby_alias_names smart_proxy_ansible,smart-proxy-ansible
Requires:      gem(net-ssh) >= 0
Requires:      gem(smart_proxy_dynflow) >= 0.8
Requires:      gem(smart_proxy_remote_execution_ssh) >= 0.4
Conflicts:     gem(smart_proxy_dynflow) >= 1
Conflicts:     gem(smart_proxy_remote_execution_ssh) >= 1
Provides:      gem(smart_proxy_ansible) = 3.5.0


%description
Proxy plugin to make foreman_ansible actions run in the proxy.

This plugin requires at least Foreman Proxy 2.3.


%package       -n gem-smart-proxy-ansible-doc
Version:       3.5.0
Release:       alt1
Summary:       Smart-Proxy ansible plugin documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета smart_proxy_ansible
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(smart_proxy_ansible) = 3.5.0

%description   -n gem-smart-proxy-ansible-doc
Smart-Proxy ansible plugin documentation files.

Proxy plugin to make foreman_ansible actions run in the proxy.

This plugin requires at least Foreman Proxy 2.3.

%description   -n gem-smart-proxy-ansible-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета smart_proxy_ansible.


%package       -n gem-smart-proxy-ansible-devel
Version:       3.5.0
Release:       alt1
Summary:       Smart-Proxy ansible plugin development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета smart_proxy_ansible
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(smart_proxy_ansible) = 3.5.0
Requires:      gem(rake) >= 13.0
Requires:      gem(webmock) >= 3
Requires:      gem(rack-test) >= 0
Requires:      gem(logger) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(smart_proxy) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(rack-test) >= 3

%description   -n gem-smart-proxy-ansible-devel
Smart-Proxy ansible plugin development package.

Proxy plugin to make foreman_ansible actions run in the proxy.

This plugin requires at least Foreman Proxy 2.3.

%description   -n gem-smart-proxy-ansible-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета smart_proxy_ansible.


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

%files         -n gem-smart-proxy-ansible-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-smart-proxy-ansible-devel
%doc README.md


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.0-alt1
- ^ 3.0.1 -> 3.5.0

* Thu Feb 11 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- + packaged gem with usage Ruby Policy 2.0
