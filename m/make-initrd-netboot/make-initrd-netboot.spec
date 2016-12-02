%add_findreq_skiplist /usr/share/make-initrd/features/*

Name: make-initrd-netboot
Version: 0.2
Release: alt1

Summary: Netboot feature for make-initrd
License: GPL
Group: System/Base

Source0: %name-%version.tar

# For new put-file utility
Requires: make-initrd >= 0.7.6-alt1

BuildArch: noarch

%description
Make-initrd netboot feature to do special type of network boot:
0) Udev loads kernel modules
1) Get ip address via DHCP (for all ethernet adapters)
2) Mount tmpfs as root filesystem (with netboot_fs_size size)
3) Download and untar root=<URL> (root=http://<addr>/rootfs.tar.gz)

%prep
%setup

%install
mkdir -p %buildroot/usr/share/make-initrd/features/
cp -a netboot %buildroot/usr/share/make-initrd/features/

%files 
%_datadir/make-initrd/features/netboot

%changelog
* Fri Dec 02 2016 Lenar Shakirov <snejok@altlinux.ru> 0.2-alt1
- Udev-ready, error catching

* Tue May 29 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1
- initial

