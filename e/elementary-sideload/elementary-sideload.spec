%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.sideload

Name: elementary-sideload
Version: 6.3.0
Release: alt1

Summary: Sideload Flatpaks on elementary OS
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/sideload

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(flatpak)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libxml-2.0)

%description
%summary

%prep
%setup
sed -i 's|^Categories=.*|Categories=PackageManager;Settings;|' data/sideload.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc LICENSE README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sat Sep 20 2025 Nikolay Strelkov <snk@altlinux.org> 6.3.0-alt1
- Initial build for Sisyphus
