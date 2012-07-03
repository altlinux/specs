%define module_name	fglrx
%define module_version	8.93
%define module_release	alt1

%define kversion       2.6.32
%define krelease       alt55
%define flavour                xen-dom0

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name


Summary:	AMD/ATI Proprietary Linux Display Driver
Name:		kernel-modules-%module_name-%flavour
Version:	1.0.%module_version
Release:	%module_release.132640.55
License:	Proprietary
Group:		System/Kernel and hardware

Packager:       Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS:	Linux
URL:		http://ati.amd.com/support/drivers/linux/linux-radeonhdd.html
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kversion-%krelease
BuildRequires: kernel-headers-%flavour = %kversion-%krelease
BuildRequires: kernel-source-%module_name-%module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Prereq:		coreutils
Prereq:         kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease

ExclusiveArch:  %ix86 x86_64

Patch1: kernel-source-fglrx-8.37.3.openvz.patch
# https://bugs.launchpad.net/ubuntu/+source/linux-restricted-modules-2.6.24/+bug/239967
Patch2: alt-fix-sigio.patch
Patch3: FGLRX-2.6.36-10-10.diff
Patch4: http://www.cosmicencounter.net/mirror/patch/sema_init.patch
Patch5: http://aur.archlinux.org/packages/catalyst-generator/catalyst-generator/makefile_compat.patch

Patch7: fglrx-2.6.38.patch

%description
Kernel drivers for AMD/ATI Proprietary Linux Catalyst(tm) software suite

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
%if "%flavour" == "ovz-smp"
%if "%kversion" == "2.6.18"
%patch1 -p1
%endif
%endif
%patch2 -p1
#patch3 -p0
%if "%kversion" == "2.6.37"
%patch4 -p5
%patch5 -p6
%endif

#patch7 -p1


sed -i 's|COMPAT_ALLOC_USER_SPACE|arch_compat_alloc_user_space|' kcl_ioctl.c

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%__ln_s ./2.6.x/Makefile ./Makefile
%make_build TEMP_DIR=$PWD/ -C %_usrsrc/linux-%kversion-%flavour modules V=1 \
	SUBDIRS=$PWD GCC_VER_MAJ=`echo "$GCC_VERSION" | sed 's/^\([0-9]\+\).*/\1/'`

%install
mkdir -p $RPM_BUILD_ROOT/%module_dir
install -p -m644 fglrx.ko $RPM_BUILD_ROOT/%module_dir

%post
%post_kernel_modules %kversion-%flavour-%krelease

%postun
%postun_kernel_modules %kversion-%flavour-%krelease

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* Thu Feb 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.8.93-alt1.132640.55
- Build for kernel-image-xen-dom0-2.6.32-alt55.

* Tue Feb 07 2012 Anton Protopopov <aspsk@altlinux.org> 1.0.8.93-alt1
- 8.93

* Tue Dec 20 2011 Anton Protopopov <aspsk@altlinux.org> 1.0.8.92-alt1
- 8.92

* Tue Nov 22 2011 Anton Protopopov <aspsk@altlinux.org> 1.0.8.91.1-alt1
- 8.91.1

* Mon Nov 14 2011 Anton Protopopov <aspsk@altlinux.org> 1.0.8.90.2-alt1
- 8.90.2

* Thu Oct 20 2011 Anton Protopopov <aspsk@altlinux.org> 1.0.8.89.2-alt1
- 8.89.2

* Tue Aug 30 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.8.88.1-alt1
- 8.88.1

* Sat Aug 06 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.8.87.2-alt1
- 8.87.2

* Mon Jun 20 2011 Anton Protopopov <aspsk@altlinux.org> 1.0.8.86.1-alt1
- 8.86.1

* Wed May 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8.85-alt1
- 8.85

* Fri May 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8.84.1-alt3
- 8.84.1

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8.80.1-alt3
- Fixed for 2.6.37

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8.80.1-alt2
- Fixed for 2.6.36+ (thnx ashen@)

* Thu Dec 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8.80.1-alt1
- 8.80.1

* Thu Nov 11 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.8.78.3-alt1
- 8.78.3

* Thu Sep 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.8.76.2-alt1
- 8.76.2

* Sat Aug 21 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.8.75.3-alt1
- 8.75.3

* Tue Jul 06 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.8.74.1-alt1
- 8.74.1

* Wed Jun 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.8.73.2-alt1

* Thu Jan 14 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.8.68.1-alt2
- build with 2.6.32 fixed

* Wed Dec 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8.68.1-alt1
- 8.68.1

* Mon Dec 07 2009 Michail Yakushin <silicium@altlinux.ru> 1.0.8.67.1-alt1
- 8.67.1

* Mon Aug 24 2009 Michail Yakushin <silicium@altlinux.ru> 1.0.8.64-alt1

- 8.64

* Mon Jul 27 2009 Anton Protopopov <aspsk@altlinux.org> 1.0.8.63.2-alt1
- 8.63.2

* Fri Jun 19 2009 Anton Protopopov <aspsk@altlinux.org> 1.0.8.62-alt1
- 8.62

* Fri May 22 2009 Michail Yakushin <silicium@altlinux.ru> 1.0.8.61.2-alt1
- 8.61.2

* Mon Apr 20 2009 Anton Protopopov <aspsk@altlinux.org> 1.0.8.60.2-alt1
- 8.60.2

* Mon Apr 06 2009 Michail Yakushin <silicium@altlinux.ru> 1.0.8.59.3-alt1
- 8.59.3 

* Mon Apr 06 2009 Anton Protopopov <aspsk@altlinux.org> 1.0.8.58.2-alt3
- "Merge" with silicium@

* Wed Mar 04 2009 Michail Yakushin <silicium@altlinux.ru> 1.0.8.58.2-alt1
- Version 8.58.2 

* Mon Mar 02 2009 Anton Protopopov <aspsk@altlinux.org> 1.0.8.58.2-alt2
- Remove dead patch

* Mon Mar 02 2009 Anton Protopopov <aspsk@altlinux.org> 1.0.8.58.2-alt1
- Version 8.58.2

* Tue Oct 28 2008 Michail Yakushin <silicium@altlinux.ru> 1.0.8.53.2-alt2
- add 2.6.27 support 

* Sat Sep 20 2008 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.53.2-alt1
- Version 8.53.2.

* Mon Sep 01 2008 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.52.2-alt2
- Bugfix release:
  + fix unresolved symbols in x86_64 build (as in 8.50.1).
  + remove obsoleted patches and macros (2.4 kernel support for example).

* Fri Aug 22 2008 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.52.2-alt1
- Version 8.52.2.

* Wed Aug 06 2008 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.51.2-alt1
- Version 8.51.2.

* Wed Jul 09 2008 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.50.1-alt2
- fix unresolved symbols in x86_64 build.

* Wed Jun 25 2008 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.50.1-alt1
- Version 8.50.1.
- Add patches from https://bugs.launchpad.net/~zilvinas-valinskas for compile
  on 2.6.25+.

* Wed May 28 2008 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.49.3.1-alt1
- Version 8.49.3.1.

* Thu May 01 2008 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.47.6-alt2
- add patch for 2.6.25+ compilation. Kudos to Gentoo ;)

* Thu Apr 17 2008 L.A. Kostis <lakostis@altlinux.org> 1.0.8.47.6-alt1
- Version 8.47.6.


* Fri Mar 07 2008 L.A. Kostis <lakostis@altlinux.org> 1.0.8.47.1-alt1
- Version 8.47.1.

* Fri Feb 15 2008 L.A. Kostis <lakostis@altlinux.org> 1.0.8.45.5.2-alt1
- Version 8.45.5.2.

* Fri Jan 18 2008 L.A. Kostis <lakostis@altlinux.org> 1.0.8.45.2.1-alt1
- Version 8.45.2.1.

* Wed Dec 26 2007 L.A. Kostis <lakostis@altlinux.org> 1.0.8.44.3.1-alt1
- Version 8.44.3.1.

* Mon Nov 26 2007 L.A. Kostis <lakostis@altlinux.org> 1.0.8.43.3-alt1
- Version 8.43.3.

* Tue Nov 20 2007 L.A. Kostis <lakostis@altlinux.org> 1.0.8.42.3-alt2
- Add patches from Sabayon Linux (mostly for 2.6.23+): 
  + ati-drivers-2.6.23.patch: fix compile with recent (2.6.23+) kernel
  + ati-drivers-8.40.4-warnings.patch: drop "unused" components of the mm API

* Wed Oct 24 2007 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.42.3-alt1
- Version 8.42.3.
- Update description.

* Thu Oct 11 2007 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.42.3-alt0.1
- Version 8.423-071009a-054262E-ATI (internal beta release).

* Fri Oct 05 2007 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.42.2-alt0.1
- Version 8.422-071002a-054011E-ATI (internal beta release).

* Thu Sep 06 2007 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.41.7-alt1
- Version 8.41.7 (internal beta release).

* Mon Aug 20 2007 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.40.4-alt1
- Version 8.40.4.

* Sat Aug 04 2007 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.39.4-alt1
- Version 8.39.4.

* Mon Jul 02 2007 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.38.6-alt1
- Version 8.38.6.

* Sun Jun 10 2007 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.37.6-alt1
- Version 8.37.6.

* Sun May 06 2007 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.37.3-alt0.1
- Version 8.37.3 (internal beta release).
- Patch for OpenVZ changes.

* Sat Apr 21 2007 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.36.5-alt1
- Version 8.36.5.

* Sun Apr 08 2007 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.35.5-alt1
- Version 8.35.5.

* Sat Feb 24 2007 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.34.8-alt1
- Version 8.34.8.

* Mon Jan 29 2007 Sergey Vlasov <vsu@altlinux.ru> 1.0.8.32.5-alt2
- Removed unneeded "Prereq: modutils".

* Thu Jan 11 2007 L.A. Kostis <lakostis@altlinux.org> 1.0.8.33.6-alt1
- Version 8.33.6.

* Thu Dec 14 2006 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.32.5-alt1
- Version 8.32.5.

* Sat Dec 09 2006 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.32.2-alt1
- Version 8.32.2 (internal beta release).

* Sat Sep 23 2006 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.29.6-alt1
- Version 8.29.6.

* Sun Aug 27 2006 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.28.8-alt1
- Version 8.28.8.

* Sat Aug 12 2006 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.28.4-alt1
- Version 8.28.4 (internal beta release).

* Fri Aug 11 2006 L.A. Kostis <lakostis@altlinux.ru> 1.0.8.27.10-alt1
- Version 8.27.10.

* Thu Jul 06 2006 LAKostis <lakostis at altlinux.ru> 1.0.8.27.4-alt1
- Version 8.27.4.
- internal beta release.
- update description.

* Wed Jun 21 2006 LAKostis <lakostis at altlinux.ru> 1.0.8.26.11-alt1
- Version 8.26.11.
- internal beta release.

* Wed May 31 2006 LAKostis <lakostis at altlinux.ru> 1.0.8.25.18-alt1
- Version 8.25.18.
- Removed all patches (moved to kernel-source-fglrx).

* Fri Apr 14 2006 LAKostis <lakostis at altlinux.ru> 1.0.8.24.8-alt1
- Version 8.24.8.
- Added patches:
  + 06_fglrx-8.24.8-x86-64-no_iommu-cleanup.patch - cleanup no_iommu calls (it's not
    used anymore in 2.6.16).

* Tue Feb 21 2006 LAKostis <lakostis at altlinux.ru> 1.0.8.22.5-alt1
- Version 8.22.5.
- Enable x86_64 support.

* Sun Jan 22 2006 LAKostis <lakostis at altlinux.ru> 1.0.8.21.7-alt1
- Version 8.21.7.

* Wed Dec 14 2005 LAKostis <lakostis at altlinux.ru> 1.0.8.20.8-alt1
- Version 8.20.8.
- Added patches:
  + 05_fglrx-8.20.8-alt-spinlock.patch: update to new spinlock API.
  
* Sun Nov 27 2005 LAKostis <lakostis at altlinux.ru> 1.0.8.19.10-alt1
- Version 8.19.10.

* Sun Oct 16 2005 LAKostis <lakostis at altlinux.ru> 1.0.8.18.6-alt1
- Version 8.18.6.
- Removed patches:
  - 01_fglrx-2.6.12-pci_name.patch (fixed upstream).
  - 02_fglrx-2.6.12-inter_module.patch (fixed upstream).
  - 03_fglrx-8.14.13-alt-2.6.12-agp.patch (fixed upstream).
  - 04_fglrx-8.14.13-alt-nopage-proto.patch (fixed upstream).

* Sat Jul 02 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.8.14.13-alt2
- Added patches to fix build with kernel 2.6.12:
  + 01_fglrx-2.6.12-pci_name.patch: use pci_name(dev) instead of dev->slot_name
    to fix compilation with kernel 2.6.12
  + 02_fglrx-2.6.12-inter_module.patch: inter_module_get() is no longer
    available in kernel 2.6.12 - avoid using it
  + 03_fglrx-8.14.13-alt-2.6.12-agp.patch: add wrappers for new agpgart
    interfaces in kernel 2.6.12 (should work for systems with a single AGP
    bridge, proper solution requires new interfaces with the binary-only part)
  + 04_fglrx-8.14.13-alt-nopage-proto.patch: fix wrong arguments for
    vm_pcie_nopage() implementation for 2.6.x

* Sun Jun 12 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.8.14.13-alt1
- Version 8.14.13.

* Wed Jun 01 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.8.12.10-alt1
- Version 8.12.10.

* Mon Mar 14 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.8.10.19-alt1
- Version 8.10.19 for X.Org 6.8.

* Sun Jan 30 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.8.8.25-alt1
- Version 8.8.25 for X.Org 6.8.
- Removed all patches (moved to kernel-source-fglrx).

* Sun Dec 26 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.11.1-alt3
- Rebuild for kernel 2.4.28.

* Sun Oct 17 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.11.1-alt2
- Rebuild for kernel 2.4.27.

* Mon Aug 16 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.11.1-alt1
- Version 3.11.1.
- Removed patches:
  - fglrx-3.2.5-agp-i875.patch (fixed upstream)
  - fglrx-3.7.6-page-count.patch (fixed upstream)

* Tue Aug 03 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.7.6-alt6
- Use %%post_kernel_modules and %%postun_kernel_modules macros in scripts.

* Wed Jun 23 2004 Anton Farygin <rider@altlinux.ru> 1.0.3.7.6-alt5
- fglrx-3.7.6-page-count.patch:
    * fixed build problem for 2.6.7 kernel

* Thu May 13 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.7.6-alt4
- Rebuild for kernel 2.4.26.

* Wed May 12 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.7.6-alt3
- Added Patch6: fglrx-3.7.6-sis-agp3-support.patch: AGP3 support for SiS 648.

* Mon Apr 12 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.7.6-alt2
- Added Patch5: fglrx-3.7.6-agp-sis-fix.patch: workaround for SiS 648 and 746
  chips (seems that they need a delay after setting AGP rate).

* Mon Mar 22 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.7.6-alt1
- Version 3.7.6.

* Fri Feb 27 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.7.0-alt4
- Updated for the new compiler version selection scheme (GCC_VERSION).

* Wed Feb 18 2004 Anton Farygin <rider@altlinux.ru> 1.0.3.7.0-alt3
- rebuild for 2.6.3

* Mon Feb 16 2004 Anton Farygin <rider@altlinux.ru> 1.0.3.7.0-alt2
- build for kernel 2.6

* Sun Jan 04 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.7.0-alt1
- Version 3.7.0.
- Fixed SMP build options (-D__SMP__ is required for SMP kernels).
- Fixed PAGE_ATTR_FIX typo in compilation options.

* Fri Nov 28 2003 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.2.8-alt3
- Added Provides/Conflicts to make sure that only one version of the package
  can be installed for each kernel version.

* Tue Nov 18 2003 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.2.8-alt2
- Fixed spec file name.
- Avoid %%postun failure when this package is removed after
  kernel-image-%%flavour (currently rpm cannot prevent this).
- Added Patch4: fglrx-3.2.8-nvidia-nforce.patch: fixed nForce AGP support.

* Sun Oct 12 2003 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.2.8-alt1
- new version (3.2.8).
- updated Patch1 (some SiS support was added in upstream, only SiS 745 remains
  unknown).
- fixed compile flags.
- Patch3: fixed AGP 2.0 support for VIA KT400 and P4X333.

* Mon Sep 29 2003 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.2.5-alt16
- Patch2: fixed Intel 875P chipset support (it does not have integrated
  graphics capability).

* Fri Sep 26 2003 Sergey Vlasov <vsu@altlinux.ru> 1.0.3.2.5-alt15
- replaced %%{_usrsrc}/kernel/sources with %%kernel_src
- Patch1: added new SiS host bridge IDs to the builtin AGP support (from
  mainstream kernel)

* Mon Sep 08 2003 Anton Farygin <rider@altlinux.ru> 1.0.3.2.5-alt14
- new version (3.2.5)

* Wed Sep 03 2003 Rider <rider@altlinux.ru> 1.0.2.9.12-alt14
- replace /usr/include to _includedir macro

* Tue Aug 26 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.2.9.12-alt13
- rebuilt with 2.4.21rel-alt14

* Fri Aug 15 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.2.9.12-alt12
- rebuilt with 2.4.21rel-alt13

* Wed Aug 13 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.2.9.12-alt11
- rebuilt with 2.4.21rel-alt12

* Tue Aug 12 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.2.9.12-alt10
- rebuilt with 2.4.21rel-alt11

* Mon Aug 11 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.2.9.12-alt9
- rebuilt with 2.4.21rel-alt10

* Thu Aug 07 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.2.9.12-alt8
- rebuilt with 2.4.21rel-alt9

* Wed Aug 06 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.2.9.12-alt7
- rebuilt with 2.4.21rel-alt8

* Wed Jul 30 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.2.9.12-alt6
- rebuilt with 2.4.21rel-alt7

* Thu Jul 17 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.2.9.12-alt5
- rebuilt with 2.4.21rel-alt6

* Wed Jul 16 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.2.9.12-alt4
- rebuilt with 2.4.21rel-alt5

* Tue Jul 08 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.2.9.12-alt3
- added -include /usr/include/linux-%{kversion}-%{flavour}/include/linux/modversions.h
  now it actually WORKS!

* Sat Jun 21 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.2.9.12-alt2
- rebuilt with 2.4.21rel kernel

* Thu Jun 05 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.2.9.12-alt1
- initial version.

