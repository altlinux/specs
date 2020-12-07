# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname foreman-tasks
%define        _version 3.0.2
%define        core_version 0.3.4

Name:          gem-%pkgname
Version:       %_version
Release:       alt1
Summary:       Tasks management engine and plugin for Foreman
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman-tasks
Vcs:           https://github.com/theforeman/foreman-tasks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

Tasks management engine for Foreman. Gives you an overview of what's
happening/happened in your Foreman instance. A framework for asynchronous tasks
in Foreman.


%package       core
Version:       %core_version
Summary:       Library code for %{gemname}-core gem
Summary(ru_RU.UTF-8): Библиотечный код для самоцвета %{gemname}-core
Group:         Development/Ruby
BuildArch:     noarch

%description   core
Library code for %{gemname}-core gem.

%description   core -l ru_RU.UTF8
Библиотечный код для самоцвета %{gemname}-core.


%package       core-doc
Summary:       Documentation files for %{gemname}-core gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %{gemname}-core
Group:         Development/Documentation
BuildArch:     noarch

%description   core-doc
Documentation files for %{gemname}-core gem.

%description   core-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %{gemname}-core.


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
%ruby_gemspecdir/%{gemname}-core-%core_version.gemspec
%ruby_gemslibdir/%{gemname}-core-%core_version

%files         core-doc
%ruby_gemsdocdir/%{gemname}-core-%core_version


%changelog
* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.2-alt1
- + packaged gem with usage Ruby Policy 2.0
