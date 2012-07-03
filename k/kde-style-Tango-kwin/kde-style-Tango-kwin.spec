%define 	content_id	37010
%define 	theme Tango

Name: 		kde-style-%theme-kwin
Version:	1.0 
Release:	alt2
Packager:  	Eugene A. Suchkov <cityhawk@altlinux.ru>

Summary: 	Port from the Metacity theme Tango	
Group: 		Graphical desktop/KDE
Url: 		http://www.opentux.com.ar/lordcrow/packs/kneu.html 
License: 	LGPL
Requires:	dekorator

BuildArch: 	noarch

Source0: %content_id-%theme-theme.tar.gz

%description
Port from the Metacity theme Tango for deKorator
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

* Mon May 22 2006 Eugene Suchkov <cityhawk@altlinux.ru> 1.0-alt1
- Packaged for sisyphus 

