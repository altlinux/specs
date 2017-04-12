Summary: Libraries to provide access to RTAS calls and RTAS events
Name: librtas
Version: 2.0.1
Release: alt1
URL:     https://github.com/nfont/librtas
License: LGPL
Group:   System/Libraries

Source0: v%version.tar.gz
Patch0:  %name-2.0.1-libversion.patch
Patch1: librtas-2.0.1-alt-pc.patch

%description
The librtas shared library provides userspace with an interface
through which certain RTAS calls can be made.  The library uses
either of the RTAS User Module or the RTAS system call to direct
the kernel in making these calls.

The librtasevent shared library provides users with a set of
definitions and common routines useful in parsing and dumping
the contents of RTAS events.

%package devel
Summary: C header files for development with librtas
Group: Development/C

%description devel
The librtas-devel packages contains the header files necessary for
developing programs using librtas.

%prep
%setup -q -n %name-%version
%patch0 -p1 -b .ln
%patch1 -p1

%build
%autoreconf
%configure \
	--disable-silent-rules \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc COPYING.LESSER README Changelog
%_libdir/librtas*.so.*

%files devel
%_libdir/librtas*.so
%_pkgconfigdir/librtas.pc
%_includedir/librtas*.h

%changelog
* Wed Apr 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.1-alt1
- initial release

