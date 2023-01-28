# SPDX-License-Identifier: GPL-2.0-only

Name: qa-qemu-vmlinuz
Summary: vmlinuz for QEMU tests from all arches
Version: 2
Release: alt1
License: GPL-2.0-only
Group: Other
BuildArch: noarch
Requires: kernel-qemu-requirer-un-def-aarch64
Requires: kernel-qemu-requirer-un-def-armh
Requires: kernel-qemu-requirer-un-def-i586
Requires: kernel-qemu-requirer-un-def-ppc64le
Requires: kernel-qemu-requirer-un-def-x86_64

%description
%summary.
This package is intended for QEMU CI tests.

%files

%changelog
* Fri Jan 27 2023 Vitaly Chikunov <vt@altlinux.org> 2-alt1
- Guarantee that kernels are kernel-image-un-def and not random flavour.

* Thu Jan 12 2023 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- First version.
