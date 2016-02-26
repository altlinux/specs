%define rname kdepim

%define pim_sover 5
%define libakregatorinterfaces libakregatorinterfaces%pim_sover
%define libakregatorprivate libakregatorprivate%pim_sover
%define libkf5calendarsupport libkf5calendarsupport%pim_sover
%define libkf5calendarsupportcollectionpage libkf5calendarsupportcollectionpage%pim_sover
%define libkf5composereditorng libkf5composereditorng%pim_sover
%define libkf5eventviews libkf5eventviews%pim_sover
%define libkf5followupreminder libkf5followupreminder%pim_sover
%define libgrantleethemeeditor libgrantleethemeeditor%pim_sover
%define libkf5grantleetheme libkf5grantleetheme%pim_sover
%define libincidenceeditorsngmobile libincidenceeditorsngmobile%pim_sover
%define libkf5incidenceeditorsng libkf5incidenceeditorsng%pim_sover
%define libkf5kaddressbookgrantlee libkf5kaddressbookgrantlee%pim_sover
%define libkaddressbookprivate libkaddressbookprivate%pim_sover
%define libkf5libkdepim libkf5libkdepim%pim_sover
%define libkf5kdepimdbusinterfaces libkf5kdepimdbusinterfaces%pim_sover
%define libkf5kdgantt2 libkf5kdgantt2%pim_sover
%define kleopatraclientcore_sover 1
%define libkleopatraclientcore libkleopatraclientcore%kleopatraclientcore_sover
%define kleopatraclientgui_sover 1
%define libkleopatraclientgui libkleopatraclientgui%kleopatraclientgui_sover
%define libkf5libkleo libkf5libkleo%pim_sover
%define libkmailprivate libkmailprivate%pim_sover
%define libkf5kmanagesieve libkf5kmanagesieve%pim_sover
%define libknotesprivate libknotesprivate%pim_sover
%define libkontactprivate libkontactprivate%pim_sover
%define libkorganizer_core libkorganizer_core%pim_sover
%define libkorganizer_interfaces libkorganizer_interfaces%pim_sover
%define libkorganizerprivate libkorganizerprivate%pim_sover
%define libkpgp libkpgp%pim_sover
%define libkf5ksieve libkf5ksieve%pim_sover
%define libkf5ksieveui libkf5ksieveui%pim_sover
%define libkf5mailcommon libkf5mailcommon%pim_sover
%define libkf5mailimporter libkf5mailimporter%pim_sover
%define libkf5messagecomposer libkf5messagecomposer%pim_sover
%define libkf5messagecore libkf5messagecore%pim_sover
%define libkf5messagelist libkf5messagelist%pim_sover
%define libkf5messageviewer libkf5messageviewer%pim_sover
%define libkf5noteshared libkf5noteshared%pim_sover
%define libkf5pimcommon libkf5pimcommon%pim_sover
%define libpimsettingexporterprivate libpimsettingexporterprivate%pim_sover
%define libkf5sendlater libkf5sendlater%pim_sover
%define libkf5templateparser libkf5templateparser%pim_sover
%define libkf5gravatar libkf5gravatar%pim_sover

Name: kde5-pim
Version: 15.12.2
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Personal Information Management
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: %name-akregator
Requires: %name-blogilo
Requires: %name-kaddressbook
Requires: %name-kalarm
Requires: %name-kleopatra
Requires: %name-kmail
Requires: %name-knotes
Requires: %name-kontact
Requires: %name-korganizer

Source: %rname-%version.tar
Patch1: alt-akonadi-plugins-dir.patch
Patch2: alt-akonadi-resources-dir.patch
Patch3: alt-install-kalarm-helper.patch
Patch4: alt-fix-linking.patch

# Automatically added by buildreq on Thu Sep 03 2015 (-bi)
# optimized out: boost-devel-headers cmake cmake-modules docbook-dtds docbook-style-xsl elfutils glibc-devel-static kde5-akonadi-devel kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbusmenu-qt52 libgpg-error libgpg-error-devel libgst-plugins1.0 libical-devel libjson-c libkf5gpgmepp-pthread libqt5-concurrent libqt5-core libqt5-dbus libqt5-declarative libqt5-designer libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-texttospeech libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbfile-devel pkg-config python-base python3 python3-base qt5-base-devel qt5-phonon-devel qt5-script-devel qt5-tools-devel qt5-webkit-devel ruby ruby-stdlibs shared-mime-info xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: extra-cmake-modules gcc-c++ grantlee5-devel kde5-akonadi-calendar-devel kde5-akonadi-search-devel kde5-gpgmepp-devel kde5-kalarmcal-devel kde5-kblog-devel kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kldap-devel kde5-kmailtransport-devel kde5-kmbox-devel kde5-kmime-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-ktnef-devel kde5-pimlibs-devel kde5-syndication-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdewebkit-devel kf5-kdnssd-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kross-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-kxmlrpcclient-devel kf5-libkgapi-devel kf5-solid-devel kf5-sonnet-devel libassuan-devel libgpgme-devel libldap-devel libsasl2-devel python-module-google qt5-quick1-devel qt5-speech-devel qt5-tools-devel-static qt5-x11extras-devel rpm-build-python3 rpm-build-ruby xsltproc zlib-devel-static
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: qt5-quick1-devel qt5-tools-devel-static qt5-x11extras-devel
#BuildRequires: qt5-speech-devel
BuildRequires: xsltproc grantlee5-devel libassuan-devel libgpgme-devel libldap-devel libsasl2-devel zlib-devel
BuildRequires: kde5-akonadi-calendar-devel kde5-akonadi-search-devel kde5-gpgmepp-devel kde5-kalarmcal-devel kde5-kblog-devel kde5-kcalcore-devel
BuildRequires: kde5-kcalutils-devel kde5-kcontacts-devel kde5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kldap-devel
BuildRequires: kde5-kmailtransport-devel kde5-kmbox-devel kde5-kmime-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-ktnef-devel
BuildRequires: kde5-pimlibs-devel kde5-syndication-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdesignerplugin-devel kf5-kdewebkit-devel kf5-kdnssd-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel
BuildRequires: kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel
BuildRequires: kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-knewstuff-devel
BuildRequires: kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kross-devel kf5-kservice-devel kf5-ktexteditor-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel
BuildRequires: kf5-kxmlrpcclient-devel kf5-libkgapi-devel kf5-solid-devel kf5-sonnet-devel

%description
Information Management applications for the K Desktop Environment.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkf5gravatar
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5gravatar
KF5 library

%package -n %libakregatorinterfaces
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libakregatorinterfaces
KF5 library

%package -n %libakregatorprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libakregatorprivate
KF5 library

%package -n %libkf5calendarsupport
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5calendarsupport
KF5 library

%package -n %libkf5calendarsupportcollectionpage
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5calendarsupportcollectionpage
KF5 library

%package -n %libkf5composereditorng
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5composereditorng
KF5 library

%package -n %libkf5eventviews
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5eventviews
KF5 library

%package -n %libkf5followupreminder
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5followupreminder
KF5 library

%package -n %libgrantleethemeeditor
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libgrantleethemeeditor
KF5 library

%package -n %libkf5grantleetheme
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5grantleetheme
KF5 library

%package -n %libincidenceeditorsngmobile
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libincidenceeditorsngmobile
KF5 library

%package -n %libkf5incidenceeditorsng
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5incidenceeditorsng
KF5 library

%package -n %libkf5kaddressbookgrantlee
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5kaddressbookgrantlee
KF5 library

%package -n %libkaddressbookprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkaddressbookprivate
KF5 library

%package -n %libkf5libkdepim
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5libkdepim
KF5 library

%package -n %libkf5kdepimdbusinterfaces
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5kdepimdbusinterfaces
KF5 library

%package -n %libkf5kdgantt2
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5kdgantt2
KF5 library

%package -n %libkleopatraclientcore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkleopatraclientcore
KF5 library

%package -n %libkleopatraclientgui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkleopatraclientgui
KF5 library

%package -n %libkf5libkleo
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5libkleo
KF5 library

%package -n %libkmailprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkmailprivate
KF5 library

%package -n %libkf5kmanagesieve
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5kmanagesieve
KF5 library

%package -n %libknotesprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libknotesprivate
KF5 library

%package -n %libkontactprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkontactprivate
KF5 library

%package -n %libkorganizer_core
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkorganizer_core
KF5 library

%package -n %libkorganizer_interfaces
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkorganizer_interfaces
KF5 library

%package -n %libkorganizerprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkorganizerprivate
KF5 library

%package -n %libkpgp
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkpgp
KF5 library

%package -n %libkf5ksieve
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5ksieve
KF5 library

%package -n %libkf5ksieveui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5ksieveui
KF5 library

%package -n %libkf5mailcommon
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5mailcommon
KF5 library

%package -n %libkf5mailimporter
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5mailimporter
KF5 library

%package -n %libkf5messagecomposer
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5messagecomposer
KF5 library

%package -n %libkf5messagecore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5messagecore
KF5 library

%package -n %libkf5messagelist
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5messagelist
KF5 library

%package -n %libkf5messageviewer
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5messageviewer
KF5 library

%package -n %libkf5noteshared
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5noteshared
KF5 library

%package -n %libkf5pimcommon
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5pimcommon
KF5 library

%package -n %libpimsettingexporterprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libpimsettingexporterprivate
KF5 library

%package -n %libkf5sendlater
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5sendlater
KF5 library

%package -n %libkf5templateparser
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5templateparser
KF5 library

%package akonadi
Summary: KDE PIM storage framework
Group: Graphical desktop/KDE
Requires: %name-common = %EVR
Requires: kde5-pim-runtime kde5-akonadi-search
%description akonadi
KDE PIM storage framework

%package akregator
Summary: RSS/Atom feed reader for KDE
Group: Networking/News
Requires: %name-common = %EVR
%description akregator
RSS/Atom feed reader for KDE

%package blogilo
Summary: Blogging client for kde
Group: Graphical desktop/KDE
Requires: %name-common = %EVR
%description blogilo
Blogilo is a blogging client for KDE, which supports famous blogging
APIs.

%package kaddressbook
Summary: Addressbook for KDE
Group: Graphical desktop/KDE
Requires: %name-common = %EVR
Requires: %name-akonadi
%description kaddressbook
Addressbook for KDE

%package kalarm
Summary: Personal Alarm Scheduler
Group: Graphical desktop/KDE
Requires: %name-common = %EVR
%description kalarm
Personal Alarm Scheduler

%package kleopatra
Summary: Certificate Manager for KDE
Group: Graphical desktop/KDE
Requires: %name-common = %EVR
Requires: gnupg2 dirmngr pinentry-x11
%description kleopatra
Certificate Manager for KDE

%package kmail
Summary: A mail client for KDE
Group: Networking/Mail
URL: http://userbase.kde.org/KMail
Requires: %name-common = %EVR
#Requires: %name-kmail-common = %version-%release
Requires: %name-akonadi
%description kmail
A mail client for KDE

%package knotes
Summary: Post-It notes on the KDE desktop
Group: Graphical desktop/KDE
Requires: %name-common = %EVR
#Requires: %name-kresources
Requires: %name-akonadi
%description knotes
Post-It notes on the desktop

%package kontact
Summary: Integrated solution to your KDE PIM
Group: Graphical desktop/KDE
Requires: %name-common = %EVR
Requires: %name-akonadi
%description kontact
Integrated solution to your KDE PIM

%package korganizer
Summary: Electronic organizer for KDE
Group: Graphical desktop/KDE
Requires: %name-common = %EVR
#Requires: %name-kresources
Requires: %name-akonadi
%description korganizer
Electronic organizer for KDE


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# rename against kde4 conflict
find kalarm -type f | \
while read f ; do
    sed -i 's|org.kde.kalarmrtcwake|org.kde5.kalarmrtcwake|g' $f
done

%build
%K5build

%install
%K5install
%K5install_move data akonadi akregator composereditor doc importwizard kaddressbook kalarm kconf_update
%K5install_move data kdepimwidgets kleopatra kmail2 knode knotes kontact korgac korganizer kwatchgnupg
%K5install_move data libkleopatra libmessageviewer messagelist messageviewer pimsettingexporter sieve

%files
%files common
%config(noreplace) %_K5xdgconf/*rc
%config(noreplace) %_K5xdgconf/kdepim.categories
%doc COPYING*
%dir %_K5srv/kontact/
%_K5icon/*/*/actions/*.*
%_K5icon/*/*/mimetypes/*.*
%_K5srvtyp/*.desktop
%_K5xdgmime/*.xml
%_K5cfg/*.kcfg

%files akonadi
%_K5bin/akonadi_*_agent
%_datadir/akonadi5/agents/*.desktop
%_K5notif/akonadi_*_agent.notifyrc
%doc %_K5doc/en/akonadi_*_agent/
#
%_K5bin/akonadiconsole
%_K5icon/*/*/apps/akonadiconsole.*
#%_K5xmlgui/akonadiconsole/
%_K5cf_upd/*akonadiconsole*
%_K5xdgapp/org.kde.akonadiconsole.desktop
#
%_K5bin/ispdb
%_K5bin/accountwizard
%_K5plug/accountwizard_plugin.so
%_datadir/akonadi5/accountwizard/*
%_K5xdgapp/org.kde.accountwizard.desktop
#
%_K5bin/importwizard
%_K5xdgapp/org.kde.importwizard.desktop
%_K5cf_upd/*importwizard*
%_K5data/importwizard/
%doc %_K5doc/en/importwizard/
#
%_K5bin/sieveeditor
%_K5xdgapp/org.kde.sieveeditor.desktop
%_K5data/sieve/
%_K5cf_upd/*sieveeditor*
#%_K5xmlgui/sieveeditor/
%doc %_K5doc/en/sieveeditor/
#
%_K5bin/konsolekalendar
%_K5xdgapp/konsolekalendar.desktop
%_K5icon/*/*/apps/konsolekalendar.*
%doc %_K5doc/en/konsolecalendar/
#
%_K5bin/storageservicemanager
%_K5xdgapp/org.kde.storageservicemanager.desktop
%_K5notif/storageservicemanager.notifyrc
#%_K5xmlgui/storageservicemanager/
%_K5cf_upd/*storageservicemanager*
#
%_K5bin/pimsettingexporter
%_K5bin/pimsettingexporterconsole
%_K5xdgapp/org.kde.pimsettingexporter.desktop
#%_K5data/pimsettingexporter/
%_K5cf_upd/*pimsettingexporter*
#%_K5xmlgui/pimsettingexporter/
%doc %_K5doc/en/pimsettingexporter/
#
%_K5bin/mboximporter
%_K5xdgapp/org.kde.mboximporter.desktop
#
%_K5bin/calendarjanitor
#%_K5bin/kincidenceeditor

%files akregator
%_K5bin/akregator
%_K5bin/akregatorstorageexporter
%_K5plug/akregator_*.so
%_K5plug/akregatorpart.so
%_K5plug/kontact_akregatorplugin.so
%_K5xdgapp/org.kde.akregator.desktop
%_K5data/akregator/
%_K5cf_upd/*akregator*
%_K5xmlgui/akregator/
%_K5notif/akregator.notifyrc
%_K5srv/kontact/akregatorplugin.desktop
%_K5srv/akregator_*.desktop
%_K5srv/feed.protocol
%_K5icon/*/*/apps/akregator*.*
%doc %_K5doc/en/akregator/

%files blogilo
%_K5bin/blogilo
%_K5xdgapp/org.kde.blogilo.desktop
#%_K5xmlgui/blogilo/
%_K5cf_upd/*blogilo*
%_K5icon/*/*/apps/blogilo.*
%doc %_K5doc/en/blogilo/

%files kaddressbook
%_K5bin/kaddressbook
%dir %_K5lib/akonadi5/contact/
%dir %_K5lib/akonadi5/contact/editorpageplugins/
%_K5lib/akonadi5/contact/editorpageplugins/cryptopageplugin.so
%_K5plug/kaddressbookpart.so
%_K5plug/kontact_kaddressbookplugin.so
%_K5xdgapp/kaddressbook-importer.desktop
%_K5xdgapp/org.kde.kaddressbook.desktop
%_K5cf_upd/*kaddressbook*
%_K5data/kaddressbook/
%_K5xmlgui/kaddressbook/
%_K5srv/kontact/kaddressbookplugin.desktop
%_K5srv/kaddressbookpart.desktop
%_K5icon/*/*/apps/kaddressbook.*
#
%dir %_K5plug/grantlee/
%dir %_K5plug/grantlee/5.?/
%_libdir/grantlee/5.?/*grantlee_*.so
#
%_K5bin/contactprintthemeeditor
%_K5xdgapp/org.kde.contactprintthemeeditor.desktop
#%_K5xmlgui/contactprintthemeeditor/
#
%_K5bin/contactthemeeditor
%_K5xdgapp/org.kde.contactthemeeditor.desktop
#%_K5xmlgui/contactthemeeditor/
%doc %_K5doc/en/contactthemeeditor/
#
%_K5xdgapp/org.kde.headerthemeeditor.desktop
%_K5bin/headerthemeeditor
#%_K5xmlgui/headerthemeeditor/
%doc %_K5doc/en/headerthemeeditor/

%files kalarm
%config(noreplace) %_K5conf_dbus_sysd/org.kde5.kalarmrtcwake.conf
%_K5bin/kalarm
%_K5bin/kalarmautostart
%_K5libexecdir/kauth/kalarm_helper
%_K5start/kalarm.autostart.desktop
%_K5xdgapp/org.kde.kalarm.desktop
%_K5cf_upd/*kalarm*
%_K5data/kalarm/
%_K5xmlgui/kalarm/
%_K5icon/*/*/apps/kalarm.*
%doc %_K5doc/en/kalarm/
%_K5dbus_sys_srv/org.kde5.kalarmrtcwake.service
%_datadir/polkit-1/actions/org.kde5.kalarmrtcwake.policy

%files kleopatra
%_K5bin/kleopatra
%_K5xdgapp/org.kde.kleopatra.desktop
%_K5xdgapp/kleopatra_import.desktop
%_K5data/kleopatra/
%_K5cf_upd/*kleopatra*
%_K5plug/kcm_kleopatra.so
#%_K5xmlgui/kleopatra/
%_K5srv/kleopatra_*.desktop
%_K5icon/*/*/apps/kleopatra.*
%doc %_K5doc/en/kleopatra/
#
%_K5bin/kwatchgnupg
#%_K5bin/kgpgconf
%_K5data/kwatchgnupg/
#%_K5xmlgui/kwatchgnupg/
%doc %_K5doc/en/kwatchgnupg/

%files kmail
%_K5bin/kmail
%_K5plug/kmailpart.so
%_K5plug/messageviewer_*.so
%_K5plug/kcm_kmail.so
%_K5plug/kcm_kmailsummary.so
%_K5plug/kontact_kmailplugin.so
%_K5plug/kcm_kpimidentities.so
%_K5plug/grantlee/*
%_K5xdgapp/org.kde.kmail.desktop
%_K5xdgapp/kmail_view.desktop
%_K5data/kmail2/
%_K5cf_upd/*kmail*
%_K5cf_upd/messageviewer.upd
%_K5data/messagelist/
%_K5data/messageviewer/
%_K5xmlgui/kmail2/
%_K5srv/kmail_*.desktop
%_K5srv/kontact/kmailplugin.desktop
%_K5srv/ServiceMenus/kmail_*.desktop
%_K5srv/kcm_kpimidentities.desktop
%_K5srv/kcmkmailsummary.desktop
%_K5icon/*/*/apps/kmail.*
%_K5notif/kmail2.notifyrc
%doc %_K5doc/en/kmail/
#
%_K5bin/ktnef
%_K5xdgapp/org.kde.ktnef.desktop
#%_K5xmlgui/ktnef/
%_K5icon/*/*/apps/ktnef.*
%doc %_K5doc/en/ktnef/

%files knotes
%_K5bin/knotes
%_K5plug/kcm_knote.so
%_K5plug/kcm_knotessummary.so
%_K5plug/kontact_knotesplugin.so
%_K5xdgapp/org.kde.knotes.desktop
%_K5data/knotes/
%_K5cf_upd/*knotes*
%_K5xmlgui/knotes/
%_K5srv/knote_*.desktop
%_K5srv/kontact/knotesplugin.desktop
%_K5srv/kcmknotessummary.desktop
%_K5icon/*/*/apps/knotes.*
%doc %_K5doc/en/knotes

%files kontact
%_K5bin/kontact
%_K5plug/kcm_kontact.so
%_K5plug/kcm_kontactsummary.so
%_K5plug/kontact_summaryplugin.so
%_K5xdgapp/kontact-admin.desktop
%_K5xdgapp/org.kde.kontact.desktop
%_K5data/kontact/
%_K5cf_upd/*kontact*
%_K5xmlgui/kontact/
%_K5xmlgui/kontactsummary/
%dir %_K5srv/kontact/
%_K5srv/kontactconfig.desktop
%_K5srv/kcmkontactsummary.desktop
%_K5icon/*/*/apps/kontact.*
%_K5icon/*/*/apps/kontact-import-wizard.*
%doc %_K5doc/en/kontact
%doc %_K5doc/en/kontact-admin

%files korganizer
%_K5bin/korgac
%_K5bin/korganizer
%_K5bin/ical2vcal
%_K5plug/korganizerpart.so
%_K5plug/kcm_apptsummary.so
%_K5plug/kcm_korganizer.so
%_K5plug/kcm_todosummary.so
%_K5plug/kcm_sdsummary.so
%_K5plug/kontact_korganizerplugin.so
%_K5plug/kontact_journalplugin.so
%_K5plug/kontact_todoplugin.so
%_K5plug/kontact_specialdatesplugin.so
%_K5plug/korg_datenums.so
%_K5plug/korg_hebrew.so
%_K5plug/korg_picoftheday.so
%_K5plug/korg_thisdayinhistory.so
%_K5start/org.kde.korgac.desktop
%_K5xdgapp/korganizer-import.desktop
%_K5xdgapp/org.kde.korganizer.desktop
%_K5data/korgac/
%_K5data/korganizer/
%_K5cf_upd/*korganizer*
%_K5xmlgui/korganizer/
%_K5srv/kontact/korganizerplugin.desktop
%_K5srv/korganizer/
%_K5srv/korganizer_*.desktop
%_K5srv/webcal.protocol
%_K5srv/kcmapptsummary.desktop
%_K5srv/kcmsdsummary.desktop
%_K5srv/kcmtodosummary.desktop
%_K5srv/kontact/journalplugin.desktop
%_K5srv/kontact/specialdatesplugin.desktop
%_K5srv/kontact/summaryplugin.desktop
%_K5srv/kontact/todoplugin.desktop
%_K5icon/*/*/apps/korganizer.*
%_K5icon/*/*/apps/korg-*.*
%_K5icon/*/*/apps/quickview.*
%doc %_K5doc/en/korganizer

%files devel
#%_K5inc/kdepim_version.h
#%_K5inc/kdepim/
%_K5link/lib*.so
#%_K5lib/cmake/kdepim
#%_K5archdata/mkspecs/modules/qt_kdepim.pri
%_K5dbus_iface/*.xml
%_K5plug/designer/*

%files -n %libakregatorinterfaces
%_K5lib/libakregatorinterfaces.so.%pim_sover
%_K5lib/libakregatorinterfaces.so.*
%files -n %libakregatorprivate
%_K5lib/libakregatorprivate.so.%pim_sover
%_K5lib/libakregatorprivate.so.*
%files -n %libkf5calendarsupport
%_K5lib/libKF5CalendarSupport.so.%pim_sover
%_K5lib/libKF5CalendarSupport.so.*
#%files -n %libkf5calendarsupportcollectionpage
#%_K5lib/libKF5CalendarSupportcollectionpage.so.%pim_sover
#%_K5lib/libKF5CalendarSupportcollectionpage.so.*
%files -n %libkf5composereditorng
%_K5lib/libKF5ComposerEditorNG.so.%pim_sover
%_K5lib/libKF5ComposerEditorNG.so.*
%_K5data/composereditor/
%files -n %libkf5eventviews
%_K5lib/libKF5EventViews.so.%pim_sover
%_K5lib/libKF5EventViews.so.*
%files -n %libkf5followupreminder
%_K5lib/libKF5FollowupReminder.so.%pim_sover
%_K5lib/libKF5FollowupReminder.so.*
%files -n %libgrantleethemeeditor
%_K5lib/libgrantleethemeeditor.so.%pim_sover
%_K5lib/libgrantleethemeeditor.so.*
%files -n %libkf5grantleetheme
%_K5lib/libKF5GrantleeTheme.so.%pim_sover
%_K5lib/libKF5GrantleeTheme.so.*
#%files -n %libincidenceeditorsngmobile
#%_K5lib/libincidenceeditorsngmobile.so.%pim_sover
#%_K5lib/libincidenceeditorsngmobile.so.*
%files -n %libkf5incidenceeditorsng
%_K5lib/libKF5IncidenceEditorsng.so.%pim_sover
%_K5lib/libKF5IncidenceEditorsng.so.*
%files -n %libkf5kaddressbookgrantlee
%_K5lib/libKF5KaddressbookGrantlee.so.%pim_sover
%_K5lib/libKF5KaddressbookGrantlee.so.*
%files -n %libkaddressbookprivate
%_K5lib/libkaddressbookprivate.so.%pim_sover
%_K5lib/libkaddressbookprivate.so.*
%files -n %libkf5libkdepim
%_K5lib/libKF5Libkdepim.so.%pim_sover
%_K5lib/libKF5Libkdepim.so.*
%_K5plug/kcm_ldap.so
%_K5srv/kcmldap.desktop
%files -n %libkf5kdepimdbusinterfaces
%_K5lib/libKF5KdepimDBusInterfaces.so.%pim_sover
%_K5lib/libKF5KdepimDBusInterfaces.so.*
%_K5data/kdepimwidgets/
%files -n %libkf5kdgantt2
%_K5lib/libKF5KDGantt2.so.%pim_sover
%_K5lib/libKF5KDGantt2.so.*
%files -n %libkleopatraclientcore
%_K5lib/libkleopatraclientcore.so.%kleopatraclientcore_sover
%_K5lib/libkleopatraclientcore.so.*
%_K5data/libkleopatra/
%files -n %libkleopatraclientgui
%_K5lib/libkleopatraclientgui.so.%kleopatraclientgui_sover
%_K5lib/libkleopatraclientgui.so.*
%files -n %libkf5libkleo
%_K5lib/libKF5Libkleo.so.%pim_sover
%_K5lib/libKF5Libkleo.so.*
%files -n %libkmailprivate
%_K5lib/libkmailprivate.so.%pim_sover
%_K5lib/libkmailprivate.so.*
%files -n %libkf5kmanagesieve
%_K5lib/libKF5KManageSieve.so.%pim_sover
%_K5lib/libKF5KManageSieve.so.*
%files -n %libknotesprivate
%_K5lib/libknotesprivate.so.%pim_sover
%_K5lib/libknotesprivate.so.*
%files -n %libkontactprivate
%_K5lib/libkontactprivate.so.%pim_sover
%_K5lib/libkontactprivate.so.*
%files -n %libkorganizer_core
%_K5lib/libkorganizer_core.so.%pim_sover
%_K5lib/libkorganizer_core.so.*
%files -n %libkorganizer_interfaces
%_K5lib/libkorganizer_interfaces.so.%pim_sover
%_K5lib/libkorganizer_interfaces.so.*
%files -n %libkorganizerprivate
%_K5lib/libkorganizerprivate.so.%pim_sover
%_K5lib/libkorganizerprivate.so.*
#%files -n %libkpgp
#%_K5lib/libkpgp.so.%pim_sover
#%_K5lib/libkpgp.so.*
%files -n %libkf5ksieve
%_K5lib/libKF5KSieve.so.%pim_sover
%_K5lib/libKF5KSieve.so.*
%files -n %libkf5ksieveui
%_K5lib/libKF5KSieveUi.so.%pim_sover
%_K5lib/libKF5KSieveUi.so.*
%files -n %libkf5mailcommon
%_K5lib/libKF5MailCommon.so.%pim_sover
%_K5lib/libKF5MailCommon.so.*
%files -n %libkf5mailimporter
%_K5lib/libKF5MailImporter.so.%pim_sover
%_K5lib/libKF5MailImporter.so.*
%files -n %libkf5messagecomposer
%_K5lib/libKF5MessageComposer.so.%pim_sover
%_K5lib/libKF5MessageComposer.so.*
%files -n %libkf5messagecore
%_K5lib/libKF5MessageCore.so.%pim_sover
%_K5lib/libKF5MessageCore.so.*
%files -n %libkf5messagelist
%_K5lib/libKF5MessageList.so.%pim_sover
%_K5lib/libKF5MessageList.so.*
%files -n %libkf5messageviewer
%_K5lib/libKF5MessageViewer.so.%pim_sover
%_K5lib/libKF5MessageViewer.so.*
%dir %_K5plug/messageviewer/
%_K5plug/messageviewer/messageviewer_*.so
%_K5data/libmessageviewer/
%_K5notif/messageviewer.notifyrc
%files -n %libkf5noteshared
%_K5lib/libKF5NoteShared.so.%pim_sover
%_K5lib/libKF5NoteShared.so.*
%files -n %libkf5pimcommon
%_K5lib/libKF5PimCommon.so.%pim_sover
%_K5lib/libKF5PimCommon.so.*
%dir %_K5plug/pimcommon/
%_K5plug/pimcommon/pimcommon_*.so
%files -n %libpimsettingexporterprivate
%_K5lib/libpimsettingexporterprivate.so.%pim_sover
%_K5lib/libpimsettingexporterprivate.so.*
%files -n %libkf5sendlater
%_K5lib/libKF5SendLater.so.%pim_sover
%_K5lib/libKF5SendLater.so.*
%files -n %libkf5templateparser
%_K5lib/libKF5TemplateParser.so.%pim_sover
%_K5lib/libKF5TemplateParser.so.*
%files -n %libkf5gravatar
%_K5lib/libKF5Gravatar.so.%pim_sover
%_K5lib/libKF5Gravatar.so.*

%changelog
* Thu Feb 25 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Mon Dec 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Mon Oct 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt2
- build without qt5-speech

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt3
- fix requires

* Wed Sep 09 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt2
- move akonadi resources to alternate place

* Fri Aug 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Fri Aug 07 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.80-alt1
- initial build
