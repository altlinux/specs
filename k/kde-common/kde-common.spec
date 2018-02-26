
%define major 4
%define minor 8
%define bugfix 3

Name: kde-common
Version: %major.%minor.%bugfix
Release: alt1

Summary: The basic directory layout for KDE
License: Public Domain
Group: System/Base

Obsoletes: kde3-common < %version-%release
Provides: kde3-common = %version-%release

BuildRequires: kde-common-devel >= 4.4.0

%description
The %name package is one of the basic KDE packages that is installed on
a %distribution system; %name contains the basic directory layout
for the K Desktop Environment, including the correct permissions for the
directories.

%install
mkdir -p %buildroot/%_sysconfdir/kde/config/kdm
mkdir -p %buildroot/%_sysconfdir/kde-profile/default
pushd %buildroot/%_sysconfdir
	mkdir -p kde/xdg/menus/applications-merged
popd
mkdir -p %buildroot/%_datadir
pushd %buildroot/%_datadir
	mkdir -p applications/kde
#
	mkdir -p doc/HTML
	for lng in %_kde_langlist; do
	mkdir -p doc/HTML/${lng}/common
	done
	mkdir -p alt/kde
	mkdir -p kde/locale/en_US
	mkdir -p kde/locale/l10n
	mkdir -p apps/profiles
	mkdir -p autostart
	mkdir -p config
	mkdir -p config.kcfg
	mkdir -p mimelnk/{all,application,audio,fonts,image,inode,interface,kdedevice,message,model,multipart,print,text,video}
	mkdir -p services/{kconfiguredialog,kded,searchproviders,useragentstrings}
	mkdir -p servicetypes
	mkdir -p templates
	mkdir -p icons/crystalsvg/{16x16,22x22,32x32,48x48,64x64,128x128,scalable}/{actions,apps,devices,filesystems,mimetypes}

	mkdir -p applnk/.hidden
	mkdir -p applnk/Applications
	mkdir -p applnk/Development
	mkdir -p applnk/Editors
	mkdir -p applnk/Edutainment/{,French}
	mkdir -p applnk/Games/{Arcade,Board,Card,Strategy,Tactic,TacticStrategy,Roguelikes}
	mkdir -p applnk/Graphics
	mkdir -p applnk/Internet/Terminal
	mkdir -p applnk/Multimedia
	mkdir -p applnk/Office
	mkdir -p applnk/Settingsmenu
	mkdir -p applnk/Settings/{Components,Databases,FileBrowsing,Help,Information,Network,Peripherals}
	mkdir -p applnk/Settings/{Personalization,PowerControl,Sound,System,WebBrowsing}
	mkdir -p applnk/Settings/LookNFeel/{Desktop,Themes,Windows}
	mkdir -p applnk/System/{ScreenSavers,Terminal}
	mkdir -p applnk/Toys
	mkdir -p applnk/Utilities
popd

mkdir -p %buildroot/%_libdir
pushd %buildroot/%_libdir
    mkdir -p kde3/plugins/styles
popd


# KDE3 new

mkdir -p %buildroot/%_K3bindir
mkdir -p %buildroot/%_K3sbindir
mkdir -p %buildroot/%_kde3_iconsdir
for lng in %_kde_langlist; do
mkdir -p %buildroot/%_K3doc/${lng}/common
done
#
mkdir -p %buildroot/%_sysconfdir/kde/xdg/menus/applications-merged
mkdir -p %buildroot/%_K3includedir
mkdir -p %buildroot/%_K3conf
mkdir -p %buildroot/%_K3cfg
mkdir -p %buildroot/%_K3libdir/kconf4_update_bin
mkdir -p %buildroot/%_K3link
mkdir -p %buildroot/%_K3lib/imports/org/kde
mkdir -p %buildroot/%_K3plug/{imageformats,phonon_platform,script,styles}
mkdir -p %buildroot/%_K3exec
mkdir -p %buildroot/%_K3start
mkdir -p %buildroot/%_K3xdg_apps
mkdir -p %buildroot/%_K3xdg_dirs
mkdir -p %buildroot/%_K3apps/kstyle/themes
mkdir -p %buildroot/%_K3emo
mkdir -p %buildroot/%_K3snd
mkdir -p %buildroot/%_K3doc/en/common
mkdir -p %buildroot/%_K3tmpl/.source
mkdir -p %buildroot/%_K3wall
#
for lng in %_kde_langlist; do
mkdir -p %buildroot/%_K3i18n/${lng}/LC_MESSAGES
mkdir -p %buildroot/%_K3i18n/${lng}/LC_SCRIPTS
done

mkdir -p %buildroot/%_K3srv
mkdir -p %buildroot/%_K3srvtyp

mkdir -p %buildroot/%_K3iconsdir/crystalsvg/{16x16,22x22,32x32,48x48,64x64,128x128,scalable}/{actions,animations,apps,categories,devices,emblems,emotes,filesystems,intl,mimetypes,places,status}/
mkdir -p %buildroot/%_K3iconsdir/crystalsvg/8x8/emblems
mkdir -p %buildroot/%_K3iconsdir/crystalsvg/scalable/{actions,animations,apps,categories,devices,emblems,emotes,filesystems,intl,mimetypes,places,status}/small/{16x16,22x22,32x32,48x48,64x64}/
mkdir -p %buildroot/%_K3iconsdir/crystalsvg/scalable/{actions,apps,categories,devices,emblems,emotes,filesystems,intl,mimetypes,places,status}/small/{16x16,22x22,32x32,48x48,64x64}/
mkdir -p %buildroot/%_K3iconsdir/crystalsvg/scalable/apps/alternativ/
mkdir -p %buildroot/%_kde3_iconsdir/hicolor/{16x16,22x22,32x32,48x48,64x64,128x128,scalable}/{actions,animations,apps,categories,devices,emblems,emotes,filesystems,intl,mimetypes,places,status}/
mkdir -p %buildroot/%_kde3_iconsdir/hicolor/scalable/{actions,animations,apps,categories,devices,emblems,emotes,filesystems,intl,mimetypes,places,status}/small/{16x16,22x22,32x32,48x48,64x64}/
mkdir -p %buildroot/%_kde3_iconsdir/hicolor/scalable/{actions,apps,categories,devices,emblems,emotes,filesystems,intl,mimetypes,places,status}/small/{16x16,22x22,32x32,48x48,64x64}/
mkdir -p %buildroot/%_kde3_iconsdir/hicolor/scalable/apps/alternativ/
mkdir -p %buildroot/%_sysconfdir/kde/custom/share/config
ln -s custom %buildroot/%_sysconfdir/kde/current
ln -s . %buildroot/%_K3datadir/share
ln -s `relative %_K3bindir %_K3datadir/bin` %buildroot/%_K3datadir/bin

pushd %buildroot/%_K3datadir
	mkdir -p applnk/.hidden
	mkdir -p applnk/Applications
	mkdir -p applnk/Development
	mkdir -p applnk/Editors
	mkdir -p applnk/Edutainment/French
	mkdir -p applnk/Games/{Arcade,Board,Card,Strategy,Tactic,TacticStrategy,Roguelikes}
	mkdir -p applnk/Graphics
	mkdir -p applnk/Internet/Terminal
	mkdir -p applnk/Multimedia
	mkdir -p applnk/Office
	mkdir -p applnk/Settingsmenu
	mkdir -p applnk/Settings/{Components,Databases,FileBrowsing,Help,Information,Network,Peripherals}
	mkdir -p applnk/Settings/{Personalization,PowerControl,Sound,System,WebBrowsing}
	mkdir -p applnk/Settings/LookNFeel/{Desktop,Themes,Windows}
	mkdir -p applnk/System/{ScreenSavers,Terminal}
	mkdir -p applnk/Toys
	mkdir -p applnk/Utilities
popd


# KDE4

mkdir -p %buildroot/%_kde4_bindir
mkdir -p %buildroot/%_kde4_sbindir
mkdir -p %buildroot/%_kde4_iconsdir
mkdir -p %buildroot/%_kde4_xdg_apps
mkdir -p %buildroot/%_kde4_xdg_dirs
for lng in %_kde_langlist; do
mkdir -p %buildroot/%_K4doc/${lng}/common
done
#
mkdir -p %buildroot/%_sysconfdir/kde4/xdg/menus/applications-merged
mkdir -p %buildroot/%_K4includedir
mkdir -p %buildroot/%_K4conf
mkdir -p %buildroot/%_K4cfg
mkdir -p %buildroot/%_K4libdir/kconf4_update_bin
mkdir -p %buildroot/%_K4link
mkdir -p %buildroot/%_K4lib/imports/org/kde
mkdir -p %buildroot/%_K4lib/platformimports/touch/org/kde/
mkdir -p %buildroot/%_K4plug/{imageformats,phonon_platform,script,styles}
mkdir -p %buildroot/%_K4exec
mkdir -p %buildroot/%_K4start
mkdir -p %buildroot/%_K4xdg_apps
mkdir -p %buildroot/%_K4xdg_dirs
mkdir -p %buildroot/%_K4apps{/kstyle/themes,/plasma/plasmoids}
mkdir -p %buildroot/%_K4emo
mkdir -p %buildroot/%_K4snd
mkdir -p %buildroot/%_K4doc/en/common
mkdir -p %buildroot/%_K4tmpl/.source
mkdir -p %buildroot/%_K4wall
#
for lng in %_kde_langlist; do
mkdir -p %buildroot/%_K4i18n/${lng}/LC_MESSAGES
mkdir -p %buildroot/%_K4i18n/${lng}/LC_SCRIPTS
done

mkdir -p %buildroot/%_K4srv
mkdir -p %buildroot/%_K4srvtyp

mkdir -p %buildroot/%_K4iconsdir/oxygen/{16x16,22x22,32x32,48x48,64x64,128x128,scalable}/{actions,animations,apps,categories,devices,emblems,emotes,filesystems,intl,mimetypes,places,status}/
mkdir -p %buildroot/%_K4iconsdir/oxygen/8x8/emblems
mkdir -p %buildroot/%_K4iconsdir/oxygen/scalable/{actions,animations,apps,categories,devices,emblems,emotes,filesystems,intl,mimetypes,places,status}/small/{16x16,22x22,32x32,48x48,64x64}/
mkdir -p %buildroot/%_K4iconsdir/oxygen/scalable/{actions,animations,apps,categories,devices,emblems,emotes,filesystems,intl,mimetypes,places,status}/hidef/
mkdir -p %buildroot/%_K4iconsdir/oxygen/scalable/{actions,apps,categories,devices,emblems,emotes,filesystems,intl,mimetypes,places,status}/small/{16x16,22x22,32x32,48x48,64x64}/
mkdir -p %buildroot/%_K4iconsdir/oxygen/scalable/{actions,apps,categories,devices,emblems,emotes,filesystems,intl,mimetypes,places,status}/hidef/
mkdir -p %buildroot/%_K4iconsdir/oxygen/scalable/apps/alternativ/
mkdir -p %buildroot/%_kde4_iconsdir/hicolor/{16x16,22x22,32x32,48x48,64x64,128x128,scalable}/{actions,animations,apps,categories,devices,emblems,emotes,filesystems,intl,mimetypes,places,status}/
mkdir -p %buildroot/%_kde4_iconsdir/hicolor/scalable/{actions,animations,apps,categories,devices,emblems,emotes,filesystems,intl,mimetypes,places,status}/small/{16x16,22x22,32x32,48x48,64x64}/
mkdir -p %buildroot/%_kde4_iconsdir/hicolor/scalable/{actions,apps,categories,devices,emblems,emotes,filesystems,intl,mimetypes,places,status}/small/{16x16,22x22,32x32,48x48,64x64}/
mkdir -p %buildroot/%_kde4_iconsdir/hicolor/scalable/apps/alternativ/
mkdir -p %buildroot/%_sysconfdir/kde4/custom/share/config
ln -s custom %buildroot/%_sysconfdir/kde4/current
ln -s . %buildroot/%_K4datadir/share
ln -s `relative %_kde4_bindir %_K4datadir/bin` %buildroot/%_K4datadir/bin
ln -s `relative %_libdir %_K4datadir/lib` %buildroot/%_K4datadir/lib


%files
%_sysconfdir/kde/
%_sysconfdir/kde-profile/
%_sysconfdir/kde4/
%_libdir/*
%_datadir/*
#
%_K3bindir
%_K3sbindir
%_K3includedir
#
%dir %_libexecdir/kde4
%_kde4_bindir
%_kde4_sbindir
%_K4includedir
%exclude %dir %_docdir
%exclude %dir %_iconsdir
%exclude %dir %_datadir/applications
%exclude %dir %_datadir/desktop-directories
%exclude %dir %_datadir/wallpapers


%changelog
* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- add share/kde4/lib

* Sun Feb 19 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Wed Jan 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Wed Aug 31 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt1
- bump version

* Fri May 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- add hidef oxygen icons subdir and LC_SCRIPTS locale subdirs

* Thu Feb 17 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt3
- add KDE3 new placement dirs

* Fri Jan 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- add qml plugins dir

* Thu Jan 27 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- bump version

* Tue Aug 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- build for M51

* Mon Apr 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- add kde3 doc common dirs

* Wed Feb 10 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- remove old macroses

* Wed Jul 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- rebuilt with kde-common-devel changes

* Tue Jul 14 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt3.M50.1
- built for M50

* Tue Jul 14 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt4
- add common html doc directories

* Tue Jul 14 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt2.M50.1
- built for M50

* Mon Jul 13 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt3
- add %%_libexecdir/kde4

* Fri Jul 10 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt2
- add %%_libexecdir/kde4/bin

* Mon Jul 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- fix to build in new environment

* Tue Jun 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt0.M50.1
- built for M50

* Mon May 18 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- update KDE4 directories

* Tue Jan 27 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt2
- fix requires

* Mon Jan 26 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- add kde_prefix/bin symlink

* Thu Dec 18 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- add kde4 plugins/script subdirectory

* Wed Jul 30 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- bump version

* Wed May 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.100-alt1
- new version

* Thu Feb 14 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt2
- rebuilt

* Wed Feb 13 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt1
- add KDE4 dirs

* Thu Oct 18 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- remove /usr/share/wallpapers

* Fri Aug 31 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- add /etc/kde-profile
- drop /var/lib/cddb

* Mon Dec 04 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- add /etc/kde/xdg/menus/applications-merged

* Mon Nov 28 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version

* Fri Jun 17 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt1
- remove ownership of /usr/share/applications

* Thu Mar 31 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt1
- new version

* Tue Jan 04 2005 ZerG <zerg@altlinux.ru> 3.3.2-alt0.0.M24
- new version

* Thu Sep 30 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.0-alt1
- new version

* Tue Jul 06 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- add %%_libdir/kde3/plugins/styles
- bump version

* Tue Jan 13 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2-alt1
- move /usr/share/icons/crystal to /usr/share/icons/crystalsvg
- remove unused dirs

* Fri Jan 31 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt3
- remove /usr/share/locale/all_languages

* Mon Oct 14 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt2
- add cddb dirs

* Wed Oct 09 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt1
- build for KDE 3.1

* Fri Aug 23 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt6
- add %_datadir/alt/kde

* Fri Apr 19 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt5
- move to /usr

* Mon Apr 08 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt4
- add some dirs

* Mon Mar 25 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt3
- add some dirs

* Mon Mar 25 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt2
- s/applnk\.kde/applnk/

* Thu Mar 21 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt1
- build for kde3

* Fri Sep 28 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0-alt0.1
- Initial revision.
