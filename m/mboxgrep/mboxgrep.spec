# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: mboxgrep
Version: 0.7.10
Release: alt1
Summary: displays e-mail messages matching a pattern
License: GPL-2.0-or-later
Group: Text tools
Url: https://mboxgrep.datatipp.se/
Vcs: https://git.datatipp.se/dspiljar/mboxgrep

Source: %name-%version.tar

BuildRequires: libpcre-devel

%define valgrind_arches %ix86 x86_64
%{?!_without_check:%{?!_disable_check:
%ifarch %valgrind_arches
BuildRequires: /proc
BuildRequires: valgrind
%endif
BuildRequires: strace
}}

%description
mboxgrep is a small utility that scans a mailbox for messages matching
a regular expression. Found messages can be either displayed on standard
output, counted, deleted, piped to a shell command or written to another
mailbox.

%prep
%setup

%build
%ifarch %ix86 x86_64
%add_optflags -fanalyzer -Wno-analyzer-malloc-leak
%endif
%add_optflags %(getconf LFS_CFLAGS) -Wno-unused-result -Wno-unused-but-set-variable
%configure
%make_build

%install
%makeinstall

%define _customdocdir %_docdir/%name

%check
%ifarch %valgrind_arches
%define valgrind valgrind --error-exitcode=2
%else
%define valgrind time
%endif
PATH=%buildroot%_bindir:$PATH
%valgrind src/mboxgrep --no-duplicates . .gear/mbox > out
sha256sum out | grep 98176f5973129e0a8b26a9986ed21cea14187096096bd5ea950d2eaf19e1ade2
strace -v -o log mboxgrep --no-duplicates . .gear/mbox > out
# Check that mbox-to-stdout hardening is enabled.
 grep '^prlimit.*RLIMIT_NPROC.*rlim_max=0}' log
 grep '^prlimit.*RLIMIT_NOFILE.*rlim_max=0}' log

%files
%doc COPYING.md INSTALL NEWS README.md ChangeLog
%_bindir/mboxgrep
%_infodir/%name.info*
%_man1dir/%name.1*

%changelog
* Sun Feb 05 2023 Vitaly Chikunov <vt@altlinux.org> 0.7.10-alt1
- First import 0.7.10-0-g0649ac9 (2023-02-04).
