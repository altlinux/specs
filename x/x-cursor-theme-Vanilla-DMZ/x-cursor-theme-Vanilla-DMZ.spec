%define theme Vanilla-DMZ

Name: x-cursor-theme-%theme
Version: 0.4
Release: alt1

Summary: Cursor theme for Xorg
License: MIT
Group: System/X11
Url: http://jimmac.musichall.cz/themes.php?skin=7

Packager: Konstantin Baev <kipruss@altlinux.org>

Source: %theme-%version.tar

BuildArch: noarch

%description
Style neutral scalable cursor theme for Xorg.

%prep
%setup -q -n %theme-%version

find -type f -exec chmod a-x {} \;

%install
mkdir -p %buildroot/%_iconsdir/%theme/
cp -ar [^C]* %buildroot/%_iconsdir/%theme/

%files
%doc COPYING
%_iconsdir/%theme

%changelog
* Mon Aug 18 2008 Konstantin Baev <kipruss@altlinux.org> 0.4-alt1
- initial build for Sisyphus

