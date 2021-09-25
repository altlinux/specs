# see also https://github.com/KOLANICH/lib7zip

# TODO: use external shared libp7zip

%define p7zip_version 16.02

Name: lib7zip
Version: 3.0.0
Release: alt2

Summary: C++ library wrapper of 7zip

Group: System/Libraries
License: Mozilla Public License 2.0
Url: https://github.com/stonewell/lib7zip

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/stonewell/lib7zip/archive/%version.tar.gz
Source: %name-%version.tar

# Source1-url: https://github.com/btolab/p7zip/archive/%p7zip_version.tar.gz
Source1: p7zip.tar

Patch1: lib7zip-fix-linking.patch
Patch2: lib7zip-fix-gcc10.patch

BuildRequires: cmake gcc-c++

%description
A library using 7z.dll/7z.so(from 7-Zip) to handle different archive types.
lib7zip is based on 7zip/p7zip source code,
but NOT including any source code from 7zip/p7zip.

%package devel
Summary: Files needed for developing with %name
Group: Development/Other
Requires: %name = %EVR

%description devel
This package contains the files that are needed when building
software that uses %name.

%prep
%setup -a1
%patch1 -p2
%patch2 -p2

%build
%cmake_insource -DBUILD_SHARED_LIB=ON -DP7ZIP_SOURCE_DIR=p7zip
%make_build

%install
install -D -m0644 src/lib7zip.h %buildroot%_includedir/lib7zip.h
mkdir -p %buildroot%_libdir/
cp -a src/lib7zip.so* %buildroot%_libdir/

%files
%doc README.md
%_libdir/%name.so.0
%_libdir/%name.so.0.1

%files devel
%_libdir/%name.so
%_includedir/lib7zip.h

%changelog
* Sat Sep 25 2021 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt2
- fix build with gcc 10

* Sun Dec 16 2018 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- initial build for ALT Sisyphus
