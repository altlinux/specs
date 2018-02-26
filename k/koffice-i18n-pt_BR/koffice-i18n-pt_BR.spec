%define lng pt_BR
%define lngg Brazil Portuguese

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

* Wed Oct 06 2010 Sergey V Turchin <zerg@altlinux.org> 2.2.2-alt0.M51.1
- built for M51

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 2.2.2-alt1
- new version

* Tue Jul 20 2010 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt0.M51.1
- built for M51

* Tue Jul 20 2010 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt1
- new version

* Wed Dec 16 2009 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt1
- new version

* Tue Jun 30 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1
- new version

* Mon Jun 08 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt1
- new version

* Thu Jan 29 2009 Sergey V Turchin <zerg at altlinux dot org> 1.9.98.5-alt1
- beta5
- initial specfile
