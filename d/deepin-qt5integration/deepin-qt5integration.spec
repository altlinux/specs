%define repo qt5integration

%def_without clang

Name: deepin-qt5integration
Version: 5.6.28
Release: alt1

Summary: Qt platform theme integration plugins for DDE

License: LGPL-3.0-or-later
Group: System/Libraries
Url: https://github.com/linuxdeepin/qt5integration

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
# dqt5-base-devel-static for libQt5ThemeSupport.a
# Automatically added by buildreq on Sat Oct 28 2023
# optimized out: cmake-modules gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libdouble-conversion3 libdtkcore-devel libdtkgui-devel libgio-devel libglvnd-devel libgpg-error libgsettings-qt libp11-kit libdqt5-concurrent libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-network libdqt5-printsupport libdqt5-svg libdqt5-widgets libdqt5-x11extras libdqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libxcb-devel pkg-config python3 python3-base python3-dev python3-module-setuptools dqt5-base-devel dqt5-svg-devel sh5 xorg-proto-devel
BuildRequires: cmake dtk6-common-devel libdtkwidget-devel libgtest-devel libmtdev-devel libqtxdg-devel dqt5-base-devel-static dqt5-x11extras-devel

# Requires: deepin-qt5platform-plugins
Requires: libdqt5-core = %_dqt5_version libdqt5-gui = %_dqt5_version libdqt5-widgets = %_dqt5_version

%if_with clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

%description
Multiple Qt plugins to provide better Qt5 integration for DDE is included.

%prep
%setup -n %repo-%version

%build
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake/Qt5X11Extras:%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DPLUGIN_INSTALL_BASE_DIR=%_dqt5_plugindir \
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files
%doc README.md
%doc LICENSE
%_dqt5_plugindir/iconengines/libdicon.so
%_dqt5_plugindir/iconengines/libdsvgicon.so
%_dqt5_plugindir/imageformats/libdci.so
%_dqt5_plugindir/imageformats/libdsvg.so
%_dqt5_plugindir/platformthemes/libqdeepin.so
%_dqt5_plugindir/styles/libchameleon.so

%changelog
* Wed May 15 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.28-alt1
- New version 5.6.28.
- Built via separate qt5 instead system (ALT #48138).

* Fri Mar 29 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.26-alt1
- New version 5.6.26.

* Wed Mar 20 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.25-alt1
- New version 5.6.25.

* Fri Jan 19 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.20.0.2.b020-alt2
- Requires: libqt5-core = %%_qt5_version.

* Tue Jan 16 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.20.0.2.b020-alt1
- New version 5.6.20-2-gb020f02.

* Sat Oct 28 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.17-alt1
- New version 5.6.17.
- Built via cmake instead qmake (by upstream).

* Fri Jun 02 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.11-alt1
- New version.

* Tue Apr 18 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.10-alt1
- New version.

* Fri Mar 17 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.6-alt1
- New version.
- Upstream:
  + fix: file-manager is crashed when loading xdgiconproxyengine.
  + fix: Calculating size different for SpinBox up and down.

* Wed Feb 15 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.5-alt1
- New version.

* Mon Dec 12 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.3-alt1
- New version.
- Updated url tag.

* Thu Oct 20 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.24-alt1
- New version.
- Upstream:
  + fix: reduces the distance between menu item icons and text.
  + chore: spinner of dtoolbutton dropdown arrow with menu.
  + feat: configurable proxy icon engine.
  + fix: editable combobox has no background color.

* Tue Jul 12 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.23.1-alt1
- New version.
- Upstream:
  + chore: Log output adjustment.
  + chore: Modify unit test generation catalog.
  + chore: Remove the debug log.
  + chore: The menu round angle follows the round corner of the control center.
  + fix: wayland menu interface is not rounded.
  + fix: At the time of warning prompt, the background color of the combobox
  input box has not changed.
  + fix: combobox pops up menu text and pictures.
  + fix: The calendar window of the non-DTK application draws a round corner.
  + fix: Combobox text with icon is too long to omit.
  + fix: MouseEvent intercepted in QScrollArea's scrollbar.
  + fix: Access null pointer for QScrollArea.
  + fix: editable combobox warning tips do not warn background color.
  + chore: remove qt5widget5 depends from themeplugin.
  + fix: The main window and sub-menu window frame overlap display.
  + chore: No BASED_DTK_DIR is generated when chooser related libraries are
  not generated.
  + chore: replace dde-qt5integration5.5.

* Fri Apr 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.20-alt1
- New version (5.5.20).

* Fri Feb 11 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.17-alt1
- New version (5.5.17).

* Thu Aug 19 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.8-alt1
- New version (5.5.8).

* Wed Jul 14 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.3-alt1
- New version (5.5.3).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.1.12-alt1
- New version (5.1.12) with rpmgs script.

* Fri Apr 30 2021 Leontiy Volodin <lvol@altlinux.org> 5.1.11-alt2
- Disabled multithreaded build.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.1.11-alt1
- New version (5.1.11) with rpmgs script.

* Fri Apr 02 2021 Leontiy Volodin <lvol@altlinux.org> 5.1.5-alt2.gitcb2a4e4
- Build from commit cb2a4e4c310b3749cd7e5e66de4c2ad3c5689550.

* Tue Dec 01 2020 Leontiy Volodin <lvol@altlinux.org> 5.1.5-alt1
- New version (5.1.5) with rpmgs script.

* Wed Nov 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.1.0.9-alt1
- New version (5.1.0.9) with rpmgs script.

* Thu Oct 08 2020 Leontiy Volodin <lvol@altlinux.org> 5.1.0.8-alt1
- New version (5.1.0.8) with rpmgs script.

* Tue Aug 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.1.0.4-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
