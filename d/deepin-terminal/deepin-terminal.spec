%define _libexecdir %_prefix/libexec
%define twver 0

Name: deepin-terminal
Version: 6.0.12
Release: alt2

Summary: Default terminal emulation application for Deepin

License: GPL-3.0+ and (LGPL-2.0+ and GPL-2.0+ and BSD-3-Clause)
Group: Terminals
Url: https://github.com/linuxdeepin/deepin-terminal

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

Requires: deepin-shortcut-viewer expect xdg-utils
Requires: icon-theme-hicolor
Requires: %name-data
Requires: terminalwidget5-data
Requires: libdqt5-widgets = %_dqt5_version
#Recommends:     deepin-manual
#Recommends:     zssh

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5 patchelf
# Automatically added by buildreq on Mon Oct 23 2023
# optimized out: cmake-modules fontconfig-devel gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libdouble-conversion3 libdtkcore-devel libdtkgui-devel libfreetype-devel libgio-devel libglvnd-devel libgpg-error libgsettings-qt libp11-kit libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-network libdqt5-printsupport libdqt5-svg libdqt5-widgets libdqt5-x11extras libdqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libxcb-devel libxcbutil-icccm pkg-config python3 python3-base dqt5-base-devel dqt5-tools sh5
BuildRequires: cmake libdtkwidget-devel libsecret-devel libxcbutil-icccm-devel lxqt-build-tools dqt5-tools-devel dqt5-x11extras-devel

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
%patch -p1

%build
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export PATH=%_dqt5_bindir:$PATH
%cmake \
    -GNinja \
    -DDTKCORE_TOOL_DIR=%_libexecdir/dtk5/DCore/bin \
    -DCMAKE_BUILD_TYPE=Release \
    -DTERM_RPATH=OFF \
    -DCMAKE_SKIP_RPATH=NO \
    -DCMAKE_SKIP_INSTALL_RPATH=NO \
    -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DVERSION=%version
cmake --build "%_cmake__builddir" -j%__nprocs
# remove broken build rpath from elfs
patchelf %_host_alias/%name --shrink-rpath --allowed-rpath-prefixes %_dqt5_libdir
# find requires for pc file
sed -i -e '/Libs/s|terminalwidget5|terminalwidget5 -L%_dqt5_libdir -lQt5Widgets|; s|Requires:.*|Requires:|;' \
  %_host_alias/3rdparty/terminalwidget/terminalwidget5.pc

%install
%cmake_install
%find_lang --with-qt %name
%find_lang --with-qt terminalwidget5

%files
%doc README.md
%doc LICENSE
%_bindir/%name

%files data -f %name.lang
%_iconsdir/hicolor/*/apps/%{name}*
%_desktopdir/%name.desktop
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/terminal/
# outside %%find_lang
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/translations/%name.qm

%files -n libterminalwidget5
%doc 3rdparty/terminalwidget/{AUTHORS,LICENSE*,CHANGELOG}
%_libdir/libterminalwidget5.so.%{twver}*

%files -n terminalwidget5-data -f terminalwidget5.lang
%dir %_datadir/terminalwidget5/
%dir %_datadir/terminalwidget5/translations/
%_datadir/terminalwidget5/kb-layouts/
%_datadir/terminalwidget5/color-schemes/

%files -n libterminalwidget5-devel
%_libdir/libterminalwidget5.so
%_pkgconfigdir/terminalwidget5.pc
%_libdir/cmake/terminalwidget5/
%_includedir/terminalwidget5/

%changelog
* Wed May 22 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.12-alt2
- Built via separate qt5 instead system (ALT #48138).

* Wed Mar 27 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.12-alt1
- New version 6.0.12.
- Cleanup spec.

* Tue Mar 05 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.11-alt1
- New version 6.0.11.
- Requires: libqt5-widgets = %%_qt5_version.

* Fri Dec 01 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.9-alt1
- New version 6.0.9.
- Cleanup spec and BRs.

* Sun Jan 08 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.1-alt1
- New version.
- Cleanup spec.

* Tue Dec 06 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.39-alt1
- New version.

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
