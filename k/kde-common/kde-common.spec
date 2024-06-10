Name: kde-common
Version: 24.1
Release: alt1

Summary: The basic files for KDE
License: GPL-3.0-or-later
Group: System/Base

BuildArch: noarch

Requires: kf6-filesystem
#Requires: kde-filesystem

Source1: kdeglobals

BuildRequires: rpm-build-xdg

%description
%{summary}.

%install
# configs
mkdir -p %buildroot/%_xdgconfigdir/
install -m 0644 %SOURCE1 %buildroot/%_xdgconfigdir/

%files
%config(noreplace) %_xdgconfigdir/kdeglobals

%changelog
* Thu Jun 06 2024 Sergey V Turchin <zerg@altlinux.org> 24.1-alt1
- redesign for KDE6

* Wed May 15 2024 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build

* Fri Jan 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Mon Aug 31 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- bump version

* Wed Apr 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.0-alt1
- bump version

* Mon Jan 26 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.1-alt1
- new version

* Fri Dec 26 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- rebuilt with new kde-common-devel (ALT#30602)

* Mon Aug 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Thu Apr 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Tue Feb 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- add compatibility directory

* Thu Jan 30 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.0-alt1
- new version

* Tue Sep 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.0-alt1
- new version

* Mon Feb 25 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt2
- add env directory for KDE4

* Fri Dec 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt1
- bump version

* Mon Sep 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.0-alt1
- bump version

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- build for M60P

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
