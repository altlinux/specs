Name: xorg-font-utils
Version: 1.2.0
Release: alt1
Serial: 1
Summary: Font utilities required for installing fonts
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: font-util xorg-x11-font-utils = %serial:%version-%release
Requires: bdftopcf mkfontdir mkfontscale xorg-font-encodings
Obsoletes: xorg-x11-font-utils

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xorg-util-macros

%description
Includes bdftruncate, and other font related utilities which are required when
installing font packages.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-mapdir=%_datadir/X11/fonts/util
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_pkgconfigdir/*.pc
%dir %_datadir/X11/fonts
%_datadir/X11/fonts/util
%_datadir/aclocal/*.m4
%_man1dir/*

%changelog
* Thu Oct 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Mon Oct 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.1-alt1
- 1.1.1

* Sat Oct 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Thu Jun 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt6
- renamed xorg-x11-font-utils to xorg-font-utils

* Tue Apr 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt5
- move encodings to a separate package (close #11328)

* Wed Nov 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt4
- updated encodings to 1.0.2

* Sat Oct 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt3
- updated encodings to 1.0.1

* Thu Jun 15 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt2
- return lost map-CP866
- added map-MICROSOFT-CP1251 (#9705)

* Tue May 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt1
- 1.0.1

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.2-alt1
- Xorg-7.0RC3

* Fri Nov 25 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.1-alt0.1
- initial release

