%define module_name             e1000e
%define module_version          3.8.7
%define module_release          alt3
%define flavour                 std-def
%define karch                   %ix86 x86_64

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/updates
%add_verify_elf_skiplist %module_dir/*

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: E1000E Driver for e1000 Intel(R) Ethernet adapter
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
URL: https://sourceforge.net/projects/e1000

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
%if 0%{?!_without_check:%{?!_disable_check:1}}
BuildRequires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease
%else
%def_without check
%endif

Requires: dmsetup
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

# To remove /etc/modprobe.d/blacklist-e1000e.conf
Conflicts: kernel-modules-e1000e-std-def <= 3.8.7-alt1
Conflicts: kernel-modules-e1000e-un-def <= 3.8.7-alt1

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
Linux kernel drivers for e1000 Intel(R) Ethernet adapter.
To learn more about Intel Ethernet visit http://communities.intel.com/community/tech/wired

%prep
rm -rf kernel-source-%module_name-%module_version
tar xf %kernel_src/kernel-source-%module_name-%module_version.tar*
%setup -D -T -n kernel-source-%module_name-%module_version

%build
cd src
%make_build CFLAGS_EXTRA=-DCONFIG_E1000E_SEPARATE_TX_HANDLER \
            KSRC=%_usrsrc/linux-%kversion-%flavour-%krelease \
            KBUILD=%_usrsrc/linux-%kversion-%flavour         \
            M=$(pwd)

%install
install -d %buildroot/%module_dir
install -m644 -D src/%module_name.ko %buildroot/%module_dir/%module_name.ko

# Warning about the conflicted module version
%triggerpostun -- kernel-modules-e1000e-std-def <= 3.8.7-alt1
if [ "$2" -gt 0 ]; then
        echo "Warning! Conflicted e1000e module for std-def kernel flavor removed."
        echo "Do not forget to manually install e1000e kernel modules for all the needed kernel flavours if you need them."
fi

%triggerpostun -- kernel-modules-e1000e-un-def <= 3.8.7-alt1
if [ "$2" -gt 0 ]; then
        echo "Warning! Conflicted e1000e module for un-def kernel flavor removed."
        echo "Do not forget to manually install e1000e kernel modules for all the needed kernel flavours if you need them."
fi

%files
%module_dir/*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
