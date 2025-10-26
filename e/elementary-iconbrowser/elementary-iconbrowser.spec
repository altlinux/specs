%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.iconbrowser

Name: elementary-iconbrowser
Version: 8.1.0
Release: alt1

Summary: Browse and search system icons
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/iconbrowser

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(gtksourceview-5)

%description
%summary on Elementary/Pantheon.

%prep
%setup
sed -i "s/Categories=.*/Categories=Graphics;2DGraphics;/" data/iconbrowser.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %appname.lang
%doc COPYING README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%exclude %_datadir/locale/zh_Hant/LC_MESSAGES/%{appname}.mo
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.appdata.xml

%changelog
* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 8.1.0-alt1
- Initial build for Sisyphus
