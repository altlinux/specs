%define nameL org.kde.isoimagewriter

Name: isoimagewriter
Version: 25.08.0
Release: alt1

Summary: Program to write hybrid ISO files onto USB disks
License: GPL-3.0-or-later
Group: Graphical desktop/KDE

Url: https://apps.kde.org/ru/isoimagewriter
Vcs: https://invent.kde.org/utilities/isoimagewriter

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules
BuildRequires: kf6-ki18n-devel kf6-kcoreaddons-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kiconthemes-devel kf6-karchive-devel kf6-kcrash-devel
BuildRequires: kf6-solid-devel

%description
%summary

%prep
%setup

%build
%K6cmake
%K6make

%install
%K6install

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc *.md LICENSES
%_bindir/%name
%_datadir/applications/%nameL.desktop
%_iconsdir/hicolor/*/apps/%nameL.svg
%_datadir/%name
%_datadir/metainfo/%nameL.appdata.xml

%changelog
* Fri Aug 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.08.0-alt1
- 25.04.3 -> 25.08.0

* Fri Jul 04 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.04.3-alt1
- 25.04.2 -> 25.04.3

* Fri Jun 06 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.04.2-alt1
- 25.04.1 -> 25.04.2

* Thu May 29 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.04.1-alt1
- Initial build for ALT Linux.
