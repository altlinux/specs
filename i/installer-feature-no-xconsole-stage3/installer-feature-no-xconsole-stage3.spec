Name: installer-feature-no-xconsole-stage3
Version: 0.1
Release: alt1

Summary: Disable xconsole in XDM by default
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Requires: xinitrc

%description
%summary

%prep
%files

%post
echo 'XCONSOLE=no' >> /etc/sysconfig/xinitrc

%changelog
* Tue Jun 19 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- installer-feature-no-xconsole simplified as a stage3 package
