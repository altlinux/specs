%define rname plasma-phonebook

Name: %rname
Version: 26.08.3
Release: alt1

Group: Graphical desktop/KDE
Summary: Contacts application for Plasma Mobile
License: GPL-2.0-only OR GPL-3.0-only
Url: https://invent.kde.org/plasma-mobile/plasma-phonebook

Requires: qml6(Qt5Compat.GraphicalEffects)
Requires: kf6-kirigami libkf6peoplewidgets kf6-kirigami-addons

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-svg-devel
BuildRequires: kf6-kconfig-devel kf6-kcontacts-devel kf6-kcoreaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kirigami-devel kf6-kpeople-devel
BuildRequires: kf6-kirigami-addons-devel

%description
Plasma Phonebook is an application for viewing, adding, editing and
removing contacts on Plasma Mobile and the desktop. It uses KPeople
for contact integration and KContacts for vCard editing.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %rname --with-kde

%files -f %rname.lang
%doc README.md LICENSES/*
%_K6bin/plasma-phonebook
%_K6xdgapp/org.kde.phonebook.desktop
%_K6icon/hicolor/*/apps/*phonebook*
%_K6plug/kpeople/actions/*phonebook*.so
%_datadir/metainfo/*phonebook*

%changelog
* Mon Nov 09 2026 Sergey V Turchin <zerg@altlinux.org> 26.08.3-alt1
- initial build
