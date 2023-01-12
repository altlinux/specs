# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%global __find_debuginfo_files %nil
%set_verify_elf_method skip

Name: qa-qemu-vmlinuz-%_arch
Summary: vmlinuz from %_arch for QEMU tests
Version: 1
Release: alt1
License: GPL-2.0-only
Group: Other
AutoReqProv: no

# xarch: aarch64 armh x86_64 i586 ppc64le
ExclusiveArch: ppc64le
BuildArch: noarch
BuildRequires: kernel > 6
BuildRequires: rpm-build-kernel-perms

%description
%summary.
This package is intended for QEMU CI tests.

%install
install -Dpm644 /boot/vmlinuz-* -t %buildroot/%_libexecdir/qemu-vmlinuz/%_arch/
%brp_strip_none %_libexecdir/qemu-vmlinuz/*

%files
%_libexecdir/qemu-vmlinuz

%changelog
* Thu Jan 12 2023 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- First version.
