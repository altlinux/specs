%define _unpackaged_files_terminate_build 1

%def_with check

Name: savedesktop
Version: 3.8.1
Release: alt1

Summary: Save your desktop configuration
License: GPL-3.0-or-later
Group: Graphical desktop/Other
URL: https://vikdevelop.github.io/SaveDesktop
VCS: https://github.com/vikdevelop/SaveDesktop

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: /usr/bin/appstreamcli
BuildRequires: /usr/bin/gtk-update-icon-cache
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: rpm-build-python3

%filter_from_requires /python3(savedesktop.core.archive)/d
%filter_from_requires /python3(savedesktop.core.password_store)/d
%filter_from_requires /python3(savedesktop.core.periodic_saving)/d
%filter_from_requires /python3(savedesktop.gui.items_dialog)/d
%filter_from_requires /python3(savedesktop.gui.more_options_dialog)/d
%filter_from_requires /python3(savedesktop.gui.password_checker)/d
%filter_from_requires /python3(savedesktop.gui.synchronization_dialogs)/d

BuildArch: noarch

Source: %name-%version.tar

%description
Save Desktop helps you back up, restore, and synchronize your entire
desktop environment with ease. It saves and imports your themes, icons,
fonts, wallpapers, extensions, desktop folder, Flatpak apps and their
data, as well as other desktop settings - all in one archive. Choose
what to include and keep your setup consistent across devices with
automatic periodic saves and synchronization.

%prep
%setup
sed -i "s|Categories=.*|Categories=GTK;Utility;FileTools;|" data/io.github.vikdevelop.SaveDesktop.desktop.in
sed -i "s|/data/icons/|%_iconsdir/|g" README.md
sed -i "s|/data/screenshots/||g" README.md

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc README.md data/screenshots/*.png
%_bindir/savedesktop
%_desktopdir/io.github.vikdevelop.SaveDesktop.desktop
%_datadir/dbus-1/services/io.github.vikdevelop.SaveDesktop.service
%_datadir/glib-2.0/schemas/io.github.vikdevelop.SaveDesktop.gschema.xml
%_iconsdir/hicolor/scalable/apps/io.github.vikdevelop.SaveDesktop.Devel.svg
%_iconsdir/hicolor/scalable/apps/io.github.vikdevelop.SaveDesktop.svg
%_iconsdir/hicolor/scalable/status/done.svg
%_iconsdir/hicolor/symbolic/apps/io.github.vikdevelop.SaveDesktop-symbolic.svg
%exclude %_datadir/locale/zh_Hans/LC_MESSAGES/savedesktop.mo
%_datadir/metainfo/io.github.vikdevelop.SaveDesktop.metainfo.xml
%dir %_datadir/savedesktop
%_datadir/savedesktop/*

%changelog
* Sat Jan 17 2026 Nikolay Strelkov <snk@altlinux.org> 3.8.1-alt1
- Initial build for Sisyphus
