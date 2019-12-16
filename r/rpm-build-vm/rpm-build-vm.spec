# SPDX-License-Identifier: GPL-2.0-only
#
# spec file to build rpm-build-vm
#
# Copyright (C) 2019 Vitaly Chikunov <vt@altlinux.org>
#

Name: rpm-build-vm
Version: 1.4.1
Release: alt1

Summary: RPM helper to run in virtualised environment
License: GPL-2.0
Group: Development/Other

Source: %name-%version.tar

%ifarch %ix86 x86_64 ppc64le aarch64
# = QEMU supported arches =
# Other arches will get a stub which will always return success

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
RPM helper to run QEMU inside hasher. This is mainly intended
for %%check section to test software under better emulated root
than fakeroot.

This is similar to multiple vm scripts, virtme, vido, and eudyptula-boot.

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
install -D -p -m 0755 vm-run      %buildroot%_bindir/vm-run
install -D -p -m 0755 vm-init     %buildroot%_sbindir/vm-init
install -D -p -m 0755 initrd-init %buildroot%_libexecdir/%name/sbin/init-bin
install -D -p -m 0755 config.mk   %buildroot%_libexecdir/%name/config.mk

%files
%_bindir/vm-run
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

%else
# = QEMU un-supported arches =

%description
A stub package instead of RPM helper to run QEMU inside hasher
on supported architectures (this one (%_arch) is unsupported).

%prep
%setup

%install
install -D -p -m 0755 vm-run-stub %buildroot%_bindir/vm-run

%files
%_bindir/vm-run

# endif for QEMU un-supported arches
%endif

%files checkinstall

%pre checkinstall
set -ex
vm-run --verbose uname
vm-run --verbose --overlay=ext4 uname

%pre
# Only allow to install inside of hasher.
[ -d /.host -a -d /.in -a -d /.out ]

%changelog
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

