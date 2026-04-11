%define _unpackaged_files_terminate_build 1

%define appname org.gnome.gitlab.ilhooq.Bookup

%def_with check

Name: bookup
Version: 1.1.6
Release: alt1

Summary: A markdown note-taking application for Gnome
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/ilhooq/bookup

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake

BuildRequires: meson
BuildRequires: cmake
BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: /usr/bin/appstream-util
BuildRequires: /usr/bin/glib-compile-schemas
BuildRequires: pkgconfig(libmarkdown)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: pkgconfig(sqlite3)

%if_with check
BuildRequires: ctest
%endif

%description
Bookup: A lightweight note-taking application

Book-up is a simple and efficient note-taking application written
in C and GTK4, designed as a clone of Notes-up.

Unlike Notes-up, Book-up doesn't have any Granite dependency,
making it ideal for non-Elementary OS users.

Features:

* Organization of notes in books (which are sqlite databases).
* Arrangement of notes in tree form.
* Markdown syntax highlighting in edit mode.
* Sections and notes can be reorganized by dragging and dropping
  with the mouse.
* Assignment of tags to make it easier to find notes.
* Easy-to-use markdown editor.
* Export notes to PDF and Markdown formats.
* Ability to customize the editor and viewer appearance.

%prep
%setup
sed -i "s/Categories=.*/Categories=GNOME;GTK;Office;WordProcessor;/" data/org.gnome.gitlab.ilhooq.Bookup.desktop.in
%ifarch %ix86
sed -i "s/\%lu/\%u/" src/bookup-window.c
%endif

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%ctest -j1 -VV

%files -f %{name}.lang
%doc COPYING README.md screenshot
%_bindir/bookup
%_desktopdir/%{appname}.desktop
%dir %_datadir/bookup
%_datadir/bookup/page.css
%_datadir/glib-2.0/schemas/org.gnome.gitlab.ilhooq.bookup.gschema.xml
%_iconsdir/hicolor/scalable/apps/%{appname}.svg
%_iconsdir/hicolor/symbolic/apps/%{appname}-symbolic.svg
%_datadir/metainfo/%{appname}.metainfo.xml
%_datadir/mime/packages/%{appname}.xml

%changelog
* Sat Apr 11 2026 Nikolay Strelkov <snk@altlinux.org> 1.1.6-alt1
- New version 1.1.6.

* Sat Jan 31 2026 Nikolay Strelkov <snk@altlinux.org> 1.1.5-alt2
- Enabled build on i586.

* Sat Nov 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.5-alt1
- Initial build for Sisyphus
