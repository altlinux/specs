# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: cdecl
Version: 18.7.2
Release: alt1
Epoch: 1
Summary: Composing and deciphering C (or C++) declarations or casts
License: GPL-3.0-or-later
Group: Development/C
Url: https://github.com/paul-j-lucas/cdecl/

Source: %name-%version.tar
BuildRequires: flex
BuildRequires: libncurses-devel
BuildRequires: libreadline-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: /dev/pts
}}

%description
cdecl (see-deh-kull) is a program primarily for composing and deciphering
C (or C++) declarations or casts, aka "gibberish." It can be used
interactively on a terminal or accept input from either the command line
or standard input.

%prep
%setup

%build
mkdir .git # Mark maintainer tree to find flex.
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rename completions completion %buildroot%_datadir/bash-completions

%check
%buildroot%_bindir/cdecl --version | grep -Fx '%name %version'
script -e -c 'make check' /dev/null ||
	{ cat test/test-suite.log; exit 1; }

%files
%doc AUTHORS COPYING ChangeLog NEWS README*
%_bindir/c*decl
%_man1dir/c*decl.1*
%_datadir/bash-completion/completions/_%name
%_datadir/zsh/site-functions/_%name

%changelog
* Sat Apr 04 2026 Vitaly Chikunov <vt@altlinux.org> 1:18.7.2-alt1
- First import cdecl-18.7.2 (2026-03-01).
