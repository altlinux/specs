%define rname qemu

%def_disable binfmt_misc

%def_disable werror
%def_enable sdl
%def_disable sdl2
%def_enable curses
%def_enable bluez
%def_enable vnc
%def_enable vnc_sasl
%def_enable vnc_jpeg
%def_enable vnc_png
%def_enable vde
%def_enable alsa
%def_disable pulseaudio
%def_disable oss
%def_enable aio
%def_enable blobs
%def_enable uuid
%def_disable smartcard
%def_enable libusb
%def_enable usb_redir
%def_enable vhost_net
%def_enable vhost_scsi
%def_disable opengl
%def_disable guest_agent
%def_enable tools
%def_enable spice
%def_enable libiscsi
%def_enable rbd
%def_disable libnfs
%def_enable seccomp
%def_enable glusterfs
%def_disable gtk
%def_disable gtk_gl
%def_enable gnutls
%def_enable nettle
%def_disable gcrypt
%def_enable virglrenderer
%def_enable tpm
%def_enable libssh2
%def_enable numa
%def_enable jemalloc
%def_enable rdma
%def_enable lzo
%def_enable snappy
%def_enable bzip2
%def_disable xen

%define _group vmusers
%define rulenum 90
%define _libexecdir /usr/libexec
%define _localstatedir /var

Name: pve-%rname
Version: 2.9.1
Release: alt6%ubt
Summary: QEMU CPU Emulator
License: GPL/LGPL/BSD
Group: Emulators
Requires: %name-system = %version-%release, %name-user = %version-%release
Conflicts: %rname
URL: http://www.nongnu.org/qemu/

Source0: qemu-%version.tar.xz
Source2: qemu-kvm.control.in
Source4: qemu-kvm.rules
# qemu-kvm back compat wrapper
Source5: qemu-kvm.sh

Source100: Logo.bmp

Patch0: qemu-alt.patch

Patch10: 0001-fr-ca-keymap-corrections.patch
Patch11: 0002-Adjust-network-script-path-to-etc-kvm.patch
Patch12: 0003-qemu-img-return-success-on-info-without-snapshots.patch
Patch13: 0004-use-kvm-by-default.patch
Patch14: 0005-virtio-balloon-fix-query.patch
Patch15: 0006-set-the-CPU-model-to-kvm64-32-instead-of-qemu64-32.patch
Patch16: 0007-qapi-modify-query-machines.patch
Patch17: 0008-qapi-modify-spice-query.patch
Patch18: 0009-ui-spice-default-to-pve-certs-unless-otherwise-speci.patch
Patch19: 0010-internal-snapshot-async.patch
Patch20: 0011-convert-savevm-async-to-threads.patch
Patch21: 0012-qmp-add-get_link_status.patch
Patch22: 0013-smm_available-false.patch
Patch23: 0014-use-whitespace-between-VERSION-and-PKGVERSION.patch
Patch24: 0015-vnc-altgr-emulation.patch
Patch25: 0016-vnc-make-x509-imply-tls-again.patch
Patch26: 0017-vnc-PVE-VNC-authentication.patch
Patch27: 0018-migrate-fix-possible-unitialised-return-value.patch
Patch28: 0019-block-rbd-disable-rbd_cache_writethrough_until_flush.patch
Patch29: 0020-block-snapshot-qmp_snapshot_drive-add-aiocontext.patch
Patch30: 0021-block-snapshot-qmp_delete_drive_snapshot-add-aiocont.patch
Patch31: 0022-glusterfs-no-default-logfile-if-daemonized.patch
Patch32: 0023-glusterfs-allow-partial-reads.patch
Patch33: 0024-block-add-the-zeroinit-block-driver-filter.patch
Patch34: 0025-qemu-img-dd-add-osize-and-read-from-to-stdin-stdout.patch
Patch35: 0026-backup-modify-job-api.patch
Patch36: 0027-backup-introduce-vma-archive-format.patch
Patch37: 0028-adding-old-vma-files.patch
Patch38: 0029-backup-fix-race-in-backup-stop-command.patch
Patch39: 0001-Revert-target-i386-disable-LINT0-after-reset.patch
Patch40: 0002-virtio-serial-fix-segfault-on-disconnect.patch
Patch41: 0003-megasas-always-store-SCSIRequest-into-MegasasCmd.patch
Patch42: 0004-slirp-check-len-against-dhcp-options-array-end.patch
Patch43: 0005-IDE-Do-not-flush-empty-CDROM-drives.patch
Patch44: 0006-bitmap-add-bitmap_copy_and_clear_atomic.patch
Patch45: 0007-memory-add-support-getting-and-using-a-dirty-bitmap-.patch
Patch46: 0008-vga-add-vga_scanline_invalidated-helper.patch
Patch47: 0009-vga-make-display-updates-thread-safe.patch
Patch48: 0010-vga-fix-display-update-region-calculation.patch
Patch49: 0011-vga-fix-display-update-region-calculation-split-scre.patch
Patch50: 0012-vga-stop-passing-pointers-to-vga_draw_line-functions.patch
Patch51: 0013-multiboot-validate-multiboot-header-address-values.patch
Patch52: 0014-virtio-fix-descriptor-counting-in-virtqueue_pop.patch
Patch53: 0015-nbd-server-CVE-2017-15119-Reject-options-larger-than.patch
Patch54: 0016-vga-migration-Update-memory-map-in-post_load.patch
Patch55: 0017-vga-drop-line_offset-variable.patch
Patch56: 0018-vga-handle-cirrus-vbe-mode-wraparounds.patch
Patch57: 0019-vga-add-ram_addr_t-cast.patch
Patch58: 0020-vga-fix-region-checks-in-wraparound-case.patch
Patch59: 0021-io-monitor-encoutput-buffer-size-from-websocket-GSou.patch
Patch60: 0022-9pfs-use-g_malloc0-to-allocate-space-for-xattr.patch
Patch61: 0023-cirrus-fix-oob-access-in-mode4and5-write-functions.patch
Patch62: 0024-virtio-check-VirtQueue-Vring-object-is-set.patch
Patch63: 0025-block-gluster-glfs_lseek-workaround.patch
Patch64: 0026-gluster-add-support-for-PREALLOC_MODE_FALLOC.patch
Patch65: 0027-target-i386-Use-host_vendor_fms-in-max_x86_cpu_initf.patch
Patch66: 0028-target-i386-Define-CPUID_MODEL_ID_SZ-macro.patch
Patch67: 0029-target-i386-Don-t-use-x86_cpu_load_def-on-max-CPU-mo.patch
Patch68: 0030-i386-Change-X86CPUDefinition-model_id-to-const-char.patch
Patch69: 0031-i386-Add-support-for-SPEC_CTRL-MSR.patch
Patch70: 0032-i386-Add-spec-ctrl-CPUID-bit.patch
Patch71: 0033-i386-Add-FEAT_8000_0008_EBX-CPUID-feature-word.patch
Patch72: 0034-i386-Add-new-IBRS-versions-of-Intel-CPU-models.patch

ExclusiveArch: x86_64
BuildRequires(pre): rpm-build-ubt
BuildRequires: glibc-devel-static zlib-devel-static glib2-devel-static
BuildRequires: texinfo perl-podlators libattr-devel libcap-devel libcap-ng-devel
BuildRequires: libxfs-devel
BuildRequires: zlib-devel libcurl-devel libpci-devel glibc-kernheaders
BuildRequires: ipxe-roms-qemu >= 1.0.0-alt4.git93acb5d seavgabios seabios libfdt-devel >= 1.4.0
BuildRequires: libpixman-devel >= 0.21.8
BuildRequires: iasl
%{?_enable_sdl:BuildRequires: libSDL-devel libX11-devel}
%{?_enable_sdl2:BuildRequires: libSDL2-devel}
%{?_enable_curses:BuildRequires: libncurses-devel}
%{?_enable_bluez:BuildRequires: libbluez-devel}
%{?_enable_alsa:BuildRequires: libalsa-devel}
%{?_enable_pulseaudio:BuildRequires: libpulseaudio-devel}
%{?_enable_vnc_sasl:BuildRequires: libsasl2-devel}
%{?_enable_vnc_jpeg:BuildRequires: libjpeg-devel}
%{?_enable_vnc_png:BuildRequires: libpng-devel}
%{?_enable_vde:BuildRequires: libvde-devel}
%{?_enable_aio:BuildRequires: libaio-devel}
%{?_enable_spice:BuildRequires: libspice-server-devel >= 0.12.0 spice-protocol >= 0.12.3}
%{?_enable_uuid:BuildRequires: libuuid-devel-static}
%{?_enable_smartcard:BuildRequires: libcacard-devel >= 2.5.0}
%{?_enable_usb_redir:BuildRequires: libusbredir-devel >= 0.5}
%{?_enable_opengl:BuildRequires: libX11-devel libepoxy-devel}
%{?_enable_guest_agent:BuildRequires: glib2-devel >= 2.38 python-base}
%{?_enable_rbd:BuildRequires: ceph-devel}
%{?_enable_libiscsi:BuildRequires: libiscsi-devel >= 1.9.0}
%{?_enable_libnfs:BuildRequires: libnfs-devel >= 1.9.3}
%{?_enable_seccomp:BuildRequires: libseccomp-devel >= 2.2.3}
%{?_enable_glusterfs:BuildRequires: pkgconfig(glusterfs-api)}
%{?_enable_gtk:BuildRequires: libgtk+3-devel >= 3.0.0 pkgconfig(vte-2.90) >= 0.32.0}
%{?_enable_gnutls:BuildRequires: libgnutls-devel >= 2.9.10}
%{?_enable_nettle:BuildRequires: libnettle-devel}
%{?_enable_gcrypt:BuildRequires: libgcrypt-devel}
BuildRequires: libtasn1-devel
%{?_enable_virglrenderer:BuildRequires: pkgconfig(virglrenderer)}
%{?_enable_libssh2:BuildRequires: libssh2-devel >= 1.2.8}
%{?_enable_libusb:BuildRequires: libusb-devel >= 1.0.13}
%{?_enable_rdma:BuildRequires: librdmacm-devel libibverbs-devel}
%{?_enable_numa:BuildRequires: libnuma-devel}
%{?_enable_jemalloc:BuildRequires: libjemalloc-devel}
%{?_enable_lzo:BuildRequires: liblzo2-devel}
%{?_enable_snappy:BuildRequires: libsnappy-devel}
%{?_enable_bzip2:BuildRequires: bzlib-devel}
%{?_enable_xen:BuildRequires: xen-devel}

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
Requires: seavgabios
Requires: seabios
Requires: ipxe-roms-qemu >= 1.0.0-alt4.git93acb5d
Requires: %name-img = %version-%release
Requires: edk2-ovmf
Conflicts: %rname-common

%description common
QEMU is a fast processor emulator using dynamic translation to achieve
good emulation speed.
This package contains common files for qemu.

%package system
Summary: QEMU CPU Emulator - full system emulation
Group: Emulators
Requires: %name-common = %version-%release
Conflicts: %rname-system

%description system
Full system emulation.  In this mode, QEMU emulates a full system
(for example a PC), including a processor and various peripherials.
It can be used to launch different Operating Systems without rebooting
the PC or to debug system code.

%package user
Summary: QEMU CPU Emulator - user mode emulation
Group: Emulators
Requires: %name-common = %version-%release
Conflicts: %rname-user

%description user
User mode emulation.  In this mode, QEMU can launch Linux processes
compiled for one CPU on another CPU.  It can be used to launch the
Wine Windows API emulator or to ease cross-compilation and
cross-debugging.

%package user-binfmt_misc
Summary: QEMU CPU Emulator - user mode emulation, binfmt_misc version
Group: Emulators
Requires: %name-aux = %version-%release
Conflicts: %rname-user-binfmt_misc

%description user-binfmt_misc
User mode emulation.  In this mode, QEMU can launch Linux processes
compiled for one CPU on another CPU.  It can be used to launch the
Wine Windows API emulator or to ease cross-compilation and
cross-debugging.
This package contains static version with enabled binfmt_misc support.
Suitable for hasher.

%package img
Summary: QEMU command line tool for manipulating disk images
Group: Emulators
Requires: %name-aux = %version-%release
Conflicts: %rname-img

%description img
This package provides a command line tool for manipulating disk images

%package guest-agent
Summary: QEMU guest agent
Group: Emulators
Requires: %name-aux = %version-%release
Conflicts: %rname-guest-agent

%description guest-agent
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides an agent to run inside guests, which communicates
with the host over a virtio-serial channel named "org.qemu.guest_agent.0"

This package does not need to be installed on the host OS.

%package doc
Summary: User documentation for %name
Group: Documentation
BuildArch: noarch
Requires: %name-aux = %version-%release

%description doc
User documentation for %name

%package aux
Summary: QEMU auxiliary package
Group: Emulators
BuildArch: noarch
Conflicts: %rname-aux

%description aux
QEMU is a generic and open source processor emulator which achieves
good emulation speed by using dynamic translation.

This is an auxiliary package.

%package -n ivshmem-tools
Summary: Client and server for QEMU ivshmem device
Group: Emulators

%description -n ivshmem-tools
This package provides client and server tools for QEMU's ivshmem device.

%set_verify_elf_method fhs=relaxed

%prep
%setup -n %rname-%version
%patch -p1

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1

cp -f %SOURCE2 qemu-kvm.control.in

%build
export CFLAGS="%optflags"
# non-GNU configure
./configure \
	--target-list=x86_64-softmmu \
	--prefix=%_prefix \
	--sysconfdir=%_sysconfdir \
	--libdir=%_libdir \
	--mandir=%_mandir \
	--libexecdir=%_libexecdir \
	--localstatedir=%_localstatedir \
	--extra-cflags="%optflags" \
	%{subst_enable werror} \
	%{?_enable_sdl:--enable-sdl --with-sdlabi=1.2} \
	%{?_enable_sdl2:--enable-sdl --with-sdlabi=2.0} \
	%{?_disable_curses:--disable-curses} \
	%{subst_enable bluez} \
	%{subst_enable vnc} \
	%{?_enable_gtk:--enable-gtk --with-gtkabi=3.0 --enable-vte} \
	%{?_disable_vnc_tls:--disable-vnc-tls} \
	%{?_disable_vnc_sasl:--disable-vnc-sasl} \
	%{?_disable_vnc_jpeg:--disable-vnc-jpeg} \
	%{?_disable_vnc_png:--disable-vnc-png} \
	%{?_disable_vde:--disable-vde} \
	%{?_disable_aio:--disable-linux-aio} \
	%{?_disable_blobs: --disable-blobs} \
	%{subst_enable spice} \
	%{?_disable_uuid:--disable-uuid} \
	--disable-debug-tcg \
	--disable-sparse \
	--disable-strip \
	--audio-drv-list="alsa" \
	--disable-xen \
	--disable-brlapi \
	--enable-curl \
	--disable-fdt \
	--enable-kvm \
	%{subst_enable virglrenderer} \
	%{subst_enable tpm} \
	%{subst_enable xen} \
	--with-system-pixman \
	%{?_enable_vhost_net:--enable-vhost-net} \
	%{?_enable_vhost_scsi:--enable-vhost-scsi } \
	%{subst_enable smartcard} \
	%{subst_enable libusb} \
	%{?_enable_usb_redir:--enable-usb-redir} \
	%{subst_enable opengl} \
	%{subst_enable seccomp} \
	%{subst_enable libiscsi} \
	%{subst_enable rbd} \
	%{subst_enable libnfs} \
	%{subst_enable glusterfs} \
	%{subst_enable libssh2} \
	%{subst_enable rdma} \
	%{subst_enable gnutls} \
	%{subst_enable nettle} \
	%{subst_enable gcrypt} \
	%{subst_enable numa} \
	%{subst_enable jemalloc} \
	%{subst_enable lzo} \
	%{subst_enable snappy} \
	%{subst_enable bzip2} \
	%{?_disable_guest_agent:--disable-guest-agent} \
	%{subst_enable tools} \
	--enable-pie \
	--enable-xfsctl \
	--enable-virtfs

%make_build

sed -i 's/@GROUP@/%_group/g' qemu-kvm.control.in

%install
%makeinstall_std

%define docdir %_docdir/%name-%version
mv %buildroot%_docdir/qemu %buildroot%docdir
install -m644 LICENSE MAINTAINERS %buildroot%docdir/

install -m 0755 %SOURCE5 %buildroot%_bindir/qemu-kvm
ln -r -s %buildroot%_bindir/qemu-kvm %buildroot%_bindir/kvm
ln -r -s %buildroot%_bindir/qemu-kvm %buildroot%_bindir/qemu

install -m 0755 vma %buildroot%_bindir/vma

rm -f %buildroot%_bindir/check-*
rm -f %buildroot%_sysconfdir/udev/rules.d/*

install -D -m 0644 %SOURCE4 %buildroot%_sysconfdir/udev/rules.d/%rulenum-%rname-kvm.rules
install -D -m 0755 %rname-kvm.control.in %buildroot%_controldir/kvm

%if_enabled vnc_sasl
install -D -p -m 0644 qemu.sasl %buildroot%_sysconfdir/sasl2/%rname.conf
%endif

%find_lang %rname

rm -f %buildroot%_datadir/%rname/pxe*rom
rm -f %buildroot%_datadir/%rname/efi*rom
rm -f %buildroot%_datadir/%rname/vgabios*bin
rm -f %buildroot%_datadir/%rname/bios.bin
rm -f %buildroot%_datadir/%rname/bios-256k.bin
rm -f %buildroot%_datadir/%rname/s390-ccw.img
rm -f %buildroot%_datadir/%rname/openbios*
rm -f %buildroot%_datadir/%rname/u-boot*

for rom in e1000 ne2k_pci pcnet rtl8139 virtio eepro100 e1000e vmxnet3 ; do
  ln -r -s %buildroot%_datadir/ipxe/pxe-${rom}.rom %buildroot%_datadir/%rname/pxe-${rom}.rom
  ln -r -s %buildroot%_datadir/ipxe.efi/efi-${rom}.rom %buildroot%_datadir/%rname/efi-${rom}.rom
done

for bios in vgabios vgabios-cirrus vgabios-qxl vgabios-stdvga vgabios-vmware vgabios-virtio ; do
  ln -r -s %buildroot%_datadir/seavgabios/${bios}.bin %buildroot%_datadir/%rname/${bios}.bin
done

ln -r -s %buildroot%_datadir/seabios/{bios,bios-256k}.bin %buildroot%_datadir/%rname/

mkdir -p %buildroot%_datadir/kvm/
ln -sf ../OVMF/OVMF_CODE.fd %buildroot%_datadir/kvm/OVMF_CODE-pure-efi.fd
ln -sf ../OVMF/OVMF_VARS.fd %buildroot%_datadir/kvm/OVMF_VARS-pure-efi.fd

%check
# Disabled on aarch64 where it fails with several errors.  Will
# investigate and fix when we have access to real hardware 
#ifnarch aarch64
#make V=1 check
#endif

%pre common
%_sbindir/groupadd -r -f %_group
if [ -f %_controldir/qemu-kvm ];then
%pre_control qemu-kvm
mv -f /var/run/control/qemu-kvm /var/run/control/kvm
else
%pre_control kvm
fi

%post common
%post_control -s vmusers kvm

%files common
%_datadir/qemu
%_datadir/kvm
%_man1dir/qemu*
%_man8dir/qemu*
%_sysconfdir/udev/rules.d/%rulenum-%rname-kvm.rules
%_controldir/*
%if_enabled vnc_sasl
%config(noreplace) %_sysconfdir/sasl2/%rname.conf
%endif

%files system -f %rname.lang
%_bindir/qemu
%_bindir/qemu-kvm
%_bindir/kvm
%_bindir/qemu*system*
%_bindir/vma

%files img
%_bindir/qemu-img
%_bindir/qemu-io
%_bindir/qemu-nbd
%_bindir/virtfs-proxy-helper
%_man1dir/virtfs-proxy-helper.*
%_libexecdir/qemu-bridge-helper

%files aux
%dir %docdir/
%docdir/LICENSE

%changelog
* Wed Jan 17 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt6%ubt
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
