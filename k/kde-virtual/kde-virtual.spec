Name:  kde-virtual
Version: 3.5
Release: alt5

%define smr KDE (dependencies package)

Summary: %smr
License: GPL
Group: Graphical desktop/KDE
URL: http://www.kde.org/

BuildArch: noarch

Source0: %name.list
Source1: %name.sh

%define kde_kde  %{expand: %(%SOURCE1 %SOURCE0 kde)}
%define kde_small  %{expand: %(%SOURCE1 %SOURCE0 small)}
%define kde_mini  %{expand: %(%SOURCE1 %SOURCE0 mini)}
%define kde_devel %{expand: %(%SOURCE1 %SOURCE0 devel)}

%define dsk %(echo -e "K Desktop Environment - virtual package\\nto easy select KDE packages during install.")
%define dsk_ru %(echo -e "K Desktop Environment - виртуальный пакет.\\nОн облегчает выбор пакетов KDE при установке.")

%description
%dsk

%package -n kde
Summary: %smr
License: GPL
Group: Graphical desktop/KDE
Requires: %kde_kde
%description -n kde
%dsk
%description -n kde -l ru_RU.KOI8-R
%dsk_ru

%package -n kde-small
Summary: %smr
License: GPL
Group: Graphical desktop/KDE
Requires: %kde_small
%description -n kde-small
%dsk
%description -n kde-small -l ru_RU.KOI8-R
%dsk_ru

%package -n kde-mini
Summary: %smr
License: GPL
Group: Graphical desktop/KDE
Requires: %kde_mini
%description -n kde-mini
%dsk
%description -n kde-mini -l ru_RU.KOI8-R
%dsk_ru

%package -n kde-devel
Summary: %smr
License: GPL
Group: Development/KDE and QT
Requires: %kde_devel
%description -n kde-devel
%dsk
%description -n kde-devel -l ru_RU.KOI8-R
%dsk_ru

%files -n kde
%files -n kde-small
%files -n kde-mini
%files -n kde-devel

%changelog
* Wed Feb 01 2012 Sergey V Turchin <zerg@altlinux.org> 3.5-alt5
- exclude kdevelop

* Mon Nov 29 2010 Sergey V Turchin <zerg@altlinux.org> 3.5-alt4
- exclude arts

* Wed Nov 24 2010 Sergey V Turchin <zerg@altlinux.org> 3.5-alt3
- exclude kdeedu-devel and kdagames-devel

* Mon May 21 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5-alt2
- add requires to gtk2-themes-qtcurve as default for GTK2

* Mon Mar 19 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5-alt1
- drom maxi, big, distr subpackages

* Thu May 05 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4-alt2
- change gtk theme Geramik to Industrial

* Thu Mar 31 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4-alt1
- new version

* Tue Oct 05 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3-alt1
- fix requires for new version

* Tue Jun 15 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2-alt6
- fix requires

* Wed Jun 02 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2-alt5
- fix requires

* Tue Jun 01 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2-alt4
- fix requires

* Fri Apr 02 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2-alt3
- fix resuires

* Wed Mar 24 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2-alt2
- fix resuires

* Fri Mar 12 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2-alt1
- update requires

* Thu Nov 13 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt9
- fix requires

* Wed Nov 05 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt8
- fix requires

* Mon Nov 03 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt7
- fix requires

* Fri Oct 24 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt6
- fix requires

* Tue Oct 14 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt5
- fix requires

* Fri Oct 03 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt4
- fix requires

* Thu Oct 02 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt3
- fix requires

* Wed Oct 01 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt2
- fix requires
- new subpackage %name-distr

* Tue Sep 23 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- fix requires

* Wed Jul 30 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- fix requires
- fix build in C locale

* Tue Apr 01 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt2
- fix requires
- update packages list

* Fri Mar 21 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1
- fix requires

* Wed Feb 26 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt15
- fix requires

* Wed Feb 19 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt14
- add package kde-junior
- fix requires

* Wed Feb 12 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt13
- add kdebase-smbclient-source to devel
- remove kde-i18n-lang

* Wed Feb 12 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt12
- remove muse from requires (requires goes to givertcap with SUID)

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt11
- add kmail-aegypten-plugins
  to kde-big kde-maxi packages

* Thu Feb 06 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt10
- add ksocrat to kde-big kde-maxi packages

* Thu Feb 06 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt9
- change requires from Geramik to gtk-engines-geramik

* Tue Feb 04 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt8
- change requires from icons-slick to kde-icon-theme-slick
  in kde package
- add requires to
  Geramik
  kde-icon-theme-aquafusion
  kde-icon-theme-marbles
  kde-icon-theme-noia
  to kde-big kde-maxi packages

* Wed Jan 29 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt7
- add icons-slick to kde kde-big kde-maxi

* Tue Jan 28 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt6
- add kdenetwork-devel to kde-devel

* Wed Jan 15 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt5
- update packages list

* Wed Jan 08 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt4
- fix packages list (about sqlgui, kdegraphics-devel)

* Mon Dec 30 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt3
- fix Group

* Thu Dec 26 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt2
- update packages.list

* Tue Dec 24 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1-alt1
- initial spec

