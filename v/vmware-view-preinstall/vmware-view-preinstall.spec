%define soname 10
%define sover 1.0.1

Name: vmware-view-preinstall
Version: 3.4.0
Release: alt4

Summary: VMware Horizon Client pre-installation scripts
License: public domain
Group: System/Configuration/Other

Url: http://altlinux.org/vmware-view
ExclusiveArch: %ix86

BuildRequires: libXScrnSaver
Requires: libudev0
Requires: libcrypto%soname >= %sover
Requires: libssl%soname >= %sover

%description
Install this package if you plan to deploy
VMware-Horizon-Client-%version bundle on this system.

%install
mkdir -p %buildroot%_libdir/%name
ln -s /usr/lib/libXss.so.1 %buildroot%_libdir/%name/

%files
%_libdir/%name

%post
for i in libssl libcrypto; do
	ln -s $i.so.%soname /`getconf SLIB`/$i.so.%sover
done

%preun
for i in libssl libcrypto; do
	rm /`getconf SLIB`/$i.so.%sover
done

%changelog
* Tue Apr 04 2017 Michael Shigorin <mike@altlinux.org> 3.4.0-alt4
- made "64-bit" package "require" i586-libXScrnSaver
  like skype-preinstall (closes: #33325);
  thanks cas@ for the hint

* Fri Sep 25 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt3
- moved scripts to vmware-view-userinstall so this package
  is a pristine preinstall one

* Tue Sep 22 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt2
- made noarch with runtime getconf(1) instead of build-time %%_lib
- added desktop file and an icon beforehand

* Fri Sep 18 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt1
- initial release

