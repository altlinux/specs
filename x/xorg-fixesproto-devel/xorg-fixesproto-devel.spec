Name: xorg-fixesproto-devel
Version: 5.0
Release: alt1
Epoch: 1
Summary: X Fixes extension protocol specification and header files
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: fixesproto = %version-%release
Conflicts: xorg-x11-proto-devel <= 7.4.0-alt1

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-xextproto-devel xorg-util-macros

%description
X Fixes extension protocol specification and header files

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--build= \
	--host=

%install
%make DESTDIR=%buildroot install

%files
%_docdir/fixesproto
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Mon Mar 14 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:5.0-alt1
- 5.0

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:4.1.2-alt1
- 4.1.2

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:4.1.1-alt2
- 4.1.1

* Sat Feb 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:4.0-alt2
- 4.0

* Tue Oct 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.1.1-alt1
- 4.1.1

* Fri May 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 4.0-alt1
- separate xorg-x11-proto-devel
