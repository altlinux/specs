Name: icon-theme-morewaita
Version: 47.3
Release: alt3

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
# cleanup from meson.build files
find %buildroot/%_iconsdir/MoreWaita/ -name meson.build -exec rm -v {} \;

# remove incorrect icons
rm %buildroot%_iconsdir/MoreWaita/scalable/apps/synaptic.svg

%files
%_iconsdir/MoreWaita/
%doc AUTHORS LICENSE README.md

%changelog
* Sat Feb 22 2025 Anton Midyukov <antohami@altlinux.org> 47.3-alt3
- remove incorrect icon for synaptic

* Mon Jan 27 2025 Anton Midyukov <antohami@altlinux.org> 47.3-alt2
- cleanup from meson.build files

* Mon Jan 27 2025 Anton Midyukov <antohami@altlinux.org> 47.3-alt1
- Initial build
