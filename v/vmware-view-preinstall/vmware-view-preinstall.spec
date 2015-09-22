%define soname 10
%define sover 1.0.1

Name: vmware-view-preinstall
Version: 3.4.0
Release: alt2

Summary: VMware Horizon Client pre-installation scripts
License: public domain
Group: System/Configuration/Other

Source0: vmware-view-client.desktop
Source1: vmware-view-client-vmware.png
Source2: vmware-view.sh
BuildArch: noarch

Requires: libudev0
Requires: libcrypto%soname >= %sover
Requires: libssl%soname >= %sover

Requires: zenity

%description
Install this package if you plan to deploy
VMware-Horizon-Client-%version bundle on this system.

%install
install -pDm644 %SOURCE0 %buildroot%_desktopdir/vmware-view-client.desktop
install -pDm644 %SOURCE1 %buildroot%_pixmapsdir/vmware-view-client-vmware.png
install -pDm755 %SOURCE2 %buildroot%_bindir/vmware-view

%files
%_desktopdir/vmware-view-client.desktop
%_pixmapsdir/vmware-view-client-vmware.png
%config(noreplace) %_bindir/vmware-view

%post
for i in libssl libcrypto; do
	ln -s $i.so.%soname /`getconf SLIB`/$i.so.%sover
done

%preun
for i in libssl libcrypto; do
	rm /`getconf SLIB`/$i.so.%sover
done

%changelog
* Tue Sep 22 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt2
- made noarch with runtime getconf(1) instead of build-time %%_lib
- added desktop file and an icon beforehand

* Fri Sep 18 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt1
- initial release

