%define _unpackaged_files_terminate_build 1

Name: kontrast
Version: 26.04.2
Release: alt1

Summary: Contrast inspection tool for Plasma and Plasma Mobile
License: GPL-3.0-only AND GPL-3.0-or-later AND CC-BY-SA-4.0
Group: Graphical desktop/KDE
Url: https://apps.kde.org/kontrast
VCS: https://invent.kde.org/accessibility/kontrast

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: futuresql-qt6-devel
BuildRequires: qcoro6-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-kcrash-devel

Requires: kf6-kconfig
Requires: kf6-kirigami
Requires: kf6-kirigami-addons
Requires: libqt6-quick
Requires: libqt6-quickcontrols2
Requires: libqt6-quicklayouts
Requires: libqt6-qml

%description
Tool to check contrast for colors that allows verifying that your colors
are correctly accessible.

%prep
%setup
sed -i "s|Categories=.*|Categories=Qt;KDE;Utility;Accessibility;|" org.kde.kontrast.desktop

%build
%K6build

%install
%K6install

%find_lang %name --with-kde

%files -f %name.lang
%doc README.md
%_bindir/kontrast
%_desktopdir/org.kde.kontrast.desktop
%_iconsdir/hicolor/scalable/apps/org.kde.kontrast.svg
%_datadir/metainfo/org.kde.kontrast.appdata.xml

%changelog
* Fri Jun 05 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.2-alt1
- New version 26.04.2.

* Thu May 07 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.1-alt1
- New version 26.04.1.

* Fri Apr 17 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.0-alt1
- New version 26.04.0.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.3-alt1
- New version 25.12.3.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.2-alt1
- New version 25.12.2.

* Thu Jan 15 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.1-alt1
- Initial build for Sisyphus
