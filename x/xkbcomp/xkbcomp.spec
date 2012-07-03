Name: xkbcomp
Version: 1.2.4
Release: alt1
Summary: compile XKB keyboard description
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libxkbfile-devel xorg-util-macros

%description
The  xkbcomp  keymap  compiler  converts a description of an XKB keymap
into one of several output formats.   The most common use  for  xkbcomp
is  to create a compiled keymap file (.xkm extension) which can be read
directly by XKB-capable X servers or utilities.   The  keymap  compiler
can  also  produce  C  header  files or XKB source files.  The C header
files produced by xkbcomp can be included by  X  servers  or  utilities
that  need a built-in default keymap.  The XKB source files produced by
xkbcomp are fully resolved and can be used to  verify  that  the  files
which typically make up an XKB keymap are merged correctly or to create
a single file which contains a complete description of the keymap.

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
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Tue Jun 21 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Tue Apr 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat Oct 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Thu Jul 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sat May 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Mon Oct 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt2
- GIT snapshot 2007-09-23 (6aae208fe5bd8f71757c294a441d7c599a1ec4a1)

* Wed Nov 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Wed Nov 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

