Name: livecd-main-repo
Version: 0.1
Release: alt1

Summary: Try to configure main repo if available
License: GPLv2+
Group: System/Configuration/Other

Url: http://www.altlinux.org/apt-repo
Source0: %name

BuildArch: noarch

%description
It checks if the main package repository in /image is reachable and if
it is, adds it to APT's sources list.

%prep

%build

%install
install -pDm755 %SOURCE0 %buildroot%_sysconfdir/firsttime.d/%name

%files
%_sysconfdir/firsttime.d/%name

%changelog
* Sat Sep 24 2022 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- initial build
