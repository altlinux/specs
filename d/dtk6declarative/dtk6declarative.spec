%define soname 6

%def_enable clang

Name: dtk6declarative
Version: 6.0.19
Release: alt2

Summary: Widget development toolkit for Deepin
Summary(ru): Инструментарий по разработке виджетов для Deepin

License: LGPL-3.0+
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dtk6declarative

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch
Patch1: dtk6declarative-6.0.19-pkgconfig-dqt6.patch

%if_enabled clang
ExcludeArch: armh
%endif

Provides: dtk6-declarative = %EVR
Obsoletes: dtk6-declarative < %EVR

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
#BuildRequires: doxygen graphviz dqt6-base-doc
BuildRequires: cmake libdtk6gui-devel dqt6-tools-devel dqt6-declarative-devel dqt6-shadertools-devel

Requires: libdqt6-core = %_dqt6_version libdqt6-qmlmodels = %_dqt6_version libdqt6-quickcontrols2 = %_dqt6_version

%description
dtkdeclarative is a widget development toolkit based on QtQuick/QtQml, which is
a brand new substitute for dtkwidget. dtkdeclarative is developed based on
qtdeclarative. It covers all existing QML widgets and adds plenty of DTK
friendly visual effects and color schemes. Compared to dtkwidget. It has:

- A primitive Qt and Qml code style.
- Adapted APIs with traditional Qml.
- Simple and quick development interfaces.
- Unified widget theme style.
- Abundant effects and colors.

%description -l ru
dtkdeclarative - это инструментарий для разработки виджетов, основанный на
QtQuick / QtQml, который является совершенно новым заменителем dtkwidget.
dtkdeclarative разрабатывается на основе qtdeclarative. Он охватывает все
существующие виджеты QML и добавляет множество дружественных DTK визуальных
эффектов и цветовых схем. По сравнению с дтквиджетом. Имеет:

- Примитивный стиль кода Qt и Qml.
- Адаптированные API с традиционным Qml.
- Простые и быстрые интерфейсы разработки.
- Унифицированный стиль темы виджета.
- Обильные эффекты и цвета.

%package -n lib%name%soname
Summary: Libraries for %name
Summary(ru): Библиотеки для %name
Group: System/Libraries
Requires: libdqt6-core = %_dqt6_version libdqt6-gui = %_dqt6_version libdqt6-qml = %_dqt6_version libdqt6-qmlmodels = %_dqt6_version libdqt6-quick = %_dqt6_version

%description -n lib%name%soname
The package provides libraries for %name.

%description -n lib%name%soname -l ru
Пакет содержит библиотеки для %name.

%package -n lib%name-devel
Summary: Development files for %name
Summary(ru): Файлы разработки для %name
Group: Development/KDE and QT
Provides: dtk6-declarative-devel = %EVR
Obsoletes: dtk6-declarative-devel < %EVR

%description -n lib%name-devel
The package provides development files for %name.

%description -n lib%name-devel -l ru
Пакет содержит библиотеки для %name.

%package -n qt-creator-data-%name
Summary: QtCreator Data files for %name
Summary(ru): Файлы данных QtCreator для %name
Group: Development/Tools
BuildArch: noarch

%description -n qt-creator-data-%name
QtCreator Data files for %name.

%description -n qt-creator-data-%name -l ru
Файлы данных QtCreator для %name.

%prep
%setup
%autopatch -p1

%build
%if_enabled clang

export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"

%endif

export CMAKE_PREFIX_PATH=%_dqt6_libdir/cmake:$CMAKE_PREFIX_PATH
export PATH=%_dqt6_bindir:$PATH

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_DOCS=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
  -DCMAKE_INSTALL_RPATH=%_dqt6_libdir \
  -DMKSPECS_INSTALL_DIR=%_dqt6_mkspecsdir/modules/ \
  -DQML_INSTALL_DIR=%_dqt6_qmldir \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DINCLUDE_INSTALL_DIR=include \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DLIB_INSTALL_DIR=%_lib \
  -DDTK_VERSION=%version \
  -DVERSION=%version \
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files
%doc LICENSE README.md
%dir %_libdir/dtk6/
%dir %_libdir/dtk6/DDeclarative/
%_libdir/dtk6/DDeclarative/dtk-exhibition
%dir %_dqt6_qmldir/Chameleon/
%_dqt6_qmldir/Chameleon/*
%dir %_dqt6_qmldir/org/deepin/
%dir %_dqt6_qmldir/org/deepin/dtk/
%_dqt6_qmldir/org/deepin/dtk/%{name}*
%_dqt6_qmldir/org/deepin/dtk/*.qml
%_dqt6_qmldir/org/deepin/dtk/libdtkdeclarativeplugin.so
%_dqt6_qmldir/org/deepin/dtk/qmldir
%dir %_dqt6_qmldir/org/deepin/dtk/private/
%_dqt6_qmldir/org/deepin/dtk/private/*
%dir %_dqt6_qmldir/org/deepin/dtk/settings/
%_dqt6_qmldir/org/deepin/dtk/settings/*
%dir %_datadir/dtk6/
%_datadir/dtk6/DDeclarative/

%files -n lib%name%soname
%_libdir/lib%name.so.%{soname}*

%files -n lib%name-devel
%_includedir/*
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%dir %_libdir/cmake/Dtk6Declarative/
%_libdir/cmake/Dtk6Declarative/*.cmake
%_dqt6_archdatadir/mkspecs/modules/qt_lib_dtkdeclarative.pri

%files -n qt-creator-data-%name
%_datadir/qtcreator/templates/wizards/projects/qml6-app-template/

%changelog
* Wed Oct 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.19-alt2
- Built with separate qt6 (ALT #48138).

* Fri Aug 30 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.19-alt1
- New version 6.0.19.

* Fri May 17 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.16-alt1
- New version 6.0.16.

* Mon Apr 22 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.11-alt1
- New version 6.0.11.

* Wed Apr 03 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.9-alt1
- Initial build for ALT Sisyphus.
