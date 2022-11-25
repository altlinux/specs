%define optflags_lto %nil

Name: deepin-terminal
Version: 5.4.38
Release: alt1
Summary: Default terminal emulation application for Deepin
License: GPL-3.0+ and (LGPL-2.0+ and GPL-2.0+ and BSD-3-Clause)
Group: Terminals
Url: https://github.com/linuxdeepin/deepin-terminal

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: dtk5-widget-devel
BuildRequires: dtk5-gui-devel
BuildRequires: dtk5-core-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: glib2-devel
BuildRequires: libat-spi2-core-devel
BuildRequires: libsecret-devel
BuildRequires: libgtest-devel
BuildRequires: libgmock-devel
BuildRequires: libxcbutil-icccm-devel
# right-click menu style
# Requires: deepin-menu
# run command by create_from_commandline
Requires: deepin-shortcut-viewer expect xdg-utils
Requires: icon-theme-hicolor
Requires: %name-data
Requires: terminalwidget5-data
#Recommends:     deepin-manual
#Recommends:     zssh

%description
%summary.

%package data
Summary: Data files of Deepin Terminal
Group: Terminals
BuildArch: noarch
Requires: icon-theme-hicolor

%description data
The %name-data package provides shared data for Deepin Terminal.

%package -n libterminalwidget5
Summary: Qt5 terminal widget
Group: System/Libraries
BuildRequires: lxqt-build-tools libutf8proc-devel

%description -n libterminalwidget5
QTermWidget is an opensource project based on KDE4 Konsole application.

The main goal of this project is to provide unicode-enabled,
embeddable QT5 widget for using as a built-in console or terminal emulation widget.

%package -n terminalwidget5-data
Summary: Data files of QTermWidget
Group: Other
BuildArch: noarch

%description -n terminalwidget5-data
The terminalwidget5-data package provides shared data for QTermWidget.

%package -n libterminalwidget5-devel
Summary: Qt5 terminal widget - development package
Group: Development/KDE and QT

%description -n libterminalwidget5-devel
Development package for QTermWidget. Contains headers and dev-libs.

%prep
%setup
# Much upstream weirdness
# sed -i '/<QHash>/i#include <QObject>\n#include <QMap>' 3rdparty/terminalwidget/lib/SessionManager.h
sed -i '/LXQtCompilerSettings/a remove_definitions(-DQT_NO_CAST_FROM_ASCII -DQT_NO_CAST_TO_ASCII)' 3rdparty/terminalwidget/CMakeLists.txt
# sed -i 's|default-config.json|src/assets/other/default-config.json|' CMakeLists.txt

%build
export PATH=%_qt5_bindir:$PATH
%cmake \
    -GNinja \
    -DDTKCORE_TOOL_DIR=%_libdir/libdtk-5*/DCore/bin \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DAPP_VERSION=%version \
    -DVERSION=%version
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang %name

%files -f %name.lang
%doc README.md
%doc LICENSE
%_bindir/%name

%files data
%_datadir/%name/
%_iconsdir/hicolor/*/apps/%{name}*
%_desktopdir/%name.desktop
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/terminal/

%files -n libterminalwidget5
%doc 3rdparty/terminalwidget/{AUTHORS,LICENSE*,CHANGELOG}
%_libdir/libterminalwidget5.so.*

%files -n terminalwidget5-data
%_datadir/terminalwidget5/

%files -n libterminalwidget5-devel
%_libdir/libterminalwidget5.so
%_pkgconfigdir/terminalwidget5.pc
%_libdir/cmake/terminalwidget5/
%_includedir/terminalwidget5/

%changelog
* Fri Nov 25 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.38-alt1
- New version.
- Upstream:
  + fix (theme switch): theme switch bug repair.
  + fix (terminal): the terminal command does not show the result.
  + fix: select copy.
  + fix: terminal width.

* Thu May 26 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.30-alt1
- New version.
- Upstream:
  + Minimize window size adjustment.

* Wed Apr 27 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.29-alt1
- New version (5.4.29).

* Fri Feb 04 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.28-alt1
- New version (5.4.28).

* Fri Oct 01 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.13-alt1
- New version (5.4.13).

* Thu Aug 26 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.12-alt1
- New version (5.4.12).
- Temporarily disabled link-time optimization.

* Wed Jun 23 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.6-alt2
- Added terminalwidget5-data in requires.

* Wed Jun 23 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.6-alt1
- New version (5.4.6) with rpmgs script.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 5.4.0.20-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.0.20-alt1
- New version (5.4.0.20) with rpmgs script.

* Wed Mar 17 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.0.13-alt1
- New version (5.4.0.13) with rpmgs script.

* Tue Dec 01 2020 Leontiy Volodin <lvol@altlinux.org> 5.4.0.6-alt1
- New version (5.4.0.6) with rpmgs script.

* Tue Nov 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.5-alt1
- New version (5.3.0.5) with rpmgs script.

* Thu Nov 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.1-alt1
- New version (5.3.0.1) with rpmgs script.

* Mon Nov 02 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.37-alt1
- New version (5.2.37) with rpmgs script.

* Fri Oct 09 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.35-alt1
- New version (5.2.35) with rpmgs script.

* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.20-alt1
- Initial build for ALT Sisyphus (thanks archlinux for this spec).
