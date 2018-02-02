Name:    kde4-regular
Version: 4.14
Release: alt7

Group: Graphical desktop/KDE
Summary: KDE4 common collection
URL: http://www.kde.org/
License: GPL

BuildArch: noarch

Requires: phonon-gstreamer
Requires: gtk2-theme-oxygen-gtk
Requires: gtk3-theme-oxygen-gtk

Requires: fonts-ttf-dejavu
Requires: fonts-ttf-google-droid-sans
Requires: fonts-ttf-google-droid-sans-mono
Requires: fonts-ttf-google-droid-serif

Requires: appmenu-qt4
Requires: kde4-styles-breeze

Requires: kde4base-workspace-core kde4base-workspace-cursors kde4base-workspace-wallpapers
Requires: kde4accessibility
Requires: kde4admin
Requires: kde4artwork
Requires: kde4base
Requires: kde4edu
Requires: kde4games
Requires: kde4graphics
Requires: kde4network
Requires: kde4-kopete-antispam
Requires: kde4pim
Requires: kde4plasma-addons
Requires: kde4toys
Requires: kde4utils
Requires: kde4-i18n-kk
Requires: kde4-i18n-ru
Requires: kde4-i18n-uk

Requires: kde4-kio-mtp
Requires: kde4-k3b
Requires: kde4-k9copy
Requires: kde4-amarok
Requires: kde4-smplayer
Requires: rekonq
Requires: konversation
Requires: kde4-smb4k
Requires: choqok
Requires: kde4-telepathy
Requires: kde4-ktorrent
Requires: bluedevil
Requires: kde4-webkitpart
Requires: kde4-kid3
Requires: kde4-krusader
Requires: kde4-synaptiks
Requires: kde4-soundkonverter
#Requires: kde4-digikam kde4-digikam-image-plugins kde4-digikam-utils kde4-digikam-i18n
Requires: kde4-kipi-plugins-core
#Requires: kdenlive
Requires: skanlite
Requires: kde4plasma-addon-yawp
Requires: kde4-ksshaskpass


Requires: calligra
Requires: calligra-l10n-kk
Requires: calligra-l10n-ru
Requires: calligra-l10n-uk

Source: .gear-rules

%description
K Desktop Environment 4 collection package
to easy select KDE packages during install
%description -l ru_RU.UTF-8
K Desktop Environment 4 сборный пакет,
облегчающий выбор пакетов KDE при установке

%files

%changelog
* Fri Feb 02 2018 Sergey V Turchin <zerg@altlinux.org> 4.14-alt7
- exclude kde4-digikam

* Wed Nov 08 2017 Sergey V Turchin <zerg@altlinux.org> 4.14-alt6
- remove kde4-kio-upnp-ms

* Tue Jun 13 2017 Sergey V Turchin <zerg@altlinux.org> 4.14-alt5
- remove sflphone-client-kde4

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 4.14-alt4
- update requires

* Thu Oct 22 2015 Sergey V Turchin <zerg@altlinux.org> 4.14-alt3
- using kde4-smplayer instead of kde4-kaffeine

* Wed Aug 05 2015 Sergey V Turchin <zerg@altlinux.org> 4.14-alt2
- remove kdenlive because KDE5 now

* Sat Sep 06 2014 Sergey V Turchin <zerg@altlinux.org> 4.14-alt1
- update requires

* Fri Sep 05 2014 Sergey V Turchin <zerg@altlinux.org> 4.12-alt2
- update requires

* Mon Apr 28 2014 Sergey V Turchin <zerg@altlinux.org> 4.12-alt1
- remove kde4-colord
- add kde4-ksshaskpass

* Mon Apr 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt9
- add kde4plasma-addon-yawp
- use fonts-ttf-google-droid instead of fonts-ttf-droid

* Fri Mar 22 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt8
- add kio-mtp and kio-upnp-ms

* Wed Feb 20 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt7
- add sflphone-client-kde4

* Mon Feb 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt6
- add appmenu-qt4

* Tue Feb 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt5
- add kde4-colord

* Fri Jan 18 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt4
- rename from kde4-default

* Sat Dec 22 2012 Sergey V Turchin <zerg@altlinux.org> 4.10-alt3
- update requires

* Fri Dec 21 2012 Sergey V Turchin <zerg@altlinux.org> 4.10-alt2
- add kde4-telepathy

* Thu Dec 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.10-alt1
- initial build
