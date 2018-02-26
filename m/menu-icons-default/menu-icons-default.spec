Name: menu-icons-default
Version: 0.2.0.12
Release: alt1

Group: Graphical desktop/Other
Summary: Icons for Menu system
License: GPL
URL: http://www.linux-mandrake.com
BuildArch: noarch

Requires: icon-theme-hicolor
Provides: menu-icons = %version-%release
Obsoletes: menu-icons-xpm, menu-icons-png, menu-icons-crystalmdk

# mandriva icons
Source1: menu-icons.tar
# viy low quality icons
Source0: menu-icons-extra.tar
Source2: oxygen.tar
Source3: scripts.tar

BuildRequires: ImageMagick

%description
Icons for menu system in png format from Mandrake Linux,
KDE Oxygen theme and specially made for ALTLinux.

%prep
%setup -c -a2 -a3

%install
mkdir -p %buildroot/%_iconsdir/hicolor/{16x16,22x22,32x32,36x36,48x48,64x64,scalable}/apps

# default mdk icons
pushd %buildroot/%_iconsdir/hicolor
    tar xf %SOURCE1
popd

# extra png icons
for f in 48x48/apps/*.png; do
	i=`basename $f`
	[ -e 32x32/apps/$i ] && install -m644 32x32/apps/$i %buildroot%_niconsdir/$i || convert -resize 32x32 $f %buildroot%_niconsdir/$i
	[ -e 16x16/apps/$i ] && install -m644 16x16/apps/$i %buildroot%_miconsdir/$i ||	convert -resize 16x16 $f %buildroot%_miconsdir/$i
	install -m644 $f %buildroot%_liconsdir/$i
	j=`echo $i | sed -e 's,.png$,,'`
	[ -e scalable/apps/$j.svg ] && install -m644 scalable/apps/$j.svg %buildroot%_iconsdir/hicolor/scalable/apps/$j.svg
done
install -m644 64x64/apps/*.png %buildroot%_iconsdir/hicolor/64x64/apps/

# map filtered oxygen icons
./scripts/map_oxygen.sh

%files
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/scalable/apps/*

%changelog
* Sun May 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0.12-alt1
- added enlightenment section

* Sat Apr 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0.11-alt1
- more icons from KDE oxygen theme

* Fri Apr 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0.10-alt1
- added utility and system pixmaps from KDE oxygen theme

* Thu Apr 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0.9-alt1
- added 2d_graphics_section

* Mon Apr 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0.8-alt1
- added development pixmaps

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0.7-alt1
- renamed to engineering_section

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0.6-alt1
- more icons from KDE oxygen theme

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0.5-alt1
- added dictionary section
- bugfixes in oxygen import script

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0.4-alt1
- more icons from KDE oxygen theme

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0.3-alt1
- added icons from KDE oxygen theme

* Sun Apr 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0.2-alt1
- integrated extra icons pack v 0.0.2;
  preparations for oxygen icon pack integration

* Fri Apr 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0.1-alt1
- added extra icons pack v 0.0.1

* Wed Mar 23 2011 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt1
- update icons from MDV

* Mon Mar 21 2011 Sergey V Turchin <zerg@altlinux.org> 0.1.2-alt1
- fix filenames with '-'
- add 32x32/apps/networking_configuration_section.png

* Mon Oct 08 2007 Sergey V Turchin <zerg at altlinux dot org> 0.1.1-alt1
- add altlinux.png

* Mon Oct 01 2007 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt3
- fix symlink path to altlinux.png

* Wed Mar 17 2004 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt2
- fix provides

* Tue Mar 09 2004 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt1
- initial spec

