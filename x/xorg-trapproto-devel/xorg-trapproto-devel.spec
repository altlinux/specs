Name: xorg-trapproto-devel
Version: 3.4.3
Release: alt2
Summary: X.org TrapProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: trapproto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: libXt-devel xorg-util-macros

%description
X.org TrapProto protocol headers.

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
* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.4.3-alt2
- updated build dependencies

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 3.4.3-alt1
- separate xorg-x11-proto-devel
