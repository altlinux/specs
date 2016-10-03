# vim: set ft=spec
# vim600: set fdm=marker:

%define rname qemu

# {{{ macros define
%def_disable binfmt_misc

%def_without alpha
%def_without aarch64
%def_without arm
%def_without cris
%def_with x86
%def_without m68k
%def_without microblaze
%def_without mips
%def_without ppc
%def_without sh4
%def_without sparc
%def_without s390x
%def_without lm32
%def_without xtensa
%def_without moxie
%def_without tilegx
%def_without tricore
%def_without unicore32

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
%def_enable guest_agent
%def_enable tools
%def_enable spice
%def_enable libiscsi
%def_enable rbd
%def_enable libnfs
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
%def_enable vhdx
%def_enable numa
%def_enable jemalloc
%def_enable rdma
%def_enable lzo
%def_enable snappy
%def_enable bzip2
%def_disable xen

%define audio_drv_list %{?_enable_oss:oss} %{?_enable_alsa:alsa} %{?_enable_sdl:sdl} %{?_enable_sdl2:sdl} %{?_enable_pulseaudio:pa}

%define _group vmusers
%define rulenum 90
%define _libexecdir /usr/libexec
%define _localstatedir /var

%global target_list_system %nil
%global target_list_user %nil

%if_with alpha
%global target_list_system %target_list_system alpha-softmmu
%global target_list_user %target_list_user alpha-linux-user
%endif

%if_with aarch64
%global target_list_system %target_list_system aarch64-softmmu
%global target_list_user %target_list_user aarch64-linux-user
%endif

%if_with arm
%global target_list_system %target_list_system arm-softmmu
%global target_list_user %target_list_user arm-linux-user armeb-linux-user
%endif

%if_with cris
%global target_list_system %target_list_system cris-softmmu
%global target_list_user %target_list_user cris-linux-user
%endif

%if_with x86
%global target_list_system %target_list_system i386-softmmu x86_64-softmmu
%global target_list_user %target_list_user i386-linux-user x86_64-linux-user
%endif

%if_with m68k
%global target_list_system %target_list_system m68k-softmmu
%global target_list_user %target_list_user m68k-linux-user
%endif

%if_with microblaze
%global target_list_system %target_list_system microblaze-softmmu microblazeel-softmmu
%global target_list_user %target_list_user microblaze-linux-user microblazeel-linux-user
%endif

%if_with mips
%global target_list_system %target_list_system mips-softmmu mipsel-softmmu mips64-softmmu mips64el-softmmu
%global target_list_user %target_list_user mips-linux-user mipsel-linux-user mips64-linux-user mips64el-linux-user mipsn32-linux-user mipsn32el-linux-user
%endif

%if_with ppc
%global target_list_system %target_list_system ppc-softmmu ppcemb-softmmu ppc64-softmmu
%global target_list_user %target_list_user ppc-linux-user ppc64-linux-user ppc64le-linux-user ppc64abi32-linux-user
%endif

%if_with sh4
%global target_list_system %target_list_system sh4-softmmu sh4eb-softmmu
%global target_list_user %target_list_user sh4-linux-user sh4eb-linux-user
%endif

%if_with sparc
%global target_list_system %target_list_system sparc-softmmu sparc64-softmmu
%global target_list_user %target_list_user sparc-linux-user sparc64-linux-user sparc32plus-linux-user
%endif

%if_with s390x
%global target_list_system %target_list_system s390x-softmmu
%global target_list_user %target_list_user s390x-linux-user
%endif

%if_with lm32
%global target_list_system %target_list_system lm32-softmmu
%endif

%if_with unicore32
%global target_list_system %target_list_system unicore32-softmmu
%global target_list_user %target_list_user unicore32-linux-user
%endif

%if_with xtensa
%global target_list_system %target_list_system xtensa-softmmu xtensaeb-softmmu
%global target_list_user %target_list_user xtensaeb-linux-user
%endif

%if_with moxie
%global target_list_system %target_list_system moxie-softmmu
%endif

%if_with tricore
%global target_list_system %target_list_system tricore-softmmu
%endif

%if_with tilegx
%global target_list_user %target_list_user tilegx-linux-user
%endif
# }}}

Name: pve-%rname
Version: 2.6.1
Release: alt6

Summary: QEMU CPU Emulator
License: GPL/LGPL/BSD
Group: Emulators
Requires: %name-system = %version-%release, %name-user = %version-%release
Conflicts: %rname

URL: http://www.nongnu.org/qemu/
Source0: qemu-kvm-src.tar.gz
Source1: qemu.binfmt
Source2: qemu-kvm.control.in
Source4: qemu-kvm.rules
# qemu-kvm back compat wrapper
Source5: qemu-kvm.sh
Source8: qemu-guest-agent.rules
Source9: qemu-guest-agent.service
Source10: qemu-guest-agent.init
Source11: OVMF_CODE-pure-efi.fd
Source12: OVMF_VARS-pure-efi.fd

Patch0: qemu-2.6-alt.patch

Patch10: 0001-9pfs-forbid-illegal-path-names.patch
Patch11: 0001-fr-ca-keymap-corrections.patch
Patch12: 0001-net-check-fragment-length-during-fragmentation.patch
Patch13: 0001-Revert-target-i386-disable-LINT0-after-reset.patch
Patch14: 0002-9pfs-forbid-.-and-.-in-file-names.patch
Patch15: 0002-Adjust-network-script-path-to-etc-kvm.patch
Patch16: 0002-net-vmxnet3-check-for-device_active-before-write.patch
Patch17: 0002-scsi-esp-fix-migration.patch
Patch18: 0003-9pfs-handle-walk-of-.-in-the-root-directory.patch
Patch19: 0003-net-vmxnet-use-g_new-for-pkt-initialisation.patch
Patch20: 0003-vnc-altgr-emulation.patch
Patch21: 0004-net-vmxnet-check-IP-header-length.patch
Patch22: 0004-qemu-img-return-success-on-info-without-snapshots.patch
Patch23: 0005-net-vmxnet-initialise-local-tx-descriptor.patch
Patch24: 0005-use-kvm-by-default.patch
Patch25: 0006-virtio-balloon-fix-query.patch
Patch26: 0006-virtio-recalculate-vq-inuse-after-migration.patch
Patch27: 0007-set-the-CPU-model-to-kvm64-32-instead-of-qemu64-32.patch
Patch28: 0007-virtio-decrement-vq-inuse-in-virtqueue_discard.patch
Patch29: 0008-iscsi-pass-SCSI-status-back-for-SG_IO.patch
Patch30: 0008-qapi-modify-query-machines.patch
Patch31: 0009-net-limit-allocation-in-nc_sendv_compat.patch
Patch32: 0009-qapi-modify-spice-query.patch
Patch33: 0010-ui-fix-refresh-of-VNC-server-surface.patch
Patch34: 0010-ui-spice-default-to-pve-certs-unless-otherwise-speci.patch
Patch35: 0011-introduce-new-vma-archive-format.patch
Patch36: 0012-vma-add-verify-command.patch
Patch37: 0013-vma-add-config-command-to-dump-the-config.patch
Patch38: 0014-vma-restore-tolerate-a-size-difference-up-to-4M.patch
Patch39: 0015-backup-modify-job-api.patch
Patch40: 0016-backup-add-pve-monitor-commands.patch
Patch41: 0017-backup-vma-add-dir-format.patch
Patch42: 0018-backup-do-not-return-errors-in-dump-callback.patch
Patch43: 0019-backup-vma-correctly-propagate-error.patch
Patch44: 0020-backup-vma-remove-async-queue.patch
Patch45: 0021-backup-vma-run-flush-inside-coroutine.patch
Patch46: 0022-backup-do-not-use-bdrv_drain_all.patch
Patch47: 0023-internal-snapshot-async.patch
Patch48: 0024-backup-vma-allow-empty-backups.patch
Patch49: 0025-backup-vma-add-BlockDriver-to-bdrv_open-in-extract_c.patch
Patch50: 0026-glusterfs-daemonize.patch
Patch51: 0027-gluster-possiblity-to-specify-a-secondary-server.patch
Patch52: 0028-qmp-add-get_link_status.patch
Patch53: 0029-smm_available-false.patch
Patch54: 0030-use-whitespace-between-VERSION-and-PKGVERSION.patch
Patch55: 0031-vma-add-firewall.patch
Patch56: 0032-vma-writer-aio_set_fd_handler-update.patch
Patch57: 0033-vma-bdrv_open-dropped-the-drv-parameter.patch
Patch58: 0034-blockdev-bdrv_open-dropped-the-drv-parameter.patch
Patch59: 0035-blockdev-backup_start-now-takes-a-BlockJobTxn.patch
Patch60: 0036-savevm-async-migration-and-bdrv_open-update.patch
Patch61: 0037-qapi-qmp_marshal_-renames-for-pve-monitor-commands.patch
Patch62: 0038-qapi-qmp_mashal_-renames-for-async-snapshot.patch
Patch63: 0039-qapi-qmp_mashal_-renames-for-get_link_status.patch
Patch64: 0040-vnc-make-x509-imply-tls-again.patch
Patch65: 0041-PVE-VNC-authentication.patch
Patch66: 0042-vma-writer-don-t-bail-out-on-zero-length-files.patch
Patch67: 0043-vma-better-driver-guessing-for-bdrv_open.patch
Patch68: 0044-block-add-the-zeroinit-block-driver-filter.patch
Patch69: 0045-vma-add-format-option-to-device-mapping.patch
Patch70: 0046-pve-cleanup-includes-all-over-the-place.patch
Patch71: 0047-zeroinit-bdrv_get_block_status-got-a-new-param.patch
Patch72: 0048-BDRV_O_CACHE_WB-was-removed.patch
Patch73: 0049-backup-bdrv_set_enable_write_cache-is-no-more.patch
Patch74: 0050-fix-possible-unitialised-return-value.patch
Patch75: 0051-net-NET_CLIENT_OPTIONS_KIND_MAX-changed.patch
Patch76: 0052-vnc-refactor-to-QIOChannelSocket.patch
Patch77: 0053-vma-use-BlockBackend-on-extract.patch
Patch78: 0054-rbd-disable-rbd_cache_writethrough_until_flush-with-.patch
Patch79: 0055-enable-cache-unsafe-for-vma-extract_content-and-qmp_.patch
Patch80: 0056-qmp_snapshot_drive-add-aiocontext.patch
Patch81: CVE-2016-6490-virtio-check-vring-descriptor-buffer-length.patch
Patch82: CVE-2016-7155-scsi-check-page-count-while-initialising-descriptor-.patch
Patch83: CVE-2016-7156-scsi-pvscsi-avoid-infinite-loop-while-building-SG-li.patch
Patch84: CVE-2016-7157-scsi-mptconfig-fix-an-assert-expression.patch
Patch85: CVE-2016-7170-vmsvga-correct-bitmap-and-pixmap-size-checks.patch
Patch86: CVE-2016-7421-scsi-pvscsi-limit-process-IO-loop-to-ring-size.patch
Patch87: CVE-2016-7423-scsi-mptsas-use-g_new0-to-allocate-MPTSASRequest-obj.patch
Patch88: x86-lapic-Load-LAPIC-state-at-post_load.patch

%set_verify_elf_method fhs=relaxed

#set_gcc_version 4.7
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
BuildArch: noarch
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

%prep
%setup -n %rname-kvm
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
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1

cp -f %SOURCE2 qemu-kvm.control.in

%build
export CFLAGS="%optflags"
# non-GNU configure
./configure \
	--target-list='%target_list_system %target_list_user' \
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
	--audio-drv-list="%audio_drv_list" \
	--disable-xen \
	--disable-brlapi \
	--enable-curl \
	--enable-fdt \
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
	%{subst_enable vhdx} \
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
	--enable-xfsctl

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

install -D -m 0644 %SOURCE8 %buildroot/lib/udev/rules.d/%rulenum-%rname-guest-agent.rules
install -D -m 0644 %SOURCE9 %buildroot%_unitdir/%rname-guest-agent.service
install -D -m 0755 %SOURCE10 %buildroot%_initdir/%rname-guest-agent

%if_enabled vnc_sasl
install -D -p -m 0644 qemu.sasl %buildroot%_sysconfdir/sasl2/%rname.conf
%endif

%find_lang %rname

rm -f %buildroot%_datadir/%rname/slof.bin
#rm -f %buildroot%_datadir/*/openbios*
rm -f %buildroot%_datadir/%rname/pxe*rom
rm -f %buildroot%_datadir/%rname/efi*rom
rm -f %buildroot%_datadir/%rname/vgabios*bin
rm -f %buildroot%_datadir/%rname/bios.bin
rm -f %buildroot%_datadir/%rname/bios-256k.bin
rm -f %buildroot%_datadir/%rname/acpi-dsdt.aml
rm -f %buildroot%_datadir/%rname/q35-acpi-dsdt.aml
#rm -f %buildroot%_datadir/%name/sgabios.bin
#rm -f %buildroot%_datadir/%name/petalogix-s3adsp1800.dtb
#rm -f %buildroot%_datadir/%name/video.x
#rm -f %buildroot%_datadir/%name/bamboo.dtb
#rm -f %buildroot%_datadir/%name/ppc_rom.bin
rm -f %buildroot%_datadir/%rname/s390-ccw.img

# the pxe ipxe images will be symlinks to the images on
# /usr/share/ipxe, as QEMU doesn't know how to look
# for other paths, yet.

for rom in e1000 ne2k_pci pcnet rtl8139 virtio ; do
  ln -r -s %buildroot%_datadir/ipxe/pxe-${rom}.rom %buildroot%_datadir/%rname/pxe-${rom}.rom
  ln -r -s %buildroot%_datadir/ipxe.efi/efi-${rom}.rom %buildroot%_datadir/%rname/efi-${rom}.rom
done

for bios in vgabios vgabios-cirrus vgabios-qxl vgabios-stdvga vgabios-vmware vgabios-virtio ; do
  ln -r -s %buildroot%_datadir/seavgabios/${bios}.bin %buildroot%_datadir/%rname/${bios}.bin
done

ln -r -s %buildroot%_datadir/seabios/{bios,bios-256k}.bin %buildroot%_datadir/%rname/
ln -r -s %buildroot%_datadir/seabios/{acpi-dsdt,q35-acpi-dsdt}.aml %buildroot%_datadir/%rname/

install -Dp -m 0644 %SOURCE11 %buildroot%_datadir/kvm/OVMF_CODE-pure-efi.fd
install -m 0644 %SOURCE12 %buildroot%_datadir/kvm/OVMF_VARS-pure-efi.fd

mkdir -p %buildroot/lib/binfmt.d
for i in dummy \
%ifnarch %{ix86} x86_64
    qemu-i386 \
%endif
%ifnarch alpha
    qemu-alpha \
%endif
%ifnarch %{arm}
    qemu-arm \
%endif
    qemu-armeb \
    qemu-cris \
    qemu-microblaze qemu-microblazeel \
%ifnarch mips
    qemu-mips qemu-mips64 \
%endif
%ifnarch mipsel
    qemu-mipsel qemu-mips64el \
%endif
%ifnarch m68k
    qemu-m68k \
%endif
%ifnarch ppc ppc64
    qemu-ppc qemu-ppc64abi32 qemu-ppc64 \
%endif
%ifnarch sparc sparc64
    qemu-sparc qemu-sparc32plus qemu-sparc64 \
%endif
%ifnarch s390 s390x
    qemu-s390x \
%endif
%ifnarch sh4
    qemu-sh4 \
%endif
    qemu-sh4eb \
; do
  test $i = dummy && continue
  grep /$i:\$ %SOURCE1 > %buildroot/lib/binfmt.d/$i.conf
  chmod 644 %buildroot/lib/binfmt.d/$i.conf
done < %SOURCE1

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

%files

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

%files user
%_bindir/qemu-*
/lib/binfmt.d/qemu-*.conf
%exclude %_bindir/qemu*system*
%exclude %_bindir/qemu-kvm
%exclude %_bindir/qemu-img
%exclude %_bindir/qemu-io
%exclude %_bindir/qemu-nbd
%exclude %_bindir/qemu-ga

%files img
%_bindir/qemu-img
%_bindir/qemu-io
%_bindir/qemu-nbd
%_bindir/virtfs-proxy-helper
%_man1dir/virtfs-proxy-helper.*
%_libexecdir/qemu-bridge-helper

%files guest-agent
%_bindir/qemu-ga
/lib/udev/rules.d/%rulenum-%rname-guest-agent.rules
%_unitdir/%rname-guest-agent.service
%_initdir/%rname-guest-agent

#files doc
#docdir/
#exclude %docdir/LICENSE

%files aux
%dir %docdir/
%docdir/LICENSE

#files -n ivshmem-tools
#_bindir/ivshmem-client
#_bindir/ivshmem-server

%changelog
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
