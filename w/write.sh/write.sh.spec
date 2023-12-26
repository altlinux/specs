Name: write.sh
Version: 0.3
Release: alt1

Summary: write Elbrus boot media
License: ALT-Public-Domain
Group: System/Configuration/Other

Url: http://altlinux.org/write.sh
Source: %name
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Requires: rsync
AutoReqProv: no

%description
This script can be used to create boot media suitable
for Elbrus CPU based computers on both optical and flash
drives (or, well, SSD/HDD) using an ISO9660 image.

ALT and OSL images have been written successfully.

%prep

%build

%install
install -pDm755 %SOURCE0 %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Tue Dec 26 2023 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- initial package (forked off mkimage-profiles 1.4.19-alt1-16-g6fd7ea58e)
