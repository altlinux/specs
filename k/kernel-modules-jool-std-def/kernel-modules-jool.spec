%define module_name             jool
%define module_version          3.4.5
%define module_release          alt2

%define flavour		std-def
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/jool

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Linux Kernel drivers support NAT64 for Jool
License: GPLv3
Group: System/Kernel and hardware
Url: https://www.jool.mx/

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
%module_name kernel driver support NAT64 for jool

%prep
rm -rf %module_name-%module_version
tar -jxvf %kernel_src/%module_name-%module_version.tar.bz2
%setup -D -T -n %module_name-%module_version

%build
pushd mod
subst "s,\${MODULES_DIR}/build,%_usrsrc/linux-%kversion-%flavour,g" stateful/Makefile
subst "s,\${MODULES_DIR}/build,%_usrsrc/linux-%kversion-%flavour,g" stateless/Makefile
make
popd

%install
install -d %buildroot/%module_dir
install -m644 -D mod/stateful/jool.ko %buildroot/%module_dir/jool.ko
install -m644 -D mod/stateless/jool_siit.ko %buildroot/%module_dir/jool_siit.ko

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Sep 20 2016 Alexei Takaseev <taf@altlinux.org> 3.4.5-alt1
- 3.4.5

* Tue Jul 12 2016 Alexei Takaseev <taf@altlinux.org> 3.4.4-alt1
- 3.4.4

* Thu May 12 2016 Alexei Takaseev <taf@altlinux.org> 3.4.3-alt1
- 3.4.3

* Mon Nov 23 2015 Alexei Takaseev <taf@altlinux.org> 3.4.2-alt1
- 3.4.2

* Thu Nov 12 2015 Alexei Takaseev <taf@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Oct 27 2015 Alexei Takaseev <taf@altlinux.org> 3.3.5-alt1
- 3.3.5

* Tue Sep 22 2015 Alexei Takaseev <taf@altlinux.org> 3.3.4-alt1
- 3.3.4

* Wed Sep 02 2015 Alexei Takaseev <taf@altlinux.org> 3.3.3-alt1
- Initial build for ALT Linux Sisyphus
