%define rname kio-extras

%define kioarchive_sover 6
%define libkioarchive libkioarchive6_%kioarchive_sover

%def_enable exiv2

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 additional kio-slaves
Url: http://www.kde.org
License: LGPL-2.0-or-later

Requires: %name-common
Requires: kf6-kio
Provides: kde5-kio-extras = %EVR
Obsoletes: kde5-kio-extras < %EVR

# djvu thumbnailer
Requires: /usr/bin/ddjvu
# ico thumbnailer: /usr/bin/wrestool
# comic thumbnailer: /usr/bin/unrar

Source: %rname-%version.tar
Patch11: alt-smb-share.patch
Patch12: alt-fix-permissions.patch
Patch13: alt-find-samba.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-5compat-devel qt6-phonon-devel
BuildRequires: qcoro6-devel
%if_enabled exiv2
BuildRequires: libexiv2-devel
%endif
BuildRequires: libjpeg-devel libmtp-devel libopenslp-devel libsmbclient-devel libssh-devel openexr-devel
BuildRequires: libtirpc-devel
BuildRequires: libimobiledevice-devel
BuildRequires: gperf libtag-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdnssd-devel kf6-kdoctools kf6-kdoctools-devel kf6-kcmutils-devel
BuildRequires: kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel kf6-kpty-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-syntax-highlighting-devel
BuildRequires: plasma6-activities-devel plasma6-activities-stats-devel
BuildRequires: kde6-kdsoap-devel kde6-kdsoap-ws-discovery-client-devel
BuildRequires: kde6-libkexiv2-devel

%description
Additional kio-slaves.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkioarchive
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkioarchive5 < %EVR
%description -n %libkioarchive
%name library


%prep
%setup -n %rname-%version
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
%K6build \
    -DINCLUDE_INSTALL_DIR=%_K6inc \
    #

%install
%K6install

%K6install_move data kio_bookmarks kio_desktop kio_docfilter kio_info konqueror remoteview
%K6install_move data doc solid dbus-1/services

# workaround against man compressor
rm -rf %buildroot/%_K6doc/*/kioworker6/man

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_K6xdgmime/*.xml

%files
%_K6exec/smbnotifier
%_K6plug/kf6/*/*.so
%_K6plug/*.so
%_K6plug/plasma/kcms/systemsettings_qwidgets/kcm_*.so
%_K6xdgapp/kcm_*.desktop
%_K6data/kio_*/
%_K6data/konqueror
%_K6data/remoteview
%_K6data/solid/actions/*.desktop
%_K6cfg/*.kcfg
%_K6dbus_srv/*.service

%files devel
#%_K6inc/Kio*/
%_includedir/Kio*/
%_K6lib/cmake/Kio*/

%files -n %libkioarchive
%_K6lib/libkioarchive6.so.*
%_K6lib/libkioarchive6.so.%kioarchive_sover


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

