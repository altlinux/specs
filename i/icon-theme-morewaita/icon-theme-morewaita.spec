Name: icon-theme-morewaita
Version: 49
Release: alt2

Summary: An expanded Adwaita-styled companion icon theme with extra icons
License: GPL-3.0-or-later AND CC-BY-SA-4.0
Group: Graphical desktop/GNOME
URL: https://github.com/somepaulo/MoreWaita
VCS: https://github.com/somepaulo/MoreWaita.git

BuildArch: noarch

Source: %name-%version.tar
# See https://altlinux.space/armatik/icon-theme-alt-workstation/issues/3
Source1: %name-alt-%version.tar

Requires: icon-naming-utils

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: icon-naming-utils
BuildRequires: gtk4-update-icon-cache
BuildRequires: %_bindir/gtk-encode-symbolic-svg

%description
An expanded Adwaita-styled companion icon theme with extra icons for popular
apps to complement Gnome Shell's original icons.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
tar -xf %SOURCE1 -C %buildroot%_iconsdir/MoreWaita/

# create additional symlinks
pushd %buildroot%_iconsdir/MoreWaita/scalable/legacy
ln -s applications-system.svg preferences.svg
ln -s preferences-desktop.svg preferences-desktop-default-applications.svg
popd

%files
%_iconsdir/MoreWaita/
%doc AUTHORS LICENSE README.md
%exclude %_iconsdir/MoreWaita/AUTHORS
%exclude %_iconsdir/MoreWaita/LICENSE

%changelog
* Mon Apr 20 2026 Anton Midyukov <antohami@altlinux.org> 49-alt2
- Add preferences.svg, preferences-desktop.svg.

* Sat Dec 13 2025 Anton Midyukov <antohami@altlinux.org> 49-alt1
- New version 49.

* Fri Jul 11 2025 Anton Midyukov <antohami@altlinux.org> 48.3.1-alt1
- New version 48.3.1.

* Wed Jul 02 2025 Anton Midyukov <antohami@altlinux.org> 48.3-alt1
- New version 48.3.

* Sat Jun 07 2025 Anton Midyukov <antohami@altlinux.org> 48.2-alt2
- altlinux: add icon alterator

* Tue Jun 03 2025 Anton Midyukov <antohami@altlinux.org> 48.2-alt1
- New version 48.2.
- Add altlinux specyphic icons.

* Sun Mar 23 2025 Anton Midyukov <antohami@altlinux.org> 48.1-alt1
- New version 48.1.

* Mon Mar 10 2025 Anton Midyukov <antohami@altlinux.org> 47.4-alt1
- New version 47.4.

* Sat Feb 22 2025 Anton Midyukov <antohami@altlinux.org> 47.3-alt3
- remove incorrect icon for synaptic

* Mon Jan 27 2025 Anton Midyukov <antohami@altlinux.org> 47.3-alt2
- cleanup from meson.build files

* Mon Jan 27 2025 Anton Midyukov <antohami@altlinux.org> 47.3-alt1
- Initial build
