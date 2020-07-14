# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname rexml

Name:          gem-%pkgname
Version:       3.2.4
Release:       alt1
Summary:       REXML is an XML toolkit for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby/rexml
Vcs:           https://github.com/ruby/rexml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
REXML was inspired by the Electric XML library for Java, which features an
easy-to-use API, small size, and speed. Hopefully, REXML, designed with the same
philosophy, has these same features. I've tried to keep the API as intuitive
as possible, and have followed the Ruby methodology for method naming and code
flow, rather than mirroring the Java API.

REXML supports both tree and stream document parsing. Stream parsing is faster
(about 1.5 times as fast). However, with stream parsing, you don't get access
to features such as XPath.


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
* Mon Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 3.2.4-alt1
- + packaged gem with usage Ruby Policy 2.0
