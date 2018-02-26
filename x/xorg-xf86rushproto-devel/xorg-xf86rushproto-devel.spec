Name: xorg-xf86rushproto-devel
Version: 1.1.2
Release: alt2
Summary: X.org XF86RushProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xf86rushproto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
X.org XF86RushProto protocol headers

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
* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt2
- updated build dependencies

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- separate xorg-x11-proto-devel
