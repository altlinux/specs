%define _unpackaged_files_terminate_build 1
%define soversion 12
ExclusiveArch: x86_64
Name:     intel-gmmlib
Version:  22.3.5
Release:  alt1
Summary:  Intel(R) Graphics Memory Management Library
License:  MIT
Group:    System/Libraries
Url:      https://github.com/intel/gmmlib
Source:   %name-%version.tar
BuildRequires: cmake rpm-macros-cmake gcc-c++
%description
The Intel(R) Graphics Memory Management Library provides device specific and buffer
management for the Intel(R) Graphics Compute Runtime for OpenCL(TM) and 
the Intel(R) Media Driver for VAAPI.

%package -n libigdgmm%soversion
Summary:  Intel(R) Graphics Memory Management Library
Group:    System/Libraries
%description -n libigdgmm%soversion
The Intel(R) Graphics Memory Management Library provides device specific and buffer
management for the Intel(R) Graphics Compute Runtime for OpenCL(TM) and
the Intel(R) Media Driver for VAAPI.

%package devel
Summary: Development files for %name
Group: Development/C
%description devel
This package provides the development environment for %name

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_STATIC_LIBS=OFF
%cmake_build

%install
%cmakeinstall_std
rm -f %buildroot/%_libdir/*.a

%files -n libigdgmm%soversion
%_libdir/*.so.%{soversion}*

%files devel
%doc README.rst
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Thu Mar 30 2023 Anton Farygin <rider@altlinux.ru> 22.3.5-alt1
- 22.3.5

* Tue Jan 17 2023 Anton Farygin <rider@altlinux.ru> 22.3.3-alt1
- 22.3.3

* Thu Nov 24 2022 Anton Farygin <rider@altlinux.ru> 22.3.1-alt1
- 22.3.1

* Mon Nov 07 2022 Anton Farygin <rider@altlinux.ru> 22.3.0-alt1
- 22.3.0

* Sun Oct 16 2022 Anton Farygin <rider@altlinux.ru> 22.2.1-alt1
- 22.2.1

* Wed Oct 05 2022 Anton Farygin <rider@altlinux.ru> 22.2.0-alt1
- 22.1.3 -> 22.2.0

* Fri May 27 2022 Anton Farygin <rider@altlinux.ru> 22.1.3-alt1
- 22.1.3

* Mon Apr 04 2022 Anton Farygin <rider@altlinux.ru> 22.1.2-alt1
- 22.1.2

* Mon Mar 14 2022 Anton Farygin <rider@altlinux.ru> 22.1.0-alt1
- 22.0.2 -> 22.1.0

* Wed Feb 02 2022 Anton Farygin <rider@altlinux.ru> 22.0.2-alt1
- 22.0.2

* Sun Jan 09 2022 Anton Farygin <rider@altlinux.ru> 22.0.1-alt1
- 22.0.1

* Fri Dec 31 2021 Anton Farygin <rider@altlinux.ru> 22.0.0-alt1
- 22.0.0

* Sun Dec 05 2021 Anton Farygin <rider@altlinux.ru> 21.3.3-alt1
- 21.3.3

* Sun Nov 07 2021 Anton Farygin <rider@altlinux.ru> 21.3.2-alt1
- 21.3.2

* Tue Oct 12 2021 Anton Farygin <rider@altlinux.ru> 21.3.1-alt1
- 21.3.1

* Mon Sep 06 2021 Anton Farygin <rider@altlinux.ru> 21.2.2-alt1
- 21.2.2

* Wed Jul 07 2021 Anton Farygin <rider@altlinux.ru> 21.2.1-alt1
- 21.2.1

* Tue May 11 2021 Anton Farygin <rider@altlinux.ru> 21.1.3-alt1
- 21.1.3

* Fri Apr 09 2021 Anton Farygin <rider@altlinux.org> 21.1.1-alt1
- 21.1.1

* Sat Jan 02 2021 Anton Farygin <rider@altlinux.ru> 20.4.1-alt1
- 20.4.1

* Mon Nov 23 2020 Anton Farygin <rider@altlinux.ru> 20.3.3-alt1
- 20.3.3

* Wed Sep 30 2020 Anton Farygin <rider@altlinux.ru> 20.3.2-alt1
- 20.3.2

* Tue Sep 15 2020 Anton Farygin <rider@altlinux.ru> 20.2.5-alt1
- 20.2.5

* Wed Aug 19 2020 Anton Farygin <rider@altlinux.ru> 20.2.4-alt1
- 20.2.4

* Mon Jun 29 2020 Anton Farygin <rider@altlinux.ru> 20.2.2-alt1
- 20.2.2

* Tue Apr 07 2020 Anton Farygin <rider@altlinux.ru> 20.1.1-alt1
- 20.1.1

* Mon Jan 13 2020 Anton Farygin <rider@altlinux.ru> 19.4.1-alt1
- 19.4.1

* Wed Nov 13 2019 Anton Farygin <rider@altlinux.ru> 19.3.4-alt1
- 19.3.4

* Fri Oct 04 2019 Anton Farygin <rider@altlinux.ru> 19.3.2-alt1
- 19.3.2

* Wed Sep 11 2019 Anton Farygin <rider@altlinux.ru> 19.2.4-alt1
- 19.2.4

* Thu Aug 15 2019 Anton Farygin <rider@altlinux.ru> 19.2.3-alt1
- 19.2.3

* Sat May 18 2019 Anton Farygin <rider@altlinux.ru> 19.1.2-alt1
- 19.1.2

* Mon Feb 18 2019 Anton Farygin <rider@altlinux.ru> 18.4.1-alt1
- 18.4.1

* Mon Oct 08 2018 Anton Farygin <rider@altlinux.ru> 18.3.0-alt1
- first build for ALT

