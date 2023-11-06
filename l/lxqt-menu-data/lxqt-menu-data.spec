Name: lxqt-menu-data
Version: 1.4.0
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
BuildRequires: qt5-tools-devel
BuildRequires: lxqt-build-tools >= 0.12.0

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
* Sun Nov 05 2023 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- initia build
