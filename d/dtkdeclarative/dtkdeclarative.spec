%define soname 5

%def_disable clang

Name: dtkdeclarative
Version: 5.6.8
Release: alt1
Summary: Widget development toolkit for Deepin
Summary(ru): Инструментарий по разработке виджетов для Deepin
License: LGPL-3.0+
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dtkdeclarative

Source: %url/archive/%version/%name-%version.tar.gz
Patch: dtkdeclarative-5.6.8-alt-fix-underlinked-libraries.patch

ExcludeArch: armh

BuildRequires(pre): rpm-build-ninja
%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: cmake
BuildRequires: qt5-base-devel qt5-tools-devel qt5-tools qt5-quickcontrols2-devel
BuildRequires: dtk5-core-devel dtk5-gui-devel dtk5-common
BuildRequires: libgtest-devel
#BuildRequires: doxygen graphviz qt5-base-doc

%description
dtkdeclarative is a widget development toolkit based on QtQuick/QtQml, which is a brand new substitute for dtkwidget. dtkdeclarative is developed based on qtdeclarative. It covers all existing QML widgets and adds plenty of DTK friendly visual effects and color schemes. Compared to dtkwidget. It has:

- A primitive Qt and Qml code style.
- Adapted APIs with traditional Qml.
- Simple and quick development interfaces.
- Unified widget theme style.
- Abundant effects and colors.

%description -l ru
dtkdeclarative - это инструментарий для разработки виджетов, основанный на QtQuick / QtQml, который является совершенно новым заменителем dtkwidget. dtkdeclarative разрабатывается на основе qtdeclarative. Он охватывает все существующие виджеты QML и добавляет множество дружественных DTK визуальных эффектов и цветовых схем. По сравнению с дтквиджетом. Имеет:

- Примитивный стиль кода Qt и Qml.
- Адаптированные API с традиционным Qml.
- Простые и быстрые интерфейсы разработки.
- Унифицированный стиль темы виджета.
- Обильные эффекты и цвета.

%package -n dtk5-declarative
Summary: Widget development toolkit for Deepin
Summary(ru): Инструментарий по разработке виджетов для Deepin
Group: System/Configuration/Other

%description -n dtk5-declarative
dtkdeclarative is a widget development toolkit based on QtQuick/QtQml, which is a brand new substitute for dtkwidget. dtkdeclarative is developed based on qtdeclarative. It covers all existing QML widgets and adds plenty of DTK friendly visual effects and color schemes. Compared to dtkwidget. It has:

- A primitive Qt and Qml code style.
- Adapted APIs with traditional Qml.
- Simple and quick development interfaces.
- Unified widget theme style.
- Abundant effects and colors.

%description -n dtk5-declarative -l ru
dtkdeclarative - это инструментарий для разработки виджетов, основанный на QtQuick / QtQml, который является совершенно новым заменителем dtkwidget. dtkdeclarative разрабатывается на основе qtdeclarative. Он охватывает все существующие виджеты QML и добавляет множество дружественных DTK визуальных эффектов и цветовых схем. По сравнению с dtkwidget имеет:

- Примитивный стиль кода Qt и Qml.
- Адаптированные API с традиционным Qml.
- Простые и быстрые интерфейсы разработки.
- Унифицированный стиль темы виджета.
- Обильные эффекты и цвета.

%package -n libdtkdeclarative%{soname}
Summary: Libraries for %name
Summary(ru): Библиотеки для %name
Group: System/Libraries

%description -n libdtkdeclarative%{soname}
The package provides libraries for %name.

%description -n libdtkdeclarative%{soname} -l ru
Пакет содержит библиотеки для %name.

%package -n dtk5-declarative-devel
Summary: Development files for %name
Summary(ru): Файлы разработки для %name
Group: Development/KDE and QT

%description -n dtk5-declarative-devel
The package provides development files for %name.

%description -n dtk5-declarative-devel -l ru
Пакет содержит библиотеки для %name.

%package -n qt-creator-data-dtkdeclarative
Summary: QtCreator Data files for %name
Summary(ru): Файлы данных QtCreator для %name
Group: Development/Tools

%description -n qt-creator-data-dtkdeclarative
QtCreator Data files for %name.

%description -n qt-creator-data-dtkdeclarative -l ru
Файлы данных QtCreator для %name.

%prep
%setup
%patch -p1
# Fix broken configs.
sed -i '/libdir=/s/${prefix}//; /includedir=/s/${prefix}//' \
  misc/dtkdeclarative.pc.in
sed -i -e '/.tools/s/@CMAKE_INSTALL_PREFIX@//; /.libs/s/@CMAKE_INSTALL_PREFIX@//; /.includes/s/@CMAKE_INSTALL_PREFIX@//;' \
  misc/qt_lib_dtkdeclarative.pri.in

%build
export PATH=%_qt5_bindir:$PATH

%if_enabled clang

export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"

%endif

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_DOCS=OFF \
  -DMKSPECS_INSTALL_DIR=%_qt5_archdatadir/mkspecs/modules/ \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DDTK_VERSION=%version \
  -DVERSION=%version \
  -DLIB_INSTALL_DIR=%_libdir \
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files -n dtk5-declarative
%doc LICENSE README.md
%_bindir/dtk-exhibition
%_qt5_qmldir/QtQuick/Controls.2/Chameleon/*
%dir %_qt5_qmldir/org/deepin/
%dir %_qt5_qmldir/org/deepin/dtk/
%_qt5_qmldir/org/deepin/dtk/libdtkdeclarativeplugin.so
%_qt5_qmldir/org/deepin/dtk/qmldir
%_desktopdir/dtk-exhibition.desktop
%_datadir/dtk5/DDeclarative/

%files -n libdtkdeclarative%{soname}
%_libdir/libdtkdeclarative.so.%{soname}*

%files -n dtk5-declarative-devel
%_includedir/*
%_libdir/libdtkdeclarative.so
%_pkgconfigdir/dtkdeclarative.pc
%dir %_libdir/cmake/DtkDeclarative/
%_libdir/cmake/DtkDeclarative/*.cmake
%_qt5_archdatadir/mkspecs/modules/qt_lib_dtkdeclarative.pri

%files -n qt-creator-data-dtkdeclarative
%_datadir/qtcreator/templates/wizards/projects/qml-app-template/

%changelog
* Wed Feb 22 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.8-alt1
- New version (5.6.8).
- Built using cmake instead qmake (by upstream).
- Fixed underlinked libraries.

* Tue Nov 29 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.0-alt1
- Initial build for ALT Sisyphus.
