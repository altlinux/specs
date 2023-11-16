%define polkit_qt5_agent_major 1
%define polkit_qt5_gui_major 1
%define polkit_qt5_core_major 1

Name: polkit-qt5
Version: 0.175.0
Release: alt1

Summary: Qt 5 bindings for PolicyKit
License: GPL-2.0-or-later
Group: System/Libraries

Url: https://invent.kde.org/libraries/polkit-qt-1
# Source-url: https://invent.kde.org/libraries/polkit-qt-1/-/archive/v%version/polkit-qt-1-v%version.tar.gz
Source: polkit-qt-1-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules cmake
BuildRequires: libpolkit1-devel
BuildPreReq: qt5-base-devel
BuildPreReq: kde-common-devel

%description
Polkit-qt5 is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package -n libpolkit-qt5-agent
Summary: %summary
Group: System/Libraries

%description -n libpolkit-qt5-agent
%summary.

%package -n libpolkit-qt5-core
Summary: %summary
Group: System/Libraries

%description -n libpolkit-qt5-core
%summary.

%package -n libpolkit-qt5-gui
Summary: %summary
Group: System/Libraries

%description -n libpolkit-qt5-gui
%summary.

%package -n libpolkitqt5-qt5-devel
Summary: Development files for PolicyKit Qt 5 bindings
Group: Development/KDE and QT
Requires: libpolkit-qt5-agent
Requires: libpolkit-qt5-core
Requires: libpolkit-qt5-gui
Provides: polkitqt5-devel

%description -n libpolkitqt5-qt5-devel
%summary.

%prep
%setup -n polkit-qt-1-%version

%build
%cmake \
	-DBUILD_EXAMPLES:BOOL=OFF \
	-DLIB_DESTINATION=%_libdir \
	#
%cmake_build

# Remove installdox file - it is not necessary here
rm -fv html/installdox

%install
%cmake_install

%files -n libpolkit-qt5-agent
%_libdir/libpolkit-qt5-agent-1.so.%{polkit_qt5_agent_major}*

%files -n libpolkit-qt5-core
%_libdir/libpolkit-qt5-core-1.so.%{polkit_qt5_core_major}*

%files -n libpolkit-qt5-gui
%_libdir/libpolkit-qt5-gui-1.so.%{polkit_qt5_gui_major}*

%files -n libpolkitqt5-qt5-devel
%doc AUTHORS README
%_includedir/polkit-qt5-1/
%_libdir/libpolkit-qt5-core-1.so
%_libdir/libpolkit-qt5-gui-1.so
%_libdir/libpolkit-qt5-agent-1.so
%_libdir/pkgconfig/polkit-qt5-1.pc
%_libdir/pkgconfig/polkit-qt5-core-1.pc
%_libdir/pkgconfig/polkit-qt5-gui-1.pc
%_libdir/pkgconfig/polkit-qt5-agent-1.pc
%_libdir/cmake/PolkitQt5-1/

%changelog
* Thu Nov 16 2023 Anton Midyukov <antohami@altlinux.org> 0.175.0-alt1
- new version (0.175.0) with rpmgs script
- update Url
- cleanup spec

* Thu Dec 16 2021 Anton Midyukov <antohami@altlinux.org> 0.114.0-alt1
- new version (0.114.0) with rpmgs script
- cleanup spec

* Tue Jul 21 2020 Michael Shigorin <mike@altlinux.org> 0.112.0-alt4
- explicit BR: rpm-macros-cmake cmake
- minor spec cleanup

* Thu Dec 27 2018 Michael Shigorin <mike@altlinux.org> 0.112.0-alt3
- adapted for e2kv4 and lcc-1.23

* Mon Sep 18 2017 Michael Shigorin <mike@altlinux.org> 0.112.0-alt2
- E2K: explicit -std=c++11

* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.112.0-alt1
- built for ALT Linux
  + based on mageia spec for 0.112.0-4.mga5
  + thanks glebfm@ for cmake-related fixup
