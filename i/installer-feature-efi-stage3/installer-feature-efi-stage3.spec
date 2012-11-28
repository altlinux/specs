Name: installer-feature-efi-stage3
Version: 0.1
Release: alt2

Summary: configure efivars kernel module for autoload
License: public domain
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch

%description
%summary
(if the installation proceeded in EFI mode)

%prep

%post
[ -d /sys/firmware/efi ] && echo efivars >> /etc/modules ||:

%files

%changelog
* Wed Nov 28 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- autoload efivars only when it's been successfully loaded by installer

* Tue Nov 13 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (see also #27970)

