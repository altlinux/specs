#global __find_debuginfo_files %nil
%global optflags_lto %nil
%define _unpackaged_files_terminate_build 1
%define rname qemu
%define _group vmusers
%define _libexecdir /usr/libexec
%define _localstatedir /var
%global firmwaredirs "%_datadir/qemu:%_datadir/seabios:%_datadir/seavgabios:%_datadir/ipxe:%_datadir/ipxe.efi"

Name: pve-%rname
Version: 7.2.0
Release: alt1
Epoch: 1
Summary: QEMU CPU Emulator
License: BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group: Emulators
URL: http://www.nongnu.org/qemu/

Source0: %name-%version.tar
Source99: debian.tar
Source100: keycodemapdb.tar
Source101: berkeley-testfloat-3.tar
Source102: berkeley-softfloat-3.tar
# qemu-kvm back compat wrapper
Source5: qemu-kvm.sh
# /etc/qemu/bridge.conf
Source12: bridge.conf

%set_verify_elf_method fhs=relaxed
%add_verify_elf_skiplist %_datadir/%rname/*
%add_findreq_skiplist %_datadir/%rname/*
%add_findreq_skiplist %_datadir/pve-edk2-firmware/*

ExclusiveArch: x86_64 aarch64

Requires: %name-system = %EVR %name-img = %EVR
Conflicts: %rname
Provides: pve-qemu-kvm = %EVR

BuildRequires: acpica bzlib-devel glib2-devel flex libacl-devel libaio-devel libalsa-devel libattr-devel libcap-devel
BuildRequires: libcap-ng-devel libcurl-devel libfdt-devel libgnutls-devel libiscsi-devel libjpeg-devel
BuildRequires: liblzo2-devel libncurses-devel libnettle-devel libnuma-devel libpci-devel libpixman-devel libpng-devel ceph-devel
BuildRequires: libsasl2-devel libseccomp-devel libspice-server-devel libusbredir-devel libxfs-devel libepoxy-devel libgbm-devel
BuildRequires: makeinfo perl-Pod-Usage pkgconfig(glusterfs-api) pkgconfig(virglrenderer) liburing-devel libuuid-devel
BuildRequires: libslirp-devel >= 4.7.0
BuildRequires: libsystemd-devel libtasn1-devel libpmem-devel libzstd-devel zlib-devel spice-protocol
BuildRequires: ipxe-roms-qemu seavgabios seabios edk2-ovmf edk2-aarch64 qboot
#BuildRequires: librdmacm-devel libibverbs-devel libibumad-devel
BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme ninja-build meson
BuildRequires: libproxmox-backup-qemu-devel >= 1.3.0

%description
QEMU is a fast processor emulator using dynamic translation to achieve
good emulation speed.  QEMU has two operating modes:

* Full system emulation.  In this mode, QEMU emulates a full system
  (for example a PC), including a processor and various peripherials.
  It can be used to launch different Operating Systems without rebooting
  the PC or to debug system code.

* User mode emulation.  In this mode, QEMU can launch Linux processes
  compiled for one CPU on another CPU.  It can be used to launch the
  Wine Windows API emulator or to ease cross-compilation and
  cross-debugging.

As QEMU requires no host kernel patches to run, it is very safe and easy
to use.

%package common
Summary: QEMU CPU Emulator - common files
Group: Emulators
Requires(pre): control >= 0.7.2
Requires(pre): shadow-utils sysvinit-utils
Requires: seavgabios seabios edk2-ovmf edk2-aarch64 qboot
Requires: ipxe-roms-qemu >= 1.0.0-alt4.git93acb5d
Requires: %name-img = %EVR
Conflicts: %rname-common
Obsoletes: %name-aux < %EVR

%description common
QEMU is a fast processor emulator using dynamic translation to achieve
good emulation speed.
This package contains common files for qemu.

%package system
Summary: QEMU CPU Emulator - full system emulation
Group: Emulators
Requires: %name-common = %EVR pve-backup-client pve-backup-file-restore numactl
Conflicts: %rname-system %rname-ivshmem-tools %rname-tools %rname-kvm-core %rname-pr-helper

%description system
Full system emulation.  In this mode, QEMU emulates a full system
(for example a PC), including a processor and various peripherials.
It can be used to launch different Operating Systems without rebooting
the PC or to debug system code.

%package img
Summary: QEMU command line tool for manipulating disk images
Group: Emulators
Conflicts: %rname-img

%description img
This package provides a command line tool for manipulating disk images

%prep
%setup
mkdir debian
tar -xf %SOURCE99 -C debian --strip-components 1
tar -xf %SOURCE100 -C ui/keycodemapdb --strip-components 1
tar -xf %SOURCE101 -C tests/fp/berkeley-testfloat-3 --strip-components 1
tar -xf %SOURCE102 -C tests/fp/berkeley-softfloat-3 --strip-components 1

for p in `cat debian/patches/series`; do
    patch -p1 < debian/patches/$p
done

%build
export CFLAGS="%optflags"
# non-GNU configure
./configure \
        --with-git-submodules=ignore \
        --target-list=x86_64-softmmu,aarch64-softmmu \
        --prefix=%_prefix \
        --sysconfdir=%_sysconfdir \
        --libdir=%_libdir \
        --mandir=%_mandir \
        --libexecdir=%_libexecdir \
        --localstatedir=%_localstatedir \
        --extra-cflags="%optflags" \
        --with-pkgversion=%name-%version-%release \
        --firmwarepath="%firmwaredirs" \
        --disable-lto \
        --disable-werror \
        --disable-debug-tcg \
        --audio-drv-list="alsa" \
        --disable-capstone \
        --disable-gtk \
        --disable-guest-agent \
        --disable-guest-agent-msi \
        --disable-libnfs \
        --disable-libssh \
        --disable-sdl \
        --disable-smartcard \
        --disable-strip \
        --disable-xen \
        --enable-virglrenderer \
        --enable-curl \
        --enable-glusterfs \
        --enable-gnutls \
        --enable-libiscsi \
        --enable-libusb \
        --enable-linux-aio \
        --enable-linux-io-uring \
        --enable-numa \
        --enable-opengl \
        --enable-rbd \
        --enable-seccomp \
	--enable-slirp \
        --enable-spice \
        --enable-usb-redir \
        --enable-virglrenderer \
        --enable-virtfs \
        --enable-virtiofsd \
        --enable-zstd

%make_build V=1

%install
%makeinstall_std

%define docdir %_docdir/%name-%version
#mv %buildroot%_docdir/qemu
mkdir -p %buildroot%docdir
install -m644 LICENSE MAINTAINERS %buildroot%docdir/
rm -rf %buildroot%_docdir/qemu

install -m 0755 %SOURCE5 %buildroot%_bindir/qemu-kvm
ln -r -s %buildroot%_bindir/qemu-kvm %buildroot%_bindir/kvm
ln -r -s %buildroot%_bindir/qemu-kvm %buildroot%_bindir/qemu
ln -sf qemu.1.xz %buildroot%_man1dir/qemu-kvm.1.xz

rm -f %buildroot%_bindir/check-*
rm -f %buildroot%_desktopdir/%rname.desktop
rm -rf %buildroot%_iconsdir

# TODO:
# Install qemu-pr-helper service
#install -m 0644 contrib/systemd/qemu-pr-helper.service %buildroot%_unitdir/qemu-pr-helper.service
#install -m 0644 contrib/systemd/qemu-pr-helper.socket %buildroot%_unitdir/qemu-pr-helper.socket
# Install rules to use the bridge helper with libvirt's virbr0
install -D -m 0644 %SOURCE12 %buildroot%_sysconfdir/%name/bridge.conf

%if_enabled vnc_sasl
install -D -p -m 0644 qemu.sasl %buildroot%_sysconfdir/sasl2/%rname.conf
%endif

%find_lang %rname

rm -f %buildroot%_datadir/%rname/pxe*rom
rm -f %buildroot%_datadir/%rname/efi*rom
rm -f %buildroot%_datadir/%rname/vgabios*bin
rm -f %buildroot%_datadir/%rname/bios.bin
rm -f %buildroot%_datadir/%rname/bios-256k.bin
rm -f %buildroot%_datadir/%rname/bios-microvm.bin
rm -f %buildroot%_datadir/%rname/qboot.rom
rm -f %buildroot%_datadir/%rname/openbios*
rm -f %buildroot%_datadir/%rname/*.dtb
rm -f %buildroot%_datadir/%rname/s390-*.img
rm -f %buildroot%_datadir/%rname/qemu_vga.ndrv
rm -f %buildroot%_datadir/%rname/slof.bin
rm -f %buildroot%_datadir/%rname/u-boot*
rm -f %buildroot%_datadir/%rname/palcode-clipper
rm -f %buildroot%_datadir/%rname/opensbi*
#rm -f %buildroot%_datadir/%rname/edk2-*
rm -f %buildroot%_datadir/%rname/firmware/*
rm -f %buildroot%_datadir/%rname/qemu-nsis.bmp
rm -rf %buildroot%_includedir

for rom in e1000 ne2k_pci pcnet rtl8139 virtio eepro100 e1000e vmxnet3 ; do
  ln -r -s %buildroot%_datadir/ipxe/pxe-${rom}.rom %buildroot%_datadir/%rname/pxe-${rom}.rom
  ln -r -s %buildroot%_datadir/ipxe.efi/efi-${rom}.rom %buildroot%_datadir/%rname/efi-${rom}.rom
done

for bios in vgabios vgabios-cirrus vgabios-qxl vgabios-stdvga vgabios-vmware vgabios-virtio vgabios-ramfb vgabios-bochs-display vgabios-ati ; do
  ln -r -s %buildroot%_datadir/seavgabios/${bios}.bin %buildroot%_datadir/%rname/${bios}.bin
done

ln -r -s %buildroot%_datadir/seabios/{bios,bios-256k,bios-microvm}.bin %buildroot%_datadir/%rname/
ln -r -s %buildroot%_datadir/qboot/bios.bin %buildroot%_datadir/%rname/qboot.rom

mkdir -p %buildroot%_datadir/pve-edk2-firmware
ln -sf ../OVMF/OVMF_CODE.fd %buildroot%_datadir/pve-edk2-firmware/OVMF_CODE.fd
ln -sf ../OVMF/OVMF_VARS.fd %buildroot%_datadir/pve-edk2-firmware/OVMF_VARS.fd
ln -sf ../OVMF/OVMF_CODE_4M.fd %buildroot%_datadir/pve-edk2-firmware/OVMF_CODE_4M.fd
ln -sf ../OVMF/OVMF_VARS_4M.fd %buildroot%_datadir/pve-edk2-firmware/OVMF_VARS_4M.fd
ln -sf ../OVMF/OVMF_CODE_4M.secboot.fd %buildroot%_datadir/pve-edk2-firmware/OVMF_CODE_4M.secboot.fd
ln -sf ../OVMF/OVMF_VARS_4M.secboot.fd %buildroot%_datadir/pve-edk2-firmware/OVMF_VARS_4M.secboot.fd
ln -sf ../OVMF/OVMF_VARS_4M.ms.fd %buildroot%_datadir/pve-edk2-firmware/OVMF_VARS_4M.ms.fd
ln -sf ../AAVMF/AAVMF_CODE.fd %buildroot%_datadir/pve-edk2-firmware/AAVMF_CODE.fd
ln -sf ../AAVMF/AAVMF_VARS.fd %buildroot%_datadir/pve-edk2-firmware/AAVMF_VARS.fd


%check
# Disabled on aarch64 where it fails with several errors.  Will
# investigate and fix when we have access to real hardware
#ifnarch aarch64
#make V=1 check
#endif

%pre common
%_sbindir/groupadd -r -f %_group

%files

%files common
%dir %docdir/
%docdir/LICENSE
%docdir/MAINTAINERS
%_datadir/%rname
%_datadir/pve-edk2-firmware
%dir %_sysconfdir/%name
%if_enabled vnc_sasl
%config(noreplace) %_sysconfdir/sasl2/%rname.conf
%endif
%_man7dir/qemu-block-drivers.*
%_man7dir/qemu-qmp-ref.*
%_man7dir/qemu-cpu-models.*

%files system -f %rname.lang
%_bindir/elf2dmp
%_bindir/qemu*system*
%_bindir/qemu-edid
%_bindir/qemu-storage-daemon
%_bindir/qemu-kvm
%_bindir/kvm
%_bindir/qemu
%_bindir/pbs-restore
%_bindir/vma
%_man1dir/qemu.1*
%_man1dir/qemu-kvm.1*
%attr(4710,root,vmusers) %_libexecdir/qemu-bridge-helper
%config(noreplace) %_sysconfdir/%name/bridge.conf
# TODO:
%_bindir/qemu-pr-helper
#%_unitdir/qemu-pr-helper.service
#%_unitdir/qemu-pr-helper.socket
%_libexecdir/vhost-user-gpu
%_libexecdir/virtfs-proxy-helper
%_man1dir/virtfs-proxy-helper.*
%_libexecdir/virtiofsd
%_man1dir/virtiofsd.*
%_man1dir/qemu-storage-daemon.1*
%_man7dir/qemu-storage-daemon-qmp-ref.*
%_man8dir/qemu-pr-helper.8*

%files img
%_bindir/qemu-img
%_bindir/qemu-io
%_bindir/qemu-nbd
%_man1dir/qemu-img.1*
%_man8dir/qemu-nbd.8*

%changelog
* Fri Mar 17 2023 Alexey Shabalin <shaba@altlinux.org> 1:7.2.0-alt1
- 7.2.0-8 (Fixes: CVE-2022-4172)
- delete cpu-add-Kunpeng-920-cpu-support.patch
- lto disable
- drop control and udev rules for set access mode to /dev/kvm

* Thu Dec 01 2022 Alexey Shabalin <shaba@altlinux.org> 1:7.1.0-alt4
- skip requires on files in /usr/share/OVMF and /usr/share/AAVMF

* Thu Dec 01 2022 Alexey Shabalin <shaba@altlinux.org> 1:7.1.0-alt3
- delete version from requires for edk2-ovmf

* Wed Nov 30 2022 Alexey Shabalin <shaba@altlinux.org> 1:7.1.0-alt2
- 7.1.0-4
- add symlinks to 4MB edk2 firmwares

* Mon Nov 14 2022 Alexey Shabalin <shaba@altlinux.org> 1:7.1.0-alt1
- 7.1.0-3 (Fixes: CVE-2020-14394, CVE-2022-0216, CVE-2021-3507
   CVE-2021-4206, CVE-2021-4207, CVE-2021-3611, CVE-2022-26353
   CVE-2022-26354, CVE-2021-3929, CVE-2022-35414)

* Wed Jun 22 2022 Alexey Shabalin <shaba@altlinux.org> 1:6.2.0-alt2
- 6.2.0-11

* Fri May 06 2022 Alexey Shabalin <shaba@altlinux.org> 1:6.2.0-alt1
- 6.2.0-5

* Tue Feb 15 2022 Alexey Shabalin <shaba@altlinux.org> 1:6.1.1-alt2
- build from gear
- add virtual pve-qemu package

* Tue Feb 15 2022 Valery Inozemtsev <shrek@altlinux.ru> 1:6.1.1-alt1
- 6.1.1-2
- Fixes:
  + CVE-2021-3713
  + CVE-2021-3748
  + CVE-2021-3930
  + CVE-2021-3947
  + CVE-2021-20196
  + CVE-2021-20203
  + CVE-2021-20257

* Mon Jan 24 2022 Alexey Shabalin <shaba@altlinux.org> 1:6.1.0-alt4
- build with libproxmox-backup-qemu-devel
- update BuildRequires and Requires
- update License
- build with --firmwarepath
- fix symlinks to edk2 aarch64 firmware
- delete /usr/share/qemu/firmware/*, included in edk2 packages

* Tue Dec 07 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:6.1.0-alt3
- 6.1.0-3

* Wed Dec 01 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:6.1.0-alt2
- 6.1.0-2

* Fri Oct 22 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:6.1.0-alt1
- 6.1.0-1

* Wed Oct 20 2021 Andrew A. Vasilyev <andy@altlinux.org> 1:6.0.0-alt2
- build in one job, race in meson.build due to missing deps

* Wed Sep 29 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:6.0.0-alt1
- 6.0.0-4

* Mon Mar 29 2021 Alexey Shabalin <shaba@altlinux.org> 1:5.1.0-alt6
- install /usr/bin/qemu-kvm script
- update udev rules and control
- fix perm of qemu-bridge-helper

* Tue Mar 16 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.0-alt5
- move PBS into separate package

* Mon Feb 01 2021 Andrew A. Vasilyev <andy@altlinux.org> 1:5.1.0-alt4
- add Kunpeng 920 cpu support

* Tue Dec 08 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.0-alt3
- 5.1.0-7

* Sat Oct 10 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.0-alt2
- 5.1.0-3 (fix CVE-2020-14364)

* Tue Sep 01 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.0-alt1
- 5.1.0-1

* Wed Mar 11 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:4.1.1-alt4
- 4.1.1-4 (fix CVE-2020-8608)

* Fri Mar 06 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:4.1.1-alt3
- 4.1.1-3 (fix CVE-2019-20382)

* Wed Jan 22 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:4.1.1-alt2
- 4.1.1-2

* Mon Nov 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:4.1.1-alt1
- 4.1.1-1

* Wed Nov 13 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:4.0.1-alt3
- 4.0.1-5

* Wed Oct 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:4.0.1-alt2
- 4.0.1-2

* Wed Oct 02 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:4.0.0-alt2
- 4.0.0-6

* Tue Aug 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:4.0.0-alt1
- 4.0.0-5

* Tue Jun 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:3.0.1-alt5
- 3.0.1-62

* Mon Jun 17 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:3.0.1-alt4
- 3.0.1-4

* Mon May 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:2.12.1-alt3
- 2.12.1-3

* Mon Oct 22 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:2.12.1-alt1
- 2.12.1-1

* Fri Sep 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 3.0.0-alt2
- fixed efi roms path

* Mon Sep 17 2018 Valery Inozemtsev <shrek@altlinux.ru> 3.0.0-alt1.S1
- 3.0.0-1

* Thu Sep 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.11.2-alt2.S1
- disable vde support

* Tue Sep 04 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.11.2-alt1.S1
- 2.11.2-1

* Mon Jul 16 2018 Igor Vlasenko <viy@altlinux.ru> 2.11.1-alt5.S1.1.qa2
- reverted repocop patch (closes: #35115)

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 2.11.1-alt5.S1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * udev-files-in-etc for pve-qemu-common

* Thu May 17 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.11.1-alt5.S1.1
- remove problematic 'evdev 86' key from en-us keymap (closes: #34856)

* Mon Apr 09 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.11.1-alt5.S1
- 2.11.1-5

* Fri Mar 23 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.11.1-alt4.S1
- 2.11.1-4

* Tue Feb 20 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt9.S1
- 2.9.1-9

* Wed Jan 17 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt6.S1
- 2.9.1-6

* Fri Dec 22 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt4.1
- rebuild with libiscsi 1.18

* Thu Dec 07 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt0.M80P.4
- backport to p8 branch

* Thu Dec 07 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt4
- fixes:
 + CVE-2017-17381 fix and backup race condition fix

* Mon Sep 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt0.M80C.1
- backport to c8 branch

* Fri Sep 08 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt0.M80P.1
- backport to p8 branch

* Fri Sep 08 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt1
- 2.9.1-1

* Mon Aug 07 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.0-alt0.M80P.3
- backport to p8 branch

* Mon Aug 07 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.0-alt3
- fix CVE-2017-7539, CVE-2017-11434, CVE-2017-11334, CVE-2017-10806, CVE-2017-10664, CVE-2017-9524, CVE-2017-9503

* Fri Jun 16 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.0-alt0.M80P.2
- backport to p8 branch

* Fri Jun 16 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.0-alt2
- merge various stable fixes

* Thu May 11 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.0-alt0.M80P.1
- backport to p8 branch

* Thu May 11 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.0-alt1
- 2.9.0-1

* Wed Apr 05 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt3.M80P.1
- backport to p8 branch

* Wed Apr 05 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt4
- 2.7.1-4

* Thu Feb 02 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt1.M80P.1
- backport to p8 branch

* Thu Feb 02 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt2
- various fixes

* Mon Jan 16 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt0.M80P.1
- backport to p8 branch

* Mon Jan 16 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Tue Dec 13 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt9.M80P.1
- backport to p8 branch

* Tue Dec 13 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt10
- 2.7.0-10

* Mon Dec 05 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt8.M80P.1
- backport to p8 branch

* Mon Dec 05 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt9
- 2.7.0-9

* Tue Nov 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt7.M80P.1
- backport to p8 branch

* Tue Nov 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt8
- 2.7.0-8

* Sun Oct 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt2.M80P.1
- backport to p8 branch

* Sun Oct 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt3
- various fixes

* Mon Oct 17 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt1.M80P.1
- backport to p8 branch

* Mon Oct 17 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt2
- 2.7.0-2

* Sun Oct 09 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.2-alt1.M80P.1
- backport to p8 branch

* Fri Oct 07 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.2-alt2
- 2.6.2-2

* Mon Oct 03 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt5.M80P.1
- backport to p8 branch

* Mon Oct 03 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt6
- various CVE fixes

* Tue Sep 20 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt4.M80P.1
- backport to p8 branch

* Mon Sep 19 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt5
- various CVE fixes

* Thu Aug 25 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt2
- added in some stable hotfixes

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Aug 02 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.0-alt2
- fixed CVE-2016-6490, CVE-2016-2391, CVE-2016-5126

* Sun Jul 10 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Wed Jun 01 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.5.1.1-alt1
- 2.5.1.1

* Tue Feb 09 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.5.0-alt1
- proxmox version
