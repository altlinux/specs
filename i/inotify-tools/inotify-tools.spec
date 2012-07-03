Name: inotify-tools
Version: 3.14
Release: alt1

Summary: Command line utilities for inotify
Group: System/Kernel and hardware
License: GPL
Url: https://github.com/rvoicilas/inotify-tools/wiki/

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

Requires: libinotifytools = %version-%release

# Automatically added by buildreq on Sun Apr 15 2012
BuildRequires: doxygen

%description
inotify-tools is a set of command-line programs for Linux providing
a simple interface to inotify. These programs can be used to monitor
and act upon filesystem events.

%package -n libinotifytools
Summary: Shared library for inotifytools
Group: System/Libraries

%description -n libinotifytools
inotify-tools is a set of command-line programs for Linux providing
a simple interface to inotify. These programs can be used to monitor
and act upon filesystem events.

This is package contains shared library.

%package devel
Summary: Headers and libraries for building apps that use libinotifytools
Group: Development/C
Requires: libinotifytools = %version-%release

%description devel
inotify-tools is a set of command-line programs for Linux providing
a simple interface to inotify. These programs can be used to monitor
and act upon filesystem events.

This package contains headers and libraries required to build applications
that use the libinotifytools library.

%prep
%setup -q

%build
%autoreconf
%configure \
	--disable-static
%make_build
make check || exit 1

%install
%make_install DESTDIR=%buildroot install

rm -rf %buildroot%_datadir/doc/

%files
%doc AUTHORS NEWS README
%_bindir/*
%_man1dir/*

%files -n libinotifytools
%_libdir/libinotifytools.so.*

%files devel
%doc libinotifytools/src/doc/html/*
%_libdir/libinotifytools.so
%dir %_includedir/inotifytools
%_includedir/inotifytools/*.h

%changelog
* Sun Apr 15 2012 Igor Zubkov <icesik@altlinux.org> 3.14-alt1
- 3.13 -> 3.14

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 3.13-alt4
- apply patch from repocop

* Sun Jul 27 2008 Igor Zubkov <icesik@altlinux.org> 3.13-alt3
- don't use obsolete macros

* Tue Jan 08 2008 Igor Zubkov <icesik@altlinux.org> 3.13-alt2
- move inotifytools library in subpackage libinotifytools

* Sat Jan 05 2008 Igor Zubkov <icesik@altlinux.org> 3.13-alt1
- 3.12 -> 3.13

* Sat Nov 24 2007 Igor Zubkov <icesik@altlinux.org> 3.12-alt1
- 3.11 -> 3.12

* Tue Sep 18 2007 Igor Zubkov <icesik@altlinux.org> 3.11-alt1
- 3.10 -> 3.11 (security release):
  + Fixes a buffer overflow in the inotifytools_snprintf function

* Sat May 05 2007 Igor Zubkov <icesik@altlinux.org> 3.10-alt1
- 3.9 -> 3.10

* Sun Apr 29 2007 Igor Zubkov <icesik@altlinux.org> 3.9-alt1
- 3.8 -> 3.9

* Wed Apr 18 2007 Igor Zubkov <icesik@altlinux.org> 3.8-alt1
- 2.6 -> 3.8

* Wed Oct 25 2006 Igor Zubkov <icesik@altlinux.org> 2.6-alt2
- import to gear
- rebuild with new gcc + glibc

* Tue Oct 03 2006 Igor Zubkov <icesik@altlinux.ru> 2.6-alt1
- 2.4 -> 2.6

* Sun Sep 10 2006 Igor Zubkov <icesik@altlinux.org> 2.4-alt1
- 2.3 -> 2.4
- buildreq

* Tue Aug 15 2006 Igor Zubkov <icesik@altlinux.ru> 2.3-alt1
- 2.2 -> 2.3

* Thu Jul 06 2006 Igor Zubkov <icesik@altlinux.ru> 2.2-alt1
- 2.2
- change url -> http://inotify-tools.sourceforge.net/

* Wed Jul 05 2006 Igor Zubkov <icesik@altlinux.ru> 2.1-alt1
- 2.1

* Thu May 11 2006 Igor Zubkov <icesik@altlinux.ru> 1.5-alt1
- 1.5

* Fri Apr 28 2006 Igor Zubkov <icesik@altlinux.ru> 1.4-alt1
- 1.4

* Thu Apr 27 2006 Igor Zubkov <icesik@altlinux.ru> 1.3-alt1
- Initial build for Sisyphus
