# vim: set ft=spec: -*- rpm-spec -*-

%define ruby_major 1.8
%define pkgname mocha

Name: ruby%{ruby_major}-%pkgname
Version: 0.9.12
Release: alt2

Summary: Library for mocking and stubbing in Ruby
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/mocha/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Mon Nov 10 2008 (-bi)
BuildRequires: ruby%{ruby_major}-stdlibs rpm-build-ruby ruby%{ruby_major}-tool-rdoc ruby-tool-setup

%description
Mocha is a library for mocking and stubbing in Ruby using a syntax
like that of JMock. Mocha provides a unified, simple and readable
syntax for both traditional and partial mocking.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib:test test/unit/*_test.rb test/unit/*/*_test.rb

%install
%ruby_install
%rdoc lib/

%files
%doc README.rdoc
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/Mocha*

%changelog
* Tue Apr 12 2011 Timur Aitov <timonbl4@altlinux.org> 0.9.12-alt2
- Rebuild for ruby1.8

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 0.9.12-alt1
- [0.9.12]

* Tue May 12 2009 Alexey I. Froloff <raorn@altlinux.org> 0.9.5-alt1
- [0.9.5]

* Mon Nov 10 2008 Sir Raorn <raorn@altlinux.ru> 0.9.2-alt1
- Built for Sisyphus

