%define soversion 2
%define qtversion 6
%define nameB QArchive

Name: qarchive
Version: 2.2.9
Release: alt4

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

%package -n lib%name%soversion
Group: System/Libraries
Summary: %nameB library

%description -n lib%name%soversion
Async C++ Cross-Platform library that modernizes libarchive using Qt.

%prep
%setup

%build
%cmake -DQARCHIVE_QT_VERSION_MAJOR=%qtversion -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install
cd %buildroot%_libdir/
mv lib%nameB.so lib%nameB.so.%version
ln -s lib%nameB.so.%version lib%nameB.so.%soversion
ln -s lib%nameB.so.%soversion lib%nameB.so

%files -n %name-devel
%_libdir/cmake/%nameB
%_pkgconfigdir/%nameB.pc
%_includedir/%nameB
%_libdir/lib%nameB.so

%files -n lib%name%soversion
%_libdir/lib%nameB.so.%soversion
%_libdir/lib%nameB.so.%soversion.*

%changelog
* Thu May 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.2.9-alt4
- change type of library (ALT #54072)

* Wed Apr 30 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.2.9-alt3
- added static library

* Sat Apr 26 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.2.9-alt2
- rebuilt with %%cmake
- removed libQArchive2 subpackage

* Tue Apr 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.2.9-alt1
- Initial build for ALT Linux (git.1467a3ed).
