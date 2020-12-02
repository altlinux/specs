# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname gnuplot

Name:          gem-%pkgname
Version:       2.6.2.1
Release:       alt1
Summary:       Utility library to aid in interacting with gnuplot from ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rdp/ruby_gnuplot
Vcs:           https://github.com/rdp/ruby_gnuplot.git
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
* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 2.6.2.1-alt1
- + packaged gem with usage Ruby Policy 2.0
