%define rname merkuro

Name: kde5-%rname
Version: 23.08.5
Release: alt5
%K5init

Group: Graphical desktop/KDE
Summary: Calendar and task management
Url: http://www.kde.org
License: GPL-3.0-or-later

ExcludeArch: %not_qt5_qtwebengine_arches

Requires: qml(QtLocation)
Requires: kde5-akonadi
Requires: kde5-akonadi-calendar
Requires: kde5-kmail-account-wizard

Source: %rname-%version.tar
Patch0: fix-menubar-display.patch
Patch1: fix_contact_create.patch

# Automatically added by buildreq on Thu Oct 05 2023 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 grantlee5-devel gtk4-update-icon-cache kde5-grantleetheme-devel kde5-ktextaddons-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-common kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-common kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-common kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXmu-devel libXrender-devel libXt-devel libassuan-devel libctf-nobfd0 libdb4-devel libdbusmenu-qt52 libdouble-conversion3 libfreetype-devel libglvnd-devel libgpg-error libgpg-error-devel libgpgme-devel libp11-kit libqca-qt5 libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libqt5-quicktest libqt5-quickwidgets libqt5-sql libqt5-svg libqt5-test libqt5-texttospeech libqt5-waylandclient libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libxcb-devel libxcbutil-keysyms libxkbcommon-devel libzxing-cpp perl pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-common qt5-base-devel qt5-declarative-devel qt5-svg-devel qt5-webengine-devel rpm-build-file rpm-build-python3 rpm-build-qml rpm-macros-python sh4 tzdata xorg-proto-devel xorg-xf86miscproto-devel
#BuildRequires: appstream clang-tools extra-cmake-modules kde5-akonadi-calendar-devel kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-kcalutils-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-libkleo-devel kde5-mailcommon-devel kde5-messagelib-devel kde5-pimcommon-devel kf5-kcalcore-devel kf5-kcontacts-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kirigami-addons-devel kf5-kirigami-devel kf5-kitemmodels-devel kf5-kpackage-devel kf5-ktextwidgets-devel kf5-plasma-framework-devel kf5-qqc2-desktop-style-devel libXScrnSaver-devel libXaw-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxcb-render-util-devel libxcbutil-cursor-devel libxcbutil-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-keysyms-devel libxkbcommon-x11-devel libxkbfile-devel python-modules-compiler python3-module-setuptools python3-module-zope qt5-imageformats qt5-quickcontrols2-devel qt5-translations qt5-wayland-devel rpm-build-qml6 tbb-devel
BuildRequires(pre): rpm-build-kf5 rpm-macros-qt5-webengine
BuildRequires: extra-cmake-modules qt5-base-devel qt5-quickcontrols2-devel qt5-wayland-devel
BuildRequires: kf5-kcalcore-devel kf5-kcontacts-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kirigami-addons-devel
BuildRequires: kf5-kirigami-devel kf5-kitemmodels-devel kf5-kpackage-devel kf5-ktextwidgets-devel
BuildRequires: kf5-plasma-framework-devel kf5-qqc2-desktop-style-devel
BuildRequires: kde5-akonadi-calendar-devel kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel
BuildRequires: kde5-kcalutils-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kmime-devel
BuildRequires: kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-libkleo-devel kde5-mailcommon-devel
BuildRequires: kde5-messagelib-devel kde5-pimcommon-devel

%description
Kirigami-based calendar and task management application that uses Akonadi.
It lets you add, edit and delete events and tasks from local and remote accounts of your choice,
while keeping changes synchronised across your Plasma desktop or phone.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Conflicts: kde5-pim-common < 16.12
%description common
%name common package

%prep
%setup -n %rname-%version
%patch0 -p1
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data locale
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories5/*.*categories
%_K5bin/merkuro-*
%_K5qml/org/kde/merkuro/
%_K5qml/org/kde/akonadi/
%_kf5_data/plasma/plasmoids/org.kde.merkuro.contact/
%_K5xdgapp/org.kde.merkuro*.desktop
%_K5icon/*/*/apps/*merkuro*.*
%_datadir/metainfo/*.xml

%changelog
* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.5-alt5
- fix requires (closes: 50747)

* Mon May 27 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.5-alt4
- clean requires

* Tue May 14 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 23.08.5-alt3
- fix contact save (closes: 48725)

* Wed Mar 27 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 23.08.5-alt2
- fix menubar display (closes: 48721)
- add the kde5-korganizer required to add accounts (closes: 48720, 48734)

* Fri Feb 16 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.5-alt1
- new version

* Fri Dec 08 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt1
- new version

* Fri Nov 10 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt1
- new version

* Wed Oct 25 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt2
- fix package

* Fri Oct 13 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt1
- new version

* Thu Oct 05 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.1-alt1
- initial build
