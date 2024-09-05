%define repo dde-wloutput-daemon

%def_disable clang

Name: deepin-wloutput-daemon
Version: 2.0.4
Release: alt2

Summary: Daemon for display settings in the DWayland

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-wloutput-daemon

Provides: %repo = %EVR

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires: cmake extra-cmake-modules libdtkcore-devel dqt5-base-devel dwayland-devel libwayland-client-devel libwayland-server-devel libwayland-cursor-devel libwayland-egl-devel
BuildRequires(pre): rpm-build-ninja
%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif

%description
%summary.

%prep
%setup -n %repo-%version

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export PATH=%_dqt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
    -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files
%doc README.md LICENSE
%_bindir/%repo
%_datadir/dbus-1/services/org.deepin.dde.KWayland1.service

%changelog
* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 2.0.4-alt2
- Built via separate qt5 instead system (ALT #48138).

* Fri Dec 08 2023 Leontiy Volodin <lvol@altlinux.org> 2.0.4-alt1
- Initial build for ALT Sisyphus.
