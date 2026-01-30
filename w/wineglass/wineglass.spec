%define _unpackaged_files_terminate_build 1

%define appname com.github.aggalex.wineglass

Name: wineglass
Version: 1.2.1
Release: alt2

Summary: GUI for Wine
License: GPL-3.0-or-later
Group: Emulators
Url: https://github.com/aggalex/Wineglass

Source: %name-%version.tar

ExcludeArch: loongarch64 riscv64

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(granite)
BuildRequires: vapi(granite)

Requires: hicolor-icon-theme
Requires: wine
Requires: winetricks
Requires: zenity

%description
Wineglass is a small application that allows the user to manage their
wineprefixes easily and install windows programs without the need of the
terminal. It can:

* Easily create and remove wineprefixes.
* Install supported windows apps on their corresponding wineprefix.
* Make installed apps available normally through the applications menu.
* Provide an easy way to add windows libraries to wineprefixes through
  "winetricks".
* Configure wine.
* run winprefix-specific system apps.

This app is useful for running windows apps and games easily without
hassle.

%prep
%setup
%patch -p1
sed -i "s|https://github.com/aggalex/Wineglass/blob/master/data/icons/64/|%_iconsdir/hicolor/64x64/apps/|" README.md

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc LICENSE.md README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/metainfo/%{appname}.appdata.xml
%dir %_datadir/wineglass
%_datadir/wineglass/dnd_image.svg
%_datadir/wineglass/style.css

%changelog
* Fri Jan 30 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.1-alt2
- Exclude loongarch64 and riscv64 arches as not runnable.

* Tue Dec 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
