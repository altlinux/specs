%define origname librapi2

Name: librapi
Version: 0.15.2
Release: alt1.1
Packager: Mobile Development Team <mobile@packages.altlinux.org>
Summary: A library that implements RAPI
License: MIT
Group: System/Libraries
Url: http://synce.sourceforge.net
Source: %origname-%version.tar
Source1: %name.map
Patch1: %name-alt-symver.patch
Patch2: %name-alt-disable-rpath.patch
Patch3: %name-alt-fix-link.patch

BuildPreReq: libsynce-devel >= 0.15.1
BuildPreReq: python-module-Pyrex >= 0.9.6
BuildPreReq: libdbus-glib-devel libdbus-devel
BuildRequires: gcc-c++ time

Provides: librapi2 = %version-%release
Obsoletes: librapi2

%description
Librapi is part of the SynCE project (%url).

The RAPI library is an open source implementation that works like RAPI.DLL,
available on Microsoft operating systems. The library makes it possible to make
remote calls to a computer running Pocket PC. Documentation for the RAPI calls
is available at this address:

http://msdn.microsoft.com/library/default.asp?url=/library/en-us/wcesdkr/htm/_wcesdk_CeRapiInit.asp

%package devel
Summary: Libraries and headers needed for developing with SynCE
Group: Development/C
Requires: %name = %version-%release

Provides: librapi2-devel = %version-%release
Obsoletes: librapi2-devel

%description devel
Libraries and headers needed for developing with RAPI

%package -n rapi-tools
Summary: Simple command line tools that use RAPI
Group: Communications

Provides: rapi2-tools = %version-%release
Obsoletes: rapi2-tools

%description -n rapi-tools
Simple command line tools that use RAPI


%package -n python-module-librapi
Summary: librapi python interface
Group: Development/Python
Requires: %name = %version-%release
Provides: librapi-python = %version-%release
Obsoletes: librapi-python

%description -n python-module-librapi
Python wrappers for %name

%prep
%setup -q -n %{name}2-%version
#%patch1 -p1
%patch2 -p1
%patch3 -p1
#install -p -m644 %SOURCE1 src/%name.map

%build
ACLOCAL="aclocal -I m4"  %autoreconf
%configure --disable-static --disable-hal-support --enable-odccm-support  --enable-udev-support
sed -i -e 's,^\(pyrapi2_la_LIBADD = \$(top_builddir)/src/librapi.la\),\1 -lpython%__python_version,g' python/Makefile
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%doc README* TODO

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
#%_datadir/aclocal

%files -n rapi-tools
%_bindir/*
%_man1dir/*
%_man3dir/*

%files -n python-module-librapi
%python_sitelibdir/*.so
%exclude %python_sitelibdir/*.la

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.15.2-alt1.1
- Rebuild with Python-2.7

* Thu Mar 03 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.2-alt1
- 0.15.2

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.1-alt1
- 0.15.1
- build withouth hal support
- disable versioning

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Mon May 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt1
- 0.15

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1.1
- Rebuilt with python 2.6

* Fri Aug 21 2009 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt1
- 0.14
- add versioning

* Sun Mar 01 2009 Alexey Shabalin <shaba@altlinux.ru> 0.13.1-alt1
- 0.13.1
- rename python package to python-module-librapi
- removed pre/post scripts

* Sun Oct 05 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12-alt1
- 0.12
- fix link with python

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 0.11-alt1.1
- Rebuilt with python-2.5.

* Wed Jan 09 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11-alt1
- 0.11

* Thu Jan 03 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt3
- update to SVN 20080102 version

* Fri Dec 07 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt2
- update to SVN 20071207 version

* Mon May 14 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt1
- 0.10.0
- buildreq updated
- removed old hack with chrpath

* Fri Jan 12 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Tue May 02 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt4
- pcp fix on x86_64 (patch by Andrzej Szombierski)

* Sun Feb 26 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt3
- x86_64 support

* Tue Feb 21 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt2
- FUR support

* Sun Jul 24 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Wed Sep 01 2004 Michael Shigorin <mike@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Sun Apr 25 2004 Michael Shigorin <mike@altlinux.ru> 0.8.9-alt1
- 0.8.9

* Thu Dec 18 2003 Michael Shigorin <mike@altlinux.ru> 0.8.1-alt4
- worked around changed behaviour of chrpath regarding non-ELF input

* Wed Dec 17 2003 Michael Shigorin <mike@altlinux.ru> 0.8.1-alt3
- removed *.la *and* uploaded -proper- packages, oops :-)

* Fri Nov 28 2003 Michael Shigorin <mike@altlinux.ru> 0.8.1-alt2
- removed *.la and devel-static subpackage

* Fri Nov 07 2003 Michael Shigorin <mike@altlinux.ru> 0.8.1-alt1
- built for ALT Linux

