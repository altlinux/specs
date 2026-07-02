%define soname 6

%def_disable clang

Name: dtk6declarative
Version: 6.7.44
Release: alt1

Summary: Widget development toolkit for Deepin
Summary(ru): Инструментарий по разработке виджетов для Deepin

License: LGPL-3.0+
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dtkdeclarative
Vcs: https://github.com/linuxdeepin/dtkdeclarative

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

%if_enabled clang
ExcludeArch: armh
%endif

Provides: dtk6-declarative = %EVR
Obsoletes: dtk6-declarative < %EVR

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6 patchelf
%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
#BuildRequires: doxygen graphviz dqt6-base-doc
BuildRequires: cmake libdtk6gui-devel dqt6-tools-devel dqt6-declarative-devel dqt6-shadertools-devel
BuildRequires: libdqt6-quickcontrols2 libdqt6-qmlcompiler vulkan-headers libwayland-client-devel

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
%patch0 -p1
# FAILED: examples/exhibition/CMakeFiles/dtk-exhibition.dir/dtk-exhibition_autogen/EWIEGA46WW/qrc_assets.cpp.o
# virtual memory exhausted: Cannot allocate memory
%ifarch i586 armh
sed -i '/add_subdirectory(exhibition)/d' \
  examples/CMakeLists.txt
%endif

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
%DQ6build \
  -DMKSPECS_INSTALL_DIR=%_dqt6_mkspecsdir/modules \
  -DBUILD_DOCS=OFF \
  -DINCLUDE_INSTALL_DIR=include \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DLIB_INSTALL_DIR=%_lib \
  -DDTK_VERSION=%version \
  -DVERSION=%version \
  -DDTK5=OFF \
#

%install
%DQ6install
patchelf %buildroot%_dqt6_qmldir/org/deepin/dtk/private/libdtkdeclarativeprivatesplugin.so --add-rpath %_dqt6_libdir
patchelf %buildroot%_dqt6_qmldir/org/deepin/dtk/settings/libdtkdeclarativesettingsplugin.so --add-rpath %_dqt6_libdir
patchelf %buildroot%_dqt6_qmldir/org/deepin/dtk/libdtkdeclarativeplugin.so --add-rpath %_dqt6_libdir

%files
%doc LICENSE README.md CHANGELOG.md
%ifnarch i586 armh
%dir %_libdir/dtk6/
%dir %_libdir/dtk6/DDeclarative/
%_libdir/dtk6/DDeclarative/dtk6-exhibition
%endif
%dir %_dqt6_qmldir/Chameleon/
%_dqt6_qmldir/Chameleon/*
%dir %_dqt6_qmldir/org/deepin/
%_dqt6_qmldir/org/deepin/dtk/
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
* Thu Jul 02 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.44-alt1
- New version 6.7.44.

* Tue Jun 09 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.43-alt1
- New version 6.7.43.

* Thu May 14 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.41-alt1
- New version 6.7.41.

* Wed Apr 15 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.39-alt1
- New version 6.7.39.
- Changed url and vcs tags.

* Thu Feb 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.48-alt2
- Fixed build on shrinked dqt6.

* Wed Dec 10 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.48-alt1
- New version 6.0.48.

* Fri Nov 07 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.46-alt1
- New version 6.0.46.

* Fri Oct 24 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.44-alt1
- New version 6.0.44.

* Wed Oct 15 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.43-alt1
- New version 6.0.43.
- Fixed overlinked libraries.

* Tue Aug 19 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.41-alt1
- New version 6.0.41.

* Fri Jun 20 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.37-alt1
- New version 6.0.37.

* Tue Jun 17 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.36-alt1
- New version 6.0.36.

* Thu Mar 06 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.30-alt1.1
- Fixed BuildRequires.

* Fri Feb 14 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.30-alt1
- New version 6.0.30.
- Enabled dqml6 provides.
- Built via gcc instead clang.

* Thu Dec 12 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.24.0.3.ed06-alt1
- New version 6.0.24-3-ged06b75.
- Added vcs tag.

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
