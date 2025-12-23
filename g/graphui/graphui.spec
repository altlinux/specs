%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname com.github.artemanufrij.graphui

Name: graphui
Version: 1.1.1
Release: alt1

Summary: Graph Visualization
License: GPL-3.0-or-later
Group: Publishing
Url: https://github.com/artemanufrij/graphui

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gtksourceview-3.0)
BuildRequires: vapi(granite)

Requires: elementary-icon-theme
Requires: graphviz

%description
Graph visualization based on graphviz, written especially
for elementary OS.

%prep
%setup
sed -i "s|Categories=.*|Categories=Office;GNOME;GTK;Chart;FlowChart;|" data/com.github.artemanufrij.graphui.desktop.in
sed -i "s|data/icons/64/|%_iconsdir/hicolor/64x64/apps/|" README.md

%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc debian/copyright README.md screenshots
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.appdata.xml

%changelog
* Tue Dec 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
