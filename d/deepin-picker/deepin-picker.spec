Name: deepin-picker
Version: 6.0.0
Release: alt1
Summary: Color picker tool for deepin
License: GPL-3.0+
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-picker
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): desktop-file-utils
BuildRequires: qt5-linguist dtk5-widget-devel libX11-devel libxcb-devel libxcbutil-devel libXext-devel libXtst-devel qt5-base-devel qt5-svg-devel qt5-x11extras-devel
Requires: icon-theme-hicolor

%description
Simplest color picker.

%prep
%setup

%build
export PATH=%_qt5_bindir:$PATH
%qmake_qt5 \
    CONFIG+=nostrip \
    PREFIX=%_prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc README.md
%doc LICENSE.txt
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/dbus-1/services/com.deepin.Picker.service

%changelog
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

