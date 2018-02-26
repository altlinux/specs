%define ruby_major 1.8
%define pkgname tzinfo

Name: ruby%{ruby_major}-%pkgname
Version: 0.3.25
Release: alt2
Summary: Daylight-savings aware timezone support for Ruby
License: MIT
Group: Development/Ruby
Url: http://rubyforge.org/projects/tzinfo/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# XXX@timonbl4: test crash with 'SecurityError: Insecure operation - require'
Patch1: ruby-tzinfo-0.3.25-alt-test.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Jul 08 2008 (-bi)
BuildRequires: ruby%{ruby_major} rpm-build-ruby ruby%{ruby_major}-stdlibs ruby%{ruby_major}-tool-rdoc ruby-tool-setup

%description
TZInfo uses the tz database (http://www.twinsun.com/tz/tz-link.htm)
to provide daylight-savings aware transformations between times in
different timezones.

This is the same database as used for zoneinfo on Unix machines.

%package doc
Summary: Documentation files for %pkgname
Group: Documentation

%description doc
Documentation files for %pkgname

%prep
%setup -q -n %pkgname-%version
%patch -p1
%patch1 -p2
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib:test test/tc_*.rb

%install
%ruby_install
%rdoc --exclude definitions --exclude indexes lib/

%add_findprov_skiplist %ruby_sitelibdir/tzinfo/definitions/*
%add_findprov_skiplist %ruby_sitelibdir/tzinfo/indexes/*

%files
%doc CHANGES README
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/TZInfo*

%changelog
* Tue Apr 26 2011 Timur Aitov <timonbl4@altlinux.org> 0.3.25-alt2
- Rebuild for ruby1.8

* Mon Mar 21 2011 Andriy Stepanov <stanv@altlinux.ru> 0.3.25-alt1
- [0.3.25]

* Fri Jul 16 2010 Alexey I. Froloff <raorn@altlinux.org> 0.3.22-alt1
- [0.3.22]

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 0.3.13-alt1
- [0.3.13]

* Tue Feb 03 2009 Sir Raorn <raorn@altlinux.ru> 0.3.12-alt1
- [0.3.12]

* Mon Nov 10 2008 Sir Raorn <raorn@altlinux.ru> 0.3.11-alt1
- [0.3.11]

* Tue Jul 08 2008 Sir Raorn <raorn@altlinux.ru> 0.3.9-alt1
- Built for Sisyphus

