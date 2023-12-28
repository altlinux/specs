%define repo dde-fcitx5configtool-plugin

%def_disable clang

Name: deepin-fcitx5configtool-plugin
Version: 5.0.17.0.4.7355
Release: alt1

Summary: The input method management plug-in of DDE control center

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/%repo

Provides: %repo = %EVR

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires: cmake extra-cmake-modules qt5-base-devel qt5-tools qt5-x11extras-devel fcitx5-devel fcitx5-qt-devel xkeyboard-config-devel iso-codes-devel appstream libdtkwidget-devel deepin-control-center-devel deepin-qt-dbus-factory-devel
BuildRequires(pre): rpm-build-ninja
%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif

%description
%summary.

%prep
%setup -n %repo-%version
%patch -p1

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export PATH=%_qt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    %nil
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang --with-qt dde-control-center

%files -f dde-control-center.lang
%doc README*.md
%dir %_libdir/dde-control-center/
%dir %_libdir/dde-control-center/modules/
%_libdir/dde-control-center/modules/libdcc-fcitx5configtool-plugin.so
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.fcitx5.configtoolplugin/
%_datadir/dsg/configs/org.deepin.fcitx5.configtoolplugin/org.deepin.fcitx5.configtoolplugin.json
# translations
%dir %_datadir/dde-control-center/
%dir %_datadir/dde-control-center/translations/
%_datadir/dde-control-center/translations/deepin-fcitx5configtool-plugin.qm
%_datadir/dde-control-center/translations/deepin-fcitx5configtool-plugin_ky@Arab.qm

%changelog
* Thu Dec 14 2023 Leontiy Volodin <lvol@altlinux.org> 5.0.17.0.4.7355-alt1
- Initial build for ALT Sisyphus.
