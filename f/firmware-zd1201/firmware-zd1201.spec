%define module zd1201

Name: firmware-%module
Version: 0.14
Release: alt1

Summary: Firmware for ZD1201 WiFi chip
License: As is
Group: System/Kernel and hardware

%define distname %module-%version-fw

Url: http://linux-lc100020.sourceforge.net
Source: http://prdownloads.sourceforge.net/linux-lc100020/%distname.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

Provides: firmware-zd1201
BuildArch: noarch

%define firmwaredir /lib/firmware

%description
This package contains the firmware required by zd1201 driver.

%prep
%setup -n %distname

%install
install -d %buildroot%firmwaredir/
install -pm644 *.fw %buildroot%firmwaredir/

%files
%doc README
%firmwaredir/*.fw

%changelog
* Thu Jan 14 2010 Michael Shigorin <mike@altlinux.org> 0.14-alt1
- 0.14
- spec based on zd1201-firmware-0.14-3mdv2010.0
