%define soname 7
Name: libva-intel-media-driver
Version: 26.2.3
Release: alt1

Summary: Intel(R) Media Driver for VAAPI
License: MIT
Group: System/Libraries
Url: https://github.com/intel/media-driver/

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: libdrm-devel libX11-devel libGL-devel libEGL-devel gcc-c++ libpciaccess-devel
BuildRequires: libva-devel >= 2.20.0
BuildRequires: cmake rpm-macros-cmake
BuildRequires: intel-gmmlib-devel >= 22.8.2
ExclusiveArch: x86_64

%description
The Intel(R) Media Driver for VAAPI is a new VA-API (Video Acceleration API) user
mode driver supporting hardware accelerated decoding, encoding, and video post
processing for GEN based graphics hardware.

%package -n libigfxcmrt%soname
Group: System/Libraries
Summary: C bindings for media runtime

%description -n libigfxcmrt%soname
cmrtlib is a runtime library needed when user wants to execute their own GPU
kernels on render engine. It calls iHD media driver to load the kernels and
allocate the resources. It provides a set of APIs for user to call directly from application.

%package -n libigfxcmrt-devel
Summary: Development files for libigfxcmrt%soname
Group: Development/C
Requires: libigfxcmrt%soname = %EVR

%description -n libigfxcmrt-devel
This package provides the development environment for libigfxcmrt

%prep
%setup
%patch0 -p1

%build
%cmake \
	-DENABLE_KERNELS=ON \
	%nil
%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSE.md README.md
%_libdir/dri//iHD_drv_video.so

%files -n libigfxcmrt%soname
%_libdir/libigfxcmrt.so.%soname
%_libdir/libigfxcmrt.so.%soname.*

%files -n libigfxcmrt-devel
%_libdir/libigfxcmrt.so
%_includedir/igfxcmrt
%_pkgconfigdir/igfxcmrt.pc

%changelog
* Mon Jun 29 2026 Anton Farygin <rider@altlinux.org> 26.2.3-alt1
- 26.2.0 -> 26.2.3

* Tue May 26 2026 Anton Farygin <rider@altlinux.org> 26.2.0-alt0.P11.0
- backport to p11

* Tue May 19 2026 Anton Farygin <rider@altlinux.org> 26.2.0-alt1
- 26.1.6 -> 26.2.0

* Mon Apr 20 2026 Anton Farygin <rider@altlinux.org> 26.1.6-alt1
- 26.1.4 -> 26.1.6

* Sat Mar 21 2026 Anton Farygin <rider@altlinux.org> 26.1.4-alt1
- 26.1.3 -> 26.1.4

* Sun Mar 08 2026 Anton Farygin <rider@altlinux.org> 26.1.3-alt1
- 26.1.1 -> 26.1.3

* Mon Feb 09 2026 Anton Farygin <rider@altlinux.org> 26.1.1-alt1
- 26.1.0 -> 26.1.1

* Wed Jan 21 2026 Anton Farygin <rider@altlinux.org> 26.1.0-alt1
- 25.4.6 -> 26.1.0

* Tue Dec 30 2025 Anton Farygin <rider@altlinux.org> 25.4.6-alt1
- 25.4.5 -> 25.4.6

* Sat Dec 06 2025 Anton Farygin <rider@altlinux.com> 25.4.5-alt1
- 25.4.4 -> 25.4.5

* Sun Nov 23 2025 Anton Farygin <rider@altlinux.com> 25.4.4-alt1
- 25.4.3 -> 25.4.4

* Mon Nov 10 2025 Anton Farygin <rider@altlinux.com> 25.4.3-alt1
- 25.3.4 -> 25.4.3

* Tue Oct 14 2025 Anton Farygin <rider@altlinux.com> 25.3.4-alt1
- 25.3.3 -> 25.3.4

* Fri Aug 29 2025 Anton Farygin <rider@altlinux.com> 25.3.3-alt1
- 25.2.5 -> 25.3.3

* Tue Jul 22 2025 Anton Farygin <rider@altlinux.com> 25.3.0-alt1
- 25.2.5 -> 25.3.0

* Thu Jun 19 2025 Anton Farygin <rider@altlinux.com> 25.2.5-alt1
- 25.2.1 -> 25.2.5

* Mon May 05 2025 Anton Farygin <rider@altlinux.com> 25.2.1-alt1
- 25.1.4 -> 25.2.1

* Mon Mar 31 2025 Anton Farygin <rider@altlinux.com> 25.1.4-alt1
- 25.1.2 -> 25.1.4

* Tue Feb 25 2025 Anton Farygin <rider@altlinux.ru> 25.1.2-alt1
- 25.1.0 -> 25.1.2

* Wed Jan 15 2025 Anton Farygin <rider@altlinux.ru> 25.1.0-alt1
- 24.4.3 -> 25.1.0

* Fri Nov 29 2024 Anton Farygin <rider@altlinux.ru> 24.4.3-alt1
- 24.3.4 -> 24.4.3

* Mon Oct 07 2024 Anton Farygin <rider@altlinux.ru> 24.3.4-alt1
- 24.3.2 -> 24.3.4

* Mon Aug 26 2024 Anton Farygin <rider@altlinux.ru> 24.3.2-alt1
- 24.3.2

* Thu Jun 27 2024 Anton Farygin <rider@altlinux.ru> 24.2.5-alt1
- 24.2.5

* Sat Jun 08 2024 Anton Farygin <rider@altlinux.ru> 24.2.4-alt1
- 24.2.4

* Fri May 03 2024 Anton Farygin <rider@altlinux.ru> 24.2.2-alt1
- 24.2.2

* Sat Mar 30 2024 Anton Farygin <rider@altlinux.ru> 24.2.0-alt1
- 24.2.0

* Sun Feb 25 2024 Anton Farygin <rider@altlinux.ru> 24.1.3-alt1
- 24.1.0 -> 24.1.3

* Wed Dec 27 2023 Anton Farygin <rider@altlinux.ru> 24.1.0-alt1
- 23.3.4 -> 24.1.0

* Tue Oct 24 2023 Anton Farygin <rider@altlinux.ru> 23.3.4-alt1
- 23.2.4 -> 23.3.4

* Thu Jul 06 2023 Anton Farygin <rider@altlinux.ru> 23.2.4-alt1
- 23.2.3 -> 23.2.4

* Sun Jun 25 2023 Anton Farygin <rider@altlinux.ru> 23.2.3-alt1
- 23.2.2 -> 23.2.3

* Mon May 22 2023 Anton Farygin <rider@altlinux.ru> 23.2.2-alt1
- 23.1.5 -> 23.2.2

* Thu Mar 30 2023 Anton Farygin <rider@altlinux.ru> 23.1.5-alt1
- 23.1.2 -> 23.1.5

* Mon Feb 27 2023 Anton Farygin <rider@altlinux.ru> 23.1.2-alt1
- 23.1.0 -> 23.1.2

* Wed Jan 18 2023 Anton Farygin <rider@altlinux.ru> 23.1.0-alt1
- 22.6.2 -> 23.1.0

* Sat Nov 12 2022 Anton Farygin <rider@altlinux.ru> 22.6.2-alt1
- 22.5.4 -> 22.6.2

* Wed Oct 05 2022 Anton Farygin <rider@altlinux.ru> 22.5.4-alt1
- 22.4.2 -> 22.5.4

* Mon Jun 06 2022 Anton Farygin <rider@altlinux.ru> 22.4.2-alt1
- 22.3.1 -> 22.4.2

* Sat Apr 09 2022 Anton Farygin <rider@altlinux.ru> 22.3.1-alt1
- 22.3.0 -> 22.3.1

* Sat Mar 26 2022 Anton Farygin <rider@altlinux.ru> 22.3.0-alt1
- 22.1.1 -> 22.3.0

* Fri Jan 28 2022 Anton Farygin <rider@altlinux.ru> 22.1.1-alt1
- 22.1.0 -> 22.1.1

* Sun Jan 09 2022 Anton Farygin <rider@altlinux.ru> 22.1.0-alt1
- 21.4.3 -> 22.1.0

* Sun Dec 05 2021 Anton Farygin <rider@altlinux.ru> 21.4.3-alt1
- 21.3.4 -> 21.4.3

* Sun Oct 03 2021 Anton Farygin <rider@altlinux.ru> 21.3.4-alt1
- 21.3.4

* Mon Sep 06 2021 Anton Farygin <rider@altlinux.ru> 21.3.3-alt1
- 21.3.3

* Wed Aug 18 2021 Anton Farygin <rider@altlinux.ru> 21.3.1-alt1
- 21.3.1

* Wed Jul 07 2021 Anton Farygin <rider@altlinux.ru> 21.2.3-alt1
- 21.2.3

* Fri Jun 11 2021 Anton Farygin <rider@altlinux.ru> 21.2.2-alt1
- 21.2.2

* Sat Apr 10 2021 Anton Farygin <rider@altlinux.org> 21.1.3-alt1
- 21.1.3

* Sun Mar 28 2021 Anton Farygin <rider@altlinux.org> 21.1.2-alt1
- 21.1.2

* Sun Jan 03 2021 Anton Farygin <rider@altlinux.ru> 20.4.5-alt1
- 20.4.5

* Mon Oct 05 2020 Anton Farygin <rider@altlinux.ru> 20.3.0-alt1
- 20.3.0

* Mon Jul 20 2020 Anton Farygin <rider@altlinux.ru> 20.2.0-alt1
- 20.2

* Mon Apr 20 2020 Anton Farygin <rider@altlinux.ru> 20.1.1-alt1
- 20.1.1

* Mon Jan 13 2020 Anton Farygin <rider@altlinux.ru> 19.4.0-alt1
- 19.4.0

* Wed Nov 13 2019 Anton Farygin <rider@altlinux.ru> 19.3.1-alt1
- 19.3.1

* Sat Oct 12 2019 Anton Farygin <rider@altlinux.ru> 19.3.0-alt1
- 19.3.0

* Thu Aug 15 2019 Anton Farygin <rider@altlinux.ru> 19.2.1-alt1
- 19.2.1

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 19.1.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Fri Apr 26 2019 Anton Farygin <rider@altlinux.ru> 19.1.0-alt1
- 19.1.0

* Mon Feb 18 2019 Anton Farygin <rider@altlinux.ru> 18.4.1-alt1
- 18.4.1

* Mon Oct 08 2018 Anton Farygin <rider@altlinux.ru> 18.3.0-alt1
- first build for ALT

