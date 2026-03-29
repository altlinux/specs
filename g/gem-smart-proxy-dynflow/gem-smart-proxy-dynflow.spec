%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname smart_proxy_dynflow

Name:          gem-smart-proxy-dynflow
Version:       1.0.0
Release:       alt1
Summary:       Dynflow runtime for Foreman smart proxy
License:       GPL-3.0-only
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_dynflow
Vcs:           https://github.com/theforeman/smart_proxy_dynflow.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         fixes.patch
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(dynflow) >= 1.6
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(public_suffix) >= 0
BuildRequires: gem(rack) >= 1.1
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rest-client) >= 2.0
BuildRequires: gem(sinatra) >= 0
BuildRequires: gem(smart_proxy) >= 0
BuildRequires: gem(sqlite3) >= 1.0
BuildRequires: gem(webmock) >= 0
BuildConflicts: gem(dynflow) >= 3.0
BuildConflicts: gem(rest-client) >= 3
BuildConflicts: gem(sqlite3) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_alias_names smart_proxy_dynflow,smart-proxy-dynflow
Requires:      ruby >= 3.0
Requires:      gem(dynflow) >= 1.6
Requires:      gem(rest-client) >= 2.0
Requires:      gem(sqlite3) >= 1.0
Conflicts:     gem(dynflow) >= 3.0
Conflicts:     gem(rest-client) >= 3
Conflicts:     gem(sqlite3) >= 2
Provides:      gem(smart_proxy_dynflow) = 1.0.0

%description
A plugin into Foreman's Smart Proxy for running Dynflow actions on the Smart
Proxy.

Simple Smart Proxy plugin containing only an API to forward all requests coming
to /dynflow and all the endpoints underneath it to the smart_proxy_dynflow_core
service. This gem is only used when smart_proxy_dynflow_core is deployed as a
standalone service.


%if_enabled    doc
%package       -n gem-smart-proxy-dynflow-doc
Version:       1.0.0
Release:       alt1
Summary:       Dynflow runtime for Foreman smart proxy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета smart_proxy_dynflow
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(smart_proxy_dynflow) = 1.0.0

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
%endif


%if_enabled    devel
%package       -n gem-smart-proxy-dynflow-devel
Version:       1.0.0
Release:       alt1
Summary:       Dynflow runtime for Foreman smart proxy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета smart_proxy_dynflow
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(smart_proxy_dynflow) = 1.0.0
Requires:      gem(dynflow) >= 1.6
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(public_suffix) >= 0
Requires:      gem(rack) >= 1.1
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rest-client) >= 2.0
Requires:      gem(sinatra) >= 0
Requires:      gem(smart_proxy) >= 0
Requires:      gem(sqlite3) >= 1.0
Requires:      gem(webmock) >= 0
Conflicts:     gem(dynflow) >= 3.0
Conflicts:     gem(rest-client) >= 3
Conflicts:     gem(sqlite3) >= 2

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
%endif


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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-smart-proxy-dynflow-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-smart-proxy-dynflow-devel
%doc LICENSE README.md
%endif


%changelog
* Mon Mar 30 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.8.2 -> 1.0.0

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
