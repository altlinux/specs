Name: drumstick
Version: 2.9.1
Release: alt1

Summary: MIDI C++ Libraries for Qt
License: GPLv3
Group: System/Libraries
Url: https://drumstick.sourceforge.net/

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Core5Compat)
BuildRequires: pkgconfig(Qt6DBus)
BuildRequires: pkgconfig(Qt6Linguist)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(fluidsynth)

%package -n libdrumstick
Summary: MIDI C++ Libraries for Qt
Group: System/Libraries

%package -n libdrumstick-widgets
Summary: MIDI Widget Library for Qt
Group: System/Libraries

%package devel
Summary: Developer files for %name
Group: Development/Other

%package examples
Summary: Set of example programs using drumstick
Group: Sound

%define desc\
Drumstick is a set of MIDI libraries using C++/Qt idioms and style.\
Includes a C++ wrapper around the ALSA library sequencer interface:\
ALSA sequencer provides software support for MIDI technology on Linux.\
A complementary library provides classes for processing SMF file formats.\
A multiplatform realtime MIDI I/O library and a GUI Widgets libraries\
are also provided.

%description %desc

%description -n libdrumstick %desc

%description -n libdrumstick-widgets %desc
This package contains MIDI Widget Library for Qt

%description devel %desc
This package contains development part of drumstick.

%description examples %desc
This package contains set of example programs using drumstick

%prep
%setup

%build
%cmake -DUSE_SONIVOX=OFF -DUSE_PULSEAUDIO=OFF -DUSE_DBUS=ON -DBUILD_DOCS=OFF
%cmake_build

%install
%cmakeinstall_std

%files -n libdrumstick
%exclude %_libdir/libdrumstick-widgets.so.*
%_libdir/libdrumstick-*.so.*
%_libdir/drumstick2

%files -n libdrumstick-widgets
%_libdir/libdrumstick-widgets.so.*
%_libdir/qt6/*/*/libdrumstick-*.so

%files devel
%_libdir/libdrumstick-*.so
%_pkgconfigdir/drumstick-*.pc
%_libdir/cmake/drumstick
%_includedir/drumstick.h
%_includedir/drumstick

%files examples
%_bindir/drumstick-*
%_datadir/drumstick
%_datadir/metainfo/*.drumstick-*.xml
%_datadir/mime/packages/*.xml
%_iconsdir/*/*/*/*.*
%_desktopdir/*.desktop

%changelog
* Thu Nov 14 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.9.1-alt1
- 2.9.1 released

* Mon Sep 23 2019 Oleg Solovyov <mcpain@altlinux.org> 1.1.3-alt1
- update to 1.1.3

* Fri Nov 03 2017 Oleg Solovyov <mcpain@altlinux.org> 1.1.0-alt1
- update to 1.1.0

* Fri Nov 03 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.2-alt2
- fix build

* Thu May 26 2016 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1
- initial build
