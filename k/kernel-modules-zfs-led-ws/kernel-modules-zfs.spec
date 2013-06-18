%define module_name zfs
%define module_version 0.6.1
%define module_release alt1

%define flavour led-ws
BuildRequires(pre): kernel-headers-modules-led-ws

%setup_kernel_module %flavour

%define strip_mod_opts --strip-unneeded -R .comment
%define module_dir /lib/modules/%kversion-%flavour-%krelease/extra

Summary: ZFS Linux modules
Name: kernel-modules-%module_name-%flavour
%define ksname %module_name
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2+
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: http://zfsonlinux.org
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-spl = %module_version
BuildRequires: kernel-source-%module_name = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease

Provides: kernel-modules-spl-%flavour = %version-%release
Provides: kernel-modules-spl-%kversion-%flavour-%krelease = %version-%release

ExclusiveArch: %karch

%description
ZFS is an advanced file system and volume manager which was originally developed
for Solaris and is now maintained by the Illumos community.
ZFS on Linux, which is also known as ZoL, is currently feature complete.
It includes fully functional and stable SPA, DMU, ZVOL, and ZPL layers.
This package contains ZFS Linux kernel modules.


%prep
%setup -cT
for i in spl %ksname; do
	tar -xf %kernel_src/$i-%module_version.tar*
done


%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
cd spl*
%configure --with-config=kernel --with-linux=%_usrsrc/linux-%kversion-%flavour
%make_build -C module
SPL_SRC_DIR="$PWD"
cd ../%{ksname}*
%configure --with-config=kernel --with-linux=%_usrsrc/linux-%kversion-%flavour --with-spl="$SPL_SRC_DIR"
%make_build -C module


%install
for d in spl* %{ksname}*; do
	%makeinstall_std -C $d/module %{!?_enable_debug:%{?strip_mod_opts:INSTALL_MOD_STRIP="%strip_mod_opts"}}
done


%files
%module_dir


%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Jun 18 2013 Led <led@altlinux.ru> 0.6.1-alt1
- initial build
