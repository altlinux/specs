%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: libarchive-qt
Version: 2.0.8
Release: alt1

Summary: Qt-based archiving solution with libarchive backend
License: LGPL-3.0-or-later
Group: System/Libraries
Url: https://gitlab.com/marcusbritanicus/libarchive-qt

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(Qt6Core)

%description
This is a simple archiving library for Qt mainly based on libarchive.
Currently it supports the following archive/compression formats:
Gzip, BZip2, LZMA2, LZip (needs lzlib or lzip binary), LZ4, Cpio, AR,
ISO9660, PAX, Shar, Zip, 7Zip, Tar.

Following formats have read (extraction) support have limited support
using extrnal binary: LZip, LZop, LrZip.

This package provides the %name shared library.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This is a simple archiving library for Qt mainly based on libarchive.
Currently it supports the following archive/compression formats:
Gzip, BZip2, LZMA2, LZip (needs lzlib or lzip binary), LZ4, Cpio, AR,
ISO9660, PAX, Shar, Zip, 7Zip, Tar.

Following formats have read (extraction) support have limited support
using extrnal binary: LZip, LZop, LrZip.

This package provides the files necessary for development with
%name.

%package -n archiver
Summary: Binary archiver based on %name
Group: File tools
Requires: %name = %version-%release

%description -n archiver
This is a simple archiving library for Qt mainly based on libarchive.
Currently it supports the following archive/compression formats:
Gzip, BZip2, LZMA2, LZip (needs lzlib or lzip binary), LZ4, Cpio, AR,
ISO9660, PAX, Shar, Zip, 7Zip, Tar.

Following formats have read (extraction) support have limited support
using extrnal binary: LZip, LZop, LrZip.

This package provides the standalone archiver binary based on %name.

%prep
%setup
rm -rfv archiver/archiver

%build
%meson \
       -Duse_qt_version=qt6 \
       -Dinstall_static=false
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc ChangeLog LICENSE README.md
%_libdir/libarchiveqt6.so.2
%_libdir/libarchiveqt6.so.2.0.8

%files -n archiver
%_bindir/archiver

%files devel
%_includedir/libarchiveqt.h
%_libdir/libarchiveqt6.so
%_pkgconfigdir/archiveqt6.pc

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 2.0.8-alt1
- Initial build for Sisyphus
