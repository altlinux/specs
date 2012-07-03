%define theme noia

Name: kde-icon-theme-%theme
Version: 1.00
Release: alt1

Summary: A set of Icons for KDE
License: LGPL
Group: Graphical desktop/KDE
Url: http://www.carlitus.net

BuildArch: noarch

Provides: kde-icon-theme

Source: noia-kde-icons-%version.tar.bz2
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
    mv noia_kde_* %theme
popd

%SOURCE1

find %buildroot/%_iconsdir/ -type f -exec chmod a-x {} \;

%files
%doc %_iconsdir/%theme/changelog
%doc %_iconsdir/%theme/readme
#
%dir %_iconsdir/%theme
%_iconsdir/%theme/index.*
%_iconsdir/%theme/??x??

%changelog
* Fri Oct 03 2003 Sergey V Turchin <zerg at altlinux dot org> 1.00-alt1
- new version

* Tue Feb 04 2003 Sergey V Turchin <zerg@altlinux.ru> 0.95-alt1
- build from BlueSphere spec
