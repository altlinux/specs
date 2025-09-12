%define nameB kjournaldbrowser
%define nameL org.kde.kjournaldbrowser

Name: kjournald
Version: 25.08.1
Release: alt1

Summary: Framework for interacting with systemd-journald
License: CC0-1.0 and MIT and BSD-3-Clause and LGPL-2.1-or-later
Group: Graphical desktop/KDE

Url: https://apps.kde.org/ru/kjournaldbrowser
Vcs: https://invent.kde.org/system/kjournald

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules qt6-base-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kcrash-devel kf6-ki18n-devel pkgconfig(Qt6Qml) libsystemd-devel
BuildRequires: kf6-kconfig-devel kf6-kirigami-devel kf6-kirigami-addons-devel

%description
%summary

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
%_bindir/%nameB
%_libdir/*.so.*
%_libdir/*.so.*
%_libdir/qt6/qml/org/kde/%name
%_datadir/applications/%nameL.desktop
%_datadir/metainfo/%nameL.appdata.xml
%_datadir/qlogging-categories6/%name.categories

%changelog
* Fri Sep 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.08.1-alt1
- 25.08.0 -> 25.08.1

* Fri Aug 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.08.0-alt1
- 25.07.70 -> 25.08.0

* Mon Apr 28 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.07.70-alt1
- Initial build for ALT Linux (git.60ace7dc).
