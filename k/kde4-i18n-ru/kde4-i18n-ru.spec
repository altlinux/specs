
%define lng ru
%define lngg Russian

Name: kde4-i18n-%lng
Version: 4.8.4
Release: alt1

Group: Graphical desktop/KDE
Summary: %lngg language support for KDE
License: GPL
Url: http://www.kde.org/

#Provides: kde-i18n-%lng = %version-%release
Requires: kde-common >= 4.1
BuildArch: noarch

Source: kde-l10n-%lng-%version.tar
Patch1: kmail-migration.patch

BuildRequires: gcc-c++ kde4libs-devel

%description
%lngg language support for KDE.


%prep
%setup -q -n kde-l10n-%lng-%version
%patch1 -p1
#find -type f -name *.gmo | while read f; do rm -f $f; done
#find -type f -name index.cache.bz2 | while read f; do rm -f $f; done
find -type f -name CMakeLists.txt | \
while read cm; do
    dirs=`grep add_subdirectory "$cm" | sed 's|.*[(]\(.*\)[)].*|\1|'`
    if [ -n "$dirs" ]; then
	pushd `dirname "$cm"`
	for d in $dirs; do
	    mkdir -p $d
	done
	popd
    fi
done

for d in docs messages
do
    [ -d $d ] || continue
    pushd $d
    grep -qe "^add_subdirectory([[:space:]]*kdepim[[:space:]]*)" CMakeLists.txt \
	|| echo "add_subdirectory( kdepim )" >> CMakeLists.txt
    popd
done

sed -i 's|изобрадени|изображени|g' messages/kdewebdev/kimagemapeditor.po


%build
%K4cmake
%K4make


%install
%K4install

if ! [ -e %buildroot/%_K4doc/%lng/common ]; then
    mkdir -p %buildroot/%_K4doc/%lng/common/
    pushd %_K4doc/en/common/
    for f in *; do
	ln -s %_K4doc/en/common/$f %buildroot/%_K4doc/%lng/common/$f
    done
    popd
fi


%files
%dir %_K4doc/%lng/
%lang(%lng) %_K4doc/%lng/*
#
%dir %_K4i18n/%lng/
%_K4i18n/%lng/entry.desktop
#
%dir %_K4i18n/%lng/
%dir %_K4i18n/%lng/LC_MESSAGES/
%lang(%lng) %_K4i18n/%lng/LC_MESSAGES/*.mo
%dir %_K4i18n/%lng/LC_SCRIPTS/
%lang(%lng) %_K4i18n/%lng/LC_SCRIPTS/*
#
%lang(%lng) %_K4apps/kvtml/%lng/
#
%lang(%lng) %_K4apps/ktuberling/sounds/%lng
%lang(%lng) %_K4apps/ktuberling/sounds/%lng.soundtheme
#%lang(%lng) %_K4apps/khangman/%lng.txt
%lang(%lng) %_K4apps/klettres/%lng
%lang(%lng) %_K4apps/katepart/syntax/logohighlightstyle.%lng.xml
#%lang(%lng) %_K4apps/kturtle/data/logokeywords.%lng.xml
#%lang(%lng) %_K4apps/kturtle/examples/%lng/

%changelog
* Sat Jun 09 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Tue May 15 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Thu Apr 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Wed Dec 14 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- built for M60P

* Mon Dec 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Mon Sep 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Mon Aug 22 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt2
- fix kimagemapeditor translation

* Fri Jul 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Wed Jun 15 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Fri May 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt2
- package LC_SCRIPTS

* Tue May 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Tue Apr 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Sat Mar 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt2
- update translations

* Fri Mar 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- bump version

* Thu Feb 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt2
- update sources

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- bump version

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Wed Sep 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Mon Aug 16 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt2
- add kdepim translations

* Wed Aug 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Wed Mar 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Wed Mar 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Fri Feb 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Tue Jan 26 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Wed Dec 02 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Wed Sep 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt2
- fix "Documents" place translation

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Mon Aug 10 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt2
- update translations

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Wed Jul 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Fri Jul 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Wed May 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Mon Apr 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Fri Mar 06 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Thu Jan 29 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Thu Jan 22 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Fri Oct 10 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Fri Sep 05 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Mon Aug 04 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Mon Jun 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt1
- new version

* Thu May 08 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt1
- new version
- temporary built 4.0.71 as 4.0.72

* Thu Apr 03 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt2
- new version

* Wed Apr 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt1
- temporary build 4.0.2 as 4.0.3

* Wed Mar 26 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt1
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
