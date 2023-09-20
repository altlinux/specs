%define subname		avkys
%define major		9.1
%define libname lib%name

Name: webcamoid
Version: %major.1
Release: alt1

Summary: A webcam funny video tool

Group: Video
License: GPL-3.0-or-later
Url: https://github.com/hipersayanX/webcamoid

Packager: Alexei Mezin <alexvm@altlinux.ru>

# Source-url: https://github.com/webcamoid/webcamoid/archive/%version.tar.gz
Source: %name-%version.tar
Patch0: %{name}_manpath.patch

BuildPreReq: rpm-macros-cmake cmake

BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gstreamer-app-1.0)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libv4l2)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(libvlc)
BuildRequires: pkgconfig(libuvc)
BuildRequires: pkgconfig(libpulse-simple)
BuildRequires: pkgconfig(libkmod)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libpostproc)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pipewire-libs-devel libjack-devel liborc-devel pipewire-libs-devel libalsa-devel

Requires: %libname = %EVR

%description
Webcamoid is a full featured webcam capture application.
Features:
    * Take pictures and record videos with the webcam.
    * Manages multiple webcams.
    * Written in C++/Qt.
    * Custom controls for each webcam.
    * Add funny effects to the webcam.
    * +60 effects available.
    * Effects with live previews.
    * Translated to many languages.
    * Use custom network and local files as capture devices.
    * Capture from desktop.

%package -n %libname
Summary: The webcamoid library
Group: System/Libraries

%description -n %libname
This package contains the library for webcamoid.

%package -n %libname-devel
Summary: Headers for developing programs that will use avkys lib
Group: Development/C++
Requires: %libname = %EVR

%description -n %libname-devel
This package contains the headers that programmers will need to develop
applications which will use avkys library as webcamoid.

%prep
%setup
#patch0 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS TODO README.md
%_bindir/webcamoid
%_desktopdir/webcamoid.desktop
%_iconsdir/hicolor/*/apps/webcamoid.*
%_man1dir/webcamoid.1*
%_libdir/avkys
# libdir/qt5/qml/AkQml
%_datadir/licenses/webcamoid/COPYING
%_datadir/metainfo/io.github.webcamoid.Webcamoid.metainfo.xml

%files -n %libname
%_libdir/lib%subname.so.*
# datadir/licenses/avkys/COPYING

%files -n %libname-devel
%_libdir/*.so

%changelog
* Tue Sep 19 2023 Artyom Bystrov <arbars@altlinux.org> 9.1.1-alt1
- New version

* Thu Feb 24 2022 Alexei Mezin <alexvm@altlinux.org> 9.0.0-alt1
- New version

* Sat Dec 11 2021 Alexei Mezin <alexvm@altlinux.org> 8.8.0-alt2
- Minor fixes in src

* Mon Jul 05 2021 Vitaly Lipatov <lav@altlinux.ru> 8.8.0-alt1
- new version 8.8.0 (with rpmrb script)

* Sun Jul 04 2021 Vitaly Lipatov <lav@altlinux.ru> 8.7.1-alt1
- initial build for ALT Sisyphus

* Tue Feb 18 2020 umeabot <umeabot> 8.7.1-2.mga8
+ Revision: 1539656
- Mageia 8 Mass Rebuild

* Wed Dec 11 2019 zezinho <zezinho> 8.7.1-1.mga8
+ Revision: 1465959
- imported package webcamoid

