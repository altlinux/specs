%define module_name     ipt-so
%define module_version  1.0
%define module_release  alt9
%define flavour         std-def

%ifarch armh
# No KVM, no tests.
%def_without check
%endif

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
BuildRequires(pre): kernel-headers-modules-std-def
%if 0%{?!_without_check:%{?!_disable_check:1}}
BuildRequires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease
BuildRequires: rpm-build-vm-run
BuildRequires: iptables iproute2 iptables-devel
%endif
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Requires: %module_name = %module_version
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release
PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %ix86 x86_64 aarch64 ppc64le armh e2k e2kv4 e2kv5 e2kv6
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
PATH=/sbin:/usr/sbin:$PATH
timeout 60 \
vm-run '
	modprobe -a iptable_filter iptable_security ip_tables
	mount -t tmpfs tmpfs /run
	export XTABLES_LIBDIR=$PWD:/%_lib/iptables
	./tests.sh test
'

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
