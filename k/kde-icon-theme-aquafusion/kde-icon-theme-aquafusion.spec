%define theme aquafusion

Name: kde-icon-theme-%theme
Version: 0.5.0
Release: alt1

Summary: A set of Icons for KDE
License: Free for non-commercial use
Group: Graphical desktop/KDE
Url: http://aquafusion.flauta-net.de

BuildArch: noarch

Provides: kde-icon-theme
Conflicts: kdeartwork-extra <= 3.1.0-alt2

Source: AquaFusion-%version.tar.bz2
Source1: kdegnomify-icons

%description
An icon theme is a set of icons that share a common look and feel. The
user can then select the icon theme that they want to use, and all apps
use icons from the theme. The initial user of icon themes is the icon
field of the desktop file specification, but in the future it can have
other uses (such as mimetype icons).

%install
mkdir -p %buildroot/%_iconsdir
pushd %buildroot/%_iconsdir/
    tar -jxf %SOURCE0
popd


%SOURCE1

%files
%doc %_iconsdir/%theme/CHANGELOG
%doc %_iconsdir/%theme/FAQ
%doc %_iconsdir/%theme/LICENSE
%doc %_iconsdir/%theme/README
#
%dir %_iconsdir/%theme
%_iconsdir/%theme/index.*
%_iconsdir/%theme/??x??

%changelog
* Tue Jan 28 2003 Sergey V Turchin <zerg@altlinux.ru> 0.5.0-alt1
- build from BlueSphere spec
