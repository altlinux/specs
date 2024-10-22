%define rname kdenetwork-filesharing
%define req_samba_pkgs samba,samba-common-tools,samba-client,samba-usershares

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Samba Filesharing Plugin
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-network-filesharing = %EVR
Obsoletes: kde5-network-filesharing < %EVR

#Requires: %req_samba_pkgs
Requires: /usr/bin/testparm

Source: %rname-%version.tar
Source10: ru-add.po
Patch1: alt-allow-guest.patch
Patch2: alt-uid-min-max.patch
Patch3: alt-i18n.patch
Patch4: alt-max-domain-uid.patch
Patch5: alt-share-under-domain-user.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: packagekit-qt6-devel
BuildRequires: qcoro6-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel kf6-kdeclarative-devel
BuildRequires: kf6-kpackage-devel

%description
Adds Configuration of Samba sharing for folders in Dolphin.

%prep
%setup -n %rname-%version
#%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .i18n
%patch4 -p1
%patch5 -p1

mv po/ru/kfileshare.po{,.old}
msgcat --use-first po/ru/kfileshare.po.old %SOURCE10 > po/ru/kfileshare.po
rm -f po/ru/kfileshare.po.old

%build
%K6build \
    -DSAMBA_INSTALL=ON \
    -DSAMBA_PACKAGE_NAME=\"%req_samba_pkgs\" \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6plug/kf6/propertiesdialog/*amba*.so
#
%_K6dbus_sys_srv/org.kde.filesharing.samba.service
%_K6exec/kauth/authhelper
%_K6dbus/system.d/org.kde.filesharing.samba.conf
%_datadir/polkit-1/actions/org.kde.filesharing.samba.policy
%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

