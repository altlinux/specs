Name: libical
Version: 0.47
Release: alt1
Summary: An implementation of basic iCAL protocols
License: LGPL/MPL
Group: System/Libraries
Url: http://sourceforge.net/projects/freeassociation/

Source: http://ovh.dl.sourceforge.net/sourceforge/freeassociation/%name-%version.tar.gz

BuildRequires: cmake gcc-c++

%description
Libical is an Open Source implementation of the IETF's iCalendar Calendaring
and Scheduling protocols (RFC 2445, 2446, and 2447). It parses iCal components
and provides a C API for manipulating the component properties, parameters,
and subcomponents

%package devel
Summary: Files for developing applications that use libical
Requires: %name = %version-%release
Group: Development/C

%description devel
The header files and libtool library  for developing applications that use libical

%prep
%setup

%build
%define lib_suffix %nil
%ifarch x86_64 ppc64
%define lib_suffix 64
%endif
mkdir -p %_target_platform
pushd %_target_platform
cmake .. \
    -DCMAKE_INSTALL_PREFIX:PATH=%prefix \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DCMAKE_C_FLAGS_RELEASE:STRING='%optflags' \
    -DCMAKE_CXX_FLAGS_RELEASE:STRING='%optflags' \
    -DLIB_DESTINATION:PATH=%_lib \
    -DLIB_SUFFIX=%lib_suffix
popd
%make -C %_target_platform

%install
%make -C %_target_platform DESTDIR=%buildroot install

%files
%doc TODO NEWS TEST THANKS
%_libdir/*.so.*

%files devel
%doc doc/UsingLibical*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
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

