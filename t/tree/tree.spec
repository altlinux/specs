# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: tree
Version: 2.1.1
Release: alt2
Epoch: 1

Summary: List contents of directories in a tree-like format
Group: File tools
License: GPL-2.0-or-later
URL: http://mama.indstate.edu/users/ice/tree/
Vcs: https://gitlab.com/OldManProgrammer/unix-tree
# Vcs: https://github.com/Old-Man-Programmer/tree
Source: %name-%version.tar

%description
Tree is a recursive directory listing program that produces a depth
indented listing of files, which is colorized ala dircolors if the
LS_COLORS environment variable is set and output is to tty.

%prep
%setup

%build
%ifnarch %e2k
# unsupported as of lcc 1.26.21
%add_optflags -fanalyzer
%endif
# Upstream have LDFLAGS=-s causing binaries to be stripped.
%make_build CFLAGS="%optflags %(getconf LFS_CFLAGS)" LDFLAGS=

%install
install -Dpm755 -t %buildroot%_bindir  tree
install -Dpm644 -t %buildroot%_man1dir doc/tree.1

%check
cd %buildroot
.%_bindir/tree

%files
%doc LICENSE CHANGES README
%_bindir/tree
%_man1dir/tree.1*

%changelog
* Mon Dec 18 2023 Michael Shigorin <mike@altlinux.org> 1:2.1.1-alt2
- E2K: avoid lcc-unsupported option

* Thu Jul 13 2023 Vitaly Chikunov <vt@altlinux.org> 1:2.1.1-alt1
- Update to 2.1.1 (2023-05-30).
- spec: %%changelog clean-up.

* Fri Oct 14 2022 Vitaly Chikunov <vt@altlinux.org> 1:2.0.4-alt1
- Update to 2.0.4 (2022-09-06).

* Fri Feb 25 2022 Vitaly Chikunov <vt@altlinux.org> 1:2.0.2-alt1
- Change upstream (Steve Baker) and update to 2.0.2 (2022-02-16).
