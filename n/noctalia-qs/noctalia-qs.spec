%define _qt6_qml %_lib/qt6/qml

Name: noctalia-qs
Version: 0.0.10
Release: alt1
License: GPL-3.0 and LGPL-3.0

Summary: Flexible toolkit for making desktop shells with QtQuick

Group: Graphical desktop/Other

Url: https://github.com/noctalia-dev/noctalia-qs
Vcs: https://github.com/noctalia-dev/noctalia-qs.git

Source: %name-%version.tar

Conflicts: quickshell

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake

BuildRequires: qt6-base-devel qt6-tools-devel
BuildRequires: qt6-declarative-devel

BuildRequires: pkgconfig(Qt6WaylandClient)
BuildRequires: pkgconfig(Qt6ShaderTools)
BuildRequires: pkgconfig(Qt6Svg)

BuildRequires: pkgconfig(jemalloc)
BuildRequires: pkgconfig(CLI11)

BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(pam)

BuildRequires: pkgconfig(glib-2.0)

Requires: qt6-declarative

%description
Noctalia-qs is a custom fork of Quickshell.

Quickshell is a toolkit for building status bars, widgets
lockscreens, and other desktop components using QtQuick.

It can be used alongside your wayland compositor or window manager
to build a complete desktop environment.

%prep
%setup

%build
%add_optflags -Wno-error=return-type
%cmake -GNinja \
    -DDISTRIBUTOR="ALT Linux package" \
	-DDISTRIBUTOR_DEBUGINFO_AVAILABLE=YES \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DINSTALL_QML_PREFIX=%_qt6_qml \
	-DINSTALL_QMLDIR=%_qt6_qmldir \
	-DCRASH_REPORTER=OFF
%cmake_build

%install
%cmake_install

%files
%_bindir/qs
%_bindir/quickshell
%_qt6_qmldir/Quickshell
%_desktopdir/dev.noctalia.noctalia-qs.desktop
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Fri Mar 27 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.0.10-alt1
- Initial build
