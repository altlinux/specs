%define _unpackaged_files_terminate_build 1

Name: parapara
Version: 3.2.11
Release: alt1

Summary: lightweight and high-speed operation image viewer
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/aharotias2/parapara

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(granite)
BuildRequires: vapi(granite)

%description
ParaPara is an image viewer created with lightweight and high-speed operation
in mind.

It is designed to be linked to the extension and opened by double-clicking from
your favorite file manager.

Features:

- two page spread view
- right-to-left and left-to-right page turning
- horizontal or vertical continuous view modes

%prep
%setup
sed -i "s/Categories=.*/Categories=Graphics;Viewer;/" data/parapara.desktop.in
sed -i "s|data/icons/symbolic/||" README.md

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
%meson_test

%files -f %{name}.lang
%doc LICENSE README.md docs
%doc data/icons/symbolic/move-two-page-left-symbolic.svg data/icons/symbolic/move-one-page-left-symbolic.svg  data/icons/symbolic/move-one-page-right-symbolic.svg  data/icons/symbolic/move-two-page-right-symbolic.svg  data/icons/symbolic/read-right-to-left-symbolic.svg  data/icons/symbolic/read-left-to-right-symbolic.svg
%_bindir/com.github.aharotias2.parapara
%_desktopdir/com.github.aharotias2.parapara.desktop
%_iconsdir/hicolor/128x128/apps/com.github.aharotias2.parapara.svg
%_iconsdir/hicolor/16x16/apps/com.github.aharotias2.parapara.svg
%_iconsdir/hicolor/24x24/apps/com.github.aharotias2.parapara.svg
%_iconsdir/hicolor/32x32/apps/com.github.aharotias2.parapara.svg
%_iconsdir/hicolor/48x48/apps/com.github.aharotias2.parapara.svg
%_iconsdir/hicolor/64x64/apps/com.github.aharotias2.parapara.svg
%_datadir/metainfo/com.github.aharotias2.parapara.appdata.xml

%changelog
* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 3.2.11-alt1
- Initial build for Sisyphus
