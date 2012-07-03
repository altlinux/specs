Name: installer-feature-autologin-stage3
Version: 0.1
Release: alt1

Summary: Configure autologin package
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Requires: autologin
Requires: installer-common-stage3
Requires: installer-feature-runlevel5-stage3

%description
%summary

%prep
%install
mkdir -p %buildroot

%post
cat << E_O_F >> /etc/sysconfig/autologin
USER=altlinux
AUTOLOGIN=yes
E_O_F

%files

%changelog
* Tue Oct 13 2009 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial package
- extraced mkimage-profiles-desktop hook for reuse
  (only autologin part, kdm-related should be apart
  and should probably require corresponding packages)
