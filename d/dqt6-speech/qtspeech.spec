%define qdoc_found %{expand:%%(if [ -e %_dqt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module dqtspeech

Name: dqt6-speech
Version: 6.10.3
Release: alt0.dde.1

Group: System/Libraries
Summary: Qt6 - QtSpeech component
Url: http://qt-project.org/
License: (GPL-2.0-only OR LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0) AND BSD-3-Clause

Source: %qt_module-everywhere-src-%version.tar

# find librares
%add_findprov_lib_path %_dqt6_libdir

BuildRequires(pre): rpm-macros-dqt6 dqt6-tools
BuildRequires: cmake glibc-devel dqt6-base-devel dqt6-declarative-devel dqt6-multimedia-devel
BuildRequires: libdqt6-qmlcompiler libdqt6-help
BuildRequires: clang-devel
BuildRequires: pkg-config glib2-devel
BuildRequires: libspeechd-devel libalsa-devel
#BuildRequires: flite-devel

%description
Qt Speech support.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
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

%package -n libdqt6-texttospeech
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-texttospeech
%summary.

%prep
%setup -n %qt_module-everywhere-src-%version
#syncqt.pl-dqt6 -version %version

#mkdir -p config.tests/flite
#ln -s %_includedir config.tests/flite/flite
#ln -s %_includedir src/plugins/tts/flite/flite

%build
#qmake_dqt6 "QMAKE_CXXFLAGS += -I/usr/include/speech-dispatcher"
%DQ6build \
    -DQT_GENERATE_SBOM:BOOL=OFF \
    -DQT_FEATURE_speechd:BOOL=ON \
    #
#    -DQT_FEATURE_flite:BOOL=ON \
%if %qdoc_found
%DQ6make --target docs
%endif

%install
%DQ6install_qt
%if %qdoc_found
#%make -C BUILD DESTDIR=%buildroot install_docs ||:
mkdir -p %buildroot/%_docdir/dqt6/
cp -ar BUILD/share/doc/dqt6/* %buildroot/%_docdir/dqt6/
%endif

%files common
%doc LICENSES/*
%dir %_dqt6_plugindir/texttospeech/

%files -n libdqt6-texttospeech
%_dqt6_libdir/libQt?TextToSpeech.so.*
%_dqt6_plugindir/texttospeech/*.so

%files
%_dqt6_qmldir/QtTextToSpeech/

%files devel
%_dqt6_headerdir/Qt*/
%_dqt6_libdir/libQt*.so
%_dqt6_libdatadir/libQt*.so
%_dqt6_libdir/libQt*.prl
%_dqt6_libdatadir/libQt*.prl
%_dqt6_libdir/cmake/Qt*/
%_dqt6_libdir/pkgconfig/Qt*.pc
%_dqt6_archdatadir/mkspecs/modules/*.pri
%_dqt6_archdatadir/metatypes/qt*.json
%_dqt6_archdatadir/modules/*.json

%files doc
%if %qdoc_found
%_dqt6_docdir/*
%endif
%_dqt6_examplesdir/*

%changelog
* Fri Oct 02 2026 Leontiy Volodin <lvol@altlinux.org> 6.10.3-alt0.dde.1
- fork qt6 for separate deepin packaging (ALT #48138)

* Tue Apr 07 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.3-alt1
- new version

* Thu Feb 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.2-alt1
- new version

* Tue Jan 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.1-alt1
- new version

* Thu Nov 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.3-alt1
- new version

* Tue Aug 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.2-alt1
- new version

* Tue Jun 03 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.1-alt1
- new version

* Thu Feb 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.8.2-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Thu Nov 16 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- initial build
