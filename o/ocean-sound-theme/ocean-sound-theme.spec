%define rname ocean-sound-theme

Name: ocean-sound-theme
Version: 6.7.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Ocean Sound Theme
Url: https://invent.kde.org/plasma/%rname
License: CC0-1.0 AND BSD-2-Clause AND CC-BY-SA-4.0

BuildArch: noarch

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel

%description
%{summary}.

%package -n sound-theme-ocean
Group: Graphical desktop/Other
Summary: %{summary}
Requires: kde-common
Provides: ocean-sound-theme = %EVR
Obsoletes: ocean-sound-theme < %EVR
%description -n sound-theme-ocean
%{summary}.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data sounds

%files -n sound-theme-ocean
%doc LICENSES/*
%_K6snd/*

%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Wed Jul 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- initial build
