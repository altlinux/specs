%def_disable check
%define pkgname tzinfo

Name: ruby-%pkgname
Version: 1.2.5
Release: alt1
Summary: Daylight-savings aware timezone support for Ruby
License: MIT
Group: Development/Ruby
Url: http://rubyforge.org/projects/tzinfo/

Source: %pkgname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-ruby

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
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc --exclude definitions --exclude indexes lib/

%add_findprov_skiplist %ruby_sitelibdir/tzinfo/definitions/*
%add_findprov_skiplist %ruby_sitelibdir/tzinfo/indexes/*

%check
%ruby_test_unit -Ilib:test test/tc_*.rb

%files
%doc CHANGES* README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/TZInfo*

%changelog
* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.25-alt1.2
- Rebuild with new Ruby autorequirements.

* Thu Dec 06 2012 Led <led@altlinux.ru> 0.3.25-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- disabled check

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

