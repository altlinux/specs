Name: livecd-online-repo
Version: 0.1
Release: alt1

Summary: Try to configure online repo if available
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/apt-repo
Source0: %name.init
Source1: %name.sysconfig
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
This package might be useful for distribution images or virtual machines
whose job is building packages with hasher and/or images with mkimage.

It checks if the online package repository is reachable and if it is,
adds it to APT's sources list.

%prep

%build

%install
install -pDm755 %SOURCE0 %buildroot%_initdir/%name
install -pDm644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/%name
%_sysconfdir/sysconfig/%name

%changelog
* Wed Nov 02 2011 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

