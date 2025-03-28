%define _unpackaged_files_terminate_build 1
%define ext_id hanabi-extension@jeffshee.github.io
%define ext_schema_id io.github.jeffshee.hanabi-extension

Name: gnome-shell-extension-hanabi
Version: 20250307
Release: alt1

Summary: Live Wallpaper for GNOME
Summary(ru_RU.UTF-8): Живые обои для GNOME
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/jeffshee/gnome-ext-hanabi
Vcs: https://github.com/jeffshee/gnome-ext-hanabi.git

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

Requires: gnome-shell >= 42.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: %_bindir/glib-compile-schemas

%description
Extension for using videos as live wallpaper for GNOME Shell.

If the screen is black. Enabling options 'Force gtk4paintablesink'
or 'Force GtkMediaFile' in the extension settings can help.

%description -l ru_RU.UTF-8
Расширение для использования видео в качестве живых обоев в GNOME Shell.

Если экран черный. Включение опции 'Force gtk4paintablesink'
или 'Force GtkMediaFile' в настройках расширения может помочь.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %ext_id --with-gnome

%check
%meson_test

%files -f %ext_id.lang
%_datadir/glib-2.0/schemas/%ext_schema_id.gschema.xml
%_datadir/gnome-shell/extensions/%ext_id/
%doc README.md

%changelog
* Fri Mar 28 2025 Vladimir Vaskov <rirusha@altlinux.org> 20250307-alt1
- Initial build.
