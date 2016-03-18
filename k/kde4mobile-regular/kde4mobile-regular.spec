%if_enabled kde_mobile
%def_disable desktop
%else
%def_enable desktop
%endif

Name:    kde4mobile-regular
Version: 4.10
Release: alt7

Group: Graphical desktop/KDE
Summary: KDE4 mobile common collection
URL: http://www.kde.org/
License: GPL

#BuildArch: noarch
Provides: %name-%_target_cpu

Requires: phonon-gstreamer
Requires: gtk2-theme-oxygen-gtk
Requires: gtk3-theme-oxygen-gtk

Requires: fonts-ttf-dejavu
Requires: fonts-ttf-google-droid-sans
Requires: fonts-ttf-google-droid-sans-mono
Requires: fonts-ttf-google-droid-serif

Requires: soprano-backend-redland
Requires: soprano-backend-virtuoso
Requires: soprano

Requires: maliit-plugins
Requires: kde4-plasma-active-maliit
Requires: kde4-artwork-active
Requires: kde4-contour
Requires: kde4-declarative-plasmoids
Requires: kde4-plasma-mobile
Requires: kde4-share-like-connect
#Requires: kde4-settings-kmobile
%if_disabled desktop
Requires: kde4-startactive
%endif

Requires: kde4base-workspace-core
Requires: kde4base-plasma-applets
Requires: kde4base-dolphin
Requires: kde4base-kwrite
Requires: kde4base-konsole
Requires: kde4plasma-addons
Requires: kde4pim-environment-mobile
Requires: kde4pim
Requires: kde4multimedia-kmix
Requires: kde4multimedia-videothumbnail
Requires: kde4utils
Requires: kde4-i18n-kk
Requires: kde4-i18n-ru
Requires: kde4-i18n-uk

Requires: kde4multimedia-dragonplayer
Requires: kde4-kamerka
Requires: kde4-telepathy
Requires: bluedevil
Requires: kde4-webkitpart
Requires: skanlite
Requires: kde4plasma-addon-yawp

#Requires: calligra
#Requires: calligra-l10n-kk
#Requires: calligra-l10n-ru
#Requires: calligra-l10n-uk

Source: .gear-rules

%description
KDE Active package to easy select packages during install
%description -l ru_RU.UTF-8
Сборный пакет KDE Active, облегчающий выбор пакетов при установке

%files

%changelog
* Fri Mar 18 2016 Sergey V Turchin <zerg@altlinux.org> 4.10-alt7
- change kamoso to kde4-kamerka

* Mon Feb 29 2016 Sergey V Turchin <zerg@altlinux.org> 4.10-alt6
- change bangarang to dragonplayer

* Tue Jul 16 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt5
- don't require kde4-startactive by default because KDE was build with Desktop profile

* Fri Apr 12 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt4
- fix requires

* Thu Apr 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt3
- fix requires

* Tue Apr 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt2
- update requires

* Mon Apr 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt1
- initial build
