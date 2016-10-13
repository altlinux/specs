Name:     guest-account
Version:  1.0
Release:  alt1

Summary:  Guest session support in LightDM
License:  GPLv2+
Group:    System/Configuration/Other
URL: 	  http://altlinux.org/Guest_session
Packager: Andrey Cherepanov <cas@altlinux.org> 
BuildArch: noarch

Source:   %name

Requires: lightdm 

%post
%_sbindir/%name enable

%preun
%_sbindir/%name disable

%description
Script for enable and disable guest session support in LightDM
(supports both login in greeter and autologin). For each guest
session it creates temporary user and cleanup this user and its
home directory at logout.

This script initially wrote for Debian and borrowed from
https://gist.github.com/pixline/6981710 and adapt for ALT Linux.

%install
install -Dm755 %SOURCE0 %buildroot%_sbindir/%name

%files
%_sbindir/%name

%changelog
* Thu Oct 13 2016 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus

