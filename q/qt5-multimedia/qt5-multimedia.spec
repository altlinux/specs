
%global qt_module qtmultimedia
%define gname qt5


Name: qt5-multimedia
Version: 5.1.1
Release: alt1

Group: System/Libraries
Summary: Qt5 - Multimedia support
Url: http://qt-project.org/
License: LGPLv2 / GPLv3

Source: %qt_module-opensource-src-%version.tar
BuildRequires: gcc-c++ glibc-devel qt5-base-devel qt5-declarative-devel
BuildRequires: qt5-tools
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gstreamer-0.10)
BuildRequires: pkgconfig(gstreamer-app-0.10)
BuildRequires: pkgconfig(gstreamer-audio-0.10)
BuildRequires: pkgconfig(gstreamer-base-0.10)
BuildRequires: pkgconfig(gstreamer-interfaces-0.10)
BuildRequires: pkgconfig(gstreamer-pbutils-0.10)
BuildRequires: pkgconfig(gstreamer-plugins-bad-0.10)
BuildRequires: pkgconfig(gstreamer-video-0.10)
BuildRequires: pkgconfig(libpulse) pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(openal)
BuildRequires: pkgconfig(xv)

%description
The Qt Multimedia module provides a rich feature set that enables you to
easily take advantage of a platforms multimedia capabilites and hardware.
This ranges from the playback and recording of audio and video content to
the use of available devices like cameras and radios.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: common-licenses
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: %name-devel
%description devel-static
%summary.

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-multimedia
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-multimedia
%summary

%prep
%setup -n %qt_module-opensource-src-%version
syncqt.pl-qt5 \
    -version %version \
    -private \
    -module QtMultimedia \
    -module QtMultimediaWidgets \
    -module QtMultimediaQuick_p \
    #

%build
%qmake_qt5
%make_build
%make docs

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs ||:


%files common

%files -n libqt5-multimedia
%doc LGPL_EXCEPTION.txt
%_qt5_libdir/libQt?Multimedia.so.*
%_qt5_libdir/libQt?MultimediaQuick_p.so.*
%_qt5_libdir/libQt?MultimediaWidgets.so.*
%_qt5_libdir/libqgsttools_p.so.*
%_qt5_archdatadir/qml/QtAudioEngine/
%_qt5_archdatadir/qml/QtMultimedia/
%_qt5_plugindir/audio/
%_qt5_plugindir/mediaservice/
%_qt5_plugindir/playlistformats/

%files devel
%_qt5_headerdir/QtMultimedia*/
%_qt5_libdir/lib*.so
%_qt5_libdir/lib*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_libdir/pkgconfig/Qt*.pc
%_qt5_archdatadir/mkspecs/modules/*.pri

%files doc
%_qt5_docdir/*

%changelog
* Mon Oct 28 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build

