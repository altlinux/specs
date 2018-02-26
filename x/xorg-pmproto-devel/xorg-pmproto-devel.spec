Name: xorg-pmproto-devel
Version: 1.0.3
Release: alt1
Summary: X.org PMProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xproxymanagementprotocol = %version-%release pmproto = %version-%release xproxymngproto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
X.org PMProto protocol headers

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
* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- separate xorg-x11-proto-devel
