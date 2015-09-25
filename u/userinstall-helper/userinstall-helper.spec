Name: userinstall-helper
Version: 0.1
Release: alt1

Summary: run anything as root from user
License: GPL
Group: System/Base

Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%define sudodir %_sysconfdir/sudoers.d
%define uinstdir %_cachedir/userinstall

%description
%summary
(provided that appropriate checksums
were installed by root)

NB: this package installs custom sudoers file
    that allows wheel group members to run it
    as root!

%prep
%setup

%install
install -pDm400 sudoers %buildroot%sudodir/userinstall
install -pDm755 userinstall-helper.sh %buildroot%_sbindir/%name
install -d %buildroot%uinstdir/goodsums
install -d %buildroot%uinstdir/files

%files
%_sbindir/%name
%attr(400,root,root) %sudodir/userinstall
%dir %uinstdir/goodsums
%dir %uinstdir/files

%changelog
* Fri Sep 25 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

