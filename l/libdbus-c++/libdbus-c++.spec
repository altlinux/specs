# -*- mode: rpm-spec; coding: utf-8 -*-
%def_disable static

Summary: A C++ bindings for libdbus and libdbus-glib
Name: libdbus-c++
Version: 0.9.0
Release: alt2
License: LGPLv2.1
Group: System/Libraries
URL: http://www.freedesktop.org/wiki/Software/dbus-c++

Provides: %name-etersoft = %EVR

Source0: dbus-c++-%version.tar.bz2
# SuSE
Patch1: libdbus-c++-gcc47.patch
Patch2: libdbus-c++-nodocdatetime.patch
Patch3: libdbus-c++-noreturn.patch
Patch4: libdbus-c++-pthread.patch
# Debian
Patch5: libdbus-c++-0.9.0-debian-fix-gcc-7-ftbfs.patch
Patch6: libdbus-c++-0.9.0-debian-fix-mutex-ftbfs.patch
# ALT
Patch10: libdbus-c++-0.9.0-alt-linking.patch
Patch11: libdbus-c++-0.9.0-alt-is_running.patch
Patch12: libdbus-c++-0.9.0-alt-enable_auth.patch
Patch13: libdbus-c++-0.9.0-alt-enable_anon.patch

# Automatically added by buildreq on Mon Feb 18 2013 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel libatk-devel libatkmm-devel libcairo-devel libcairomm-devel libdbus-c++ libdbus-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglibmm-devel libgtk+2-devel libpango-devel libpangomm-devel libsigc++2-devel libstdc++-devel libsystemd-daemon libwayland-client libwayland-server pkg-config python-base ruby ruby-stdlibs
#BuildRequires: cups-filters doxygen fonts-ttf-dejavu gcc-c++ glibc-devel-static graphviz libdbus-c++-devel libexpat-devel libgtkmm2-devel rpm-build-ruby
BuildRequires: doxygen gcc-c++ glibc-devel libexpat-devel libdbus-devel libgtkmm2-devel
BuildRequires: /usr/bin/dot

%description
This package contains C++ bindings for libdbus and libdbus-glib, provides
ability to reflect dbus methods and signals into a more natural C++ object system

%package devel
Summary: Development files for libdbus-c++
Group: Development/C++
Requires: %name = %EVR
Provides: %name-etersoft-devel = %EVR

%description devel
This package provides development files for libdbus-c++.

%if_enabled static
%package devel-static
Summary: Static version of libdbus-c++
Group: Development/C++
Requires: %name-devel = %EVR
Provides: %name-etersoft-devel-static = %EVR
%description devel-static
This package contains static version of libdbus-c++ library.
%endif

%package apidocs
Summary: libdbus-c++ API documentation
Group: Development/C++
%description apidocs
This package contains Doxygen-generated API documentation for libdbus-c++ library

%package examples
Summary: Example programs which make use of libdbus-c++
Group: Development/C++
Requires: %name-devel = %EVR
%description examples
Example programs which make use of libdbus-c++

%prep
%setup -q -n dbus-c++
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p1
%patch6 -p1
#
%patch10 -p0
%patch11 -p1
%patch12 -p1
%patch13 -p1
./bootstrap

%build
%configure \
	   --disable-ecore \
	   --enable-glib \
	   --enable-doxygen-docs \
	   --disable-examples \
	   %{subst_enable static} \
	   #
%make -C src libdbus-c++-1.la
%make_build
rm -rf libdbus-c*%{version}-doc
tar xvfj libdbus-c*%{version}-doc.tar.bz2

%install
%make -C src DESTDIR=%buildroot install-libLTLIBRARIES
%makeinstall
make -C examples clean

%files
%doc AUTHORS
%doc TODO
%_libdir/libdbus*.so.*

%files devel
%_libdir/libdbus*.so
%_includedir/dbus-c++-?
%_pkgconfigdir/dbus-c++*.pc
# Also include tools here
%_bindir/*

%if_enabled static
%files devel-static
%_libdir/libdbus*.a
%endif

%files apidocs
%doc libdbus-c*%{version}-doc/doc/html

%files examples
%doc examples

%changelog
* Tue May 15 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt2
- Fixed build with new toolchain.

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Feb 18 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- new version
- merge patches from SuSE

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt11.qa2
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.0-alt11.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for libdbus-c++
  * postclean-05-filetriggers for spec file

* Sat Jul 11 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.5.0-alt11
- Fix installation error for debug.h

* Fri Jul 10 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.5.0-alt10
- Update to last upstream changes
- Fix build with gcc-4.4

* Thu Apr 02 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.5.0-alt9
- Add anonymous support for authentification

* Tue Mar 31 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.5.0-alt8
- Add providing for specify patched library by Etersoft
 + libdbus-c++-etersoft
 + libdbus-c++-etersoft-devel
 + libdbus-c++-etersoft-devel-static
- Change packager

* Wed Mar 25 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.5.0-alt7
- Add some improvements to library:
 + added unix user function support for authentification
 + fixed detach_connection() method in Server

* Tue Mar 24 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.5.0-alt6
- Add some improvements to library:
 + fixed potential problems with RefCnt destroyed pointer
 + fixed detach_server() for terminated connections
 + added run() method to BusDispatcher

* Thu Mar 05 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.5.0-alt5
- Update from freedesktop (update since to Sun Feb 22 2009)
- Add some improvements to library:
 + added detach_connection() method to Server
 + added is_running() method to BusDispatcher

* Thu Mar 05 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.5.0-alt4
- Update from freedesktop (update since to Thu Jan 8 2009)
- Change package SPEC-file from morozov@ repo at git.alt

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt3
- fix build with gcc 4.3
- cleanup spec, remove post/postun sections

* Tue Jan 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt2
- build with glib (add glib-integration.h)

* Tue Jan 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- initial build for ALT Linux Sisyphus

* Mon Jul  2 2007 Alexey Morozov <morozov@altlinux.org> 0.5.0-alt1.svn11223
- Initial build for ALT Linux

* Thu Feb 8 2007 Ben Martin
- initial spec file


