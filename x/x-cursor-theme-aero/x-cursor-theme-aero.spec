%define theme aero

Name: x-cursor-theme-%theme
Version: 20080112
Release: alt1

Summary: Cursor theme for Xorg
License: GPL
Group: System/X11
Url: http://kde-look.org/content/show.php/Aero+Mouse+Cursors+with+Drop+Shadow?content=67833

Packager: Konstantin Baev <kipruss@altlinux.org>

Source: %theme.tar

BuildArch: noarch

%description
Cursor theme for Xorg

%prep
%setup -q -n %theme

find -type f -exec chmod a-x {} \;

%install
mkdir -p %buildroot/%_iconsdir/%theme/
cp -ar * %buildroot/%_iconsdir/%theme/

%files
%_iconsdir/%theme

%changelog
* Mon Aug 18 2008 Konstantin Baev <kipruss@altlinux.org> 20080112-alt1
- initial build for Sisyphus

