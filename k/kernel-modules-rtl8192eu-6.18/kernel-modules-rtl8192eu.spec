%define module_name	rtl8192eu
%define module_version	5.11.2.3
%define module_release	alt1

%define flavour		6.18
%define karch		%ix86 x86_64 aarch64 ppc64le armh
BuildRequires(pre): kernel-headers-modules-6.18
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: Realtek rtl8192eu official Linux driver
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: MIT
Group: System/Kernel and hardware


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
This driver is based on the (latest) official Realtek v5.11.2.3 driver
with fixes and improvements to support the latest kernels.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
sed -i 's/__DATE__/"1970-01-01"/g; s/__TIME__/"00:00:00"/g' core/rtw_debug.c

%build
%make_build KSRC=%_usrsrc/linux-%kversion-%flavour \
%ifarch aarch64
            CONFIG_PLATFORM_ARM_AARCH64=y
%endif

%install
install -d %buildroot%module_dir
install 8192eu.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(LC_TIME=C date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Dec 16 2025 Danila Skachedubov <skachedubov@altlinux.org> 5.11.2.3-alt1
- New version
- Add support for kernel 6.19

* Sat Apr 22 2023 Andrey Cherepanov <cas@altlinux.org> 5.2.19.1-alt2
- Removed patch for kernel 6.0+

* Wed Jul 10 2019 Dmitry Terekhin <jqt4@altlinux.org> 5.2.19.1-alt1
- Initial build
