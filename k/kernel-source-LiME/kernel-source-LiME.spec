%define module_name LiME
%define module_version 1.9.1
%define module_release	alt5

Name: kernel-source-%module_name
Version: %module_version
Release: %module_release
Summary: External Linux kernel modules sources for LiME
License: GPLv2
Group: Development/Kernel
Url: https://github.com/504ensicsLabs/LiME
BuildArch: noarch

BuildRequires(pre): rpm-build-kernel
%{?!_without_check:%{?!_disable_check:
BuildRequires: kernel-headers-modules-%kernel_latest
BuildRequires: kernel-%kernel_latest
BuildRequires: rpm-build-vm
}}

Source0: %name-%version.tar.bz2
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

%description
%module_name Linux Memory Extractor module sources for Linux kernel.

%prep
%setup

%install
install -pDm0644 %_sourcedir/%name-%version.tar.bz2 -t %kernel_srcdir

%files
%_usrsrc/*

%check
# Testing here is convenient, but ignore the test result as it is
# supposed for kernel-modules build stage to match the flavour exactly.
./check.sh || true

%changelog
* Thu Apr 03 2025 Vitaly Chikunov <vt@altlinux.org> 1.9.1-alt5
- Add informational build/run tests in %%check and make them runnable at
  kernel-modules build.

* Wed Apr 02 2025 Paul Wolneykien <manowar@altlinux.org> 1.9.1-alt4
- Fixed Wint-conversion error on aarch64 (thx Vitaly Chikunov).

* Wed Apr 02 2025 Paul Wolneykien <manowar@altlinux.org> 1.9.1-alt3
- Updated to git@1f99bc6 from github.com/504ensicsLabs/LiME.

* Wed Dec 16 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.9.1-alt2
- compat with kernel 5.10

* Tue Oct 06 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.9.1-alt1
- 1.9.1

* Wed Jun 19 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.8.1-alt1
- 1.8.1 (kernels 4.14+ support)

* Tue Jul 11 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.7.8-alt1
- 1.7.6

* Wed Aug 24 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.7.5-alt1
- 1.7.5

* Tue Jan 20 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1-alt1
- initial build

