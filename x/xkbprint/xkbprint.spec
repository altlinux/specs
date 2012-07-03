Name: xkbprint
Version: 1.0.3
Release: alt1

Summary: print an XKB keyboard description
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: libX11-devel libXau-devel libXdmcp-devel libxkbfile-devel
BuildRequires: pkg-config xorg-proto-devel xorg-util-macros

%description
The  xkbprint  comman  generates a printable or encapsulated PostScript
description of the XKB keyboard description specified by  source.   The
source  can be any compiled keymap (.xkm) file that includes a geometry
description or an X display specification.  If an output_file is speci-
fied,  xkbprint writes to it.  If no output file is specified, xkbprint
creates replaces the extension of the source  file  with  .ps  or  .eps
depending on the requested format.  If the source is a non-local X dis-
play (e.g.:0), xkbprint appends the appropriate prefix to  the  display
specification,  replacing  the colon with a dash.  For a local display,
xkprint uses server-n where n is the number of the display.

%prep
%setup

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
* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

