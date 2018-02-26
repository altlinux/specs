Name: livecd-isomd5sum
Version: 0.1
Release: alt1

Summary: Check whether live ISO isn't corrupt
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Mkimage/Profiles/m-p
Source: %name.init
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Requires: isomd5sum

%description
This package provides convenient checkisomd5 wrapper
for live images with implanted md5 to be self-checked.

%prep

%build

%install
install -pDm755 %SOURCE0 %buildroot%_initdir/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/%name

%changelog
* Fri Nov 11 2011 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

