Name: libpgm-index-legacy
Version: 2022.08.02
Release: alt1

Summary: Legacy PGM-index snapshot required by Manticore Columnar

License: Apache-2.0
Group: Development/C++
Url: https://github.com/manticoresoftware/PGM-index

# Source-url: https://github.com/manticoresoftware/PGM-index/archive/5a5a763c7c07e56f56fd33137dcee9f1b3c3b640.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

ExclusiveArch: x86_64

%description
Legacy PGM-index snapshot used by Manticore Columnar.

%package devel
Summary: Header files and CMake configuration for %name
Group: Development/C++

%description devel
Header files and CMake configuration for the legacy PGM-index API
used by Manticore Columnar.

%prep
%setup
subst '/add_subdirectory(test)/d' CMakeLists.txt
subst 's|set(PGM_CMAKE_DIR "lib/cmake/ManticorePGM")|set(PGM_CMAKE_DIR "%_lib/cmake/ManticorePGM")|' CMakeLists.txt

%build
%cmake_insource \
    -DBUILD_PGM_TUNER=OFF \
    -DCMAKE_DISABLE_FIND_PACKAGE_OpenMP=ON

%install
%makeinstall_std

%files devel
%_includedir/manticore-pgm/
%_cmakedir/ManticorePGM/

%changelog
* Mon Aug 24 2026 Vitaly Lipatov <lav@altlinux.ru> 2022.08.02-alt1
- initial package
