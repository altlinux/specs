# TODO: use system sqlite

%def_disable static
# Enable or disable clang compiler...
%ifarch %e2k
%def_without clang
%else
%def_with clang
%endif

Name: tdlib
Version: 1.8.0
Release: alt1.1

Summary: Cross-platform library for building Telegram clients

License: Boost
Group: Development/C++
Url: https://github.com/tdlib/td

ExcludeArch: %ix86

# Source-url: %url/archive/v%version.tar.gz#/%name-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

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

%package devel-static
Summary: Static libraries for %name
Group: Development/C++
Requires: %name-devel = %EVR

%description devel
%summary.

%description devel-static
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

%cmake -DCMAKE_INSTALL_LIBDIR=%_lib
%cmake_build

%install
%cmakeinstall_std

%if_disabled static
rm -fv %buildroot%_libdir/*.a
%endif

#check
# inet only
#./BUILD/test/run_all_tests --filter -client

%files
%doc LICENSE_1_0.txt
%doc README.md CHANGELOG.md
%_libdir/libtd*.so.%version

%files devel
%_includedir/td
%_libdir/libtd*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/Td

%if_enabled static
%files devel-static
%_libdir/libtd*.a
%endif

%changelog
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
