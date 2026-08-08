%define sover 4

Name: lerc
Version: 4.2.0
Release: alt1

Summary: Limited Error Raster Compression library
License: Apache-2.0
Group: Graphics
URL: https://github.com/Esri/lerc

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

%description
Lerc is an open source image or raster format which supports rapid
encoding and decoding for any pixel type. Users set the maximum
compression error per pixel while encoding, so the precision of the
original input image is preserved (within user defined error bounds).

%package -n liblerc%sover
Summary: Shared libraries of lerc
Group: System/Libraries

%description -n liblerc%sover
Lerc is an open source image or raster format which supports rapid
encoding and decoding for any pixel type.
This package contains shared libraries of lerc.

%package -n liblerc-devel
Summary: Development files of lerc
Group: Development/C++
Requires: liblerc%sover = %version-%release

%description -n liblerc-devel
Lerc is an open source image or raster format which supports rapid
encoding and decoding for any pixel type.
This package contains development files of lerc.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%check
libdir=$(dirname "$(find . -name 'libLerc.so.%sover' | head -1)")
g++ %optflags src/LercTest/main.cpp -o lercTest -L"$libdir" -lLerc
LD_LIBRARY_PATH="$libdir" ./lercTest

%files -n liblerc%sover
%_libdir/libLerc.so.%sover

%files -n liblerc-devel
%_includedir/Lerc_c_api.h
%_includedir/Lerc_types.h
%_libdir/libLerc.so
%_pkgconfigdir/Lerc.pc

%changelog
* Sat Aug 08 2026 Anton Farygin <rider@altlinux.org> 4.2.0-alt1
- Initial build for ALT Sisyphus.
