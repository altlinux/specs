%define _unpackaged_files_terminate_build 1

Name: kde5-plasma-theme-arc
Version: 20220908
Release: alt1
Summary: Arc KDE customization
License: GPLv3
Group: Graphical desktop/KDE
Url: https://github.com/PapirusDevelopmentTeam/arc-kde
Source: %name-%version.tar
Patch1: alt-fix-install-dir.patch

BuildArch: noarch

%description
Arc KDE - This is a port of the popular GTK theme Arc
for Plasma 5 desktop with a few additions and extras.

%prep
%setup
%patch1 -p1

%install
%makeinstall_std

%files
%_datadir/kf5/Kvantum/Arc
%_datadir/kf5/Kvantum/ArcDark
%_datadir/kf5/Kvantum/ArcDarker
%_datadir/kf5/aurorae/themes/Arc
%_datadir/kf5/aurorae/themes/Arc-Dark
%_datadir/kf5/color-schemes/Arc.colors
%_datadir/kf5/color-schemes/ArcDark.colors
%_datadir/kf5/konsole/Arc.colorscheme
%_datadir/kf5/konsole/ArcDark.colorscheme
%_datadir/kf5/konversation/themes/papirus
%_datadir/kf5/konversation/themes/papirus-dark
%_datadir/kf5/plasma/desktoptheme/Arc-Color
%_datadir/kf5/plasma/desktoptheme/Arc-Dark
%_datadir/kf5/plasma/look-and-feel/com.github.varlesh.arc-dark
%_datadir/kf5/wallpapers/Arc
%_datadir/kf5/wallpapers/Arc-Dark
%_datadir/kf5/wallpapers/Arc-Mountains
%_datadir/kf5/yakuake/skins/arc
%_datadir/kf5/yakuake/skins/arc-dark
%_datadir/kf5/plasma/look-and-feel/com.github.varlesh.arc
%_datadir/kf5/plasma/look-and-feel/com.github.varlesh.arc-darker
%doc LICENSE AUTHORS

%changelog
* Sat Oct 01 2022 Alexander Makeenkov <amakeenk@altlinux.org> 20220908-alt1
- Updated to version 20220908

* Thu Feb 06 2020 Alexander Makeenkov <amakeenk@altlinux.org> 20180614-alt4
- Fix installation directory

* Thu Feb 06 2020 Alexander Makeenkov <amakeenk@altlinux.org> 20180614-alt3
- Renamed package to kde5-plasma-theme-arc

* Tue Feb 04 2020 Alexander Makeenkov <amakeenk@altlinux.org> 20180614-alt2
- Update from upstream git 04873ca

* Wed Dec 18 2019 Alexander Makeenkov <amakeenk@altlinux.org> 20180614-alt1
- Initial build for ALT
