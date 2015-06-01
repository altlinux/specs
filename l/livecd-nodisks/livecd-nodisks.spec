Name: livecd-nodisks
Version: 0.1
Release: alt1

Summary: drop local drive block device nodes on boot
License: public domain
Group: System/Configuration/Other

Url: http://en.altlinux.org/regular
Source0: %name.init
Source1: %name.service

BuildArch: noarch
Requires(post): chkconfig
Requires(preun): chkconfig

%description
%summary
(so that no data on preinstalled disks is harmed;
another flash drive or so could be added though)

%install
install -pDm755 %SOURCE0 %buildroot%_initdir/%name
install -pDm644 %SOURCE1 %buildroot%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/%name
%_unitdir/%name.service

%changelog
* Mon Oct 27 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

