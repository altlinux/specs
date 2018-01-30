%define IF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define IF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define IF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define IF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"

%define module_name	rtl8723de
%define module_version	5.1.1.8
%define module_release alt5

%define flavour		std-def
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define norm_version	%kversion

%define module_dir /lib/modules/%kversion-%flavour-%krelease/net/wireless/realtek/rtlwifi/%module_name

Name: kernel-modules-%module_name-%flavour
Group: System/Kernel and hardware
Summary: Module for Realtek RTL8723DE
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
Url: https://github.com/smlinux/rtl8723de
License: GPLv2

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
ExclusiveArch: %karch

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease

BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
%IF_ver_lteq "%kversion" "4.10"
BuildRequires: kernel-source-%module_name-4.10down = %module_version
%else
BuildRequires: kernel-source-%module_name = %module_version
%endif

%description
These packages contain Realtek RTL8723DE module.

%prep
rm -rf kernel-source-%module_name-%module_version
tar xvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
make ARCH=%base_arch CROSS_COMPILE= KSRC=%_usrsrc/linux-%kversion-%flavour modules

%install
install -D -m 644 8723de.ko %buildroot/%module_dir/rtl8723de.ko

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Jan 09 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt5
- use other sources branch for old kernels

* Tue Jan 09 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt4
- fix build requires

* Tue Jan 09 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt3
- fix build requires

* Tue Jan 09 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt2
- fix build requires

* Tue Jan 09 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt1
- initial build
