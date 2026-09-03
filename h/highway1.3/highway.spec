
%define major 1
%define minor 3
%define bugfix 0
%define sover %major.%minor

%define rname highway
%define libhwy libhwy%sover
%define libhwy_contrib libhwy_contrib%sover
%define libhwy_test libhwy_test%sover

Name: %rname%sover
Version: %major.%minor.%bugfix
Release: alt1

Group: System/Libraries
Summary: Efficient and performance-portable SIMD wrapper libraries
License: Apache-2.0
URL: https://github.com/google/highway
VCS: https://github.com/google/highway.git

Source: %rname-%version.tar
Patch1: 0001-Detect-clang-19-20-21-also-allow-user-override.patch
Patch2: 0002-Detect-not-yet-released-clang-22-for-users-building-.patch
Patch3: 0003-SVE-still-broken-on-Clang-22-msan-fail-on-svcnt.patch 

BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc cmake gcc-c++
BuildRequires: ctest libgtest-devel

%description
Highway is a C++ libraries that provides portable SIMD/vector intrinsics.

%package -n %libhwy
Summary: %name library
Group: System/Libraries
%description -n %libhwy
%name library.

%package -n %libhwy_contrib
Summary: %name library
Group: System/Libraries
%description -n %libhwy_contrib
%name library.

%package -n %libhwy_test
Summary: %name library
Group: System/Libraries
%description -n %libhwy_test
%name library.

%package devel
Summary: Development files for Highway
Group: Development/C++
Conflicts: highway-devel
%description devel
Development files for Highway libraries.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
# force soname
sed -i '/LIBRARY_SOVERSION/s/${hwy_VERSION_MAJOR}/%sover/' CMakeLists.txt

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DHWY_SYSTEM_GTEST=ON \
    -DHWY_CMAKE_RVV:BOOL=OFF \
%ifarch %ix86
    -DHWY_CMAKE_SSE2=ON \
%endif
%ifarch armh
    -DHWY_CMAKE_ARM7=ON \
%endif
    #

%cmake_build

%install
%cmake_install

mv %buildroot/%_pkgconfigdir/libhwy{,%sover}.pc
mv %buildroot/%_pkgconfigdir/libhwy-contrib{,%sover}.pc
mv %buildroot/%_pkgconfigdir/libhwy-test{,%sover}.pc
install -d %buildroot/%_sysconfdir/alternatives/packages.d/
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name-devel <<__EOF__
%_pkgconfigdir/libhwy.pc %_pkgconfigdir/libhwy%sover.pc %EVR
%_pkgconfigdir/libhwy-contrib.pc %_pkgconfigdir/libhwy-contrib%sover.pc %EVR
%_pkgconfigdir/libhwy-test.pc %_pkgconfigdir/libhwy-test%sover.pc %EVR
__EOF__

%ifnarch armh %ix86
%check
%cmake_build -t test
%endif

%files -n %libhwy
%_libdir/libhwy.so.%sover
%_libdir/libhwy.so.*

%files -n %libhwy_contrib
%_libdir/libhwy_contrib.so.%sover
%_libdir/libhwy_contrib.so.*

%files -n %libhwy_test
%_libdir/libhwy_test.so.%sover
%_libdir/libhwy_test.so.*

%files devel
%config %_sysconfdir/alternatives/packages.d/%name-devel
%_includedir/hwy/
%_libdir/lib*.so
%_pkgconfigdir/libhwy*.pc
%_libdir/cmake/hwy/

%changelog
* Thu Sep 03 2026 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt1
- alternate package

* Fri Apr 24 2026 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Thu Aug 14 2025 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sat Jun 01 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Feb 19 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Thu Aug 31 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- updated to 1.0.7-2-gfed142a

* Sun Jan 29 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3
- enabled %%check for all arches

* Tue Dec 27 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- first build for Sisyphus

