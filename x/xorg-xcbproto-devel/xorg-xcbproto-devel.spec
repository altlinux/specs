Name: xorg-xcbproto-devel
Version: 1.7.1
Release: alt1

Summary: XML-XCB protocol descriptions
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xcbproto = %version-%release xcb-proto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xml-utils xorg-util-macros

%description
XML-XCB protocol descriptions.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure
%make

%install
%make DESTDIR=%buildroot install

%files
%doc NEWS README TODO
%python_sitelibdir/xcbgen
%_datadir/xcb
%_datadir/pkgconfig/*.pc

%changelog
* Tue Mar 27 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Wed Jan 11 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.7-alt1
- 1.7

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt2.1
- Rebuild with Python-2.7

* Fri Aug 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.6-alt2
- git snapshot 2010-06-23 (e7aa34e6b3d846d0508ef08e74ea95d86da047d0)

* Fri Dec 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6-alt1
- 1.6

* Tue Dec 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5-alt2
- added DRI2 protocol

* Fri May 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5-alt1
- 1.5

* Tue Feb 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4-alt1
- 1.4

* Wed Dec 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3-alt1
- 1.3

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- separate xorg-x11-proto-devel
