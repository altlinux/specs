%define soname 7
Name: libva-intel-media-driver
Version: 24.3.4
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
BuildRequires: intel-gmmlib-devel >= 22.3.12
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
%_libdir/dri/*.so

%files -n libigfxcmrt%soname
%_libdir/libigfxcmrt.so.%soname
%_libdir/libigfxcmrt.so.%soname.*

%files -n libigfxcmrt-devel
%_libdir/libigfxcmrt.so
%_includedir/igfxcmrt
%_pkgconfigdir/igfxcmrt.pc

%changelog
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

