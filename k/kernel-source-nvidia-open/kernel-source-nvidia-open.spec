# -*- rpm-spec -*-
%define module_name	nvidia-open
%define module_version  610.43.02

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: alt1
Provides: kernel-source-%module_name-%module_version
Summary: NVIDIA Linux open GPU kernel module source
License: MIT and GPLv2
Group: Development/Kernel
Url: https://github.com/NVIDIA/open-gpu-kernel-modules
Vcs: https://github.com/NVIDIA/open-gpu-kernel-modules

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
* Mon Jun 08 2026 L.A. Kostis <lakostis@altlinux.ru> 610.43.02-alt1
- 610.43.02.

* Mon May 11 2026 L.A. Kostis <lakostis@altlinux.ru> 595.71.05-alt1
- 595.71.05.

* Wed Mar 25 2026 L.A. Kostis <lakostis@altlinux.ru> 595.58.03-alt1
- 595.58.03.

* Thu Mar 12 2026 L.A. Kostis <lakostis@altlinux.ru> 595.45.04-alt1
- 595.45.04.

* Tue Feb 03 2026 L.A. Kostis <lakostis@altlinux.ru> 590.48.01-alt1
- 590.48.01.

* Thu Jan 15 2026 L.A. Kostis <lakostis@altlinux.ru> 580.126.09-alt1
- 580.126.09.

* Sat Dec 20 2025 L.A. Kostis <lakostis@altlinux.ru> 580.119.02-alt1
- 580.119.02.

* Sun Dec 07 2025 L.A. Kostis <lakostis@altlinux.ru> 580.105.08-alt1
- 580.105.08.
- Fix license tag.

* Sat Oct 11 2025 L.A. Kostis <lakostis@altlinux.ru> 580.95.05-alt1
- 580.95.05.

* Thu Sep 18 2025 L.A. Kostis <lakostis@altlinux.ru> 580.82.09-alt1
- 580.82.09.

* Mon Sep 08 2025 L.A. Kostis <lakostis@altlinux.ru> 580.82.07-alt1
- 580.82.07.

* Wed Aug 13 2025 L.A. Kostis <lakostis@altlinux.ru> 580.76.05-alt1
- 580.76.05.

* Sun Jul 27 2025 L.A. Kostis <lakostis@altlinux.ru> 575.64.05-alt1
- 575.64.05.

* Thu Jun 26 2025 L.A. Kostis <lakostis@altlinux.ru> 575.64-alt1
- 575.64.
- Apply latest suspend/resume fixes from upcoming version.

* Fri May 30 2025 L.A. Kostis <lakostis@altlinux.ru> 575.57.08-alt1
- 575.57.08.

* Fri Apr 18 2025 L.A. Kostis <lakostis@altlinux.ru> 575.51.02-alt1
- 575.51.02.

* Wed Mar 19 2025 L.A. Kostis <lakostis@altlinux.ru> 570.133.07-alt1
- 570.133.07.

* Sat Mar 08 2025 L.A. Kostis <lakostis@altlinux.ru> 570.124.04-alt1
- 570.124.04.

* Mon Feb 10 2025 L.A. Kostis <lakostis@altlinux.ru> 570.86.16-alt1
- 570.86.16.

* Fri Dec 06 2024 L.A. Kostis <lakostis@altlinux.ru> 565.77-alt1
- 565.77.

* Thu Oct 24 2024 L.A. Kostis <lakostis@altlinux.ru> 565.57.01-alt1
- 565.57.01.

* Thu Aug 29 2024 L.A. Kostis <lakostis@altlinux.ru> 560.35.03-alt1
- 560.35.03.

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

