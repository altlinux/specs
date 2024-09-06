%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtspeech

Name: qt6-speech
Version: 6.7.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - QtSpeech component
Url: http://qt-project.org/
License: (GPL-2.0-only OR LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0) AND BSD-3-Clause

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake glibc-devel qt6-base-devel qt6-declarative-devel qt6-multimedia-devel
BuildRequires: pkg-config glib2-devel
BuildRequires: libspeechd-devel libalsa-devel
#BuildRequires: flite-devel

%description
Qt Speech support.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt6-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: qt6-base-devel
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

%package -n libqt6-texttospeech
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-texttospeech
%summary.

%prep
%setup -n %qt_module-everywhere-src-%version
#syncqt.pl-qt6 -version %version

#mkdir -p config.tests/flite
#ln -s %_includedir config.tests/flite/flite
#ln -s %_includedir src/plugins/tts/flite/flite

%build
#qmake_qt6 "QMAKE_CXXFLAGS += -I/usr/include/speech-dispatcher"
%Q6build \
    -DQT_FEATURE_speechd:BOOL=ON \
    #
#    -DQT_FEATURE_flite:BOOL=ON \
%if %qdoc_found
%make -C BUILD docs
%endif

%install
%Q6install_qt
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot install_docs ||:
%endif

%files common
%doc LICENSES/*
%dir %_qt6_plugindir/texttospeech/

%files -n libqt6-texttospeech
%_qt6_libdir/libQt?TextToSpeech.so.*
%_qt6_plugindir/texttospeech/*.so

%files
%_qt6_qmldir/QtTextToSpeech/

%files devel
%_qt6_headerdir/Qt*/
%_qt6_libdir/libQt*.so
%_qt6_libdatadir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/cmake/Qt*/
%_qt6_libdir/pkgconfig/Qt*.pc
%_qt6_archdatadir/mkspecs/modules/*.pri
%_qt6_archdatadir/metatypes/qt*.json
%_qt6_archdatadir/modules/*.json

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif
%_qt6_examplesdir/*

%changelog
* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Thu Nov 16 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- initial build
