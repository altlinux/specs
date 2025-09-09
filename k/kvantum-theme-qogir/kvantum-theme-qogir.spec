%filter_from_requires /sudo/d
%filter_from_requires /sed/d

Name: kvantum-theme-qogir
Version: 2024.12.20
Release: alt1
Summary: Qogir KDE theme

Group: Graphical desktop/KDE
License: GPL-3.0
Url: https://github.com/vinceliuice/Qogir-kde
VCS: https://github.com/vinceliuice/Qogir-kde

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: %name-alt-disable-root-check.patch

BuildArch: noarch

Provides: plasma5-theme-qogir
Provides: kde5-plasma-theme-qogir
Obsoletes: plasma5-theme-qogir
Obsoletes: kde5-plasma-theme-qogir

# look-and-feel loses icons if applied this theme
Requires: Kvantum icon-theme-qogir

%description
Qogir kde is a flat Design theme for KDE Plasma desktop.

%prep
%setup -n %name-buildroot
%patch0 -p1
%patch1 -p1
sed -e 's|$HOME/.local/share/|install/|; s|$HOME/.config/|install/|;' \
    -i install.sh
sed -i 's|/usr/share/sddm/themes|%buildroot%_datadir/sddm/themes|' sddm/install.sh
# remove dpkg from requires
rm -f plasma/plasmoids/org.kde.plasma.win7showdesktop/translate/plasmoidlocaletest

%install
mkdir -p %buildroot%_datadir/Kvantum
mkdir -p %buildroot%_datadir/sddm/themes
mkdir -p %buildroot%_datadir/plasma/plasmoids

./install.sh
cp -a install/* %buildroot%_datadir
./sddm/install.sh

%files
%doc AUTHORS LICENSE README.md
%_datadir/Kvantum/Qogir*
%_datadir/aurorae/themes/Qogir*
%_datadir/color-schemes/Qogir*.colors
%_datadir/plasma/desktoptheme/Qogir*
%_datadir/plasma/look-and-feel/com.github.vinceliuice.Qogir*
%_datadir/plasma/layout-templates/*
%_datadir/plasma/plasmoids/*
%_datadir/wallpapers/Qogir*
%_datadir/sddm/themes/Qogir*

%changelog
* Tue Sep 09 2025 Leontiy Volodin <lvol@altlinux.org> 2024.12.20-alt1
- New version 2024.12.20.
- Renamed: kde5-plasma-theme-qogir -> kvantum-theme-qogir.
- Added VCS tag.

* Sat Feb 24 2024 Leontiy Volodin <lvol@altlinux.org> 2024.02.03-alt1.git6e61df9
- Updated from git (commit: 6e61df9).

* Mon Mar 27 2023 Leontiy Volodin <lvol@altlinux.org> 2023.01.30-alt1.git5f80b0a
- Updated from git (commit: 5f80b0a).

* Fri Jul 15 2022 Leontiy Volodin <lvol@altlinux.org> 2022.07.08-alt1.gitf240eae
- Updated from git (commit: f240eae).

* Tue Aug 24 2021 Leontiy Volodin <lvol@altlinux.org> 2021.08.16-alt1.git421a2a6
- Updated from git (commit: 421a2a6).
- Obsoleted plasma5-theme-qogir package.

