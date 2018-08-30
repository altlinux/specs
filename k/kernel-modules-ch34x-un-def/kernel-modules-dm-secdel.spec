%define module_name     ch34x
%define module_version  20180821
%define module_release  alt1
%define flavour         un-def
%define karch x86_64 i586

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: Linux %module_name modules for CH340 serial to usb chip.
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-un-def
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
Linux %module_name modules for CH340 serial to usb chip.

%prep
rm -rf %module_name-%module_version
tar xf %kernel_src/kernel-source-%module_name-%module_version.tar*
%setup -D -T -n kernel-source-%module_name-%module_version

%build
make -C %_usrsrc/linux-%kversion-%flavour-%krelease M=$(pwd) modules

%install
install -d %buildroot/%module_dir
install -m644 -D ch34x.ko %buildroot/%module_dir/

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
