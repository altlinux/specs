# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: forkstat
Version: 0.03.00
Release: alt1
Summary: Process fork/exec/exit monitoring tool
License: GPL-2.0-or-later
Group: Monitoring
Url: https://github.com/ColinIanKing/forkstat

Source: %name-%version.tar

%description
Forkstat is a program that logs process fork(), exec() and exit()
activity. It is useful for monitoring system behaviour and to track down
rogue processes that are spawning off processes and potentially abusing
the system.

Note that forkstat uses the Linux netlink connector to gather process
activity and this may miss events if the system is overly busy. Netlink
connector also requires root privilege.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
export CFLAGS='%{optflags}'
%make_build

%install
%makeinstall_std

%files
%doc COPYING README.md
%_bindir/forkstat
%_man8dir/forkstat.*
%_datadir/bash-completion/completions/forkstat

%changelog
* Wed Dec 07 2022 Vitaly Chikunov <vt@altlinux.org> 0.03.00-alt1
- Update to V0.03.00 (2022-12-06).

* Wed May 18 2022 Vitaly Chikunov <vt@altlinux.org> 0.02.17-alt1
- First import V0.02.17 (2021-11-15).
