%define _unpackaged_files_terminate_build 1

Name: plasma5-theme-adapta
Version: 20180828
Release: alt1
Summary: Adapta KDE customization
License: GPLv3
Group: Graphical desktop/KDE
Url: https://github.com/PapirusDevelopmentTeam/adapta-kde
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch

%description
Adapta KDE - This is a port of the popular GTK theme Adapta
for Plasma 5 desktop with a few additions and extras.

%prep
%setup

%install
%makeinstall_std
rm -f %buildroot%_datadir/wallpapers/src/mountain.svg

%files
%_datadir/Kvantum/Adapta
%_datadir/Kvantum/AdaptaNokto
%_datadir/aurorae/themes/Adapta
%_datadir/color-schemes/Adapta.colors
%_datadir/color-schemes/AdaptaNokto.colors
%_datadir/konsole/Adapta.colorscheme
%_datadir/konsole/AdaptaNokto.colorscheme
%_datadir/plasma/desktoptheme/Adapta
%_datadir/plasma/look-and-feel/com.github.varlesh.adapta
%_datadir/wallpapers/Adapta
%_datadir/yakuake/skins/adapta-nokto
%_datadir/yakuake/skins/adapta
%doc LICENSE

%changelog
* Thu Dec 19 2019 Alexander Makeenkov <amakeenk@altlinux.org> 20180828-alt1
- Initial build for ALT
