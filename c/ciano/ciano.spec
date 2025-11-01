%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname com.github.robertsanseries.ciano

Name: ciano
Version: 0.2.4
Release: alt1

Summary: A multimedia file converter focused on simplicity
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/robertsanseries/ciano

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

Requires: /usr/bin/ffmpeg
Requires: /usr/bin/convert

%description
Convert videos, music and pictures with the best possible experience.

%prep
%setup
sed -i "s/Categories=.*/Categories=GTK;Utility;FileTools;/" data/com.github.robertsanseries.ciano.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %appname.lang
%doc AUTHORS LICENSE README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%dir %_datadir/ciano
%dir %_datadir/ciano/images
%_datadir/ciano/images/%{appname}.svg
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/metainfo/%{appname}.appdata.xml
%_pixmapsdir/%{appname}.png

%changelog
* Sat Nov 01 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.4-alt1
- Initial build for Sisyphus
