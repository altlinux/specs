
%global qt_module dqtdeclarative

%define optflags_lto %nil

Name: dqt5-declarative
Version: 5.15.13
Release: alt0.dde.1
# %%if "%%version" == "%%{get_version dqt5-tools-common}"
%def_disable bootstrap
# %%else
# %%def_enable bootstrap
# %%endif

Group: System/Libraries
Summary: Qt5 - QtDeclarative component
Url: http://qt.io/
License:  LGPL-2.1 with Qt-LGPL-exception-1.1 or LGPL-3.0-only

Source: %qt_module-everywhere-src-%version.tar
Source10: rpm-build-qml.tar
Source20: kde-qt-5.15.tar
Source1: qml
Source2: qml.env
Source3: find-provides.sh
Source4: find-requires.sh
#
Patch10: Link-with-libatomic-on-riscv32-64.patch
Patch11: alt-remove-createSize.patch
Patch12: alt-multiscreen-applet-sigsegv-fix.patch

%include %SOURCE1
%qml_req_skipall 0
%qml_add_req_nover Qt.test.qtestroot
%define __find_provides %SOURCE3
%define __find_requires %SOURCE4
%add_findprov_lib_path %_dqt5_libdir

BuildRequires(pre): rpm-macros-dqt5
# BuildRequires(pre): dqt5-tools-common
BuildRequires: rpm-build-python3
BuildRequires: gcc-c++ glibc-devel dqt5-base-devel
# %%if_disabled bootstrap
# BuildRequires: dqt5-tools
# %%endif

%description
%summary


%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: dqt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: dqt5-base-devel rpm-build-dqml
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

%package -n libdqt5-qml
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libdqt5-core = %_dqt5_version
Obsoletes: libdqt5-v8 < %version-%release
#Conflicts: dqt5-quickcontrols < 5.7
Provides: dqt5-qtdeclarative = %version-%release
%description -n libdqt5-qml
%summary

%package -n libdqt5-quick
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libdqt5-core = %_dqt5_version
# Provides: libQtQuick5 = %%version-release
%description -n libdqt5-quick
%summary

%package -n libdqt5-quickparticles
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libdqt5-core = %_dqt5_version
%description -n libdqt5-quickparticles
%summary

%package -n libdqt5-quicktest
Group: System/Libraries
Summary: Qt5 - library
# Provides: qml(Qt.test.qtestroot)
Requires: %name-common = %EVR
Requires: libdqt5-core = %_dqt5_version
%description -n libdqt5-quicktest
%summary

%package -n libdqt5-quickwidgets
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libdqt5-core = %_dqt5_version
%description -n libdqt5-quickwidgets
%summary

%package -n libdqt5-quickshapes
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libdqt5-core = %_dqt5_version
%description -n libdqt5-quickshapes
%summary

%package -n libdqt5-qmlmodels
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libdqt5-core = %_dqt5_version
%description -n libdqt5-qmlmodels
%summary

%package -n libdqt5-qmlworkerscript
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libdqt5-core = %_dqt5_version
%description -n libdqt5-qmlworkerscript
%summary

%package -n rpm-build-dqml
Group: Development/Other
Summary: RPM helper macros to rebuild QML packages
%description -n rpm-build-dqml
These helper macros provide possibility to rebuild
QML modules by some Alt Linux Team Policy compatible way.

%prep
%include %SOURCE2
%setup -n %qt_module-everywhere-src-%version -a10 -a20
mv rpm-build-qml src/
ls -1d kde-qt-5.15/*.patch | sort | \
while read p; do
    echo $p
    patch -p1 < $p
done
#
%patch10 -p1
%patch11 -p1
%patch12 -p1
sed -i -E 's|MODULE_VERSION[[:space:]]+.*$|MODULE_VERSION = %version|' .qmake.conf
syncqt.pl-dqt5 -version %version
mkdir bin_add
ln -s %__python3 bin_add/python

%build
%define qdoc_found %{expand:%%(if [ -e %_dqt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}

export PATH=$PWD/bin_add:$PATH
%qmake_dqt5
%make_build
%if %qdoc_found
%make docs
%endif

#build rpm-build-dqml
export BUILDFLAGS="-I../../include/QtQml/%version -I../../include/QtQml/%version/QtQml -I../../include/QtQml"
pushd src/rpm-build-qml
%qmake_dqt5 rpmbqml-qmlinfo.pro
%make_build
popd

%install
%install_dqt5
%if %qdoc_found
%make INSTALL_ROOT=%buildroot install_docs ||:
%endif

#install rpm-build-dqml
pushd src/rpm-build-qml
install -pD -m755 rpmbqml-qmlinfo %buildroot%_bindir/rpmbdqml-qmlinfo
install -pD -m755 rpmbqml-prov-enum.pl %buildroot%_bindir/rpmbdqml-prov-enum.pl
install -pD -m755 qml.prov %buildroot%_rpmlibdir/dqml.prov
install -pD -m755 qml.prov.files %buildroot%_rpmlibdir/dqml.prov.files
install -pD -m755 qml.req %buildroot%_rpmlibdir/dqml.req
install -pD -m755 qml.req.files %buildroot%_rpmlibdir/dqml.req.files
popd

mkdir -p %buildroot%_rpmmacrosdir/
cat %SOURCE1 | sed 's|define[[:space:]][[:space:]]*||' >> %buildroot%_rpmmacrosdir/dqml
cat %SOURCE2 >> %buildroot%_rpmmacrosdir/dqml.env

%files common
%doc LICENSE.*EXCEPT*
%doc dist/changes*
%dir %_dqt5_qmldir/
%dir %_dqt5_qmldir/Qt/
%dir %_dqt5_qmldir/Qt/labs/
%dir %_dqt5_qmldir/QtQml/
%dir %_dqt5_qmldir/QtQuick/
%dir %_dqt5_plugindir/qmltooling/


%files doc
%if %qdoc_found
%_dqt5_docdir/*
%endif
%_dqt5_examplesdir/*

%files -n libdqt5-qml
%_dqt5_libdir/libQt5Qml.so.*
%_dqt5_qmldir/builtins.qmltypes
%_dqt5_qmldir/Qt/labs/animation/
%_dqt5_qmldir/Qt/labs/folderlistmodel/
%_dqt5_qmldir/Qt/labs/qmlmodels/
%_dqt5_qmldir/Qt/labs/settings/
%_dqt5_qmldir/Qt/labs/sharedimage/
%_dqt5_qmldir/Qt/labs/wavefrontmesh/
%_dqt5_qmldir/Qt/test/qtestroot/
%_dqt5_qmldir/QtQml/*
%_dqt5_qmldir/QtQuick/LocalStorage/
%_dqt5_qmldir/QtQuick/Layouts/
%_dqt5_qmldir/QtQuick/Shapes/
%files -n libdqt5-quick
%_dqt5_libdir/libQt5Quick.so.*
%_dqt5_qmldir/QtQuick.2/
%_dqt5_qmldir/QtQuick/Window.2/

%files -n libdqt5-quickparticles
%_dqt5_libdir/libQt5QuickParticles.so.*
%_dqt5_qmldir/QtQuick/Particles.2/
%files -n libdqt5-quicktest
%_dqt5_libdir/libQt5QuickTest.so.*
%_dqt5_qmldir/QtTest/
%files -n libdqt5-quickwidgets
%_dqt5_libdir/libQt5QuickWidgets.so.*
%files -n libdqt5-quickshapes
%_dqt5_libdir/libQt5QuickShapes.so.*
%files -n libdqt5-qmlmodels
%_dqt5_libdir/libQt5QmlModels.so.*
%files -n libdqt5-qmlworkerscript
%_dqt5_libdir/libQt5QmlWorkerScript.so.*


%files devel
%_bindir/qml*
%_dqt5_plugindir/qmltooling/*
%_dqt5_bindir/qml*
%_dqt5_libdir/libQt*.so
%_dqt5_libdatadir/libQt*.so
%_dqt5_libdir/libQt*.prl
%_dqt5_libdatadir/libQt*.prl
%_dqt5_headerdir/Qt*/
%_dqt5_archdatadir/mkspecs/modules/*.pr*
%_dqt5_archdatadir/mkspecs/features/*.pr*
%_dqt5_libdir/metatypes/qt5qml*.json
%_dqt5_libdir/metatypes/qt5quick*.json
%_dqt5_libdir/cmake/Qt*/
%_dqt5_libdir/pkgconfig/Qt?Qml*.pc
%_dqt5_libdir/pkgconfig/Qt?Quick*.pc

%files devel-static
%_dqt5_libdir/libQt?QmlDevTools.a
%_dqt5_libdatadir/libQt?QmlDevTools.a
%_dqt5_libdir/libQt?PacketProtocol.a
%_dqt5_libdatadir/libQt?PacketProtocol.a
%_dqt5_libdir/libQt?QmlDebug.a
%_dqt5_libdatadir/libQt?QmlDebug.a

%files -n rpm-build-dqml
%doc src/rpm-build-qml/LICENSE
%_rpmmacrosdir/dqml
%_rpmmacrosdir/dqml.env
%_rpmlibdir/dqml.req
%_rpmlibdir/dqml.req.files
%_rpmlibdir/dqml.prov
%_rpmlibdir/dqml.prov.files
%_bindir/rpmbdqml-prov-enum.pl
%_bindir/rpmbdqml-qmlinfo

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

* Tue Feb 14 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.8-alt2
- update fixes from kde/qt-5.15

* Wed Jan 18 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.8-alt1
- new version

* Fri Dec 23 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.7-alt5
- update kde/qt-5.15 changes

* Thu Dec 15 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.7-alt4
- optimize provides generator (thanks iv@alt) (closes: 44642)

* Thu Dec 01 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.7-alt3
- revert KDE 7f067fa8a52

* Thu Nov 17 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.7-alt2
- automate bootstrap mode

* Tue Nov 15 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.7-alt1
- new version

* Fri Oct 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.6-alt1
- new version

* Tue Aug 16 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt2
- build docs

* Mon Jul 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Tue May 17 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt9
- update fixes from kde/qt-5.15

* Wed Feb 02 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 5.15.2-alt8
- Broke infinite loop in qml.prov triggered in vtk-9.1.0.

* Tue Feb 01 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt7
- update fixes from kde/qt-5.15

* Mon Jan 24 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt6
- update fixes from kde/qt-5.15

* Wed Dec 08 2021 Slava Aseev <ptrnine@altlinux.org> 5.15.2-alt5
- fix segfault after toggle the "Show Background" on applet

* Fri Oct 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt4
- build without LTO enabled
- update fixes from kde/qt-5.15

* Mon Jul 19 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt3
- add fixes from kde/qt-5.15

* Fri Feb 19 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt2
- build docs

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt1
- new version

* Thu Sep 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.1-alt1
- new version

* Thu Jul 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Fri Jul 03 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.9-alt2
- build docs

* Mon Jun 22 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.9-alt1
- new version

* Sat May 30 2020 Nikita Ermakov <arei@altlinux.org> 5.12.8-alt3
- link with libatomic on riscv32/64

* Thu Apr 16 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt2
- build docs

* Thu Apr 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Tue Mar 17 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt4
- build docs

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt3
- build docs

* Thu Feb 27 2020 Oleg Solovyov <mcpain@altlinux.org> 5.12.7-alt2
- fix automatic qml provides

* Thu Feb 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Fri Dec 13 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt3
- build with python3

* Fri Oct 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt2
- build docs

* Mon Oct 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Thu Jun 27 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt2
- provide qt5-qtdeclarative and libQtQuick5

* Mon Jun 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1
- new version

* Thu Aug 16 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt2
- build docs

* Fri Aug 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt1
- new version

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt1
- new version

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1
- new version

* Wed Mar 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1.2
- build docs

* Mon Feb 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1.1
- don't build docs

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1
- new version

* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1
- new version

* Wed Oct 25 2017 Oleg Solovyov <mcpain@altlinux.org> 5.9.2-alt3
- add rpm-build-qml package

* Mon Oct 23 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt2
- build docs

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1
- new version

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Thu Mar 31 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt2
- build docs

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Thu Oct 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt2
- force SSE2 compile flags for ix86

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Mon Jul 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Fri Jun 05 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Tue Feb 24 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Fri Dec 12 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Tue Sep 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Wed Jun 25 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Wed Jun 04 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt2
- build docs

* Mon Jun 02 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Wed Feb 12 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1.M70P.2
- build docs

* Mon Nov 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1.M70P.1
- built for M70P

* Thu Oct 24 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2
- build docs

* Thu Sep 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
