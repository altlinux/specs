%def_enable snapshot
%define _name libical
%define ver_major 2

%def_with bdb
%def_disable introspection

Name: %_name%ver_major
Version: %ver_major.0.1
Release: alt0.5

Summary: An implementation of basic iCAL protocols
Group: System/Libraries
License: LGPL2.1+/MPL-1.0
Url: https://github.com/%_name

%if_disabled snapshot
Source: %url/%_name/releases/download/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Patch: %_name-1.0.1-alt-libdir.patch

BuildRequires: cmake gcc-c++ ctest libicu-devel
%{?_with_bdb:BuildRequires: libdb4-devel}
%{?_enable introspection:BuildRequires: gobject-introspection-devel}

%description
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents

%prep
%setup -n %_name-%version
%patch -p1

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
	-DSHARED_ONLY:BOOL=ON \
	%{?_with_bdb:-DWITH_BDB:BOOL=ON} \
	%{?_enable_introspection:-DGOBJECT_INTROSPECTION:BOOL=ON} \
	-DUSE_INTEROPERABLE_VTIMEZONES:BOOL=ON
%cmake_build

%install
%cmakeinstall_std

%check
LD_LIBRARY_PATH=%buildroot%_libdir %make test -C BUILD

%files
%doc TODO TEST THANKS
%_libdir/*.so.*

%exclude %_includedir/*
%exclude %_libdir/*.so
%exclude %_pkgconfigdir/*.pc
%exclude %_libdir/cmake/*

%changelog
* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt0.5
- compat library

* Mon Jun 20 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt0.4
- updated to v2.0.0-8-g6feb01a
- used interoperable rather than exact vtimezones
  (https://sourceforge.net/p/freeassociation/bugs/95/#ff5c)

* Mon Feb 08 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt0.3
- rebuild against libicu*.so.56

* Mon Jan 25 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt0.2
- added libicu-devel as dependence for -devel subpackage

* Mon Jan 25 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt0.1
- updated to v2.0.0-5-g2402a36

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Thu Sep 10 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt3
- built with SHARED_ONLY=ON to prevent cmake search for the static libraries (ALT #31266)

* Fri Mar 27 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt2
- CMakeLists.txt: fixed hardcoded libdir producing broken
  pkgconfig file under x86_64

* Fri Dec 26 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Wed Nov 20 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt2
- soname bump
- %%check section

* Sat Nov 16 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Sat Nov 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.47-alt1
- 0.47

* Sat Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.46-alt1
- 0.46

* Sat May 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.44-alt1
- 0.44

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.43-alt1
- change mainstream
- new version

* Fri Mar 16 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.26-alt3
- new release

* Wed Nov 1 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.26-alt2
- fix pkgconfig file

* Sun Oct 29 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.26-alt1
- new version from http://www.aurore.net/projects/libical/ fork of libical

* Wed Dec 14 2005 Vitaly Lipatov <lav@altlinux.ru> 0.24-alt0.2RC4
- add missed dir
- add RC sign to release

* Fri Nov 04 2005 Vitaly Lipatov <lav@altlinux.ru> 0.24-alt0.1
- new version (spec updated according to spec from PLD)

* Wed May 12 2004 Ott Alex <ott@altlinux.ru> 0.23a-alt3
- Remove .la files

* Mon Dec 23 2002 AEN <aen@altlinux.ru> 0.23a-alt2
- #dir %_includedir/libicalvcal added

* Thu Oct 03 2002 AEN <aen@altlinux.ru> 0.23a-alt1
- first build for Sisyphus, sources from mozilla cvs

