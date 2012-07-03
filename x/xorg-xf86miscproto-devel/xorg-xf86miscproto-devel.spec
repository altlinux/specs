Name: xorg-xf86miscproto-devel
Version: 0.9.3
Release: alt1
Summary: X.org XF86MiscProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xf86miscproto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
X.org XF86MiscProto protocol headers

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
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9.2-alt1
- separate xorg-x11-proto-devel
