Name: xorg-xproto-devel
Version: 7.0.23
Release: alt1
Summary: X proto header files
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xproto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xmlto xorg-sgml-doctools xorg-util-macros

%description
X proto header files

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--host= \
	--build=

%install
%make DESTDIR=%buildroot install

%files
%dir %_docdir/xproto
%_docdir/xproto/*.html
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Fri Mar 16 2012 Valery Inozemtsev <shrek@altlinux.ru> 7.0.23-alt1
- 7.0.23

* Thu Jun 23 2011 Valery Inozemtsev <shrek@altlinux.ru> 7.0.22-alt1
- 7.0.22

* Sun Apr 17 2011 Valery Inozemtsev <shrek@altlinux.ru> 7.0.21-alt1
- 7.0.21

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 7.0.20-alt1
- 7.0.20

* Wed Nov 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 7.0.19-alt1
- 7.0.19

* Wed Aug 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 7.0.18-alt1
- 7.0.18

* Sat May 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 7.0.17-alt1
- 7.0.17

* Thu Sep 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 7.0.16-alt1
- 7.0.16

* Mon Mar 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 7.0.15-alt1
- 7.0.15

* Fri Oct 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 7.0.14-alt1
- 7.0.14

* Tue Jul 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 7.0.13-alt2
- added dead_perispomeni to keysymdef.h
- fixed typo in dead_dasia

* Fri May 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 7.0.13-alt1
- separate xorg-x11-proto-devel

