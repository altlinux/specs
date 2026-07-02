# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-wayland-session
Summary: Files needed for the LXQt Wayland Session
Version: 0.4.1
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
%filter_from_requires /^hyprland/d

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
%_bindir/lxqt-qdbus
%_datadir/lxqt/graphics/lxqt-labwc.png
%_datadir/lxqt/wallpapers/origami-dark-labwc.png
%_datadir/lxqt/wayland/
%_datadir/wayland-sessions/lxqt-wayland.desktop
%_man1dir/startlxqtwayland.1.*
%_man1dir/lxqt-wayland-session.1.*

%files -n openbox-theme-Vent
%_datadir/themes/Vent/
%_datadir/themes/Vent-dark/

%changelog
* Thu Jul 02 2026 Anton Midyukov <antohami@altlinux.org> 0.4.1-alt1
- New version 0.4.1.

* Mon Apr 20 2026 Anton Midyukov <antohami@altlinux.org> 0.4.0-alt1
- New version 0.4.0.

* Thu Mar 05 2026 Anton Midyukov <antohami@altlinux.org> 0.3.2-alt1
- New version 0.3.2.

* Mon Dec 22 2025 Anton Midyukov <antohami@altlinux.org> 0.3.1-alt1
- New version 0.3.1.

* Wed Nov 05 2025 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Wed Jul 30 2025 Anton Midyukov <antohami@altlinux.org> 0.2.1-alt1
- New version 0.2.1.

* Fri Jul 18 2025 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt2
- add upstream patches:
  + Updated sway config to 1.11
  + Updated Labwc conf to 0.9

* Thu Apr 17 2025 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt1
- New version 0.2.0.

* Wed Jan 22 2025 Anton Midyukov <antohami@altlinux.org> 0.1.1-alt2
- new snapshot (20250114)

* Tue Nov 26 2024 Anton Midyukov <antohami@altlinux.org> 0.1.1-alt1
- New version 0.1.1.

* Thu Nov 14 2024 Anton Midyukov <antohami@altlinux.org> 0.1.0-alt1
- initial build
