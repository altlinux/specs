%define _unpackaged_files_terminate_build 1
%define xdg_name de.philippun1.Snoop

Name: snoop
Version: 0.4.1
Release: alt1

Summary: Snoop through your files
License: GPL-3.0-or-later
Group: File tools
Url: https://gitlab.gnome.org/philippun1/snoop/
VCS: https://gitlab.gnome.org/philippun1/snoop/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(blueprint-compiler)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gtksourceview-5)

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
* Fri Nov 22 2024 Alexey Volkov <qualimock@altlinux.org> 0.4.1-alt1
- New version 0.4.1

* Mon Nov 11 2024 Alexey Volkov <qualimock@altlinux.org> 0.4-alt2
- Fix license and group

* Mon Nov 11 2024 Alexey Volkov <qualimock@altlinux.org> 0.4-alt1
- Initial build for ALT
