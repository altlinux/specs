# -*- rpm-spec -*-
%define module_name	nvidia-open
%define module_version  560.31.02

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: alt1
Provides: kernel-source-%module_name-%module_version
Summary: NVIDIA Linux open GPU kernel module source
License: MIT/GPLv2
Group: Development/Kernel
Url: https://github.com/NVIDIA/open-gpu-kernel-modules
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%version.tar

BuildPreReq: kernel-build-tools
BuildArch: noarch

%description
NVIDIA Linux open GPU kernel module source.

%prep
%setup -c -q

%install
mkdir -p %kernel_srcdir
tar jcf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Mon Aug 12 2024 L.A. Kostis <lakostis@altlinux.ru> 560.31.02-alt1
- 560.31.02.

* Mon Jul 15 2024 L.A. Kostis <lakostis@altlinux.ru> 555.58.02-alt1
- 555.58.02.

* Thu Jun 06 2024 L.A. Kostis <lakostis@altlinux.ru> 550.90.07-alt1
- 550.90.07.

* Mon Apr 29 2024 L.A. Kostis <lakostis@altlinux.ru> 550.78-alt1
- 550.78.

* Sat Apr 06 2024 L.A. Kostis <lakostis@altlinux.ru> 550.67-alt1
- 550.67.

* Sat Feb 24 2024 L.A. Kostis <lakostis@altlinux.ru> 550.54.14-alt1
- 550.54.14.

* Thu Feb 08 2024 L.A. Kostis <lakostis@altlinux.ru> 550.40.07-alt1
- 550.40.07.

* Wed Nov 29 2023 L.A. Kostis <lakostis@altlinux.ru> 545.29.06-alt1
- 545.29.06.

* Thu Nov 02 2023 L.A. Kostis <lakostis@altlinux.ru> 545.29.02-alt1
- 545.29.02.

* Sun Oct 22 2023 L.A. Kostis <lakostis@altlinux.ru> 545.23.06-alt1
- 545.23.06.

* Wed Sep 06 2023 L.A. Kostis <lakostis@altlinux.ru> 535.104.05-alt1
- 535.104.05.

* Thu Aug 17 2023 L.A. Kostis <lakostis@altlinux.ru> 535.98-alt1
- 535.98.

* Wed Jul 19 2023 L.A. Kostis <lakostis@altlinux.ru> 535.86.05-alt1
- 535.86.05.

* Sat Jul 01 2023 L.A. Kostis <lakostis@altlinux.ru> 535.54.03-alt1
- 535.54.03.

* Wed May 31 2023 L.A. Kostis <lakostis@altlinux.ru> 535.43.02-alt1
- 535.43.02.

* Thu Mar 23 2023 L.A. Kostis <lakostis@altlinux.ru> 530.41.03-alt1
- 530.41.03.

* Thu Mar 02 2023 L.A. Kostis <lakostis@altlinux.ru> 530.30.02-alt1
- 530.30.02.

* Fri Feb 10 2023 L.A. Kostis <lakostis@altlinux.ru> 525.89.02-alt1
- 525.89.02.

* Sun Jan 22 2023 L.A. Kostis <lakostis@altlinux.ru> 525.85.05-alt1
- 525.85.05.

* Fri Jan 06 2023 L.A. Kostis <lakostis@altlinux.ru> 525.78.01-alt1
- 525.78.01.

* Fri Dec 23 2022 L.A. Kostis <lakostis@altlinux.ru> 525.60.13-alt1
- 525.60.13.

* Thu Dec 01 2022 L.A. Kostis <lakostis@altlinux.ru> 525.60.11-alt1
- 525.60.11.

* Fri Nov 11 2022 L.A. Kostis <lakostis@altlinux.ru> 525.53-alt1
- 525.53.

* Tue Nov 01 2022 L.A. Kostis <lakostis@altlinux.ru> 520.56.06-alt1
- Initial build for ALTLinux.

