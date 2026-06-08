%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%add_findreq_skiplist %_K6data/lokalize/scripts/*.py
%add_findreq_skiplist %_K6data/lokalize/scripts/*/*.py
%add_findprov_skiplist %_K6data/lokalize/scripts/*.py
%add_findprov_skiplist %_K6data/lokalize/scripts/*/*.py
%add_python3_path %_K6data/lokalize

%define rname lokalize
Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Development/Tools
Summary: Computer-aided translation system
Url: http://www.kde.org
License: BSD-3-Clause AND GFDL-1.2-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-or-later

Provides: kde5-lokalize = %EVR
Obsoletes: kde5-lokalize < %EVR
#Requires: kross-python python3-module-PyQt6

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: rpm-build-python3
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libhunspell-devel desktop-file-utils
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel
BuildRequires: kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel kf6-kcrash-devel

%description
Lokalize is the localization tool for KDE and other open source software.


%prep
%setup -n %rname-%version
sed -i 's|\(.*FIND_LIBRARY.*HUNSPELL_LIBRARIES.*NAMES\)|\1 hunspell|' cmake/FindHUNSPELL.cmake

%build
%K6build

%install
%K6install
%K6install_move data lokalize
%find_lang %name --with-kde --all-name

# fix menu file
desktop-file-install --mode=0755 --dir %buildroot/%_K6xdgapp \
    --remove-category=Office \
    %buildroot/%_K6xdgapp/org.kde.lokalize.desktop

%files -f %name.lang
%doc LICENSES/*
%_K6bin/lokalize
%_K6data/lokalize/
%_K6xdgapp/org.kde.lokalize.desktop
%_K6cfg/lokalize*
%_K6icon/*/*/apps/*lokalize.*
%_K6notif/lokalize*
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*lokalize*.xml


%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Fri Jul 25 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed Jun 11 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Thu Mar 06 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Wed Jan 29 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

