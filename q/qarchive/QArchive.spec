%define qtversion 6
%define nameB QArchive

Name: qarchive
Version: 2.2.9
Release: alt2

Summary: Async C++ Cross-Platform library that modernizes libarchive using Qt.
License: BSD-3-Clause
Group: System/Libraries

Url: https://github.com/antony-jr/QArchive
Vcs: https://github.com/antony-jr/QArchive

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: qt6-base-devel libarchive-devel

%description
%nameB is a cross-platform C++ library that modernizes libarchive.
This library helps you to extract and compress archives supported by libarchive.
The whole library itself is crafted to work perfectly well with the Qt event loop
and thus its a perfect fit for your Qt projects.

%package devel
Group:Development/C++
Summary: Development files for %nameB

%description devel
This package contains libraries and header files for
developing applications that use %nameB.

%prep
%setup

%build
%cmake -DQARCHIVE_QT_VERSION_MAJOR=%qtversion
%cmake_build

%install
%cmake_install
rm %buildroot%_libdir/lib%nameB.a

%files -n %name-devel
%_libdir/cmake/%nameB
%_pkgconfigdir/%nameB.pc
%_includedir/%nameB

%changelog
* Sat Apr 26 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.2.9-alt2
- rebuilt with %%cmake
- removed libQArchive2 subpackage

* Tue Apr 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.2.9-alt1
- Initial build for ALT Linux (git.1467a3ed).
