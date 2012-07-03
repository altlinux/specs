Name: xsetpointer
Version: 1.0.1
Release: alt1.1

Summary: set an X Input device as the main pointer
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2


BuildRequires: libX11-devel libXau-devel libXdmcp-devel libXext-devel libXi-devel
BuildRequires: pkg-config xorg-proto-devel xorg-util-macros

%description
Xsetpointer  sets  an  XInput  device as the main pointer.  When called
with the -l flag it lists the available devices.

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
* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Thu Sep 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

