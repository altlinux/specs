%define module_name	bcmwl
%define module_version	6.30.223.271
%define module_release alt12

%define flavour		centos
%define karch x86_64
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-centos

%setup_kernel_module %flavour

%define norm_version	%kversion

%define module_dir /lib/modules/%kversion-%flavour-%krelease/net

Summary: Modules for Broadcom IEEE 802.11a/b/g/n adapters
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: Proprietary
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: https://github.com/antoineco/broadcom-wl
BuildRequires: perl sharutils
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

Patch: %{module_name}-centos9.patch

%description
These packages contain Broadcom's IEEE 802.11a/b/g/n hybrid Linux device
driver for use with Broadcom's BCM4311-, BCM4312-, BCM4313-, BCM4321-,
BCM4322-, BCM43224-, and BCM43225-, BCM43227- and BCM43228-based hardware

NOTE: You must read the LICENSE.TXT file in the lib directory before
using this software.
%prep
rm -rf kernel-source-%module_name-%module_version

tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2

%setup -D -T -n kernel-source-%module_name-%module_version

# centos backported some fixes for 5.17+
if [ %flavour == "centos" ]; then
%patch -p1
fi

%build
cd bcmwl
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
make -C %_usrsrc/linux-%kversion-%flavour M=`pwd` modules

%install
mkdir -p $RPM_BUILD_ROOT%module_dir/

cd bcmwl
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
make -C %_usrsrc/linux-%kversion-%flavour INSTALL_MOD_PATH=%buildroot INSTALL_MOD_DIR=net M=`pwd`  modules_install

# blacklist several modules (see ALT bugs #26265, #26250)
mkdir -p %buildroot/%_sysconfdir/modprobe.d
cat > %buildroot/%_sysconfdir/modprobe.d/blacklist-bcm.conf << __EOF__
blacklist bcm43xx
blacklist ssb
blacklist b43
__EOF__
cat > %buildroot/%_sysconfdir/modprobe.d/blacklist-bcm2.conf << __EOF__
blacklist b44
blacklist b43legacy
blacklist bcma
blacklist brcmsmac
blacklist brcmfmac
blacklist bcma-pci-bridge
__EOF__

%files
%module_dir
%config(noreplace) %_sysconfdir/modprobe.d/blacklist-bcm.conf
%config(noreplace) %_sysconfdir/modprobe.d/blacklist-bcm2.conf

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Jan 23 2023 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt12
- karch: drop %%ix86 arch.

* Fri Dec 23 2022 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt11
- Update -centos patch.

* Sat Apr 30 2022 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt10
- Fix -centos support.

* Fri Dec 10 2021 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt9
- .spec cleanup.

* Sun Nov 28 2021 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt8
- karch: add centos kernel support.

* Wed Jun 02 2021 L.A. Kostis <lakostis@alltinux.ru> 6.30.223.271-alt7
- Sync w/ sisyphus changes.
- Enable back %%x86 arch support.

* Thu May 20 2021 L.A. Kostis <lakostis@alltinux.ru> 6.30.223.271-alt6
- Use updated sources.
- Cleanup .spec
- Disable %%x86 arch support.

* Wed Mar 08 2017 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt5
- Remove obsoleted patches (sync w/ 6.30.223.271+bdcom-0ubuntu1).

* Mon Mar 06 2017 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt4
- Rediffed patches:
  + synced with ubuntu package (6.30.223.248+bdcom-0ubuntu11).

* Thu Jun 30 2016 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt3
- Blacklisted brcmfmac driver (FullMAC version).

* Wed Jun 29 2016 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt2
- Updated description, remake binaries copying process.
- Cleanup patches.

* Wed Jun 29 2016 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.271-alt1
- 6.30.223.271.
- added patch to remove nl80211_band definition.

* Sat Sep 12 2015 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.248-alt9
- update 4.2 patch.
- add more patches from ubuntu.

* Mon Sep 07 2015 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.248-alt8
- fix build with 4.2+ kernel.

* Thu May 07 2015 L.A. Kostis <lakostis@altlinux.ru> 6.30.223.248-alt7
- Add fix for kernel 4.0+ compatiblity.

* Fri Dec 12 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.248-alt6
- build with kernel 3.18 fixed

* Fri Nov 14 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.248-alt5
- blacklist split

* Tue Oct 21 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.248-alt4
- build with kernel 3.17 fixed
- increased blacklist

* Mon Sep  8 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.248-alt3
- new version

* Tue Jun 24 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.30-alt3
- add support for kernel 3.15

* Tue Feb 18 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.30-alt2
- fixed version

* Mon Feb 17 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.30-alt1
- new version

* Wed Aug  7 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.30-alt1
- new version

* Wed Jul 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.100.82.112-alt5
- add support for kernel 3.10

* Mon Dec 17 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.100.82.112-alt4
- new template

* Mon Jun 11 2012 Anton Protopopov <aspsk@altlinux.org> 5.100.82.112-alt3
- fix to build with kernel 3.4

* Thu Jan 12 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.100.82.112-alt2
- fix to build with kernel 3.2

* Thu Jan 12 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.100.82.112-alt1
- 5.100.82.112

* Thu Sep 15 2011 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt6
- Add 'conf' extension to modprobe configuration file

* Wed Sep 14 2011 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt5
- Blacklist several modules (ALT 26265)

* Thu Feb 17 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.60.48.36-alt4
- 2.6.35 patch extended to infinity

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt3
- technical

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt2
- technical

* Wed Nov 10 2010 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt1
- 5.60.48.36

* Wed Jan 13 2010 Anton Protopopov <aspsk@altlinux.org> 5.10.91.9.3-alt1
- 5.10.91.9.3

* Tue May 26 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.91.9-alt1
- 5.10.91.9

* Tue Apr 21 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.79.10-alt2
- Fix module position (closes: 19603)

* Wed Mar 25 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.79.10-alt1
- initial build

