%define sover 12

Name: fmt
Version: 12.2.0
Release: alt1
Epoch: 1

Summary: An open-source formatting library for C++
License: BSD
Group: System/Libraries

Vcs: https://github.com/%{name}lib/%name
Url: http://%{name}lib.net/

# https://github.com/%{name}lib/%name/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

# https://github.com/fmtlib/%name/pull/4813
Patch0: %name-12.2.0-fix-fallback-unit128-bitwise-not.patch

BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++

%description
fmt (formerly cppformat) is an open-source formatting library.
It can be used as a fast and safe alternative to printf and IOStreams.

%package -n lib%name%sover
Summary: An open-source formatting library for C++
Group: System/Libraries

%description -n lib%name%sover
fmt (formerly cppformat) is an open-source formatting library.
It can be used as a fast and safe alternative to printf and IOStreams.

%package -n lib%name-devel
Summary: An open-source formatting library for C++
Group: Development/C++

%description -n lib%name-devel
fmt (formerly cppformat) is an open-source formatting library.
It can be used as a fast and safe alternative to printf and IOStreams.

%prep
%setup
%patch0 -p1
%ifarch %e2k
# [  FAILED  ] float_test.isnan
sed -i 's/fegetexceptflag(&fe, FE_ALL_EXCEPT)/fe = 0/' test/format-test.cc
# error: _BitInt is not supported on this target
sed -i 's/FMT_USE_BITINT 1/FMT_USE_BITINT 0/' include/fmt/base.h
%endif

# Remove political badge
sed -i '/\[!\[Support/,+1d' README.md

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DFMT_PKGCONFIG_DIR:PATH=%_pkgconfigdir \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	%nil

%cmake_build

%check
%ctest

%install
%cmake_install
%__rm -f %buildroot%_libdir/lib%name-c.a

%files -n lib%name%sover
%doc CONTRIBUTING.md ChangeLog.md LICENSE README.md
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name
%_cmakedir/%name
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%changelog
* Fri Jun 19 2026 Nazarov Denis <nenderus@altlinux.org> 1:12.2.0-alt1
- New version 12.2.0.

* Tue Dec 09 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1:12.1.0-alt1.2
- e2k build fix

* Tue Nov 25 2025 Nazarov Denis <nenderus@altlinux.org> 1:12.1.0-alt1.1
- Remove illegal political lines from readme

* Wed Oct 29 2025 Nazarov Denis <nenderus@altlinux.org> 1:12.1.0-alt1
- New version 12.1.0.

* Wed Sep 17 2025 Nazarov Denis <nenderus@altlinux.org> 1:12.0.0-alt1
- New version 12.0.0.

* Sun May 04 2025 Nazarov Denis <nenderus@altlinux.org> 1:11.2.0-alt1
- New version 11.2.0.

* Thu Feb 27 2025 Nazarov Denis <nenderus@altlinux.org> 1:11.1.4-alt1
- New version 11.1.4.

* Sun Jan 26 2025 Nazarov Denis <nenderus@altlinux.org> 1:11.1.3-alt1
- New version 11.1.3.

* Mon Jan 13 2025 Nazarov Denis <nenderus@altlinux.org> 1:11.1.2-alt1
- New version 11.1.2.

* Sat Oct 19 2024 Nazarov Denis <nenderus@altlinux.org> 1:11.0.2-alt1
- New version 11.0.2.

* Fri Jan 05 2024 Nazarov Denis <nenderus@altlinux.org> 1:10.2.1-alt1
- New version 10.2.1.

* Tue Jan 02 2024 Nazarov Denis <nenderus@altlinux.org> 1:10.2.0-alt1
- New version 10.2.0.

* Mon Oct 16 2023 Nazarov Denis <nenderus@altlinux.org> 1:10.1.1-alt2
- Fix version (ALT #48029)

* Wed Oct 11 2023 Nazarov Denis <nenderus@altlinux.org> 1:10.1.1-alt1
- New version 10.1.1. (ALT #47948)

* Sat Jul 01 2023 Nazarov Denis <nenderus@altlinux.org> 1:9.1.0-alt1.2
- Fix FTBFS

* Thu May 18 2023 Nazarov Denis <nenderus@altlinux.org> 1:9.1.0-alt1.1
- Rollback to version 9.0.1.

* Wed May 10 2023 Nazarov Denis <nenderus@altlinux.org> 10.0.0-alt1
- Updated to upstream version 10.0.0.

* Sat Aug 27 2022 Nazarov Denis <nenderus@altlinux.org> 9.1.0-alt1
- Updated to upstream version 9.0.1.

* Wed Jul 06 2022 Nazarov Denis <nenderus@altlinux.org> 9.0.0-alt1
- Updated to upstream version 9.0.0.

* Fri Jan 07 2022 Nazarov Denis <nenderus@altlinux.org> 8.1.1-alt1
- Updated to upstream version 8.1.1.

* Sat Nov 06 2021 Nazarov Denis <nenderus@altlinux.org> 8.0.1-alt1
- Updated to upstream version 8.0.1.

* Sun Jan 24 2021 Nazarov Denis <nenderus@altlinux.org> 7.1.3-alt1
- Updated to upstream version 7.1.3.

* Fri Jun 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.1-alt1
- Updated to upstream version 6.2.1.

* Fri Apr 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.0-alt1
- Updated to upstream version 6.2.0.

* Tue Feb 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.2-alt1
- Updated to upstream version 6.1.2.

* Wed Jan 30 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.3.0-alt1
- initial
