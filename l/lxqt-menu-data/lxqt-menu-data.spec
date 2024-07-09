Name: lxqt-menu-data
Version: 2.0.0
Release: alt1

Summary: Freedesktop.org application menu definition files
License: LGPL-2.1-or-later
Group: Graphical desktop/Other

Url: https://github.com/lxqt/lxqt-menu-data
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-xdg
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-tools-devel
BuildRequires: lxqt2-build-tools

BuildArch: noarch

Obsoletes: lxde-lxmenu-data

%description
Replacement for lxmenu-data (LXDE). Provides the translations for menu
categories. Runtime dependency for lxqt-panel and pcmanfm-qt.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Development files for %name.

%prep
%setup
%autopatch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%_datadir/desktop-directories/lxqt-*.directory
%_xdgconfigdir/menus/*.menu

%files devel
%_datadir/cmake/%name

%changelog
* Wed Jun 12 2024 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- new version 2.0.0

* Fri Nov 10 2023 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt1
- new version 1.4.1

* Sun Nov 05 2023 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- initia build
