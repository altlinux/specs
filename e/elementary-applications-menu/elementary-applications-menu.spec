%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname slingshot

%def_with check

Name: elementary-applications-menu
Version: 8.0.4
Release: alt1.git.6f5b14b

Summary: Applications Menu for elementary OS and the Pantheon desktop environment
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/applications-menu

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(switchboard-3)
BuildRequires: pkgconfig(wingpanel-9)
BuildRequires: pkgconfig(zeitgeist-2.0)

%if_with check
BuildRequires: /usr/bin/bc
%endif

%description
Slingshot is an launcher for Pantheon, written in Vala and utilizing
GTK+ and Cairo.

It features an optional category view and fast application search that
uses Synapse as a back-end.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc COPYING README.md
%_libdir/io.elementary.wingpanel.applications-menu/switchboard-plugin
%_libdir/wingpanel-9/libslingshot.so
%_datadir/glib-2.0/schemas/io.elementary.desktop.wingpanel.applications-menu.gschema.xml
%_datadir/metainfo/io.elementary.wingpanel.applications-menu.metainfo.xml

%changelog
* Sat May 09 2026 Nikolay Strelkov <snk@altlinux.org> 8.0.4-alt1.git.6f5b14b
- Initial build for Sisyphus from danirabbit/gtk4 branch.
