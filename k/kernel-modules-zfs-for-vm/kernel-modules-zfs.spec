%define module_name zfs
%define module_version 2.4.2
%define module_release alt1

%define flavour for-vm
%define karch %ix86 x86_64 aarch64
BuildRequires(pre): kernel-headers-modules-for-vm

%setup_kernel_module %flavour

%define strip_mod_opts --strip-unneeded -R .comment
%define module_dir /lib/modules/%kversion-%flavour-%krelease/fs

Summary: ZFS Linux modules
Name: kernel-modules-%module_name-%flavour
%define ksname %module_name
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License:  CDDL-1.0
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: https://zfsonlinux.org/
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
%if "%flavour" != "talos"
Provides: zfs-kernel-module = %EVR
%endif

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

* Thu Jun 04 2026 Anton Farygin <rider@altlinux.org> 2.4.2-alt1
- 2.4.0 -> 2.4.2

* Sun Dec 21 2025 Anton Farygin <rider@altlinux.org> 2.4.0-alt1
- 2.3.5 -> 2.4.0

* Tue Nov 25 2025 Anton Farygin <rider@altlinux.com> 2.3.5-alt1
- 2.3.3 -> 2.3.5

* Wed Oct 29 2025 Maxim Slipenko <maks1ms@altlinux.org> 2.3.3-alt2
- Remove provides zfs-kernel-module

* Wed Aug 06 2025 Anton Farygin <rider@altlinux.com> 2.3.3-alt1
- 2.3.2 -> 2.3.3

* Mon May 12 2025 Anton Farygin <rider@altlinux.com> 2.3.2-alt1
- 2.3.1 -> 2.3.2

* Thu Mar 20 2025 Anton Farygin <rider@altlinux.ru> 2.3.1-alt2
- Added  virtual Provides zfs-kernel-module to allow module installation
  by name during other packages' build process.

* Tue Mar 18 2025 Anton Farygin <rider@altlinux.ru> 2.3.1-alt1
- 2.2.7 -> 2.3.1

* Wed Jan 15 2025 Anton Farygin <rider@altlinux.ru> 2.2.7-alt1
- 2.2.6 -> 2.2.7

* Thu Oct 17 2024 Anton Farygin <rider@altlinux.ru> 2.2.6-alt1
- 2.2.2 -> 2.2.6

* Wed Dec 27 2023 Anton Farygin <rider@altlinux.ru> 2.2.2-alt1
- 2.1.13 -> 2.2.2

* Wed Nov 01 2023 Anton Farygin <rider@altlinux.ru> 2.1.13-alt1
- 2.1.12 -> 2.1.13

* Sun Jun 11 2023 Anton Farygin <rider@altlinux.ru> 2.1.12-alt1
- 2.1.9 -> 2.1.12

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
