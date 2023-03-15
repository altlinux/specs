%define module_name     rtw89
%define module_version  0.0
%define module_release  alt4.git.4f3464d

%define flavour         un-def
%define karch %ix86 x86_64 aarch64 ppc64le armh
BuildRequires(pre): kernel-headers-modules-un-def
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: Realtek RTL8852AE driver kernel module.
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL-2.0
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
URL: https://github.com/lwfinger/rtw89
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
Realtek RTL8852AE driver kernel module.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour modules M=`pwd`

%install
install -d %buildroot%module_dir
install rtw*.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Mar 14 2023 Anton Farygin <rider@altlinux.ru> 0.0-alt4.git.4f3464d
- update to 4f3464d

* Fri Mar 10 2023 Anton Farygin <rider@altlinux.ru> 0.0-alt3.git.fce040c
- update to fce040c

* Fri Dec 30 2022 Anton Farygin <rider@altlinux.ru> 0.0-alt2.git.e834edf
- update to  e834edf

* Fri Aug 13 2021 Nikolai Kostrigin <nickel@altlinux.org> 0.0-alt1.git.250c6f4
- Initial build for Sisyphus
