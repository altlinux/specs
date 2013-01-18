Name:    kde4-regular
Version: 4.10
Release: alt4

Group: Graphical desktop/KDE
Summary: KDE4 common collection
URL: http://www.kde.org/
License: GPL

BuildArch: noarch

Requires: phonon-gstreamer
Requires: gtk2-theme-oxygen-gtk
Requires: gtk3-theme-oxygen-gtk

Requires: fonts-ttf-dejavu
Requires: fonts-ttf-droid

Requires: soprano-backend-redland
Requires: soprano-backend-virtuoso
Requires: soprano

Requires: kde4base-workspace-core kde4base-workspace-cursors kde4base-workspace-wallpapers
Requires: kde4accessibility
Requires: kde4admin
Requires: kde4artwork
Requires: kde4base
Requires: kde4edu
Requires: kde4games
Requires: kde4graphics
Requires: kde4network
Requires: kde4pim
Requires: kde4plasma-addons
Requires: kde4toys
Requires: kde4utils
Requires: kde4-i18n-kk
Requires: kde4-i18n-ru
Requires: kde4-i18n-uk

Requires: kde4-k3b
Requires: kde4-amarok
Requires: kde4-kaffeine
Requires: rekonq
Requires: konversation
Requires: kde4-smb4k
Requires: choqok
Requires: kde4-telepathy
Requires: kde4-kopete-antispam
Requires: kde4-ktorrent
Requires: bluedevil
Requires: kde4-webkitpart
Requires: kde4-k9copy
Requires: kde4-kid3
Requires: kde4-krusader
Requires: kde4-synaptiks
Requires: kde4-soundkonverter
Requires: kde4-digikam kde4-digikam-image-plugins kde4-digikam-utils kde4-digikam-i18n
Requires: kde4-kipi-plugins
Requires: kdenlive
Requires: skanlite


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
* Fri Jan 18 2013 Sergey V Turchin <zerg@altlinux.org> 4.10-alt4
- rename from kde4-default

* Sat Dec 22 2012 Sergey V Turchin <zerg@altlinux.org> 4.10-alt3
- update requires

* Fri Dec 21 2012 Sergey V Turchin <zerg@altlinux.org> 4.10-alt2
- add kde4-telepathy

* Thu Dec 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.10-alt1
- initial build
