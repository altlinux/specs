# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define polkit_qt6_agent_major 1
%define polkit_qt6_gui_major 1
%define polkit_qt6_core_major 1

Name: polkit-qt6
Version: 0.175.0
Release: alt1

Summary: Qt 6 bindings for PolicyKit
License: GPL-2.0-or-later
Group: System/Libraries

Url: https://invent.kde.org/libraries/polkit-qt-1
# Source-url: https://invent.kde.org/libraries/polkit-qt-1/-/archive/v%version/polkit-qt-1-v%version.tar.gz
Source: polkit-qt-1-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules cmake
BuildRequires: libpolkit1-devel
BuildPreReq: qt6-base-devel
BuildPreReq: kde-common-devel

%description
Polkit-qt6 is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package -n libpolkit-qt6-agent
Summary: %summary
Group: System/Libraries

%description -n libpolkit-qt6-agent
%summary.

%package -n libpolkit-qt6-core
Summary: %summary
Group: System/Libraries

%description -n libpolkit-qt6-core
%summary.

%package -n libpolkit-qt6-gui
Summary: %summary
Group: System/Libraries

%description -n libpolkit-qt6-gui
%summary.

%package -n libpolkitqt6-qt6-devel
Summary: Development files for PolicyKit Qt 6 bindings
Group: Development/KDE and QT
Requires: libpolkit-qt6-agent
Requires: libpolkit-qt6-core
Requires: libpolkit-qt6-gui
Provides: polkitqt6-devel

%description -n libpolkitqt6-qt6-devel
%summary.

%prep
%setup -n polkit-qt-1-%version

%build
%cmake \
	-DBUILD_EXAMPLES:BOOL=OFF \
	-DLIB_DESTINATION=%_libdir \
	-DQT_MAJOR_VERSION=6 \
	#
%cmake_build

# Remove installdox file - it is not necessary here
rm -fv html/installdox

%install
%cmake_install

%files -n libpolkit-qt6-agent
%_libdir/libpolkit-qt6-agent-1.so.%{polkit_qt6_agent_major}*

%files -n libpolkit-qt6-core
%_libdir/libpolkit-qt6-core-1.so.%{polkit_qt6_core_major}*

%files -n libpolkit-qt6-gui
%_libdir/libpolkit-qt6-gui-1.so.%{polkit_qt6_gui_major}*

%files -n libpolkitqt6-qt6-devel
%doc AUTHORS README
%_includedir/polkit-qt6-1/
%_libdir/libpolkit-qt6-core-1.so
%_libdir/libpolkit-qt6-gui-1.so
%_libdir/libpolkit-qt6-agent-1.so
%_libdir/pkgconfig/polkit-qt6-1.pc
%_libdir/pkgconfig/polkit-qt6-core-1.pc
%_libdir/pkgconfig/polkit-qt6-gui-1.pc
%_libdir/pkgconfig/polkit-qt6-agent-1.pc
%_libdir/cmake/PolkitQt6-1/

%changelog
* Thu Nov 16 2023 Anton Midyukov <antohami@altlinux.org> 0.175.0-alt1
- Initial build
