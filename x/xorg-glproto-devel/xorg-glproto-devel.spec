Name: xorg-glproto-devel
Version: 1.4.15
Release: alt1
Summary: X.org GLProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: glproto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xorg-util-macros

%description
X.org GLProto protocol headers

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%install
%make DESTDIR=%buildroot install

%files
%_includedir/GL
%_pkgconfigdir/*.pc

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.4.15-alt1
- 1.4.15

* Thu Jun 30 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.14-alt1
- 1.4.14

* Thu May 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.13-alt1
- 1.4.13

* Wed Aug 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.4.12-alt1
- 1.4.12

* Sat Jan 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.4.11-alt1
- 1.4.11

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4.10-alt1
- 1.4.10

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.9-alt1
- separate xorg-x11-proto-devel
