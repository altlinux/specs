%def_with qt5
%def_with qt6

Name: qadwaitadecorations
Version: 0.1.5
Release: alt1
Summary: Qt decoration plugin implementing Adwaita-like client-side decorations
Group: Graphical desktop/GNOME
License: LGPL-2.1-or-later
URL: https://github.com/FedoraQt/QAdwaitaDecorations

# Source-url: https://github.com/FedoraQt/QAdwaitaDecorations/archive/%version/QAdwaitaDecorations-%version.tar.gz
Source: QAdwaitaDecorations-%version.tar
# https://github.com/FedoraQt/QAdwaitaDecorations/commit/f40f31dadc074bd989db6dd90e52eecf33c4567b.patch
Patch: f40f31da.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  wayland-devel

%description
%summary.

%if_with qt5
%package qt5
Summary: Qt decoration plugin implementing Adwaita-like client-side decorations
Group: Graphical desktop/GNOME
BuildRequires: qt5-base-devel >= 5.15.2
BuildRequires: qt5-base-devel-static >= 5.15.2
BuildRequires: qt5-wayland-devel >= 5.15.2
BuildRequires: qt5-svg-devel >= 5.15.2

%description qt5
%summary.
%endif

%if_with qt6
%package qt6
Summary: Qt decoration plugin implementing Adwaita-like client-side decorations
Group: Graphical desktop/GNOME
BuildRequires: qt6-base-devel >= 6.5.0
BuildRequires: qt6-base-devel-static >= 6.5.0
BuildRequires: qt6-wayland-devel >= 6.5.0
BuildRequires: qt6-svg-devel >= 6.5.0

%description qt6
%summary.
%endif

%prep
%setup -n QAdwaitaDecorations-%version
%patch -p1

%build
%if_with qt5
%define _cmake__builddir %_target_platform-qt5
%cmake -DUSE_QT6=false
%cmake_build
%endif

%if_with qt6
%define _cmake__builddir %_target_platform-qt6
%cmake -DUSE_QT6=true
%cmake_build
%endif

%install
%if_with qt5
%define _cmake__builddir %_target_platform-qt5
%cmake_install
%endif

%if_with qt6
%define _cmake__builddir %_target_platform-qt6
%cmake_install
%endif

%if_with qt5
%files qt5
%doc README.md LICENSE
%_qt5_plugindir/wayland-decoration-client/libqadwaitadecorations.so
%endif

%if_with qt6
%files qt6
%doc README.md LICENSE
%_qt6_plugindir/wayland-decoration-client/libqadwaitadecorations.so
%endif

%changelog
* Mon Sep 30 2024 Anton Midyukov <antohami@altlinux.org> 0.1.5-alt1
- Initial build
