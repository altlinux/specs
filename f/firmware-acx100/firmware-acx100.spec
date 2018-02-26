
%define firmware_name acx100

Name: firmware-%firmware_name
Version: 1.2.1.34
Release: alt1
License: distributable
Group: System/Kernel and hardware
Summary: Firmware for the acx driver
Source0: %firmware_name-fw-%version.tar.gz
Url: http://%firmware_name.sourceforge.net/
Packager: Sergey Alembekov <rt@altlinux.ru>
BuildArch: noarch
Provides: firmware-%firmware_name = %version
Provides: firmware-%firmware_name-1.2.1.34 = %version
Obsoletes: firmware-%firmware_name-1.2.1.34

%description
This package contains the firmware for the acx driver.
It supports (well, most) WLAN cards that use the TNETW1130 (aka ACX111) 802.11g+/b+ chipset or the TNETW1100 (aka ACX100) 802.11b+ chipset.

%prep
%setup -q -c

%__tar -zxvf %SOURCE0

%install
install -d $RPM_BUILD_ROOT/lib/firmware

install -p */* $RPM_BUILD_ROOT/lib/firmware

%files
%defattr(644,root,root,755)
/lib/firmware/*

%changelog
* Mon Aug 27 2007 Sergey Alembekov <rt@altlinux.ru> 1.2.1.34-alt1
 -initial release

