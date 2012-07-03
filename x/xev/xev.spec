Name: xev
Version: 1.2.0
Release: alt1
Summary: print contents of X events
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXrandr-devel xorg-util-macros

%description
Xev creates a window and then asks the X server to send it events when-
ever  anything  happens to the window (such as it being moved, resized,
typed in, clicked in, etc.).  You can also attach  it  to  an  existing
window.   It  is  useful  for seeing what causes events to occur and to
display the information that they contain; it is essentially  a  debug-
ging and development tool, and should not be needed in normal usage.

%prep
%setup -q

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
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sat Mar 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Fri Jun 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Fri Jan 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

