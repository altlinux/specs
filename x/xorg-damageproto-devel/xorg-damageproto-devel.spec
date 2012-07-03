Name: xorg-damageproto-devel
Version: 1.2.1
Release: alt1

Summary: Damage extension protocol specification and header files
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: damageproto = %version-%release
Conflicts: xorg-x11-proto-devel <= 7.4.0-alt1

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
Damage extension protocol specification and header files.

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
%_docdir/damageproto
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Thu Aug 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Fri May 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- separate xorg-x11-proto-devel
