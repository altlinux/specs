%define _cmake__builddir BUILD
%define _libexecdir %_prefix/libexec
%define twver 0
# prevent bytes written limit by hasher-privd
%global __find_debuginfo_files %nil

Name: deepin-terminal
Version: 6.5.38
Release: alt1

Summary: Default terminal emulation application for Deepin

License: GPL-3.0+ and (LGPL-2.0+ and GPL-2.0+ and BSD-3-Clause)
Group: Terminals
Url: https://github.com/linuxdeepin/deepin-terminal
Vcs: https://github.com/linuxdeepin/deepin-terminal

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: icon-theme-hicolor
Requires: %name-data = %EVR
Requires: terminalwidget6-data = %EVR
Requires: libdqt6-gui = %_dqt6_version

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6 patchelf rpm-macros-cmake
BuildRequires: cmake dqt6-5compat-devel dqt6-lxqt-build-tools dqt6-tools-devel dtk6-common-devel libchardet-devel libdtk6widget-devel libicu-devel libsecret-devel libuchardet-devel libxcbutil-icccm-devel vulkan-headers

%description
%summary.

%package data
Summary: Data files of Deepin Terminal
Group: Terminals
BuildArch: noarch
Requires: icon-theme-hicolor

%description data
The %name-data package provides shared data for Deepin Terminal.

%package -n libterminalwidget6
Summary: Qt5 terminal widget
Group: System/Libraries

%description -n libterminalwidget6
QTermWidget is an opensource project based on KDE4 Konsole application.

The main goal of this project is to provide unicode-enabled,
embeddable QT5 widget for using as a built-in console or terminal emulation widget.

%package -n terminalwidget6-data
Summary: Data files of QTermWidget
Group: Other
BuildArch: noarch
Provides: terminalwidget5-data = %EVR
Obsoletes: terminalwidget5-data < %EVR

%description -n terminalwidget6-data
The terminalwidget5-data package provides shared data for QTermWidget.

%package -n libterminalwidget6-devel
Summary: Qt5 terminal widget - development package
Group: Development/KDE and QT

%description -n libterminalwidget6-devel
Development package for QTermWidget. Contains headers and dev-libs.

%prep
%setup
%patch -p1

%build
export CMAKE_PREFIX_PATH=%_dqt6_datadir/cmake:$CMAKE_PREFIX_PATH
%DQ6build -DDTKCORE_TOOL_DIR=%_libexecdir/dtk6/DCore/bin
# find Qt6 libs in a non-standart location
patchelf %_cmake__builddir/%name --add-rpath %_dqt6_libdir

%install
%DQ6install
%find_lang --with-qt %name
%find_lang --with-qt terminalwidget6
patchelf %buildroot%_libdir/libterminalwidget6.so.%twver --add-rpath %_dqt6_libdir

%files
%doc README.md
%doc LICENSE
%doc debian/changelog
%_bindir/%name

%files data -f %name.lang
%_iconsdir/hicolor/*/apps/%{name}*
%_desktopdir/%name.desktop
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/terminal/
%dir %_datadir/deepin-debug-config/
%dir %_datadir/deepin-debug-config/deepin-debug-config.d/
%_datadir/deepin-debug-config/deepin-debug-config.d/org.deepin.terminal.json
%dir %_datadir/deepin-log-viewer/
%dir %_datadir/deepin-log-viewer/deepin-log.conf.d/
%_datadir/deepin-log-viewer/deepin-log.conf.d/org.deepin.terminal.json
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.terminal/
%_datadir/dsg/configs/org.deepin.terminal/org.deepin.terminal.json
# outside %%find_lang
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/translations/%name.qm

%files -n libterminalwidget6
%_libdir/libterminalwidget6.so.%{twver}*

%files -n terminalwidget6-data -f terminalwidget6.lang
%doc 3rdparty/terminalwidget/{AUTHORS,LICENSE*,CHANGELOG}
%dir %_datadir/terminalwidget6/
%dir %_datadir/terminalwidget6/translations/
%_datadir/terminalwidget6/kb-layouts/
%_datadir/terminalwidget6/color-schemes/

%files -n libterminalwidget6-devel
%_libdir/libterminalwidget6.so
%_pkgconfigdir/terminalwidget6.pc
%_libdir/cmake/terminalwidget6/
%_includedir/terminalwidget6/

%changelog
* Thu Jun 25 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.38-alt1
- New version 6.5.38.
- Built on Qt6 for DDE.

* Thu Feb 19 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.28-alt1
- New version 6.5.28.
- Built on separate lxqt-build-tools (no qt required).

* Wed Jan 21 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.25-alt1
- New version 6.5.25.

* Mon Dec 08 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.22-alt1
- New version 6.5.22.

* Wed Nov 19 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.20-alt1
- New version 6.5.20.

* Thu Oct 16 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.18-alt1
- New version 6.5.18.

* Mon Oct 06 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.17-alt1
- New version 6.5.17.

* Thu Sep 11 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.16-alt1
- New version 6.5.16.
- Fixed overlinked libraries.

* Tue Sep 09 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.5-alt1
- New version 6.5.5.

* Tue Apr 08 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.4-alt1
- New version 6.5.4.

* Wed Jan 15 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.17-alt1
- New version 6.0.17.

* Tue Dec 03 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.16-alt1
- New version 6.0.16.
- Added vcs tag.

* Wed Sep 25 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.14-alt1
- New version 6.0.14.

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
