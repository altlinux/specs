Name: xfsinfo
Version: 1.0.2
Release: alt2

Summary: X font server information utility
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libFS-devel libX11-devel xorg-proto-devel
BuildRequires: xorg-util-macros libXdmcp-devel libXau-devel

%description
Xfsinfo is a utility for displaying information about an X font server.
It is used to examine the capabilities of a server, the predefined values
for  various  parameters used in communicating between clients and
the server, and the font catalogues  and  alternate  servers  that  are
available.

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
* Mon Jun 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- fixed buildrequires

* Sat May 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

