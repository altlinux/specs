# TODO:
# GIF: wait for giflib >=5.2.1
# https://bugzilla.altlinux.org/36576
# SVG: libresvg (not now)

%define pre %nil
Name: libsail
Version: 1.2.0
Release: alt1

Summary: Squirrel Abstract Image Library

License: MIT
Group: System/Libraries
Url: https://github.com/HappySeaFox/sail

# Source-url: https://github.com/HappySeaFox/sail/archive/refs/tags/v%version%pre.tar.gz
Source: %name-%version.tar
# https://github.com/HappySeaFox/sail/commit/c2b218ebb804e7ecb2e9a10cd92027ffeba5f4a7
Patch0: libsail-munit-drop-ATOMIC_VAR_INIT.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake ctest
#BuildRequires: libgif-devel
BuildRequires: libpng-devel libtiff-devel libjpeg-devel libwebp-devel libjasper-devel libavif-devel

%description
Squirrel Abstract Image Library
The missing small and fast image decoding library for humans (not for machines).

%package devel
Summary: Header files for the %name library
Group: Development/C++

%description devel
Header files for the %name library.

%prep
%setup
%patch0 -p1

%build
%cmake_insource \
	-DSAIL_EXCEPT_CODECS="gif" \
	-DSAIL_BUILD_EXAMPLES=OFF
%make_build

%check
# use the codecs from buildroot (%%check runs after %%install)
export SAIL_CODECS_PATH=%buildroot%_libdir/sail/codecs
%__ctest --output-on-failure --parallel %_smp_build_ncpus

%install
%makeinstall_std
%if %_lib == "lib64"
mv %buildroot/usr/lib/cmake %buildroot%_libdir/
%endif

%files
%doc README.md
%_bindir/sail
%_libdir/libsail*.so.*
%dir %_libdir/sail/
%dir %_libdir/sail/codecs/
%_libdir/sail/codecs/*.so
%_libdir/sail/codecs/*.info
%_datadir/sail/
%_man1dir/*

%files devel
%_libdir/cmake/*
%_libdir/libsail*.so
%_pkgconfigdir/*.pc
%_includedir/sail/

%changelog
* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0
- add upstream patch: drop deprecated ATOMIC_VAR_INIT in munit (fix build with gcc 15)
- run tests in %%check

* Sun Mar 08 2026 Vitaly Lipatov <lav@altlinux.ru> 0.9.10-alt1
- new version 0.9.10

* Wed Mar 12 2025 Vitaly Lipatov <lav@altlinux.ru> 0.9.8-alt1
- new version 0.9.8 (with rpmrb script)

* Tue Dec 03 2024 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- new version 0.9.7 (with rpmrb script)

* Mon Feb 19 2024 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version (0.9.1) with rpmgs script

* Sat Aug 05 2023 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt2.rc3
- update to 0.9.0-rc3
- add BR: libavif-devel

* Mon Jan 03 2022 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- initial build for ALT Sisyphus
