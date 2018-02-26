Name: liboop
Version: 1.0
Release: alt3.qa2

Summary: Libraries for low-level event loop management

License: LGPL
Group: System/Libraries
Url: http://liboop.ofb.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://download.ofb.net/liboop/%name.tar.bz2

Patch0: %name-libwww-fix.patch
Patch1: %name-nolibs.patch
Patch2: %name-as-needed.patch

# Automatically added by buildreq on Wed Jan 16 2008
BuildRequires: gcc-c++ glib2-devel libadns-devel libreadline-devel libssl-devel libtcl tcl-devel w3c-libwww-devel zlib-devel

%description
liboop is a low-level event loop management library for POSIX-based
operating systems. It supports the development of modular, multiplexed
applications which may respond to events from several sources. It
replaces the "select() loop" and allows the registration of event
handlers for file and network I/O, timers and signals. Since processes
use these mechanisms for almost all external communication, liboop can
be used as the basis for almost any application.

%package bindings
Summary: liboop bindings for specific libraries
Group: Development/Other
Requires: %name = %version

%description bindings
liboop bindings for specific libraries (dns, glib, readline).

%package binding-tcl
Summary: liboop binding for tcl library
Group: Development/Other
Requires: %name = %version

%description binding-tcl
liboop binding for tcl library.

%package binding-www
Summary: liboop binding for w3c-libwww library
Group: Development/Other
Requires: %name = %version

%description binding-www
liboop binding for w3c-libwww library.

%package devel
Summary: Header files for liboop
Group: Development/Other
Requires: %name = %version

%description devel
liboop is a low-level event loop management library.

This package contains the header files and libraries needed to write
or compile programs that use liboop.

%package bindings-devel
Summary: Header files for liboop binding libraries
Group: Development/Other
Requires: %name-bindings = %version
Requires: %name-devel = %version

%description bindings-devel
liboop is a low-level event loop management library.

This package contains the header files and libraries needed to write
or compile programs that use liboop binding libraries.

%package binding-tcl-devel
Summary: Header file for liboop tcl binding library
Group: Development/Other
Requires: %name-binding-tcl = %version
Requires: %name-devel = %version
Requires: tcl-devel

%description binding-tcl-devel
This package contains the header file needed to write or compile
programs that use liboop tcl binding library.

%package binding-www-devel
Summary: Header file for liboop w3c-libwww binding libraries
Group: Development/Other
Requires: %name-bindings = %version
Requires: %name-devel = %version
Requires: w3c-libwww-devel

%description binding-www-devel
This package contains the header file needed to write or compile
programs that use liboop w3c-libwww binding library.


%prep
%setup -q
#%patch0 -p1
#%patch1 -p1
%patch2
%__subst "s|8\.3 |8.5 |g" configure.ac

%build
%autoreconf
%configure --disable-static --with-libwww --with-glib
# hack for SMP build
%make_build || %make

%install
%makeinstall_std

%files
%_libdir/liboop.so.*

%files devel
%_libdir/liboop.so
#%_libdir/liboop.la
%_includedir/oop.h
%_includedir/oop-read.h

%files bindings
%_libdir/liboop-adns.so.*
%_libdir/liboop-glib2.so.*
%_libdir/liboop-rl.so.*

%files binding-tcl
%_libdir/liboop-tcl.so.*

%files binding-www
%_libdir/liboop-www.so.*

%files bindings-devel
%_libdir/liboop-adns.so
%_libdir/liboop-glib2.so
%_libdir/liboop-rl.so
%_includedir/oop-adns.h
%_includedir/oop-glib.h
%_includedir/oop-rl.h
%_pkgconfigdir/*

%files binding-tcl-devel
%_libdir/liboop-tcl.so
%_includedir/oop-tcl.h

%files binding-www-devel
%_libdir/liboop-www.so
%_includedir/oop-www.h

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3.qa2
- Fixed build

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sun Jan 11 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt3
- cleanup spec
- fix build with new libtcl8.5

* Wed Jan 16 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- update buildreq
- build with glib2

* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1.1
- fix for as-needed in test compiling
- disable glib build

* Sun Mar 26 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- patch for ld --as-needed 

* Tue Dec 27 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)
- disable build with glib
