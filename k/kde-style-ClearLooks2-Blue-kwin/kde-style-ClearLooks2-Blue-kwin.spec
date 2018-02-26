%define 	content_id	34338
%define 	theme ClearLooks2-Blue

Name: 		kde-style-%theme-kwin
Version:	0.2 
Release:	alt2
Packager:  	Eugene A. Suchkov <cityhawk@altlinux.ru>

Summary: 	Port from the Metacity theme %theme
Group: 		Graphical desktop/KDE
Url: 		http://www.kde-look.org/content/show.php?content=%content_id
License: 	LGPL
Requires:	dekorator

BuildArch: 	noarch

Source0: %content_id-%theme-theme.tar.gz

%description
Port from the Metacity theme %theme for deKorator
%prep
%setup -n %theme-theme

%install
mkdir -p %buildroot/%_datadir/apps/deKorator/themes/%theme-theme
cp -r * %buildroot/%_datadir/apps/deKorator/themes/%theme-theme
find %buildroot/%_datadir/apps/deKorator/themes/%theme-theme -type f | xargs chmod 644 

%files
%_datadir/apps/deKorator/themes

%changelog
* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 0.2-alt2
- Removed set_strip_method macro

* Tue May 22 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.2-alt1
- Packaged for sisyphus 

