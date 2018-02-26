Name: xlogo
Version: 1.0.4
Release: alt1

Summary: display the X Window System logo
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

# Automatically added by buildreq on Thu Apr 14 2011
# optimized out: fontconfig fontconfig-devel libICE-devel libSM-devel libX11-devel libXmu-devel libXrender-devel libXt-devel libfreetype-devel pkg-config xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: libXaw-devel libXext-devel libXft-devel

BuildRequires: xorg-util-macros

%description
The xlogo program displays the X Window System logo. That's all.

%prep
%setup

%build
%autoreconf
%configure --disable-xprint

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc README
%_bindir/*
%_man1dir/*
%_x11appconfdir/*

%changelog
* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Tue Apr 26 2011 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1.2
- Release bump for rebuild

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1.1
- Recalculate buildreq

* Wed Nov 03 2010 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Wed Sep 22 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Tue Dec 09 2008 Fr. Br. George <george@altlinux.ru> 1.0.1-alt2
- Sync with upstream up to aw7 downgrade patch

* Sun Feb 26 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- XOrg7 initial build

