# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname smart-proxy-dynflow
%define        gemname smart_proxy_dynflow
%define        _version 0.3.0
%define        core_version 0.2.6

Name:          gem-%pkgname
Version:       %_version
Release:       alt1
Summary:       Dynflow runtime for Foreman smart proxy
License:       GPLv3
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_dynflow
Vcs:           https://github.com/theforeman/smart_proxy_dynflow.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

A plugin into Foreman's Smart Proxy for running Dynflow actions on the Smart
Proxy.

Simple Smart Proxy plugin containing only an API to forward all requests coming
to /dynflow and all the endpoints underneath it to the smart_proxy_dynflow_core
service. This gem is only used when smart_proxy_dynflow_core is deployed as
a standalone service.


%package       core
Version:       %core_version
Summary:       Library code for %{gemname}_core gem
Summary(ru_RU.UTF-8): Библиотечный код для самоцвета %{gemname}_core
Group:         Development/Documentation
BuildArch:     noarch

%description   core
This gem can be either use as a standalone service or run as a part of
the Smart Proxy process. Either way, this gem's purpose is to allow running
Dynflow actions and provide a simple API for triggering actions and querying
information about execution plans.


%description   core -l ru_RU.UTF8
Библиотечный код для самоцвета %{gemname}_core.


%package       -n %{pkgname}-core
Summary:       Executable file for %{gemname}_core gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %{gemname}_core
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %{pkgname}-core
Executable file for %{gemname}_core gem.

%description   -n %{pkgname}-core -l ru_RU.UTF8
Исполнямка для %{gemname}_core самоцвета.


%package       core-doc
Summary:       Documentation files for %{gemname}_core gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %{gemname}_core
Group:         Development/Documentation
BuildArch:     noarch

%description   core-doc
Documentation files for %{gemname}_core gem.

%description   core-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %{gemname}_core.


%package       doc
Version:       %_version
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

%files         core
%doc README*
%ruby_gemspecdir/%{gemname}_core-%core_version.gemspec
%ruby_gemslibdir/%{gemname}_core-%core_version

%files         -n %pkgname-core
%_bindir/%{gemname}_core

%files         core-doc
%ruby_gemsdocdir/%{gemname}_core-%core_version


%changelog
* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with usage Ruby Policy 2.0
