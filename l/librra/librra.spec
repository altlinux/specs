Name: librra
Version: 0.14
Release: alt2.1
Packager: Mobile Development Team <mobile@packages.altlinux.org>
Summary: Synchronization library for SynCE
License: MIT
Group: System/Libraries

Url: http://synce.sourceforge.net
Source: %name-%version.tar.gz
Source1: %name-0.14.map
Patch1: %name-0.14-alt-link-python.patch
Patch2: %name-0.14-alt-symver.patch

BuildPreReq: libsynce-devel >= 0.14
BuildPreReq: librapi-devel >= 0.14
BuildPreReq: python-module-Pyrex
BuildPreReq: libmimedir
BuildRequires: gcc-c++ time

%description
Required to communicate with a handheld device running WinCE

%package devel
Summary: Libraries and headers needed for developing with librra
Group: Development/C
Requires: %name = %version

%description devel
Libraries and headers needed for developing with librra


%package -n python-module-librra
Summary: librra python interface
Group: Development/Python
Requires: %name = %version-%release
Provides: librra-python = %version-%release
Obsoletes: librra-python

%description -n python-module-librra
Python wrappers for %name

%prep
%setup -q
%patch1 -p1
# %patch2 -p1
# install -p -m644 %SOURCE1 lib/%name.map


%build
%autoreconf
%configure --disable-static --disable-rpath --enable-recurrence
%make

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%doc README
%_bindir/*
%_man1dir/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n python-module-librra
%python_sitelibdir/*.so
%exclude %python_sitelibdir/*.la

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.14-alt2.1
- Rebuild with Python-2.7

* Thu Mar 03 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt2
- rebuild
- disable versioning
- fix link with libpython2.6

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1.1
- Rebuilt with python 2.6

* Mon Aug 24 2009 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt1
- 0.14
- add versioning

* Sun Mar 01 2009 Alexey Shabalin <shaba@altlinux.ru> 0.13-alt1
- 0.13
- rename python package to python-module-librra

* Sun Oct 05 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12-alt1
- 0.12

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 0.11-alt1.1
- Rebuilt with python-2.5.

* Wed Jan 09 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11-alt1
- 0.11

* Wed Jan 02 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt3
- update to SVN 20080102 version

* Fri Dec 07 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt2
- update to SVN 20071207 version

* Mon May 14 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Sat Jul 15 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt7
- gcc4.1 compatible

* Sun Feb 26 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt6
- x86_64 support

* Mon Nov 07 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt5
- synce-build-patch applyed

* Sun Jul 24 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt4
- 0.9.1

* Mon May 23 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.9.0-alt4
- rra-all_day_event_local_time patch added

* Sat May 14 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.9.0-alt3
- rra-comma_separated patch added
- rra-recurrence-escape patch added

* Mon May 09 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.9.0-alt2
- updating rra patch (2 fields fix)

* Wed Apr 27 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.9.0-alt1
- patch from synce-devel@ (thanks to mike@)
- changing Packager field
- original spec belong to Michael Shigorin <mike@altlinux.ru>:
- 0.9.0
- patch merged upstream
- added %_datadir/aclocal/*.m4
- moved *.h to %_includedir/rra/

* Sun Apr 25 2004 Michael Shigorin <mike@altlinux.ru> 0.8.9-alt1
- 0.8.9
- build fix suggested by David Eriksson <twogood users sourceforge net>
- added synce-matchmaker binary/manpage

* Fri Nov 28 2003 Michael Shigorin <mike@altlinux.ru> 0.8.4-alt2
- removed *.la and devel-static subpackage

* Wed Nov 26 2003 Michael Shigorin <mike@altlinux.ru> 0.8.4-alt1
- built for ALT Linux (SynCE dependency)

