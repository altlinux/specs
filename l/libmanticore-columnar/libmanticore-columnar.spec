Name: libmanticore-columnar
Version: 13.9.0
Release: alt1

Summary: Manticore Columnar Library is a column-oriented storage library

License: Apache-2.0
Group: Text tools
Url: https://github.com/manticoresoftware/columnar

# Source-url: https://github.com/manticoresoftware/columnar/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Patch1: libmanticore-columnar-system-pgm.patch
Patch2: libmanticore-columnar-propagate-skip-knn.patch
Patch3: libmanticore-columnar-respect-embedded-build.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.21
BuildRequires: gcc-c++
BuildRequires: /proc
BuildRequires: libfastpfor-devel
BuildRequires: libpgm-index-legacy-devel >= 2022.08.02
BuildRequires: libstreamvbyte-devel-static

ExclusiveArch: x86_64

%def_without avx

%description
Manticore Columnar Library is a column-oriented storage library,
aiming to provide decent performance with low memory footprint at big data volume.
When used in combination with Manticore Search can be beneficial for faster / lower
resource consumption log/metrics analytics and running log / metric analytics in docker / kubernetes.

%package devel
Summary: API headers for building Manticore Search with columnar support
Group: Development/C++

%description devel
API header files and CMake configuration for building Manticore Search
with columnar library support.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
subst 's|"lib/cmake/columnar"|"%_lib/cmake/columnar"|' CMakeLists.txt

%build
%if_with avx
%global avx_cmake_opts %{nil}
%else
%global avx_cmake_opts -DCOLUMNAR_EMBEDDED_BUILD=ON
%endif

%cmake_insource \
    -DBUILD_TESTING=0 \
    -DSKIP_KNN=ON \
    %{avx_cmake_opts}
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_libdir/
mv %buildroot/usr/share/manticore/modules/*.so %buildroot%_libdir/

# API-only install (headers + cmake config for manticore build)
cmake -S . -B api-build -DAPI_ONLY=ON -DCMAKE_INSTALL_PREFIX=/usr
DESTDIR=%buildroot cmake --install api-build

%files
%doc README.md
%_libdir/lib_manticore_columnar.so
%if_with avx
%_libdir/lib_manticore_columnar_avx2.so
%_libdir/lib_manticore_columnar_avx512.so
%endif
%_libdir/lib_manticore_secondary.so
%if_with avx
%_libdir/lib_manticore_secondary_avx2.so
%_libdir/lib_manticore_secondary_avx512.so
%endif

%files devel
%_includedir/manticore-columnar-api/
%_cmakedir/columnar/

%changelog
* Fri Aug 21 2026 Vitaly Lipatov <lav@altlinux.ru> 13.9.0-alt1
- new version 13.9.0

* Mon Mar 30 2026 Vitaly Lipatov <lav@altlinux.ru> 10.2.0-alt1
- new version 10.2.0
- fix cmake config install path to %%_cmakedir
- remove unused old patch file

* Thu Mar 02 2023 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0 (with rpmrb script)

* Mon Jun 27 2022 Vitaly Lipatov <lav@altlinux.ru> 1.15.4-alt1
- new version 1.15.4 (with rpmrb script)

* Tue Dec 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.12.2-alt1
- initial build for ALT Sisyphus
