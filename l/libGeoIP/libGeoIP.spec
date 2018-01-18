%define origname geoip-api-c
%define _name GeoIP

# due to hasher network isolation
%def_disable check

Name: lib%_name
Version: 1.6.12
Release: alt1

Summary: GeoIP is a C library find what country an IP address or hostname originates from
License: LGPLv2.1+
Group: System/Libraries
URL: https://github.com/maxmind/%origname

Source: %url/releases/download/v%version/%_name-%version.tar.gz

# Automatically added by buildreq on Sun Apr 17 2011
BuildRequires: zlib-devel

# Both library and lookup tools unusable without database. But user can choose
# to get this file directly from MaxMind site, without installing our packaged
# GeoIP database. Hence this is file rather than package requirement.
Requires: /usr/share/GeoIP/GeoIP.dat

%description
%origname is a C library that enables the user to find the country that any IP
address or hostname originates from. It uses a file based database that is
accurate as of March 2003. This database simply contains IP blocks as keys,
and countries as values. This database should be more complete and accurate
than using reverse DNS lookups. Commercial databases and automatic update
services are available from http://www.maxmind.com/

This module can be used to automatically select the geographically closest
mirror, to analyze your web server logs to determine the countries of your
visitors, for credit card fraud detection, and for software export controls.

%package devel
Summary: GeoIP headers, libraries
Group: Development/C
Requires: %name = %version-%release

%description devel
%origname is a C library that enables the user to find the country that
any IP address or hostname originates from.

This package contain the devel files for %origname.

%package tools
Summary: GeoIP tools
Group: System/Libraries
Requires: %name = %version-%release

%description tools
%origname is a C library that enables the user to find the country that
any IP address or hostname originates from.

This package contain few tools for %origname such as lookup, export,
autoupdate.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure --disable-static \
	--disable-data-files
%make_build

%check
%make check

%install
%makeinstall_std

%files
%_libdir/%name.so.*

%files devel
%doc ChangeLog
%_includedir/*.h
%_libdir/%name.so
%_pkgconfigdir/geoip.pc

%files tools
%_bindir/geoiplookup*
%_man1dir/*

%changelog
* Thu Jan 18 2018 Yuri N. Sedunov <aris@altlinux.org> 1.6.12-alt1
- 1.6.12

* Mon May 29 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.11-alt1
- 1.6.11

* Tue Jan 26 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.9-alt1
- 1.6.9

* Mon Nov 02 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.7-alt1
- 1.6.7

* Thu Jul 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt1
- 1.6.6

* Wed Apr 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.5-alt1
- 1.6.5

* Fri Feb 07 2014 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2 (new url/origname)

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Thu Dec 15 2011 Michael Shigorin <mike@altlinux.org> 1.4.8-alt1.1
- NMU: moved "make check" to %%check section,
  disabled by default due to hasher network isolation,
  argh

* Sun Jun 26 2011 Victor Forsiuk <force@altlinux.org> 1.4.8-alt1
- 1.4.8

* Sun Apr 17 2011 Victor Forsiuk <force@altlinux.org> 1.4.7-alt1
- 1.4.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.6-alt2.1
- Rebuilt for debuginfo

* Mon Nov 01 2010 Victor Forsiuk <force@altlinux.org> 1.4.6-alt2
- Rebuilt for soname set-versions.

* Wed Mar 11 2009 Victor Forsyuk <force@altlinux.org> 1.4.6-alt1
- 1.4.6

* Mon Dec 15 2008 Victor Forsyuk <force@altlinux.org> 1.4.5-alt2
- Remove obsolete ldconfig calls.

* Fri Sep 19 2008 Victor Forsyuk <force@altlinux.org> 1.4.5-alt1
- 1.4.5

* Thu Mar 13 2008 Victor Forsyuk <force@altlinux.org> 1.4.4-alt1
- 1.4.4

* Wed Sep 05 2007 Victor Forsyuk <force@altlinux.org> 1.4.3-alt1
- 1.4.3

* Wed Aug 15 2007 Victor Forsyuk <force@altlinux.org> 1.4.2-alt2
- Remove database files from package. GeoIP databases updated way more often
  than library itself. So we will package them separately and just require
  presence of GeoIP.dat file at install time.

* Thu Mar 22 2007 Victor Forsyuk <force@altlinux.org> 1.4.2-alt1
- 1.4.2

* Tue Feb 06 2007 Victor Forsyuk <force@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Oct 09 2006 Victor Forsyuk <force@altlinux.org> 1.4.0-alt1
- 1.4.0
- License: GPL --> LGPL
- Fixed build with --as-needed.
- Move header files from sub-dir to /usr/include (to meet expectation
  of software that uses libGeoIP).
- Place config straight in /etc (subdirectory just for one file is
  little overkill :).

* Wed Mar 02 2005 Dmitry Vukolov <dav@altlinux.ru> 1.3.8-alt1
- version 1.3.8

* Sat Sep 11 2004 Dmitry Vukolov <dav@altlinux.ru> 1.3.6-alt1
- new version
- GeoIP_country_code_by_name test disabled

* Fri Aug 06 2004 Dmitry Vukolov <dav@altlinux.ru> 1.3.5-alt1
- version 1.3.5
- *.a files moved to the (optional) devel-static package
- GeoIP.conf.default will be overwritten on update
- Ukrainian description locale corrected

* Mon Feb  2 2004 Serhii Hlodin <hlodin@altlinux.ru> 1.3.1-alt2
- Minor fixes for Sisyphus

* Thu Nov 27 2003 Serhii Hlodin <hlodin@altlinux.ru> 1.3.1-alt1
- Initial build from original SPEC-file by Peter Bieringer
- Create additional packages: devel-static and tools
