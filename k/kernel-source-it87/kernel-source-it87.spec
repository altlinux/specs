# -*- rpm-spec -*-
%define module_name	it87
%define module_version  1.0
%define git 60d9def

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: alt3.g%{git}
Provides: kernel-source-%module_name-%module_version
Summary: IT86XXX/87XXX/Sis950 sensor kernel module driver
License: GPL-2.0-or-later
Group: Development/Kernel
Url: https://github.com/frankcrawford/it87
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%version.tar

Patch0: it87-alt-add-b550-aorus-elite-v2.patch
Patch1: alt-modname.patch

BuildPreReq: kernel-build-tools
BuildArch: noarch

%description
This driver implements support for the IT8603E, IT8620E, IT8622E, IT8623E,
IT8628E, IT8705F, IT8712F, IT8716F, IT8718F, IT8720F, IT8721F, IT8726F, IT8728F,
IT8732F, IT8758E, IT8771E, IT8772E, IT8781F, IT8782F, IT8783E/F, IT8786E,
IT8790E, and SiS950 chips.

These chips are 'Super I/O chips', supporting floppy disks, infrared ports,
joysticks and other miscellaneous stuff. For hardware monitoring, they
include an 'environment controller' with 3 temperature sensors, 3 fan
rotation speed sensors, 8 voltage sensors, associated alarms, and chassis
intrusion detection.

%package -n %module_name-blacklist
Summary: blacklist upstream kernel %module_name module
Group: System/Kernel and hardware

%description -n %module_name-blacklist
blacklist upstream kernel %module_name module

%package -n %module_name-sensors-conf
Summary: %module_name configurations to use with lm_sensors
Group: System/Kernel and hardware
Requires: lm_sensors3

%description -n %module_name-sensors-conf
%module_name configurations to use with lm_sensors

%prep
%setup -c -q
pushd kernel-source-%module_name-%module_version
%autopatch -p1
popd
pushd kernel-source-%module_name-%module_version/"Sensors configs"
ln -s GA-B550M-DS3H.conf GA-B550-AORUS-ELITE-V2.conf
popd

%install
mkdir -p %buildroot{%_sysconfdir/modprobe.d,%_datadir/lm_sensors3/configs/Gigabyte_%module_name}
pushd kernel-source-%module_name-%module_version
cp -ar "Sensors configs"/* %buildroot%_datadir/lm_sensors3/configs/Gigabyte_%module_name/
popd
echo 'blacklist %module_name' > %buildroot%_sysconfdir/modprobe.d/%module_name.conf
mkdir -p %kernel_srcdir
tar jcf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n %module_name-blacklist
%_sysconfdir/modprobe.d/%module_name.conf

%files -n %module_name-sensors-conf
%_datadir/lm_sensors3/configs/Gigabyte_%module_name

%changelog
* Fri Oct 24 2025 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt3.g60d9def
- GIT 60d9def.

* Sun Aug 10 2025 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt2.g4bff981
- Add B550 AORUS ELITE V2.
- Rename module to gb-i87 to coexists with existing in-kernel module.

* Fri Aug 08 2025 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt1.g4bff981
- Initial build for ALTLinux.
