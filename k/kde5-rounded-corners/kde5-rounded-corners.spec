Name: kde5-rounded-corners
Version: 0.6.7
Release: alt1
%K5init no_altplace

Group: Graphical desktop/KDE
Summary: Rounds the corners of your windows in KDE Plasma
URL: https://github.com/matinlotfali/KDE-Rounded-Corners
License: GPL-3.0-only

Source: %name-%version.tar
Patch: %name-%version-alt-no-use-kf6-and-qt6.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: plasma5-kwin-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kwindowsystem-devel

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%K5build

%install
%K5install

%files
%doc LICENSE README.*
%_K5data/kwin/shaders/shapecorners*.frag
%_K5plug/kwin/effects/configs/kwin_shapecorners_config.so
%_K5plug/kwin/effects/plugins/kwin4_effect_shapecorners.so

%changelog
* Thu Jul 4 2024 Anton Kurachenko <srebrov@altlinux.org> 0.6.7-alt1
- Initial build for Sisyphus.
