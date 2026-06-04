
%define rname skanpage

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphics
Summary: Multi-page scanning application
Url: http://www.kde.org
License:  GPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides:  kde5-skanpage = %EVR
Obsoletes: kde5-skanpage < %EVR

Requires: qt6-imageformats kde6-kquickimageeditor

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
# libqt6-pdf from qt6-webengine
BuildRequires: qt6-webengine-devel
BuildRequires: libgomp-devel libleptonica-devel tesseract-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-ki18n-devel kf6-kirigami-devel
BuildRequires: kf6-purpose-devel kf6-kxmlgui-devel kf6-kcolorscheme-devel kf6-kio-devel
BuildRequires: ksanecore-devel
BuildRequires: kde6-kquickimageeditor-devel

%description
Skanpage is a multi-page scanning application built using the libksane library and a QML interface.
It supports saving to image and PDF files.

%prep
%setup -n %rname-%version

sed -i 's|#include <KSaneCore/|#include <KSaneCore6/|' src/*.{h,cpp}

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/skanpage
%_K6xdgapp/*skanpage*.desktop
%_K6icon/hicolor/*/apps/*skanpage*
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml


%changelog
* Thu Jun 04 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Fri May 08 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
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

