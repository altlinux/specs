%define bumblebeed_group xgrp
%define pm_metod bbswitch

Name: bumblebee
Version: 3.2.1
Release: alt7

Summary: Bumblebee - support for NVidia Optimus laptops on Linux
Group: System/Kernel and hardware
License: GPLv3
Url: http://bumblebee-project.org

Source: http://bumblebee-project.org/%name-%version.tar.gz
Source1: bumblebeed.in

# Configure the name of the Bumbleblee server group
Patch1: %name-3.1-alt-CONF_GID.patch
# https://github.com/Bumblebee-Project/Bumblebee/issues/699
Patch2: nvidia_modeset-detection_bug699_01.patch
Patch3: nvidia_modeset-detection_bug699_02.patch
Patch4: nvidia_umv_detection_bug699.patch
# https://github.com/Bumblebee-Project/Bumblebee/issues/573
Patch5: hexadicimal_bug573.patch
Patch6: nvidia_modeset-detection_bug699_03.patch
Patch7: alt-disable-xdrvswitch.patch

Requires: NVIDIA_GLX VirtualGL
# see ALT #29213
# Requires: bbswitch

BuildRequires: help2man libX11-devel glib2-devel
BuildRequires: libbsd-devel >= 0.2.0

%description
Bumblebee daemon is a rewrite of the original Bumblebee service,
providing an elegant and stable means of managing Optimus hybrid
graphics chipsets. A primary goal of this project is to not only enable
use of the discrete GPU for rendering, but also to enable smart power
management of the dGPU when it's not in use.

To enable power management functionality you need to install
kernel-modules-bbswitch package for your running kernel.


%prep
%setup
%patch1 -b .gid
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

cp %SOURCE1 scripts/sysvinit/

%build
%autoreconf
%configure CONF_GID=%bumblebeed_group \
	CONF_DRIVER=nvidia \
	CONF_DRIVER_MODULE_NVIDIA=nvidia \
	CONF_LDPATH_NVIDIA=%_x11sysconfdir/lib_nvidia/current \
	CONF_MODPATH_NVIDIA=%_x11sysconfdir/%{_lib}_nvidia/current,%_x11modulesdir \
	CONF_PM_METHOD=%pm_metod

%make_build

%install
%makeinstall_std

install -pD -m644 scripts/systemd/bumblebeed.service %buildroot/%systemd_unitdir/bumblebeed.service
install -pD -m755 scripts/sysvinit/bumblebeed %buildroot/%_initdir/bumblebeed

%pre
groupadd -r -f %bumblebeed_group

%post
%post_service bumblebeed

%preun
%preun_service bumblebeed

%files
%_sbindir/bumblebeed
%_bindir/optirun
%exclude %_bindir/%name-bugreport
/lib/udev/rules.d/99-bumblebee-nvidia-dev.rules
%_sysconfdir/bash_completion.d/%name
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/%name.conf
%config %_sysconfdir/%name/xorg.conf.nouveau
%config %_sysconfdir/%name/xorg.conf.nvidia
%dir %_sysconfdir/%name/xorg.conf.d
%config %_sysconfdir/%name/xorg.conf.d/10-dummy.conf
%config %systemd_unitdir/bumblebeed.service
%config %_initdir/bumblebeed
%_man1dir/bumblebeed.1*
%_man1dir/optirun.1*
%doc README.markdown doc/RELEASE_NOTES*

%exclude %_docdir/bumblebee

%changelog
* Wed Nov 29 2017 Sergey V Turchin <zerg@altlinux.org> 3.2.1-alt7
- disable OpenGL libs switching

* Wed Nov 29 2017 Sergey V Turchin <zerg@altlinux.org> 3.2.1-alt6
- fix nvidia module path on 32-bit systems

* Wed Nov 29 2017 Sergey V Turchin <zerg@altlinux.org> 3.2.1-alt4.M80P.1
- build for M80P

* Wed Nov 29 2017 Sergey V Turchin <zerg@altlinux.org> 3.2.1-alt5
- fix nvidia module path on 32-bit systems

* Tue Nov 28 2017 Sergey V Turchin <zerg@altlinux.org> 3.2.1-alt3.M80P.1
- build for M80P

* Tue Nov 28 2017 Sergey V Turchin <zerg@altlinux.org> 3.2.1-alt4
- fix unload nvidia_drm
- fix nvidia libs path
- fix nvidia module path

* Tue Apr 05 2016 Mikhail Efremov <sem@altlinux.org> 3.2.1-alt3
- Add patches from upstream's bug tracker (closes: #31863).

* Tue Jul 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt2
- removed forbidden dep on bbswitch (ALT #29213)

* Fri Jul 05 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Tue Feb 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.1-alt1
- 3.1 (ALT #28605)
- removed "noreplace" tag for bumblebee.conf

* Tue Jan 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt2
- enabled power management via bbswitch kernel module

* Mon Jan 23 2012 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- first test build for Sisyphus
- set bumblebeed group to xgrp
- set nvidia driver by default
- TODO: power management via bbswitch

