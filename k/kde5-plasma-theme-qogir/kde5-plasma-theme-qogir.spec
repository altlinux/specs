%filter_from_requires /sudo/d
%filter_from_requires /sed/d

Name: kde5-plasma-theme-qogir
Version: 2023.01.30
Release: alt1.git5f80b0a
Summary: Qogir KDE theme

Group: Graphical desktop/KDE
License: GPL-3.0
Url: https://github.com/vinceliuice/Qogir-kde

Source: %name-%version.tar.gz
Patch: 0001-Disable-root-check.patch

BuildArch: noarch

Provides: plasma5-theme-qogir
Obsoletes: plasma5-theme-qogir

# look-and-feel loses icons if applied this theme
Requires: Kvantum icon-theme-qogir

%description
Qogir kde is a flat Design theme for KDE Plasma desktop.

%prep
%setup -n %name-buildroot
%patch -p1

# remove dpkg from requires
rm -f plasma/plasmoids/org.kde.plasma.win7showdesktop/translate/plasmoidlocaletest

%build
%install
mkdir -p %buildroot%_datadir/Kvantum
mkdir -p %buildroot%_datadir/sddm/themes/Qogir
mkdir -p %buildroot%_datadir/kf5/sddm/themes/Qogir
mkdir -p %buildroot%_datadir/kf5/plasma/plasmoids

subst 's|$HOME/.local/share/|%buildroot%_datadir/kf5/|; s|$HOME/.config/|%buildroot%_datadir/kf5/|' install.sh
./install.sh
subst 's|/usr/share/sddm/themes|%buildroot%_datadir/sddm/themes|' sddm/install.sh
./sddm/install.sh

mv -f %buildroot%_datadir/kf5/Kvantum/* %buildroot%_datadir/Kvantum/

%files
%doc AUTHORS LICENSE README.md
%_datadir/kf5/aurorae/themes/Qogir*
%_datadir/kf5/color-schemes/Qogir*.colors
%_datadir/kf5/plasma/desktoptheme/Qogir*
%_datadir/kf5/plasma/look-and-feel/com.github.vinceliuice.Qogir*
%_datadir/kf5/plasma/layout-templates/*
%_datadir/kf5/plasma/plasmoids/*
%_datadir/Kvantum/Qogir*
%_datadir/sddm/themes/Qogir*
%_datadir/kf5/wallpapers/Qogir*

%changelog
* Mon Mar 27 2023 Leontiy Volodin <lvol@altlinux.org> 2023.01.30-alt1.git5f80b0a
- Updated from git (commit: 5f80b0a).

* Fri Jul 15 2022 Leontiy Volodin <lvol@altlinux.org> 2022.07.08-alt1.gitf240eae
- Updated from git (commit: f240eae).

* Tue Aug 24 2021 Leontiy Volodin <lvol@altlinux.org> 2021.08.16-alt1.git421a2a6
- Updated from git (commit: 421a2a6).
- Obsoleted plasma5-theme-qogir package.

