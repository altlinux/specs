# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname csv

Name:          gem-%pkgname
Version:       3.1.2
Release:       alt1
Summary:       CSV Reading and Writing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby/csv
Vcs:           https://github.com/ruby/csv.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.

This library provides a complete interface to CSV files and data. It offers
tools to enable you to read and write to and from Strings or IO objects, as
needed.


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


%changelog
* Mon Mar 16 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.2-alt1
- + packaged gem with usage Ruby Policy 2.0
