Name: xorg-proto-devel
Version: 2018.4
Release: alt1
Summary: X.Org combined protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xorg-bigreqsproto-devel xorg-dri3proto-devel xorg-inputproto-devel xorg-randrproto-devel xorg-videoproto-devel xorg-xf86driproto-devel
Provides: xorg-evieproto-devel xorg-kbproto-devel xorg-recordproto-devel xorg-xcbproto-devel
Provides: xorg-compositeproto-devel xorg-fixesproto-devel xorg-pmproto-devel xorg-renderproto-devel xorg-xcmiscproto-devel xorg-xf86rushproto-devel
Provides: xorg-damageproto-devel xorg-presentproto-devel xorg-resourceproto-devel xorg-xextproto-devel xorg-xf86vidmodeproto-devel
Provides: xorg-dmxproto-devel xorg-fontsproto-devel xorg-scrnsaverproto-devel xorg-xf86bigfontproto-devel xorg-xineramaproto-devel
Provides: xorg-dri2proto-devel xorg-glproto-devel xorg-xf86dgaproto-devel xorg-xproto-devel

Obsoletes: xorg-bigreqsproto-devel xorg-dri3proto-devel xorg-inputproto-devel xorg-randrproto-devel xorg-videoproto-devel xorg-xf86driproto-devel
Obsoletes: xorg-evieproto-devel xorg-kbproto-devel xorg-recordproto-devel xorg-xcbproto-devel
Obsoletes: xorg-compositeproto-devel xorg-fixesproto-devel xorg-pmproto-devel xorg-renderproto-devel xorg-xcmiscproto-devel xorg-xf86rushproto-devel
Obsoletes: xorg-damageproto-devel xorg-presentproto-devel xorg-resourceproto-devel xorg-xextproto-devel xorg-xf86vidmodeproto-devel
Obsoletes: xorg-dmxproto-devel xorg-fontsproto-devel xorg-printproto-devel xorg-scrnsaverproto-devel xorg-xf86bigfontproto-devel xorg-xineramaproto-devel
Obsoletes: xorg-dri2proto-devel xorg-glproto-devel xorg-xf86dgaproto-devel xorg-xproto-devel

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: fop xmlto xsltproc xorg-sgml-doctools xorg-util-macros

%description
X.Org combined protocol headers

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
%_docdir/xorgproto
%_includedir/*
%_datadir/pkgconfig/*.pc

%changelog
* Mon May 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 2018.4-alt1
- initial build

