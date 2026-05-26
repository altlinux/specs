# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname smart_proxy_ansible

Name:          gem-smart-proxy-ansible
Version:       3.7.1
Release:       alt1
Summary:       Smart-Proxy ansible plugin
License:       GPL-3.0-only
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_ansible
Vcs:           https://github.com/theforeman/smart_proxy_ansible.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(smart_proxy) >= 0
BuildRequires: gem(smart_proxy_dynflow) >= 0.9.4
BuildRequires: gem(smart_proxy_remote_execution_ssh) >= 0.5.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(smart_proxy_dynflow) >= 2.0.0
BuildConflicts: gem(smart_proxy_remote_execution_ssh) >= 2.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names smart_proxy_ansible,smart-proxy-ansible
Requires:      ruby >= 3.0
Requires:      gem(smart_proxy_dynflow) >= 0.9.4
Requires:      gem(smart_proxy_remote_execution_ssh) >= 0.5.0
Conflicts:     gem(smart_proxy_dynflow) >= 2.0.0
Conflicts:     gem(smart_proxy_remote_execution_ssh) >= 2.0.0
Provides:      gem(smart_proxy_ansible) = 3.7.1

%description
Proxy plugin to make foreman_ansible actions run in the proxy.

This plugin requires at least Foreman Proxy 2.3.


%if_enabled    doc
%package       -n gem-smart-proxy-ansible-doc
Version:       3.7.1
Release:       alt1
Summary:       Smart-Proxy ansible plugin documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета smart_proxy_ansible
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(smart_proxy_ansible) = 3.7.1

%description   -n gem-smart-proxy-ansible-doc
Smart-Proxy ansible plugin documentation files.

Proxy plugin to make foreman_ansible actions run in the proxy.

This plugin requires at least Foreman Proxy 2.3.

%description   -n gem-smart-proxy-ansible-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета smart_proxy_ansible.
%endif


%if_enabled    devel
%package       -n gem-smart-proxy-ansible-devel
Version:       3.7.1
Release:       alt1
Summary:       Smart-Proxy ansible plugin development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета smart_proxy_ansible
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(smart_proxy_ansible) = 3.7.1
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(smart_proxy) >= 0
Conflicts:     gem(rake) >= 14

%description   -n gem-smart-proxy-ansible-devel
Smart-Proxy ansible plugin development package.

Proxy plugin to make foreman_ansible actions run in the proxy.

This plugin requires at least Foreman Proxy 2.3.

%description   -n gem-smart-proxy-ansible-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета smart_proxy_ansible.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-smart-proxy-ansible-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-smart-proxy-ansible-devel
%doc LICENSE README.md
%endif


%changelog
* Tue May 26 2026 Pavel Skrylev <majioa@altlinux.org> 3.7.1-alt1
- ^ 3.0.1 -> 3.7.1
- * define explicit dependencies

* Thu Feb 11 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- + packaged gem with usage Ruby Policy 2.0
