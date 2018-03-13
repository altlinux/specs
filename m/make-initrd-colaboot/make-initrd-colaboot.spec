%add_findreq_skiplist /usr/share/make-initrd/features/*

Name: make-initrd-colaboot
Version: 0.5
Release: alt1

Summary: CoLaBoot feature for make-initrd
License: GPL
Group: System/Base
Packager: Michael A. Kangin <prividen@altlinux.org>

Source0: %name-%version.tar

Requires: make-initrd >= 0.7.6-alt1
Requires: dhcpcd curl

BuildArch: noarch

%description
Make-initrd CoLaBoot (Compressed Layers Boot) feature allow to boot host
with a separate compressed (squashfs) layers, mounted as overlayfs.
Layers can be aquired from network (HTTP(S)/FTP/TFTP/... (see curl(1)),
or from local filesystem (ISO/HDD).
Boot kernel modules may be added to initrd or provided as a separate
initramfs image.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/make-initrd/features/
mkdir -p %buildroot%_sysconfdir/initrd.mk.d/
cp -a colaboot %buildroot%_datadir/make-initrd/features/
cp colaboot.mk.example %buildroot%_sysconfdir/initrd.mk.d/

%files 
%_datadir/make-initrd/features/colaboot
%config(noreplace) %_sysconfdir/initrd.mk.d/colaboot.mk.example
%doc docs/*

%changelog
* Tue Mar 13 2018 Michael A. Kangin <prividen@altlinux.org> 0.5-alt1
- Initial build

