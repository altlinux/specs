# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: sbsigntools
Version: 0.9.4
Release: alt1
Summary: Signing utility for UEFI secure boot
License: GPL-3.0-or-later
Url: https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git
# Url(ccan): http://ccodearchive.net/
# Vcs(ccan): https://github.com/rustyrussell/ccan
Group: Development/Other

Source: %name-%version.tar

ExcludeArch: ppc64le
BuildRequires: binutils-devel
BuildRequires: gnu-efi
BuildRequires: help2man
BuildRequires: libuuid-devel
BuildRequires: openssl
BuildRequires: openssl-devel

%description
Tools to add signatures to EFI binaries and Drivers.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%doc README AUTHORS LICENSE.GPLv3 COPYING ChangeLog NEWS
%_bindir/sbattach
%_bindir/sbkeysync
%_bindir/sbsiglist
%_bindir/sbsign
%_bindir/sbvarsign
%_bindir/sbverify
%_man1dir/*.1*

%changelog
* Sat Feb 13 2021 Vitaly Chikunov <vt@altlinux.org> 0.9.4-alt1
- First import of v0.9.4 (2020-06-11) + update (2020-08-12).
