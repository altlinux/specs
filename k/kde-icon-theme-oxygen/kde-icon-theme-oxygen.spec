%define theme OxygenKDE3
%define srcname oxygen

Name: kde-icon-theme-%srcname
Version: 0.1
Release: alt2

Summary: Oxygen Icon Theme for KDE3
License: LGPL
Group: Graphical desktop/KDE
Url: http://www.kde-look.org/content/show.php/Oxygen+Icon+Theme+for+KDE3?content=79046

Packager: Konstantin Baev <kipruss@altlinux.org>

Source: %srcname.tar

BuildArch: noarch

%description
This is the Oxygen Icon theme made for KDE4 by the Oxygen Team modified to work with KDE3, simply install it like any other KDE3 theme (restarting KDE is recommended to correct certain icons from not changing), I made this theme so that KDE4 and KDE3 applications don't look so odd next to each other, but you can just use it as a normal Icon Theme if you want. Thank You :-)

Remember the Oxygen Icon Theme is still incomplete so there may be a few missing icons (they will be replaced by the crystalsvg ones of course)

%prep
%setup -q -n %srcname

find -type f -exec chmod a-x {} \;

%install
mkdir -p %buildroot/%_iconsdir/%theme/
cp -ar [^AC]* %buildroot/%_iconsdir/%theme/

%files
%doc AUTHORS COPYING
%_iconsdir/%theme

%changelog
* Fri Aug 15 2008 Konstantin Baev <kipruss@altlinux.org> 0.1-alt2
- directories .svn deleted

* Tue Aug 12 2008 Konstantin Baev <kipruss@altlinux.org> 0.1-alt1
- initial build for Sisyphus
