%define _unpackaged_files_terminate_build 1
%define nameB kjournaldbrowser
%define nameL org.kde.kjournaldbrowser

Name: kjournald
Version: 26.04.3
Release: alt1

Summary: Framework for interacting with systemd-journald
License: CC0-1.0 and MIT and BSD-3-Clause and LGPL-2.1-or-later and LGPL-3.0-or-later
Group: Graphical desktop/KDE

Url: https://apps.kde.org/ru/kjournaldbrowser
Vcs: https://invent.kde.org/system/kjournald

Source: %name-%version.tar

Requires: kf6-kconfig

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
%_libdir/qt?/qml/org/kde/%name
%_libdir/kf?/devel/*.so
%_datadir/applications/%nameL.desktop
%_datadir/metainfo/%nameL.appdata.xml
%_datadir/qlogging-categories?/%name.categories

%changelog
* Thu Jul 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 26.04.3-alt1
- 26.04.2 -> 26.04.3

* Thu Jun 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 26.04.2-alt1
- 26.04.1 -> 26.04.2

* Fri May 08 2026 Aleksandr Shamaraev <shad@altlinux.org> 26.04.1-alt1
- 26.04.0 -> 26.04.1
- changed license

* Fri Apr 17 2026 Aleksandr Shamaraev <shad@altlinux.org> 26.04.0-alt1
- 25.12.3 -> 26.04.0

* Fri Mar 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 25.12.3-alt1
- 25.12.2 -> 25.12.3

* Fri Feb 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 25.12.2-alt1
- 25.12.1 -> 25.12.2

* Fri Jan 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 25.12.1-alt1
- 25.12.0 -> 25.12.1

* Fri Dec 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.12.0-alt1
- 25.08.3 -> 25.12.0

* Fri Nov 07 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.08.3-alt1
- 25.08.2 -> 25.08.3

* Fri Oct 10 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.08.2-alt1
- 25.08.1 -> 25.08.2

* Fri Sep 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.08.1-alt1
- 25.08.0 -> 25.08.1

* Fri Aug 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.08.0-alt1
- 25.07.70 -> 25.08.0

* Mon Apr 28 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.07.70-alt1
- Initial build for ALT Linux (git.60ace7dc).
