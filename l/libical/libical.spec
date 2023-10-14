%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define api_ver 3.0

%def_enable ninja
%def_with bdb
%def_enable ical_glib
%def_enable introspection
%def_enable vala
%define __isa_bits %(s="%_lib"; s=${s#lib}; echo "${s:-32}")
%if "%__isa_bits" == "64"
%def_enable check
%else
%def_disable check
%endif
%def_enable docs
%def_with cxx
%def_with system_tzdata

Name: libical
Version: 3.0.17
Release: alt1

Summary: An implementation of basic iCAL protocols
Group: System/Libraries
License: LGPL-2.1-only or MPL-2.0
Url: https://github.com/%name

%if_disabled snapshot
Source: %url/%name/releases/download/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

%define tzdata_ver 2023c
%define glib_ver 2.38
%define xml2_ver 2.7.3
%{?_with_system_tzdata:Requires: tzdata >= %tzdata_ver}

BuildRequires(pre): rpm-macros-cmake rpm-build-gir
BuildRequires: cmake gcc-c++ gtk-doc libicu-devel icu-utils
%{?_enable_ninja:BuildRequires: ninja-build}
%{?_with_system_tzdata:BuildRequires: tzdata >= %tzdata_ver}
%{?_with_bdb:BuildRequires: libdb4-devel}
%{?_enable_ical_glib:BuildRequires: libgio-devel >= %glib_ver libxml2-devel >= %xml2_ver}
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir
BuildRequires: gobject-introspection-devel}
%{?_enable_vala:BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_enable_check:BuildRequires: ctest python3-module-pygobject3}

%description
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents

%package devel
Summary: Files for developing applications that use libical
Group: Development/C
Requires: %name = %version-%release
# since 2.0.0
Requires: libicu-devel

%description devel
The header files and libtool library for developing applications that use
libical.

%package gir
Summary: GObject introspection data for the Libical
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Libical library.

%package gir-devel
Summary: GObject introspection devel data for the Libical
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the Libical library.

%package -n %name-glib
Summary: A GObject interface of the libical library
Group: System/Libraries
Requires: %name = %version-%release

%description -n %name-glib
This package provides Libical-Glib library with GObject bindings to
libical library.

%package -n %name-glib-devel
Summary: Files for developing applications that use Libical-Glib
Group: Development/C
Requires: %name-glib = %version-%release
Requires: %name-devel = %version-%release

%description -n %name-glib-devel
The header files and libtool library for developing applications that use
Libical-Glib.

%package -n %name-glib-gir
Summary: GObject introspection data for the Libical-Glib
Group: System/Libraries
Requires: %name-glib = %version-%release

%description -n %name-glib-gir
GObject introspection data for the Libical-Glib library.

%package -n %name-glib-gir-devel
Summary: GObject introspection devel data for the Libical-Glib
Group: Development/Other
BuildArch: noarch
Requires: %name-glib-gir = %version-%release
Requires: %name-glib-devel = %version-%release

%description -n %name-glib-gir-devel
GObject introspection devel data for the Libical-Glib library.

%package -n %name-glib-devel-doc
Summary: Development documentation for Libical-Glib
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-gloib-devel < %version-%release

%description -n %name-glib-devel-doc
This package contains development documentation for the Libical-Glib
library.

%prep
%setup
#src/libical/icaltz-util.h:#define ZONES_TAB_SYSTEM_FILENAME "zone.tab"
sed -i 's|zone.tab|zone1970.tab|' src/libical/icaltz-util.h

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
	%{?_enable_ninja:-GNinja} \
	-DCMAKE_BUILD_TYPE:STRING="Release" \
	-DSHARED_ONLY:BOOL=ON \
	%{?_with_cxx:-DWITH_CXX_BINDINGS:BOOL=ON} \
	%{?_enable_ical_glib:-DICAL_GLIB:BOOL=ON} \
	%{?_enable_introspection:-DGOBJECT_INTROSPECTION:BOOL=ON} \
	%{?_enable_vala:-DICAL_GLIB_VAPI=ON} \
	%{?_disable_docs:-DICAL_BUILD_DOCS:BOOL=OFF} \
	%{?_with_system_tzdata:-DUSE_BUILTIN_TZDATA:BOOL=OFF}
%nil
%cmake_build

%install
%cmake_install

%check
%cmake_build -t test

%files
%_libdir/libical.so.*
%_libdir/libicalss.so.*
%_libdir/libicalvcal.so.*
%if_with cxx
%_libdir/libical_cxx.so.*
%_libdir/libicalss_cxx.so.*
%endif
%doc TODO TEST THANKS ReleaseNotes.txt README*

%files devel
%_includedir/%name/
%_libdir/libical.so
%_libdir/libicalss.so
%_libdir/libicalvcal.so
%if_with cxx
%_libdir/libical_cxx.so
%_libdir/libicalss_cxx.so
%endif
%_pkgconfigdir/%name.pc
%_libdir/cmake/LibIcal/
%doc doc/UsingLibical*

%files -n %name-glib
%_libdir/%name-glib.so.*

%files -n %name-glib-devel
%_libexecdir/%name/ical-glib-src-generator
%_includedir/%name-glib/
%_libdir/%name-glib.so
%_pkgconfigdir/%name-glib.pc
%{?_enable_vala:%_vapidir/*}

%if_enabled introspection
%files gir
%_typelibdir/ICal-%api_ver.typelib

%files gir-devel
%_girdir/ICal-%api_ver.gir

%files -n %name-glib-gir
%_typelibdir/ICalGLib-%api_ver.typelib

%files -n %name-glib-gir-devel
%_girdir/ICalGLib-%api_ver.gir
%endif

%if_enabled docs
%files -n %name-glib-devel-doc
%_datadir/gtk-doc/html/%name-glib/
%endif


%changelog
* Sun Oct 15 2023 Yuri N. Sedunov <aris@altlinux.org> 3.0.17-alt1
- 3.0.17

* Sun Jul 09 2023 Yuri N. Sedunov <aris@altlinux.org> 3.0.16-alt2
- updated to v3.0.16-18-gcdfdaa02
- built with system tzdata (2023c-alt1)
- src/libical/icaltz-util.h:
  switched ZONES_TAB_SYSTEM_FILENAME to zone1970.tab

* Tue Oct 18 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.16-alt1
- 3.0.16

* Fri Oct 07 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.15-alt1
- 3.0.15

* Tue Mar 01 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.14-alt1
- 3.0.14

* Tue Jan 18 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.13-alt1
- 3.0.13

* Thu Dec 09 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.12-alt1
- 3.0.12
- build with ninja instead of make

* Sun Oct 10 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.11-alt1
- 3.0.11

* Tue May 11 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.10-alt1.1
- rebuild with new cmake macros

* Sun Apr 18 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.10-alt1
- 3.0.10

* Sat Feb 27 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.9-alt1
- updated to v3.0.9-8-g66b2fe2d

* Sun Mar 15 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0.8-alt1
- 3.0.8

* Mon Dec 16 2019 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt1
- 3.0.7

* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 3.0.6-alt1
- 3.0.6

* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.0.5-alt2
- added ical-glib Vala bindings

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.0.5-alt1
- 3.0.5

* Wed Aug 15 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Wed Jul 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt3
- rebuilt against libicu*.so.62

* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt2.1
- rebuilt for e2kv4

* Tue Mar 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt2
- fixed buildreqs

* Thu Mar 01 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Sun Feb 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Mon Nov 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1
- new libical-glib-* subpackages

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

