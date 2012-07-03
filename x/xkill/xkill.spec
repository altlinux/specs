Name: xkill
Version: 1.0.3
Release: alt1

Summary: kill a client by its X resource
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
Source1: %name.desktop
Source2: %name-icons.tar.bz2

BuildRequires: libX11-devel libXau-devel libXdmcp-devel libXmu-devel pkg-config
BuildRequires: xorg-proto-devel xorg-util-macros

%description
Xkill is a utility for forcing the X server  to  close  connections  to
clients.   This  program  is very dangerous, but is useful for aborting
programs that have displayed undesired windows on a user's screen.   If
no  resource identifier is given with -id, xkill will display a special
cursor as a prompt for the user to select a window to be killed.  If  a
pointer button is pressed over a non-root window, the server will close
its connection to the client that created the window.

%prep
%setup

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%__install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
%__mkdir_p %buildroot%_iconsdir
%__tar -xjf %SOURCE2 -C %buildroot%_iconsdir/

%files
%_bindir/*
%_desktopdir/%name.desktop
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_miconsdir/%name.xpm
%_man1dir/*

%changelog
* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt2.1
- Automatic buildreqfix
- Autobuild watchfile added

* Tue Mar 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- fixed %%_iconsdir

* Sun Jan 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

