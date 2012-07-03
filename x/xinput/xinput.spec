Name: xinput
Version: 1.5.3
Release: alt1
Summary: utility to configure and test XInput devices
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXext-devel libXi-devel xorg-util-macros

%description
xinput - utility to configure and test XInput devices

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Thu Nov 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.5.3-alt1
- 1.5.3

* Fri Jun 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Mon Mar 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Tue Oct 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Tue Oct 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4.99.3-alt1
- 1.4.99.3

* Thu May 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Thu Dec 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- initial release
