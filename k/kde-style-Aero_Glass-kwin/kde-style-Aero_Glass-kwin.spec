%define 	content_id	39007
%define 	theme Aero_Glass

Name: 		kde-style-%theme-kwin
Version:	1.0 
Release:	alt2
Packager:  	Eugene A. Suchkov <cityhawk@altlinux.ru>

Summary: 	%theme Window Decorations
Group: 		Graphical desktop/KDE
Url: 		http://www.kde-look.org/content/show.php?content=%content_id
License: 	LGPL
Requires:	dekorator

BuildArch: 	noarch

Source0: %content_id-%theme-theme.tar.gz

%description
%theme for deKorator
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

* Tue May 22 2006 Eugene Suchkov <cityhawk@altlinux.ru> 1.0-alt1
- Packaged for sisyphus 

