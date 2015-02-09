%define snapshot 20140212

Name: polkit-qt5
Version: 0.112.0
Release: alt1

Summary: Qt 5 bindings for PolicyKit
License: GPLv2+
Group: System/Libraries

Url: https://projects.kde.org/projects/kdesupport/polkit-qt-1
Source0: polkit-qt-1-%version.tar.bz2
Source1: Doxyfile

BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: doxygen
BuildRequires: libpolkit1-devel
BuildPreReq: qt5-base-devel
#BuildPreReq: rpm-build-kf5
BuildPreReq: kde-common-devel

%description
Polkit-qt5 is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

#--------------------------------------------------------------------

%define polkit_qt5_agent_major 1

%package -n libpolkit-qt5-agent
Summary: %summary
Group: System/Libraries

%description -n libpolkit-qt5-agent
%summary.

%files -n libpolkit-qt5-agent
%_libdir/libpolkit-qt5-agent-1.so.%{polkit_qt5_agent_major}*

#--------------------------------------------------------------------

%define polkit_qt5_core_major 1

%package -n libpolkit-qt5-core
Summary: %summary
Group: System/Libraries

%description -n libpolkit-qt5-core
%summary.

%files -n libpolkit-qt5-core
%_libdir/libpolkit-qt5-core-1.so.%{polkit_qt5_core_major}*

#--------------------------------------------------------------------

%define polkit_qt5_gui_major 1

%package -n libpolkit-qt5-gui
Summary: %summary
Group: System/Libraries

%description -n libpolkit-qt5-gui
%summary.

%files -n libpolkit-qt5-gui
%_libdir/libpolkit-qt5-gui-1.so.%{polkit_qt5_gui_major}*

#--------------------------------------------------------------------

%package -n libpolkitqt5-qt5-devel
Summary: Development files for PolicyKit Qt 5 bindings
Group: Development/KDE and QT
Requires: libpolkit-qt5-agent = %version-%release
Requires: libpolkit-qt5-core = %version-%release
Requires: libpolkit-qt5-gui = %version-%release
Provides: polkitqt5-devel  = %version-%release

%description -n libpolkitqt5-qt5-devel
%summary.

%files -n libpolkitqt5-qt5-devel
%doc AUTHORS COPYING README
%_includedir/polkit-qt5-1/
%_libdir/libpolkit-qt5-core-1.so
%_libdir/libpolkit-qt5-gui-1.so
%_libdir/libpolkit-qt5-agent-1.so
%_libdir/pkgconfig/polkit-qt5-1.pc
%_libdir/pkgconfig/polkit-qt5-core-1.pc
%_libdir/pkgconfig/polkit-qt5-gui-1.pc
%_libdir/pkgconfig/polkit-qt5-agent-1.pc
%_libdir/cmake/PolkitQt5-1/

#--------------------------------------------------------------------

%prep
%setup -n polkit-qt-1-%version

%build
%cmake_insource \
	-DBUILD_EXAMPLES:BOOL=OFF \
	-DLIB_DESTINATION=%_libdir \
	#
%make_build
doxygen %SOURCE1

# Remove installdox file - it is not necessary here
rm -fv html/installdox

%install
%makeinstall_std

%changelog
* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.112.0-alt1
- built for ALT Linux
  + based on mageia spec for 0.112.0-4.mga5
  + thanks glebfm@ for cmake-related fixup
