%define _unpackaged_files_terminate_build 1
%define xdg_name de.philippun1.Snoop

Name: snoop
Version: 0.4
Release: alt1

Summary: Snoop through your files
License: GPL-3.0
Group: Sound
Url: https://gitlab.gnome.org/philippun1/snoop/
VCS: https://gitlab.gnome.org/philippun1/snoop/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: libgtk4-devel
BuildRequires: libadwaita-gir-devel
BuildRequires: libadwaita-devel
BuildRequires: libgtksourceview5-devel

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/snoop
%_datadir/nautilus-python/extensions/snoop.py
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/appdata/%xdg_name.appdata.xml
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Mon Nov 11 2024 Alexey Volkov <qualimock@altlinux.org> 0.4-alt1
- Initial build for ALT
