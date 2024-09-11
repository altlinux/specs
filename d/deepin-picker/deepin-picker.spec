Name: deepin-picker
Version: 6.0.1
Release: alt2

Summary: Color picker tool for deepin

License: GPL-3.0+
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-picker

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): desktop-file-utils
BuildRequires: dqt5-linguist libdtkwidget-devel libX11-devel libxcb-devel libxcbutil-devel libXext-devel libXtst-devel dqt5-base-devel dqt5-svg-devel dqt5-x11extras-devel

Requires: icon-theme-hicolor

%description
Simplest color picker.

%prep
%setup

%build
export PATH=%_dqt5_bindir:$PATH
%qmake_dqt5 \
  CONFIG+=nostrip \
  PREFIX=%_prefix \
  QMAKE_RPATHDIR=%_dqt5_libdir \
#
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
%find_lang --with-qt %name

%files -f %name.lang
%doc README.md
%doc LICENSE.txt
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/dbus-1/services/com.deepin.Picker.service
# package translations outside find_lang
#%%dir %%_datadir/%%name/
#%%dir %%_datadir/%%name/translations/
#%%_datadir/%%name/translations/deepin-picker.qm
#%%_datadir/%%name/translations/deepin-picker_es_419.qm

%changelog
* Wed Sep 11 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.1-alt2
- Built via separate qt5 instead system (ALT #48138).

* Thu Apr 04 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.1-alt1
- New version.

* Fri Mar 03 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.0-alt1
- New version.

* Fri Jun 17 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.28-alt1
- New version.
- Upstream:
  + fix: Use the picker card under wayland.
  + fix: wayland: You can't click on the color collector under the touch screen
  and can't click to pick color.
  + fix: wayland: Click on Esc after tapping the color collector to get out
  of the color collector
  + fix: Multi-screen-copy screen cannot use the color collector normally.

* Tue Apr 19 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.24-alt1
- New version (5.0.24).

* Thu Jul 01 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.18-alt1
- New version (5.0.18).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.16-alt1
- New version (5.0.16) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.14-alt1
- New version (5.0.14) with rpmgs script.

* Tue Nov 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.10-alt1
- New version (5.0.10) with rpmgs script.

* Thu Nov 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.8-alt1
- New version (5.0.8) with rpmgs script.
- Enabled debuginfo.

* Mon Aug 03 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.6-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

