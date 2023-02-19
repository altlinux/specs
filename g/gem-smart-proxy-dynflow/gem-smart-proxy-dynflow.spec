%define        gemname smart_proxy_dynflow

Name:          gem-smart-proxy-dynflow
Version:       0.8.2
Release:       alt1
Summary:       Dynflow runtime for Foreman smart proxy
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_dynflow
Vcs:           https://github.com/theforeman/smart_proxy_dynflow.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         fixes.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.7
BuildRequires: gem(webmock) >= 1
BuildRequires: gem(pry) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(public_suffix) >= 0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0.52.1
BuildRequires: gem(logging-journald) >= 2.0
BuildRequires: gem(rack) >= 1.1
BuildRequires: gem(sinatra) >= 0
BuildRequires: gem(dynflow) >= 1.6
BuildRequires: gem(rest-client) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(logging-journald) >= 3
BuildConflicts: gem(dynflow) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rack-test >= 1.1.0,rack-test < 2
%ruby_alias_names smart_proxy_dynflow,smart-proxy-dynflow
Requires:      gem(dynflow) >= 1.6
Requires:      gem(rest-client) >= 0
Requires:      gem(sqlite3) >= 0
Conflicts:     gem(dynflow) >= 2
Provides:      gem(smart_proxy_dynflow) = 0.8.2


%description
A plugin into Foreman's Smart Proxy for running Dynflow actions on the Smart
Proxy.

Simple Smart Proxy plugin containing only an API to forward all requests coming
to /dynflow and all the endpoints underneath it to the smart_proxy_dynflow_core
service. This gem is only used when smart_proxy_dynflow_core is deployed as a
standalone service.


%package       -n gem-smart-proxy-dynflow-doc
Version:       0.8.2
Release:       alt1
Summary:       Dynflow runtime for Foreman smart proxy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета smart_proxy_dynflow
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(smart_proxy_dynflow) = 0.8.2

%description   -n gem-smart-proxy-dynflow-doc
Dynflow runtime for Foreman smart proxy documentation files.

A plugin into Foreman's Smart Proxy for running Dynflow actions on the Smart
Proxy.

Simple Smart Proxy plugin containing only an API to forward all requests coming
to /dynflow and all the endpoints underneath it to the smart_proxy_dynflow_core
service. This gem is only used when smart_proxy_dynflow_core is deployed as a
standalone service.

%description   -n gem-smart-proxy-dynflow-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета smart_proxy_dynflow.


%package       -n gem-smart-proxy-dynflow-devel
Version:       0.8.2
Release:       alt1
Summary:       Dynflow runtime for Foreman smart proxy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета smart_proxy_dynflow
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(smart_proxy_dynflow) = 0.8.2
Requires:      gem(bundler) >= 1.7
Requires:      gem(webmock) >= 1
Requires:      gem(pry) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(public_suffix) >= 0
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0.52.1
Requires:      gem(logging-journald) >= 2.0
Requires:      gem(rack) >= 1.1
Requires:      gem(sinatra) >= 0
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(logging-journald) >= 3

%description   -n gem-smart-proxy-dynflow-devel
Dynflow runtime for Foreman smart proxy development package.

A plugin into Foreman's Smart Proxy for running Dynflow actions on the Smart
Proxy.

Simple Smart Proxy plugin containing only an API to forward all requests coming
to /dynflow and all the endpoints underneath it to the smart_proxy_dynflow_core
service. This gem is only used when smart_proxy_dynflow_core is deployed as a
standalone service.

%description   -n gem-smart-proxy-dynflow-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета smart_proxy_dynflow.


%prep
%setup
%autopatch

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

%files         -n gem-smart-proxy-dynflow-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-smart-proxy-dynflow-devel
%doc README.md


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 0.8.2-alt1
- ^ 0.6.0 -> 0.8.2

* Mon Nov 15 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- ^ 0.5.2 -> 0.6.0
- * default configs for the gem

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.2-alt1
- ^ 0.3.0 -> 0.5.2

* Fri Jan 22 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1.1
- ! requires for smart_proxy_dynflow_core gem

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with usage Ruby Policy 2.0
