Name: installer-feature-efi-stage3
Version: 0.1
Release: alt1

Summary: configure efivars kernel module for autoload
License: public domain
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch

%description
%summary

%prep

%post
echo efivars >> /etc/modules

%files

%changelog
* Tue Nov 13 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (see also #27970)

