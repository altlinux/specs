%define module_name bbswitch
%define module_version 0.4.1

%define module_release alt2

%define kversion 3.4.4
%define krelease alt1
%define flavour un-def

%define base_arch %(echo %_target_cpu | sed 's/i.86/i386/;s/athlon/i386/')

%define module_dir /lib/modules/%kversion-%flavour-%krelease/acpi

Summary: bbswitch module
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.197636.1
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: https://github.com/Bumblebee-Project/bbswitch.git

BuildRequires(pre): rpm-build-kernel
BuildRequires: perl
BuildRequires: rpm >= 4.0.2-75
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Provides: %module_name

Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %ix86 x86_64

Requires: %module_name

%description
bbswitch is a kernel module which automatically detects the required
ACPI calls for two kinds of Optimus laptops. It has been verified to
work with "real" Optimus and "legacy" Optimus laptops (at least, that is
how I call them). The machines on which these tests has performed are:

- Clevo B7130 - GT 425M ("real" Optimus, Lekensteyns laptop)
- Dell Vostro 3500 - GT 310M ("legacy" Optimus, Samsagax' laptop)

(note: there is no need to add more supported laptops here as the universal
calls should work for every laptop model supporting either Optimus calls)

It's preferred over manually hacking with the acpi_call module because it can
detect the correct handle preceding _DSM and has some built-in safeguards.

%prep
rm -rf %module_name-%{module_version}*
tar xf %kernel_src/%module_name-%module_version.tar.*
%setup -D -T -n %module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour-%krelease/gcc_version.inc
make KDIR=%_usrsrc/linux-%kversion-%flavour-%krelease

%install
%__mkdir_p %buildroot/%module_dir
%__install -pD -m644 %module_name.ko \
    %buildroot%module_dir/

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease
%files
%defattr(644,root,root,755)
%module_dir

%changelog
* Mon Jun 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.1-alt2.197636.1
- Build for kernel-image-un-def-3.4.4-alt1.

* Thu Jan 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt2.197122.1
- rebuilt for 3.2.2

* Tue Jan 24 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1.197121.2
- first build

