%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: kaichat-addons
Version: 0.0.0
Release: alt3_git20260610

Summary: Addons for KAIChat
License: CC0-1.0 AND MIT AND GPL-2.0-or-later AND BSD-3-Clause
Group: Graphical desktop/KDE
Url: https://invent.kde.org/utilities/kaichat-addons

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules

BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)

BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-ktextaddons-devel >= 1.9.0
BuildRequires: kweathercore-devel
BuildRequires: reuse

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K6lib/qt6/plugins/autogeneratetext/toolplugins/textautogeneratetext_weathertoolplugin.so
%_K6lib/qt6/plugins/autogeneratetext/toolplugins/textautogeneratetext_wikipediatoolplugin.so
%_K6data/qlogging-categories6/kaichat-addons.categories

%changelog
* Thu Jun 11 2026 Nikolay Strelkov <snk@altlinux.org> 0.0.0-alt3_git20260610
- Updated to newer commit e3b947cc.

* Fri May 22 2026 Nikolay Strelkov <snk@altlinux.org> 0.0.0-alt2_git20260204
- Enable build on riscv64 and loongarch64.

* Wed Feb 04 2026 Nikolay Strelkov <snk@altlinux.org> 0.0.0-alt1_git20260204
- Initial build for Sisyphus
