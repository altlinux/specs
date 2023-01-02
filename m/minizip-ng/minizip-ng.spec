%define rname minizip
%define sover 3

%filter_from_provides /^pkgconfig(%rname)/d

Name: %rname-ng
Version: %sover.0.8
Release: alt1

Summary: Fork of the popular zip manipulation library found in the zlib distribution
License: Zlib
Group: System/Libraries

Url: https://github.com/zlib-ng/%name/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/zlib-ng/%name/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: bzlib-devel
BuildRequires: cmake >= 3.13
BuildRequires: gcc-c++
BuildRequires: liblzma-devel
BuildRequires: libssl-devel
BuildRequires: libzstd-devel
BuildRequires: zlib-devel

%description
Fork of the popular zip manipulation library found in the zlib distribution.

Features:

 * Creating and extracting zip archives.
 * Adding and removing entries from zip archives.
 * Read and write raw zip entry data.
 * Reading and writing zip archives from memory.
 * Zlib, BZIP2, and LZMA compression methods.
 * Password protection through Traditional PKWARE and WinZIP AES encryption.
 * Buffered streaming for improved I/O performance.
 * NTFS timestamp support for UTC last modified, last accessed, and creation dates.
 * Disk split support for splitting zip archives into multiple files.
 * Preservation of file attributes across file systems.
 * Follow and store symbolic links.
 * Unicode filename support through UTF-8 encoding.
 * Legacy character encoding support CP437, CP932, CP936, CP950.
 * Turn off compilation of compression, decompression, or encryption.
 * Windows (Win32 & WinRT), macOS and Linux platform support.
 * Streaming interface for easy implementation of additional platforms.
 * Support for Apple's compression library ZLIB implementation.
 * Zero out local file header information.
 * Zip/unzip of central directory to reduce size.
 * Ability to generate and verify CMS signature for each entry.
 * Recover the central directory if it is corrupt or missing.
 * Example minizip command line tool.

%package -n lib%rname%sover
Summary: Fork of the popular zip manipulation library found in the zlib distribution
Group: System/Libraries

%description -n lib%rname%sover
Fork of the popular zip manipulation library found in the zlib distribution.

Features:

 * Creating and extracting zip archives.
 * Adding and removing entries from zip archives.
 * Read and write raw zip entry data.
 * Reading and writing zip archives from memory.
 * Zlib, BZIP2, and LZMA compression methods.
 * Password protection through Traditional PKWARE and WinZIP AES encryption.
 * Buffered streaming for improved I/O performance.
 * NTFS timestamp support for UTC last modified, last accessed, and creation dates.
 * Disk split support for splitting zip archives into multiple files.
 * Preservation of file attributes across file systems.
 * Follow and store symbolic links.
 * Unicode filename support through UTF-8 encoding.
 * Legacy character encoding support CP437, CP932, CP936, CP950.
 * Turn off compilation of compression, decompression, or encryption.
 * Windows (Win32 & WinRT), macOS and Linux platform support.
 * Streaming interface for easy implementation of additional platforms.
 * Support for Apple's compression library ZLIB implementation.
 * Zero out local file header information.
 * Zip/unzip of central directory to reduce size.
 * Ability to generate and verify CMS signature for each entry.
 * Recover the central directory if it is corrupt or missing.
 * Example minizip command line tool.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Provides: libminizip2-devel = %EVR
Provides: pkgconfig(%name) = %version
Obsoletes: libminizip2-devel <= 2.10.2
Conflicts: lib%rname-devel

%description -n lib%name-devel
The package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=TRUE
%cmake_build

%install
%cmakeinstall_std

%files -n lib%rname%sover
%doc LICENSE README.md
%_libdir/lib%rname.so.*

%files -n lib%name-devel
%_includedir/*.h
%dir %_libdir/cmake/%rname
%_libdir/cmake/%rname/*.cmake
%_pkgconfigdir/%rname.pc
%_libdir/lib%rname.so

%changelog
* Mon Jan 02 2023 Nazarov Denis <nenderus@altlinux.org> 3.0.8-alt1
- Version 3.0.8

* Sun Oct 16 2022 Nazarov Denis <nenderus@altlinux.org> 3.0.7-alt2
- Improved version 3.0.7

* Fri Oct 14 2022 Nazarov Denis <nenderus@altlinux.org> 3.0.7-alt1
- Version 3.0.7

* Thu Apr 28 2022 Nazarov Denis <nenderus@altlinux.org> 3.0.6-alt1
- Version 3.0.6

* Sun Mar 06 2022 Nazarov Denis <nenderus@altlinux.org> 3.0.5-alt1
- Version 3.0.5

* Mon Nov 29 2021 Nazarov Denis <nenderus@altlinux.org> 3.0.4-alt1
- Version 3.0.4

* Tue Sep 07 2021 Nazarov Denis <nenderus@altlinux.org> 3.0.3-alt1
- Version 3.0.3

* Mon May 10 2021 Nazarov Denis <nenderus@altlinux.org> 3.0.2-alt1
- Version 3.0.2

* Fri Mar 05 2021 Nazarov Denis <nenderus@altlinux.org> 3.0.1-alt1
- Version 3.0.1

* Sun Feb 14 2021 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt2
- Remove library suffix from cmake
- Remove pkgconfig(%rname) from provides in devel package

* Sun Jan 24 2021 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt1
- Change name to %name
- Version 3.0.0

* Wed Oct 28 2020 Nazarov Denis <nenderus@altlinux.org> 2.10.2-alt1
- Version 2.10.2

* Mon Oct 12 2020 Nazarov Denis <nenderus@altlinux.org> 2.9.3-alt1
- Initial build for ALT Linux

