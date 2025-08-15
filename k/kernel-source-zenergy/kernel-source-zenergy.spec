# -*- rpm-spec -*-
%define module_name	zenergy
%define module_version  1.0
%define git f77293f

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: alt1.g%{git}
Provides: kernel-source-%module_name-%module_version
Summary: Based on AMD_ENERGY driver, but with some jiffies added so non-root users can read it safely
License: GPLv2
Group: Development/Kernel
Url: https://github.com/BoukeHaarsma23/zenergy
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%version.tar

BuildPreReq: kernel-build-tools
BuildArch: noarch

%description
The Energy driver exposes the energy counters that are reported via the Running
Average Power Limit (RAPL) Model-specific Registers (MSRs) via the hardware
monitor (HWMON) sysfs interface.

1. Power, Energy and Time Units MSR_RAPL_POWER_UNIT/ C001_0299: shared with all
   cores in the socket

2. Energy consumed by each Core MSR_CORE_ENERGY_STATUS/ C001_029A: 32-bitRO,
   Accumulator, core-level power reporting

3. Energy consumed by Socket MSR_PACKAGE_ENERGY_STATUS/ C001_029B: 32-bitRO,
   Accumulator, socket-level power reporting, shared with all cores in socket

These registers are updated every 1ms and cleared on reset of the system.

Note: If SMT is enabled, Linux enumerates all threads as cpus. Since, the
energy status registers are accessed at core level, reading those registers
from the sibling threads would result in duplicate values. Hence, energy
counter entries are not populated for the siblings.

%prep
%setup -c -q

%install
mkdir -p %kernel_srcdir
tar jcf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%doc %name-%version/README.md %name-%version/LICENSE
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Fri Aug 15 2025 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt1.gf77293f
- GIT f77293f.
- Added fix for kernel 6.16+.
