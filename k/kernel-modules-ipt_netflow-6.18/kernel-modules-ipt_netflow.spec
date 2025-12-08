%define module_name	ipt_netflow
%define module_version	2.6

%define module_release alt3

%define flavour		6.18
%define karch %ix86 x86_64 aarch64 ppc64le armh
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-6.18

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: Netflow iptables module for Linux kernel
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
URL: https://github.com/nuclearcat/ipt-netflow
BuildRequires(pre): rpm-build-kernel
BuildRequires: iptables-devel
BuildRequires: rpm >= 4.0.2-75
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Requires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
Ipt-netflow is very fast and effective Netflow exporting module for
Linux kernel. Designed for Linux router with heavy network load.
This is netfilter/iptables module adding support for NETFLOW target.

%prep
rm -rf %module_name-%{module_version}*
tar xf %kernel_src/%module_name-%module_version.tar.*
%setup -D -T -n %module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
./configure --kdir=%_usrsrc/linux-%kversion-%flavour-%krelease \
            --enable-macaddress \
            --enable-vlan \
            --enable-promisc \
            --enable-natevents \
            --enable-direction \
            --enable-sample \
            --disable-dkms \
            --disable-dkms-install

make KDIR=%_usrsrc/linux-%kversion-%flavour-%krelease

%install
mkdir -p %buildroot/%module_dir
install ipt_NETFLOW.ko %buildroot/%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Dec 08 2025 Alexei Takaseev <taf@altlinux.org> 2.6-alt3
- Update to git:13a2b84bccdafea3ff84dab341dc2a14615adada
- Change URL
- Enable features: promisc, natevents, direction, sample
- Drop patches, all fixes on new upstream

* Mon Apr 14 2025 Alexei Takaseev <taf@altlinux.org> 2.6-alt2
- Update to git:0eb2092e930c78fc726d5d05abbcc81aa6c41b89
- Build with 6.12 fixed

* Tue Feb 10 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru>  2.1-alt1
- new version

* Wed Oct 22 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru>  2.0.1-alt1
- new version

* Fri Sep  6 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru>  1.8-alt3
- Build with 3.11 fixed

* Wed Jul 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru>  1.8-alt2
- Build with 3.10 fixed
