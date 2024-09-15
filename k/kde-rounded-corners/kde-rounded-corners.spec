%define _unpackaged_files_terminate_build 1

Name: kde-rounded-corners
Version: 0.6.7
Release: alt2
%K6init no_altplace

Group: Graphical desktop/KDE
Summary: Rounds the corners of your windows in KDE Plasma
URL: https://github.com/matinlotfali/KDE-Rounded-Corners
License: GPL-3.0-only

Provides: kde5-rounded-corners = %EVR
Obsoletes: kde5-rounded-corners < %EVR

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: kwin-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kcmutils-devel
BuildRequires: qt6-declarative-devel

%description
%summary.

%prep
%setup

%build
%K6build

%install
%K6install

%files
%doc LICENSE README.*
%_K6data/kwin/shaders/shapecorners*.frag
%_K6plug/kwin/effects/configs/kwin_shapecorners_config.so
%_K6plug/kwin/effects/plugins/kwin4_effect_shapecorners.so

%changelog
* Sun Sep 15 2024 Anton Kurachenko <srebrov@altlinux.org> 0.6.7-alt2
- Build for KF6.

* Thu Jul 4 2024 Anton Kurachenko <srebrov@altlinux.org> 0.6.7-alt1
- Initial build for Sisyphus.
