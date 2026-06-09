%define rname kiten

%define soname 6
%define libkiten libkiten%soname

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Japanese reference/learning tool
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kiten = %EVR
Obsoletes: kde5-kiten < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-wayland-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-karchive-devel kf6-kcrash-devel kf6-kdoctools-devel
BuildRequires: kf6-kio-devel kf6-knotifications-devel kf6-kparts-devel kf6-ktextwidgets-devel

%description
Kiten is a Japanese reference/learning tool with features:
    * Search with english keyword, Japanese reading, or a Kanji string on a list of EDICT files.
    * Search with english keyword, Japanese reading, number of strokes, grade number, or a Kanji on a list of KANJIDIC files.
    * Comes with all necessary files.
    * Very fast.
    * Limit searches to only common entries.
    * Nested searches of results possible.
    * Compact, small, fast interface.
    * Global KDE keybindings for searching highlighted strings.
    * Learning dialog. (One can even open up multiple ones and have them sync between each other.)
    * Browse Kanji by grade.
    * Add Kanji to a list for later learning.
    * Browse list, and get quizzed on them.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-kiten-common = %EVR
Obsoletes: kde5-kiten-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkiten
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkiten5 < %EVR
%description -n %libkiten
%name library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data kiten

# cleanup
rm -rf %buildroot/%_datadir/fonts/ ||:

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6bin/kiten*
%_K6data/kiten/
%_K6icon/*/*/apps/kiten.*
%_K6xdgapp/org.kde.kiten*.desktop
%_K6cfg/kiten*
%_datadir/metainfo/*.xml

%files devel
%_K6inc/libkiten/
%_K6link/lib*.so

%files -n %libkiten
%_K6lib/libkiten.so.%soname
%_K6lib/libkiten.so.*


%changelog
* Tue Jun 09 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Tue Mar 10 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Oct 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Jul 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed May 28 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Mon Feb 24 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

