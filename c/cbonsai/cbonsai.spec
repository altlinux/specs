# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: cbonsai
Version: 1.3.1
Release: alt1
Summary: grow bonsai trees in your terminal
License: GPL-2.0-only
Group: Other
Url: https://gitlab.com/jallbrit/cbonsai

Source: %name-%version.tar
BuildRequires: libncursesw-devel

%description
cbonsai is a bonsai tree generator, written in C using ncurses.
There are 2 modes of operation: intelligently creates, colors, and
positions a bonsai tree, and is entirely static (see finished bonsai
tree), and live (see growth step-by-step).

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%ifarch x86_64
%add_optflags -fanalyzer
%endif
export CFLAGS='%optflags'
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc LICENSE README.md
%_bindir/cbonsai
%_datadir/bash-completion/completions/cbonsai

%changelog
* Sat Oct 21 2023 Vitaly Chikunov <vt@altlinux.org> 1.3.1-alt1
- First import v1.3.1-10-g50fe627 (2023-01-25).
