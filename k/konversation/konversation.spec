
%define rname konversation
Name: %rname
Version: 24.08.1
Release: alt1
%define beta %nil
%K6init no_altplace

AutoReq: yes, nopython
%add_python3_path %_datadir/%rname
%add_findreq_skiplist %_datadir/%rname/scripts/bug

Group: Networking/IRC
Summary: Konversation is a user friendly Internet Relay Chat client.
License: GPL-2.0-or-later
Url: http://konversation.kde.org

Requires: qca-qt6-ossl qt6-dbus
Requires: kde-runtime
Provides: kde5-konversation = %EVR
Obsoletes: kde5-konversation < %EVR

Source0: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-build-python3
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-tools-devel qt6-multimedia-devel qt6-5compat-devel qt6-dbus
BuildRequires: libqca-qt6-devel qt6-phonon-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kdoctools kf6-kdoctools-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-kglobalaccel-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kidletime-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-knotifyconfig-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwallet-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel kf6-kcrash-devel
BuildRequires: kf6-knewstuff-devel

%description
Konversation is a simple and easy-to-use IRC client for KDE with support for 
SSL connections, strikeout, multi-channel joins, away/unaway messages, 
ignore list functionality, full Unicode support, the ability to auto-connect 
to a server, optional timestamps in chat windows, configurable background colors, 
and much more. 

%prep
%setup -q -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang --with-kde %rname

# purge use of /usr/bin/env
sed -i \
  -e "s|^#!/usr/bin/env bash|#!/bin/bash|g" \
  -e "s|^#!/usr/bin/env perl|#!/usr/bin/perl|g" \
  -e "s|^#!/usr/bin/env python$|#!%{__python3}|g" \
  %buildroot/%_datadir/%rname/scripts/* \
  %buildroot/%_datadir/%rname/scripting_support/python/konversation/*.py

%files -f %rname.lang
%doc AUTHORS README ChangeLog
%doc LICENSES/*
%_K6bin/*
%_K6xdgapp/org.kde.%rname.desktop
%_K6icon/hicolor/*/*/*.*
%_datadir/qlogging-categories6/*.*categories
%_datadir/%rname/
%_datadir/knsrcfiles/konversation*.*
%_K6notif/*
%_K6dbus_srv/*.service
%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

