%def_disable static

Name: libcommoncpp2
Version: 1.8.1
Release: alt2

%define docdir %_docdir/%name-%version

Summary: "Common C++ v2" - A GNU package for creating portable C++ programs

License: GPL
Group: Development/C++
Url: http://cplusplus.sourceforge.net/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libstdc++-devel zlib-devel libxml2-devel doxygen
BuildRequires: info

%description
Common C++ is a GNU package which offers portable "abstraction" of system
services such as threads, networks, and sockets.  Common C++ also offers
individual frameworks generally useful to developing portable C++
applications including a object persistance engine, math libraries,
threading, sockets, etc.  Common C++ is small, and highly portable.
Common C++ will support most Unix operating systems as well
as Win32, in addition to GNU/Linux.

%package devel
Summary: Common C++ devel files
Group: Development/C
Requires: %name = %version-%release
Requires: libstdc++-devel zlib-devel libxml2-devel gcc-c++

%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%package doc
Summary: Documentation for %name
Group: Development/C

%description devel
Common C++ devel files

%description devel-static
Common C++ devel static files

%description doc
Documentation for %name

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static}
# SMP-b0rken
make

%install
%make_install install DESTDIR=%buildroot
mkdir -p %buildroot%docdir
cp -a AUTHORS NEWS README THANKS TODO doc/html %buildroot%docdir

%files
%dir %docdir
%docdir/[A-Z]*
%_libdir/*.so.*

%files devel
%_bindir/*
%_libdir/*.so
%_datadir/aclocal/*
%_includedir/*
%_pkgconfigdir/*

%if_enabled statc
%files devel-static
%_libdir/*.a
%endif

%files doc
%docdir/html
%_infodir/commoncpp2.*

%changelog
* Thu Dec 15 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.1-alt2
- rebuilt without rpath pointing to standard paths

* Wed Nov 10 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.1-alt1
- 1.8.1 released

* Fri Nov 20 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.3-alt2
- obsolete by filetriggers macros removed, again

* Fri May  8 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.3-alt1
- 1.7.3 released

* Thu Feb 12 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt1
- 1.7.0 released

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt2
- obsolete by filetriggers macros removed

* Sun Oct 26 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt1
- 1.6.3 released

* Sun Feb 24 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.1-alt1
- 1.6.1 released

* Sat Jan  6 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.3-alt0.2
- 1.5.3 released

* Sun Sep 17 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.26-alt0.1
- new version (1.3.26)
- fix includes (bug #10010), thanks to Valery Inozemtsev

* Wed Apr 05 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.25-alt0.1
- new version (1.3.25)
- change packager, build with ld --as-needed
- cleanup spec, enable make_build

* Wed Feb 08 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.22-alt2
- NMU: big spec cleanups
- fix install method, add README, etc. to main package
- add pkgconfig files to -devel package
- doc package does not require %name anymore
- static package requires %name-devel now

* Thu Jan 05 2006 Gor <vg@altlinux.ru> 1.3.22-alt1
- new version (fix bug #8779)
- small spec cleanups 

* Mon Jan 17 2005 Gor <vg@altlinux.ru> 1.2.5-alt1
- new version
- move to gcc-3.4 

* Wed Feb 25 2004 Gor <vg@altlinux.ru> 1.1.0-alt2
- spec cleanups about infodir

* Thu Feb 19 2004 Gor <vg@altlinux.ru> 1.1.0-alt1
- new version , url fixed

* Tue Dec 30 2003 Gor <vg@altlinux.ru> 1.0.13-alt4
- gcc3.3 fix

* Wed Dec 24 2003 Gor <vg@altlinux.ru> 1.0.13-alt3
- small build fix

* Mon Sep 08 2003 Gor <vg@altlinux.ru> 1.0.13-alt2
- small build fix

* Fri Aug 29 2003 Gor <vg@altlinux.ru> 1.0.13-alt1
- new version

* Thu Feb 20 2003 Gor <vg@altlinux.ru> 1.0.8-alt2
- missing dep to libxml2 added

* Tue Feb 18 2003 Gor <vg@altlinux.ru> 1.0.8-alt1
- new version

* Wed Nov 20 2002 Gor <vg@altlinux.ru> 1.0.6-alt1
- new version

* Thu Oct 17 2002 Gor <vg@altlinux.ru> 1.0.5-alt1
- new version

* Tue Sep 3 2002 Gor <vg@altlinux.ru> 1.0.1-alt0.1
- new version
- built with & require g++3.2

* Mon Aug 27 2002 Gor <vg@altlinux.ru> 1.0.0-alt0.2
- .spec cleanups

* Mon Aug 26 2002 Gor <vg@altlinux.ru> 1.0.0-alt0.1
- New version

* Tue Jun 11 2002 Gor <gor@mail.od.ua> 0.99.4-alt0.2
- initial build of V2
- manpages moved to doc package
