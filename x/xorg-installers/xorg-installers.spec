Name: xorg-installers
Version: 7.8
Release: alt8

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
%ifarch %e2k
Requires: xorg-drv-radeon
#Requires: xorg-drv-siliconmotion
%else
Requires: xorg-drv-ati xorg-drv-intel xorg-drv-cirrus xorg-drv-nouveau xorg-drv-qxl xorg-drv-amdgpu
%endif

%description -n xorg-drv-video
xorg-drv-video requires video drivers for X Window System for PCI, AGP
and PCI-E cards

%package -n xorg-drv-input
Summary: input drivers for X Window System
Group: System/X11
Requires: xorg-drv-evdev xorg-drv-synaptics

%description -n xorg-drv-input
xorg-drv-input requires all input drivers for X Window System

%files -n xorg-utils
%files -n xorg-apps
%files -n xorg-drv-video
%files -n xorg-drv-input

%changelog
* Thu May 31 2018 Valery Inozemtsev <shrek@altlinux.ru> 7.8-alt8
- xorg-drv-video: remove nv, openchrome

* Mon May 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 7.8-alt7
- remove xorg-proto-devel subpackage

* Thu May 03 2018 Michael Shigorin <mike@altlinux.org> 7.8-alt6
- support e2kv4 through %%e2k

* Mon Oct 23 2017 Mikhail Efremov <sem@altlinux.org> 7.8-alt5
- xorg-drv-video: Add amdgpu.

* Wed Jul 26 2017 Michael Shigorin <mike@altlinux.org> 7.8-alt4
- E2K: use only specific drivers in metapackage

* Mon Dec 12 2016 Valery Inozemtsev <shrek@altlinux.ru> 7.8-alt3
- removed very very old video drivers

* Wed Mar 13 2013 Mikhail Efremov <sem@altlinux.org> 7.8-alt2
- Added xorg-proto-devel subpackage.

* Tue Mar 12 2013 Mikhail Efremov <sem@altlinux.org> 7.8-alt1
- Initial build.

