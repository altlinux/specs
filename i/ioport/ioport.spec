# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: ioport
Version: 1.2
Release: alt1
Summary: Access PC I/O ports from command line
License: GPLv2+
Group: System/Kernel and hardware
Url: https://people.redhat.com/rjones/ioport/
Vcs:git://git.annexia.org/ioport.git

Source: %name-%version.tar

ExclusiveArch: %ix86 x86_64

BuildRequires: perl-Pod-Perldoc

%description
This package adds commands to access machine I/O ports directly.

%prep
%setup

%build
%add_optflags -Wextra -Werror -fanalyzer
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc COPYING README
%_bindir/*
%_man1dir/*

%changelog
* Fri Aug 12 2022 Vitaly Chikunov <vt@altlinux.org> 1.2-alt1
- First import 1.2 (2018-01-05).
