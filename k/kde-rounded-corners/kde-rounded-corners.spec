%define _unpackaged_files_terminate_build 1

Name: kde-rounded-corners
Version: 0.9.0
Release: alt1
%K6init no_altplace

Summary: Rounds the corners of your windows in KDE Plasma
License: GPL-3.0-only
Group: Graphical desktop/KDE
Url: https://github.com/matinlotfali/KDE-Rounded-Corners
Vcs: https://github.com/matinlotfali/KDE-Rounded-Corners.git

Provides: kde5-rounded-corners = %EVR
Obsoletes: kde5-rounded-corners < %EVR

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: libvulkan-devel
BuildRequires: extra-cmake-modules
BuildRequires: kwin-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kcmutils-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: qt6-declarative-devel

%description
%summary.

%prep
%setup

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSE README.*
%_K6data/kwin/shaders/shapecorners*.frag
%_K6plug/kwin/effects/configs/kwin_shapecorners_config.so
%_K6plug/kwin/effects/plugins/kwin4_effect_shapecorners.so

%changelog
* Thu Jul 02 2026 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- New version.

* Mon Apr 06 2026 Sergey V Turchin <zerg@altlinux.org> 0.8.7-alt1
- New version.

* Thu Dec 18 2025 Anton Kurachenko <srebrov@altlinux.org> 0.8.6-alt1
- New version 0.8.6.

* Mon Sep 29 2025 Anton Kurachenko <srebrov@altlinux.org> 0.8.5-alt1
- New version 0.8.5.

* Sat Aug 23 2025 Anton Kurachenko <srebrov@altlinux.org> 0.8.1-alt1
- New version 0.8.1.

* Sat May 03 2025 Anton Kurachenko <srebrov@altlinux.org> 0.7.2-alt1
- New version 0.7.2.

* Sun Feb 02 2025 Anton Kurachenko <srebrov@altlinux.org> 0.7.1-alt1
- New version 0.7.1.

* Fri Jan 24 2025 Anton Kurachenko <srebrov@altlinux.org> 0.7.0-alt2
- Added RU translation.

* Sun Jan 19 2025 Anton Kurachenko <srebrov@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Sun Sep 15 2024 Anton Kurachenko <srebrov@altlinux.org> 0.6.7-alt2
- Build for KF6.

* Thu Jul 4 2024 Anton Kurachenko <srebrov@altlinux.org> 0.6.7-alt1
- Initial build for Sisyphus.
