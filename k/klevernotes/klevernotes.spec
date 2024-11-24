%define nameU org.kde.klevernotes

Name: klevernotes
Version: 1.1.0
Release: alt1

Summary: KleverNotes is a note taking and management application
License: GPL-2.0-or-later
Group: Graphical desktop/KDE

URL: https://invent.kde.org/office/klevernotes
Vcs: https://invent.kde.org/office/klevernotes

Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: cmake qt6-base-devel extra-cmake-modules qt6-base-devel qt6-declarative-devel libqt6-quickcontrols2 qt6-webengine-devel 
BuildRequires: qt6-svg-devel kf6-kirigami-devel kf6-kirigami-addons-devel kf6-kcoreaddons-devel kf6-kconfig-devel kf6-ki18n-devel kf6-kconfigwidgets-devel kf6-kio-devel libgomp13-devel

%description
KleverNotes is a note taking and management application for your mobile and desktop devices. It uses markdown and allow you to preview your content.

%prep
%setup

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
* Sun Nov 24 2024 Aleksandr Shamaraev <shad@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
