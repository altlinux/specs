# SPDX-License-Identifier: GPL-2.0-only

Name: qa-qemu-vmlinuz
Summary: vmlinuz for QEMU tests from all arches
Version: 1
Release: alt1
License: GPL-2.0-only
Group: Other
BuildArch: noarch
Requires: qa-qemu-vmlinuz-aarch64
Requires: qa-qemu-vmlinuz-armh
Requires: qa-qemu-vmlinuz-i586
Requires: qa-qemu-vmlinuz-ppc64le
Requires: qa-qemu-vmlinuz-x86_64

%description
%summary.
This package is intended for QEMU CI tests.

%files

%changelog
* Thu Jan 12 2023 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- First version.
