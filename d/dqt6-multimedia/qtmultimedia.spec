%define qdoc_found %{expand:%%(if [ -e %_dqt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%define optflags_lto -ffat-lto-objects

%global qt_module dqtmultimedia
%def_disable bootstrap
%def_enable pulse

Name: dqt6-multimedia
Version: 6.7.2
Release: alt0.dde.1

Group: System/Libraries
Summary: Qt6 - Multimedia support
Url: http://qt.io/
License:  GPL-3.0-only or LGPL-3.0-only


Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-dqt6
BuildRequires: cmake glibc-devel
BuildRequires: rpm-build-dqml6
BuildRequires: dqt6-base-devel dqt6-declarative dqt6-declarative-devel dqt6-shadertools-devel dqt6-svg-devel
BuildRequires: libxkbcommon-x11-devel libXrandr-devel
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
BuildRequires(pre): dqt6-tools
%endif

# find libraries
%add_findprov_lib_path %_dqt6_libdir

%description
The Qt Multimedia module provides a rich feature set that enables you to
easily take advantage of a platforms multimedia capabilites and hardware.
This ranges from the playback and recording of audio and video content to
the use of available devices like cameras and radios.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: dqt6-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: dqt6-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: %name-devel
%description devel-static
%summary.

%package doc
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libdqt6-multimedia
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-multimedia
%summary

%package -n libdqt6-multimediaquick
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
Provides: %name = %EVR
Obsoletes: %name < %EVR
Provides: dqml6(QtMultimedia)
AutoProv: yes,noqml6
# gstreamer plugins may be required for proper audio and video playback
Requires: gst-plugins-base1.0 gst-plugins-good1.0 gst-plugins-bad1.0 gst-plugins-ugly1.0 gst-libav
%description -n libdqt6-multimediaquick
%summary

%package -n libdqt6-multimediawidgets
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-multimediawidgets
%summary

%package -n libdqt6-spatialaudio
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-spatialaudio
%summary


%prep
%setup -n %qt_module-everywhere-src-%version

# disable some examples
for e in multimedia/video/qmlvideo multimedia/screencapture ; do
    exam=`basename $e`
    subdir=`dirname $e`
    sed -i "/qt_internal_add_example.*${exam}/d" examples/$subdir/CMakeLists.txt
done

%build
%ifarch %e2k
%add_optflags -mno-sse
%endif
%DQ6build
%if %qdoc_found
%DQ6make --target docs
%endif

%install
%DQ6install_qt
%if %qdoc_found
mkdir -p %buildroot%_dqt6_docdir
cp -a BUILD/share/doc/dqt6/* %buildroot%_dqt6_docdir ||:
%endif

# relax depends on plugins files
for f in %buildroot/%_dqt6_libdir/cmake/Qt?*/{*,}/Qt*Targets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

%files common
%doc LICENSES/*

%files -n libdqt6-multimedia
%_dqt6_libdir/libQt?Multimedia.so.*
%_dqt6_plugindir/multimedia/

%files -n libdqt6-multimediaquick
%_dqt6_libdir/libQt?MultimediaQuick.so.*
%_dqt6_archdatadir/qml/QtMultimedia/

%files -n libdqt6-multimediawidgets
%_dqt6_libdir/libQt?MultimediaWidgets.so.*

%files -n libdqt6-spatialaudio
%_dqt6_libdir/libQt?SpatialAudio.so.*

%files devel
%_dqt6_headerdir/QtMultimedia*/
%_dqt6_headerdir/QtSpatialAudio/
%_dqt6_headerdir/QtQGstreamerMediaPlugin/
%_dqt6_libdir/lib*.so
%_dqt6_libdir/lib*.a
%_dqt6_libdatadir/lib*.so
%_dqt6_libdatadir/lib*.a
%_dqt6_libdir/lib*.prl
%_dqt6_libdatadir/lib*.prl
%_dqt6_libdir/cmake/Qt*/
%_dqt6_archdatadir/mkspecs/modules/*.pri
%_dqt6_archdatadir/metatypes/qt6*.json
%_dqt6_archdatadir/modules/*.json
%_dqt6_libdir/pkgconfig/Qt?*.pc

%files doc
%if_disabled bootstrap
%if %qdoc_found
%_dqt6_docdir/*
%endif
%endif
%_dqt6_examplesdir/*

%changelog
* Fri Dec 13 2024 Leontiy Volodin <lvol@altlinux.org> 6.7.2-alt0.dde.1
- fork Qt6 for separate deepin buildings (ALT #48138)

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Fri Feb 23 2024 Michael Shigorin <mike@altlinux.org> 6.6.2-alt1.1
- E2K: disable SSE due to x86 asm (ilyakurdyukov@)

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 25 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Tue Dec 07 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Tue Dec 07 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.1-alt1
- initial build
