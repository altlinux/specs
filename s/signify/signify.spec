# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: signify
Version: 32
Release: alt1
Summary: OpenBSD tool to sign and verify signatures on files
License: ISC
Group: File tools
Url: https://flak.tedunangst.com/post/signify
# Url: https://www.openbsd.org/papers/bsdcan-signify.html
Vcs: https://github.com/openbsd/src
# Base Vcs: https://github.com/aperezdc/signify

Source: %name-%version.tar
BuildRequires: libbsd-devel

%description
A portable version of the OpenBSD tool to sign and verify signatures on
files using Ed25519 signature with SHA256 checksums.

Note: The signatures aren't compatible with GnuPG/OpenPGP.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%make_build CFLAGS="%optflags"

%install
%makeinstall_std PREFIX=%_prefix

%check
%make_build check

%files
%define _customdocdir %_docdir/%name
%doc CHANGELOG.md COPYING README.md
%_bindir/signify
%_man1dir/signify.1*

%changelog
* Sat Jul 05 2025 Vitaly Chikunov <vt@altlinux.org> 32-alt1
- First import of v32-5-gaa90571 with update from OpenBSD tree.
