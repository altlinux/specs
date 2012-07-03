Name: xorg-sgml-doctools
Version: 1.10
Release: alt1
Summary: Xorg sgml doc tools
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
Xorg xorg-sgml-doctools documentation

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--build= \
	--host=

%make

%install
%make DESTDIR=%buildroot install

%files
%_datadir/pkgconfig/*.pc
%_datadir/sgml/X11

%changelog
* Wed Mar 07 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.10-alt1
- 1.10

* Thu Jun 23 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.8-alt1
- 1.8

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.5-alt1
- 1.5

* Sun Sep 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- 1.2

* Wed Nov 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

