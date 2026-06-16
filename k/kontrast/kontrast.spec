%define rname kontrast

Name: %rname
Version: 26.04.2
Release: alt2

Group: Graphical desktop/KDE
Summary: Contrast inspection tool for Plasma and Plasma Mobile
License: GPL-3.0-only AND GPL-3.0-or-later AND CC-BY-SA-4.0
Url: https://apps.kde.org/kontrast
VCS: https://invent.kde.org/accessibility/kontrast

Requires: qt6-declarative
Requires: kf6-kconfig
Requires: kf6-kirigami
Requires: kf6-kirigami-addons

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
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

%description
Tool to check contrast for colors that allows verifying that your colors
are correctly accessible.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install

%find_lang %name --with-kde

%files -f %name.lang
%doc README.md
%_K6bin/kontrast
%_K6xdgapp/*kontrast*.desktop
%_K6icon/hicolor/*/apps/*kontrast*
%_datadir/metainfo/*kontrast*

%changelog
* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt2
- update packaging

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
