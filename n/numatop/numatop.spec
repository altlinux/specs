# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: numatop
Version: 2.4
Release: alt1
Summary: An observation tool for runtime memory locality characterization and analysis on a NUMA system
License: BSD-3-Clause
Group: System/Kernel and hardware
Url: https://github.com/intel/numatop
ExclusiveArch: x86_64 ppc64le

Source: %name-%version.tar
BuildRequires: libcheck-devel
BuildRequires: libnuma-devel
BuildRequires: libncursesw-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: rpm-build-vm
}}

%description
numatop is an observation tool for runtime memory locality
characterization and analysis of processes and threads running on a NUMA
system. It helps the user to characterize the NUMA behavior of processes
and threads and to identify where the NUMA-related performance bottlenecks
reside. The tool uses hardware performance counter sampling technologies
and associates the performance data with Linux system runtime information
to provide real-time analysis in production systems.

%prep
%setup
# warning: "_FORTIFY_SOURCE" redefined
sed -i 's/-D_FORTIFY_SOURCE=2//' Makefile.am

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
# https://github.com/intel/numatop/issues/88
vm-run %make_build check VERBOSE=1

%files
%doc AUTHORS COPYING README.md SECURITY.md
%_bindir/numatop
%_man8dir/numatop.8*

%changelog
* Sat Sep 07 2024 Vitaly Chikunov <vt@altlinux.org> 2.4-alt1
- First import v2.4-46-g15c81a8 (2024-08-26).
