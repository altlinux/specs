%define module_name	it87
%define git %nil
%define module_version	2.0
%define module_release	alt2

%define flavour		6.12
%define karch %ix86 x86_64

BuildRequires(pre): kernel-headers-modules-6.12
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/updates

Summary: %module_name kernel module
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: https://github.com/frankcrawford/it87
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version-alt2

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %EVR

Obsoletes: %module_name-blacklist <= %EVR

%requires_kimage

ExclusiveArch: x86_64

%description
This driver implements support for the IT8603E, IT8620E, IT8622E, IT8623E,
IT8628E, IT8705F, IT8712F, IT8716F, IT8718F, IT8720F, IT8721F, IT8726F, IT8728F,
IT8732F, IT8758E, IT8771E, IT8772E, IT8781F, IT8782F, IT8783E/F, IT8786E,
IT8790E, and SiS950 chips.

These chips are 'Super I/O chips', supporting floppy disks, infrared ports,
joysticks and other miscellaneous stuff. For hardware monitoring, they
include an 'environment controller' with 3 temperature sensors, 3 fan
rotation speed sensors, 8 voltage sensors, associated alarms, and chassis
intrusion detection.

%prep
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
if [ -n "%flavour" -a "%flavour" == 'lks-wks' ]; then
echo 'got wks flavour, applying llvm macros'
%setup_llvm_env
fi
%make_build EXTRA_CFLAGS=-DIT87_DRIVER_VERSION='\"%version-%release\"' -C %_usrsrc/linux-%kversion-%flavour M=`pwd` V=1 modules

%install
install -pDm644 %module_name.ko %buildroot%module_dir/%module_name.ko

%files
%defattr(644,root,root,755)
%module_dir/%module_name.ko*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Nov 02 2026 L.A. Kostis <lakostis@altlinux.org> 2.0-alt2
- Get rid of -blacklist dependency (use /updates dir).
- karch: make x86_only.

* Fri Oct 23 2026 L.A. Kostis <lakostis@altlinux.org> 2.0-alt1
- 2.0.

* Fri Oct 24 2025 L.A. Kostis <lakostis@altlinux.org> 1.0-alt3.g60d9def
- karch: set to x86 and x86_64 only.

* Fri Oct 24 2025 L.A. Kostis <lakostis@altlinux.org> 1.0-alt2.g60d9def
- GIT 60d9def.

* Fri Aug 08 2025 L.A. Kostis <lakostis@altlinux.org> 1.0-alt1.g4bff981
- Initial build for Sisyphus.
