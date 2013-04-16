%define icons_name SimpleSL

Name: icon-theme-simple-sl
Version: 2.1
Release: alt4

Summary: Additonal sets of icons Simple for Simply Linux
Summary(ru_RU.UTF-8): Набор пиктограмм Simple для Simply Linux
License: GPL
URL: http://www.gnome-look.org/content/show.php/Simple?content=99470

Group: Graphical desktop/XFce
Source0: %icons_name-%version.tar
Source1: actions-%version.tar
BuildArch: noarch

%description
Sets of icons for Simply Linux based on original icons - Simple.

%description -l ru_RU.UTF-8
Набор пиктограмм для Simply Linux основанный на оригинальном наборе
пиктограмм Simple.

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
* Tue Apr 16 2013 Mikhail Efremov <sem@altlinux.org> 2.1-alt4
- Added SL logo icon as avatar-default.
- Forked from icon-theme-simple.

* Tue May 24 2011 Mikhail Efremov <sem@altlinux.org> 2.1-alt3
- Symlink xfce4-clock to clock icon.
- Minor spec cleanup.

* Fri Jan 22 2010 Denis Koryavov <dkoryavov@altlinux.org> 2.1-alt2
- Fixed bug with Parole media player (changed 4 icon).

* Fri Jan 15 2010 Denis Koryavov <dkoryavov@altlinux.org> 2.1-alt1
- Update to version 2.1.

* Sun Oct 11 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.95-alt1
- First build for Sisyphus.

