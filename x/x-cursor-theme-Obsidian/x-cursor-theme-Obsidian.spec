%define theme Obsidian

Name: x-cursor-theme-%theme
Version: 1.0
Release: alt1

Summary: Cursor theme for Xorg
License: GPL
Group: System/X11
Url: http://kde-look.org/content/show.php/Obsidian+Cursors?content=73135

Packager: Konstantin Baev <kipruss@altlinux.org>

Source: %theme.tar

BuildArch: noarch

%description
Obsidian Cursors is a shiny and clean cursor set created in Inkscape
based upon my previous Polar Cursor Theme

%prep
%setup -q -n %theme

find -type f -exec chmod a-x {} \;

%install
mkdir -p %buildroot/%_iconsdir/%theme/
cp -ar * %buildroot/%_iconsdir/%theme/

%files
%_iconsdir/%theme

%changelog
* Mon Aug 18 2008 Konstantin Baev <kipruss@altlinux.org> 1.0-alt1
- initial build for Sisyphus

