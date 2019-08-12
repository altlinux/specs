# SPDX-License-Identifier: GPL-2.0-only
#
# spec file to build rpm-build-vm
#
# Copyright (C) 2019 Vitaly Chikunov <vt@altlinux.org>
#

Name: rpm-build-vm
Version: 1.0
Release: alt2

Summary: RPM helper to run in virtualised environment
License: GPL-2.0
Group: Development/Other
Source0: %name-%version.tar

# /proc is required for qemu 9p to work, otherwise you'll get
# confusing ENOENT when creating a file. This is because
# `qemu/hw/9pfs/9p-local.c:fchmodat_nofollow' is doing chmod
# over `/proc/self/fd/%%d'.
Requires: /proc

%ifarch %ix86 x86_64
Requires: qemu-system-x86-core
%endif
%ifarch ppc64le
Requires: qemu-system-ppc-core
%endif
%ifarch aarch64
Requires: qemu-system-aarch64-core
%endif

# Try to load un-def kernel this way to avoid "forbidden dependencies"
# from sisyphus_check
Requires: kernel > 5.0

Requires: make-initrd
Requires: mount

%description
RPM helper to run QEMU inside of hasher. This is mainly intended
for %%check section to test softwares under better emulated root
than fakeroot.

%prep
%setup -q

%install
install -D -p -m 0755 vm-run      %buildroot%_bindir/vm-run
install -D -p -m 0755 vm-init     %buildroot%_sbindir/vm-init
install -D -p -m 0755 initrd-init %buildroot%_libexecdir/%name/sbin/init-bin
install -D -p -m 0755 config.mk   %buildroot%_libexecdir/%name/config.mk

%files
%_bindir/vm-run
%_sbindir/vm-init
%_libexecdir/%name/sbin/init-bin
%_libexecdir/%name/config.mk

%pre
# Only allow to install inside of hasher.
[ -d /.host -a -d /.in -a -d /.out ]

%post
# We don't have 9pnet_virtio and virtio_pci modules built-in in the kernel,
# so initrd is needed to preload them before mounting rootfs.
KERN=$(ls /boot/vmlinuz-*)
KVER=${KERN#/boot/vmlinuz-}
# Create /boot/initrd-$KVER.img
# This will take ~5 sec.
time make-initrd --no-checks --config=%_libexecdir/%name/config.mk --kernel=$KVER

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

%changelog
* Mon Aug 12 2019 Vitaly Chikunov <vt@altlinux.org> 1.0-alt2
- Improvements for ppc64le.

* Mon Aug 05 2019 Vitaly Chikunov <vt@altlinux.org> 1.0-alt1
- Initial version.

