Name: xorg-rgb
Version: 1.0.4
Release: alt1
Summary: uncompile an rgb color-name database
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Obsoletes: rgb xorg-x11-rgb
Provides: rgb xorg-x11-rgb = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xorg-xproto-devel xorg-util-macros

%description
The  showrgb  program reads an rgb color-name database compiled for use
with the dbm database routines and converts it  back  to  source  form,
printing  the  result  to standard output.  The default database is the
one that X was built with, and may be overridden on the  command  line.

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
%_datadir/X11/rgb*
%_man1dir/*

%changelog
* Thu Oct 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Fri Jun 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Jun 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- renamed xorg-x11-rgb to xorg-rgb

* Fri May 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial release

