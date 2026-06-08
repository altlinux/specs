%define rname kimagemapeditor

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Development/Other
Summary: An HTML imagemap editor
Url: http://www.kde.org
License: GPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides:  kde5-kimagemapeditor = %EVR
Obsoletes: kde5-kimagemapeditor < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules
BuildRequires: qt6-wayland-devel qt6-webengine-devel
BuildRequires: kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kdoctools-devel kf6-kguiaddons-devel
BuildRequires: kf6-kiconthemes-devel kf6-kio-devel kf6-kparts-devel kf6-ktextwidgets-devel

%description
An HTML imagemap editor.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kimagemapeditor
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K6bin/kimagemapeditor
%_K6plug/kf6/parts/*kimagemapeditor*.so
%_K6xdgapp/org.kde.kimagemapeditor.desktop
%_K6icon/*/*/actions/*.*
%_K6icon/*/*/apps/*kimagemapeditor.*
%_K6data/kimagemapeditor/
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*kimagemapeditor*.xml

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

