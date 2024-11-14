# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-wayland-session
Summary: Files needed for the LXQt Wayland Session
Version: 0.1.0
Release: alt1
License: LGPL-2.1 and MIT and BSD-3-Clause and GPL-3.0 and GPL-2.0
Group: Graphical desktop/Other
Url: https://github.com/lxqt/lxqt-wayland-session
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: liblxqt-devel
BuildRequires: qt6-tools-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: xdg-user-dirs

Requires: lxqt-session >= 2.1.0
Requires: lxqt-themes
Requires: openbox-theme-Vent
Requires: labwc-base
Requires: xorg-xwayland
Requires: qt6-wayland
%add_findreq_skiplist %_datadir/lxqt/wayland/lxqt-river-init

%description
Files needed for the LXQt Wayland Session: Wayland session start script, its
desktop entry for display managers and default configurations for actually
supported compositors.

%package -n openbox-theme-Vent
Summary: A Openbox (labwc) theme engine - Vent
Summary(ru_RU.UTF-8): Тема для Openbox (labwc) - Vent
Group: Graphical desktop/Other
BuildArch: noarch

%description -n openbox-theme-Vent
This package contains the Openbox (labwc) theme engine named Vent.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE* README.md
%_bindir/startlxqtwayland
%_datadir/lxqt/graphics/lxqt-labwc.png
%_datadir/lxqt/wallpapers/origami-dark-labwc.png
%_datadir/lxqt/wayland/
%_datadir/wayland-sessions/lxqt-wayland.desktop

%files -n openbox-theme-Vent
%_datadir/themes/Vent/
%_datadir/themes/Vent-dark/

%changelog
* Thu Nov 14 2024 Anton Midyukov <antohami@altlinux.org> 0.1.0-alt1
- initial build
