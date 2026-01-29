# TODO: use system sqlite

# about versioning:
# https://github.com/tdlib/td/issues/2215

# check tag in Source-url every release

%def_disable static
%def_enable tde2e
# Enable or disable clang compiler...
%ifarch %e2k
%def_without clang
%else
%def_with clang
%endif

Name: tdlib
Version: 1.8.52
Release: alt2

Summary: Cross-platform library for building Telegram clients

License: Boost
Group: Development/C++
Url: https://github.com/tdlib/td

#Source-url: %url/archive/v%version.tar.gz#/%name-%version.tar.gz
# Source-url: https://github.com/tdlib/td/commit/3870c29b158b75ca5e48e0eebd6b5c3a7994a000
Source: %name-%version.tar

Patch: %name-system-crypto.patch

#BuildRequires(pre): rpm-macros-ninja-build
#BuildRequires: ninja-build

BuildRequires: gperftools-devel
BuildRequires: gperf
BuildRequires: libssl-devel
BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: cmake

BuildRequires(pre): rpm-build-intro >= 2.1.5

# Building with default settings require at least 16 GB of free RAM.
# Builds on ARM and other low-memory architectures are failing.
#ExclusiveArch: %ix86 x86_64 arch64
ExcludeArch: armh

# minimalize memory using
%ifarch %ix86 armh
%define optflags_debug -g0
%endif


%if_with clang
BuildRequires: clang
BuildRequires: llvm llvm-devel
# clang-12: error: unsupported argument 'auto' to option 'flto='
%define optflags_lto -flto=thin
%remove_optflags -frecord-gcc-switches
%endif

# use no more than system_memory/6300 build procs (see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
%_tune_parallel_build_by_procsize 6300

%description
TDLib (Telegram Database library) is a cross-platform library for
building Telegram clients. It can be easily used from almost any
programming language.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%package -n tde2e-devel-static
Group: Development/C++
Summary: Development files for tde2e (from tdlib)

%package devel-static
Summary: Static libraries for %name
Group: Development/C++
Requires: %name-devel = %EVR

%description devel
%summary.

%description devel-static
%summary.

%description -n tde2e-devel-static
%summary.

%prep
%setup
%patch -p2

%if_with packaged_sqlite
rm -rfv sqlite/
%endif

%build
%if_with clang
export CC=clang
export CXX=clang++
%endif

%ifarch i586
export LDFLAGS="%{?ldflags} -Wl,--no-as-needed -latomic -Wl,--as-needed"
%endif

%define _cmake__builddir %_target_platform
%cmake -B %_target_platform \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DBUILD_SHARED_LIBS=1 \
  -DBUILD_TESTING=OFF
%cmake_build

%if_enabled tde2e
%define _cmake__builddir %_target_platform-e2e
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_EXE_LINKER_FLAGS:STRING="$LDFLAGS" \
    -DCMAKE_SHARED_LINKER_FLAGS:STRING="$LDFLAGS" \
    -DCMAKE_MODULE_LINKER_FLAGS:STRING="$LDFLAGS" \
    -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=OFF \
    -DCMAKE_C_FLAGS="%optflags -fno-lto" \
    -DCMAKE_CXX_FLAGS="%optflags -fno-lto" \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=%_lib \
    -DBUILD_TESTING=OFF \
    -DTD_ENABLE_JNI=OFF \
    -DTD_ENABLE_DOTNET=OFF \
    -DTD_WITH_ABSEIL=ON \
    -DTD_E2E_ONLY=ON \
    -DTDE2E_ENABLE_INSTALL=ON \
    -DTDE2E_INSTALL_INCLUDES=ON
%cmake_build
%endif

%install
%define _cmake__builddir %_target_platform
%cmake_install --parallel %{?_smp_build_ncpus}
%if_enabled tde2e
%define _cmake__builddir %_target_platform-e2e
%cmake_install --parallel %{?_smp_build_ncpus}
%endif

%if_disabled static
find "%buildroot%_libdir" -type f -name '*.a' \
  ! -path "%buildroot%_libdir/libtde2e.a" \
  ! -path "%buildroot%_libdir/libtdutils.a" \
  -print -delete
%endif

%if_disabled tde2e
rm -f %_libdir/libtde2e.a
rm -f %_libdir/libtdutils.a
%endif

#check
# inet only
#./BUILD/test/run_all_tests --filter -client

%if_enabled tde2e
%files -n tde2e-devel-static
%_pkgconfigdir/tde2e.pc
%_pkgconfigdir/tdutils.pc
%_libdir/cmake/tde2e/
%_libdir/libtde2e.a
%_libdir/libtdutils.a
%_includedir/td/e2e/
%endif

%files
%doc LICENSE_1_0.txt
%doc README.md CHANGELOG.md
%_libdir/libtd*.so.%version

%files devel
%exclude %_pkgconfigdir/tde2e.pc
%exclude %_pkgconfigdir/tdutils.pc
%_includedir/td/tl/
%_includedir/td/telegram/
%_libdir/libtd*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/Td/
%exclude %_libdir/cmake/Td/TdStaticTarget*

%if_enabled static
%files devel-static
%exclude %_libdir/libtde2e.a
%exclude %_libdir/libtdutils.a
%_libdir/libtd*.a
%_libdir/cmake/Td/TdStaticTarget*
%endif

%changelog
* Fri Jan 16 2026 Arseniy Romenskiy <romenskiy@altlinux.org> 1.8.52-alt2
- Add tde2e-devel-static.

* Tue Aug 26 2025 Artem Semenov <savoptik@altlinux.org> 1.8.52-alt1
- Updated to 1.8.52

* Thu Feb 8 2024 Artem Semenov <savoptik@altlinux.org> 1.8.21-alt2
- Disabled provision of static targets to CMake;
- Fix provide libs in devel package (closes: 48693).

* Wed Nov 08 2023 Vitaly Lipatov <lav@altlinux.ru> 1.8.21-alt1
- new version (1.8.21) with rpmgs script

* Wed Aug 02 2023 Vitaly Lipatov <lav@altlinux.ru> 1.8.14-alt1
- new version (1.8.14) with rpmgs script

* Sun Mar 19 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.8.0-alt1.1
- e2k: build without clang

* Sat Mar 11 2023 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Sat Sep 11 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- new version 1.7.0 (with rpmrb script)
- fix build, disable build for armh (due clang segfault)

* Mon Sep 28 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- new version 1.6.0 (with rpmrb script)
- cleanup spec, enable static subpackage
- build with make instead of ninja

* Tue Oct 29 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Thu May 02 2019 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Sun Dec 16 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt2
- build with clang
- disable i586 build

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- initial build for ALT Sisyphus

* Sun Sep 16 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3.0-2
- Fixed issue with crypto policies.

* Sat Sep 15 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3.0-1
- Initial SPEC release.
