# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: fnotifystat
Version: 0.03.00
Release: alt1
Summary: Fnotifystat is a program that dumps the file system activity in a given period of time
License: GPL-2.0-or-later
Group: System/Kernel and hardware
Url: https://github.com/ColinIanKing/fnotifystat

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
CFLAGS="%optflags" %make_build

%install
%makeinstall_std

%files
%doc COPYING README.md
%_bindir/fnotifystat
%_man8dir/fnotifystat.8*
%_datadir/bash-completion/completions/fnotifystat

%changelog
* Sat Sep 07 2024 Vitaly Chikunov <vt@altlinux.org> 0.03.00-alt1
- First import V0.03.00-1-g3044254 (2024-08-02).
