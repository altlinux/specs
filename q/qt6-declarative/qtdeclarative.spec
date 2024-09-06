%global qt_module qtdeclarative

%define optflags_lto %nil

Name: qt6-declarative
Version: 6.7.2
Release: alt1
%if "%version" == "%{get_version qt6-tools-common}"
%def_disable bootstrap
%else
%def_enable bootstrap
%endif

Group: System/Libraries
Summary: Qt6 - QtDeclarative component
Url: http://qt.io/
License:  LGPL-2.1 with Qt-LGPL-exception-1.1 or LGPL-3.0-only

Requires: libqt6-qml
Requires: libqt6-quick
Requires: libqt6-quickparticles
Requires: libqt6-quickshapes
Requires: libqt6-qmlmodels
Requires: libqt6-qmlworkerscript
Requires: libqt6-labsanimation
Requires: libqt6-labsfolderlistmodel
Requires: libqt6-labssettings
Requires: libqt6-labssharedimage
Requires: libqt6-labswavefrontmesh
Requires: libqt6-qmlcore
Requires: libqt6-qmllocalstorage
Requires: libqt6-qmlxmllistmodel
Requires: libqt6-quickcontrols2
Requires: libqt6-quickdialogs2
Requires: libqt6-quicklayouts
Requires: libqt6-quicktemplates2
Requires: libqt6-quickeffects
Requires: libqt6-qmlnetwork
Requires: libqt6-quickcontrols2basic
Requires: libqt6-quickcontrols2fusion
Requires: libqt6-quickcontrols2imagine
Requires: libqt6-quickcontrols2material

Source: %qt_module-everywhere-src-%version.tar
Source10: rpm-build-qml.tar
Source1: qml6
Source2: qml6.env
Source3: find-provides.sh
Source4: find-requires.sh

%include %SOURCE1
%qml6_req_skipall 1
%qml6_add_req_nover Qt.test.qtestroot
%define __find_provides %SOURCE3
%define __find_requires %SOURCE4

# Automatically added by buildreq on Wed Dec 01 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libdouble-conversion3 libglvnd-devel libgpg-error libqt6-concurrent libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-opengl libqt6-openglwidgets libqt6-shadertools libqt6-sql libqt6-test libqt6-widgets libsasl2-3 libssl-devel libstdc++-devel libvulkan-devel perl pkg-config python-modules python2-base python3 python3-base python3-module-paste qt6-base-common qt6-base-devel rpm-build-file rpm-build-gir rpm-build-python3 rpm-macros-python sh4 tzdata
#BuildRequires: ccmake glslang libGLU-devel libxkbcommon-devel python-modules-compiler python3-dev qt6-shadertools-devel rpm-build-qml tbb-devel
BuildRequires(pre): rpm-macros-qt6 qt6-tools-common
BuildRequires: rpm-build-python3
BuildRequires: gcc-c++ glibc-devel qt6-base-devel qt6-shadertools-devel
BuildRequires: cmake glslang libGLU-devel libxkbcommon-devel
%if_disabled bootstrap
BuildRequires: qt6-tools
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
Requires: %name-common
Requires: qt6-base-devel rpm-build-qml6
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

%package -n rpm-build-qml6
Group: Development/Other
Summary: RPM helper macros to rebuild QML packages
%description -n rpm-build-qml6
These helper macros provide possibility to rebuild
QML modules by some Alt Linux Team Policy compatible way.

%package -n libqt6-qml
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-qml
%summary

%package -n libqt6-quick
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
Provides: libQtQuick6 = %version-release
%description -n libqt6-quick
%summary

%package -n libqt6-quickparticles
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickparticles
%summary

%package -n libqt6-quicktest
Group: System/Libraries
Summary: Qt6 - library
Provides: qml(Qt.test.qtestroot)
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quicktest
%summary

%package -n libqt6-quickwidgets
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickwidgets
%summary

%package -n libqt6-quickshapes
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickshapes
%summary

%package -n libqt6-qmlmodels
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-qmlmodels
%summary

%package -n libqt6-qmlworkerscript
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-qmlworkerscript
%summary

%package -n libqt6-quickcontrols2impl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickcontrols2impl
%summary

%package -n libqt6-quickdialogs2
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickdialogs2
%summary

%package -n libqt6-quickdialogs2quickimpl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickdialogs2quickimpl
%summary

%package -n libqt6-quickdialogs2utils
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickdialogs2utils
%summary

%package -n libqt6-quickcontrols2
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickcontrols2
%summary

%package -n libqt6-qmlxmllistmodel
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-qmlxmllistmodel
%summary

%package -n libqt6-qmllocalstorage
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-qmllocalstorage
%summary

%package -n libqt6-quicklayouts
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quicklayouts
%summary

%package -n libqt6-quicktemplates2
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quicktemplates2
%summary

%package -n libqt6-qmlcore
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-qmlcore
%summary

%package -n libqt6-labswavefrontmesh
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-labswavefrontmesh
%summary

%package -n libqt6-labssharedimage
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-labssharedimage
%summary

%package -n libqt6-labssettings
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-labssettings
%summary

%package -n libqt6-labsqmlmodels
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-labsqmlmodels
%summary

%package -n libqt6-labsfolderlistmodel
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-labsfolderlistmodel
%summary libqt6-labsfolderlistmodel

%package -n libqt6-labsanimation
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-labsanimation
%summary

%package -n libqt6-qmlcompiler
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-qmlcompiler
%summary

%package -n libqt6-quickeffects
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickeffects
%summary

%package -n libqt6-qmlnetwork
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-qmlnetwork
%summary

%package -n libqt6-quickcontrols2basic
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickcontrols2basic
%summary

%package -n libqt6-quickcontrols2basicstyleimpl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickcontrols2basicstyleimpl
%summary

%package -n libqt6-quickcontrols2fusion
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickcontrols2fusion
%summary

%package -n libqt6-quickcontrols2fusionstyleimpl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickcontrols2fusionstyleimpl
%summary

%package -n libqt6-quickcontrols2imagine
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickcontrols2imagine
%summary

%package -n libqt6-quickcontrols2imaginestyleimpl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickcontrols2imaginestyleimpl
%summary

%package -n libqt6-quickcontrols2material
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickcontrols2material
%summary

%package -n libqt6-quickcontrols2materialstyleimpl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickcontrols2materialstyleimpl
%summary

%package -n libqt6-quickcontrols2universal
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickcontrols2universal
%summary

%package -n libqt6-quickcontrols2universalstyleimpl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quickcontrols2universalstyleimpl
%summary

%prep
%include %SOURCE2
%setup -n %qt_module-everywhere-src-%version -a10
# disable some examples
for e in qml/dynamicscene quick/imageprovider quick/imageresponseprovider quickcontrols/attachedstyleproperties ; do
    exam=`basename $e`
    subdir=`dirname $e`
    sed -i "/qt_internal_add_example.*${exam}/d" examples/$subdir/CMakeLists.txt
done

mv rpm-build-qml src/
mkdir bin_add
ln -s %__python3 bin_add/python

%build
%if_enabled bootstrap
%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%else
%define qdoc_found 0
%endif
export PATH=$PWD/bin_add:$PATH
%Q6build
%if %qdoc_found
%Q6make --target docs
%endif

#build rpm-build-qml
export BUILDFLAGS="-I../../include/QtQml/%version -I../../include/QtQml/%version/QtQml -I../../include/QtQml"
pushd src/rpm-build-qml
#qmake_qt6 rpmbqml-qmlinfo.pro
#make_build
popd

%install
%Q6install_qt
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot VERBOSE=1 install_docs ||:
%endif

# relax depends on plugins files
for f in %buildroot/%_libdir/cmake/Qt?*/{*,}/Qt*Targets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

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
%files common
%doc LICENSES/*
%doc dist/changes*
%dir %_qt6_qmldir/
%dir %_qt6_qmldir/Qt/
%dir %_qt6_qmldir/Qt/labs/
%dir %_qt6_qmldir/QtQml/
%dir %_qt6_qmldir/QtQuick/

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif
%_qt6_examplesdir/*

%files -n libqt6-qml
%_qt6_libdir/libQt?Qml.so.*
%_qt6_qmldir/QmlTime/
%_qt6_qmldir/QtQuick/Window/
%_qt6_qmldir/QtQml/Base/
%_qt6_qmldir/QtQml/libqmlmetaplugin.so
%_qt6_qmldir/QtQml/qmldir
%_qt6_qmldir/builtins.qmltypes
%_qt6_qmldir/jsroot.qmltypes
%files -n libqt6-quick
%_qt6_libdir/libQt?Quick.so.*
%_qt6_qmldir/QtQuick/libqtquick2plugin.so
%_qt6_qmldir/QtQuick/plugins.qmltypes
%_qt6_qmldir/QtQuick/qmldir
%files -n libqt6-quickparticles
%_qt6_libdir/libQt?QuickParticles.so.*
%_qt6_qmldir/QtQuick/Particles/
%files -n libqt6-quicktest
%_qt6_libdir/libQt?QuickTest.so.*
%_qt6_qmldir/Qt/test/
%_qt6_qmldir/QtTest/
%files -n libqt6-quickwidgets
%_qt6_libdir/libQt?QuickWidgets.so.*
%files -n libqt6-quickshapes
%_qt6_libdir/libQt?QuickShapes.so.*
%_qt6_qmldir/QtQuick/Shapes/
%files -n libqt6-qmlcompiler
%_qt6_libdir/libQt6QmlCompiler.so.*
%files -n libqt6-qmlmodels
%_qt6_libdir/libQt?QmlModels.so.*
%_qt6_qmldir/Qt/labs/qmlmodels/
%_qt6_qmldir/QtQml/Models/
%files -n libqt6-qmlworkerscript
%_qt6_libdir/libQt?QmlWorkerScript.so.*
%_qt6_qmldir/QtQml/WorkerScript/
%files -n libqt6-labsanimation
%_qt6_libdir/libQt?LabsAnimation.so.*
%_qt6_qmldir/Qt/labs/animation/
%files -n libqt6-labsfolderlistmodel
%_qt6_libdir/libQt?LabsFolderListModel.so.*
%_qt6_qmldir/Qt/labs/folderlistmodel/
%files -n libqt6-labsqmlmodels
%_qt6_libdir/libQt?LabsQmlModels.so.*
%files -n libqt6-labssettings
%_qt6_libdir/libQt?LabsSettings.so.*
%_qt6_qmldir/Qt/labs/settings/
%files -n libqt6-labssharedimage
%_qt6_libdir/libQt?LabsSharedImage.so.*
%_qt6_qmldir/Qt/labs/sharedimage/
%files -n libqt6-labswavefrontmesh
%_qt6_libdir/libQt?LabsWavefrontMesh.so.*
%_qt6_qmldir/Qt/labs/wavefrontmesh/
%files -n libqt6-qmlcore
%_qt6_libdir/libQt?QmlCore.so.*
%_qt6_qmldir/QtCore/
%files -n libqt6-qmllocalstorage
%_qt6_libdir/libQt?QmlLocalStorage.so.*
%_qt6_qmldir/QtQuick/LocalStorage/
%files -n libqt6-qmlxmllistmodel
%_qt6_libdir/libQt?QmlXmlListModel.so.*
%_qt6_qmldir/QtQml/XmlListModel/
%files -n libqt6-quickcontrols2
%_qt6_libdir/libQt?QuickControls2.so.*
%dir %_qt6_qmldir/QtQuick/Controls/
%_qt6_qmldir/QtQuick/Controls/impl/
%_qt6_qmldir/QtQuick/Controls/libqtquickcontrols2plugin.so
%_qt6_qmldir/QtQuick/Controls/plugins.qmltypes
%_qt6_qmldir/QtQuick/Controls/qmldir
%_qt6_qmldir/QtQuick/NativeStyle/
%files -n libqt6-quickcontrols2impl
%_qt6_libdir/libQt?QuickControls2Impl.so.*
%files -n libqt6-quickdialogs2
%_qt6_libdir/libQt?QuickDialogs2.so.*
%_qt6_qmldir/QtQuick/Dialogs/
%files -n libqt6-quickdialogs2quickimpl
%_qt6_libdir/libQt?QuickDialogs2QuickImpl.so.*
%files -n libqt6-quickdialogs2utils
%_qt6_libdir/libQt?QuickDialogs2Utils.so.*
%files -n libqt6-quicklayouts
%_qt6_libdir/libQt?QuickLayouts.so.*
%_qt6_qmldir/QtQuick/Layouts/
%files -n libqt6-quicktemplates2
%_qt6_libdir/libQt?QuickTemplates2.so.*
%_qt6_qmldir/QtQuick/Templates/
%_qt6_qmldir/Qt/labs/platform/
%files -n libqt6-quickeffects
%_qt6_libdir/libQt?QuickEffects.so.*
%_qt6_qmldir/QtQuick/Effects/
%files -n libqt6-qmlnetwork
%_qt6_libdir/libQt6QmlNetwork.so.*
%_qt6_qmldir/QtNetwork/
%files -n libqt6-quickcontrols2basic
%_qt6_libdir/libQt6QuickControls2Basic.so.*
%_qt6_qmldir/QtQuick/Controls/Basic/
%files -n libqt6-quickcontrols2basicstyleimpl
%_qt6_libdir/libQt6QuickControls2BasicStyleImpl.so.*
%files -n libqt6-quickcontrols2fusion
%_qt6_libdir/libQt6QuickControls2Fusion.so.*
%_qt6_qmldir/QtQuick/Controls/Fusion/
%files -n libqt6-quickcontrols2fusionstyleimpl
%_qt6_libdir/libQt6QuickControls2FusionStyleImpl.so.*
%files -n libqt6-quickcontrols2imagine
%_qt6_libdir/libQt6QuickControls2Imagine.so.*
%_qt6_qmldir/QtQuick/Controls/Imagine/
%files -n libqt6-quickcontrols2imaginestyleimpl
%_qt6_libdir/libQt6QuickControls2ImagineStyleImpl.so.*
%files -n libqt6-quickcontrols2material
%_qt6_libdir/libQt6QuickControls2Material.so.*
%_qt6_qmldir/QtQuick/Controls/Material/
%files -n libqt6-quickcontrols2materialstyleimpl
%_qt6_libdir/libQt6QuickControls2MaterialStyleImpl.so.*
%files -n libqt6-quickcontrols2universal
%_qt6_libdir/libQt6QuickControls2Universal.so.*
%_qt6_qmldir/QtQuick/Controls/Universal/
%files -n libqt6-quickcontrols2universalstyleimpl
%_qt6_libdir/libQt6QuickControls2UniversalStyleImpl.so.*

%files devel
%_bindir/qml*
%_qt6_bindir/qml*
%_qt6_libexecdir/qml*
%_qt6_plugindir/qmltooling/*
%_qt6_plugindir/qmllint/*
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
%_qt6_archdatadir/metatypes/qt*.json
%_qt6_archdatadir/modules/*.json
%_pkgconfigdir/Qt?*.pc
%_qt6_qmldir/QtQuick/Controls/designer/
%_qt6_qmldir/QtQuick/tooling/

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
* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Mon Jan 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt2
- using qdoc_found macro at build

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Mon Dec 19 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt6
- automate bootstrap mode

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

