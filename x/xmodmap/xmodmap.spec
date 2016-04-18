Name: xmodmap
Version: 1.0.9
Release: alt1
Summary: utility for modifying keymaps and pointer button mappings in X
License: MIT/X11
Group: System/X11
Url: https://cgit.freedesktop.org/xorg/app/xmodmap/

Source: %name-%version.tar.gz
Patch: xmodmap-1.0.6-alt1.1.patch

BuildRequires: libX11-devel xorg-util-macros

%description
The xmodmap program is used to edit and display the  keyboard  modifier
map  and  keymap  table that are used by client applications to convert
event keycodes into keysyms.  It is usually run from the user's session
startup  script to configure the keyboard according to personal tastes.

%prep
%setup
%patch -p1

%build
%add_optflags
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Mon Apr 18 2016 Fr. Br. George <george@altlinux.ru> 1.0.9-alt1
- Autobuild version bump to 1.0.9

* Mon Jul 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.1
- Fixed build

* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Fri Sep 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Tue Oct 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Fri Aug 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sun Jan 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- added MDK pointer patch

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

