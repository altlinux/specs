Name: icon-theme-morewaita
Version: 47.3
Release: alt1

Summary: An expanded Adwaita-styled companion icon theme with extra icons
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/somepaulo/MoreWaita
Vcs: https://github.com/somepaulo/MoreWaita

BuildArch: noarch

Source: %name-%version.tar

Requires: icon-naming-utils

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson icon-naming-utils gtk4-update-icon-cache %_bindir/gtk-encode-symbolic-svg

%description
An expanded Adwaita-styled companion icon theme with extra icons for popular apps to complement
Gnome Shell's original icons.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
cp -r scalable symbolic %buildroot/%_iconsdir/MoreWaita/

%files
%_iconsdir/MoreWaita/
%doc AUTHORS LICENSE README.md

%changelog
* Mon Jan 27 2025 Anton Midyukov <antohami@altlinux.org> 47.3-alt1
- Initial build
