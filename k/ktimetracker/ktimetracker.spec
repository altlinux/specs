%define nameL org.kde.ktimetracker

Name: ktimetracker
Version: 6.0.0
Release: alt1

Summary: Todo management and time tracker
License: GPL-2.0-or-later and BSD-2-Clause and GPL-3.0-only and CC-BY-SA-4.0 and LGPL-3.0-only and GFDL-1.2-only
Group: Office

Url: https://apps.kde.org/ru/ktimetracker
Vcs: https://invent.kde.org/pim/ktimetracker

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules clang qt6-base-devel qt6-5compat-devel
BuildRequires: kf6-kconfig-devel kf6-kwidgetsaddons-devel kf6-kcoreaddons-devel 
BuildRequires: kf6-kdbusaddons-devel kf6-kdoctools-devel kf6-ki18n-devel 
BuildRequires: kf6-kidletime-devel kf6-kjobwidgets-devel kf6-kio-devel
BuildRequires: kf6-knotifications-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-kxmlgui-devel kf6-ktextwidgets-devel kf6-kcalendarcore-devel 
BuildRequires: kf6-kcmutils-devel kf6-kiconthemes-devel kf6-kcrash-devel
BuildRequires: qt6-declarative-devel

%description
KTimeTracker tracks time spent on various tasks. It is useful for tracking hours 
to be billed to different clients or just to find out what percentage of your day 
is spent playing Doom or reading Slashdot.

%prep
%setup

%build
%K6cmake
%K6make

%install
%K6install

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc *.md LICENSES
%_bindir/%name
%_datadir/applications/%nameL.desktop
%_datadir/dbus-1/interfaces/*.xml
%_iconsdir/hicolor/*/apps/%name.svg
%_iconsdir/breeze-dark/*/apps/%name.svg
%_datadir/metainfo/%nameL.appdata.xml

%changelog
* Thu Jul 31 2025 Aleksandr Shamaraev <shad@altlinux.org> 6.0.0-alt1
- Initial build for ALT Linux.
