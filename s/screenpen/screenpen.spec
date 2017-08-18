Summary: ROSA ScreenPen
Name: screenpen
Version: 0.0.3
Release: alt1
License: GPLv3+
Group: Graphics
Url: http://www.rosalab.ru/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: https://abf.io/uxteam/screenpen-devel/archive/screenpen-devel-v%version.tar.gz
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(Qt5Widgets)

%description
ROSA on-screen drawing application for presentations.

%prep
%setup -n screenpen-devel-v%version

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DLIBRARY_INSTALL_DIR=%_lib
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/%name

%changelog
* Fri Aug 18 2017 Anton Midyukov <antohami@altlinux.org> 0.0.3-alt1
- Initial build for ALT Sisyphus.
