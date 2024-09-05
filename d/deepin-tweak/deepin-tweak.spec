%def_without clang

Name: deepin-tweak
Version: 1.2.2.0.17.6a00
Release: alt2

Summary: Setting tool built on dtkdeclarative
Summary(ru): Инструмент настройки, созданный на dtkdeclarative

License: LGPL-3.0+
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dtkdeclarative

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-tweak-1.1.0-alt-fix-undefined-elfs.patch

# dtkdeclarative doesn't built for armh
ExcludeArch: armh

Requires: dtkdeclarative

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
# Automatically added by buildreq on Sat Oct 28 2023
# optimized out: bash5 bashrc cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt libp11-kit libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-network libdqt5-qml libdqt5-qmlmodels libdqt5-quick libdqt5-svg libdqt5-widgets libdqt5-xml libsasl2-3 libssl-devel libstdc++-devel pkg-config python3 python3-base dqt5-base-devel dqt5-declarative-devel sh5
BuildRequires: cmake gsettings-qt-devel libdtkdeclarative-devel dqt5-declarative-devel dqt5-tools

%if_with clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

%description
Deepin Tweak is an advanced setting tool built on dtkdeclarative. Deepin Tweak only provides limited built-in functions, most of which need to be provided by other developers in the community according to the requirements of plug-in development.

%description -l ru
Deepin Tweak - это продвинутый инструмент настройки, созданный на основе dtkdeclarative. Deepin Tweak предоставляет только ограниченные встроенные функции, большинство из которых должны предоставляться другими разработчиками в сообществе в соответствии с требованиями разработки плагинов.

%prep
%setup
%patch -p1

%build
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export CPLUS_INCLUDE_PATH=%_includedir/qt5:$CPLUS_INCLUDE_PATH
export PATH=%_dqt5_bindir:$PATH

%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DMKSPECS_INSTALL_DIR=%_dqt5_archdatadir/mkspecs/ \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
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
%dir %_libdir/%name/
%_libdir/%name/lib%{name}*.so

%changelog
* Fri May 31 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.2.0.17.6a00-alt2
- Built via separate qt5 instead system (ALT #48138).

* Sat Dec 30 2023 Leontiy Volodin <lvol@altlinux.org> 1.2.2.0.17.6a00-alt1
- New version 1.2.2-17-g6a0061b.

* Sat Oct 28 2023 Leontiy Volodin <lvol@altlinux.org> 1.2.2-alt1.1
- Rebuilt with dtk.
- Cleanup spec and BRs.

* Tue Mar 21 2023 Leontiy Volodin <lvol@altlinux.org> 1.2.2-alt1
- New version.

* Fri Dec 02 2022 Leontiy Volodin <lvol@altlinux.org> 1.1.0-alt1.1
- Fixed startup.

* Tue Nov 29 2022 Leontiy Volodin <lvol@altlinux.org> 1.1.0-alt1
- Initial build for ALT Sisyphus.
