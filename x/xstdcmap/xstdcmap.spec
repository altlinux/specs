Name: xstdcmap
Version: 1.0.2
Release: alt1

Summary: X standard colormap utility
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: libICE-devel libSM-devel libX11-devel libXau-devel
BuildRequires: libXdmcp-devel libXext-devel libXmu-devel libXt-devel
BuildRequires: pkg-config xorg-proto-devel xorg-util-macros

%description
The xstdcmap utility can be used to selectively  define  standard  col-
ormap  properties.   It  is  intended to be run from a user's X startup
script to create standard colormap definitions in order  to  facilitate
sharing  of scarce colormap resources among clients.  Where at all pos-
sible, colormaps are created with read-only allocations.

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
* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

