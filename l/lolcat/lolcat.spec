# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: lolcat
Version: 1.2
Release: alt1
Summary: High-performance implementation of a colorful cat
License: WTFPL
Group: Text tools
Url: https://github.com/jaseg/lolcat

Source: %name-%version.tar

%description
%summary.

This lolcat clone is an attempt to reduce the world's carbon dioxide
emissions by optimizing inefficient code. It's >10x as fast and <0.1%%
as large as the original one.

%prep
%setup

%build
%make_build CFLAGS='%optflags %(getconf LFS_CFLAGS)'

%install
mkdir -p %buildroot%_bindir
%make_install DESTDIR=%buildroot%_bindir install

%files
%doc README.md LICENSE
%_bindir/lolcat
%_bindir/censor

%changelog
* Sat Apr 02 2022 Vitaly Chikunov <vt@altlinux.org> 1.2-alt1
- First import v1.2-2-g1a32b1a (2021-10-14).
