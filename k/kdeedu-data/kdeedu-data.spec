%define rname kdeedu-data

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Common KDE EDU data
Url: http://www.kde.org
License: GPL-2.0-only

Requires: kde-common
Provides:  kde5-kdeedu-data = %EVR
Obsoletes: kde5-kdeedu-data < %EVR

BuildArch: noarch

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6

BuildRequires: extra-cmake-modules qt6-declarative-devel kf6-ki18n-devel

%description
%summary

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data apps

%files
%doc COPYING*
%_K6data/apps/kvtml/
%_K6icon/*/*/actions/*.*


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

