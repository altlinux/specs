%global _unpackaged_files_terminate_build 1

Name: showmethekey
Version: 1.18.4
Release: alt1

Summary: Show keys you typed on screen
License: Apache-2.0
Group: Graphics
Url: https://showmethekey.alynx.one
Vcs: https://github.com/AlynxZhou/showmethekey

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: libevdev-devel
BuildRequires: libudev-devel
BuildRequires: libinput-devel
BuildRequires: libadwaita-devel
BuildRequires: libjson-glib-devel
BuildRequires: libxkbcommon-devel

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
# No need to package the license info twice
rm %buildroot%_datadir/licenses/showmethekey/LICENSE
%find_lang %name

%files -f %name.lang
%doc *.md
%_bindir/showmethekey-cli
%_bindir/showmethekey-gtk
%_desktopdir/one.alynx.showmethekey.desktop
%_datadir/glib-2.0/schemas/one.alynx.showmethekey.gschema.xml
%_iconsdir/hicolor/128x128/apps/one.alynx.showmethekey.png
%_iconsdir/hicolor/64x64/apps/one.alynx.showmethekey.png
%_iconsdir/hicolor/scalable/apps/one.alynx.showmethekey.svg
%_datadir/metainfo/one.alynx.showmethekey.metainfo.xml
%_datadir/polkit-1/actions/one.alynx.showmethekey.policy
%_datadir/polkit-1/rules.d/one.alynx.showmethekey.rules

%changelog
* Tue Aug 12 2025 Alexander Stepchenko <geochip@altlinux.org> 1.18.4-alt1
- Initial build for ALT
