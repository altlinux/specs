%define _unpackaged_files_terminate_build 1

Name: plasma5-theme-arc
Version: 20180614
Release: alt1
Summary: Arc KDE customization
License: GPLv3
Group: Graphical desktop/KDE
Url: https://github.com/PapirusDevelopmentTeam/arc-kde
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch

%description
Arc KDE - This is a port of the popular GTK theme Arc
for Plasma 5 desktop with a few additions and extras.

%prep
%setup

%install
%makeinstall_std

%files
%_datadir/Kvantum/Arc
%_datadir/Kvantum/ArcDark
%_datadir/Kvantum/ArcDarker
%_datadir/aurorae/themes/Arc
%_datadir/aurorae/themes/Arc-Dark
%_datadir/color-schemes/Arc.colors
%_datadir/color-schemes/ArcDark.colors
%_datadir/konsole/Arc.colorscheme
%_datadir/konsole/ArcDark.colorscheme
%_datadir/konversation/themes/papirus
%_datadir/konversation/themes/papirus-dark
%_datadir/plasma/desktoptheme/Arc-Color
%_datadir/plasma/desktoptheme/Arc-Dark
%_datadir/plasma/look-and-feel/com.github.varlesh.arc-dark
%_datadir/wallpapers/Arc
%_datadir/wallpapers/Arc-Dark
%_datadir/yakuake/skins/arc
%_datadir/yakuake/skins/arc-dark
%doc LICENSE AUTHORS

%changelog
* Wed Dec 18 2019 Alexander Makeenkov <amakeenk@altlinux.org> 20180614-alt1
- Initial build for ALT
