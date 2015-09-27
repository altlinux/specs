%define soname 10
%define sover 1.0.1

Name: vmware-view-preinstall
Version: 3.4.0
Release: alt3

Summary: VMware Horizon Client pre-installation scripts
License: public domain
Group: System/Configuration/Other

Url: http://altlinux.org/vmware-view
BuildArch: noarch

Requires: libudev0
Requires: libcrypto%soname >= %sover
Requires: libssl%soname >= %sover

%description
Install this package if you plan to deploy
VMware-Horizon-Client-%version bundle on this system.

%files

%post
for i in libssl libcrypto; do
	ln -s $i.so.%soname /`getconf SLIB`/$i.so.%sover
done

%preun
for i in libssl libcrypto; do
	rm /`getconf SLIB`/$i.so.%sover
done

%changelog
* Fri Sep 25 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt3
- moved scripts to vmware-view-userinstall so this package
  is a pristine preinstall one

* Tue Sep 22 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt2
- made noarch with runtime getconf(1) instead of build-time %%_lib
- added desktop file and an icon beforehand

* Fri Sep 18 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt1
- initial release

