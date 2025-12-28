%define _unpackaged_files_terminate_build 1

%define appname io.github.ecommunity.app-generator

Name: elementary-app-generator
Version: 1.0.0
Release: alt1

Summary: Create an elementary OS app using one of the pre-made app templates
License: GPL-3.0-or-later
Group: Development/GNOME and GTK+
Url: https://github.com/ellie-commons/app-generator

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libadwaita-1)

%description
%summary

%prep
%setup
sed -i "s|Categories=.*|Categories=GTK;Development;ProjectManagement;|" data/app-generator.desktop.in
sed -i "s|https://raw.githubusercontent.com/elementary-community/app-generator/refs/heads/main/data/||" README.md
sed -i "s|data/icons/128.svg|/usr/share/icons/hicolor/128x128/apps/io.github.ecommunity.app-generator.svg|" README.md

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc LICENSE README.md data/io.github.ecommunity.app-generator.png
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/metainfo/%{appname}.appdata.xml

%changelog
* Sat Dec 27 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
