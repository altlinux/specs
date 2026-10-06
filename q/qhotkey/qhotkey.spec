%define abiversion 1

Name: qhotkey
Version: 1.5.0
Release: alt1

Summary: Global shortcut and hotkey library for Qt applications

License: BSD-3-Clause
Group: System/Libraries
URL: https://github.com/Skycoder42/QHotkey
# Source-url: https://github.com/Skycoder42/QHotkey/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Patch0: qhotkey-pkgconfig.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: pkgconfig(Qt6Core) pkgconfig(Qt6Gui) pkgconfig(x11)

%description
QHotkey provides global shortcuts for Qt applications, including when
the application is not active.

%package -n libqhotkey%abiversion
Summary: Global shortcut library for Qt 6
Group: System/Libraries

%description -n libqhotkey%abiversion
Shared QHotkey library for Qt 6 applications.

%package -n libqhotkey-devel
Summary: Development files for QHotkey
Group: Development/C++

%description -n libqhotkey-devel
Headers and CMake configuration for developing Qt 6 applications with QHotkey.

%prep
%setup
%patch0 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DQT_DEFAULT_MAJOR_VERSION=6 \
    -DBUILD_SHARED_LIBS=ON \
    -DQHOTKEY_INSTALL=ON \
    -DQHOTKEY_EXAMPLES=OFF \
    %nil
%cmake_build

%install
%cmake_install

%files -n libqhotkey%abiversion
%doc LICENSE
%_libdir/libqhotkey.so.%abiversion
%_libdir/libqhotkey.so.%version

%files -n libqhotkey-devel
%_includedir/QHotkey
%_includedir/qhotkey.h
%_libdir/libqhotkey.so
%_libdir/cmake/QHotkey/
%_pkgconfigdir/qhotkey.pc

%changelog
* Tue Oct 06 2026 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- Initial build for ALT Sisyphus.
