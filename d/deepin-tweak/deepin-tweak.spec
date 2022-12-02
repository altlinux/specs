%def_disable clang

Name: deepin-tweak
Version: 1.1.0
Release: alt1.1
Summary: Setting tool built on dtkdeclarative
Summary(ru): Инструмент настройки, созданный на dtkdeclarative
License: LGPL-3.0+
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dtkdeclarative

Source: %url/archive/%version/%name-%version.tar.gz
Patch: 0001-fix-undefined-elfs.patch

# dtkdeclarative doesn't built for armh
ExcludeArch: armh

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake
BuildRequires: qt5-base-devel qt5-tools qt5-quickcontrols2-devel
BuildRequires: dtk5-common dtk5-core-devel dtk5-gui-devel dtk5-declarative-devel gsettings-qt-devel
Requires: dtk5-declarative

%description
Deepin Tweak is an advanced setting tool built on dtkdeclarative. Deepin Tweak only provides limited built-in functions, most of which need to be provided by other developers in the community according to the requirements of plug-in development.

%description -l ru
Deepin Tweak - это продвинутый инструмент настройки, созданный на основе dtkdeclarative. Deepin Tweak предоставляет только ограниченные встроенные функции, большинство из которых должны предоставляться другими разработчиками в сообществе в соответствии с требованиями разработки плагинов.

%prep
%setup
%patch -p1

%build
export PATH=%_qt5_bindir:$PATH

%if_enabled clang

export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"

%endif

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DMKSPECS_INSTALL_DIR=%_qt5_archdatadir/mkspecs/ \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DDTK_VERSION=%version \
  -DVERSION=%version \
  -DLIB_INSTALL_DIR=%_libdir \
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%dir %_datadir/%name/
%dir %_datadir/%name/plugins/
%_datadir/%name/plugins/*
%dir %_libdir/dtkdeclarative/
%dir %_libdir/dtkdeclarative/qml-app/
%_libdir/dtkdeclarative/qml-app/*.so

%changelog
* Fri Dec 02 2022 Leontiy Volodin <lvol@altlinux.org> 1.1.0-alt1.1
- Fixed startup.

* Tue Nov 29 2022 Leontiy Volodin <lvol@altlinux.org> 1.1.0-alt1
- Initial build for ALT Sisyphus.
