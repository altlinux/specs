
Name: x-cursor-themes-Crystalcursors
Version: 0.9
Release: alt1

Summary: X cursors theme with the crystal style
License: LGPL
Group: System/X11
Url: http://digilander.libero.it/m4rt/html/crystalcursors.html

Packager: Konstantin Baev <kipruss@altlinux.org>

Source0: Crystalcursors.tar
Source1: crystalblue.tar
Source2: crystalgray.tar
Source3: crystalgreen.tar
Source4: crystalwhite.tar

BuildArch: noarch

%description
Cursor theme for Xorg

%prep
%setup -q -n Crystalcursors
tar xf %SOURCE1
tar xf %SOURCE2
tar xf %SOURCE3
tar xf %SOURCE4

find -type f -exec chmod a-x {} \;

%install
mkdir -p %buildroot/%_iconsdir/crystalblue/
mkdir -p %buildroot/%_iconsdir/crystalgray/
mkdir -p %buildroot/%_iconsdir/crystalgreen/
mkdir -p %buildroot/%_iconsdir/crystalwhite/
cp -ar crystalblue %buildroot/%_iconsdir/
cp -ar crystalgray %buildroot/%_iconsdir/
cp -ar crystalgreen %buildroot/%_iconsdir/
cp -ar crystalwhite %buildroot/%_iconsdir/

%files
%_iconsdir/crystalblue
%_iconsdir/crystalgray
%_iconsdir/crystalgreen
%_iconsdir/crystalwhite
%doc CHANGELOG CREDITS LICENSE README

%changelog
* Thu Aug 21 2008 Konstantin Baev <kipruss@altlinux.org> 0.9-alt1
- initial build for Sisyphus

