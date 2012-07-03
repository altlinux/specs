%def_disable static

Name: libccrtp
Version: 1.7.1
Release: alt3.1

%define docdir %_docdir/%name-%version

Summary: Common C++ class framework for RTP/RTCP

License: GPL
Group: System/Libraries
Url: http://www.gnu.org/software/ccrtp/

Source: %name-%version-%release.tar
Patch: %name-1.7.1-alt-gcc4.6.patch

BuildRequires: doxygen gcc-c++ libcommoncpp2-devel >= 1.7.0 libgcrypt-devel libstdc++-devel

%description
ccRTP is a generic, extensible and efficient C++ framework for
developing applications based on the Real-Time Transport Protocol
(RTP) from the IETF. It is based on Common C++ and provides a full
RTP/RTCP stack for sending and receiving of realtime data by the use
of send and receive packet queues. ccRTP supports unicast,
multi-unicast and multicast, manages multiple sources, handles RTCP
automatically, supports different threading models and is generic as
for underlying network and transport protocols.

%package devel
Summary: Header files for ccrtp library
Group: Development/Other
Requires: %name = %version-%release
Requires: libcommoncpp2-devel >= 1.6.1

%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%package doc
Summary: Documentation for %name
Group: Development/C

%description devel
Header files for ccrtp library.

%description devel-static
Common C++ devel static files

%description doc
Documentation for %name

%prep
%setup
%patch -p1

%build
%configure %{subst_enable static}
make

%install
%make_install install DESTDIR=%buildroot
mkdir -p %buildroot%docdir
cp -a AUTHORS COPYING.addendum README doc/srcmodel* doc/html %buildroot%docdir

%files
%dir %docdir
%docdir/[A-Z]*
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/ccrtp
%_pkgconfigdir/*.pc

%files doc
%docdir/html
%docdir/srcmodel*
%_infodir/*.info*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Tue Jun 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt3.1
- Fixed build with gcc 4.6

* Wed Nov 10 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.1-alt3
- rebuilt with new commoncpp

* Fri Nov 20 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.1-alt2
- obsolete by filetriggers macros removed, again

* Fri May  8 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.1-alt1
- 1.7.1 released

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.2-alt2
- obsolete by filetriggers macros removed

* Sun Oct 26 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.2-alt1
- 1.6.2 released

* Sun Feb 24 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.0-alt1
- 1.6.0 released

* Sat Jan  6 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt0.2
- 1.5.1 released

* Wed Sep 20 2006 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt0.2
- rebuild with new libcommoncpp2

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt0.1
- new version 1.4.1 (with rpmrb script)

* Wed Feb 08 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt0.2
- rebuild with new libcommoncpp2 (1.3.22)

* Mon Jan 02 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)
