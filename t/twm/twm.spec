Name: twm
Version: 1.0.10
Release: alt2
Epoch: 1
Summary: Tab Window Manager for the X Window System
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
Source3: system.twmrc
Source4: twm.png

BuildRequires: libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel
BuildRequires: libXdmcp-devel libXmu-devel libXt-devel pkg-config
BuildRequires: xorg-proto-devel xorg-util-macros flex

%description
Twm  is  a  window manager for the X Window System.  It provides title-
bars, shaped windows, several forms of  icon  management,  user-defined
macro  functions,  click-to-type and pointer-driven keyboard focus, and
user-specified key and pointer button bindings.

%prep
%setup

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

install -pD -m644 %SOURCE3 %buildroot%_sysconfdir/X11/%name/system.twmrc

install -pD -m644 %SOURCE4 %buildroot%_miconsdir/%name.png
mkdir -p %buildroot%_sysconfdir/X11/wmsession.d
cat > %buildroot%_sysconfdir/X11/wmsession.d/20twm << EOF
NAME=TWM
EXEC=%_bindir/%name
DESC=Tab Window Manager
ICON=%name
SCRIPT:
exec %_bindir/%name
EOF

mkdir -p %buildroot%_datadir/xsessions/
cat > %buildroot%_datadir/xsessions/%name.desktop << EOF
[Desktop Entry]
Name=TWM
Comment=Tab Window Manager
Icon=%name
TryExec=%_bindir/%name
Exec=%_bindir/%name
Type=Application
Terminal=false
EOF

%files
%dir %_sysconfdir/X11/%name
%config(noreplace) %_sysconfdir/X11/%name/system.twmrc
%_sysconfdir/X11/wmsession.d/20twm
%_datadir/xsessions/%name.desktop
%_miconsdir/%name.png
%_bindir/%name
%_man1dir/*
%_x11x11dir/twm/*

%changelog
* Tue Nov 16 2021 Igor Vlasenko <viy@altlinux.org> 1:1.0.10-alt2
- NMU: WM packaging policy 2.0:
- added pixmap
- added .desktop

* Wed Sep 19 2018 Fr. Br. George <george@altlinux.ru> 1:1.0.10-alt1
- Autobuild version bump to 1.0.10

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 1:1.0.9-alt1
- Autobuild version bump to 1.0.9

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 1:1.0.8-alt1
- Autobuild version bump to 1.0.8

* Thu Jul 28 2011 Fr. Br. George <george@altlinux.ru> 1:1.0.7-alt1
- Autobuild version bump to 1.0.7
- System-wide config file added

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1:1.0.6-alt1
- Autobuild version bump to 1.0.6

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1:1.0.4-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.4-alt1
- 1.0.4

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2-alt1
- 1.0.2

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.2-alt1
- Xorg-7.0RC3

* Mon Nov 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.1-alt0.1
- initial release

