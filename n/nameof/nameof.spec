%define _unpackaged_files_terminate_build 1

Name: nameof
Version: 0.11.0
Release: alt1

Summary: Header-only C++17 library for obtaining expression and type names
Summary(ru_RU.UTF-8): Заголовочная библиотека C++17 для получения имён выражений и типов
License: MIT
Group: Development/C++
Url: https://github.com/Neargye/nameof
Vcs: https://github.com/Neargye/nameof.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildPreReq: cmake >= 3.22
BuildPreReq: ctest gcc-c++ libfmt-devel pkg-config

%description
Nameof is a header-only C++17 library for obtaining names of variables,
types, functions, macros, and enum values. It supports compile-time name
extraction and dynamic type names through RTTI.

%description -l ru_RU.UTF-8
Nameof — заголовочная библиотека C++17 для получения имён переменных,
типов, функций, макросов и значений перечислений. Поддерживает получение
имён на этапе компиляции и имён динамических типов с помощью RTTI.

%package -n lib%name-devel
Summary: Header-only C++17 library for obtaining expression and type names
Summary(ru_RU.UTF-8): Заголовочная библиотека C++17 для получения имён выражений и типов
Group: Development/C++

%description -n lib%name-devel
Nameof is a header-only C++17 library for obtaining names of variables,
types, functions, macros, and enum values. This package contains the
header, CMake and pkg-config metadata, documentation, and examples.

%description -n lib%name-devel -l ru_RU.UTF-8
Nameof — заголовочная библиотека C++17 для получения имён переменных,
типов, функций, макросов и значений перечислений. Пакет содержит
заголовочный файл, метаданные CMake и pkg-config, документацию и примеры.

%prep
%setup

%build
# Keep all installed metadata architecture-independent and relocatable.
%cmake \
    -DCMAKE_INSTALL_LIBDIR=share \
    -DCMAKE_INSTALL_INCLUDEDIR=include \
    -DCMAKE_INSTALL_DATADIR=share \
    -DNAMEOF_OPT_INSTALL=ON \
    -DNAMEOF_OPT_BUILD_EXAMPLES=OFF \
    -DNAMEOF_OPT_BUILD_TESTS=ON \
    -DNAMEOF_TEST_REQUIRE_FMT=ON
%cmake_build

%install
%cmake_install

%check
# Compile-fail tests match English compiler diagnostics.
export LC_ALL=C
%ctest --no-tests=error

# Check the installed CMake package, not the source-tree target.
%cmake -S test/cmake-consumer -B %_cmake__builddir/consumer \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_CXX_STANDARD_REQUIRED=ON \
    -Dnameof_DIR=%buildroot%_datadir/cmake/%name
cmake --build %_cmake__builddir/consumer --parallel %_smp_build_ncpus
%ctest --test-dir %_cmake__builddir/consumer --no-tests=error

export PKG_CONFIG_PATH=
export PKG_CONFIG_LIBDIR=%buildroot%_datadir/pkgconfig
unset PKG_CONFIG_SYSROOT_DIR
pkg-config --validate %name
test "$(pkg-config --modversion %name)" = %version
g++ %optflags -std=c++17 $(pkg-config --cflags %name) \
    test/cmake-consumer/main.cpp -o %_cmake__builddir/pkgconfig-consumer
%_cmake__builddir/pkgconfig-consumer

%files -n lib%name-devel
%doc README.md doc example
%_includedir/%name.hpp
%dir %_datadir/cmake/%name
%_datadir/cmake/%name/nameofConfig.cmake
%_datadir/cmake/%name/nameofConfigVersion.cmake
%_datadir/pkgconfig/%name.pc
%dir %_datadir/%name
%doc %_datadir/%name/LICENSE

%changelog
* Thu Nov 05 2026 Georgij Tsarin <crystarm@altlinux.org> 0.11.0-alt1
- Initial build for Sisyphus.

