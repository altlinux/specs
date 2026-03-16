%define nameU org.kde.klevernotes

Name: klevernotes
Version: 1.2.5
Release: alt2

Summary: KleverNotes is a note taking and management application
License: GPL-2.0-or-later
Group: Graphical desktop/KDE

Packager: Aleksandr Shamaraev <shad@altlinux.org>

URL: https://invent.kde.org/office/klevernotes
Vcs: https://invent.kde.org/office/klevernotes

Source0: %name-%version.tar
Source1: ru.tar

ExclusiveArch: x86_64 aarch64 loongarch64

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: cmake qt6-base-devel extra-cmake-modules qt6-base-devel qt6-declarative-devel libqt6-quickcontrols2 qt6-webengine-devel 
BuildRequires: qt6-svg-devel kf6-kirigami-devel kf6-kirigami-addons-devel kf6-kcoreaddons-devel kf6-kconfig-devel kf6-ki18n-devel 
BuildRequires: kf6-kconfigwidgets-devel kf6-kio-devel libgomp13-devel kf6-kiconthemes-devel

# These deps are required, but are not autodetected:
Requires: kf6-kirigami kf6-kirigami-addons
Requires: kf6-qqc2-desktop-style libkf6sonnetcore

%description
KleverNotes is a note taking and management application for your mobile and desktop devices. It uses markdown and allow you to preview your content.

%prep
%setup

tar -xf %SOURCE1 -C po/

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_datadir/applications/%nameU.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/locale/*/LC_MESSAGES/%name.mo
%_datadir/metainfo/%nameU.metainfo.xml
%doc *.md 

%changelog
* Tue Mar 17 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.2.5-alt2
- added required dependencies

* Thu Oct 30 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.2.5-alt1
- 1.2.4 -> 1.2.5

* Wed Sep 24 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.2.4-alt1
- 1.2.3 -> 1.2.4

* Wed Sep 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.2.3-alt2
- update to git.8cf319e9

* Sat Aug 30 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.2.3-alt1
- 1.2.2 -> 1.2.3 (git.dc88e95b)

* Fri Apr 04 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.2.2-alt2
- Created and added russian translate.

* Tue Mar 25 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.2.2-alt1
- 1.2.1 -> 1.2.2

* Fri Mar 21 2025 Ivan A. Melnikov <iv@altlinux.org> 1.2.1-alt1.1
- NMU:
  + and missing kf6-kirigami dependencies
  + build on loongarch64

* Thu Mar 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.2.1-alt1
- 1.2.0 -> 1.2.1

* Tue Mar 18 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.2.0-alt1
- 1.2.0

* Sun Nov 24 2024 Aleksandr Shamaraev <shad@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
