# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname tty-table

Name:          gem-%pkgname
Version:       0.11.0.1
Release:       alt0.1
Summary:       A flexible and intuitive table generator
License:       MIT
Group:         Development/Ruby
Url:           https://ttytoolkit.org/
Vcs:           https://github.com/piotrmurach/tty-table.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.


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
%ruby_build --use=%gemname --version-replace=%version

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
* Tue Sep 8 2020 Pavel Skrylev <majioa@altlinux.org> 0.11.0.1-alt0.1
- + packaged gem with usage Ruby Policy 2.0
