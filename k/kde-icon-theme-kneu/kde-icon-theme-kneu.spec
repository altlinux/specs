%define theme kneu

Name: kde-icon-theme-%theme
Version: 0.2 
Release: alt2
Packager:     Eugene A. Suchkov <cityhawk@altlinux.ru>

Summary: A set of Icons for KDE
Group: Graphical desktop/KDE
Url: http://www.opentux.com.ar/lordcrow/packs/kneu.html 
License: LGPL

BuildArch: noarch

Provides: kde-icon-theme
Provides: icons-%theme = %version-%release
Obsoletes: icons-%theme

Source: kNeu-alpha-%version.tar.gz

%description
kNeu is a brand new Icon Theme based entirely on Sivestre Herrera's DLG Neu Icon Set.
It intends to be some cartoonish, but not stupid. Quiet, but not silent. Shiny, but not scandalous.
When you look at your screen, this icon set intends to say: "hey. they look really nice in my KDE!"


%install
mkdir -p %buildroot/%_iconsdir
pushd %buildroot/%_iconsdir/
    tar zxf %SOURCE0
    mv kNeu-alpha-%version %theme
    pushd %theme
	find -type f -exec chmod a-x {} \;
	#
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
* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 0.2-alt2
- removed set_strip_method macro

* Fri May 05 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.2-alt1
- Inital build 

