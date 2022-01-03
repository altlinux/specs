# TODO: 
# GIF: wait for giflib >=5.2.1
# https://bugzilla.altlinux.org/36576
# SVG: libresvg

%define pre -pre19
Name: libsail
Version: 0.9.0
Release: alt1

Summary: Squirrel Abstract Image Library

License: MIT
Group: System/Libraries
Url: https://github.com/HappySeaFox/sail

# Source-url: https://github.com/HappySeaFox/sail/archive/refs/tags/v%version%pre.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake

BuildRequires: libpng-devel libtiff-devel libjpeg-devel zlib-devel libwebp-devel libjasper-devel

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

%build
%cmake_insource \
	-DSAIL_EXCEPT_CODECS="gif" \
	-DSAIL_BUILD_TESTS=OFF \
	-DSAIL_BUILD_EXAMPLES=OFF
%make_build

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

%files devel
%_libdir/cmake/*
%_libdir/libsail*.so
%_pkgconfigdir/libsail*.pc
%_includedir/sail/

%changelog
* Mon Jan 03 2022 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- initial build for ALT Sisyphus
