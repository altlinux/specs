%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%define optflags_lto -ffat-lto-objects

%global qt_module qtmultimedia
%def_disable bootstrap
%def_enable pulse

Name: qt6-multimedia
Version: 6.4.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - Multimedia support
Url: http://qt.io/
License:  GPL-3.0-only or LGPL-3.0-only

Provides: qml6(QtMultimedia)
# gstreamer plugins may be required for proper audio and video playback
Requires: gst-plugins-base1.0 gst-plugins-good1.0 gst-plugins-bad1.0 gst-plugins-ugly1.0 gst-libav

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6
BuildRequires: cmake glibc-devel
BuildRequires: rpm-build-qml6
BuildRequires: qt6-base-devel qt6-declarative qt6-declarative-devel qt6-shadertools-devel qt6-svg-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libavformat-devel libavcodec-devel libswresample-devel libswscale-devel libavutil-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-app-1.0)
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
%if_enabled pulse
BuildRequires: pkgconfig(libpulse) pkgconfig(libpulse-mainloop-glib)
%endif
BuildRequires: pkgconfig(openal)
BuildRequires: pkgconfig(xv)
%if_disabled bootstrap
BuildRequires(pre): qt6-tools
%endif

%description
The Qt Multimedia module provides a rich feature set that enables you to
easily take advantage of a platforms multimedia capabilites and hardware.
This ranges from the playback and recording of audio and video content to
the use of available devices like cameras and radios.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt6-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt6-base-devel
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
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libqt6-multimedia
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-multimedia
%summary

%package -n libqt6-multimediaquick
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-multimediaquick
%summary

%package -n libqt6-multimediawidgets
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-multimediawidgets
%summary

%package -n libqt6-spatialaudio
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-spatialaudio
%summary


%prep
%setup -n %qt_module-everywhere-src-%version

%build
%Q6build
%if %qdoc_found
%make -C BUILD docs
%endif

%install
%Q6install_qt
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot install_docs ||:
%endif

# relax depends on plugins files
for f in %buildroot/%_libdir/cmake/Qt?*/{*,}/Qt*Targets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

%files common
%doc LICENSES/*

%files
%doc *LICENSE*
%_qt6_archdatadir/qml/QtMultimedia/
#%_qt6_plugindir/audio/
#%_qt6_plugindir/mediaservice/
#%_qt6_plugindir/playlistformats/
%_qt6_plugindir/multimedia/

%files -n libqt6-multimedia
%_qt6_libdir/libQt?Multimedia.so.*
%files -n libqt6-multimediaquick
%_qt6_libdir/libQt?MultimediaQuick.so.*
%files -n libqt6-multimediawidgets
%_qt6_libdir/libQt?MultimediaWidgets.so.*
%files -n libqt6-spatialaudio
%_qt6_libdir/libQt?SpatialAudio.so.*

%files devel
%_qt6_headerdir/QtMultimedia*/
%_qt6_headerdir/QtSpatialAudio/
%_qt6_libdir/lib*.so
%_qt6_libdir/lib*.a
%_qt6_libdatadir/lib*.so
%_qt6_libdatadir/lib*.a
%_qt6_libdir/lib*.prl
%_qt6_libdatadir/lib*.prl
%_qt6_libdir/cmake/Qt*/
%_qt6_archdatadir/mkspecs/modules/*.pri
%_qt6_libdir/metatypes/qt6*.json
%_qt6_datadir/modules/*.json
%_pkgconfigdir/Qt?*.pc

%files doc
%if_disabled bootstrap
%if %qdoc_found
%_qt6_docdir/*
%endif
%endif
%_qt6_examplesdir/*

%changelog
* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 25 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Tue Dec 07 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Tue Dec 07 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.1-alt1
- initial build
