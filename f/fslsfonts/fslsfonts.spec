Name: fslsfonts
Version: 1.0.3
Release: alt1
Summary: list fonts served by X font server
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libFS-devel xorg-util-macros

%description
Fslsfonts  lists  the fonts that match the given pattern.  The wildcard
character "*" may be used to match any sequence of characters (including
none),  and  "?"  to match any single character.  If no pattern is
given, "*" is assumed.

The "*" and "?" characters must be quoted to prevent  them  from  being
expanded by the shell.

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
* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Mon Jun 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

