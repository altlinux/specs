%define lng ru
%define lngg Russian

Name: koffice-i18n-%lng
Version: 2.3.3
Release: alt2
%define beta %nil

Group: Graphical desktop/KDE
Summary: %lngg language support for koffice
License: GPL
Url: http://www.koffice.org/

Provides: koffice-i18n-lang = %version-%release
Obsoletes: koffice-i18n-%lngg
Requires: koffice-common

Source: koffice-l10n-%lng-%version.tar.bz2

BuildArch: noarch
BuildRequires: gcc-c++ kde4base-runtime-devel kde4libs-devel

%description
%lngg language support for koffice.


%prep
%setup -q -n koffice-l10n-%lng-%version

%build
%K4build

%install
%K4install

%files
%lang(%lng) %_K4i18n/%lng/LC_MESSAGES/*.mo
%lang(%lng) %_K4doc/%lng
#%lang(%lng) %_K4apps/koffice/autocorrect/%lng.xml

%changelog
* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 2.3.3-alt2
- fix build requires

* Wed Mar 16 2011 Sergey V Turchin <zerg@altlinux.org> 2.3.3-alt1
- new version

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 2.2.2-alt0.M51.1
- built for M51

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 2.2.2-alt1
- new version

* Tue Jul 20 2010 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt0.M51.1
- built for M51

* Tue Jul 20 2010 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt1
- new version

* Mon Jan 26 2009 Sergey V Turchin <zerg at altlinux dot org> 1.9.98.5-alt1
- beta5

* Fri Dec 12 2008 Sergey V Turchin <zerg at altlinux dot org> 1.9.98.3-alt1
- new beta

* Mon Nov 24 2008 Sergey V Turchin <zerg at altlinux dot org> 1.9.98.2-alt1
- new beta

* Fri Jun 08 2007 Sergey V Turchin <zerg at altlinux dot org> 1.6.3-alt1
- new version

* Mon Feb 26 2007 Sergey V Turchin <zerg at altlinux dot org> 1.6.2-alt1
- new version

* Mon Jan 15 2007 Sergey V Turchin <zerg at altlinux dot org> 1.6.1-alt1
- new version

* Thu Oct 19 2006 Sergey V Turchin <zerg at altlinux dot org> 1.6.0-alt1
- new version

* Mon Jul 17 2006 Sergey V Turchin <zerg at altlinux dot org> 1.5.2-alt1
- new version

* Tue May 23 2006 Sergey V Turchin <zerg at altlinux dot org> 1.5.1-alt1
- new version

* Thu Apr 13 2006 Sergey V Turchin <zerg at altlinux dot org> 1.5.0-alt1
- new version
