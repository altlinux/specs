Name: libxcbutil
Version: 0.3.6
Release: alt2
Serial: 1
Summary: XCB support libraries
License: MIT
Group: System/Libraries
URL: http://xcb.freedesktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xcb-util = %version-%release
Obsoletes: xcb-util < %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gperf libxcb-devel xorg-xproto-devel

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

These libraries are currently included, roughly ordered by maturity:
render-util: Convenience functions for the Render extension.
aux: Convenient access to connection setup and some core requests.
atom: Standard core X atom constants and atom caching.
property: Callback X property-change handling.
icccm: Both client and window-manager helpers for ICCCM.
keysyms: Standard X key constants and conversion to/from keycodes.
event: Callback X event handling.
image: Port of Xlib's XImage and XShmImage functions.
wm: Framework for window manager implementation.

%package devel
Summary: Header files for XCB util libraries
Group: Development/C
Requires: %name = %version-%release
Provides: xcb-util-devel = %version-%release
Obsoletes: xcb-util-devel < %version-%release

%description devel
Header files for XCB util libraries.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/xcb
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.3.6-alt2
- rebuild

* Mon Aug 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.3.6-alt1
- 0.3.6

* Thu Jul 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4-alt1
- 1.4

* Fri May 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.5-alt1
- 0.3.5

* Fri Apr 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.4-alt1
- 0.3.4

* Fri Feb 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Tue Dec 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Fri Nov 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.1-alt2
- don't build libxcb-wm.so.0

* Fri Nov 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Wed Sep 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Thu Aug 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.1-alt2
- obsoletes xcb-util

* Thu Aug 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.1-alt1
- initial release

