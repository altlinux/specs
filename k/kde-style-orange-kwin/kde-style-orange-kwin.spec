%define 	content_id	40562
%define 	theme orange

Name: 		kde-style-%theme-kwin
Version:	1.0 
Release:	alt2

Summary: 	Port of a FVWM theme  
Group: 		Graphical desktop/KDE
Url: 		http://www.kde-look.org/content/show.php?content=40562
License: 	GPL
Requires:	dekorator

BuildArch: 	noarch

Source0: %content_id-%theme-theme.tar.gz

%description
Port of a FVWM theme by stonecrest 
to deKorator with some additional buttons...

%prep
%setup -n %theme-theme

%install
mkdir -p %buildroot/%_datadir/apps/deKorator/themes/%theme-theme
cp -r * %buildroot/%_datadir/apps/deKorator/themes/%theme-theme
find %buildroot/%_datadir/apps/deKorator/themes/%theme-theme -type f | xargs chmod 644 

%files
%_datadir/apps/deKorator/themes

%changelog
* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 1.0-alt2
- removed set_strip_method macro

* Fri Jan 26 2007 Eugene V. Horohorin <genix@altlinux.ru> 1.0-alt1
- initial build

