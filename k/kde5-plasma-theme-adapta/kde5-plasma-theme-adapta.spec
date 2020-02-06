%define _unpackaged_files_terminate_build 1

Name: kde5-plasma-theme-adapta
Version: 20180828
Release: alt4
Summary: Adapta KDE customization
License: GPLv3
Group: Graphical desktop/KDE
Url: https://github.com/PapirusDevelopmentTeam/adapta-kde
Source: %name-%version.tar
Patch1: alt-fix-install-dir.patch
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch

%description
Adapta KDE - This is a port of the popular GTK theme Adapta
for Plasma 5 desktop with a few additions and extras.

%prep
%setup
%patch1 -p1

%install
%makeinstall_std
rm -f %buildroot%_datadir/kf5/wallpapers/src/mountain.svg

%files
%_datadir/kf5/Kvantum/Adapta
%_datadir/kf5/Kvantum/AdaptaNokto
%_datadir/kf5/aurorae/themes/Adapta
%_datadir/kf5/color-schemes/Adapta.colors
%_datadir/kf5/color-schemes/AdaptaNokto.colors
%_datadir/kf5/konsole/Adapta.colorscheme
%_datadir/kf5/konsole/AdaptaNokto.colorscheme
%_datadir/kf5/plasma/desktoptheme/Adapta
%_datadir/kf5/plasma/look-and-feel/com.github.varlesh.adapta
%_datadir/kf5/wallpapers/Adapta
%_datadir/kf5/yakuake/skins/adapta-nokto
%_datadir/kf5/yakuake/skins/adapta
%doc LICENSE

%changelog
* Thu Feb 06 2020 Alexander Makeenkov <amakeenk@altlinux.org> 20180828-alt4
- Fix installation directory

* Thu Feb 06 2020 Alexander Makeenkov <amakeenk@altlinux.org> 20180828-alt3
- Renamed package to kde5-plasma-theme-adapta

* Tue Feb 04 2020 Alexander Makeenkov <amakeenk@altlinux.org> 20180828-alt2
- Update from upstream git ae539ff

* Thu Dec 19 2019 Alexander Makeenkov <amakeenk@altlinux.org> 20180828-alt1
- Initial build for ALT
