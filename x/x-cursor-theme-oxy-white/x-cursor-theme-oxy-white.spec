%define theme oxy-white

Name: x-cursor-theme-%theme
Version: 20080912
Release: alt1

Summary: Cursor theme for Xorg
License: GPL
Group: System/X11
Url: http://www.kde-look.org/content/show.php/OxyWhite?content=89058

Packager: Evgeny V Shishkov <shev@altlinux.org>

Source: %theme.tar.gz

BuildArch: noarch

%description
Oxygen cursor theme for Xorg

%prep
%setup -q -n %theme

find -type f -exec chmod a-x {} \;

%install
mkdir -p %buildroot/%_iconsdir/%theme/
cp -ar * %buildroot/%_iconsdir/%theme/



%files
%_iconsdir/%theme

%changelog
* Fri Sep 12 2008 Evgeny V. Shishkov <shev@altlinux.org> 20080912-alt1
- initial build for Sisyphus
