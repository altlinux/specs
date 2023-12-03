# -*- rpm-spec -*-
%define module_name	anbox
# use debian numeration
%define module_version  14
%define git ae26ba2

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: alt4.g%{git}
Provides: kernel-source-%module_name-%module_version
Summary: Anbox kernel modules sources
License: GPLv3/GPLv2
Group: Development/Kernel
Url: http://github.com/anbox/anbox-modules
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%version.tar

BuildPreReq: kernel-build-tools
BuildArch: noarch

%description
Anbox kernel modules sources.

%package -n anbox-kernel-conf
Group: System/Kernel and hardware
Summary: Anbox kernel modules configuration
BuildArch: noarch

%description -n anbox-kernel-conf
Configuration for anbox kernel modules.

%prep
%setup -c -q

%install
# ashmem_linux non needed for kernels >= 5.18
sed -i -e '/^ashmem_linux/d' %name-%version/anbox.conf
install -m644 -pD %name-%version/anbox.conf %buildroot%_sysconfdir/modules-load.d/anbox.conf
install -m644 -pD %name-%version/99-anbox.rules %buildroot%_udevrulesdir/99-anbox.rules

mkdir -p %kernel_srcdir
tar jcf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n anbox-kernel-conf
%_sysconfdir/modules-load.d/anbox.conf
%_udevrulesdir/99-anbox.rules

%changelog
* Sun Dec 03 2023 L.A. Kostis <lakostis@altlinux.ru> 14-alt4.gae26ba2
- Apply fixes from kernel-6.6:
  + binderfs: Drop unused #include <linux/radix-tree.h>
  + binder: fix memory leak in binder_init()
  + binder: fix UAF of alloc->vma in race with munmap()
  + binderfs: convert to ctime accessor functions

* Wed Sep 13 2023 L.A. Kostis <lakostis@altlinux.ru> 14-alt3.gae26ba2
- udev.rules: remove useless macros.

* Thu Jun 01 2023 L.A. Kostis <lakostis@altlinux.ru> 14-alt2.gae26ba2
- Apply fixes to compile with 6.3+ kernel.

* Fri Mar 31 2023 L.A. Kostis <lakostis@altlinux.ru> 14-alt1.gae26ba2
- Updated to GIT ae26ba2 from choff.

* Fri Mar 31 2023 L.A. Kostis <lakostis@altlinux.ru> 13-alt1.g98f0f3b
- Initial build for ALTLinux.
