%define module_name             ixgbe
%define module_version          5.18.11
%define module_release          alt1

%define flavour std-def
%define karch x86_64 aarch64 ppc64le

BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/updates
%add_verify_elf_skiplist %module_dir/*

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Intel(R) 10GbE PCI Express Linux Network Driver
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: http://www.intel.com/network/connectivity/products/server_adapters.htm

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name

Patch1: allow-all-sfp.patch

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

# Due to /etc/modprobe.d/blacklist-ixgbe.conf
Conflicts: kernel-modules-ixgbe-std-def < 5.12.5-alt2
Conflicts: kernel-modules-ixgbe-un-def < 5.12.5-alt2

Requires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
%module_name contains the Intel(R) 10GbE PCI Express Linux Network Driver.

%prep
rm -rf %module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
%patch1 -p1

%build
pushd src
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build KSRC=%_usrsrc/linux-%kversion-%flavour
popd

%install
install -Dp -m600 src/%module_name.ko %buildroot/%module_dir/%module_name.ko

# Warning about the conflicted module version
%triggerpostun -- kernel-modules-ixgbe-std-def < 5.12.5-alt2
if [ "$2" -gt 0 ]; then
        echo "Warning! Conflicted ixgbe module for std-def kernel flavor removed."
        echo "Do not forget to manually install ixgbe kernel modules for all the needed kernel flavours if you need them."
fi

%triggerpostun -- kernel-modules-ixgbe-un-def < 5.12.5-alt2
if [ "$2" -gt 0 ]; then
        echo "Warning! Conflicted ixgbe module for un-def kernel flavor removed."
        echo "Do not forget to manually install ixgbe kernel modules for all the needed kernel flavours if you need them."
fi

%files
%module_dir/*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Wed Feb 15 2023 Alexei Takaseev <taf@altlinux.org> 5.18.11-alt1
- 5.18.11
- Change License: to GPL-2.0-only


* Tue Dec 20 2022 Alexei Takaseev <taf@altlinux.org> 5.18.6-alt1
- 5.18.6

* Mon Oct 17 2022 Alexei Takaseev <taf@altlinux.org> 5.17.1-alt1
- 5.17.1

* Fri Aug 05 2022 Alexei Takaseev <taf@altlinux.org> 5.16.5-alt1
- 5.16.5

* Mon May 23 2022 Alexei Takaseev <taf@altlinux.org> 5.15.2-alt1
- 5.15.2

* Mon Mar 14 2022 Alexei Takaseev <taf@altlinux.org> 5.14.6-alt1
- 5.14.6

* Thu Jan 20 2022 Alexei Takaseev <taf@altlinux.org> 5.13.4-alt2
- Fix build with kernel >= 5.15

* Wed Oct 20 2021 Alexei Takaseev <taf@altlinux.org> 5.13.4-alt1
- 5.13.4

* Sat Aug 28 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.12.5-alt3
- remove old modules to avoid ixgbe blacklisting

* Wed Aug 25 2021 Andrew A. Vasilyev <andy@altlinux.org> 5.12.5-alt2
- put module to "updates" directory, no blacklisting necessary

* Wed Jul 14 2021 Alexei Takaseev <taf@altlinux.org> 5.12.5-alt1
- 5.12.5

* Tue Mar 09 2021 Alexei Takaseev <taf@altlinux.org> 5.11.3-alt1
- 5.11.3

* Mon Feb 08 2021 Alexei Takaseev <taf@altlinux.org> 5.10.2-alt1
- 5.10.2
- Allow all vendors sfp+

* Thu Oct 01 2020 Alexei Takaseev <taf@altlinux.org> 5.9.4-alt1
- 5.9.4

* Wed Aug 19 2020 Alexei Takaseev <taf@altlinux.org> 5.8.1-alt1
- 5.8.1
- Build 64bit-only

* Thu May 21 2020 Alexei Takaseev <taf@altlinux.org> 5.7.1-alt1
- 5.7.1
- Added support for 5.6 kernel version

* Wed May 13 2020 Alexei Takaseev <taf@altlinux.org> 5.6.4-alt1
- 5.6.4
- Fix build with kernel >= 5.4

* Sat Nov 16 2019 Alexei Takaseev <taf@altlinux.org> 5.6.3-alt1
- initial build
