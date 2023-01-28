# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%global __find_debuginfo_files %nil
%set_verify_elf_method skip

%define kflavour un-def

Name: kernel-qemu-requirer-%kflavour-%_arch
Summary: vmlinuz (%kflavour) from %_arch for QEMU tests
Version: 2
Release: alt1
License: GPL-2.0-only
Group: Other
AutoReqProv: no

# xarch: aarch64 armh x86_64 i586 ppc64le
ExclusiveArch: aarch64
BuildArch: noarch
BuildRequires: kernel-image-%kflavour
BuildRequires: rpm-build-kernel-perms
# /usr/src/in/srpm/qa-qemu-vmlinuz-x86_64-2-alt1.src.rpm: forbidden dependencies: kernel-image-un-def
# sisyphus_check: check-deps ERROR: package dependencies violation
# hsh-rebuild: qa-qemu-vmlinuz-x86_64-2-alt1.src.rpm: sisyphus_check failed.

%description
%summary.
This package is intended for QEMU CI tests only.

Package is weirdly named with 'kernel-' prefix to allow
   BuildRequires: kernel-image-%kflavour
to pass sisyphus_check.

%install
install -Dpm644 /boot/vmlinuz-* -t %buildroot/%_libexecdir/qemu-vmlinuz/%_arch/
%brp_strip_none %_libexecdir/qemu-vmlinuz/*

%files
%_libexecdir/qemu-vmlinuz

%changelog
* Fri Jan 27 2023 Vitaly Chikunov <vt@altlinux.org> 2-alt1
- Rename and do flavoured BR: kernel-image-un-def.

* Thu Jan 12 2023 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- First version.
