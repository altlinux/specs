%global qt_module dqtdeclarative

%define optflags_lto %nil

Name: dqt6-declarative
Version: 6.7.2
Release: alt0.dde.1
# %%if "%%version" == "%%{get_version dqt6-tools-common}"
%def_disable bootstrap
# %%else
# %%def_enable bootstrap
# %%endif

Group: System/Libraries
Summary: Qt6 - QtDeclarative component
Url: http://qt.io/
License:  LGPL-2.1 with Qt-LGPL-exception-1.1 or LGPL-3.0-only

Requires: libdqt6-qml
Requires: libdqt6-quick
Requires: libdqt6-quickparticles
Requires: libdqt6-quickshapes
Requires: libdqt6-qmlmodels
Requires: libdqt6-qmlworkerscript
Requires: libdqt6-labsanimation
Requires: libdqt6-labsfolderlistmodel
Requires: libdqt6-labssettings
Requires: libdqt6-labssharedimage
Requires: libdqt6-labswavefrontmesh
Requires: libdqt6-qmlcore
Requires: libdqt6-qmllocalstorage
Requires: libdqt6-qmlxmllistmodel
Requires: libdqt6-quickcontrols2
Requires: libdqt6-quickdialogs2
Requires: libdqt6-quicklayouts
Requires: libdqt6-quicktemplates2
Requires: libdqt6-quickeffects
Requires: libdqt6-qmlnetwork
Requires: libdqt6-quickcontrols2basic
Requires: libdqt6-quickcontrols2fusion
Requires: libdqt6-quickcontrols2imagine
Requires: libdqt6-quickcontrols2material

Source: %qt_module-everywhere-src-%version.tar
Source10: rpm-build-dqml.tar
Source1: qml6
Source2: qml6.env
Source3: find-provides.sh
Source4: find-requires.sh

# find librares
%add_findprov_lib_path %_dqt6_libdir

%include %SOURCE1
%dqml6_req_skipall 1
%dqml6_add_req_nover Qt.test.qtestroot
%define __find_provides %SOURCE3
%define __find_requires %SOURCE4

# Automatically added by buildreq on Wed Dec 01 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libdouble-conversion3 libglvnd-devel libgpg-error libqt6-concurrent libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-opengl libqt6-openglwidgets libqt6-shadertools libqt6-sql libqt6-test libqt6-widgets libsasl2-3 libssl-devel libstdc++-devel libvulkan-devel perl pkg-config python-modules python2-base python3 python3-base python3-module-paste qt6-base-common qt6-base-devel rpm-build-file rpm-build-gir rpm-build-python3 rpm-macros-python sh4 tzdata
#BuildRequires: ccmake glslang libGLU-devel libxkbcommon-devel python-modules-compiler python3-dev qt6-shadertools-devel rpm-build-qml tbb-devel
BuildRequires(pre): rpm-macros-dqt6 rpm-build-ninja
# BuildRequires(pre): dqt6-tools-common
BuildRequires: rpm-build-python3
BuildRequires: gcc-c++ glibc-devel dqt6-base-devel dqt6-shadertools-devel
BuildRequires: cmake glslang libGLU-devel libxkbcommon-devel
# %%if_disabled bootstrap
# BuildRequires: dqt6-tools
# %%endif

%description
%summary


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
Requires: dqt6-base-devel rpm-build-dqml6
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

%package -n rpm-build-dqml6
Group: Development/Other
Summary: RPM helper macros to rebuild QML packages
%description -n rpm-build-dqml6
These helper macros provide possibility to rebuild
QML modules by some Alt Linux Team Policy compatible way.

%package -n libdqt6-qml
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-qml
%summary

%package -n libdqt6-quick
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
# Provides: libQtQuick6 = %%version-release
%description -n libdqt6-quick
%summary

%package -n libdqt6-quickparticles
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickparticles
%summary

%package -n libdqt6-quicktest
Group: System/Libraries
Summary: Qt6 - library
# Provides: qml(Qt.test.qtestroot)
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quicktest
%summary

%package -n libdqt6-quickwidgets
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickwidgets
%summary

%package -n libdqt6-quickshapes
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickshapes
%summary

%package -n libdqt6-qmlmodels
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-qmlmodels
%summary

%package -n libdqt6-qmlworkerscript
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-qmlworkerscript
%summary

%package -n libdqt6-quickcontrols2impl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickcontrols2impl
%summary

%package -n libdqt6-quickdialogs2
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickdialogs2
%summary

%package -n libdqt6-quickdialogs2quickimpl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickdialogs2quickimpl
%summary

%package -n libdqt6-quickdialogs2utils
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickdialogs2utils
%summary

%package -n libdqt6-quickcontrols2
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickcontrols2
%summary

%package -n libdqt6-qmlxmllistmodel
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-qmlxmllistmodel
%summary

%package -n libdqt6-qmllocalstorage
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-qmllocalstorage
%summary

%package -n libdqt6-quicklayouts
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quicklayouts
%summary

%package -n libdqt6-quicktemplates2
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quicktemplates2
%summary

%package -n libdqt6-qmlcore
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-qmlcore
%summary

%package -n libdqt6-labswavefrontmesh
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-labswavefrontmesh
%summary

%package -n libdqt6-labssharedimage
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-labssharedimage
%summary

%package -n libdqt6-labssettings
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-labssettings
%summary

%package -n libdqt6-labsqmlmodels
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-labsqmlmodels
%summary

%package -n libdqt6-labsfolderlistmodel
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-labsfolderlistmodel
%summary libdqt6-labsfolderlistmodel

%package -n libdqt6-labsanimation
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-labsanimation
%summary

%package -n libdqt6-qmlcompiler
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-qmlcompiler
%summary

%package -n libdqt6-quickeffects
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickeffects
%summary

%package -n libdqt6-qmlnetwork
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-qmlnetwork
%summary

%package -n libdqt6-quickcontrols2basic
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickcontrols2basic
%summary

%package -n libdqt6-quickcontrols2basicstyleimpl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickcontrols2basicstyleimpl
%summary

%package -n libdqt6-quickcontrols2fusion
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickcontrols2fusion
%summary

%package -n libdqt6-quickcontrols2fusionstyleimpl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickcontrols2fusionstyleimpl
%summary

%package -n libdqt6-quickcontrols2imagine
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickcontrols2imagine
%summary

%package -n libdqt6-quickcontrols2imaginestyleimpl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickcontrols2imaginestyleimpl
%summary

%package -n libdqt6-quickcontrols2material
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickcontrols2material
%summary

%package -n libdqt6-quickcontrols2materialstyleimpl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickcontrols2materialstyleimpl
%summary

%package -n libdqt6-quickcontrols2universal
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickcontrols2universal
%summary

%package -n libdqt6-quickcontrols2universalstyleimpl
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-quickcontrols2universalstyleimpl
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

mv rpm-build-dqml src/
mkdir bin_add
ln -s %__python3 bin_add/python

%build
%if_enabled bootstrap
%define qdoc_found %{expand:%%(if [ -e %_dqt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%else
%define qdoc_found 0
%endif
export PATH=$PWD/bin_add:$PATH
%DQ6build -DCMAKE_MAKE_PROGRAM=ninja
%if %qdoc_found
%DQ6make --target docs
%endif

#build rpm-build-qml
export BUILDFLAGS="-I../../include/QtQml/%version -I../../include/QtQml/%version/QtQml -I../../include/QtQml"
pushd src/rpm-build-dqml
#qmake_dqt6 rpmbqml-qmlinfo.pro
#make_build
popd

%install
%DQ6install_qt
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot VERBOSE=1 install_docs ||:
%endif

# relax depends on plugins files
for f in %buildroot/%_dqt6_libdir/cmake/Qt?*/{*,}/Qt*Targets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

#install rpm-build-dqml
pushd src/rpm-build-dqml

# FIXME rpmbdqml-qmlinfo
ln -s /bin/true %buildroot/%_bindir/rpmbdqml6-qmlinfo
#install -pD -m755 rpmbqml-qmlinfo %buildroot/%_bindir/rpmbdqml6-qmlinfo
# end FIXME
install -pD -m755 rpmbqml6-prov-enum.pl %buildroot/%_bindir/rpmbdqml6-prov-enum.pl
install -pD -m755 qml6.prov %buildroot/%_rpmlibdir/dqml6.prov
install -pD -m755 qml6.prov.files %buildroot/%_rpmlibdir/dqml6.prov.files
install -pD -m755 qml6.req %buildroot/%_rpmlibdir/dqml6.req
install -pD -m755 qml6.req.files %buildroot/%_rpmlibdir/dqml6.req.files
popd

mkdir -p %buildroot%_rpmmacrosdir/
cat %SOURCE1 | sed 's|define[[:space:]][[:space:]]*||' >> %buildroot%_rpmmacrosdir/dqml6
cat %SOURCE2 >> %buildroot%_rpmmacrosdir/dqml6.env


%files
%files common
%doc LICENSES/*
%doc dist/changes*
%dir %_dqt6_qmldir/
%dir %_dqt6_qmldir/Qt/
%dir %_dqt6_qmldir/Qt/labs/
%dir %_dqt6_qmldir/QtQml/
%dir %_dqt6_qmldir/QtQuick/

%files doc
%if %qdoc_found
%_dqt6_docdir/*
%endif
%_dqt6_examplesdir/*

%files -n libdqt6-qml
%_dqt6_libdir/libQt?Qml.so.*
%_dqt6_qmldir/QmlTime/
%_dqt6_qmldir/QtQuick/Window/
%_dqt6_qmldir/QtQml/Base/
%_dqt6_qmldir/QtQml/libqmlmetaplugin.so
%_dqt6_qmldir/QtQml/qmldir
%_dqt6_qmldir/builtins.qmltypes
%_dqt6_qmldir/jsroot.qmltypes
%files -n libdqt6-quick
%_dqt6_libdir/libQt?Quick.so.*
%_dqt6_qmldir/QtQuick/libqtquick2plugin.so
%_dqt6_qmldir/QtQuick/plugins.qmltypes
%_dqt6_qmldir/QtQuick/qmldir
%files -n libdqt6-quickparticles
%_dqt6_libdir/libQt?QuickParticles.so.*
%_dqt6_qmldir/QtQuick/Particles/
%files -n libdqt6-quicktest
%_dqt6_libdir/libQt?QuickTest.so.*
%_dqt6_qmldir/Qt/test/
%_dqt6_qmldir/QtTest/
%files -n libdqt6-quickwidgets
%_dqt6_libdir/libQt?QuickWidgets.so.*
%files -n libdqt6-quickshapes
%_dqt6_libdir/libQt?QuickShapes.so.*
%_dqt6_qmldir/QtQuick/Shapes/
%files -n libdqt6-qmlcompiler
%_dqt6_libdir/libQt6QmlCompiler.so.*
%files -n libdqt6-qmlmodels
%_dqt6_libdir/libQt?QmlModels.so.*
%_dqt6_qmldir/Qt/labs/qmlmodels/
%_dqt6_qmldir/QtQml/Models/
%files -n libdqt6-qmlworkerscript
%_dqt6_libdir/libQt?QmlWorkerScript.so.*
%_dqt6_qmldir/QtQml/WorkerScript/
%files -n libdqt6-labsanimation
%_dqt6_libdir/libQt?LabsAnimation.so.*
%_dqt6_qmldir/Qt/labs/animation/
%files -n libdqt6-labsfolderlistmodel
%_dqt6_libdir/libQt?LabsFolderListModel.so.*
%_dqt6_qmldir/Qt/labs/folderlistmodel/
%files -n libdqt6-labsqmlmodels
%_dqt6_libdir/libQt?LabsQmlModels.so.*
%files -n libdqt6-labssettings
%_dqt6_libdir/libQt?LabsSettings.so.*
%_dqt6_qmldir/Qt/labs/settings/
%files -n libdqt6-labssharedimage
%_dqt6_libdir/libQt?LabsSharedImage.so.*
%_dqt6_qmldir/Qt/labs/sharedimage/
%files -n libdqt6-labswavefrontmesh
%_dqt6_libdir/libQt?LabsWavefrontMesh.so.*
%_dqt6_qmldir/Qt/labs/wavefrontmesh/
%files -n libdqt6-qmlcore
%_dqt6_libdir/libQt?QmlCore.so.*
%_dqt6_qmldir/QtCore/
%files -n libdqt6-qmllocalstorage
%_dqt6_libdir/libQt?QmlLocalStorage.so.*
%_dqt6_qmldir/QtQuick/LocalStorage/
%files -n libdqt6-qmlxmllistmodel
%_dqt6_libdir/libQt?QmlXmlListModel.so.*
%_dqt6_qmldir/QtQml/XmlListModel/
%files -n libdqt6-quickcontrols2
%_dqt6_libdir/libQt?QuickControls2.so.*
%dir %_dqt6_qmldir/QtQuick/Controls/
%_dqt6_qmldir/QtQuick/Controls/impl/
%_dqt6_qmldir/QtQuick/Controls/libqtquickcontrols2plugin.so
%_dqt6_qmldir/QtQuick/Controls/plugins.qmltypes
%_dqt6_qmldir/QtQuick/Controls/qmldir
%_dqt6_qmldir/QtQuick/NativeStyle/
%files -n libdqt6-quickcontrols2impl
%_dqt6_libdir/libQt?QuickControls2Impl.so.*
%files -n libdqt6-quickdialogs2
%_dqt6_libdir/libQt?QuickDialogs2.so.*
%_dqt6_qmldir/QtQuick/Dialogs/
%files -n libdqt6-quickdialogs2quickimpl
%_dqt6_libdir/libQt?QuickDialogs2QuickImpl.so.*
%files -n libdqt6-quickdialogs2utils
%_dqt6_libdir/libQt?QuickDialogs2Utils.so.*
%files -n libdqt6-quicklayouts
%_dqt6_libdir/libQt?QuickLayouts.so.*
%_dqt6_qmldir/QtQuick/Layouts/
%files -n libdqt6-quicktemplates2
%_dqt6_libdir/libQt?QuickTemplates2.so.*
%_dqt6_qmldir/QtQuick/Templates/
%_dqt6_qmldir/Qt/labs/platform/
%files -n libdqt6-quickeffects
%_dqt6_libdir/libQt?QuickEffects.so.*
%_dqt6_qmldir/QtQuick/Effects/
%files -n libdqt6-qmlnetwork
%_dqt6_libdir/libQt6QmlNetwork.so.*
%_dqt6_qmldir/QtNetwork/
%files -n libdqt6-quickcontrols2basic
%_dqt6_libdir/libQt6QuickControls2Basic.so.*
%_dqt6_qmldir/QtQuick/Controls/Basic/
%files -n libdqt6-quickcontrols2basicstyleimpl
%_dqt6_libdir/libQt6QuickControls2BasicStyleImpl.so.*
%files -n libdqt6-quickcontrols2fusion
%_dqt6_libdir/libQt6QuickControls2Fusion.so.*
%_dqt6_qmldir/QtQuick/Controls/Fusion/
%files -n libdqt6-quickcontrols2fusionstyleimpl
%_dqt6_libdir/libQt6QuickControls2FusionStyleImpl.so.*
%files -n libdqt6-quickcontrols2imagine
%_dqt6_libdir/libQt6QuickControls2Imagine.so.*
%_dqt6_qmldir/QtQuick/Controls/Imagine/
%files -n libdqt6-quickcontrols2imaginestyleimpl
%_dqt6_libdir/libQt6QuickControls2ImagineStyleImpl.so.*
%files -n libdqt6-quickcontrols2material
%_dqt6_libdir/libQt6QuickControls2Material.so.*
%_dqt6_qmldir/QtQuick/Controls/Material/
%files -n libdqt6-quickcontrols2materialstyleimpl
%_dqt6_libdir/libQt6QuickControls2MaterialStyleImpl.so.*
%files -n libdqt6-quickcontrols2universal
%_dqt6_libdir/libQt6QuickControls2Universal.so.*
%_dqt6_qmldir/QtQuick/Controls/Universal/
%files -n libdqt6-quickcontrols2universalstyleimpl
%_dqt6_libdir/libQt6QuickControls2UniversalStyleImpl.so.*

%files devel
%_bindir/qml*
%_dqt6_bindir/qml*
%_dqt6_libexecdir/qml*
%_dqt6_plugindir/qmltooling/*
%_dqt6_plugindir/qmllint/*
%_dqt6_libdir/libQt*.so
%_dqt6_libdatadir/libQt*.so
%_dqt6_libdir/libQt*.prl
%_dqt6_libdatadir/libQt*.prl
%_dqt6_headerdir/Qt*/
%_dqt6_archdatadir/mkspecs/modules/*.pr*
%_dqt6_archdatadir/mkspecs/features/*.pr*
%_dqt6_libdir/cmake/Qt*/
%_dqt6_libdatadir/libQt*.a
%_dqt6_libdir/libQt?*.a
%_dqt6_archdatadir/metatypes/qt*.json
%_dqt6_archdatadir/modules/*.json
%_dqt6_libdir/pkgconfig/Qt?*.pc
%_dqt6_qmldir/QtQuick/Controls/designer/
%_dqt6_qmldir/QtQuick/tooling/

%files devel-static

%files -n rpm-build-dqml6
%doc src/rpm-build-dqml/LICENSE
%_rpmmacrosdir/dqml6
%_rpmmacrosdir/dqml6.env
%_rpmlibdir/dqml6.req
%_rpmlibdir/dqml6.req.files
%_rpmlibdir/dqml6.prov
%_rpmlibdir/dqml6.prov.files
%_bindir/rpmbdqml6-prov-enum.pl
%_bindir/rpmbdqml6-qmlinfo

%changelog
* Wed Oct 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.7.2-alt0.dde.1
- fork qt6 for separate deepin packaging (ALT #48138)

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

