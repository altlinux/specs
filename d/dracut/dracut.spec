# SPDX-License-Identifier: GPL-2.0-or-later

%define _unpackaged_files_terminate_build 1
%define dracutlibdir %prefix/lib/dracut
%define bash_completion_dir %(pkg-config --variable=completionsdir bash-completion)
%def_enable documentation

# We ship a .pc file but don't want to have a dep on pkg-config. We
# strip the automatically generated dep here and instead co-own the
# directory.
%filter_from_requires /pkg-config/d
%filter_from_requires /^\/usr\/share\/pkgconfig/d

Name: dracut
Version: 111
Release: alt1

Summary: Initramfs generator using udev
Group: System/Base

# The entire source code is GPLv2+
# except install/* which is LGPLv2+
# except util/* which is GPLv2
License: GPLv2+ and LGPLv2+ and GPLv2

Vcs: https://github.com/dracut-ng/dracut-ng.git
Url: https://github.com/dracut-ng/dracut-ng/wiki/

Source: %name-%version.tar

BuildRequires: bash >= 4
BuildRequires: git-core
BuildRequires: pkgconfig(libkmod) >= 23
BuildRequires: pkgconfig(libsystemd) >= 257

BuildRequires: systemd-devel
BuildRequires: bash-completion

%if_enabled documentation
BuildRequires: docbook-style-xsl docbook-dtds xsltproc
BuildRequires: asciidoctor xsltproc
%endif

Provides: dracut-ng = %EVR
Requires: systemd-filesystem
Requires: bash >= 4
Requires: coreutils
Requires: cpio
Requires: filesystem >= 3
Requires: findutils
Requires: grep
Requires: kmod
Requires: sed
Requires: xz
Requires: gzip
Requires: pigz

Requires: util-linux >= 2.21
Requires: udev >= 219
Requires: hardlink
Requires: kpartx
Requires: procps
AutoReq: noshell, noshebang

%description
dracut contains tools to create bootable initramfses for the Linux
kernel. Unlike previous implementations, dracut hard-codes as little
as possible into the initramfs. dracut contains various modules which
are driven by the event-based udev. Having root on MD, DM, LVM2, LUKS
is supported as well as NFS, iSCSI, NBD, FCoE with the dracut-network
package.

%package network
Summary: Dracut modules to build a dracut initramfs with network support
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
Requires: iputils
Requires: iproute
Requires: curl
AutoReq: noshell, noshebang

%description network
This package requires everything which is needed to build a generic
all purpose initramfs with network support with dracut.

%package network-manager
Summary: Dracut modules to build a dracut initramfs with network manager
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
Requires: NetworkManager
AutoReq: noshell, noshebang

%description network-manager
This package requires everything which is needed to build a generic
all purpose initramfs with NetworkManager dracut module.

%package caps
Summary: Dracut modules to build a dracut initramfs which drops capabilities
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
Requires: libcap-utils
AutoReq: noshell, noshebang

%description caps
This package requires everything which is needed to build an
initramfs with dracut, which drops capabilities.

%package live
Summary: Dracut modules to build a dracut initramfs with live image capabilities
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
Requires: %name-network = %EVR
Requires: tar gzip coreutils bash dmsetup curl parted
#Requires: fuse ntfs-3g
AutoReq: noshell, noshebang

%description live
This package requires everything which is needed to build an
initramfs with dracut, with live image capabilities, like Live CDs.

%package config-generic
Summary: Dracut configuration to turn off hostonly image generation
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
AutoReq: noshell, noshebang

%description config-generic
This package provides the configuration to turn off the host specific initramfs
generation with dracut and generates a generic image by default.

%package config-rescue
Summary: Dracut configuration to turn on rescue image generation
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
AutoReq: noshell, noshebang

%description config-rescue
This package provides the configuration to turn on the rescue initramfs
generation with dracut.

%package tools
Summary: Dracut tools to build the local initramfs
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
AutoReq: noshell, noshebang

%description tools
This package contains tools to assemble the local initrd and host configuration.

%package squash
Summary: Dracut module to build an initramfs with most files in a squashfs image
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
Requires: squashfs-tools
AutoReq: noshell, noshebang

%description squash
This package provides a dracut module to build an initramfs, but store most files
in a squashfs image, result in a smaller initramfs size and reduce runtime memory
usage.

%package fips
Summary: Dracut modules to build a dracut initramfs with an integrity check
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
Requires: libkcapi-fipscheck
Requires: libkcapi-hmaccalc
AutoReq: noshell, noshebang

%description fips
This package requires everything which is needed to build an
initramfs with dracut, which does an integrity check of the kernel
and its cryptography during startup.

%package ima
Summary: Dracut modules to build a dracut initramfs with IMA
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
#Requires: evmctl
Requires: keyutils
AutoReq: noshell, noshebang

%description ima
This package requires everything which is needed to build an
initramfs (using dracut) which tries to load an IMA policy during startup.

%prep
%setup

%build
%configure \
    --systemdsystemunitdir=%_unitdir \
    --bashcompletiondir=%bash_completion_dir \
    --libdir=%prefix/lib

%make_build DRACUT_VERSION=%version DRACUT_FULL_VERSION=%version

%install
%makeinstall_std \
    libdir=%prefix/lib enable_test=no DRACUT_FULL_VERSION=%version-%release

# Cleanup
rm -frv -- %buildroot%dracutlibdir/modules.d/11fips
rm -frv -- %buildroot%dracutlibdir/modules.d/11fips-crypto-policies
rm -frv -- %buildroot%dracutlibdir/dracut.conf.d/fips

# we do not support dash in the initramfs
rm -frv -- %buildroot%dracutlibdir/modules.d/10dash

# with systemd IMA and selinux modules do not make sense
rm -frv -- %buildroot%dracutlibdir/modules.d/75securityfs
rm -frv -- %buildroot%dracutlibdir/modules.d/76masterkey
rm -frv -- %buildroot%dracutlibdir/modules.d/77integrity
rm -frv -- %buildroot%dracutlibdir/dracut.conf.d/ima

%ifnarch s390 s390x
# remove architecture specific modules
rm -frv -- %buildroot%dracutlibdir/modules.d/68cms
rm -frv -- %buildroot%dracutlibdir/modules.d/69cio_ignore
rm -frv -- %buildroot%dracutlibdir/modules.d/73zipl
rm -frv -- %buildroot%dracutlibdir/modules.d/74dasd
rm -frv -- %buildroot%dracutlibdir/modules.d/74dasd_mod
rm -frv -- %buildroot%dracutlibdir/modules.d/74dasd_rules
rm -frv -- %buildroot%dracutlibdir/modules.d/74dcssblk
rm -frv -- %buildroot%dracutlibdir/modules.d/74zfcp
rm -frv -- %buildroot%dracutlibdir/modules.d/74znet
%else
rm -frv -- %buildroot%dracutlibdir/modules.d/10warpclock
%endif
%ifnarch ppc ppc64
rm -frv -- %buildroot%dracutlibdir/modules.d/70ppcmac
%endif

rm -fv -- %buildroot%dracutlibdir/dracut.conf.d/test*
rm -fv -- %buildroot%dracutlibdir/dracut.conf.d/*.example

mkdir -p %buildroot/boot/dracut
mkdir -p %buildroot/%_var/lib/dracut/overlay
mkdir -p %buildroot%_logdir
touch %buildroot%_logdir/dracut.log
mkdir -p %buildroot%_sharedstatedir/initramfs

rm -fv %buildroot%_mandir/man?/*suse*

echo 'hostonly="no"' > %buildroot%dracutlibdir/dracut.conf.d/02-generic-image.conf
echo 'dracut_rescue_image="yes"' > %buildroot%dracutlibdir/dracut.conf.d/02-rescue.conf

%files
%doc README.md AUTHORS NEWS.md
%doc COPYING
%_bindir/dracut
%bash_completion_dir/dracut
%bash_completion_dir/lsinitrd
%_bindir/lsinitrd
%dir %dracutlibdir
%dir %dracutlibdir/modules.d
%dracutlibdir/dracut-functions.sh
%dracutlibdir/dracut-functions
%dracutlibdir/dracut-logger.sh
%dracutlibdir/dracut-initramfs-restore
%dracutlibdir/dracut-install
%dracutlibdir/dracut-util
%dracutlibdir/skipcpio
%config(noreplace) %_sysconfdir/dracut.conf
%dracutlibdir/dracut.conf.d/01-dist.conf
%dir %_sysconfdir/dracut.conf.d
%dir %dracutlibdir/dracut.conf.d
%dracutlibdir/dracut.conf.d/generic
%dracutlibdir/dracut.conf.d/hostonly
%dracutlibdir/dracut.conf.d/no-network
%dracutlibdir/dracut.conf.d/rescue

%_datadir/pkgconfig/dracut.pc

%if_enabled documentation
%_mandir/man8/dracut.8*
%_mandir/man8/*service.8*
%_mandir/man1/lsinitrd.1*
%_mandir/man7/dracut.kernel.7*
%_mandir/man7/dracut.cmdline.7*
%_mandir/man7/dracut.modules.7*
%_mandir/man7/dracut.bootup.7*
%_mandir/man5/dracut.conf.5*
%endif

%dracutlibdir/modules.d/10bash
%dracutlibdir/modules.d/10systemd
%ifnarch s390 s390x
%dracutlibdir/modules.d/10warpclock
%endif
#%dracutlibdir/modules.d/11fips
%dracutlibdir/modules.d/11systemd-ac-power
%dracutlibdir/modules.d/11systemd-ask-password
%dracutlibdir/modules.d/11systemd-bsod
%dracutlibdir/modules.d/11systemd-battery-check
%dracutlibdir/modules.d/11systemd-coredump
%dracutlibdir/modules.d/11systemd-creds
%dracutlibdir/modules.d/11systemd-hostnamed
%dracutlibdir/modules.d/11systemd-initrd
%dracutlibdir/modules.d/11systemd-integritysetup
%dracutlibdir/modules.d/11systemd-journald
%dracutlibdir/modules.d/11systemd-ldconfig
%dracutlibdir/modules.d/11systemd-modules-load
%dracutlibdir/modules.d/11systemd-pcrextend
%dracutlibdir/modules.d/11systemd-portabled
%dracutlibdir/modules.d/11systemd-pstore
%dracutlibdir/modules.d/11systemd-repart
%dracutlibdir/modules.d/11systemd-resolved
%dracutlibdir/modules.d/11systemd-sysext
%dracutlibdir/modules.d/11systemd-sysctl
%dracutlibdir/modules.d/11systemd-sysusers-service
%dracutlibdir/modules.d/11systemd-timedated
%dracutlibdir/modules.d/11systemd-timesyncd
%dracutlibdir/modules.d/11systemd-tmpfiles
%dracutlibdir/modules.d/11systemd-udevd
%dracutlibdir/modules.d/11systemd-veritysetup
%dracutlibdir/modules.d/13modsign
%dracutlibdir/modules.d/13rescue
%dracutlibdir/modules.d/14watchdog
%dracutlibdir/modules.d/14watchdog-modules
%dracutlibdir/modules.d/16dbus-broker
%dracutlibdir/modules.d/16dbus-daemon
%dracutlibdir/modules.d/16rngd
%dracutlibdir/modules.d/19dbus
%dracutlibdir/modules.d/20i18n
%dracutlibdir/modules.d/30convertfs
%dracutlibdir/modules.d/45drm
%dracutlibdir/modules.d/45simpledrm
%dracutlibdir/modules.d/45plymouth
%dracutlibdir/modules.d/68lvmmerge
%dracutlibdir/modules.d/68lvmthinpool-monitor
%dracutlibdir/modules.d/70bluetooth
%dracutlibdir/modules.d/70btrfs
%dracutlibdir/modules.d/70crypt
%dracutlibdir/modules.d/70crypt-lib
%dracutlibdir/modules.d/70devicetree-firmware
%dracutlibdir/modules.d/70dm
%dracutlibdir/modules.d/70dmraid
%dracutlibdir/modules.d/70fs-lib
%dracutlibdir/modules.d/70kernel-modules
%dracutlibdir/modules.d/70kernel-modules-export
%dracutlibdir/modules.d/70kernel-modules-extra
%dracutlibdir/modules.d/70lvm
%dracutlibdir/modules.d/70mdraid
%dracutlibdir/modules.d/70memdisk
%dracutlibdir/modules.d/70multipath
%dracutlibdir/modules.d/70numlock
%dracutlibdir/modules.d/70nvdimm
%dracutlibdir/modules.d/70overlayfs
%ifarch ppc ppc64
%dracutlibdir/modules.d/70ppcmac
%endif
%dracutlibdir/modules.d/70pcmcia
%dracutlibdir/modules.d/70qemu
%dracutlibdir/modules.d/71overlayfs-crypt
%dracutlibdir/modules.d/71systemd-cryptsetup
%dracutlibdir/modules.d/73crypt-gpg
%dracutlibdir/modules.d/73crypt-loop
%dracutlibdir/modules.d/73fido2
%dracutlibdir/modules.d/74debug
%dracutlibdir/modules.d/73pcsc
%dracutlibdir/modules.d/73pkcs11
%dracutlibdir/modules.d/73tpm2-tss
%dracutlibdir/modules.d/74fstab-sys
%dracutlibdir/modules.d/74hwdb
%dracutlibdir/modules.d/74lunmask
%dracutlibdir/modules.d/74nvmf
%dracutlibdir/modules.d/74resume
%dracutlibdir/modules.d/74rootfs-block
%dracutlibdir/modules.d/74rootfs-block-fallback
%dracutlibdir/modules.d/74terminfo
%dracutlibdir/modules.d/74udev-rules
%dracutlibdir/modules.d/74virtfs
%dracutlibdir/modules.d/74virtiofs
%ifarch s390 s390x
%dracutlibdir/modules.d/69cio_ignore
%dracutlibdir/modules.d/73zipl
%dracutlibdir/modules.d/74dasd
%dracutlibdir/modules.d/74dasd_mod
%dracutlibdir/modules.d/74dcssblk
%dracutlibdir/modules.d/74zfcp
%endif
#%dracutlibdir/modules.d/75securityfs
%dracutlibdir/modules.d/76biosdevname
#%dracutlibdir/modules.d/76masterkey
%dracutlibdir/modules.d/76systemd-emergency
%dracutlibdir/modules.d/77dracut-systemd
%dracutlibdir/modules.d/77ecryptfs
%dracutlibdir/modules.d/77initqueue
#%dracutlibdir/modules.d/77integrity
%dracutlibdir/modules.d/77pollcdrom
%dracutlibdir/modules.d/77selinux
%dracutlibdir/modules.d/77syslog
%dracutlibdir/modules.d/77usrmount
%dracutlibdir/modules.d/78systemd-sysusers
%dracutlibdir/modules.d/80base
%dracutlibdir/modules.d/81busybox
%dracutlibdir/modules.d/84memstrack
%dracutlibdir/modules.d/85shell-interpreter
%dracutlibdir/modules.d/86shutdown
%attr(0644,root,root) %ghost %config(missingok,noreplace) %_logdir/dracut.log
%dir %_sharedstatedir/initramfs
%_unitdir/dracut-shutdown.service
%_unitdir/sysinit.target.wants/dracut-shutdown.service
%_unitdir/dracut-shutdown-onfailure.service
%_unitdir/dracut-cmdline.service
%_unitdir/dracut-initqueue.service
%_unitdir/dracut-mount.service
%_unitdir/dracut-pre-mount.service
%_unitdir/dracut-pre-pivot.service
%_unitdir/dracut-pre-trigger.service
%_unitdir/dracut-pre-udev.service
%_unitdir/initrd.target.wants/dracut-cmdline.service
%_unitdir/initrd.target.wants/dracut-initqueue.service
%_unitdir/initrd.target.wants/dracut-mount.service
%_unitdir/initrd.target.wants/dracut-pre-mount.service
%_unitdir/initrd.target.wants/dracut-pre-pivot.service
%_unitdir/initrd.target.wants/dracut-pre-trigger.service
%_unitdir/initrd.target.wants/dracut-pre-udev.service
%_kernel_installdir/50-dracut.install

%files network
%dracutlibdir/modules.d/10systemd-network-management
%dracutlibdir/modules.d/11systemd-networkd
%dracutlibdir/modules.d/35connman
%dracutlibdir/modules.d/40network
%dracutlibdir/modules.d/45net-lib
%dracutlibdir/modules.d/45systemd-import
%dracutlibdir/modules.d/45url-lib
%dracutlibdir/modules.d/70kernel-network-modules
%dracutlibdir/modules.d/70qemu-net
%dracutlibdir/modules.d/70uefi-lib
%dracutlibdir/modules.d/74cifs
%dracutlibdir/modules.d/74fcoe
%dracutlibdir/modules.d/74fcoe-uefi
%dracutlibdir/modules.d/74iscsi
%dracutlibdir/modules.d/74nbd
%dracutlibdir/modules.d/74nfs
%dracutlibdir/modules.d/74ssh-client
%ifarch s390 s390x
%dracutlibdir/modules.d/68cms
%dracutlibdir/modules.d/74znet
%dracutlibdir/modules.d/74zfcp
%endif

%files network-manager
%dracutlibdir/modules.d/35network-manager

%files caps
%dracutlibdir/modules.d/12caps

%files live
%dracutlibdir/modules.d/70dmsquash-live
%dracutlibdir/modules.d/70dmsquash-live-autooverlay
%dracutlibdir/modules.d/70dmsquash-live-ntfs
%dracutlibdir/modules.d/70img-lib
%dracutlibdir/modules.d/70livenet

%files tools
%if_enabled documentation
%doc %_man8dir/dracut-catimages.8*
%endif

%_bindir/dracut-catimages
%dir /boot/dracut
%dir %_var/lib/dracut
%dir %_var/lib/dracut/overlay

%files squash
%dracutlibdir/modules.d/74squash-erofs
%dracutlibdir/modules.d/74squash-squashfs
%dracutlibdir/modules.d/87squash
%dracutlibdir/modules.d/88squash-lib

%files config-generic
%dracutlibdir/dracut.conf.d/02-generic-image.conf

%files config-rescue
%dracutlibdir/dracut.conf.d/02-rescue.conf
%prefix/lib/kernel/install.d/51-dracut-rescue.install

#%files fips
#%config %_sysconfdir/dracut.conf.d/40-fips.conf
#%dracutlibdir/modules.d/01fips
#%dracutlibdir/dracut.conf.d/fips

#%files ima
#%config %_sysconfdir/dracut.conf.d/40-ima.conf
#%dracutlibdir/modules.d/96securityfs
#%dracutlibdir/modules.d/97masterkey
#%dracutlibdir/modules.d/98integrity
#%dracutlibdir/dracut.conf.d/ima

%changelog
* Fri Jun 26 2026 Alexey Shabalin <shaba@altlinux.org> 111-alt1
- 111

* Tue Dec 30 2025 Alexey Shabalin <shaba@altlinux.org> 109-alt1
- 109

* Wed Aug 20 2025 Alexey Shabalin <shaba@altlinux.org> 108-alt1
- 108
- Cherry-pick some commits from main branch.

* Tue May 20 2025 Alexey Shabalin <shaba@altlinux.org> 107-alt1
- 107

* Mon Apr 07 2025 Alexey Shabalin <shaba@altlinux.org> 106-alt1
- 106
- Cherry-pick some commits from main branch.

* Sat Nov 02 2024 Alexey Shabalin <shaba@altlinux.org> 105-alt1
- 105

* Sat Jul 20 2024 Alexey Shabalin <shaba@altlinux.org> 103-alt1
- 103

* Thu Jul 04 2024 Alexey Shabalin <shaba@altlinux.org> 102-alt1
- 102

* Thu May 23 2024 Alexey Shabalin <shaba@altlinux.org> 101-alt1
- 101
- Switch to new upstream https://github.com/dracut-ng/dracut-ng.git

* Sun Dec 10 2023 Alexey Shabalin <shaba@altlinux.org> 060-alt0.1
- 060 pre-release

* Fri Mar 24 2023 Alexey Shabalin <shaba@altlinux.org> 059-alt1
- 059

* Sat Jul 23 2022 Alexey Shabalin <shaba@altlinux.org> 057-alt1
- 057

* Wed Mar 23 2022 Alexey Shabalin <shaba@altlinux.org> 056-alt1
- 056

* Wed Aug 11 2021 Andrey Sokolov <keremet@altlinux.org> 055-alt3
- Move network-manager module to separate package (closes 40705)

* Fri Jul 30 2021 Andrey Sokolov <keremet@altlinux.org> 055-alt2
- Move url-lib module to network package, add dependency on curl (closes 40591)

* Mon May 31 2021 Alexey Shabalin <shaba@altlinux.org> 055-alt1
- 055

* Fri Mar 12 2021 Alexey Shabalin <shaba@altlinux.org> 053-alt1
- 053

* Fri Dec 18 2020 Alexey Shabalin <shaba@altlinux.org> 051-alt1
- 051

* Sun Nov 08 2020 Alexey Shabalin <shaba@altlinux.org> 050-alt4.git.831e31
- Fixed path /usr/lib/udev -> /lib/udev

* Sat Nov 07 2020 Alexey Shabalin <shaba@altlinux.org> 050-alt3.git.831e31
- Install dracut, dracut-catimages, mkinitrd to sbindir
- Delete requires to systemd

* Sat Nov 07 2020 Alexey Shabalin <shaba@altlinux.org> 050-alt2.git.831e31
- Update to upstream master snapshot
- Update spec
- Disable autoreq for shell scripts

* Wed Mar 18 2020 Vitaly Chikunov <vt@altlinux.org> 050-alt1
- Initial import into ALT.
- Based on dracut native spec.
