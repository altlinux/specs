%define theme nuvola

Name: kde-icon-theme-%theme
Version: 1.0
Release: alt2

Summary: A set of Icons for KDE
Group: Graphical desktop/KDE
Url: http://www.icon-king.com/
#Url: http://www.kde-look.org/usermanager/search.php?username=dave
License: LGPL

BuildArch: noarch

Provides: kde-icon-theme
Provides: icons-%theme = %version-%release
Obsoletes: icons-%theme

Source: %theme-%{version}.tar.bz2

%description
An icon theme is a set of icons that share a common look and feel. The
user can then select the icon theme that they want to use, and all apps
use icons from the theme. The initial user of icon themes is the icon
field of the desktop file specification, but in the future it can have
other uses (such as mimetype icons).

%prep
%setup -qn %theme
#rm -rf extras kdm ???x???
find -type f -exec chmod a-x {} \;
#
#mv index.desktop index.theme
subst "s/Inherits=.*/Inherits=default.kde,hicolor/" index.theme
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

%build
for m in "amarok.*"
do
    find -type f -name $m | \
    while read f
    do
	rm -f $f
    done
done

%install
mkdir -p %buildroot/%_iconsdir/%theme/
cp -ar * %buildroot/%_iconsdir/%theme/


%files
%doc readme*  author thanks.to
#
%dir %_iconsdir/%theme
%_iconsdir/%theme/index.*
%_iconsdir/%theme/??x??
%_iconsdir/%theme/???x???

%changelog
* Thu Apr 05 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt2
- package 128x128 icons
- remove amarok icon
- move docs to %_docdir

* Tue Nov 30 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt1
- 1.0 release

* Tue Jun 22 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt0.1.beta
- new version

* Thu Aug 28 2003 Sergey V Turchin <zerg at altlinux dot org> 0.2.5-alt1
- initial spec

