# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-clip
Version: 2.5.0
Release: alt1

Summary: Lightweight clipboard history applet by LXQt for X11 and Wayland
License: LGPL-2.1-or-later
Group: Graphical desktop/Other

URL: https://lxqt-project.org/
VCS: https://github.com/lxqt/lxqt-clip

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Replace for lxqt metapackage
Obsoletes: qlipper <= 6.1.0-alt1

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: liblxqt-devel
BuildRequires: qt6-tools-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kguiaddons-devel

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang --with-qt %name

%files -f %name.lang
%_sysconfdir/xdg/autostart/lxqt-clip-autostart.desktop
%_bindir/lxqt-clip
%_desktopdir/lxqt-clip.desktop
%_iconsdir/hicolor/128x128/apps/lxqt-clip.png
%dir %_datadir/lxqt/translations/lxqt-clip/

%changelog
* Fri Nov 20 2026 Anton Midyukov <antohami@altlinux.org> 2.5.0-alt1
- Initial build.
