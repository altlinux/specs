Name: vivaldi-preinstall
Version: 0.1
Release: alt1

Summary: Set correct environment for Vivaldi
License: GPL
Group: Networking/WWW

Url: https://vivaldi.com/
Packager: Nazarov Denis <nenderus@altlinux.org>
BuildArch: noarch

Source0: vivaldi

%description
Set correct environment for Vivaldi

%install
%__install -Dp -m0644 %SOURCE0 %buildroot%_sysconfdir/default/vivaldi

%files
%_sysconfdir/default/vivaldi

%changelog
* Sat Apr 16 2016 Nazarov Denis <nenderus@altlinux.org> 0.1-alt1
- Initial release for ALT Linux

