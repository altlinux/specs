Name:    kde4mobile-regular
Version: 4.10
Release: alt3

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
%ifarch arm
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

Requires: bangarang
Requires: kamoso
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
* Thu Apr 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt3
- fix requires

* Tue Apr 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt2
- update requires

* Mon Apr 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt1
- initial build
