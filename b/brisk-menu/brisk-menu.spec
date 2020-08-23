Name:     brisk-menu
Version:  0.6.2
Release:  alt1

Summary:  An efficient menu for the MATE Desktop
License:  GPLv2
Group:    Other
Url:      https://github.com/getsolus/brisk-menu

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Source1:  translations.tar

BuildRequires(pre): meson
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: libgtk+3-devel
BuildRequires: mate-panel-devel
BuildRequires: mate-menus-devel
BuildRequires: libnotify-devel

Requires: mate-menu-editor

%description
brisk-menu is a modern and efficient menu designed to improve the MATE
Desktop Environment with modern, first-class options. The purpose of
this project is to provide a usable menu as seen in other desktops
without the bloat and performance issues.

%prep
%setup
tar xf %SOURCE1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc AUTHORS README.md
%_libexecdir/%name
%_datadir/dbus-1/services/org.mate.panel.applet.BriskMenuFactory.service
%_datadir/glib-2.0/schemas/com.solus-project.brisk-menu.gschema.xml
%_datadir/mate-panel/applets/com.solus_project.brisk.BriskMenu.mate-panel-applet
%_iconsdir/hicolor/scalable/actions/brisk_system-log-out-symbolic.svg

%changelog
* Sat Aug 22 2020 Andrey Cherepanov <cas@altlinux.org> 0.6.2-alt1
- New version.

* Tue Sep 10 2019 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1
- New version.
- Add translations from https://github.com/getsolus/brisk-menu-translations.git.

* Fri Aug 09 2019 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- New version.

* Wed Jun 05 2019 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt2.gitc809be3
- Add mate-menu-editor to requirements.

* Thu May 30 2019 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1.gitc809be3
- Initial build for Sisyphus.
