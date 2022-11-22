# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: kdumpid
Version: 1.3
Release: alt1
Summary: Identify any kernel core dump file
License: GPL-2.0-or-later
Group: Development/Kernel
Url: https://kdumpid.sourceforge.io/
Vcs: https://git.code.sf.net/p/kdumpid/code

Source: %name-%version.tar
BuildRequires: binutils-devel
BuildRequires: libkdumpfile-devel
BuildRequires: zlib-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: rpm-build-vm
}}

%description
The kdumpid utility can be used to find out the exact kernel architecture and
version of an unknown kernel core dump.

This utility should provide a fast and reliable method to find out the most
important information about an unknown kernel crash dump, such as the
architecture and kernel release. Think of it as a kind of "file" utility for
kernel dumps.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%make_build CUSTOM_CFLAGS="%optflags"

%install
%makeinstall_std BINDIR=%_bindir MANDIR=%_mandir

%ifarch %ix86 x86_64 ppc64le aarch64
# armh does not have /proc/kcore
%check
vm-run --kvm=cond ./kdumpid -v /proc/kcore
%endif

%files
%doc README.markdown
%_bindir/kdumpid
%_man1dir/*.1*

%changelog
* Tue Nov 22 2022 Vitaly Chikunov <vt@altlinux.org> 1.3-alt1
- First import v1.3-3-gbeb8ea6 (2022-08-16).
