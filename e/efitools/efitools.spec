# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: efitools
Version: 1.9.2
Release: alt3
Summary: UEFI secure boot toolkit
Group: Development/Other
License: GPL-2.0-only
Url: https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git
# Doc: https://blog.hansenpartnership.com/the-meaning-of-all-the-uefi-keys/
# Doc: https://blog.hansenpartnership.com/uefi-secure-boot/

Source: %name-%version.tar
Patch3500: alt-loongarch64.patch
ExcludeArch: ppc64le
BuildRequires: gnu-efi
BuildRequires: help2man
BuildRequires: openssl
BuildRequires: openssl-devel
BuildRequires: perl-File-Slurp
BuildRequires: sbsigntools

%description
Useful tools for manipulating UEFI secure boot platforms.

%prep
%setup
%patch3500 -p1

%build
%make_build

%install
%makeinstall_std DOCDIR=%buildroot%_docdir/%name-%version

%files
%doc README COPYING
%_bindir/*
%_datadir/efitools
%_man1dir/*.1*

%changelog
* Tue May 07 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.9.2-alt3
- NMU: fixed FTBFS on LoongArch.

* Wed Feb 17 2021 Vitaly Chikunov <vt@altlinux.org> 1.9.2-alt2
- Fix ALT beekeeper rebuild failures.

* Sat Feb 13 2021 Vitaly Chikunov <vt@altlinux.org> 1.9.2-alt1
- First import of v1.9.2 (2019-01-08).
