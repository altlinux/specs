# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname diffy

Name:          gem-%pkgname
Version:       3.4.0
Release:       alt1
Summary:       Easy Diffing in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/samg/diffy
Vcs:           https://github.com/samg/diffy.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Need diffs in your ruby app? Diffy has you covered. It provides a convenient
way to generate a diff from two strings or files. Instead of reimplementing
the LCS diff algorithm Diffy uses battle tested Unix diff to generate diffs,
and focuses on providing a convenient interface, and getting out of your way.


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
* Thu Dec 16 2020 Pavel Skrylev <majioa@altlinux.org> 3.4.0-alt1
- + packaged gem with usage Ruby Policy 2.0
