# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname foreman-remote-execution
%define        gemname foreman_remote_execution
%define        _version 4.2.1
%define        core_version 1.4.0

Name:          gem-%pkgname
Version:       %_version
Release:       alt1
Summary:       A plugin bringing remote execution to the Foreman
License:       GPLv3
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_remote_execution
Vcs:           https://github.com/theforeman/foreman_remote_execution.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
A plugin bringing remote execution to the Foreman, completing the config
management functionality with remote management functionality.


%package       core
Version:       %core_version
Summary:       Library code for %{gemname}_core gem
Summary(ru_RU.UTF-8): Библиотечный код для самоцвета %{gemname}_core
Group:         Development/Documentation
BuildArch:     noarch

%description   core
Library code for %{gemname}_core gem.

%description   core -l ru_RU.UTF8
Библиотечный код для самоцвета %{gemname}_core.


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

%files         core-doc
%ruby_gemsdocdir/%{gemname}_core-%core_version


%changelog
* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 4.2.1-alt1
- + packaged gem with usage Ruby Policy 2.0
