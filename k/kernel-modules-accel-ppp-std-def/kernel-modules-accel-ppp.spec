%define module_name             accel-ppp
%define module_version          1.8.0
%define module_release          alt1

%define flavour		std-def
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/ipoe

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Linux Kernel drivers support IPoE for accel-ppp
License: GPLv2
Group: System/Kernel and hardware
Url: http://sourceforge.net/projects/accel-ppp/

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel cmake
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
%module_name kernel driver support IPoE for accel-ppp

%prep
rm -rf %module_name-%module_version
tar -jxvf %kernel_src/%module_name-%module_version.tar.bz2
%setup -D -T -n %module_name-%module_version

%build
%cmake \
      -DKDIR=%_usrsrc/linux-%kversion-%flavour \
      -DBUILD_IPOE_DRIVER=TRUE \
      ..

make -C BUILD/drivers/ipoe

%install
install -d %buildroot/%module_dir
install -m644 -D BUILD/drivers/ipoe/driver/ipoe.ko %buildroot/%module_dir/ipoe.ko


%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Fri May 09 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt1
- 1.8.0 release

* Mon Apr 14 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt0.beta.1
- Initial build for Sisuphus
