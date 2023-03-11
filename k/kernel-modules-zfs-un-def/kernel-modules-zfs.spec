%define module_name zfs
%define module_version 2.1.9
%define module_release alt1

%define flavour un-def
%define karch %ix86 x86_64 aarch64 ppc64le armh
BuildRequires(pre): kernel-headers-modules-un-def

%setup_kernel_module %flavour

%define strip_mod_opts --strip-unneeded -R .comment
%define module_dir /lib/modules/%kversion-%flavour-%krelease/fs

# The kernel 5.10 on powerpc has a GPL-only symbol mmu_feature_keys, which block build zfs with an error:
# ERROR: modpost: GPL-incompatible module zfs.ko uses GPL-only symbol 'mmu_feature_keys'
%if "%(rpmvercmp '%kversion' '5.10')" >= "0"
ExcludeArch: ppc64le %ix86
%endif

Summary: ZFS Linux modules
Name: kernel-modules-%module_name-%flavour
%define ksname %module_name
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License:  CDDL-1.0
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: http://zfsonlinux.org
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
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
rm -rf %module_name-%module_version
tar xvf %kernel_src/%module_name-%module_version.tar.*
%setup -D -T -n %module_name-%module_version

%build
%autoreconf
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
export CC="gcc${GCC_VERSION:+-$GCC_VERSION}"
%configure --with-config=kernel --with-linux=%_usrsrc/linux-%kversion-%flavour
%make_build -C module

%install
%makeinstall_std -C module \
	INSTALL_MOD_DIR=$(basename %module_dir) \
	%{!?_enable_debug:%{?strip_mod_opts:INSTALL_MOD_STRIP="%strip_mod_opts"}}

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Sat Mar 11 2023 Anton Farygin <rider@altlinux.ru> 2.1.9-alt1
- 2.1.7 -> 2.1.9

* Wed Jan 11 2023 Anton Farygin <rider@altlinux.ru> 2.1.7-alt1
- 2.1.6 -> 2.1.7

* Tue Oct 04 2022 Anton Farygin <rider@altlinux.ru> 2.1.6-alt1
- 2.1.5 -> 2.1.6

* Thu Sep 08 2022 Anton Farygin <rider@altlinux.ru> 2.1.5-alt1
- 2.1.4 -> 2.1.5

* Fri Apr 22 2022 Anton Farygin <rider@altlinux.ru> 2.1.4-alt1
- 2.1.2 -> 2.1.4

* Wed Jan 05 2022 Anton Farygin <rider@altlinux.ru> 2.1.2-alt1
- 2.1.1 -> 2.1.2

* Sat Nov 06 2021 Anton Farygin <rider@altlinux.ru> 2.1.1-alt1
- 2.1.0 -> 2.1.1

* Tue Aug 10 2021 Anton Farygin <rider@altlinux.ru> 2.1.0-alt1
- 2.0.4 -> 2.1.0

* Wed Mar 24 2021 Anton Farygin <rider@altlinux.org> 2.0.4-alt1
- 0.8.6 -> 2.0.4
