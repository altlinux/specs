%define _unpackaged_files_terminate_build 1

%def_with check

%define abiversion 0
%define libname libbase64

Name: base64
Version: 0.5.2
Release: alt1

Summary: Fast Base64 stream encoder/decoder with SIMD acceleration
License: BSD-2-Clause
Group: System/Libraries
URL: https://github.com/aklomp/base64
VCS: https://github.com/aklomp/base64.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
%{?_with_check:BuildRequires: ctest}

%description
Fast, SIMD-accelerated Base64 stream encoder/decoder in portable C with
runtime dispatch (SSSE3/SSE4.1/SSE4.2/AVX/AVX2/AVX512 on x86_64, NEON
on aarch64). The plain-C codec is always built in as the baseline
fallback.

%package -n %{libname}_%abiversion
Summary: Shared library for fast Base64 encoding/decoding
Group: System/Libraries

%description -n %{libname}_%abiversion
Runtime shared library libbase64.so.%abiversion.

%package devel
Summary: Development files for libbase64
Group: Development/C
Requires: %{libname}_%abiversion = %EVR

%description devel
Header, pkg-config file, CMake metadata (target aklomp::base64) and
the development symlink for libbase64.

%prep
%setup

%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DBASE64_BUILD_CLI=OFF \
    -DBASE64_WITH_AVX512=OFF \
    -DBASE64_WITH_AVX=OFF \
    -DBASE64_WITH_AVX2=OFF \
    -DBASE64_WERROR=OFF \
    -DBASE64_BUILD_TESTS=%{?_with_check:ON}%{?!_with_check:OFF}
%cmake_build

%install
%cmake_install
# Upstream hasn`t .pc in CMakeLists/Makefile.
# Make our
mkdir -p %buildroot%_pkgconfigdir
cat > %buildroot%_pkgconfigdir/libbase64.pc <<EOF
prefix=%_prefix
libdir=%_libdir
includedir=%_includedir

Name: libbase64
Description: Fast Base64 encoding/decoding
Version: %version
Libs: -L%_libdir -lbase64
Cflags: -I%_includedir
EOF
rm %buildroot%_bindir/test_base64 %buildroot%_bindir/benchmark

%check
ctest --test-dir %_target_platform --output-on-failure

%files -n %{libname}_%abiversion
%doc LICENSE README.md
%_libdir/%libname.so.%abiversion
%_libdir/%libname.so.%abiversion.*

%files devel
%_includedir/libbase64.h
%_libdir/%libname.so
%_pkgconfigdir/libbase64.pc
%_libdir/cmake/base64/

%changelog
* Mon Aug 31 2026 Timofei Fedotov <sovtouch@altlinux.org> 0.5.2-alt1
- Initial build for ALT Sisyphus.
