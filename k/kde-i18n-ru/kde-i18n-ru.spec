%define lng ru
%define lngg Russian
%undefine __libtoolize

Name: kde-i18n-%lng
Version: 3.5.13
Release: alt1

Group: Graphical desktop/KDE
Summary: %lngg language support for KDE
License: GPL
Url: http://www.kde.org/

Provides: kde-i18n-lang = %version-%release
Requires: kde-common
BuildArch: noarch
Conflicts: kdevelop-i18n < %version-%release 

Source: %name-%{version}.tar.bz2
#Source: %name-3.3.0.tar.bz2
#
Source1: admin.tar.bz2
#
Source101: kde-i18n-ru-kmail-add.po
Source102: kde-i18n-ru-kdmgreet-add.po
Source104: kde-i18n-ru-kppp-add.po
Source105: kde-i18n-ru-desktop_kdebase-add.po
Source106: kde-i18n-ru-kcmkicker-add.po
Source107: kde-i18n-ru-kcmkonqhtml-add.po
Source108: kde-i18n-ru-kio_devices-add.po
Source109: kde-i18n-ru-kdesktop-add.po
Source111: kde-i18n-ru-khtmlsettingsplugin-add.po
Source112: kde-i18n-ru-kcmkio-add.po
Source113: kde-i18n-ru-ark-add.po

Patch10: kde-i18n-ru-kmail.patch

BuildRequires: kdelibs-devel xml-utils

%description
%lngg language support for KDE.


%prep
#%setup -q -n %name-%version -a1
#%setup -q -n %name-3.3.0 -a1
%setup -q -a1

find -type f -name *.gmo | while read f; do rm -f $f; done
find -type f -name index.cache.bz2 | while read f; do rm -f $f; done

#cat SOURCE50 > messages/kdewebdev/kommander.po 

cat %SOURCE101 >> messages/kdepim/kmail.po
cat %SOURCE102 >> messages/kdebase/kdmgreet.po
cat %SOURCE104 >> messages/kdenetwork/kppp.po
cat %SOURCE105 >> messages/kdebase/desktop_kdebase.po
cat %SOURCE106 >> messages/kdebase/kcmkicker.po
cat %SOURCE107 >> messages/kdebase/kcmkonqhtml.po
cat %SOURCE108 >> messages/kdebase/kio_devices.po
cat %SOURCE109 >> messages/kdebase/kdesktop.po
cat %SOURCE111 >> messages/kdeaddons/khtmlsettingsplugin.po
cat %SOURCE112 >> messages/kdebase/kcmkio.po
cat %SOURCE113 >> messages/kdeutils/ark.po

%patch10 -p1

#autoreconf -fisv


%build
%K3configure
%make_build

%install
%K3install

%files
%dir %_K3doc/%lng/
%lang(%lng) %_K3doc/%lng/*
#
#%dir %_K3i18n/%lng/
%_K3i18n/%lng/charset
%_K3i18n/%lng/*.desktop
%_K3i18n/%lng/*.png
#
#%dir %_K3i18n/%lng/LC_MESSAGES/
%lang(%lng) %_K3i18n/%lng/LC_MESSAGES/*.mo
#
%lang(%lng) %_K3apps/katepart/syntax/logohighlightstyle.%lng.xml
%lang(%lng) %_K3apps/kturtle/data/logokeywords.%lng.xml
%lang(%lng) %_K3apps/kturtle/examples/%lng/
#%lang(%lng) %_K3apps/ktuberling/sounds/%lng
%lang(%lng) %_K3apps/khangman/data/%lng/
%lang(%lng) %_K3apps/kanagram/data/%lng/

%changelog
* Sun Mar 25 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- Build for TDE 3.5.13 release

* Mon Mar 21 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt4
- fix build requires

* Tue Mar 01 2011 Andrey Cherepanov <cas@altlinux.org> 3.5.10-alt3
- Migration on new KDE3 placement

* Thu Jun 11 2009 Andrey Cherepanov <cas@altlinux.org> 3.5.10-alt2
- Fix KTip translation (closes: #17606) 

* Wed Aug 27 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Sat Dec 29 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt5
- update kgpg.po (#13616); thanks cas@alt

* Tue Nov 20 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt4
- update kommander.po (#13479); thanks cas@alt

* Fri Nov 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt3
- update ark translation

* Thu Nov 01 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt2
- add ark password creation string

* Thu Oct 18 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Fri Sep 28 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt7
- update kwin_clients.po kcmkwm.po; thanks cas@alt

* Tue Jul 31 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt6
- update desktop_kdebase.po

* Mon Jul 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt5
- update kcmlaptop.po klaptopdaemon.po

* Fri Jul 06 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt4
- update timezones.po

* Mon Jun 18 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt3
- update kio.po klaptopdaemon.po

* Tue Jun 05 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt2
- update timezones.po

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version

* Tue Mar 27 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt2
- add translation of new http caching options

* Tue Jan 30 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Wed Oct 18 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version

* Wed Sep 06 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- new version

* Tue Jun 06 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version

* Wed Apr 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
- new version

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt1
- new version

* Wed Dec 14 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version

* Wed Jun 08 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt1
- new version

* Fri Apr 01 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt1
- rebuild

* Wed Jan 05 2005 ZerG <zerg@altlinux.ru> 3.3.2-alt0.0.M24
- new version

* Wed Oct 13 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt2
- update tarball

* Thu Oct 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt1
- new version

* Mon Aug 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt4
- fix translation "Click for new standard session\n" in konsole

* Fri Jul 23 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt3
- fix translation of kmail reply template

* Mon Jul 05 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt2
- remove kfilereplace.mo

* Wed Jun 09 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version

* Wed Apr 21 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- new version

* Tue Mar 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- new version

* Mon Feb 09 2004 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt5
- add some translations(kmail,kgpg,etc.) from KDE_3_2_BRANCH
- add krandr translation from KDE_3_2_BRANCH

* Wed Jan 21 2004 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt4
- translate "Open Terminal" on kdesktop

* Tue Oct 21 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt3
- add translation of "Mobile Disk" on desktop

* Thu Oct 16 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt2
- fix transtation devices on desktop

* Tue Oct 07 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- update documentation from HEAD

* Fri Aug 22 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- new version

* Fri Jul 11 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt2
- add kio_devices.po

* Tue Jun 03 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt1
- new version

* Thu Apr 10 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt1
- new version

* Tue Feb 04 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt4
- release 3.1

* Mon Jan 13 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt3
- 3.1rc6

* Wed Nov 27 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt2
- update from cvs

* Fri Oct 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt1
- update from cvs

* Tue Aug 27 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt1
- new version

* Fri Aug 09 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt1
- new version

* Wed Jun 19 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.0.1-alt3
- Removed requires to locales-ru

* Tue Jun 18 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt2
- fix Poweroff translation for kdm

* Thu May 23 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt1
- new version

* Mon May 20 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt5
- update from cvs

* Wed May 08 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt4
- update from cvs

* Thu Apr 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt3
- move to /usr

* Mon Apr 15 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- update from cvs

* Thu Apr 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- release

* Wed Apr 03 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt0.2.beta2
- rename package

* Fri Mar 29 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt0.1.beta2
- build for ALT

* Mon Feb 04 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2

* Thu Dec 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1.1mdk
-

* Wed Dec 12 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-1mdk
- kde 3.0beta1

* Wed Nov 14 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2.2-1mdk
- kde 2.2.2

* Fri Sep 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2.1-2mdk
- update code

* Thu Sep 18 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2.1-1mdk
- kde 2.2.1

* Tue Aug 29 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-2mdk
- remove koffice messages

* Tue Aug 07 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-1mdk
- kde 2.2

* Sat Aug 04 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-0.pre1.1mdk
- kde 2.2 pre1

* Sun Jul 01 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2-0.beta1.1mdk
- KDE 2.2.beta1

* Sun Jun 10 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2-0.alpha2.1mdk
- KDE 2.2.alpha2

* Wed Mar 28 2001 David BAUDENS <baudens@mandrakesoft.com> 2.1.1-2mdk
- Add Obsoletes tag to allow clean update

* Tue Mar 22 2001 David BAUDENS <baudens@mandrakesoft.com> 2.1.1-1mdk
- KDE 2.1.1

* Sun Feb 26 2001 David BAUDENS <baudens@mandrakesoft.com> 2.1-1mdk
- KDE 2.1
