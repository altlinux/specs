Name:     libiec61850
Version:  1.6.0
Release:  alt1

Summary:  Open source libraries for IEC 61850 and IEC 60870-5-104
License:  GPL-3.0
Group:    System/Libraries
Url:      https://github.com/mz-automation/libiec61850

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
%global optflags_lto %optflags_lto -ffat-lto-objects
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
* Wed Aug 14 2024 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- New version.

* Sun Jun 09 2024 Andrey Cherepanov <cas@altlinux.org> 1.5.3-alt1
- New version (fixes CVE-2022-21159, CVE-2022-1302, CVE-2021-45769).

* Thu Sep 23 2021 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1
- New version (Fixes: CVE-2020-15158).

* Tue Dec 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.2.1-alt1
- Updated to upstream version 1.4.2.1 (Fixes: CVE-2019-6135, CVE-2019-6136,
  CVE-2019-6138, CVE-2019-6719, CVE-2019-16510, CVE-2019-1010300, CVE-2020-7054).

* Mon Jan 14 2019 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
