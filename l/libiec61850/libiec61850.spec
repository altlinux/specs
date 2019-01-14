Name:     libiec61850
Version:  1.3.1
Release:  alt1

Summary:  Open source libraries for IEC 61850 and IEC 60870-5-104
License:  GPLv3
Group:    Other
Url:      https://libiec61850.com/libiec61850/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Patch1:   %name-alt-fix-DSO.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
This library provides an implementation of IEC61850 on top of the MMS
(Manufacturing Message Specification) protocol in standard C. It also
provides support for intra-substation communication via GOOSE.

%package devel
Group: Development/C++
Summary: Development files for %name

%description devel
Development files for %name.

%package devel-static
Group: Development/C++
Summary: Development files for %name as static library

%description devel-static
Development files for %name as static library.

%prep
%setup
%patch1 -p2

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/%name
%_datadir/pkgconfig/%name.pc

%files devel-static
%_libdir/*.a

%changelog
* Mon Jan 14 2019 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
