%define nameL com.georgefb.mangareader

Name: mangareader
Version: 2.5.1
Release: alt1

Summary: Qt manga reader for local files
License: GPL-3.0-only and CC-BY-SA-4.0 and BSD-2-Clause and CC0-1.0
Group: Office

Url: https://github.com/g-fb/mangareader
Vcs: https://github.com/g-fb/mangareader

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules gcc-c++
BuildRequires: qt6-base-devel kf6-karchive-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kio-devel kf6-kxmlgui-devel pkgconfig(Qt6Qml)

%description
A manga reader for local files. Works with folders and archives.

%prep
%setup

%build
%K6cmake
%K6make

%install
%K6install
cd %buildroot%_datadir/config.kcfg/
mv settings.kcfg %name.kcfg

%files
%doc *.md LICENSES
%_bindir/%name
%_datadir/applications/%nameL.desktop
%_datadir/config.kcfg/%name.kcfg
%_iconsdir/hicolor/*/apps/*
%_datadir/kxmlgui5/%name/*.rc
%_datadir/metainfo/%nameL.metainfo.xml

%changelog
* Sun May 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.5.1-alt1
- 2.5.0 -> 2.5.1

* Sun May 17 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.5.0-alt1
- 2.4.0 -> 2.5.0
- changed license

* Fri Apr 10 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.4.0-alt1
- 2.3.0 -> 2.4.0

* Sun Feb 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.3.0-alt1
- 2.2.2 -> 2.3.0

* Tue May 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.2.2-alt1
- 2.2.1 -> 2.2.2

* Sat May 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.2.1-alt1
- Initial build for ALT Linux.
