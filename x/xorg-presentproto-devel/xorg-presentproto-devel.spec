Name: xorg-presentproto-devel
Version: 1.0
Release: alt1
Summary: Present Protocol Headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: presentproto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
Present protocol specification and Xlib/Xserver headers

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%install
%make DESTDIR=%buildroot install

%files
%_datadir/doc/presentproto
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Wed Jan 08 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt1
- initial release

