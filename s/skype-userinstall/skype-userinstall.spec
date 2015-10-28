Name: skype-userinstall
Version: 4.3.0.37
Release: alt3

Summary: Skype pre-installation scripts
License: public domain; CC-BY-ND (skype icon)
Group: System/Configuration/Other

Url: http://altlinux.org/skype
Source: %name-%version.tar
ExclusiveArch: %ix86

Requires: skype-preinstall >= 0.1-alt2
Requires: userinstall-helper >= 0.2

%define uinstdir %_cachedir/userinstall

%description
Install this package if you need a script to help install
Skype %version package for SUSE on this system.

%prep
%setup

%install
install -pDm644 skype.desktop %buildroot%_desktopdir/skype.desktop
install -pDm644 skype.png %buildroot%_pixmapsdir/skype.png
install -pDm755 skype.sh %buildroot%_bindir/skype

mkdir -p %buildroot%uinstdir
cp -a checksums %buildroot%uinstdir/goodsums

%files
# this one will clobber itself during real skype deployment
# that shouldn't get clobbered again by this package upgrade
%config(noreplace) %_bindir/skype
%config(noreplace) %_desktopdir/skype.desktop
%config(noreplace) %_pixmapsdir/skype.png
%uinstdir/goodsums/*

%changelog
* Fri Jan 15 2016 Michael Shigorin <mike@altlinux.org> 4.3.0.37-alt3
- thus not noarch anymore

* Fri Jan 15 2016 Michael Shigorin <mike@altlinux.org> 4.3.0.37-alt2
- x86-only (x86_64 gets arepo)

* Wed Oct 28 2015 Michael Shigorin <mike@altlinux.org> 4.3.0.37-alt1
- initial release based on vmware-view-userinstall 3.4.0-alt2

