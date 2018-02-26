# vim: set ft=spec: -*- rpm-spec -*-

%define ruby_major 1.8

Name: ruby%{ruby_major}-rexical
Version: 1.0.5
Release: alt3

Summary: Lexical scanner generator for ruby
Group: Development/Ruby
License: LGPL
Url: https://github.com/tenderlove/rexical
Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
BuildRequires: libruby%{ruby_major}-devel ruby%{ruby_major}-stdlibs ruby-tool-setup

Source: %name-%version.tar
Patch1: ruby-rexical-1.0.5-alt-pick-of-rubygems.patch

%description
Rexical is a lexical scanner generator. It is written in Ruby itself,
and generates Ruby program. It is designed for use with Racc.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %name-%version
%patch1 -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
pushd test
%ruby_vendor -I../lib
find . -name 'test*.rb' -print0 |
	xargs -r0 -n 1 %ruby_test_unit -I../lib -I./
popd

%install
%ruby_install
%rdoc lib/

%files
%_bindir/rex
%ruby_sitelibdir/*
%doc README.rdoc DOCUMENTATION.en.rdoc

%files doc
%doc CHANGELOG*
%ruby_ri_sitedir/Rexical*

%changelog
* Tue Apr 26 2011 Timur Aitov <timonbl4@altlinux.org> 1.0.5-alt3
- Rebuild for ruby1.8

* Thu Mar 24 2011 Andriy Stepanov <stanv@altlinux.ru> 1.0.5-alt2
- Pick off rubygems.

* Thu Mar 24 2011 Andriy Stepanov <stanv@altlinux.ru> 1.0.5-alt1
- [1.0.5]
