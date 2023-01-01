Name: gbrainy
Version: 2.4.6
Release: alt1

Summary: Brain training puzzle game
Summary(ru_RU.UTF-8): Игра-головоломка для тренировки мозга

License: GPL-2.0-or-later
Group: Games/Puzzles
Url: https://wiki.gnome.org/Apps/gbrainy

# libgtk-sharp3-devel missing from ppc64le
ExcludeArch: ppc64le

# Source-url: https://gitlab.gnome.org/GNOME/gbrainy/-/archive/%version/gbrainy-%version.tar.gz
Source: %name-%version.tar

BuildRequires: intltool
BuildRequires: librsvg-devel
BuildRequires: libgtk-sharp3-devel
BuildRequires: mono-devel
BuildRequires: yelp-tools

BuildRequires(pre): rpm-build-mono

%description
gbrainy is a puzzle game and trainer for fun and brain training.
Offers the following types of games: Logic puzzles. Games based on arithmetic
operations. Memory trainers. Gbrainy offers different levels of difficulty,
making gbrainy fun for kids, adults, and seniors. Gbrainy can also be easily
extended with new games developed by third parties.
Gbrainy is developed for GNOME and runs on GNU/Linux and various versions of
Unix.

%description -l ru_RU.UTF-8
gbrainy - игра-головоломка и тренажер для развлечения и тренировки мозга.
Предлагает следующие виды игр: Логические головоломки. Игры, основанные на
арифметических операциях. Тренажеры памяти. Gbrainy предлагает разные уровни
сложности, что делает gbrainy развлечением для детей, взрослых и пожилых людей.
Gbrainy также может быть легко дополнен новыми играми, разработанными третьими
сторонами.
Gbrainy разработан для GNOME и работает на GNU/Linux и различных версиях Unix.

%prep
%setup

%build
%autoreconf
%configure --libdir=%_monodir
%make_build

%install
%makeinstall_std

# Remove icons from the pixmaps directory according to the packaging policy.
# https://www.altlinux.org/Icon_Paths_Policy
rm -f %buildroot%_pixmapsdir/*

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README
%_bindir/%name
%_datadir/help/*/%name
%_monodir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/%name.appdata.xml
%_man6dir/gbrainy.6.*
%_gamesdatadir/%name

%changelog
* Sun Jan 01 2023 Evgeny Chuck <koi@altlinux.org> 2.4.6-alt1
- new version (2.4.6) with rpmgs script
- gbrainy.pc.in removed as extensions are no longer supported by the developer

* Fri Sep 02 2022 Evgeny Chuck <koi@altlinux.org> 2.4.5-alt1
- new version (2.4.5) with rpmgs script
- mono libraries packaged as per policy
- fixed path to development library in pkg file

* Thu Aug 11 2022 Evgeny Chuck <koi@altlinux.org> 2.4.4-alt1
- new version (2.4.4) with rpmgs script

* Tue Dec 01 2009 Ilya Shpigor <elly@altlinux.org> 1.20-alt1
- new version 1.20

* Sun Oct 25 2009 Ilya Shpigor <elly@altlinux.org> 1.12-alt1
- initial build for ALT Linux Sisyphus

* Sat Aug 22 2009 Frederik Himpe <fhimpe@mandriva.org> 1.12-1mdv2010.0
+ Revision: 419737
- update to new version 1.12

* Sun Jun 14 2009 Frederik Himpe <fhimpe@mandriva.org> 1.11-1mdv2010.0
+ Revision: 385900
- update to new version 1.11

* Sat Mar 14 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1-2mdv2009.1
+ Revision: 354880
- BuildRequires mono-addins
- Update to new version 1.1

* Fri Dec 26 2008 Frederik Himpe <fhimpe@mandriva.org> 1.01-1mdv2009.1
+ Revision: 319318
- Fix BuildRequires
- update to new version 1.01

* Wed Sep 03 2008 Funda Wang <fundawang@mandriva.org> 1.00-2mdv2009.0
+ Revision: 279411
- fix file list

* Mon Sep 01 2008 Frederik Himpe <fhimpe@mandriva.org> 1.00-1mdv2009.0
+ Revision: 278651
- Fix BuildRequires
- Update to version 1.00, adding config file to file list

* Fri Aug 22 2008 Funda Wang <fundawang@mandriva.org> 0.70-2mdv2009.0
+ Revision: 275022
- rebuild
- fix br in order to backport

* Sat Jun 21 2008 Funda Wang <fundawang@mandriva.org> 0.70-1mdv2009.0
+ Revision: 227757
- update to new version 0.70

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Apr 15 2008 Funda Wang <fundawang@mandriva.org> 0.61-1mdv2009.0
+ Revision: 193655
- BR gnome-sharp2-devel
- New version 0.61

* Sat Mar 08 2008 Funda Wang <fundawang@mandriva.org> 0.60-1mdv2008.1
+ Revision: 182089
- New version 0.60

* Sun Feb 24 2008 Funda Wang <fundawang@mandriva.org> 0.5.3-1mdv2008.1
+ Revision: 174264
- New version 0.53

* Fri Feb 08 2008 Funda Wang <fundawang@mandriva.org> 0.5.2-1mdv2008.1
+ Revision: 164029
- New version 0.52

* Sun Jan 27 2008 Funda Wang <fundawang@mandriva.org> 0.5.1-1mdv2008.1
+ Revision: 158577
- add missing file
- New version 0.51

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 21 2007 Funda Wang <fundawang@mandriva.org> 0.4.1-1mdv2008.1
+ Revision: 111010
- fix file list
- drop patch0
- New version 0.41

* Fri Nov 09 2007 Funda Wang <fundawang@mandriva.org> 3mdv2008.1-current
+ Revision: 107078
- rebuild for new lzma

* Sun Oct 28 2007 Funda Wang <fundawang@mandriva.org> 0.3-2mdv2008.1
+ Revision: 102721
- fix startup script (bug#35093)

* Fri Oct 26 2007 Funda Wang <fundawang@mandriva.org> 0.3-1mdv2008.1
+ Revision: 102284
- More BR
- add filelist
- Import gbrainy
- create gbrainy

