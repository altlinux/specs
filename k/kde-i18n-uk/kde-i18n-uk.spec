%define lng uk
%define lngg Ukrainian

Name: kde-i18n-%lng
Version: 3.5.13
Release: alt1

Group: Graphical desktop/KDE
Summary: %lngg language support for KDE
License: GPL
Url: http://www.kde.org/

BuildArch: noarch
Provides: kde-i18n-lang = %version-%release
Requires: kde-common
Conflicts: kdevelop-i18n < %version-%release 

Source: kde-i18n-%lng-%{version}.tar.bz2
#Source: kde-i18n-%lng-3.3.0.tar.bz2

BuildRequires: kdelibs-devel xml-utils

%description
%lngg language support for KDE.

%prep
#%setup -q -n kde-i18n-%lng-%version
#%setup -q -n kde-i18n-%lng-3.3.0
%setup -q

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
#
#%dir %_K3i18n/%lng/LC_MESSAGES/
%lang(%lng) %_K3i18n/%lng/LC_MESSAGES/*.mo
#
#%lang(%lng) %_K3apps/katepart/syntax/logohighlightstyle.%lng.xml
#%lang(%lng) %_K3apps/kturtle/data/logokeywords.%lng.xml
#%lang(%lng) %_K3apps/kturtle/examples/%lng/
#%lang(%lng) %_K3apps/ktuberling/sounds/%lng
#%lang(%lng) %_K3apps/khangman/data/%lng/

%changelog
* Sun Mar 25 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- Build for TDE 3.5.13 release

* Mon Mar 14 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt2
- move to alternate place

* Wed Aug 27 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Thu Oct 18 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version

* Tue Jan 30 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Wed Oct 18 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version

* Wed Sep 06 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- new version

* Tue Jun 06 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version

* Thu Apr 06 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
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

* Mon Jul 05 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt2
- remove kfilereplace.mo

* Wed Jun 09 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version

* Wed Apr 21 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- new version

* Tue Mar 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- new version

* Fri Aug 22 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- new version

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

* Wed Jun 19 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.0.1-alt1
- Removed requires to locales-uk

* Thu May 23 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt1
- new version

* Mon May 20 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt3
- update from cvs

* Thu Apr 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- move to /usr

* Thu Apr 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- release

* Wed Apr 03 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt0.2.beta2
- rename package

* Mon Feb 04 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2

* Thu Dec 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1.1mdk
-

* Wed Dec 12 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-1mdk
- kde 3.0beta1

* Wed Nov 14 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2.2-1mdk
- kde 2.2.2

* Fri Sep 21 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2.1-2mdk
- Update code

* Thu Sep 18 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2.1-1mdk
- kde 2.2.1

* Wed Aug 29 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-2mdk
- remove koffice messages

* Wed Aug 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-1mdk
- kde 2.2

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
