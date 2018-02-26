Name: xorg-xf86dgaproto-devel
Version: 2.1
Release: alt2
Serial: 1
Summary: X.org XF86DGAProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xf86dgaproto = %version-%release
Conflicts: xorg-x11-proto-devel <= 7.4.0-alt1

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xorg-util-macros

%description
X.org XF86DGAProto protocol headers

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%install
%make DESTDIR=%buildroot install

%files
%_includedir/X11
%_pkgconfigdir/*.pc

%changelog
* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1-alt2
- 2.1

* Sat Feb 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.3-alt2
- 2.0.3

* Mon Oct 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.1-alt1
- 2.1

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.0.3-alt1
- separate xorg-x11-proto-devel
