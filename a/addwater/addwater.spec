%define APP_ID dev.qwery.AddWater
%def_enable check

Name: addwater
Version: 1.1.6
Release: alt1

Summary: Keep Firefox in fashion
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://addwater.qwery.dev/
Vcs: https://github.com/largestgithubuseronearth/addwater
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: meson >= 0.59.0
BuildRequires: gtk4-update-icon-cache
BuildRequires: pkgconfig(gio-2.0)
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
BuildRequires: %_bindir/glib-compile-schemas
%endif

BuildArch: noarch

%description
A utility app to easily install the GNOME for Firefox Theme and automatically
update it in the background. This theme keeps Firefox fashionable within
the GNOME design ecosystem, and provides many helpful features to customize
the interface to make browsing even more pleasant:

* Supports light and dark style
* Hide Tab Bar when only one tab is open
* Use an OLED-friendly pitch black instead of grey
* Customize Tab Bar position, position of controls, alignment, and more
* Hide redundant microphone, webcam, screen share indicators
* Supports Flatpak, Snap, Librewolf, and Floorp variants of Firefox

The GNOME for Firefox Theme itself is developed and maintained by Rafael
Mardojai CM.

The Firefox browser is not included and must be downloaded separately.
This project is not affiliated or endorsed by the Mozilla Foundation.
Firefox is a trademark of the Mozilla Foundation
in the U.S. and other countries.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/scalable/apps/%APP_ID.svg
%_iconsdir/hicolor/symbolic/apps/apps/%APP_ID-symbolic.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Wed Nov 13 2024 Oleg Shchavelev <oleg@altlinux.org> 1.1.6-alt1
- Initial build
