# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-atomic/icons to altlinux branch 

%define _unpackaged_files_terminate_build 1

Name: icon-theme-alt-atomic
Version: 0.1
Release: alt1

Summary: Icon theme for ALT Atomic
Group: Graphics
License: CC-BY-SA-4.0
Url: https://atomic.alt-gnome.ru/
Vcs: https://altlinux.space/alt-atomic/icons.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: python3(cairosvg)
BuildRequires: gtk4-update-icon-cache

%description
%summary.

%package onyx
Summary: ALT Atomic Onyx theme
Group: Graphics

BuildArch: noarch

Requires: icon-theme-morewaita
Requires: icon-theme-adwaita
Requires: icon-theme-adwaita-legacy
Requires: alt-atomic-icons

%description onyx
%summary.

%package -n alt-atomic-icons
Summary: ALT Atomic icons
Group: Graphics

BuildArch: noarch

Requires: icon-theme-hicolor

%description -n alt-atomic-icons
%summary.

%package -n alt-atomic-logos
Summary: ALT Atomic logos
Group: Graphics

BuildArch: noarch

%description -n alt-atomic-logos
%summary.

%prep
%setup

%build
python3 ./create_png.py
%meson
%meson_build

%install
%meson_install

%files onyx
%_iconsdir/ALTAtomicOnyx

%files -n alt-atomic-icons
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg

%files -n alt-atomic-logos
%_datadir/distro-logos/*

%changelog
* Thu Aug 21 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.1-alt1
- Initial build.
