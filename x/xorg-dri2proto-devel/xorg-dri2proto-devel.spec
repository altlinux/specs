Name: xorg-dri2proto-devel
Version: 2.6
Release: alt1
Summary: DRI2 Protocol Headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: dri2proto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xorg-util-macros

%description
DRI2 Protocol Headers

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%install
%make DESTDIR=%buildroot install

%files
%_datadir/doc/dri2proto
%_includedir/X11
%_pkgconfigdir/*.pc

%changelog
* Thu Jun 30 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.6-alt1
- 2.6

* Thu May 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.4-alt1
- 2.4

* Tue Feb 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.3-alt1
- 2.3

* Sat Jan 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.2-alt1
- 2.2

* Sat Jun 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.1-alt1
- 2.1

* Mon Apr 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt1
- 2.0

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.99.3-alt1
- 1.99.3

* Thu Oct 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.99.1-alt1
- 1.99.1

* Fri May 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- separate xorg-x11-proto-devel
