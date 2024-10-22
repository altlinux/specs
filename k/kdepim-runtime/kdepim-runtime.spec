%define rname kdepim-runtime

%define pim_sover 6
%define libmaildir libmaildir%pim_sover
%define libfolderarchivesettings libfolderarchivesettings%pim_sover
%define libakonadi_filestore libakonadi-filestore%pim_sover
%define libkmindexreader libkmindexreader%pim_sover
%define libakonadi_singlefileresource libakonadi-singlefileresource%pim_sover
%define libnewmailnotifier libnewmailnotifier%pim_sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

ExcludeArch: %not_qt6_qtwebengine_arches

Group: Graphical desktop/KDE
Summary: Akonadi resources
Url: http://www.kde.org
License: LGPL-2.0-or-later

Provides: kde5-pim-runtime = %EVR
Obsoletes: kde5-pim-runtime < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: qt6-webengine-devel
BuildRequires: qt6-speech-devel qt6-networkauth-devel
BuildRequires: libqca-qt6-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: xsltproc libsasl2-devel boost-devel
BuildRequires: kf6-kdav-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel  kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel
BuildRequires: kf6-knotifyconfig-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwallet-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-kcalendarcore-devel kf6-kcontacts-devel kf6-kholidays-devel kf6-ktexttemplate-devel
BuildRequires: akonadi-calendar-devel kcalutils-devel
BuildRequires: kidentitymanagement-devel kimap-devel kmailtransport-devel kmbox-devel kmime-devel kpimtextedit-devel
BuildRequires: akonadi-devel akonadi-mime-devel akonadi-contacts-devel akonadi-notes-devel pimcommon-devel
BuildRequires: kde6-libkgapi-devel kde6-libkdepim-devel kldap-devel grantleetheme-devel

%description
This package contains the Akonadi resources which can be used without the applications in kdepim.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-pim-runtime-common = %EVR
Obsoletes: kde5-pim-runtime-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libmaildir
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libmaildir5 < %EVR
%description -n %libmaildir
%name library

%package -n %libfolderarchivesettings
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libfolderarchivesettings5 < %EVR
%description -n %libfolderarchivesettings
%name library

%package -n %libakonadi_filestore
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libakonadi_filestore
%name library

%package -n %libkmindexreader
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkmindexreader5 < %EVR
%description -n %libkmindexreader
%name library

%package -n %libnewmailnotifier
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libnewmailnotifier
%name library

%package -n %libakonadi_singlefileresource
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libakonadi_singlefileresource
%name library

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
# workaround against sasl plugins dir
#for sffx in 3 4 5 6 ; do
#    mkdir -p  %buildroot/%_libdir/sasl2-$sffx
#    for f in %buildroot/%_libdir/sasl2/*.so* ; do
#	fname=`basename "$f"`
#	ln -s ../sasl2/"$fname" %buildroot/%_libdir/sasl2-$sffx/"$fname"
#    done
#done

%find_lang %name --with-kde --all-name

mv %buildroot/%_K6xdgmime/kdepim{,5}-mime.xml

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_K6xdgmime/kdepim5-mime.xml

%files
%_K6bin/gidmigrator
%_K6bin/akonadi_*
%_K6plug/pim6/akonadi/config/*.so
%_K6plug/pim6/kcms/kaddressbook/*.so
%_K6plug/pim6/mailtransport/*.so
%_K6plug/kf6/kio/*.so
%_K6xdgapp/org.kde.akonadi*.desktop
%_datadir/akonadi/agents/*
%_datadir/akonadi/firstrun/*
%_datadir/akonadi/davgroupware-providers/
%_K6icon/*/*/apps/*.*
%_K6notif/akonadi_*

%files devel
#%_K6link/lib*.so
%_K6dbus_iface/*.xml

%files -n %libmaildir
%_K6lib/libmaildir.so.%pim_sover
%_K6lib/libmaildir.so.*
%files -n %libnewmailnotifier
%_K6lib/libnewmailnotifier.so.%pim_sover
%_K6lib/libnewmailnotifier.so.*
%files -n %libfolderarchivesettings
%_K6lib/libfolderarchivesettings.so.%pim_sover
%_K6lib/libfolderarchivesettings.so.*
%files -n %libakonadi_filestore
%_K6lib/libakonadi-filestore.so.%pim_sover
%_K6lib/libakonadi-filestore.so.*
%files -n %libkmindexreader
%_K6lib/libkmindexreader.so.%pim_sover
%_K6lib/libkmindexreader.so.*
%files -n %libakonadi_singlefileresource
%_K6lib/libakonadi-singlefileresource.so.%pim_sover
%_K6lib/libakonadi-singlefileresource.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

