%define icons_name Simple

Name: icon-theme-simple
Version: 2.1
Release: alt3

Summary: Additonal sets of icons for the GNOME and Xfce
Summary(ru_RU.UTF-8): Набор пиктограмм Simple для GNOME и Xfce
License: GPL
URL: http://www.gnome-look.org/content/show.php/Simple?content=99470

Group: Graphical desktop/GNOME
Source0: Simple-%{version}.tar.bz2
Source1: actions-%{version}.tar.bz2
BuildArch: noarch

%description
Sets of icons for GNOME and XFCE based on original icons - OxygenRefit2.

%description -l ru_RU.UTF-8
Набор пиктограмм Simple для среды GNOME и XFCE основанный на оригинальном наборе
пиктограмм OxygenRefit2. Разрабатывается в рамках проекта Simplicity и лучше всего
сочетается с темой gtk2-theme-simplicity.

%install
install -m755 -d %buildroot%_iconsdir
tar xjf %SOURCE0 -C %buildroot%_iconsdir/
tar xjf %SOURCE1 -C %buildroot%_iconsdir/
mv -f %buildroot%_iconsdir/actions-%{version}/* %buildroot%_iconsdir/%icons_name-%{version}/scalable/actions/
rm -rf %buildroot%_iconsdir/actions-%{version}
mv %buildroot%_iconsdir/%icons_name-%{version} %buildroot%_iconsdir/%icons_name
ln -s %_iconsdir/%icons_name/scalable/apps/clock.png %buildroot%_iconsdir/%icons_name/scalable/apps/xfce4-clock.png

%files
%_iconsdir/%icons_name

%changelog
* Tue May 24 2011 Mikhail Efremov <sem@altlinux.org> 2.1-alt3
- Symlink xfce4-clock to clock icon.
- Minor spec cleanup.

* Fri Jan 22 2010 Denis Koryavov <dkoryavov@altlinux.org> 2.1-alt2
- Fixed bug with Parole media player (changed 4 icon). 

* Fri Jan 15 2010 Denis Koryavov <dkoryavov@altlinux.org> 2.1-alt1
- Update to version 2.1.

* Sun Oct 11 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.95-alt1
- First build for Sisyphus.

