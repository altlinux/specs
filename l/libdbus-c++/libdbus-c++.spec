# -*- mode: rpm-spec; coding: utf-8 -*-
%def_disable static

%define examples_dir %_prefix/src/%name-%version

Summary: A C++ bindings for libdbus and libdbus-glib
Name: libdbus-c++
Version: 0.5.0
Release: alt11.qa2
License: LGPLv2.1
Group: System/Libraries
URL: http://www.freedesktop.org/wiki/Software/dbus-c++
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

Source0: dbus-c++-%version.tar.bz2

# Automatically added by buildreq on Tue Jan 08 2008
BuildRequires: doxygen gcc-c++ libdbus-devel libexpat-devel glib2-devel

Provides: %name-etersoft = %version-%release

%description
This package contains C++ bindings for libdbus and libdbus-glib, provides
ability to reflect dbus methods and signals into a more natural C++ object system

%package devel
Summary: Development files for libdbus-c++
Group: Development/C++
Requires: %name = %version-%release
Provides: %name-etersoft-devel = %version-%release

%description devel
This package provides development files for libdbus-c++.

%if_enabled static
%package devel-static
Summary: Static version of libdbus-c++
Group: Development/C++
Requires: %name-devel = %version-%release
Provides: %name-etersoft-devel-static = %version-%release
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
Requires: %name-devel = %version
%description examples
Example programs which make use of libdbus-c++

%prep
%setup -q -n dbus-c++

%build
./autogen.sh

%configure \
	   --enable-glib \
	   --enable-doxygen-docs \
	   %{subst_enable static} \
	   #

%make_build

%install
%makeinstall_std

# install apidocs manually
mkdir -p %buildroot%_defaultdocdir/%name-%version
cp -pr AUTHORS TODO doc/html %buildroot%_defaultdocdir/%name-%version
mkdir -p %buildroot%examples_dir
cp -pr config.{status,sub} Makefile{,.in,.am} missing install-sh %buildroot%examples_dir/
cp -pr examples/ %buildroot%examples_dir/
for d in %buildroot%examples_dir/examples/*/.libs; do
    (cd $d; mv -f * ../;);
#    rm -rf $d;
done
find %buildroot%examples_dir/ -type f -print0 | \
     xargs -0 sed -i -e 's,%_builddir/dbus-c++,%examples_dir,g'

%clean

%files
%doc %_defaultdocdir/%name-%version/AUTHORS
%doc %_defaultdocdir/%name-%version/TODO
%_libdir/libdbus*.so.*
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/libdbus-c++-%version 

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
%doc %_defaultdocdir/%name-%version/html
%exclude %_defaultdocdir/%name-%version/html/Makefile.am

%files examples
%examples_dir

%changelog
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


