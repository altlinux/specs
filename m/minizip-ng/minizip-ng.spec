%define compat_name minizip
%define sover 4

%filter_from_provides /^pkgconfig(%compat_name)/d

Name: %compat_name-ng
Version: 4.0.3
Release: alt1

Summary: Fork of the popular zip manipulation library found in the zlib distribution
License: Zlib
Group: System/Libraries

Url: https://github.com/zlib-ng/%name/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/zlib-ng/%name/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

Patch0: %name-soversion-alt.patch

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

%package -n lib%name%sover
Summary: Fork of the popular zip manipulation library found in the zlib distribution
Group: System/Libraries

%description -n lib%name%sover
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

%package -n lib%compat_name%sover
Summary: Fork of the popular zip manipulation library found in the zlib distribution
Group: System/Libraries

%description -n lib%compat_name%sover
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
Obsoletes: libminizip2-devel <= 2.10.2

%description -n lib%name-devel
The package contains libraries and header files for
developing applications that use %name.

%package -n lib%name-compat-devel
Summary: Development files for %compat_name
Group: Development/C
Conflicts: lib%compat_name-devel

%description -n lib%name-compat-devel
The package contains libraries and header files for
developing applications that use %compat_name.

%prep
%setup
%patch0 -p1

%build

# Build normal versions

%define _cmake__builddir %_target_platform

%cmake \
	-DCMAKE_INSTALL_LIBDIR:PATH=%_libdir \
	-DBUILD_SHARED_LIBS:BOOL=TRUE \
	-DMZ_COMPAT:BOOL=FALSE
%cmake_build

# Build compat versions

%define _cmake__builddir %_target_platform-compat

%cmake \
	-DCMAKE_INSTALL_LIBDIR:PATH=%_libdir \
	-DBUILD_SHARED_LIBS:BOOL=TRUE \
	-DMZ_COMPAT:BOOL=TRUE
%cmake_build

%install
%define _cmake__builddir %_target_platform
%cmakeinstall_std

%define _cmake__builddir %_target_platform-compat
%cmakeinstall_std

%files -n lib%name%sover
%doc LICENSE README.md
%_libdir/lib%name.so.*

%files -n lib%compat_name%sover
%doc LICENSE README.md
%_libdir/lib%compat_name.so.*

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/*.h
%dir %_libdir/cmake/%name
%_libdir/cmake/%name/%{name}*.cmake
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%files -n lib%name-compat-devel
%dir %_includedir/%compat_name
%_includedir/%compat_name/*.h
%dir %_libdir/cmake/%compat_name
%_libdir/cmake/%compat_name/%{compat_name}*.cmake
%_pkgconfigdir/%compat_name.pc
%_libdir/lib%compat_name.so

%changelog
* Mon Nov 13 2023 Nazarov Denis <nenderus@altlinux.org> 4.0.3-alt1
- New version 4.0.3.

* Sat Aug 05 2023 Nazarov Denis <nenderus@altlinux.org> 4.0.1-alt1
- New version 4.0.1.
- Build also no compat version.

* Sat May 20 2023 Nazarov Denis <nenderus@altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Mon Apr 10 2023 Nazarov Denis <nenderus@altlinux.org> 3.0.10-alt1
- Version 3.0.10

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
- Remove pkgconfig(%compat_name) from provides in devel package

* Sun Jan 24 2021 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt1
- Change name to %name
- Version 3.0.0

* Wed Oct 28 2020 Nazarov Denis <nenderus@altlinux.org> 2.10.2-alt1
- Version 2.10.2

* Mon Oct 12 2020 Nazarov Denis <nenderus@altlinux.org> 2.9.3-alt1
- Initial build for ALT Linux

