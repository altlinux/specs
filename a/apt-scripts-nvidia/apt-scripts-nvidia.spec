Name: apt-scripts-nvidia
Version: 0.4.0
Release: alt1

Summary: APT Lua scripts for NVIDIA driver
License: GPL
Group: System/Configuration/Packaging

Source: scripts-nvidia-%version.tar

BuildRequires: apt

%description
apt-get install-nvidia
	This scripts will install NVIDIA driver.

%prep
%setup -qn scripts-nvidia-%version

%build

%install
for f in *.lua; do install -pD -m755 $f %buildroot/%_datadir/apt/scripts/$f; done
for f in *.conf; do install -pD -m644 $f %buildroot/etc/apt/apt.conf.d/$f; done
%ifnarch x86_64
# remove arepo helper
rm -f %buildroot/%_datadir/apt/scripts/nvidia-64bit-helper.*
rm -f %buildroot/etc/apt/apt.conf.d/nvidia-64bit-helper.*
%endif

#cat *.conf >.apt.conf
#apt-get -c .apt.conf -o Dir::Bin::scripts=%buildroot/%_datadir/apt/scripts install-nvidia
#apt-get -c .apt.conf script ./install-nvidia.lua

mkdir -p %buildroot/etc/buildreqs/files/ignore.d
ls *.conf |sed 's:^:^/etc/apt/apt.conf.d/:;s:[.]:[.]:g' >%buildroot/etc/buildreqs/files/ignore.d/%name

%files
%_datadir/apt/scripts/*
%config /etc/apt/apt.conf.d/*
%config /etc/buildreqs/files/ignore.d/%name

%changelog
* Fri Jan 29 2016 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- upgrade installed kernel module if possible

* Mon Sep 28 2015 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- install 64-bit helper script only on specific architecture

* Fri Sep 18 2015 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- install 32-bit packages with 64-bit nvidia_glx_* on x86_64

* Tue Jul 22 2014 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt1
- install 32-bit drivers on x86_64

* Tue Feb 25 2014 Sergey V Turchin <zerg@altlinux.org> 0.1.2-alt1
- fix upgrade existing driver when duplicated kernels allowed

* Thu Feb 13 2014 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt1
- add reminding to apt-get update

* Wed Feb 12 2014 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial build
