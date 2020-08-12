# SPDX-License-Identifier: GPL-2.0-only
#
# spec file to build rpm-build-vm
#
# Copyright (C) 2019 Vitaly Chikunov <vt@altlinux.org>
#

Name: rpm-build-vm
Version: 1.13
Release: alt1

Summary: RPM helper to run in virtualised environment
License: GPL-2.0
Group: Development/Other

Source: %name-%version.tar

%define supported_arches %ix86 x86_64 ppc64le aarch64

%ifarch %supported_arches
# = QEMU supported arches =
# Other arches will get a stub which will always return success

# /proc is required for qemu 9p to work, otherwise you'll get
# confusing ENOENT when creating a file. This is because
# `qemu/hw/9pfs/9p-local.c:fchmodat_nofollow' is doing chmod
# over `/proc/self/fd/%%d'.
Requires: /proc
Requires: /dev/kvm

# Try to load un-def kernel this way to avoid "forbidden dependencies"
# from sisyphus_check
Requires: kernel > 5.0

Requires: make-initrd
Requires: mount
%endif

%ifarch %ix86 x86_64
Requires: qemu-system-x86-core
%endif
%ifarch ppc64le
Requires: qemu-system-ppc-core
%endif
%ifarch aarch64
Requires: qemu-system-aarch64-core
%endif

%description
RPM helper to run QEMU inside hasher. This is mainly intended
for %%check section to test software under better emulated root
than fakeroot.

This is similar to multiple vm scripts, virtme, vido, and eudyptula-boot.
%ifnarch %supported_arches

This package is a stub instead of RPM helper to run QEMU inside hasher
on supported architectures (this one (%_arch) is unsupported).
%endif

%package checkinstall
Summary: Checkinstall for vm-run
Group: Development/Other
BuildArch: noarch
PreReq: %name = %EVR

%description checkinstall
Run checkinstall tests for vm-run.

%prep
%setup

%install
%ifnarch %supported_arches
install -D -p -m 0755 vm-run-stub %buildroot%_bindir/vm-run
%else
install -D -p -m 0755 vm-run      %buildroot%_bindir/vm-run
install -D -p -m 0755 vm-init     %buildroot%_sbindir/vm-init
install -D -p -m 0755 initrd-init %buildroot%_libexecdir/%name/sbin/init-bin
install -D -p -m 0755 config.mk   %buildroot%_libexecdir/%name/config.mk
%endif

%pre
# Only allow to install inside of hasher.
[ -d /.host -a -d /.in -a -d /.out ]

%files checkinstall

%files
%_bindir/vm-run

%ifarch %supported_arches
%_sbindir/vm-init
%_libexecdir/%name

%post
# We don't have 9pnet_virtio and virtio_pci modules built-in in the kernel,
# so initrd is needed to preload them before mounting rootfs.

ls /boot/vmlinuz-* | while read KERN; do
	KVER=${KERN#/boot/vmlinuz-}
	echo "Generating initrd for $KERN"
	make-initrd --no-checks --config=%_libexecdir/%name/config.mk --kernel=$KVER
done
rm -rf /tmp/make-initrd.*

# Fix permissions to boot the installed kernel
(
  find /boot -type f,d -print0
  find /lib/modules -type f,d -print0
) | xargs -0r chmod a+rX

# Required in case of --udevd option to vm-run
mkdir -p /run/udev
chmod a+twx /run/udev

# Just in case
mkdir -p /run/dbus
chmod a+twx /run/dbus

# u&mount should to be readable
control mount unprivileged

# For --overlay=
chmod a+twx /mnt

# Allow user creation
chmod a+r /etc/login.defs
%endif

%pre checkinstall
set -ex
vm-run --verbose uname
vm-run --verbose --overlay=ext4 uname

%changelog
* Wed Aug 12 2020 Vitaly Chikunov <vt@altlinux.org> 1.13-alt1
- Make kernel shutdown quicker.

* Mon Aug 10 2020 Vitaly Chikunov <vt@altlinux.org> 1.12-alt1
- Make console output non-truncated on shutdown.
- Fix tty support for console.

* Sat Aug 08 2020 Vitaly Chikunov <vt@altlinux.org> 1.11-alt1
- x86_64,i586: Try to make kernel more robust with 'no_timer_check'.
- spec: Move checkinstall %%pre outside of %%ifarch to fix noarch check.

* Thu Jul 02 2020 Vitaly Chikunov <vt@altlinux.org> 1.10-alt1
- ppc: Use cap-ccf-assist=off for kvm-type=HV.

* Tue Jun 30 2020 Vitaly Chikunov <vt@altlinux.org> 1.9-alt1
- Propagate exported functions into vm subshell.

* Sat Jun 20 2020 Vitaly Chikunov <vt@altlinux.org> 1.8-alt1
- aarch64: Fix `.gic_version not found' (qemu).
- spec: Fix `different set of noarch packages' (girar).

* Mon Feb 24 2020 Vitaly Chikunov <vt@altlinux.org> 1.7-alt2
- Require /dev/kvm.

* Fri Jan 24 2020 Vitaly Chikunov <vt@altlinux.org> 1.7-alt1
- ppc: Make use of KVM.

* Thu Jan 23 2020 Vitaly Chikunov <vt@altlinux.org> 1.6-alt1
- Fix `Multiple devices detected in same VirtFS export' warning.

* Thu Jan 23 2020 Vitaly Chikunov <vt@altlinux.org> 1.5-alt1
- aarch64: Make use of KVM.

* Mon Dec 30 2019 Ivan A. Melnikov <iv@altlinux.org> 1.4.1-alt3
- Fix build on qemu-less architectures (closes: #37629).

* Sat Dec 28 2019 Vitaly Chikunov <vt@altlinux.org> 1.4.1-alt2
- Fix build on unsupported arches.

* Mon Dec 16 2019 Vitaly Chikunov <vt@altlinux.org> 1.4.1-alt1
- Quickfix of 1.4 (MAXMEM handling).

* Mon Dec 16 2019 Vitaly Chikunov <vt@altlinux.org> 1.4-alt2
- Optimize spec.
- Add checkinstall package.

* Mon Dec 16 2019 Vitaly Chikunov <vt@altlinux.org> 1.4-alt1
- Limit 32-bit system memory.

* Thu Dec 12 2019 Vitaly Chikunov <vt@altlinux.org> 1.3-alt1
- Initialize cpu and mem to the max, support share_network=1,
  handle multiple kernels using --kernel= option.

* Sat Aug 31 2019 Vitaly Chikunov <vt@altlinux.org> 1.2-alt1
- Improvements corresponding to v1.2.

* Mon Aug 19 2019 Vitaly Chikunov <vt@altlinux.org> 1.1-alt1
- Do not use `qemu' binary on x86 due to qemu repackage.

* Mon Aug 19 2019 Vitaly Chikunov <vt@altlinux.org> 1.0-alt5
- Make stub vm-run output a warning message

* Sun Aug 18 2019 Michael Shigorin <mike@altlinux.org> 1.0-alt4
- Rework to provide a stub package on qemu-unsupported arches
  (that can be added into BuildRequires: unconditionally).

* Thu Aug 15 2019 Vitaly Chikunov <vt@altlinux.org> 1.0-alt3
- Add ExclusiveArch for only supported arches.

* Mon Aug 12 2019 Vitaly Chikunov <vt@altlinux.org> 1.0-alt2
- Improvements for ppc64le.

* Mon Aug 05 2019 Vitaly Chikunov <vt@altlinux.org> 1.0-alt1
- Initial version.

