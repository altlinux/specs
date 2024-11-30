%define APP_ID io.github.ronniedroid.concessio
%def_enable check

Name: concessio
Version: 0.1.9
Release: alt1

Summary: Understand file permissions
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://github.com/ronniedroid/concessio
Vcs: https://github.com/ronniedroid/concessio
Source0: %name-%version.tar

Requires: typelib(Adw) >= 1
Requires: typelib(Gdk) >= 4.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.62.0
BuildRequires: gtk4-update-icon-cache
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gjs-1.0)

%description
Concessio helps you understand and convert between unix permissions
representations

* Convert between symbolic and numeric representations of UNIX file permissions
* Use toggle buttons to update the symbolic and numeric fields
* Open a file to read it's permissions and convert them
* Open the help dialog to read and understand the UNIX permissions system

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %APP_ID

%check
%meson_test

%files -f %APP_ID.lang
%_bindir/%APP_ID
%_desktopdir/%APP_ID.desktop
%_datadir/dbus-1/services/%APP_ID.service
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/%APP_ID
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Sat Nov 30 2024 Oleg Shchavelev <oleg@altlinux.org> 0.1.9-alt1
- New version 0.1.9
- Add typelib(Adw), typelib(Gdk) dependencies (ALT #52170)

* Sun Nov 24 2024 Oleg Shchavelev <oleg@altlinux.org> 0.1.8-alt1
- Initial build
