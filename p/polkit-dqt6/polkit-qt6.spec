# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define polkit_qt6_agent_major 1
%define polkit_qt6_gui_major 1
%define polkit_qt6_core_major 1

Name: polkit-dqt6
Version: 0.175.0
Release: alt0.dde.2

Summary: Qt 6 PolicyKit bindings fork for DDE
License: GPL-2.0-or-later
Group: System/Libraries

Url: https://invent.kde.org/libraries/polkit-qt-1
# Source-url: https://invent.kde.org/libraries/polkit-qt-1/-/archive/v%version/polkit-qt-1-v%version.tar.gz
Source: polkit-dqt-1-%version.tar

# provide libraries
%add_findprov_lib_path %_dqt6_libdir

BuildRequires(pre): rpm-macros-dqt6
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules cmake
BuildRequires: libpolkit1-devel
BuildRequires: libvulkan-devel
BuildPreReq: dqt6-base-devel
# BuildPreReq: kde-common-devel

%description
Polkit-qt6 is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package -n libpolkit-dqt6-agent
Summary: %summary
Group: System/Libraries

%description -n libpolkit-dqt6-agent
%summary.

%package -n libpolkit-dqt6-core
Summary: %summary
Group: System/Libraries

%description -n libpolkit-dqt6-core
%summary.

%package -n libpolkit-dqt6-gui
Summary: %summary
Group: System/Libraries

%description -n libpolkit-dqt6-gui
%summary.

%package -n libpolkitqt6-dqt6-devel
Summary: Development files for PolicyKit Qt 6 bindings fork
Group: Development/KDE and QT
Requires: libpolkit-dqt6-agent
Requires: libpolkit-dqt6-core
Requires: libpolkit-dqt6-gui

%description -n libpolkitqt6-dqt6-devel
%summary.

%prep
%setup -n polkit-dqt-1-%version
sed -i '/Requires:/d' *.pc.cmake

%build
%DQ6build \
	-DBUILD_EXAMPLES:BOOL=OFF \
	-DCMAKE_INSTALL_LIBDIR=%_lib/dqt6/lib \
	-DCMAKE_INSTALL_INCLUDEDIR=include/dqt6 \
	-DQT_MAJOR_VERSION=6 \
	#

# Remove installdox file - it is not necessary here
rm -fv html/installdox

%install
%DQ6install

%files -n libpolkit-dqt6-agent
%_dqt6_libdir/libpolkit-qt6-agent-1.so.%{polkit_qt6_agent_major}*

%files -n libpolkit-dqt6-core
%_dqt6_libdir/libpolkit-qt6-core-1.so.%{polkit_qt6_core_major}*

%files -n libpolkit-dqt6-gui
%_dqt6_libdir/libpolkit-qt6-gui-1.so.%{polkit_qt6_gui_major}*

%files -n libpolkitqt6-dqt6-devel
%doc AUTHORS README
%_dqt6_headerdir/polkit-qt6-1/
%_dqt6_libdir/libpolkit-qt6-core-1.so
%_dqt6_libdir/libpolkit-qt6-gui-1.so
%_dqt6_libdir/libpolkit-qt6-agent-1.so
%_dqt6_libdir/pkgconfig/polkit-qt6-1.pc
%_dqt6_libdir/pkgconfig/polkit-qt6-core-1.pc
%_dqt6_libdir/pkgconfig/polkit-qt6-gui-1.pc
%_dqt6_libdir/pkgconfig/polkit-qt6-agent-1.pc
%_dqt6_libdir/cmake/PolkitQt6-1/

%changelog
* Wed Sep 24 2025 Leontiy Volodin <lvol@altlinux.org> 0.175.0-alt0.dde.2
- build required packages with dQt instead default Qt

* Wed Sep 03 2025 Leontiy Volodin <lvol@altlinux.org> 0.175.0-alt0.dde.1
- fork qt6 for separate deepin packaging (ALT #48138)
- enable vulkan support

* Thu Nov 16 2023 Anton Midyukov <antohami@altlinux.org> 0.175.0-alt1
- Initial build
