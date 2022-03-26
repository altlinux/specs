# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: sslscan
Version: 2.0.12
Release: alt1
Summary: sslscan tests SSL/TLS enabled services to discover supported cipher suites
License: GPL-3.0-or-later
Group: Networking/Other

Source: %name-%version.tar
BuildRequires: libssl-devel

%description
%summary

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%make_build CFLAGS="%optflags" DEFINES=-DVERSION='\"%version-%release\"'

%install
%makeinstall_std

%check
%buildroot%_bindir/sslscan --version

%files
%doc LICENSE README.md
%_bindir/sslscan
%_man1dir/sslscan.1.xz

%changelog
* Sat Mar 26 2022 Vitaly Chikunov <vt@altlinux.org> 2.0.12-alt1
- Update to 2.0.12 (2022-02-23).

* Wed Jun 02 2021 Vitaly Chikunov <vt@altlinux.org> 2.0.10-alt1
- First import of 2.0.10-4-g5224502 (2021-05-29).
