Name: xorg-installers
Version: 7.8
Release: alt3
Summary: Set of various Xorg-related installers
License: MIT/X11
Group: System/X11

%description
A set of virtual packages for install various
Xorg packages.

%package -n xorg-utils
Summary: Utilities for the X Window System
Group: System/X11
Requires: xinit setxkbmap sessreg xf86dga xsetroot xcmsdb xconsole xmodmap xrdb
Requires: xdpyinfo xgamma xhost xrandr xrefresh xsetmode xstdcmap xvinfo
Requires: xkbevd xkbprint xlsfonts xprop xset

%description -n xorg-utils
Some useful utilities for the X Window System

%package -n xorg-apps
Summary: Graphical applications for Xorg
Group: System/X11
Requires: xmessage glxgears xfontsel xvidtune xkill xev

%description -n xorg-apps
Graphical applications for Xorg

%package -n xorg-drv-video
Summary: video drivers for X Window System
Group: System/X11
Requires: xorg-drv-ati xorg-drv-intel xorg-drv-nv xorg-drv-openchrome xorg-drv-cirrus
Requires: xorg-drv-nouveau xorg-drv-qxl

%description -n xorg-drv-video
xorg-drv-video requires video drivers for X Window System for PCI, AGP
and PCI-E cards

%package -n xorg-drv-input
Summary: input drivers for X Window System
Group: System/X11
Requires: xorg-drv-evdev xorg-drv-synaptics

%description -n xorg-drv-input
xorg-drv-input requires all input drivers for X Window System

%package -n xorg-proto-devel
Summary: X proto header files
Group: Development/C
Requires: xorg-bigreqsproto-devel xorg-compositeproto-devel xorg-damageproto-devel xorg-dmxproto-devel xorg-evieproto-devel
Requires: xorg-fixesproto-devel xorg-fontsproto-devel xorg-glproto-devel xorg-inputproto-devel xorg-kbproto-devel
Requires: xorg-pmproto-devel xorg-randrproto-devel xorg-recordproto-devel xorg-renderproto-devel xorg-resourceproto-devel
Requires: xorg-scrnsaverproto-devel xorg-videoproto-devel xorg-xcbproto-devel xorg-xcmiscproto-devel xorg-xextproto-devel
Requires: xorg-xf86bigfontproto-devel xorg-xf86dgaproto-devel xorg-xf86driproto-devel xorg-xf86rushproto-devel
Requires: xorg-xf86vidmodeproto-devel xorg-xineramaproto-devel xorg-xproto-devel

%description -n xorg-proto-devel
X proto header files

%files -n xorg-utils
%files -n xorg-apps
%files -n xorg-drv-video
%files -n xorg-drv-input
%files -n xorg-proto-devel

%changelog
* Mon Dec 12 2016 Valery Inozemtsev <shrek@altlinux.ru> 7.8-alt3
- removed very very old video drivers

* Wed Mar 13 2013 Mikhail Efremov <sem@altlinux.org> 7.8-alt2
- Added xorg-proto-devel subpackage.

* Tue Mar 12 2013 Mikhail Efremov <sem@altlinux.org> 7.8-alt1
- Initial build.

