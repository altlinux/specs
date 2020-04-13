# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname rubyforge

Name:          gem-%pkgname
Version:       2.0.4
Release:       alt1
Summary:       A script which automates a limited set of rubyforge operations
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/devrandom/rubyforge
Vcs:           https://github.com/devrandom/rubyforge.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         hoe-setup.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hoe)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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
%patch

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

%files         -n %pkgname
%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir


%changelog
* Mon Jun 10 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.4-alt1
- + packaged gem with usage Ruby Policy 2.0
