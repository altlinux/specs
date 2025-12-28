%define _unpackaged_files_terminate_build 1

%define appname app.paletti.gtk

Name: paletti
Version: 2025.05
Release: alt1

Summary: Create a color palette from an image
License: Leptonica
Group: Graphics
Url: https://github.com/Eroica/Paletti

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(lept)

%description
Paletti reduces an image into fewer colors to simplify it visually or to
create color palettes.

%prep
%setup -q -n %{name}-%{version}/gtk
sed -i "s|gtk/data/icons/hicolor/256x256/apps/app.paletti.gtk.png|%_iconsdir/hicolor/256x256/apps/app.paletti.gtk.png|" ../README.asciidoc
sed -i "s|:imagesdir: docs/images|:imagesdir: .|" ../README.asciidoc
sed -i "s|Categories=.*|Categories=GTK;Graphics;2DGraphics;RasterGraphics;|" data/app.paletti.gtk.desktop.in

sed -i "s|version: \'v.*',|version: \'v%{version}',|" meson.build
sed -i "s|version = \"v.*\",|version = \"v%{version}\",|" src/application.vala

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc ../LICENSE ../README.asciidoc ../docs/images/Paletti.gif
%_bindir/Paletti
%_desktopdir/%{appname}.desktop
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/*/apps/%{appname}.png
%_iconsdir/hicolor/symbolic/apps/%{appname}-symbolic.svg
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sun Dec 28 2025 Nikolay Strelkov <snk@altlinux.org> 2025.05-alt1
- Initial build for Sisyphus
