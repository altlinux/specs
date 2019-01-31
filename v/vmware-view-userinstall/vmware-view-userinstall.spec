%define soname 10
%define sover 1.0.1

Name: vmware-view-userinstall
Version: 4.10.0
Release: alt1

Summary: VMware Horizon Client pre-installation scripts
License: public domain
Group: System/Configuration/Other

Url: http://altlinux.org/vmware-view
Source: %name-%version.tar
ExclusiveArch: %ix86

Requires: vmware-view-preinstall >= 3.4.0-alt3
Requires: userinstall-helper >= 0.2

%define uinstdir %_cachedir/userinstall

%description
Install this package if you need a script to help install
VMware-Horizon-Client-%version bundle on this system.

%prep
%setup

%install
install -pDm644 vmware-view-client.desktop \
	%buildroot%_desktopdir/vmware-view-client.desktop
install -pDm644 vmware-view-client-vmware.png \
	%buildroot%_pixmapsdir/vmware-view-client-vmware.png
install -pDm755 vmware-view.sh %buildroot%_bindir/vmware-view

mkdir -p %buildroot%uinstdir
cp -a checksums %buildroot%uinstdir/goodsums

%files
# this one will clobber itself during real vmware-view deployment
# that shouldn't get clobbered again by this package upgrade
%config(noreplace) %_bindir/vmware-view
%_desktopdir/vmware-view-client.desktop
%_pixmapsdir/vmware-view-client-vmware.png
%uinstdir/goodsums/*

%changelog
* Thu Jan 31 2019 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt1
- support for VMware-Horizon-Client-4.10.0-11053294.x86.bundle

* Tue Apr 04 2017 Michael Shigorin <mike@altlinux.org> 3.4.0-alt4
- sync ExclusiveArch: to vmware-view-preinstall 3.4.0-alt4
  to avoid an unmet dependency

* Wed Oct 28 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt2
- rewrote to use userinstall-sh-functions too

* Fri Sep 25 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt1
- split off vmware-view-preinstall 3.4.0-alt2
- rewrote to rely upon userinstall-helper

