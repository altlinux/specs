
%define sover 0
%define libsmb4kcore libsmb4kcore%sover
%define libsmb4kdialogs libsmb4kdialogs%sover

%define rname smb4k
Name: %rname
Version: 3.2.90
Release: alt1
%K6init

Group: Networking/Other
Summary: A KDE SMB/CIFS share browser
License: GPL-2.0-or-later
Url: http://smb4k.sourceforge.net/

Requires: %libsmb4kcore
Requires: samba-client cifs-utils
Provides:  kde5-smb4k = %EVR
Obsoletes: kde5-smb4k < %EVR

Source: %name-%version.tar
Patch1: alt-soname.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libsmbclient-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kdoctools-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-knotifications-devel kf6-kpackage-devel kf6-kparts-devel kf6-ktextwidgets-devel kf6-kwallet-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kcrash-devel kf6-kdnssd-devel kf6-kirigami-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: plasma6-lib-devel

%description
Smb4K is an SMB/CIFS share browser for KDE. It uses the Samba software suite to
access the SMB/CIFS shares of the local network neighborhood. Its purpose is to
provide a program that's easy to use and has as many features as possible.

%package -n %libsmb4kcore
Summary: %name library
Group: System/Libraries
%description -n %libsmb4kcore
%name library.

%package -n %libsmb4kdialogs
Summary: %name library
Group: System/Libraries
%description -n %libsmb4kdialogs
%name library.


%prep
%setup -q
%patch1 -p1

%build
%K6build

%install
%K6install
%K6install_move data kconf_update
%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K6bin/*
%_K6plug/*.so
%_K6exec/kauth/mounthelper
%_K6qml/org/kde/smb4k/
%_K6xdgapp/*smb4k*.desktop
%_K6data/plasma/plasmoids/*smb4k*/
%_K6cfg/smb4k.kcfg
%_K6icon/*/*/apps/*.*
%_K6dbus/system.d/*smb4k*.conf
%_K6dbus_sys_srv/*smb4k*.service
%_K6notif/smb4k.*
%_datadir/polkit-1/actions/*smb4k*.policy
%_datadir/metainfo/*.xml

%files -n %libsmb4kcore
%_K6lib/libsmb4kcore.so.%sover
%_K6lib/libsmb4kcore.so.*
%files -n %libsmb4kdialogs
%_K6lib/libsmb4kdialogs.so.%sover
%_K6lib/libsmb4kdialogs.so.*

%changelog
* Tue Nov 05 2024 Sergey V Turchin <zerg@altlinux.org> 3.2.90-alt1
- inittial build
