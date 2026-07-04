%define _unpackaged_files_terminate_build 1

Name: kde-rounded-corners-x11
Version: 0.9.0
Release: alt1
%K6init no_altplace

Summary: Rounds the corners of your windows in KDE Plasma (x11)
License: GPL-3.0-only
Group: Graphical desktop/KDE
Url: https://github.com/matinlotfali/KDE-Rounded-Corners
Vcs: https://github.com/matinlotfali/KDE-Rounded-Corners.git

Source: %name-%version.tar

# https://github.com/matinlotfali/KDE-Rounded-Corners/pull/432
Requires: kde-rounded-corners

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: kwin-devel
BuildRequires: kwin-x11-devel
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
%K6build -DKWIN_X11=ON

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSE README.*
%_K6plug/kwin-x11/effects/configs/kwin_shapecorners_config.so
%_K6plug/kwin-x11/effects/plugins/kwin4_effect_shapecorners.so
%exclude %_K6data/kwin/shaders/shapecorners*.frag

%changelog
* Sat Jul 04 2026 Anton Kurachenko <srebrov@altlinux.org> 0.9.0-alt1
- New version 0.9.0.

* Sun Apr 12 2026 Anton Kurachenko <srebrov@altlinux.org> 0.8.7-alt1
- New version 0.8.7.

* Thu Dec 18 2025 Anton Kurachenko <srebrov@altlinux.org> 0.8.6-alt1
- New version 0.8.6.

* Mon Sep 29 2025 Anton Kurachenko <srebrov@altlinux.org> 0.8.5-alt1
- New version 0.8.5.

* Sat Aug 23 2025 Anton Kurachenko <srebrov@altlinux.org> 0.8.1-alt1
- Initial build for ALT.
