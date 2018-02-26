Name: xsetmode
Version: 1.0.0
Release: alt1.1

Summary: set the mode for an X Input device
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2


BuildRequires: libX11-devel libXau-devel libXdmcp-devel libXext-devel
BuildRequires: libXi-devel pkg-config xorg-proto-devel xorg-util-macros

%description
Xsetmode  sets the mode of an XInput device to either absolute or rela-
tive.  This isn't appropriate for all device types.

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
* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

