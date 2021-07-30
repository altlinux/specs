%add_findreq_skiplist /usr/share/make-initrd/features/*

Name: make-initrd-netboot
Version: 0.4.2
Release: alt1

Summary: Netboot feature for make-initrd
License: GPLv2+
Group: System/Base

Source0: %name-%version.tar

# For modern init script scheme
Requires: make-initrd >= 0.9.0

# Programs packed into initrd
Requires: coreutils curl dhcpcd >= 9.0.0 grep iproute2 sed tar zstd

BuildArch: noarch

%description
Make-initrd netboot feature to do special type of network boot:
1) Get ip address via DHCP (for all ethernet adapters)
2) Mount tmpfs as root filesystem (with <netboot_fs_size> size)
3) Download and untar <netboot_url>/common.tar.zst
4) Download and untar <netboot_url>/<IP_ADDRESS>.tar.zst

Ethernet module should be added to MODULES_PRELOAD.

%prep
%setup

%install
mkdir -p %buildroot/usr/share/make-initrd/features/
cp -a netboot %buildroot/usr/share/make-initrd/features/

%files 
%_datadir/make-initrd/features/netboot

%changelog
* Fri Jul 30 2021 Dmitry V. Levin <ldv@altlinux.org> 0.4.2-alt1
- Fixed handling of more than a single ntp server (by Gleb Fotengauer-Malinovskiy).

* Fri Dec 18 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.1-alt1
- Fixed dhcpcd >= 9.0.0 support (quote all lease variable values).

* Thu Dec 17 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4-alt1
- Added dependencies for programs used in initrd.
- Fixed work with and switched to dhcpcd >= 9.0.0.

* Wed Jul 08 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3-alt2
- Updated package %%description.

* Wed Jun 26 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3-alt1
- Ported to modern make-initrd scheme with modules made as init-scripts.

* Tue May 29 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1
- initial
