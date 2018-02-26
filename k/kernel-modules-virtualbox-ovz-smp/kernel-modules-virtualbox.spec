%define module_name	virtualbox
%define module_version	4.1.12

%define module_release	alt1

%define drv_module_name	vboxdrv
%define pci_module_name	vboxpci
%define net_module_name	vboxnetflt
%define net_module_adaptor_name	vboxnetadp

%define kversion	2.6.32
%define krelease	alt8
%define flavour		ovz-smp

%define base_arch %(echo %_target_cpu | sed 's/i.86/i386/;s/athlon/i386/')

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: VirtualBox modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.132640.8
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: http://www.virtualbox.org/
BuildRequires(pre): rpm-build-kernel
BuildPreReq: gcc-c++
BuildRequires: perl
BuildRequires: rpm >= 4.0.2-75
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%drv_module_name = %module_version
BuildRequires: kernel-source-%pci_module_name = %module_version
BuildRequires: kernel-source-%net_module_name = %module_version
BuildRequires: kernel-source-%net_module_adaptor_name = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %ix86 x86_64

Requires: %module_name-common

%description
This package contains VirtualBox modules (vboxdrv) that are needed
for VirtualBox to run. Note that you have to compile these modules on the
system with your VirtualBox version installed or you will have to specify
your VirtualBox version as `version' parameter when loading these modules
or in your /etc/modules.conf file.

%prep
%setup -T -c -n kernel-source-%module_name-%module_version
%__tar jxvf %kernel_src/kernel-source-%drv_module_name-%module_version.tar.bz2
%__tar jxvf %kernel_src/kernel-source-%pci_module_name-%module_version.tar.bz2
%__tar jxvf %kernel_src/kernel-source-%net_module_name-%module_version.tar.bz2
%__tar jxvf %kernel_src/kernel-source-%net_module_adaptor_name-%module_version.tar.bz2

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make -C kernel-source-%drv_module_name-%module_version \
    KERN_DIR=%_usrsrc/linux-%kversion-%flavour/
cp kernel-source-%drv_module_name-%module_version/Module.symvers \
    kernel-source-%pci_module_name-%module_version
%make -C kernel-source-%pci_module_name-%module_version \
    KERN_DIR=%_usrsrc/linux-%kversion-%flavour/
cp kernel-source-%drv_module_name-%module_version/Module.symvers \
    kernel-source-%net_module_name-%module_version
%make -C kernel-source-%net_module_name-%module_version \
    KERN_DIR=%_usrsrc/linux-%kversion-%flavour/
cp kernel-source-%drv_module_name-%module_version/Module.symvers \
    kernel-source-%net_module_adaptor_name-%module_version
%make -C kernel-source-%net_module_adaptor_name-%module_version \
    KERN_DIR=%_usrsrc/linux-%kversion-%flavour/

%install
%__mkdir_p %buildroot/%module_dir
%__install -pD -m644 kernel-source-%drv_module_name-%module_version/vboxdrv.ko \
    %buildroot%module_dir/
%__install -pD -m644 kernel-source-%pci_module_name-%module_version/vboxpci.ko \
    %buildroot%module_dir/
%__install -pD -m644 kernel-source-%net_module_name-%module_version/vboxnetflt.ko \
    %buildroot%module_dir/
%__install -pD -m644 kernel-source-%net_module_adaptor_name-%module_version/vboxnetadp.ko \
    %buildroot%module_dir/

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* Wed Apr 04 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.12-alt1.132640.8
- Build for kernel-image-ovz-smp-2.6.32-alt8.

* Tue Apr 03 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.12-alt1
- Update to new release

* Sun Apr 01 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.10-alt1
- Update to new release with 3.2 kernel support

* Sat Jan 14 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.6-alt2
- fix to build with 3.2 kernel

* Fri Dec 02 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.6-alt1
- Update to new release

* Sun Oct 30 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.4-alt1
- Update to new release

* Wed Sep 21 2011 Anton Protopopov <aspsk@altlinux.org> 4.0.12-alt2
- Technical

* Mon Jul 25 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.12-alt1
- 4.0.12

* Sun Feb 20 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.4-alt1
- Update to new release

* Sun Feb 06 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.2-alt1
- Update to new release

* Thu Jan 06 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.12-alt1
- Update to new release

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 3.2.4-alt3
- technical

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 3.2.4-alt2
- technical

* Thu Jun 10 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.4-alt1
- Update to new release

* Tue May 11 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.8-alt1
- Update to new release

* Sun Apr 04 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.6-alt1
- Update to new release

* Wed Mar 10 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.4-alt1
- Update to new release

* Tue Nov 03 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.10-alt1
- Updated to new release

* Wed Oct 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.8-alt1
- Updated to new release

* Sun Sep 20 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.6-alt1
- Updated to new release

* Tue Aug 11 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.4-alt1
- Updated to new release

* Thu Jul 23 2009 Anton Protopopov <aspsk@altlinux.org> 3.0.2-alt2
- Merge with sin@ to enforce inheritance

* Mon Jul 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.2-alt1
- Updated to new release

* Sun Jul 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.0-alt2
- Add vboxnetadp building

* Wed Jul 08 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.0-alt1
- Updated to new release

* Sat Jun 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.2.4-alt1
- Updated to new release

* Tue May 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.2.2-alt1
- Updated to new release

* Wed Feb 25 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.4-alt1
- Updated to new release

* Fri Dec 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.0-alt1
- Updated to new release
- Built new netfilter module with vboxdrv Module.symvers

* Sat Nov 08 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.0.4-alt1
- Updated to new release

* Thu Sep 04 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.6-alt1
- Updated to last release

* Sun Aug 31 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.4-alt1
- Updated to last release

* Sun Jun 08 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.2-alt1
- Updated to last release

* Fri Apr 18 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.6-alt2
- Added requires for common package

* Fri Mar 28 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.6-alt1
- Initial virtualbox modules build

