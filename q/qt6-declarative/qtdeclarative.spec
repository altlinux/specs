%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module qtdeclarative
%def_enable bootstrap

%define optflags_lto %nil

Name: qt6-declarative
Version: 6.2.4
Release: alt5

Group: System/Libraries
Summary: Qt6 - QtDeclarative component
Url: http://qt.io/
License:  LGPL-2.1 with Qt-LGPL-exception-1.1 or LGPL-3.0-only

Source: %qt_module-everywhere-src-%version.tar
Source10: rpm-build-qml.tar
Source1: qml6
Source2: qml6.env
Source3: find-provides.sh
Source4: find-requires.sh

%include %SOURCE1
%qml6_req_skipall 0
%qml6_add_req_nover Qt.test.qtestroot
%define __find_provides %SOURCE3
%define __find_requires %SOURCE4

# Automatically added by buildreq on Wed Dec 01 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libdouble-conversion3 libglvnd-devel libgpg-error libqt6-concurrent libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-opengl libqt6-openglwidgets libqt6-shadertools libqt6-sql libqt6-test libqt6-widgets libsasl2-3 libssl-devel libstdc++-devel libvulkan-devel perl pkg-config python-modules python2-base python3 python3-base python3-module-paste qt6-base-common qt6-base-devel rpm-build-file rpm-build-gir rpm-build-python3 rpm-macros-python sh4 tzdata
#BuildRequires: ccmake glslang libGLU-devel libxkbcommon-devel python-modules-compiler python3-dev qt6-shadertools-devel rpm-build-qml tbb-devel
BuildRequires(pre): rpm-macros-qt6
BuildRequires: rpm-build-python3
BuildRequires: gcc-c++ glibc-devel qt6-base-devel qt6-shadertools-devel
BuildRequires: cmake glslang libGLU-devel libxkbcommon-devel
%if_disabled bootstrap
BuildRequires: qt6-tools
BuildRequires: rpm-build-qml6
%endif

%description
%summary


%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt6-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt6-base-devel rpm-build-qml6
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

%package -n rpm-build-qml6
Group: Development/Other
Summary: RPM helper macros to rebuild QML packages
%description -n rpm-build-qml6
These helper macros provide possibility to rebuild
QML modules by some Alt Linux Team Policy compatible way.

%package -n libqt6-qml
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
Obsoletes: libqt6-v8 < %version-%release
Provides: qt6-qtdeclarative = %version-%release
%description -n libqt6-qml
%summary

%package -n libqt6-quick
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
Provides: libQtQuick6 = %version-release
%description -n libqt6-quick
%summary

%package -n libqt6-quickparticles
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickparticles
%summary

%package -n libqt6-quicktest
Group: System/Libraries
Summary: Qt6 - library
Provides: qml(Qt.test.qtestroot)
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quicktest
%summary

%package -n libqt6-quickwidgets
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickwidgets
%summary

%package -n libqt6-quickshapes
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickshapes
%summary

%package -n libqt6-qmlmodels
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-qmlmodels
%summary

%package -n libqt6-qmlworkerscript
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-qmlworkerscript
%summary

%package -n libqt6-quickcontrols2impl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickcontrols2impl
%summary

%package -n libqt6-quickdialogs2
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickdialogs2
%summary

%package -n libqt6-quickdialogs2quickimpl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickdialogs2quickimpl
%summary

%package -n libqt6-quickdialogs2utils
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickdialogs2utils
%summary

%package -n libqt6-quickcontrols2
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickcontrols2
%summary

%package -n libqt6-qmlxmllistmodel
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-qmlxmllistmodel
%summary

%package -n libqt6-qmllocalstorage
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-qmllocalstorage
%summary

%package -n libqt6-quicklayouts
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quicklayouts
%summary

%package -n libqt6-quicktemplates2
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quicktemplates2
%summary

%package -n libqt6-qmlcore
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-qmlcore
%summary

%package -n libqt6-labswavefrontmesh
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-labswavefrontmesh
%summary

%package -n libqt6-labssharedimage
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-labssharedimage
%summary

%package -n libqt6-labssettings
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-labssettings
%summary

%package -n libqt6-labsqmlmodels
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-labsqmlmodels
%summary

%package -n libqt6-labsfolderlistmodel
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-labsfolderlistmodel
%summary libqt6-labsfolderlistmodel

%package -n libqt6-labsanimation
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-labsanimation
%summary

%prep
%include %SOURCE2
%setup -n %qt_module-everywhere-src-%version -a10
# disable deps to qtquick
sed -i '/dynamicscene/d' examples/qml/CMakeLists.txt

mv rpm-build-qml src/
mkdir bin_add
ln -s %__python3 bin_add/python

%build
export PATH=$PWD/bin_add:$PATH
%Q6build
%if_disabled bootstrap
%make -C BUILD docs
%endif

#build rpm-build-qml
export BUILDFLAGS="-I../../include/QtQml/%version -I../../include/QtQml/%version/QtQml -I../../include/QtQml"
pushd src/rpm-build-qml
#qmake_qt6 rpmbqml-qmlinfo.pro
#make_build
popd

%install
%Q6install_qt
%if_disabled bootstrap
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot install_docs ||:
%endif
%endif

#install rpm-build-qml
pushd src/rpm-build-qml

# FIXME rpmbqml-qmlinfo
ln -s /bin/true %buildroot/%_bindir/rpmbqml6-qmlinfo
#install -pD -m755 rpmbqml-qmlinfo %buildroot/%_bindir/rpmbqml6-qmlinfo
# end FIXME
install -pD -m755 rpmbqml6-prov-enum.pl %buildroot/%_bindir/rpmbqml6-prov-enum.pl
install -pD -m755 qml6.prov %buildroot/%_rpmlibdir/qml6.prov
install -pD -m755 qml6.prov.files %buildroot/%_rpmlibdir/qml6.prov.files
install -pD -m755 qml6.req %buildroot/%_rpmlibdir/qml6.req
install -pD -m755 qml6.req.files %buildroot/%_rpmlibdir/qml6.req.files
popd

mkdir -p %buildroot%_rpmmacrosdir/
cat %SOURCE1 | sed 's|define[[:space:]][[:space:]]*||' >> %buildroot%_rpmmacrosdir/qml6
cat %SOURCE2 >> %buildroot%_rpmmacrosdir/qml6.env


%files
%_qt6_qmldir/*

%files common
%doc *LICENSE*
%doc dist/changes*
%dir %_qt6_qmldir/
%dir %_qt6_qmldir/Qt/
%dir %_qt6_qmldir/Qt/labs/
%dir %_qt6_qmldir/QtQml/
%dir %_qt6_qmldir/QtQuick/

%files doc
%if_disabled bootstrap
%_qt6_docdir/*
%endif
%_qt6_examplesdir/*

%files -n libqt6-qml
%_qt6_libdir/libQt?Qml.so.*
%files -n libqt6-quick
%_qt6_libdir/libQt?Quick.so.*
%files -n libqt6-quickparticles
%_qt6_libdir/libQt?QuickParticles.so.*
%files -n libqt6-quicktest
%_qt6_libdir/libQt?QuickTest.so.*
%files -n libqt6-quickwidgets
%_qt6_libdir/libQt?QuickWidgets.so.*
%files -n libqt6-quickshapes
%_qt6_libdir/libQt?QuickShapes.so.*
%files -n libqt6-qmlmodels
%_qt6_libdir/libQt?QmlModels.so.*
%files -n libqt6-qmlworkerscript
%_qt6_libdir/libQt?QmlWorkerScript.so.*
%files -n libqt6-labsanimation
%_qt6_libdir/libQt?LabsAnimation.so.*
%files -n libqt6-labsfolderlistmodel
%_qt6_libdir/libQt?LabsFolderListModel.so.*
%files -n libqt6-labsqmlmodels
%_qt6_libdir/libQt?LabsQmlModels.so.*
%files -n libqt6-labssettings
%_qt6_libdir/libQt?LabsSettings.so.*
%files -n libqt6-labssharedimage
%_qt6_libdir/libQt?LabsSharedImage.so.*
%files -n libqt6-labswavefrontmesh
%_qt6_libdir/libQt?LabsWavefrontMesh.so.*
%files -n libqt6-qmlcore
%_qt6_libdir/libQt?QmlCore.so.*
%files -n libqt6-qmllocalstorage
%_qt6_libdir/libQt?QmlLocalStorage.so.*
%files -n libqt6-qmlxmllistmodel
%_qt6_libdir/libQt?QmlXmlListModel.so.*
%files -n libqt6-quickcontrols2
%_qt6_libdir/libQt?QuickControls2.so.*
%files -n libqt6-quickcontrols2impl
%_qt6_libdir/libQt?QuickControls2Impl.so.*
%files -n libqt6-quickdialogs2
%_qt6_libdir/libQt?QuickDialogs2.so.*
%files -n libqt6-quickdialogs2quickimpl
%_qt6_libdir/libQt?QuickDialogs2QuickImpl.so.*
%files -n libqt6-quickdialogs2utils
%_qt6_libdir/libQt?QuickDialogs2Utils.so.*
%files -n libqt6-quicklayouts
%_qt6_libdir/libQt?QuickLayouts.so.*
%files -n libqt6-quicktemplates2
%_qt6_libdir/libQt?QuickTemplates2.so.*

%files devel
%_bindir/qml*
%_qt6_bindir/qml*
%_qt6_libexecdir/qml*
%_qt6_plugindir/qmltooling/*
%_qt6_libdir/libQt*.so
%_qt6_libdatadir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdatadir/libQt*.prl
%_qt6_headerdir/Qt*/
%_qt6_archdatadir/mkspecs/modules/*.pr*
%_qt6_archdatadir/mkspecs/features/*.pr*
%_libdir/cmake/Qt*/
%_qt6_libdatadir/libQt*.a
%_qt6_libdir/libQt?*.a
%_qt6_libdir/metatypes/qt*.json
%_qt6_datadir/modules/*.json

%files devel-static

%files -n rpm-build-qml6
%doc src/rpm-build-qml/LICENSE
%_rpmmacrosdir/qml6
%_rpmmacrosdir/qml6.env
%_rpmlibdir/qml6.req
%_rpmlibdir/qml6.req.files
%_rpmlibdir/qml6.prov
%_rpmlibdir/qml6.prov.files
%_bindir/rpmbqml6-prov-enum.pl
%_bindir/rpmbqml6-qmlinfo

%changelog
* Thu Dec 15 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt5
- optimize provides generator (thanks iv@alt)

* Thu Oct 13 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt4
- fix package depends generator

* Thu Oct 13 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt3
- fix prov/req names

* Thu Jul 14 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt2
- fix build requires for rpm-build-qml6

* Wed May 25 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Tue Dec 07 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Mon Nov 29 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.1-alt1
- initial build

