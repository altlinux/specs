%define xf86 XFree86

Name: xorg-bitmaps
Version: 1.1.0
Release: alt1
Serial: 1
Summary: Bitmaps that are shared between X applications
License: MIT/X11
Group: Development/Other
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Obsoletes: %xf86-bitmaps xorg-x11-bitmaps
Provides: xbitmaps %xf86-bitmaps = 4.4 xorg-x11-bitmaps = %serial:%version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
Bitmaps that are shared between X applications

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--build= \
	--host=

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_includedir/X11/bitmaps
%_datadir/pkgconfig/*.pc

%changelog
* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Thu Jun 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt3
- renamed xorg-x11-bitmaps to xorg-bitmaps

* Wed Jan 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt2
- moved pkgconfig files to %_datadir/pkgconfig

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.1-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

