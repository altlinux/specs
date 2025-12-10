%define module_name     ipt-so
%define module_version  1.0
%define module_release  alt10
%define flavour         6.18

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: Iptables match for Security Options (IPSO) Labels (kernel module)
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
Url: https://github.com/vt-alt/ipt-so/

BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-6.18
%if 0%{?!_without_check:%{?!_disable_check:1}}
BuildRequires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease
BuildRequires: figlet
BuildRequires: iproute2
BuildRequires: iptables
BuildRequires: iptables-devel
BuildRequires: rpm-build-vm-run
%endif
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Requires: %module_name = %module_version
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release
PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %ix86 x86_64 aarch64 ppc64le armh
ExclusiveOS: Linux

%description
Iptables match for Security Options (IPSO) Labels (kernel module).

%prep
rm -rf %module_name-%module_version
tar xf %kernel_src/kernel-source-%module_name-%module_version.tar*
%setup -D -T -n %module_name-%module_version

%build
make -C %_usrsrc/linux-%kversion-%flavour-%krelease M=$(pwd) modules VERSION=%version-%release
%{?!_without_check:%{?!_disable_check:make}}

%install
install -m644 -D xt_so.ko %buildroot/%module_dir/xt_so.ko

%files
%module_dir

%check
VERSION=%version ./check.sh

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Wed Dec 10 2025 Vitaly Chikunov <vt@altlinux.org> 1.0-alt10
- spec: check: Improve tests run.
