%define rname kpeoplevcard

%define sover 0
%define libkimageannotator libkimageannotator%sover

Name: kde5-%rname
Version: 0.6.1
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: Expose VCard contacts to KPeople
Url: https://invent.kde.org/pim/kpeoplevcard
License: LGPL-2.1-or-later

Requires: %name-common

Source: %rname-%version.tar
Patch1: alt-i18n.patch


# Automatically added by buildreq on Fri Mar 15 2024 (-bi)
# optimized out: bash5 cmake cmake-modules debugedit elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libdouble-conversion3 libglvnd-devel libgpg-error libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-test libqt5-widgets libqt5-xml libsasl2-3 libssl-devel libstdc++-devel python3 python3-base python3-dev python3-module-setuptools qt5-base-devel rpm-build-file rpm-build-python3 sh5 tzdata
#BuildRequires: appstream extra-cmake-modules kf5-kcodecs-devel kf5-kconfig-devel kf5-kcontacts-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kpeople-devel python3-module-mpl_toolkits qt5-imageformats qt5-svg-devel qt5-virtualkeyboard-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: kf5-kcodecs-devel kf5-kconfig-devel kf5-kcontacts-devel kf5-kcoreaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kpeople-devel

%description
%summary

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
Requires: %name-common
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup -n %rname-%version
%patch1 -p1


%build
%K5build

%install
%K5install
%find_lang %name --all-name --with-qt

%files common -f %name.lang
%doc COPYING
# LICENSES/*

%files
%_K5plug/kpeople/datasource/KPeopleVCard.so

%files devel
%_libdir/cmake/KF5PeopleVCard/

%changelog
* Fri Mar 15 2024 Sergey V Turchin <zerg@altlinux.org> 0.6.1-alt1
- initial build
