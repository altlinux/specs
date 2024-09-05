%define qdoc_found %{expand:%%(if [ -e %_dqt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module dqtmultimedia
%def_disable bootstrap
%def_enable pulse

Name: dqt5-multimedia
Version: 5.15.13
Release: alt0.dde.1

Group: System/Libraries
Summary: Qt5 - Multimedia support
Url: http://qt.io/
License: LGPLv2 / GPLv3

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-build-ubt rpm-macros-dqt5
BuildRequires: gcc-c++ glibc-devel dqt5-base-devel dqt5-xmlpatterns-devel dqt5-declarative-devel
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
BuildRequires(pre): dqt5-tools
%endif

# find libraries
%add_findprov_lib_path %_dqt5_libdir

%description
The Qt Multimedia module provides a rich feature set that enables you to
easily take advantage of a platforms multimedia capabilites and hardware.
This ranges from the playback and recording of audio and video content to
the use of available devices like cameras and radios.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: dqt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: dqt5-base-devel
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
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libdqt5-multimedia
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libdqt5-core = %_dqt5_version
# gstreamer plugins may be required for proper audio and video playback
Requires: gst-plugins-base1.0 gst-plugins-good1.0 gst-plugins-bad1.0 gst-plugins-ugly1.0 gst-libav
Provides: dqt5-multimedia = %EVR
#Provides: qml(QtMultimedia)
AutoProv: no,lib
%description -n libdqt5-multimedia
%summary

%prep
%setup -n %qt_module-everywhere-src-%version
syncqt.pl-dqt5 -version %version

%build
%qmake_dqt5 GST_VERSION=1.0
%make_build
%if_disabled bootstrap
%if %qdoc_found
export QT_HASH_SEED=0
%make docs
%endif
%endif

%install
%install_dqt5
%if_disabled bootstrap
%if %qdoc_found
%make INSTALL_ROOT=%buildroot install_docs ||:
%endif
%endif


%files common

%files -n libdqt5-multimedia
%doc LICENSE*EXCEPT*
%_dqt5_libdir/libQt?Multimedia.so.*
%_dqt5_libdir/libQt?MultimediaQuick.so.*
%_dqt5_libdir/libQt?MultimediaWidgets.so.*
%_dqt5_libdir/libQt?MultimediaGstTools.so.*
%_dqt5_archdatadir/qml/QtAudioEngine/
%_dqt5_archdatadir/qml/QtMultimedia/
%_dqt5_plugindir/audio/
%_dqt5_plugindir/mediaservice/
%_dqt5_plugindir/playlistformats/

%files devel
%_dqt5_headerdir/QtMultimedia*/
%_dqt5_libdir/lib*.so
%_dqt5_libdatadir/lib*.so
%_dqt5_libdir/lib*.prl
%_dqt5_libdatadir/lib*.prl
%_dqt5_libdir/cmake/Qt*/
%_dqt5_libdir/pkgconfig/Qt*.pc
%_dqt5_archdatadir/mkspecs/modules/*.pri

%files doc
%if_disabled bootstrap
%if %qdoc_found
%_dqt5_docdir/*
%endif
%endif
%_dqt5_examplesdir/*

%changelog
* Thu Jul 25 2024 Leontiy Volodin <lvol@altlinux.org> 5.15.13-alt0.dde.1
- fork qtbase for separate deepin buildings (ALT #48138)

* Thu Apr 04 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.13-alt1
- new version

* Wed Jan 10 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.12-alt1
- new version

* Wed Nov 22 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.11-alt1
- new version

* Mon Jul 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.10-alt1
- new version

* Wed Apr 26 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.9-alt1
- new version

* Wed Jan 18 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.8-alt1
- new version

* Tue Nov 15 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.7-alt1
- new version

* Fri Oct 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.6-alt1
- new version

* Mon Jul 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt1
- new version

* Fri Nov 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.1-alt2
- add compatibility provides

* Thu Sep 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.1-alt1
- new version

* Fri Jul 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Mon Jun 22 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.9-alt1
- new version

* Thu Apr 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Thu Feb 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Mon Oct 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Mon Jun 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Wed Mar 06 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Fri Aug 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt1%ubt
- new version

* Mon Jun 18 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt2%ubt
- rebuild with new ffmpeg

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt1%ubt
- new version

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Fri Jan 19 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt3%ubt
- fix requires

* Thu Jan 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.9.3-alt2%ubt
- Added runtime dependencies on gstreamer plugins.

* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Wed Aug 23 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt2%ubt
- allow to build without pulseaudio

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1%ubt
- new version

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Tue Jul 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Mon May 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt2
- build with gstreamer-1.0

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Tue Jun 03 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Mon Feb 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Thu Dec 12 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt0.M70P.1
- built for M70P

* Mon Oct 28 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build

