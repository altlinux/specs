%define module_name	ipt_netflow
%define module_version	2.6

%define module_release alt2

%define flavour		6.12
%define karch %ix86 x86_64 aarch64 ppc64le armh
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-6.12

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: Netflow iptables module for Linux kernel
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Patch0001: 1001-compat-Really-fix-__has_attribute-usage.patch
Patch0002: 1002-fix-detect-modularized-CONFIG_BRIDGE_NETFILTER.patch
Patch0003: 1003-fix-backward-compatible-building-with-kernel-5.3.patch
Patch0004: 1004-Fix-dkms-status-invocation.patch
Patch0005: 1005-Do-not-check-for-dkms-if-called-from-dkms.patch
Patch0006: 1006-Set-KDIR-early-if-called-from-dkms-and-get-version-f.patch
Patch0007: 1007-dkms.conf-Declare-BUILD_EXCLUSIVE_KERNEL_MIN-3.patch
Patch0008: 1008-Fix-module-build-for-Linux-v4.3.patch
Patch0009: 1009-Unexporting-find_module-has-been-backported-to-Linux.patch
Patch0010: 1010-compat-Linux-6.11-support.patch
Patch0011: 1011-Restore-ctl_table-backwards-compatibility.patch
Patch0012: 1012-Fix-module-build-for-Linux-v6.12.patch
Patch0013: 2001-physindev-has-been-replaced-by-physinif-in-Linux-v6..patch
Patch0014: cross.patch
Patch0015: disable-kernel-check.patch
Patch0016: dont-hardcode-current-gcc.patch
Patch0017: ignore-unknown-configure-options.patch
Patch0018: properly-pass-CPPFLAGS-and-LDFLAGS.patch
Patch0019: replace-strlcpy-by-strscpy.patch
Patch0020: use-get_random_u32_below-instead-of-deprecated-prand.patch
Patch0021: verbose.patch


ExclusiveOS: Linux
Url: http://sourceforge.net/projects/ipt-netflow/
BuildRequires(pre): rpm-build-kernel
BuildRequires: iptables-devel
BuildRequires: rpm >= 4.0.2-75
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
Ipt-netflow is very fast and effective Netflow exporting module for
Linux kernel. Designed for Linux router with heavy network load.
This is netfilter/iptables module adding support for NETFLOW target.

%prep
rm -rf %module_name-%{module_version}*
tar xf %kernel_src/%module_name-%module_version.tar.*
%setup -D -T -n %module_name-%module_version
%autopatch -p1

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
./configure --kdir=%_usrsrc/linux-%kversion-%flavour-%krelease --enable-macaddress --enable-vlan
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
