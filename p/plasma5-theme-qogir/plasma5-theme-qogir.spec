Name: plasma5-theme-qogir
Version: 20190506
Release: alt1.giteae6302
Summary: Qogir KDE theme

Group: Graphical desktop/KDE
License: GPL3
Url: https://github.com/vinceliuice/Qogir-kde

Source: %name-%version.tar.gz

BuildArch: noarch
Packager: Leontiy Volodin <lvol@altlinux.org>

# look-and-feel loses icons if applied this theme
Requires: Kvantum icon-theme-qogir

%description
Qogir kde is a flat Design theme for KDE Plasma desktop.

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/aurorae/themes
cp -a ./aurorae/themes/* %buildroot%_datadir/aurorae/themes
mkdir -p %buildroot%_datadir/color-schemes
cp -a ./color-schemes/* %buildroot%_datadir/color-schemes
mkdir -p %buildroot%_datadir/plasma/desktoptheme
cp -a ./plasma/desktoptheme/* %buildroot%_datadir/plasma/desktoptheme
mkdir -p %buildroot%_datadir/plasma/look-and-feel
cp -a ./plasma/look-and-feel/* %buildroot%_datadir/plasma/look-and-feel
mkdir -p %buildroot%_datadir/Kvantum
cp -a ./Kvantum/* %buildroot%_datadir/Kvantum

%files
%doc AUTHORS LICENSE README.md
%_datadir/aurorae/themes/Qogir*
%_datadir/color-schemes/Qogir*.colors
%_datadir/plasma/desktoptheme/Qogir*
%_datadir/plasma/look-and-feel/com.github.vinceliuice.Qogir*
%_datadir/Kvantum/Qogir*

%changelog
* Mon May 06 2019 Leontiy Volodin <lvol@altlinux.org> 20190506-alt1.giteae6302
- Updated from git (commit: eae6302)
- Fixed %%description

* Mon Apr 15 2019 Leontiy Volodin <lvol@altlinux.org> 20190404-alt2.git3bd657a
- Fixed error with applying theme without icons

* Mon Apr 15 2019 Leontiy Volodin <lvol@altlinux.org> 20190404-alt1.git3bd657a
- Initial build for ALT Sysiphus

