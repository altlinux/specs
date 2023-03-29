%define module_name	evdi
%define module_version	1.12.0
%define module_release	alt4

%define flavour		un-def
%define karch %ix86 x86_64 armh aarch64
BuildRequires(pre): kernel-headers-modules-un-def
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: DisplayLink kernel module
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
URL: https://github.com/DisplayLink/evdi
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %EVR

PreReq: coreutils
PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

Patch1: %module_name-1.12.0-centos9.patch
Patch2: %module_name-1.12.0-drm-framebuffer.patch
# https://github.com/DisplayLink/evdi/pull/401
Patch3: %module_name-1.12.0-kernel-6.2.patch

%description
Extensible Virtual Display Interface

The Extensible Virtual Display Interface (EVDI) is a Linux kernel module that
enables management of multiple screens, allowing user-space programs to take
control over what happens with the image. It is essentially a virtual display
you can add, remove and receive screen updates for, in an application that uses
the libevdi library.

%prep
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

# centos backported some fixes for 5.15+
if [ %flavour == "centos" ]; then
%patch1 -p1
else
%patch2 -p1
fi
%patch3 -p2

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour M=`pwd` modules

%install
install -d %buildroot%module_dir
install evdi.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Sun Mar 12 2023 L.A. Kostis <lakostis@altlinux.org> 1.12.0-alt4
- Added patch for 6.2+ kernels (gh pull #401).

* Thu Dec 08 2022 L.A. Kostis <lakostis@altlinux.org> 1.12.0-alt3
- update centos9 patch.
- update drm-framebuffer patch (upstream commit
  bdc258b25df4d00f222fde0e3c5003bf88ef17b5).

* Thu Oct 06 2022 L.A. Kostis <lakostis@altlinux.org> 1.12.0-alt2
- Add patch to compile w/ kernel 6.0+.

* Tue Aug 16 2022 L.A. Kostis <lakostis@altlinux.org> 1.12.0-alt1
- Updated to 1.12.0.

* Wed Jul 20 2022 L.A. Kostis <lakostis@altlinux.org> 1.11.0-alt2
- Updated -centos9 patch (due drm backport changes).

* Fri Jun 03 2022 L.A. Kostis <lakostis@altlinux.org> 1.11.0-alt1
- Updated to 1.11.0.
- Updated -centos9 patch.

* Mon Mar 21 2022 L.A. Kostis <lakostis@altlinux.org> 1.10.1-alt1
- Updated to 1.10.1.
- Cleanup patches.

* Fri Feb 11 2022 L.A. Kostis <lakostis@altlinux.org> 1.10.0-alt4
- Fix build with recent centos9 kernel (tnx glebfm@ for ideas)
- Fix merge from ChromeOS (see upstream issue #340).

* Sat Jan 29 2022 L.A. Kostis <lakostis@altlinux.org> 1.10.0-alt3
- Restore kmarch for centos.

* Sat Jan 29 2022 L.A. Kostis <lakostis@altlinux.org> 1.10.0-alt2
- Restore workaround for centos.

* Sat Jan 29 2022 L.A. Kostis <lakostis@altlinux.org> 1.10.0-alt1
- Updated to 1.10.0.

* Sun Dec 19 2021 L.A. Kostis <lakostis@altlinux.org> 1.9.1-alt7
- Fix compile with recent centos9 kernel.

* Mon Nov 29 2021 L.A. Kostis <lakostis@altlinux.org> 1.9.1-alt6
- Add -centos kernel support.

* Thu Nov 25 2021 L.A. Kostis <lakostis@altlinux.org> 1.9.1-alt5
- Bump release.

* Thu Nov 25 2021 L.A. Kostis <lakostis@altlinux.org> 1.9.1-alt4
- Enable armh.
- Apply some fixes from upstream PRs:
  + 0001-Add-support-for-cursor-planes.patch (PR 314)
  + 0001-Remove-compat-calls-for-5.15-kernel.patch (fix compile on 5.15+ kernels)
  + 0002-Fix-dma_buf_vunmap-failing-on-kernel-5.11.patch (PR 315)

* Thu Nov 25 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.9.1-alt3
- build with kernel 5.15 fixed

* Mon Nov 22 2021 L.A. Kostis <lakostis@altlinux.org> 1.9.1-alt2
- Add ExclusiveArch.

* Mon Nov 22 2021 L.A. Kostis <lakostis@altlinux.org> 1.9.1-alt1
- Initial build for Sisyphus.
