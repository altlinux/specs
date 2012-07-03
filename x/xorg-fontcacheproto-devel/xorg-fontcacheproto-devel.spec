Name: xorg-fontcacheproto-devel
Version: 0.1.3
Release: alt1

Summary: X.org FontcacheProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: fontcacheproto = %version-%release
Conflicts: xorg-x11-proto-devel <= 7.4.0-alt1

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xorg-util-macros

%description
X.org FontcacheProto protocol headers

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
* Sat Oct 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Fri May 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.1.2-alt1
- separate xorg-x11-proto-devel
