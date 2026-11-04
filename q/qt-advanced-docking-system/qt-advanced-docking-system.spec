Name: qt-advanced-docking-system
Version: 5.1.1
Release: alt1

Summary: Advanced Docking System for Qt

License: LGPL-2.1-or-later
Group: Development/C++
Url: https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System
# Source-url: https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

%define abiversion 5

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel

%description
Qt Advanced Docking System provides customizable docking layouts for Qt
Widgets applications.

%package -n libqtadvanceddocking%abiversion-qt6
Summary: Qt Advanced Docking System shared library
Group: System/Libraries

%description -n libqtadvanceddocking%abiversion-qt6
Qt Advanced Docking System shared library for Qt 6 applications.

%package -n libqtadvanceddocking-qt6-devel
Summary: Development files for Qt Advanced Docking System
Group: Development/C++
Requires: libqtadvanceddocking%abiversion-qt6 = %EVR

%description -n libqtadvanceddocking-qt6-devel
Headers and CMake configuration files for Qt Advanced Docking System.

%prep
%setup

%build
%cmake \
	-DBUILD_STATIC=OFF \
	-DBUILD_EXAMPLES=OFF \
	-DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
# the license goes to %%doc
rm -rv %buildroot%_datadir/ads/

%files -n libqtadvanceddocking%abiversion-qt6
%_libdir/libqtadvanceddocking-qt6.so.%{abiversion}
%_libdir/libqtadvanceddocking-qt6.so.%{abiversion}.*
%doc LICENSE gnu-lgpl-v2.1.md

%files -n libqtadvanceddocking-qt6-devel
%_includedir/qtadvanceddocking-qt6/
%_libdir/libqtadvanceddocking-qt6.so
%_libdir/cmake/qtadvanceddocking-qt6/

%changelog
* Tue Nov 03 2026 Vitaly Lipatov <lav@altlinux.ru> 5.1.1-alt1
- new version (5.1.1)

