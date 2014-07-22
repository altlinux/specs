Name: apt-scripts-nvidia
Version: 0.2.0
Release: alt1

Summary: APT Lua script for NVIDIA driver
License: GPL
Group: System/Configuration/Packaging

Source: scripts-nvidia-%version.tar

BuildRequires: apt
BuildArch: noarch

%description
apt-get install-nvidia
	This script will install NVIDIA driver.

%prep
%setup -qn scripts-nvidia-%version

%build

%install
for f in *.lua; do install -pD -m755 $f %buildroot/usr/share/apt/scripts/$f; done
for f in *.conf; do install -pD -m644 $f %buildroot/etc/apt/apt.conf.d/$f; done

#cat *.conf >.apt.conf
#apt-get -c .apt.conf -o Dir::Bin::scripts=%buildroot/usr/share/apt/scripts install-nvidia
#apt-get -c .apt.conf script ./install-nvidia.lua

mkdir -p %buildroot/etc/buildreqs/files/ignore.d
ls *.conf |sed 's:^:^/etc/apt/apt.conf.d/:;s:[.]:[.]:g' >%buildroot/etc/buildreqs/files/ignore.d/%name

%files
/usr/share/apt
%config /etc/apt/apt.conf.d/*
%config /etc/buildreqs/files/ignore.d/%name

%changelog
* Tue Jul 22 2014 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt1
- install 32-bit drivers on x86_64

* Tue Feb 25 2014 Sergey V Turchin <zerg@altlinux.org> 0.1.2-alt1
- fix upgrade existing driver when duplicated kernels allowed

* Thu Feb 13 2014 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt1
- add reminding to apt-get update

* Wed Feb 12 2014 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial build
