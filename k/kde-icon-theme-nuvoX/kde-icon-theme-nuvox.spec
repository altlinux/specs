%define theme nuvoX

Name: kde-icon-theme-%theme
Version: 0.3 
Release: alt2
Packager:     Eugene A. Suchkov <cityhawk@altlinux.ru>

Summary: A set of Icons for KDE
Group: Graphical desktop/KDE
Url: http://xavier.corredor.llano.googlepages.com/nuvox 
License: GPL

BuildArch: noarch

Provides: kde-icon-theme
Provides: icons-%theme = %version-%release
Obsoletes: icons-%theme

Source: nuvoX_%version.tar.bz2

%description
this theme is mainly based on three other themes:nuovola, nuoveXT, OS-L, (some icons of other theme) and of course Plus own designs.

%install
mkdir -p %buildroot/%_iconsdir
pushd %buildroot/%_iconsdir/
    tar jxf %SOURCE0
    mv nuvoX_%version %theme
    pushd %theme
	find -type f -exec chmod a-x {} \;
	#
	mv index.desktop index.theme
	subst "s/Inherits=.*/Inherits=hicolor,default.kde/" index.theme
	subst "s/\[KDE Icon Theme\]/[Icon Theme]/" index.theme
	#
	find ./ -type l -exec rm -f {} \;
	#
	find ./ -type f -name go.png| \
	while read n
	do
    	    n=`dirname $n`
    	    ln -s go.png $n/kmenu.png ||:
	done
    popd
popd

%files
%dir %_iconsdir/%theme
%_iconsdir/%theme/


%changelog
* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 0.3-alt2
- Removed set_strip_method macro

* Wed May 31 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.3-alt1
- Inital build 

