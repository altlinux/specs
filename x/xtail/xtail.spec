# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: xtail
Version: 2.1
Release: alt1
Summary: Like "tail -f", but works on truncated files, directories, more
Group: System/Base
License: MIT
# License reference: https://unicom.crosenthal.com/sw/license
# Url(historical): http://www.unicom.com/sw/xtail
Url: https://unicom.crosenthal.com/sw/xtail
# Url: https://tracker.debian.org/pkg/xtail
# Vcs: https://salsa.debian.org/debian/xtail.git

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS) -D_FORTIFY_SOURCE=3 -fstack-protector-strong -fstack-clash-protection
%autoreconf
%configure
%make_build

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
%makeinstall prefix=%buildroot install

%files
%_bindir/xtail
%_man1dir/xtail.*

%changelog
* Thu May 26 2022 Vitaly Chikunov <vt@altlinux.org> 2.1-alt1
- First import debian/2.1-8-5-g6c3aeef (2021-10-09).
