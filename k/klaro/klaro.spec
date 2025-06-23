%define _unpackaged_files_terminate_build 1
%define app_id io.github.denysmb.klaro

Name: klaro
Version: 1.0.1
Release: alt2

Summary: Simple and fast translation app for KDE Plasma
License: GPL-3.0-or-later
Group: Text tools
Url: https://github.com/DenysMb/Klaro
Vcs: https://github.com/DenysMb/Klaro

Source: %name-%version.tar

Requires: kf6-kirigami
Requires: kf6-kirigami-addons
Requires: kf6-qqc2-desktop-style
Requires: libkf6sonnetui
Requires: translate-shell

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel
BuildRequires: kf6-kirigami-devel kf6-kirigami
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-qqc2-desktop-style-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: libvulkan-devel


%description
A simple and fast translation app for KDE Plasma that helps you translate
text between different languages.

%prep
%setup

%build
%K6build

%install
%K6install

%find_lang --with-kde %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/metainfo/%app_id.metainfo.xml
%doc README.md

%changelog
* Mon Jun 23 2025 Semen Fomchenkov <armatik@altlinux.org> 1.0.1-alt2
- Add translate-shell to runtime requires.

* Tue Jun 10 2025 Semen Fomchenkov <armatik@altlinux.org> 1.0.1-alt1
- Initial build.
