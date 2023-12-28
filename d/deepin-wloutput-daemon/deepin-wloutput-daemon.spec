%define repo dde-wloutput-daemon

%def_disable clang

Name: deepin-wloutput-daemon
Version: 2.0.4
Release: alt1

Summary: Daemon for display settings in the DWayland

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/%repo

Provides: %repo = %EVR

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires: cmake extra-cmake-modules libdtkcore-devel qt5-base-devel dwayland-devel libwayland-client-devel libwayland-server-devel libwayland-cursor-devel libwayland-egl-devel
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
export PATH=%_qt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    %nil
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files
%doc README.md LICENSE
%_bindir/%repo
%_datadir/dbus-1/services/org.deepin.dde.KWayland1.service

%changelog
* Fri Dec 08 2023 Leontiy Volodin <lvol@altlinux.org> 2.0.4-alt1
- Initial build for ALT Sisyphus.
