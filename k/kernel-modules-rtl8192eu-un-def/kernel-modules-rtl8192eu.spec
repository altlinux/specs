%define module_name	rtl8192eu
%define module_version	5.11.2.1
%define module_release	alt1

%define flavour		un-def
%define karch		%ix86 x86_64
BuildRequires(pre): kernel-headers-modules-un-def
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: Realtek rtl8192eu official Linux driver
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: MIT
Group: System/Kernel and hardware

Packager: Dmitry Terekhin <jqt4@altlinux.org>

ExclusiveOS: Linux
URL: https://github.com/clnhub/rtl8192eu-linux
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %karch

%description
This driver is based on the (latest) official Realtek v5.2.19.1 driver
with fixes and improvements to support the latest kernels.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
%make_build KSRC=%_usrsrc/linux-%kversion-%flavour

%install
install -d %buildroot%module_dir
install 8192eu.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Sat Apr 22 2023 Andrey Cherepanov <cas@altlinux.org> 5.2.19.1-alt2
- Removed patch for kernel 6.0+

* Wed Jul 10 2019 Dmitry Terekhin <jqt4@altlinux.org> 5.2.19.1-alt1
- Initial build
