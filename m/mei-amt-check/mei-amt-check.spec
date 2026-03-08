# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: mei-amt-check
Version: 20180507
Release: alt1
Summary: Check whether AMT is enabled and provisioned under Linux
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://github.com/mjg59/mei-amt-check

Source: %name-%version.tar

%description
A simple tool that tells you whether AMT is enabled and provisioned on
Linux systems. Requires that the mei_me driver (part of the upstream
kernel) be loaded.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS) -W
%make_build CFLAGS="%optflags"

%install
install -Dp mei-amt-check -t %buildroot%_bindir

%files
%doc LICENSE README.md
%_bindir/mei-amt-check

%changelog
* Sun Mar 08 2026 Vitaly Chikunov <vt@altlinux.org> 20180507-alt1
- First import ec921d1 (2018-05-07) + PR19 (2025-12-16).
