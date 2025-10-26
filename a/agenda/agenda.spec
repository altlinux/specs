%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname com.github.dahenson.agenda

# TODO - fix GLib-GIO-FATAL-ERROR: Settings schema 'com.github.dahenson.agenda' is not installed
%def_without check

Name: agenda
Version: 1.2.1
Release: alt1

Summary: A simple, fast, no-nonsense to-do (task) list
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/dahenson/agenda

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: vapi(granite)

%if_with check
BuildRequires: /usr/bin/glib-compile-schemas
%endif

%description
A simple, fast, no-nonsense to-do (task) list for elementary OS.

Sometimes, you just need a task list to keep you motivated. Agenda
presents you with a quick and easy way to write down your tasks
and tick them off as you complete them. The list is saved automatically,
so you can close the list to get it out of the way and re-open it for a
quick check at any time.

%prep
%setup
sed -i 's|^Categories=.*|Categories=GTK;Office;ProjectManagement;|' data/com.github.dahenson.agenda.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
%meson_test

%files -f %{name}.lang
%doc LICENSE README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/metainfo/%{appname}.appdata.xml
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml

%changelog
* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
