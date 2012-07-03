Name:  kde-i18n
Version: 3.5
Release: alt4

Summary: KDE translations (virtual package)
License: GPL
Group: Graphical desktop/KDE
URL: http://i18n.kde.org/

Requires: kde-i18n-es >= %version
Requires: kde-i18n-kk >= %version
Requires: kde-i18n-pt_BR >= %version
Requires: kde-i18n-ru >= %version
Requires: kde-i18n-uk >= %version

BuildArch: noarch

%description
Empty package which only requires all KDE translations.

%files

%changelog
* Mon Mar 14 2011 Sergey V Turchin <zerg@altlinux.org> 3.5-alt4
- sync requires with KDE4

* Wed Aug 27 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5-alt3
- add Belarusian to requires

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5-alt2
- add Kazakh to requires

* Wed Dec 14 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5-alt1
- new version

* Thu Jun 09 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4-alt1
- initial spec

