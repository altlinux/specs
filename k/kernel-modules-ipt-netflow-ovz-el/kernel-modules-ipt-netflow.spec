%define module_name	ipt-netflow
%define module_version	1.7.1
%define module_release	alt1

%define kversion       2.6.32
%define krelease       alt71
%define flavour        ovz-el

%define module_dir /lib/modules/%kversion-%flavour-%krelease/kernel/net/ipv4/netfilter/

Summary:	ipt_NETFLOW linux 2.6 kernel module
Name:		kernel-modules-%module_name-%flavour
Version:	1.0.%module_version
Release:	%module_release.132640.71
License:	GPL
Group:		System/Kernel and hardware

Packager:       Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS:	Linux
URL:		sourceforge.net/projects/ipt-netflow/
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-headers-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

BuildRequires: iptables iptables-devel

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Prereq:		coreutils
Prereq:         kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease

ExclusiveArch:  %ix86 x86_64

%description
Ipt-netflow is very fast and effective Netflow exporting module
for Linux kernel (up to 2.6.37). Designed for Linux router with
heavy network load.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
./configure \
        --kver="%kversion" \
        --kdir="%_usrsrc/linux-%kversion-%flavour" \
        #
%make_build all

%install
mkdir -p $RPM_BUILD_ROOT/%module_dir
install -p -m644 ipt_NETFLOW.ko $RPM_BUILD_ROOT/%module_dir

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* Wed Jun 27 2012 Anton Protopopov <aspsk@altlinux.org> 1.0.1.7.1-alt1.132640.71
- Build for kernel-image-ovz-el-2.6.32-alt71.

* Thu May 26 2011 Anton Protopopov <aspsk@altlinux.org> 1.0.1.7.1-alt1
- Initial build for ALT
