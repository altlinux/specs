%define module_name	anbox
%define module_version	14
%define git ae26ba2
%define module_release	alt2.g%{git}

%define flavour		std-def
%define karch %ix86 x86_64 aarch64 ppc64le armh
BuildRequires(pre): kernel-headers-modules-std-def
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: Anbox kernel modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2/GPLv3
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
URL: http://github.com/anbox/anbox-modules
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %EVR

PreReq: coreutils
PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
Requires: anbox-kernel-conf = %module_version
ExclusiveArch: %karch

%description
Anbox kernel modules necessary to run the Anbox Android container runtime.
They're split out of the original Anbox repository to make packaging in various
Linux distributions easier.

%prep
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
# ashmem required only for kernels <= 5.18
KMODULES='binder'
for module in $KMODULES; do
pushd "$module"
%make_build -C %_usrsrc/linux-%kversion-%flavour M=`pwd` V=1 modules
popd
done

%install
install -d %buildroot%module_dir
KMODULES='binder'
for module in $KMODULES; do
pushd "$module"
install *.ko %buildroot%module_dir
popd
done

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Thu Jun 01 2023 L.A. Kostis <lakostis@altlinux.org> 14-alt2.gae26ba2
- .spec: rename.
- now 6.3+ kernel compatible.

* Fri Mar 31 2023 L.A. Kostis <lakostis@altlinux.org> 14-alt1.gae26ba2
- Initial build for Sisyphus.
