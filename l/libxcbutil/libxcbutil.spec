Name: libxcbutil
Version: 0.4.1
Release: alt1
Epoch: 1
Summary: XCB util modules
License: MIT
Group: System/Libraries
URL: http://xcb.freedesktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Source1: m4.tar
Patch: %name-%version-%release.patch

BuildRequires: doxygen libxcb-devel xorg-xproto-devel xorg-util-macros

%description
The XCB util modules provides a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package devel
Summary: Header files for XCB util libraries
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files for XCB util libraries

%prep
%setup -q -a1
%patch -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc NEWS COPYING README.md
%_libdir/*.so.*

%files devel
%_includedir/xcb
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Tue Dec 20 2022 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.1-alt1
- 0.4.1

* Wed Oct 15 2014 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.0-alt1
- 0.4.0

* Wed Aug 29 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.3.9-alt1
- 0.3.9

* Mon May 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.3.8-alt1
- 0.3.8

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

