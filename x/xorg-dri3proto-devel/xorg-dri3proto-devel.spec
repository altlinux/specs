Name: xorg-dri3proto-devel
Version: 1.0
Release: alt1
Summary: DRI3 Protocol Headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: dri3proto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
DRI3 protocol specification and Xlib/Xserver headers

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%install
%make DESTDIR=%buildroot install

%files
%_datadir/doc/dri3proto
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Wed Jan 08 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt1
- initial release

