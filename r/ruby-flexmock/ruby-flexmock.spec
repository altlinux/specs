# vim: set ft=spec : -*- rpm-spec -*-

%define pkgname flexmock

Name: ruby-%pkgname
Version: 0.9.0
Release: alt1

Summary: Simple mock object library for Ruby unit testing
Group: Development/Ruby
License: MIT
Url: http://rubyforge.org/projects/flexmock/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
#Patch: %pkgname-%version-%release.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Aug 26 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
FlexMock is a simple, but flexible, mock object library for Ruby unit
testing.

%package doc
Summary: Documentation files for %pkgname
Group: Documentation

%description doc
Documentation files for %pkgname

%prep
%setup -n %pkgname-%version
#patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib -I. test/*.rb

%install
%ruby_install
%rdoc lib/

%files
%doc CHANGES README.rdoc
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/FlexMock*

%changelog
* Tue Mar 22 2011 Andriy Stepanov <stanv@altlinux.ru> 0.9.0-alt1
- [0.9.0]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.6-alt1
- [0.8.6]

* Tue Aug 26 2008 Sir Raorn <raorn@altlinux.ru> 0.8.2-alt1
- Built for Sisyphus

