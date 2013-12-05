%define icons_name SimpleSchool

Name: icon-theme-simple-school
Version: 2.1
Release: alt4

Summary: Additonal sets of icons for the GNOME and Xfce (School edition)
Summary(ru_RU.UTF-8): Набор значков Simple для GNOME и Xfce (редакция для школьных дистрибутивов)
License: GPL
URL: http://www.gnome-look.org/content/show.php/Simple?content=99470

Group: Graphical desktop/GNOME
Source0: SimpleSchool-%{version}.tar
Source1: actions-%{version}.tar
BuildArch: noarch

Conflicts: icon-theme-simple
Conflicts: icon-theme-simple-sl

%description
Sets of icons for GNOME and XFCE based on original icons - OxygenRefit2.

%description -l ru_RU.UTF-8
Набор пиктограмм Simple для среды GNOME и XFCE основанный на оригинальном наборе
пиктограмм OxygenRefit2. Разрабатывается в рамках проекта Simplicity и лучше всего
сочетается с темой gtk2-theme-simplicity.

%install
install -m755 -d %buildroot%_iconsdir
tar xf %SOURCE0 -C %buildroot%_iconsdir/
tar xf %SOURCE1 -C %buildroot%_iconsdir/
mv -f %buildroot%_iconsdir/actions-%{version}/* %buildroot%_iconsdir/%icons_name-%{version}/scalable/actions/
rm -rf %buildroot%_iconsdir/actions-%{version}
mv %buildroot%_iconsdir/%icons_name-%{version} %buildroot%_iconsdir/%icons_name
ln -s %_iconsdir/%icons_name/scalable/apps/clock.png %buildroot%_iconsdir/%icons_name/scalable/apps/xfce4-clock.png

%files
%_iconsdir/%icons_name

%changelog
* Thu Dec 05 2013 Andrey Cherepanov <cas@altlinux.org> 2.1-alt4
- New icon theme for school distributions
- Set P7 logo as menu and LightDM icon
- Forked from icon-theme-simple.
